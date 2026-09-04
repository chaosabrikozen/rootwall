#!/usr/bin/env python3
"""
Build the published survey page from the note's public edition.

Usage:  python3 build_note.py rootwall_hundred_platform_note_public_edition_v1_0.md hundred-platforms/index.html

Reuses the rulebook's stylesheet, so the two documents are visibly the same
publication rather than two websites.

Gives every numbered point a stable id so it can be linked to and cited:
    rootwall.ai/hundred-platforms#p63
"""

import re
import sys
import os
import html
import markdown

from build_rulebook import CSS

EXTRA_CSS = """
/* the survey's numbered points, given their own addresses */
ol.points{list-style:none;padding-left:0;counter-reset:none}
ol.points > li{
  position:relative;padding-left:2.6rem;margin-bottom:1rem;
}
ol.points > li > .pnum{
  position:absolute;left:0;top:0;width:2.1rem;text-align:right;
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.82rem;font-weight:650;color:var(--ink-faint);
  padding-top:.22em;
}
ol.points > li:target{background:var(--panel);box-shadow:-.8rem 0 0 var(--panel),.8rem 0 0 var(--panel)}
ol.points > li:target > .pnum{color:var(--accent)}
ol.points > li:hover a.anchor{opacity:1}
ol.points ul{margin-top:.6rem}
.standfirst{
  font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.95rem;line-height:1.6;color:var(--ink-soft);
  margin:0 0 2rem;padding-bottom:1.5rem;border-bottom:1px solid var(--rule);
}
.standfirst strong{color:var(--ink)}
"""

PAGE = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>What a hundred UK and EU software platforms require of the third parties calling their APIs</title>
<meta name="description" content="A survey of roughly one hundred UK and EU software platforms, read on 28 August 2026. Seven publish a partner rulebook. None holds a record of what a third party actually did. Every document quoted is linked and archived.">
<meta property="og:title" content="What a hundred UK and EU software platforms require of the third parties calling their APIs">
<meta property="og:description" content="Seven of a hundred platforms publish partner rules. None holds a record of what a third party actually did. Surveyed 28 August 2026, every document archived.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://rootwall.ai/hundred-platforms">
<link rel="canonical" href="https://rootwall.ai/hundred-platforms">
<style>{css}</style>
</head>
<body>
<div class="topbar"><div class="inner">
  <a class="home" href="/">Rootwall</a>
  <span class="doc">The survey &middot; version 1.0</span>
</div></div>
<div class="wrap">
{toc}
{body}
<footer>
  <p>Every numbered point on this page has its own address. To cite one, use the link beside its number &mdash; for example <code>rootwall.ai/hundred-platforms#p63</code>.</p>
  <p><a href="/">Front page</a> &middot; <a href="/rulebook">The rulebook</a> &middot; <a href="/scope-class">Example class</a> &middot; <a href="/questions">Common questions</a> &middot; <a href="/fees">Schedule of fees</a> &middot; <a href="/history">Version history</a> &middot; <a href="/disputes">Disputes</a> &middot; <a href="/privacy">Privacy</a></p>
  <p>Corrections, and anything else in this note: <a href="mailto:info@rootwall.ai">info@rootwall.ai</a></p>
</footer>
</div>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "df6516715bb74e70ab48c22f8c1de1ec"}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""


def anchor(target):
    return ('<a class="anchor" href="#{t}" aria-label="Link to point {n}" '
            'title="Link to point {n}">#</a>').format(
                t=html.escape(target, quote=True), n=target.lstrip('p'))


def number_points(body):
    """Give every top-level ordered-list item a stable id (p1, p2, ...).

    The note is one continuous run of numbered points broken across sections,
    so the numbers in the markdown are authoritative and must not be recomputed
    by the browser. Nested lists inside a point are left alone.
    """
    out = []
    i = 0
    depth = 0          # nesting depth of ol/ul
    counter = [0]      # current number inside the top-level ol
    n_points = 0
    token = re.compile(r'<(/?)(ol|ul|li)\b[^>]*>')
    while i < len(body):
        m = token.search(body, i)
        if not m:
            out.append(body[i:])
            break
        out.append(body[i:m.start()])
        tag, closing, name = m.group(0), m.group(1), m.group(2)
        if name in ('ol', 'ul'):
            if not closing:
                depth += 1
                if depth == 1 and name == 'ol':
                    start = re.search(r'start="(\d+)"', tag)
                    counter[0] = int(start.group(1)) if start else 1
                    tag = '<ol class="points">'
            else:
                depth -= 1
        elif name == 'li' and not closing and depth == 1:
            pid = 'p{}'.format(counter[0])
            tag = '<li id="{i}"><span class="pnum">{n}</span>{a}'.format(
                i=pid, n=counter[0], a=anchor(pid))
            counter[0] += 1
            n_points += 1
        out.append(tag)
        i = m.end()
    return ''.join(out), n_points


def add_ids(body):
    """Section headings get citable ids, tables get a scroll container."""
    def slugged(m):
        level, text = m.group(1), m.group(2)
        plain = re.sub(r'<[^>]+>', '', text)
        slug = re.sub(r'[^a-z0-9]+', '-', plain.lower()).strip('-')[:48].strip('-')
        return '<h{l} id="{i}">{t}<a class="anchor" href="#{i}">#</a></h{l}>'.format(
            l=level, i=slug, t=text)
    body = re.sub(r'<h([123])>(.*?)</h[123]>', slugged, body, flags=re.S)
    body = body.replace('<table>', '<div class="tablewrap"><table>')
    body = body.replace('</table>', '</table></div>')
    return body


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


def split_standfirst(md_text):
    """The title and the metadata block above the first rule become the masthead."""
    head, rest = md_text.split('\n---\n', 1)
    title = re.search(r'^#\s+(.*)$', head, re.M).group(1).strip()
    meta = head.split('\n', 1)[1].strip()
    return title, meta, rest


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else \
        'rootwall_hundred_platform_note_public_edition_v1_0.md'
    dest = sys.argv[2] if len(sys.argv) > 2 else os.path.join('hundred-platforms', 'index.html')

    with open(src, encoding='utf-8') as fh:
        md_text = fh.read()

    title, meta, rest = split_standfirst(md_text)

    head_html = '<h1 id="top">{}</h1>\n<div class="standfirst">{}</div>'.format(
        html.escape(title),
        markdown.markdown(meta, output_format='html5'))

    body = markdown.markdown(
        rest,
        extensions=['tables', 'sane_lists'],
        output_format='html5',
    )
    body, n_points = number_points(body)
    body = add_ids(body)
    body = head_html + '\n' + body

    toc = build_toc(body)

    os.makedirs(os.path.dirname(dest) or '.', exist_ok=True)
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write(PAGE.format(css=CSS + EXTRA_CSS, toc=toc, body=body))

    print('wrote {}  ({} numbered points anchored)'.format(dest, n_points))


if __name__ == '__main__':
    main()
