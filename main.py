from agent import generate_response
from memory import add_experience, get_relevant_memories
from evaluator import get_user_score
from learner import create_lesson


print("SELF-LEARNING AI AGENT")
print("-" * 30)

# Get task from user
task = input("\nEnter your task: ")

# Search relevant previous memories
memories = get_relevant_memories(task)

# Generate AI response
response = generate_response(task, memories)

print("\nAGENT RESPONSE:\n")
print(response)

# Get user feedback
score = get_user_score()

# Create lesson from feedback
lesson = create_lesson(
    task,
    response,
    score
)

# Save the experience
add_experience(
    task,
    response,
    score,
    lesson
)

print("\nLearning saved successfully!")

print("\nLesson learned:")
print(lesson)