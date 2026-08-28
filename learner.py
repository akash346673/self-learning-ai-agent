def create_lesson(task, response, score):
    """Create a lesson based on user feedback."""

    if score >= 4:
        return (
            "The response was successful. "
            "Use a similar clear and helpful approach "
            "for related tasks."
        )

    elif score == 3:
        return (
            "The response was acceptable, but it could be "
            "more specific, clear, and useful."
        )

    else:
        return (
            "The response was not successful. "
            "Try a different approach and provide a more "
            "accurate and relevant answer."
        )