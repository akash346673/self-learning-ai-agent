# Self-Learning AI Agent

A feedback-driven self-learning AI agent built with Python and a
local Ollama language model.

The agent generates responses, collects user feedback, stores previous
experiences, retrieves relevant memories, and uses lessons from previous
interactions to influence future responses.

The project is also developed using Agile methodologies with GitHub
Issues and GitHub Projects using a Kanban workflow.

---

## Project Overview

Traditional AI applications generally generate a response and stop.

This project adds a feedback and memory loop:

User Task
    ↓
Retrieve Relevant Experiences
    ↓
Generate AI Response
    ↓
User Feedback
    ↓
Create Lesson
    ↓
Store Experience
    ↓
Use Lesson in Future Tasks

The underlying language model is not retrained. Instead, the agent
learns through persistent memory, feedback, and contextual prompting.

---

## Objectives

- Generate AI responses using a local language model.
- Store previous interactions.
- Collect user feedback.
- Convert feedback into reusable lessons.
- Retrieve relevant previous experiences.
- Use previous lessons when generating future responses.
- Track learning statistics.
- Develop the project incrementally using Agile practices.

---

## Technologies Used

- Python
- Ollama
- Qwen 2.5 3B
- JSON-based persistent memory
- Git
- GitHub
- GitHub Issues
- GitHub Projects
- Kanban workflow

---

## System Architecture

```text
                    ┌─────────────────┐
                    │     User        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    main.py      │
                    │ Application Flow│
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
      ┌───────────────┐             ┌────────────────┐
      │   memory.py   │             │    agent.py    │
      │ Memory Search │             │ Ollama / LLM   │
      └───────┬───────┘             └───────┬────────┘
              │                             │
              └──────────────┬──────────────┘
                             ▼
                    ┌─────────────────┐
                    │   AI Response   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  evaluator.py   │
                    │ User Feedback   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   learner.py    │
                    │ Create Lesson   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ agent_memory.json│
                    │ Persistent Memory│
                    └─────────────────┘


self-learning-ai-agent/
│
├── agent.py
├── evaluator.py
├── learner.py
├── memory.py
├── stats.py
├── main.py
│
├── agent_memory.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── AGILE_BACKLOG.md
├── SPRINT_PLAN.md
└── RETROSPECTIVE.md
