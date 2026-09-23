# Gwen's lesson plan (curriculum)

Training order. Each lesson is worked through with the lesson workflow
(`02-lesson-workflow-draft.md`): read, study from approved sources, do,
verify, report, log.

## Lesson 1 — Workflows (prepared)

- `01-what-is-a-workflow.md` — what a workflow is, the roles (Muse explains,
  Gwen does), evidence rules.
- `02-lesson-workflow-draft.md` — DRAFT of the lesson loop, to develop
  together with Gwen. Her first assignment: critique and improve it.

## Lesson 2 — Mail server: set up James, create her account (skeleton)

- `03-mail-server-lesson.md`
- Objective: understand how Apache James runs on Lampy and create her own
  mailbox (`gwen@localhost`, the password Kit chose).
- This lesson is real work, not an exercise: the account she creates is the
  administrator identity she will use going forward.
- Hands-on: add the user through James's WebAdmin API from inside the
  container, then verify the account exists.

## Lesson 3 — Text-based ER and systems diagrams (skeleton)

- `04-text-diagrams-lesson.md`
- Objective: read and write text-based entity-relationship diagrams and
  systems diagrams.
- Example material: text-based renderings of Lampy's own diagrams —
  the forum database ER diagram and the Lampy system diagrams, drawn as
  text (not images), prepared as part of this lesson.
- Hands-on: describe the forum ER in her own words; draw a text diagram
  of one part of the Lampy stack.

## Later lessons (planned, not yet written)

- Webserver study page: setting up a web server, as questions + hyperlinks
  to approved sources (Kit's request — comes after the workflow is settled).
- PostgreSQL administration, Apache administration, James administration —
  one lesson per system she administers, each grounded in her reference
  library (which she consults herself, per the training rule).
- Initiate a virus scan (Kit's request 2026-09-22): Gwen runs a real
  ClamWin on-demand scan on Toetop through a controlled wrapper script —
  scan-only, no quarantine or deletion without explicit approval — then
  reads the report, interprets the results, and files her findings.
  Objective: her first real maintenance task end to end: invoke, monitor,
  verify, report.
- White-hat firewall exercise (Kit's request 2026-09-22): Gwen learns
  firewall administration by attacking our own configuration — with
  permission, on our systems only. She reads the current firewall rules,
  writes down what each rule should allow and block, then empirically
  tests them with controlled connection attempts (port probes, allowed
  vs. denied paths) and reports every mismatch between the rules as
  written and the behavior as measured. Strict scope: our own machines
  only (Toetop, the Lampy containers); connection attempts only, no
  payloads, no exploitation, no external targets. Objective: understand
  what a firewall rule actually does by verifying it, and give us a real
  audit of our configuration in the process.
- Python IDE lesson: writing scripts not yet in her repository (Kit's
  request 2026-09-22): working in her own Python IDE/workspace, Gwen
  studies the existing script pack's patterns (argument handling, safety
  rails, logging, confirmation gates for destructive operations), then
  authors a brand-new admin script for a task nothing covers yet, tests
  it, and submits it for review. Objective: she extends her own toolkit
  following the established conventions, instead of only running
  scripts others wrote.

## Approved sources (the only references lessons may link to)

- Her local library: PostgreSQL 16 documentation (PDF), Debian
  Administrator's Handbook (PDF).
- Official documentation sites: https://httpd.apache.org/docs/2.4/
  (Apache), https://james.apache.org/ (James),
  https://github.com/MicrosoftDocs (Microsoft docs sources).
