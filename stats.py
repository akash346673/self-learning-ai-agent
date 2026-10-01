from memory import load_memory


def calculate_stats():
    """Calculate learning statistics from saved experiences."""

    memory = load_memory()

    if not memory:
        return {
            "total_experiences": 0,
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0,
            "successful_responses": 0,
            "needs_improvement": 0,
        }

    scores = [
        experience["score"]
        for experience in memory
    ]

    successful_responses = sum(
        1 for score in scores if score >= 4
    )

    needs_improvement = sum(
        1 for score in scores if score <= 3
    )

    return {
        "total_experiences": len(scores),
        "average_score": round(sum(scores) / len(scores), 2),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "successful_responses": successful_responses,
        "needs_improvement": needs_improvement,
    }


def display_stats():
    """Display learning statistics."""

    stats = calculate_stats()

    print("\nLEARNING STATISTICS")
    print("-" * 30)

    print(
        f"Total experiences: "
        f"{stats['total_experiences']}"
    )

    print(
        f"Average score: "
        f"{stats['average_score']}/5"
    )

    print(
        f"Highest score: "
        f"{stats['highest_score']}/5"
    )

    print(
        f"Lowest score: "
        f"{stats['lowest_score']}/5"
    )

    print(
        f"Successful responses: "
        f"{stats['successful_responses']}"
    )

    print(
        f"Needs improvement: "
        f"{stats['needs_improvement']}"
    )