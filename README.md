# Gwen's Training

Training program for **Gwen**, the AI administrator of the Lampy home-server
stack (PostgreSQL/TimescaleDB, Apache HTTPD, Apache James mail server, and
supporting services).

## The training rule

- **Muse explains the process.** He describes the goal and the workflow.
- **Gwen does the work.** She follows the steps, runs the scripts, reads the
  sources herself.
- She looks procedures up in **approved references** rather than being quoted
  procedures.
- Completion evidence is recorded honestly as **proved/verified, tried, or
  failed** — never asserted.

## Contents

| File | What it is |
|---|---|
| `00-curriculum.md` | The lesson plan: training order, lesson objectives, planned later lessons, approved sources |
| `01-what-is-a-workflow.md` | Lesson 1 reading: what a workflow is, the roles, why workflows matter |
| `02-lesson-workflow-draft.md` | DRAFT of the lesson loop — Gwen's first assignment is to critique and improve it |
| `03-mail-server-lesson.md` | Lesson 2 skeleton: Apache James, creating her own admin mailbox (real work, not an exercise) |
| `04-text-diagrams-lesson.md` | Lesson 3 skeleton: reading and writing text-based ER and systems diagrams |
| `lesson1-prompt.md` | The prompt given to Gwen's runner when Lesson 1 begins |
| `smoke-prompt.txt` | A minimal smoke-test prompt for the runner |
| `gwen_ask.py` | Helper script: sends a prompt file to Gwen's local runner (Ollama API) and prints the response with run metadata |

## Approved sources

Lessons may link only to:

- Her local reference library: PostgreSQL 16 documentation (PDF), Debian
  Administrator's Handbook (PDF).
- Official docs: https://httpd.apache.org/docs/2.4/ (Apache),
  https://james.apache.org/ (James), https://github.com/MicrosoftDocs
  (Microsoft docs sources).

## Planned later lessons

Webserver study page (questions + hyperlinks), one administration lesson per
system she administers (PostgreSQL, Apache, James), a ClamWin virus-scan
maintenance task, a white-hat firewall audit exercise, and a Python IDE
lesson on authoring new admin scripts. See `00-curriculum.md` for details.
