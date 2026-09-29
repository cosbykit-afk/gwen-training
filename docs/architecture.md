Living document — update these diagrams when adding features.

# gwen-training — Architecture

Training materials for **Gwen**, Kit's Lampy administrator-in-training
(Lampy home-server stack: PostgreSQL/TimescaleDB, Apache HTTPD, Apache
James mail server, supporting services). The repo is curriculum, lesson
files, prompts, and one runner script — there is no persistent data
model; lesson-run evidence is recorded as prose status in the lesson
files per the training rule.

## Current status (2026-09-28)

Training is **paused by Kit** — the Ollama stack is flaky and the
`gwen:latest` model was down at the morning retry. Lesson 3 paused at
turn 14; a retry is staged. The diagrams below describe the intended
pipeline, not currently-running work.

## 1. Context diagram (level 0)

```mermaid
flowchart
    E1["Kit"]
    E2["Muse"]
    E3["Approved doc sources"]
    E4["Gwen runner"]
    E5["Lampy stack"]
    SYS("Gwen training material")
    E1 -->|"curriculum and requests"| SYS
    SYS -->|"run results"| E1
    E2 -->|"process explanations"| SYS
    E3 -->|"reference material"| SYS
    SYS -->|"lesson prompts"| E4
    E4 -->|"run responses"| SYS
    E4 -->|"admin work"| E5
```

## 2. Level-1 data flow diagram

```mermaid
flowchart
    E1["Kit"]
    E2["Muse"]
    E3["Approved doc sources"]
    E4["Gwen runner"]
    E5["Lampy stack"]
    P1("1.0 Author curriculum and lessons")
    P2("2.0 Prepare lesson prompts")
    P3("3.0 Run prompt on runner")
    P4("4.0 Guide lesson work")
    P5("5.0 Verify evidence")
    D1[("D1 Lesson files")]
    D2[("D2 Prompt files")]
    E1 -->|"training plan"| P1
    E3 -->|"approved sources"| P1
    P1 -->|"curriculum plus lessons"| D1
    D1 -->|"lesson content"| P2
    P2 -->|"prompt files"| D2
    D2 -->|"prompt text"| P3
    P3 -->|"prompt request"| E4
    E4 -->|"generated response plus run metadata"| P3
    P3 -->|"response with run metadata"| E1
    E2 -->|"process explanations"| P4
    D1 -->|"lesson steps"| P4
    E4 -->|"work attempts"| P4
    P4 -->|"evidence report"| D1
    P4 -->|"admin work"| E5
    D1 -->|"evidence records"| P5
    P5 -->|"verified results"| E1
    P5 -->|"next lesson"| P1
```

## 3. Entity–relationship diagram

```mermaid
erDiagram
    TRAINEE ||--o{ LESSON : works_through
    TRAINEE {
        string name PK
        string role
    }
    LESSON {
        int lesson_number PK
        string title
        string status
        string objectives
        string trainee_name FK
    }
    LESSON ||--o{ PROMPT : uses
    PROMPT {
        string file_path PK
        string target_model
        int lesson_number FK
    }
    LESSON }o--o{ REFERENCE_SOURCE : cites
    REFERENCE_SOURCE {
        string name PK
        string url
        string kind
    }
```

No persistent data model exists in this repo. The diagram above documents
the document types only — lessons, prompts, and reference sources as
files. Lesson-run evidence is recorded as prose status in the lesson
files per the training rule, not in a database.

## Grounding notes

- OBSERVED: 11 files on `main` — `README.md`, `LICENSE`,
  `00-curriculum.md`, `01-what-is-a-workflow.md`,
  `02-lesson-workflow-draft.md`, `03-mail-server-lesson.md`,
  `04-text-diagrams-lesson.md`, `lesson1-prompt.md`,
  `smoke-prompt.txt`, `gwen_ask.py`, `docs/architecture.md`.
- OBSERVED: the only commit since 2026-09-28 is `cb5f546a`
  (2026-09-28T21:23, "docs: add SAD architecture doc") — repo content is
  otherwise unchanged since 2026-09-26-era curriculum work.
- OBSERVED: README's training rule — Muse explains the process, Gwen
  does the work, she looks procedures up in approved references, and
  completion evidence is recorded honestly as proved/verified, tried, or
  failed.
- OBSERVED: `00-curriculum.md` — Lesson 1 Workflows (prepared:
  `01-what-is-a-workflow.md` reading, `02-lesson-workflow-draft.md` draft
  lesson loop with Gwen's first assignment to critique it); Lesson 2
  mail server (skeleton); Lesson 3 text-based diagrams (skeleton);
  later lessons planned but not written (webserver, per-system admin
  lessons, ClamWin scan task, firewall audit exercise, Python IDE).
- OBSERVED: `gwen_ask.py` POSTs the prompt file to
  `http://localhost:11434/api/generate` with `{"model": "gwen:latest",
  "stream": False}` and prints the response plus `---META---`
  `{done, total_duration, eval_count, prompt_eval_count}`.
- OBSERVED: approved sources (README) — local reference library
  (PostgreSQL 16 docs PDF, Debian Administrator's Handbook PDF) and
  official docs (`https://httpd.apache.org/docs/2.4/`,
  `https://james.apache.org/`, MicrosoftDocs GitHub sources).
- OBSERVED: Lesson 2 is real work, not an exercise —
  `03-mail-server-lesson.md` objective is creating her `gwen@localhost`
  mailbox, "the administrator identity she will use from now on."
- OBSERVED: `smoke-prompt.txt` — the runner smoke test is "Reply with
  exactly: Gwen online."
- OBSERVED (program records, 2026-09-28): Kit paused training — Ollama
  stack flaky, `gwen:latest` down at the morning retry; Lesson 3 paused
  at turn 14, retry staged. The "Current status" section above records
  this honestly; the diagrams describe the intended pipeline.
- INFERRED: `P5`'s "next lesson" output — the curriculum lists later
  lessons as planned, but no evidence-verification artifacts (reports,
  logs) exist in the repo; the loop's trigger is the training rule and
  `02-lesson-workflow-draft.md` (read, study, do, verify, report, log),
  not an observed file.
- INFERRED: `P4` → `E5` "admin work" — grounded in Lesson 2's objective
  (mailbox creation on the Lampy stack), but no admin-work output has
  been observed in the repo.
