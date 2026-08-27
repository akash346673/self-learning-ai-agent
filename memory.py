import json
import os

MEMORY_FILE = "agent_memory.json"


def load_memory():
    """Load all saved experiences."""

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_memory(memory):
    """Save all experiences."""

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


def add_experience(task, response, score, lesson):
    """Save a new experience."""

    memory = load_memory()

    experience = {
        "task": task,
        "response": response,
        "score": score,
        "lesson": lesson
    }

    memory.append(experience)
    save_memory(memory)


def get_relevant_memories(task, limit=3):
    """Find previous experiences related to the current task."""

    memory = load_memory()

    task_words = set(task.lower().split())
    scored_memories = []

    for experience in memory:
        old_words = set(experience["task"].lower().split())

        similarity = len(task_words.intersection(old_words))

        scored_memories.append(
            (similarity, experience)
        )

    scored_memories.sort(
        key=lambda item: item[0],
        reverse=True
    )

    relevant_memories = []

    for similarity, experience in scored_memories[:limit]:
        if similarity > 0:
            relevant_memories.append(experience)

    return relevant_memories