#!/usr/bin/env python3
"""
Build the public rulebook page from rulebook.md.

Usage:  python3 build_rulebook.py rulebook.md rulebook/index.html

Gives every clause a stable id so it can be linked to and cited:
    rootwall.ai/rulebook#22.3
"""

import re
import sys
import os
import html
import markdown

CSS = """
:root {
  --ink:#17171a; --ink-soft:#4a4a52; --ink-faint:#74747e;
  --paper:#fbfaf8; --panel:#f2f0ec; --rule:#dcd9d2; --accent:#7a2f1e;
  --measure:46rem;
}
@media (prefers-color-scheme: dark) {
  :root {
    --ink:#e8e6e1; --ink-soft:#b2afa8; --ink-faint:#86837c;
    --paper:#16161a; --panel:#1e1e23; --rule:#33333a; --accent:#d98b72;
  }
}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%; scroll-behavior:smooth}
body{
  margin:0;background:var(--paper);color:var(--ink);
  font-family:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;
}
.sans{font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}

/* top bar */
.topbar{border-bottom:1px solid var(--rule);background:var(--paper)}
.topbar .inner{
  max-width:var(--measure);margin:0 auto;padding:1rem 1.5rem;
  display:flex;justify-content:space-between;align-items:baseline;gap:1rem;
}
.topbar a.home{
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.9rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;
  color:var(--ink);text-decoration:none;
}
.topbar .doc{
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint);
}

.wrap{max-width:var(--measure);margin:0 auto;padding:3rem 1.5rem 6rem}

h1{
  font-size:1.5rem;line-height:1.3;font-weight:600;letter-spacing:-.008em;
  margin:3.5rem 0 1.25rem;padding-bottom:.6rem;border-bottom:2px solid var(--ink);
}
h1:first-of-type{margin-top:0}
h2{font-size:1.14rem;line-height:1.35;font-weight:650;margin:2.75rem 0 1rem}
h3{font-size:1rem;font-weight:650;margin:1.5rem 0 .75rem}
p{margin:0 0 1rem}
strong{font-weight:650;color:var(--ink)}
em{font-style:italic}
a{color:var(--accent)}
hr{border:0;border-top:1px solid var(--rule);margin:3rem 0}

ul,ol{padding-left:1.4rem;margin:0 0 1rem}
li{margin-bottom:.5rem}

/* lettered sub-items inside a clause */
p.sub{
  margin-left:1.6rem;margin-bottom:.55rem;text-indent:-1.6rem;
  padding-left:0;color:var(--ink-soft);
}
p.sub strong{color:var(--ink)}

/* clause anchors */
.clause{position:relative}
.cnum{font-weight:650;color:var(--ink)}
a.anchor{
  text-decoration:none;color:var(--ink-faint);opacity:0;
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.78rem;margin-left:.45rem;vertical-align:.08em;
  transition:opacity .12s ease;
}
.clause:hover a.anchor,h1:hover a.anchor,h2:hover a.anchor,a.anchor:focus{opacity:1}
:target{background:var(--panel);outline:none}
:target{scroll-margin-top:1.5rem}
h1:target,h2:target,p:target{
  box-shadow:-.8rem 0 0 var(--panel),.8rem 0 0 var(--panel);
}

/* tables */
.tablewrap{overflow-x:auto;margin:0 0 1.5rem;border:1px solid var(--rule)}
table{border-collapse:collapse;width:100%;font-size:.88rem;line-height:1.45}
th,td{text-align:left;vertical-align:top;padding:.6rem .75rem;border-bottom:1px solid var(--rule)}
th{
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;
  color:var(--ink-faint);font-weight:650;background:var(--panel);
}
tr:last-child td{border-bottom:0}

/* blockquote */
blockquote{
  margin:1.5rem 0;padding:1.1rem 1.3rem;background:var(--panel);
  border-left:2px solid var(--accent);
}
blockquote > :last-child{margin-bottom:0}
blockquote h3{margin-top:0;font-size:.88rem;letter-spacing:.04em;text-transform:uppercase}

/* contents */
details.toc{
  border:1px solid var(--rule);background:var(--panel);
  padding:1rem 1.3rem;margin:0 0 3rem;
}
details.toc summary{
  cursor:pointer;font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.76rem;font-weight:650;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-faint);
}
details.toc ol{list-style:none;padding:0;margin:1.1rem 0 .25rem;
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:.86rem}
details.toc li{margin-bottom:.3rem}
details.toc li.part{margin-top:.95rem;font-weight:650}
details.toc li.part:first-child{margin-top:0}
details.toc a{text-decoration:none;color:var(--ink-soft)}
details.toc a:hover{color:var(--accent)}
details.toc li.part a{color:var(--ink)}

footer{
  margin-top:4rem;padding-top:1.4rem;border-top:1px solid var(--rule);
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.78rem;line-height:1.7;color:var(--ink-faint);
}
footer p{margin:0 0 .35rem}

@media (max-width:34rem){
  body{font-size:16px}
  .wrap{padding:2rem 1.15rem 4rem}
  h1{font-size:1.3rem}
  p.sub{margin-left:1.2rem;text-indent:-1.2rem}
}
"""

PAGE = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Rootwall Scheme Rulebook</title>
<meta name="description" content="The full text of the Rootwall Scheme Rulebook. Admission, delegation, evidence, breach and consequence. Every clause separately linkable.">
<style>{css}</style>
</head>
<body>
<div class="topbar"><div class="inner">
  <a class="home" href="/">Rootwall</a>
  <span class="doc">Scheme Rulebook</span>
