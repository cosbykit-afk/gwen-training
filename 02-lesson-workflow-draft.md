# Lesson workflow (DRAFT — to develop together)

This is a first draft of the workflow you will use to work through lessons.
It is not final. Your first job as a thinking administrator is to read it,
try it on your first lesson, and tell Muse what you would change. A workflow
that you helped shape is one you will actually follow.

## The loop

For each lesson you are given:

- **Step 1 — Read.** Read the lesson's objective, its questions, and its links
  to approved sources.
  - Done when: you can restate the objective in your own words.

- **Step 2 — Study.** Look up the answers in your approved sources **yourself**.
  Your reference library (PostgreSQL documentation, Debian handbook,
  MicrosoftDocs, the Apache and James documentation sites) is where
  procedures live. Do not ask Muse to explain the manual to you.
  - Done when: you can answer each lesson question and name the source
    each answer came from.

- **Step 3 — Do.** If the lesson has hands-on tasks, carry them out with your
  Python scripts.
  - Done when: each task's script ran and you kept its output.

- **Step 4 — Verify.** Prove the work worked: config tests, status checks,
  reading back what you changed. Match this against the "Done when" line
  of every step you ran.
  - Done when: every claim you will report has evidence behind it.

- **Step 5 — Report.** Tell Muse, in your own words: what the lesson taught,
  what you did, what the evidence showed, and what failed or surprised you.
  - Done when: the report is sent and every claim in it is scoped
    (proved / tried / failed).

- **Step 6 — Log.** Append the lesson's outcome to your learning log:
  date, lesson name, what you learned, what you changed, open questions.
  - Done when: the log entry exists.

## Questions for you (answer when we develop this together)

1. Is any step unclear or in the wrong order?
2. What should happen when a step fails — retry, skip, or stop and ask?
3. How should the learning log be organized so you can find old entries?
4. What belongs in the workflow that is missing here?

## Learning log format (proposed)

```
## YYYY-MM-DD — <lesson name>
- Learned: ...
- Did: ... (scripts run, outputs kept where)
- Evidence: ...
- Failed / surprised by: ...
- Open questions: ...
```
