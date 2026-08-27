from memory import add_experience, get_relevant_memories
from evaluator import get_user_score
from learner import create_lesson


task = "How do I learn Python?"

response = """
Start by learning Python basics such as variables,
data types, conditions, loops, and functions.
Practice regularly by building small projects.
"""

print("AGENT RESPONSE:")
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

print("\nNew lesson:")
print(lesson)

print("\nRelevant memories:")

results = get_relevant_memories(task)

for memory in results:
    print("\nTask:", memory["task"])
    print("Score:", memory["score"])
    print("Lesson:", memory["lesson"])