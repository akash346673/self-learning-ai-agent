import os

from dotenv import load_dotenv
from openai import OpenAI


# Load variables from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found. "
        "Check your .env file."
    )


# Create OpenAI client
client = OpenAI(api_key=api_key)


def generate_response(task, memories):
    """
    Generate an AI response using the user's task
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
Do not mention your internal memory system to the user unless asked.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text