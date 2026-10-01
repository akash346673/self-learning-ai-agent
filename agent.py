import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"


def generate_response(task, memories):
    """
    Generate an AI response using Ollama
    and relevant previous memories.
    """

    memory_context = ""

    if memories:
        memory_context = "\nPrevious relevant experiences:\n"

        for index, memory in enumerate(memories, start=1):
            memory_context += f"""
Experience {index}:
Task: {memory["task"]}
Response: {memory["response"]}
Score: {memory["score"]}
Lesson: {memory["lesson"]}
"""

    prompt = f"""
You are a helpful self-learning AI assistant.

Answer the user's task clearly, accurately, and helpfully.

USER TASK:
{task}

{memory_context}

Use previous experiences and lessons only when they are relevant.
Do not mention your internal memory system unless the user asks about it.
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