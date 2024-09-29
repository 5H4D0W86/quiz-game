def ask_question(question, answer):
#Ask the user a question and return True if they answer correctly.
    user_answer = input(question + "\n").strip().lower()
    if user_answer == answer.lower():
        print("Correct!\n")
        return True
    else:
        print("Incorrect! The correct answer was: " + answer + "\n")
        return False

def start_quiz():
#Start the quiz game.
    print("Welcome to the Quiz Game!\n")

    while True:
        score = 0

        # List of questions and answers
        questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What programming language is this script written in?", "answer": "python"},
            {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
            {"question": "What is the boiling point of water in Celsius?", "answer": "100"}
        ]

        # Loop through questions and ask each one
        for q in questions:
            if ask_question(q['question'], q['answer']):
                score += 1

        # End of the quiz
        print(f"Quiz complete! Your final score is: {score}/{len(questions)}")

        # Ask if the player wants to play again
        play_again = input("Do you wish to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    start_quiz()