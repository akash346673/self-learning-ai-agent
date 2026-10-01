import json
import os
import re

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


def tokenize(text):
    """Convert text into useful lowercase words."""

    return set(
        re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    )


def calculate_similarity(task, previous_task):
    """Calculate simple word-based similarity."""

    task_words = tokenize(task)
    previous_words = tokenize(previous_task)

    if not task_words or not previous_words:
        return 0

    common_words = task_words.intersection(previous_words)

    return len(common_words) / len(task_words)


def get_relevant_memories(task, limit=3):
    """Find the most relevant previous experiences."""

    memory = load_memory()

    scored_memories = []

    for experience in memory:
        similarity = calculate_similarity(
            task,
            experience["task"]
        )

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