import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"


def generate_response(task, memories):
    """
    Generate an AI response using Ollama and
    lessons learned from previous experiences.
    """

    memory_context = ""

    if memories:
        memory_context = "\nRelevant previous experiences and lessons:\n"

        for index, memory in enumerate(memories, start=1):
            memory_context += f"""
Experience {index}:
Previous task: {memory["task"]}
Previous response: {memory["response"]}
Previous score: {memory["score"]}/5
Lesson learned: {memory["lesson"]}
"""

    prompt = f"""
You are a self-learning AI assistant.

Your goal is to answer the user's task accurately,
clearly, and helpfully.

Before answering, consider the lessons learned from
previous experiences.

IMPORTANT:
- Use previous lessons when they are relevant.
- If a previous response received a low score, avoid
  repeating the weaknesses described in its lesson.
- If a previous response received a high score, preserve
  the useful qualities described in its lesson.
- Do not blindly copy previous answers.
- Adapt the lessons to the current task.
- Do not mention the internal memory system unless asked.

{memory_context}

CURRENT USER TASK:
{task}

Now provide the best possible answer.
"""

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]