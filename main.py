from memory import add_experience, get_relevant_memories
from evaluator import get_user_score
from learner import create_lesson


task = input("Enter your task: ")

response = """
This is currently a test response.
Soon, the OpenAI agent will generate this response.
"""

print("\nAGENT RESPONSE:")
print(response)

score = get_user_score()

lesson = create_lesson(
    task,
    response,
    score
)

add_experience(
    task,
    response,
    score,
    lesson
)

print("\nLearning saved successfully!")

print("\nLesson learned:")
print(lesson)

print("\nRelevant memories:")

results = get_relevant_memories(task)

for memory in results:
    print("\nTask:", memory["task"])
    print("Score:", memory["score"])
    print("Lesson:", memory["lesson"])