</div></div>
<div class="wrap">
{toc}
{body}
<footer>
  <p>Every clause on this page has its own address. To cite one, use the link beside its number &mdash; for example <code>rootwall.ai/rulebook#22.3</code>. Numbering is stable: clauses removed in a later version are marked <em>[Reserved]</em> and their numbers are never reused.</p>
  <p>Contact: <a href="mailto:info@rootwall.ai">info@rootwall.ai</a> &middot; <a href="/privacy">Privacy</a></p>
</footer>
</div>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "df6516715bb74e70ab48c22f8c1de1ec"}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""

SUB_RE = re.compile(r'^ {2}\(([a-z0-9]+)\)\s+(.*)$')
CONT_RE = re.compile(r'^ {6,}\S')


def preprocess(md_text):
    """Turn 2-space-indented "(a) ..." sub-items into standalone paragraphs.

    Markdown would otherwise glue them into one run-on paragraph, because the
    source is hard-wrapped and the items are not separated by blank lines.
    """
    lines = md_text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        m = SUB_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        parts = ['({}) {}'.format(m.group(1), m.group(2).strip())]
        i += 1
        while i < len(lines) and CONT_RE.match(lines[i]):
            parts.append(lines[i].strip())
            i += 1
        if out and out[-1].strip() != '':
            out.append('')
        out.append(' '.join(parts))
        out.append('')
    return '\n'.join(out)


def anchor(target):
    return ('<a class="anchor" href="#{t}" aria-label="Link to {t}" '
            'title="Link to {t}">#</a>').format(t=html.escape(target, quote=True))


def add_ids(body):
    """Give every clause and heading a stable, citable id."""
    counts = {'clause': 0, 'section': 0}

    # Clauses: <p><strong>22.3A</strong> text...
    def clause(m):
        num = m.group(1)
        counts['clause'] += 1
        return ('<p class="clause" id="{n}"><span class="cnum">{n}</span>{a} '
                .format(n=num, a=anchor(num)))
    body = re.sub(r'<p><strong>(\d{1,2}\.\d{1,2}[A-Z]?)</strong>\s*', clause, body)

    # Numbered sections: <h2>22. Retention</h2>
    def section(m):
        num, rest = m.group(1), m.group(2)
        counts['section'] += 1
        return '<h2 id="{n}">{n}. {r}{a}</h2>'.format(n=num, r=rest, a=anchor(num))
    body = re.sub(r'<h2>(\d{1,2})\.\s+(.*?)</h2>', section, body)

    # Schedules: <h2>Schedule 1 — Standing</h2>
    def schedule(m):
        n, rest = m.group(1), m.group(2)
        sid = 'schedule-' + n
        return '<h2 id="{i}">Schedule {n}{r}{a}</h2>'.format(
            i=sid, n=n, r=rest, a=anchor(sid))
    body = re.sub(r'<h2>Schedule (\d)(.*?)</h2>', schedule, body)

    # Parts: <h1>Part 1 — The Scheme</h1>
    def part(m):
        n, rest = m.group(1), m.group(2)
        pid = 'part-' + n
        return '<h1 id="{i}">Part {n}{r}{a}</h1>'.format(i=pid, n=n, r=rest, a=anchor(pid))
    body = re.sub(r'<h1>Part (\d)(.*?)</h1>', part, body)

    # Remaining headings get slug ids so the contents can reach them.
    def slugged(m):
        level, text = m.group(1), m.group(2)
        slug = re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', text).lower()).strip('-')
        slug = slug[:48].strip('-')
        return '<h{l} id="{i}">{t}{a}</h{l}>'.format(l=level, i=slug, t=text, a=anchor(slug))
    body = re.sub(r'<h([12])>(.*?)</h[12]>', slugged, body)

    # Lettered sub-items
    body = re.sub(r'<p>(\([a-z0-9]+\)\s)', r'<p class="sub">\1', body)

    # Tables need a scroll container of their own
    body = body.replace('<table>', '<div class="tablewrap"><table>')
    body = body.replace('</table>', '</table></div>')

    return body, counts


def build_toc(body):
    items = []
    for m in re.finditer(r'<h([12]) id="([^"]+)">(.*?)(?:<a class="anchor".*?</a>)?</h[12]>',
                         body, re.S):
        level, hid, text = m.group(1), m.group(2), m.group(3)
        text = re.sub(r'<[^>]+>', '', text).strip()
        if not text:
            continue
        cls = 'part' if level == '1' else ''
        items.append('<li class="{c}"><a href="#{i}">{t}</a></li>'.format(
            c=cls, i=html.escape(hid, quote=True), t=html.escape(text)))
    return ('<details class="toc"><summary>Contents</summary>\n<ol>\n'
            + '\n'.join(items) + '\n</ol>\n</details>')


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else 'rulebook.md'
    dest = sys.argv[2] if len(sys.argv) > 2 else os.path.join('rulebook', 'index.html')

    with open(src, encoding='utf-8') as fh:
        md_text = fh.read()

    body = markdown.markdown(
        preprocess(md_text),
        extensions=['tables', 'sane_lists', 'md_in_html'],
        output_format='html5',
    )
    body, counts = add_ids(body)
    toc = build_toc(body)

    os.makedirs(os.path.dirname(dest) or '.', exist_ok=True)
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write(PAGE.format(css=CSS, toc=toc, body=body))

    print('wrote {}  ({} clauses, {} numbered sections anchored)'.format(
        dest, counts['clause'], counts['section']))


if __name__ == '__main__':
    main()
