from evaluator import get_user_score
from learner import create_lesson


task = "How do I learn Python?"

response = """
Start with Python basics such as variables,
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

print("\nYour score:", score)

print("\nLesson learned:")
print(lesson)