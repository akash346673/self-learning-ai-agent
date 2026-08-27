def get_user_score():
    """Ask the user to rate the response from 1 to 5."""

    while True:
        try:
            score = int(input("\nRate the response from 1 to 5: "))

            if 1 <= score <= 5:
                return score

            print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")