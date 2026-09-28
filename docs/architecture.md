Living document — update these diagrams when adding features.

# gwen-training — Architecture

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
    E2["Gwen runner"]
    E3["Approved doc sources"]
    P1("1.0 Author curriculum and lessons")
    P2("2.0 Prepare lesson prompts")
    P3("3.0 Run prompt on runner")
    P4("4.0 Guide lesson work")
    P5("5.0 Verify evidence")
    D1[("D1 Lesson files")]
    D2[("D2 Prompt files")]
    D3[("D3 Reference list")]
    E1 -->|"training plan"| P1
    E3 -->|"approved sources"| P1
    P1 -->|"curriculum plus lessons"| D1
    D1 -->|"lesson content"| P2
    P2 -->|"prompt files"| D2
    D2 -->|"prompt text"| P3
    P3 -->|"response with run metadata"| E1
    E2 -->|"lesson execution"| P4
    D1 -->|"lesson steps"| P4
    P4 -->|"evidence report"| P5
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
    }
    LESSON ||--o{ PROMPT : uses
    PROMPT {
        string file_path PK
        string target_model
    }
    LESSON }o--o{ REFERENCE_SOURCE : cites
    REFERENCE_SOURCE {
        string name PK
        string url
        string kind
    }
```

No persistent data model exists in this repo. The diagram above documents the document types only — lessons, prompts, and reference sources as files. Lesson-run evidence is recorded as prose status in the lesson files per the training rule, not in a database.

## Grounding notes

- OBSERVED: 10 files — `README.md`, `LICENSE`, `00-curriculum.md`, `01-what-is-a-workflow.md`, `02-lesson-workflow-draft.md`, `03-mail-server-lesson.md`, `04-text-diagrams-lesson.md`, `lesson1-prompt.md`, `smoke-prompt.txt`, `gwen_ask.py`.
- OBSERVED: README training rule — Muse explains the processes, Gwen does the work, she looks procedures up in approved references, and completion evidence is recorded honestly as proved or verified, tried, or failed.
- OBSERVED: `00-curriculum.md` is the lesson plan — Lesson 1 workflows prepared, Lesson 2 mail server skeleton, Lesson 3 text diagrams skeleton, later lessons planned but not written.
- OBSERVED: `gwen_ask.py` sends a prompt file to `http://localhost:11434/api/generate` with model `gwen:latest` and prints the response plus run metadata.
- OBSERVED: approved sources — local reference library (PostgreSQL 16 docs PDF, Debian administrator handbook PDF) and official docs (httpd.apache.org, james.apache.org, Microsoft docs).
- OBSERVED: Lesson 2 is real work not an exercise — the mailbox Gwen creates becomes her administrator identity on the Lampy stack.
- INFERRED: the response returned by the runner is shown to Kit but is not persisted in the repo; no lesson-run log store was observed.
- INFERRED: P5 evidence verification loop — the training rule and lesson workflow draft describe it, but no completed lesson evidence files were observed.
