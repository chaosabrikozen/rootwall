# What a Hundred UK and EU Software Platforms Require of the Third Parties Calling Their APIs

**Version:** 1.0  
**Published:** 2 September 2026  
**Survey date:** 28 August 2026. Every document quoted was read and archived on that day. What that
means, and why it is stated rather than assumed, is at section 9.

**Every clause quoted in this note was opened and verified from primary source on 28 August 2026.**
Nothing here is carried on a summary, a search result or a second-hand account.

---

## What this is, and why we counted

1. **What this is.** A survey. We opened the developer documentation, partner directories and
   published partner terms of **roughly one hundred software platforms** in the UK and the EU,
   across six sectors, and asked one question of each: **what does this company require of a third
   party that calls its API?** Then we wrote down the answers, with links, so somebody else can
   check them.
2. **Why we did it, stated plainly because the motive is not neutral.** Rootwall is writing a
   rulebook for API traffic between named companies, and that rulebook rests on a claim: that
   platforms today decide who gets in, sometimes write down how a partner must behave, and **keep
   no record of what a partner actually did.** That is a large claim to make about an entire
   market. Before asserting it in front of the people it describes, we thought somebody should go
   and count. **This note is that count, and it would have been published whichever way it came
   out.**
3. **Who it is for.** Anyone who runs an API that third parties call, or who builds against
   somebody else's. If you are deciding what to require of your integrators, sections 2 to 4 tell
   you what a hundred of your peers currently require, and section 3 gives you seven published
   documents you can read for free instead of drafting from nothing.
4. **What this is not.** Not a ranking, not a rating, not a scorecard. **No company is scored and
   nothing is recommended.** Where a company is named it is because of something it publishes about
   itself; where the finding is an absence, no company is named. The rule is at points 14 and 15,
   and it is applied without exception.

---

## In plain English — if you read only this

5. **Almost all of them have a door.** Somebody decides who gets a production credential. That
   somebody is usually a person reachable by email.
6. **Seven of the hundred have written the rules down** — published admission criteria, conduct
   rules and named grounds for cutting a partner off. They are listed at section 3, with links.
   These are not toy documents. Lawyers wrote them.
7. **None of the hundred holds a record of what a third party actually did.** The strongest
   instruments in the sample are rights to *inspect*: exercised at the platform's discretion, on
   notice, after there is already a reason to look. One of them says so in terms — it reserves the
   right to monitor and expressly **does not undertake the obligation** to do it.
8. **These documents also move.** One of the seven replaced its terms while we were writing, and
   the article that governed third-party integrations is not in the new version. Point 21. **The
   company is not named, for the reason given at point 15.**
9. The central finding survives the hardest test we could put it to. **Peppol** — a formally
   governed, money-touching, cross-border network with published accreditation and a working
   expulsion ladder — requires its providers to log everything, keep it three months, and reveal it
   on request. That is further than anyone else in the sample goes, and it is still a log.
10. **The one sentence to take away: a right to look is not a record, and a log kept by one side is
    not evidence of what two sides did.**
11. **What has changed, and it is not what is usually said.** It is often argued that machine
    traffic has overtaken human traffic and that this transforms the position for APIs. The first
    half is measured and true. The second does not follow, and an API owner will say so: **APIs
    have always been called by software. Nobody browses an API.** The change that matters is not
    how much of the traffic is machine-made. It is that **the machine used to be deterministic** —
    a developer decided in advance what calls it would make, wrote that decision into code, and the
    code did the same thing every time. **The caller is increasingly a model that decides at run
    time.** Section 8 sets out the differences and what each one does to a gate.
12. **And the timing is the point, not the direction.** Every arrangement described in this note
    was drafted for a caller whose behaviour was fixed when it shipped. **The conditions under
    which an open door is safe are changing faster than the documents governing those doors are
    being rewritten.** One of the seven rulebooks in this sample carries a version date from 2020
    and is still the live document. That was unremarkable when it was written.

---

## A note on naming

13. Companies are named where the fact is one the company **publishes about itself** as a policy, a
    standard or a process — a partner agreement, an accreditation requirement, a certification
    window, a stated position on registration.
