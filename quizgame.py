import random
import sys

# Question bank - easily expandable
QUESTIONS = [
    {"question": "What is the capital of France?", "answer": ["paris"]},
    {"question": "What is 2 + 2?", "answer": ["4", "four"]},
    {"question": "What programming language is this script written in?", "answer": ["python"]},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": ["harper lee"]},
    {"question": "What is the boiling point of water in Celsius?", "answer": ["100", "100 degrees", "one hundred"]},
    {"question": "What is the largest planet in our solar system?", "answer": ["jupiter"]},
    {"question": "What year did the Titanic sink?", "answer": ["1912"]},
    {"question": "What is the chemical symbol for gold?", "answer": ["au"]},
    {"question": "How many continents are there?", "answer": ["7", "seven"]},
    {"question": "What is the square root of 64?", "answer": ["8", "eight"]}
]

class QuizGame:
    """A simple quiz game with multiple choice questions."""
    
    def __init__(self, questions=None):
        """Initialize the quiz game with a set of questions."""
        self.questions = questions or QUESTIONS.copy()
        self.score = 0
        self.total_questions = 0
    
    def check_answer(self, user_answer, correct_answers):
        """
        Check if the user's answer matches any of the correct answers.
        
        Args:
            user_answer (str): The user's input
            correct_answers (list): List of acceptable answers
            
        Returns:
            bool: True if answer is correct, False otherwise
        """
        if not user_answer:
            return False
            
        user_answer = user_answer.strip().lower()
        return any(user_answer == ans.lower() for ans in correct_answers)
    
    def ask_question(self, question_data, question_num, total_questions):
        """
        Ask a single question and return whether it was answered correctly.
        
        Args:
            question_data (dict): Dictionary containing question and answer
            question_num (int): Current question number
            total_questions (int): Total number of questions
            
        Returns:
            bool: True if answered correctly, False otherwise
        """
        print(f"Question {question_num}/{total_questions}")
        print("-" * 40)
        
        try:
            user_answer = input(f"{question_data['question']}\nYour answer: ").strip()
            
            if not user_answer:
                print("❌ Please enter an answer next time!\n")
                return False
                
            if self.check_answer(user_answer, question_data['answer']):
                print("✅ Correct!\n")
                return True
            else:
                # Show the first (primary) correct answer
                print(f"❌ Incorrect! The correct answer was: {question_data['answer'][0].title()}\n")
                return False
                
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            sys.exit()
        except EOFError:
            print("\n\nInput ended. Thanks for playing!")
            sys.exit()
    
    def get_yes_no_input(self, prompt):
        """
        Get a yes/no response from the user with flexible input handling.
        
        Args:
            prompt (str): The question to ask the user
            
        Returns:
            bool: True for yes, False for no
        """
        yes_responses = ['yes', 'y', '1', 'true', 'yep', 'yeah']
        
        while True:
            try:
                response = input(prompt).strip().lower()
                if response in yes_responses:
                    return True
                elif response in ['no', 'n', '0', 'false', 'nope']:
                    return False
                else:
                    print("Please enter 'yes' or 'no' (or 'y'/'n')")
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye!")
                return False
    
    def calculate_grade(self, score, total):
        """Calculate letter grade based on percentage."""
        if total == 0:
            return "N/A"
        
        percentage = (score / total) * 100
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"
    
    def display_results(self):
        """Display the final quiz results with detailed feedback."""
        percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        grade = self.calculate_grade(self.score, self.total_questions)
        
        print("=" * 50)
        print("🎯 QUIZ RESULTS")
        print("=" * 50)
        print(f"Final Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        print(f"Grade: {grade}")
        
        # Performance feedback
        if percentage >= 90:
            print("🏆 Excellent work! You're a quiz master!")
        elif percentage >= 80:
            print("🎉 Great job! Well done!")
        elif percentage >= 70:
            print("👍 Good effort! Keep it up!")
        elif percentage >= 60:
            print("📚 Not bad! A little more study and you'll improve!")
        else:
            print("💪 Keep practicing! You'll get better!")
        print()
    
    def run_quiz(self):
        """Run a complete quiz session."""
        # Create a copy and shuffle for randomization
        quiz_questions = self.questions.copy()
        random.shuffle(quiz_questions)
        
        self.score = 0
        self.total_questions = len(quiz_questions)
        
        print("🧠 Starting your quiz...\n")
        
        # Ask all questions
        for i, question_data in enumerate(quiz_questions, 1):
            if self.ask_question(question_data, i, self.total_questions):
                self.score += 1
        
        # Show results
        self.display_results()
    
    def start_game(self):
        """Start the main game loop."""
        print("🎮 Welcome to the Enhanced Quiz Game!")
        print("Answer the questions as accurately as possible.")
        print("Type your answers and press Enter.\n")
        
        # Ask about difficulty/number of questions
        if len(self.questions) > 5:
            if self.get_yes_no_input(f"Would you like to answer all {len(self.questions)} questions? (y/n): "):
                pass  # Use all questions
            else:
                try:
                    num_questions = int(input("How many questions would you like? (1-10): "))
                    num_questions = max(1, min(num_questions, len(self.questions)))
                    self.questions = random.sample(self.questions, num_questions)
                    print(f"Great! You'll get {num_questions} questions.\n")
                except ValueError:
                    print("Invalid input. Using 5 questions.\n")
                    self.questions = random.sample(self.questions, 5)
        
        # Main game loop
        while True:
            self.run_quiz()
            
            # Ask to play again
            if not self.get_yes_no_input("Would you like to play again? (y/n): "):
                print("Thanks for playing! 👋 Goodbye!")
                break
            else:
                print("\n" + "="*50 + "\n")

def main():
    """Main function to start the quiz game."""
    try:
        game = QuizGame()
        game.start_game()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please restart the game.")

if __name__ == "__main__":
    main()