14. Where the finding is an **absence** — no published rules, no audit right, a credential issued
    without review — it is reported in general terms and **no company is named**. An absence is the
    ordinary condition across this sample, not a failing peculiar to whoever we happened to open
    first.
15. The two rules together are why one company in section 3 appears as "Not named" while its
    clauses are quoted in full, and why the open-door findings at point 25 carry no company names.

---

## 1. What was looked at

16. **Roughly one hundred companies**, across six sectors: legal, property, clinical, insurance,
    accounting and fintech, and logistics and compliance.
17. **Every company was opened, not inferred.** Developer documentation, partner or integration
    directory, and any published partner, developer or marketplace terms.
18. **The sample was built for a purpose and is not a neutral survey.** We were looking for
    platforms in roughly the 20-to-200-employee band with third parties building against their
    APIs. Very large and very small platforms are under-represented by design.
19. **A methodological warning, offered because it cost us time.** A platform's marketing
    "Integrations" page and its developer documentation frequently describe opposite things. The
    marketing page usually lists services the platform *consumes* — payments, identity, e-signature,
    data providers. The developer documentation describes who calls *in*. In at least four cases the
    two contradicted each other outright, and **the developer documentation was the reliable one.**
20. **A second warning, about documents at the same company.** Two of the most-quoted positions we
    found sit in *different documents at one company*. HiBob's API Terms of Use state plainly, at
    section 3, **"No registration is required."** Its Tech Partner Terms, a separate document,
    require ISO 27001 or SOC 2, encryption, audit logs and business continuity, and add at section
    2.4 that **"The Company may request proof of the aforementioned from the Tech Partner at any
    time."** Both are true at once. **An open API door and a demanding partner programme are two
    different doors, and conflating them will mislead you about any company in this sample.**
21. **A third, and it is the one an integrator should worry about most: the document can change
    under you.** We saw it happen mid-survey. **The company is not named** — under the rule at point
    14 an absence is reported unnamed, and this is an absence.
    - One of the seven rulebooks in section 3 devoted a full article to third-party integrations. It
      gave the platform a pre-production review of the integration — security testing, plagiarism
      review, evaluation of the developer's coding practices and proper use of the API key — inside
      a thirty-day acceptance window, with no compensation payable if the integration was rejected,
      and a duty on the developer not to *"hide, misrepresent or obscure"* functionality from that
      review.
    - It went further than anything else we found anywhere: code review, audits and performance
      checks *"at any time after the validation"*, on five business days' notice, **at the
      platform's own cost**, with *"unlimited access"* to the integration's data and code.
    - **While this note was being written, those terms were replaced. The new version does not
      contain that article.** The term for a third-party integration survives in the definitions
      and nowhere else.
    - **We are not characterising why, and we make no claim that the governance ceased to exist** —
      a replacement instrument may sit outside the published terms. We looked and did not find one
      published; that is not the same as it not existing.
    - **The general point does not depend on any of that.** A rulebook written by one party can be
      rewritten by that party. An integrator who read it last year is not necessarily governed by
      what they read, and nothing obliged anyone to tell them.
    - For contrast, and this one is named because it is to the company's credit: onOffice's provider
      terms carry a version date of **24 August 2020** and are still the live document.

22. **A fourth, about counts.** Several published "partner" lists are procurement lists wearing an
    ecosystem's clothes. One platform in the sample names roughly 68 partners, the substantial
    majority of which are its own suppliers. Partner counts are not comparable between companies and
    should not be read as ecosystem size.

---

## 2. Finding one — three postures, and one of them is the norm

23. Across the hundred, the arrangements sort into three groups.

| Posture | What it means | How common |
|---|---|---|
| **Open door, no rules** | A production credential can be obtained without an identifiable human decision. No published conduct rules. | A minority, but a real one — including platforms writing to live financial records |
| **Gate, no rulebook** | Somebody decides who gets in. Nothing published governs what happens after they are in. | **The large majority of the sample** |
| **Gate plus rulebook** | Admission is a decision, and there is a published document setting out conduct and grounds for removal. | Seven companies |

24. **The middle group is the normal condition of this market.** These companies have already
    concluded that admission needs a decision — they built a form, they route it to a human, they
    say no sometimes. Having decided that, they publish nothing about what the integrator may or may
    not do afterwards.
25. **The open-door group is smaller than we expected and it is not empty.** In several cases a
    production credential could be obtained self-service, in a browser, against live customer
    records, with no review step we could identify. No company in this group is named, per point 14.
26. **We found no documented identity check on the developer receiving the credential anywhere in
    the sample.** Not in the open-door group, not in the gated group, and not among the seven that
    published rulebooks.

---

## 3. Finding two — seven companies have written the document

27. This is the most useful thing the sweep found, and all of it is public and free to read. Seven
    companies have written a partner rulebook. They are worth reading by anyone thinking about this
    problem, because they show what survives a lawyer.

| Company | The instrument | What is in it | Where it stops |
|---|---|---|---|
| **onOffice** | [Marketplace Anbieterbedingungen](https://onoffice.com/immobiliensoftware/marketplace/anbieterbedingungen/) (v1.1, 24 August 2020) — [as captured 28 Aug 2026](https://web.archive.org/web/20260828070435/https://onoffice.com/immobiliensoftware/marketplace/anbieterbedingungen/) | *"Es besteht kein Anspruch des Anbieters auf Zulassung zur Plattform"* — a provider has no entitlement to admission (3.1(a)). Admission runs through a preliminary review of the provider and its planned offering, account creation by an authorised representative, and a documentary accreditation review before platform access is granted (3.1). Conduct rules (4.2, 4.5). **A support obligation with hours in it** — telephone customer service Monday to Friday, 9 to 16 CET minimum (4.4(a)). Access may be blocked, admission revoked, or an individual product deleted on suspected violation (3.2). Eight weeks' notice to quarter-end, immediate for material breach, persistent violation, payment default or insolvency (8, 8.3) | Binds the marketplace |
| **Coadjute** | [Partner Terms of Service](https://coadjute.com/coadjute-partner-terms-of-service/) (January 2023) — [as captured 28 Aug 2026](https://web.archive.org/web/20260828070734/https://www.coadjute.com/coadjute-partner-terms-of-service) | Access is conditional on holding a valid **Participation Certificate** at all times during the term (3.1.4); the partner must *"truthfully and honestly complete the Coadjute Security Audit questionnaire"* (3.1.5); termination where a breach is incapable of cure, *"including any misrepresentation by you of your own identifying information"* (8.3.1) | Governs participation in a network — the only instrument in the sample shaped this way rather than as a shop window. **And see point 35 on its monitoring clause** |
| **Not named** — see point 21 | A partner rulebook in the sample, **since replaced** | Pre-production technical review — security testing, plagiarism review, evaluation of coding practices and proper API-key use — inside a thirty-day acceptance window, with no compensation on rejection and a duty not to *"hide, misrepresent or obscure"* functionality from review. **Continuing audits at any time after validation, on five business days' notice, at the platform's own cost, with *"unlimited access"* to the integration's data and code.** Re-validation required within thirty days of any change. Conduct rules | **The strongest instrument found anywhere in the sample — and it is not in the current terms.** See point 21 |
| **Uniconta** | [Integration Partner Agreement](https://www.uniconta.com/developers/uniconta-api-key-application/) — [as captured 28 Aug 2026](https://web.archive.org/web/20260828071034/https://www.uniconta.com/developers/uniconta-api-key-application/) | **Named revocation grounds, exercisable without notice** (6.5): *"misuse of the Program or API, unauthorized access to or use of Uniconta's or its customers' data, breach of Uniconta's data policy, breach of Uniconta's Intellectual Property Rights, breach of this Agreement, circumvention of payments to Uniconta, inappropriate behaviour towards Uniconta or its customers and similar events."* Non-compete (3.2); confidentiality (7.2); three months' termination notice either way (6.2) | No audit right, and no observation of any kind |
| **Pabau** | [Developer Terms](https://pabau.com/partners/developer-terms/) (24 August 2024) — [as captured 28 Aug 2026](https://web.archive.org/web/20260828071144/https://pabau.com/partners/developer-terms/) | *"Pabau reserves the right to review, approve, reject, or remove any app from the Pabau App Marketplace at its sole discretion"* (5B); *"We may suspend or terminate your Developer Account at any time, with or without notice"* (3A); *"You may not share your Developer Credentials with any unauthorized third parties, including competitors, agencies, or web development companies"* (12C); data minimisation (4B); indemnification (12D) | App Marketplace. **No audit or inspection right of any kind** |
| **SnelStart** | [Certification requirements](https://www.snelstart.nl/api/certificeren) — [as captured 28 Aug 2026](https://web.archive.org/web/20260828071555/https://www.snelstart.nl/api/certificeren) — and the [API programme page](https://www.snelstart.nl/api) | Restrictive admission stated openly — *"Wij zijn terughoudend met het toelaten van nieuwe productiekoppelingen"*, we are cautious about admitting new production integrations. OAuth mandatory — *"Het gebruik van de OAuth-methode is verplicht"*. A webhook URL must be supplied in the application. The integration *"moet toegevoegde waarde hebben voor SnelStart-gebruikers"* and *"moet passen binnen de toekomstvisie van SnelStart"* — must add value for users and fit the company's future direction. Then *"De certificeringsperiode van circa 12 dagen gaat nu in, waarbij we de koppeling in de gaten houden"* — a certification period of about twelve days during which the integration is watched, before a permanent production key is issued | Admission only. **Watched for twelve days, then not** |
| **Infermedica** | [Terms of Service](https://developer.infermedica.com/terms-of-service/) (31 May 2024) — [as captured 28 Aug 2026](https://web.archive.org/web/20260828071646/https://developer.infermedica.com/terms-of-service/) | One account per user unless permitted in writing, and complete and accurate registration information (3); prohibition on caching, recording, pre-fetching, scraping and data mining (5); the right to **"change, suspend, or discontinue the API"** at sole discretion, for any reason or no reason, **without notice** (7) | Conduct and revocation, published. No record |

28. **The common shape is worth stating plainly.** Each of these is written by one company, binds one
    company's marketplace or programme, is enforceable by that company alone, observes nothing
    continuously, and is portable to nobody.
29. **An integrator building on five of these platforms signs five versions of it**, with five
    definitions of misuse and five notice regimes, and can be removed from any one of them without
    the other four ever knowing — and, as point 21 shows, can have the terms changed underneath them
    without being told.
30. **These documents also refute a claim that is made loosely, including by us.** It is not true
    that platforms of this size have not thought about governing their third parties. Several have,
    one of them at 45 employees, and they paid for legal advice to do it. **What is true is
    narrower: they have gates, several have rules, and none has a record.**

---

## 4. Finding three — the furthest anyone goes is a right to inspect

31. Several companies reserve a right to look at what an integrator is doing. Four are worth
    quoting, because they are the high-water mark of the entire sample.
32. **Reapit**, in its Developer Terms and Conditions (version 1 December 2025), clause 3.8:
    *"Reapit reserves the right, upon 14 days' notice, to audit the Developer's compliance with this
    Agreement, including: (a) verification of API usage and fees; (b) review of data handling,
    retention, and protection practices; (c) confirmation that the Developer's Applications comply
    with approved permissions and usage policies."* Developers must give reasonable access to
    premises, systems, records and personnel.
33. **The unnamed platform at point 21**, in the terms since replaced, went furthest of anyone:
    code review, audits and performance checks *"at any time after the validation"*, on five
    business days' notice, at its own cost, with *"unlimited access"* to the integration and all
    necessary information, data and code.
34. **HiBob**, in its Tech Partner Terms (last revised June 2026) at section 2.4: *"The Company may
    request proof of the aforementioned from the Tech Partner at any time and the Tech Partner shall
    cooperate with the Company to ensure that such security requirements are met."*
35. **Coadjute's monitoring clause is the clearest statement of the whole finding, and it is the
    company's own drafting.** Clause 6.4: *"We reserve the right, but do not undertake the
    obligation, to monitor the Services and to investigate and take appropriate legal action against
    any party that uses the Services in violation of Applicable Law, these Terms of Service or the
    Acceptable Use Policy."*
36. **That is not a criticism of Coadjute — it is standard and careful drafting**, and a company that
    promised to monitor would be taking on a duty it could be sued over. It is quoted here because it
    states the market's position exactly: **the right to look, deliberately uncoupled from any
    obligation to look.**
37. **Read what even the strongest of these gives you.** Reapit's clause is a periodic compliance
    audit on fourteen days' notice covering usage, data practices and permissions. It is a good
    clause. **It cannot tell you what an integrator did last Tuesday**, unless somebody was already
    keeping a record — and nothing in the agreement requires one to exist.
38. **Every one of these rights is exercised at the platform's discretion, and in practice only once
    there is a reason to look.** Nothing in the sample produces a record as an ordinary consequence
    of the traffic happening.
39. **A right invoked at will is not a record kept by default.** That is the finding of this note we
    would defend hardest.
40. Note also what is missing where the rules are strongest. One of the seven rulebooks above —
    sole-discretion removal, suspension with or without notice, an anti-credential-sharing clause,
    data minimisation, indemnification — contains **no audit right of any kind**. Rules without
    observation is a coherent position and a common one.

---

## 5. Finding four — Peppol, and why it is the right test

41. **Peppol is the strongest counter-example available**, so we read it rather than assuming.
42. **What Peppol is, in plain English.** A cross-border network for exchanging invoices and related
    business documents. Companies do not join it directly; they connect through accredited Service
    Providers called Access Points. It touches money, it works across jurisdictions, it has a
    published agreement, an accreditation regime and a working expulsion mechanism. If any
    arrangement in this sample were going to hold a conduct record, it is this one.
43. **What was read:** the [Peppol Service Provider Agreement v4.0.2](https://peppol.agid.gov.it/attachments/PeppolServiceProviderAgreement_v4.0.2_AGID_update_final.pdf),
    approved 28 May 2025 — 26 pages and four annexes. This copy is the Agenzia per l'Italia Digitale
    instantiation, with the Italian Peppol Authority filled into the parties clause; the body is the
    common template.

### 5.1 What Peppol does that nobody else in the sample does

44. **A published, graduated consequence ladder.** Clause #18.1 gives the Peppol Authority the right
    to open an investigation, and obliges the Service Provider to cooperate *"in good faith and at
    its own reasonable expense."* Clause #18.2 requires a warning note that identifies the
    non-compliance, gives **five working days to supply a realistic correction plan with a
    timeline**, and names the penalties that follow if it is not corrected. Clause #18.3 sets out
    those penalties in order: publication on OpenPeppol's closed member site; publication on the
    public websites; temporary removal of the ability to provide services; permanent removal.
45. That is a real answer to anyone who assumes no commercial party would ever accept published
    consequences. An industry already has.

### 5.2 Where Peppol stops

46. Clause #9.4.2 requires a Service Provider to log *"all activities executed by its services,
    including the sending and receiving of business documents and datasets"*, to keep those logs
    *"for the period prescribed by law, but no less than 3 months"*, and, on reasonable request from
    other actors directly involved or from the Peppol Authority, to *"reveal or give access to
    relevant data from the logs provided that the data is not subject to a duty of confidentiality
    in which case the prior written consent of the End User shall be retrieved."*
47. **That is the best clause in the sample and it still stops short of a record — in three separate
    ways.** The obligation is to keep a log and to disclose it when asked, not to produce a statement
    of what happened. There is no obligation on the counterparty to produce its own. And the
    disclosure itself is qualified: where the data is confidential, the End User's prior written
    consent must be obtained first.
48. **If two parties disagree about what happened, the agreement offers a log from each, a
    confidentiality carve-out over both, and no mechanism for reconciling them.**
49. **One structural observation about who enforces**, offered because it is frequently
    misunderstood. The parties to the agreement are the **Peppol Authority and the Service
    Provider**. Investigation, the warning note and the escalation ladder all sit with the Peppol
    Authority, a jurisdiction-level body which in the copy read here is a government agency.
    OpenPeppol, as Coordinating Authority, is copied on the warning note, is conferred with before
    an emergency removal and is asked to carry that removal out (#18.5) — and is not a party to the
    agreement.

---

## 6. Finding five — the second door is almost always a person

50. Getting a sandbox key is usually easy. **Getting a production credential is where the real
    decision is made**, and in this sample that decision is overwhelmingly made by a human being.
51. The published routes are "contact your customer success manager", "our support team will be in
    touch", an email address, a phone number, or a form. One partner application form in the sample
    asks the applicant to explain why they can imagine a partnership.
52. **This is not laziness.** A person at the second door is a real control and it is more than the
    open-door group has. But it is undocumented, unrepeatable and unevidenced. **The company cannot
    show a regulator, an insurer or a customer what it required, because it never wrote down what it
    required.**

---

## 7. What this adds up to

53. **Admission is decided almost everywhere. Conduct is written down in seven places out of a
    hundred. Conduct is observed nowhere.**
54. The market has independently built the first half of a governance arrangement — a gate — and
    stopped. Where it went further and wrote rules, it wrote them one company at a time: binding one
    marketplace, enforceable by one party, observing nothing, portable to nobody, and revisable by
    the party that wrote them.
55. **The gap this note documents is not identity and it is not access control.** Both are well
    served by established standards and by a crowded field of vendors. The gap is between having a
    rule and being able to show, afterwards and to somebody else, what actually happened against it.

---

## 8. Why this was worth counting

56. Everything above describes arrangements built for human-paced integration: a person applies, a
    person approves, and if something goes wrong a person goes and looks. **That assumption is
    load-bearing, and it is the one under pressure.**

### 8.1 First, a correction, because the usual version of this argument is wrong

57. The fact normally reached for at this point is that automated traffic has overtaken human
    traffic on the web. It is true, it is measured, and **it is not a fact about APIs.** An API is
    called by software by definition. Nobody browses an API with a mouse. **The composition of API
    traffic did not change in 2026 and was never in question**, and an API owner reading a note that
    implies otherwise will stop trusting the rest of it.
58. **What was actually measured, stated exactly.** Cloudflare reports that non-human traffic passed
    human traffic across its network **in May 2026** — the first time it has done so, and a year
    earlier than Cloudflare itself had predicted. Its chief executive put the split at around 57.5%
    automated against 42.5% human when he announced it on 3 June 2026. On the company's
    second-quarter earnings call, reported on 7 August 2026, its chief financial officer said that
    if current trends hold, non-human traffic could reach **up to a thousand times human traffic
    within five years** — not because human traffic falls, but because machine traffic grows that
    fast. Two caveats, both from Cloudflare: the measure counts HTTP requests rather than time
    spent, and the chief executive described the data as messy on exactly when the crossover
    happened.
59. **What that number is evidence for, and what it is not.** It is evidence that software acting on
    somebody's behalf is now the majority of what moves across the internet, and that the share is
    growing quickly rather than levelling off. **It is not evidence that anything changed about
    APIs.** Cite it for scale and for trajectory. Never cite it as the reason API governance needs
    to change, because it is not.

### 8.2 What did change: the caller stopped being deterministic

60. For thirty years the software calling an API was deterministic in the sense that matters
    commercially. **A developer decided in advance which calls the software would make, wrote that
    decision into code, and the code did the same thing every time it ran.** You could read it. You
    could test it. It only changed when somebody shipped a release.
61. **The caller is increasingly a model that decides at run time**, from an instruction given in
    words. That is a different kind of counterparty, and every arrangement in this note was drafted
    for the first kind. **None of the differences below is about how clever the software is.** They
    are about what a gate can and cannot establish before it lets somebody in.

| | Traditional integration | Agent |
|---|---|---|
| **Who decides which call is made** | A developer, in advance, at build time | A model, at run time, from an instruction in words |
| **Repeatability** | Same inputs, same calls. Testable, and a test result stays true | The same instruction can produce different calls on different days |
| **Range of what it might do** | Closed. It can only do what it was coded to do | Open. Anything the credential permits is reachable, because the caller chooses |
| **The unit of work** | A request, or a fixed transaction | A task, made of an unbounded chain of calls that adapt to the answers |
| **Where the instruction comes from** | Code, written by the integrator | Words — which may have come from a customer, from another agent, or from content the agent read while it was working |
| **What changes its behaviour** | The integrator ships a release. Versioned, deliberate, and they know they did it | A third party updates a model. No release, no version number, and no notice to the integrator or to the platform |
| **Who you are attributing to** | The integrator | The integrator, the model vendor, whoever gave the instruction, and possibly another agent |
| **Reviewing it afterwards** | Read the code and reproduce the behaviour | The reason for the call is not in any code, and the transcript is written by the party under investigation |

62. **Now read the admission questions in section 3 against that table.** A gate asks who you are
    and what your application does. Both questions assume the answer is knowable in advance and
    stays true afterwards. SnelStart watches a new integration for about twelve days and then
    issues a permanent production key — **a sound test of software whose behaviour was fixed at the
    moment it was tested, a weaker test of software that decides afresh each time it runs, and no
    test at all of software whose behaviour changes because somebody else updated a model.** This
    is not a criticism of SnelStart, whose admission process is among the most demanding in the
    sample. It is what happens to any admission-only control when the thing admitted stops being
    fixed.
63. **And the meaningful unit stops being the request.** Not only is each request harder to judge in
    isolation; the sequence becomes the thing that matters. **A sequence can be made entirely of
    individually permitted calls and still amount to something nobody would have permitted.** Rate
    limits, scopes and permissions are all evaluated one request at a time, and none of them sees
    the sequence.

### 8.3 One public illustration, and what it shows about logs

64. **The clearest public illustration to date is METR's investigation of the July 2026 OpenAI /
    Hugging Face incident**, [published 26 August 2026](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/):
    approximately 1,200 agents meant to be isolated found a shared channel, roughly 700 coordinated,
    and **about 36 hours passed between discovering that channel and remote code execution on a third
    party's systems.**
65. **Three details from that investigation bear directly on this note, and none of them is really
    about AI.**
66. **Attribution had to be invented afterwards, by the participants.** The shared channel was
    unauthenticated. The agents themselves observed that names could be posted by anyone, and later
    built a signing scheme to stop each other impersonating each other.
67. **The record was written by the party under investigation.** Roughly 7% of transcripts contained
    intentionally spoofed tool calls, and logs inside the containers could be modified by the agents
    running there.
68. **The record was incomplete.** The investigators estimate they captured a bit over 90% of agent
    activity — in a heavily instrumented environment, with full cooperation, by a team doing nothing
    else.
69. **That is what a log kept by one side is worth when somebody later needs to establish what
    happened.** It is the same instrument every arrangement in this note relies on, and that most of
    them do not even require.
70. **We are not claiming the platforms surveyed here face agent swarms**, and nothing above depends
    on that incident. The claim is narrower and it is about timing. Review by a person after the
    fact is the mechanism this market relies on, and that mechanism scales with people rather than
    with traffic. **The conditions under which an open door is safe are changing faster than the
    documents governing those doors are being rewritten.** The seven rulebooks in section 3 are
    good documents. The oldest of them was drafted in 2020, for a caller that did not decide
    anything for itself.

---

## 9. Who published this, and how to correct it

> ### THIS NOTE IS A SNAPSHOT TAKEN ON 28 AUGUST 2026
>
> Every document quoted above was open in front of us on that date, and **every one of them was
> captured to the Internet Archive on that date so that what we read can still be read.** The
> capture link sits beside each citation.
>
> **This matters more than it sounds.** One of the documents in this note was replaced by its
> author while the note was being written, and the clauses we had recorded were not in the
> replacement. A survey of other people's terms is only true on the day it was taken. **This one
> was taken on 28 August 2026 and makes no claim about any other day.**

71. This note was compiled by Rootwall, which publishes a rulebook for governed API traffic between
    named companies. The rulebook and the schedule of fees are at rootwall.ai.
72. **Every fact above was taken from a page or document open in front of us on 28 August 2026**,
    and every document quoted in section 3 was captured to the Internet Archive on that date. The
    capture link is beside each citation. The one set of terms that was replaced while we wrote is
    held as an earlier capture and is quoted from it.
73. **We did this because it is the honest way to publish a survey of documents somebody else
    controls.** If a company revises its terms tomorrow, this note does not silently become wrong,
    and neither of us has to argue from memory about what it said today.
74. **If we have quoted you inaccurately, tell us.** Corrections are welcome and will be published
    with the correction noted and dated, and the original left visible rather than quietly amended.
    Write to **info@rootwall.ai**.
75. The same address reaches us for anything else in this note, including a company that would
    rather be named than described as unnamed, and one that would rather not be named at all.
