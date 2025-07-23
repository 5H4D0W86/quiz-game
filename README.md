# 🧠 Quiz Game

A fun, interactive command-line quiz game built in Python that tests your general knowledge across various topics!

## 🎯 Features

- **🎲 Randomized Questions**: Questions appear in random order each game
- **✅ Flexible Answer Checking**: Multiple acceptable answers for each question (e.g., "4" or "four")
- **📊 Smart Scoring**: Get percentage scores, letter grades, and performance feedback
- **🎮 Customizable Length**: Choose how many questions you want to answer
- **🔄 Replay Option**: Play multiple rounds without restarting
- **💡 Progress Tracking**: See your progress with "Question X of Y" indicators
- **🎨 Enhanced UI**: Clean formatting with emojis and visual feedback
- **⚡ Error Handling**: Graceful handling of interruptions and invalid inputs

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation & Running
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/quiz-game.git
   cd quiz-game
   ```

2. Run the game:
   ```bash
   python quiz_game.py
   ```

3. Follow the on-screen prompts and enjoy!

## 🎮 How to Play

1. **Start the game** - Run the script and you'll see a welcome message
2. **Choose question count** - Decide how many questions you want (or play all available)
3. **Answer questions** - Type your answers and press Enter
4. **Get instant feedback** - See if you're right or wrong immediately
5. **View your results** - Get a detailed score breakdown with letter grade
6. **Play again** - Choose to start another round or quit

### Example Game Flow
```
🎮 Welcome to the Enhanced Quiz Game!
Answer the questions as accurately as possible.
Type your answers and press Enter.

Would you like to answer all 10 questions? (y/n): y

🧠 Starting your quiz...

Question 1/10
----------------------------------------
What is the capital of France?
Your answer: Paris
✅ Correct!

Question 2/10
----------------------------------------
What is 2 + 2?
Your answer: 4
✅ Correct!

[... more questions ...]

==================================================
🎯 QUIZ RESULTS
==================================================
Final Score: 8/10
Percentage: 80.0%
Grade: B
🎉 Great job! Well done!

Would you like to play again? (y/n): n
Thanks for playing! 👋 Goodbye!
```

## 📝 Question Bank

The game currently includes questions covering:
- **Geography** (capitals, countries)
- **Mathematics** (basic arithmetic, geometry)
- **Science** (chemistry, physics, astronomy)
- **Literature** (famous authors and works)
- **General Knowledge** (history, programming)

### Current Questions Include:
- Capital cities
- Basic math problems
- Science facts
- Historical events
- Programming concepts
- And more!

## 🛠️ Customization

### Adding New Questions
You can easily add new questions by editing the `QUESTIONS` list in the code:

```python
QUESTIONS = [
    {"question": "Your question here?", "answer": ["answer1", "answer2"]},
    # Add more questions...
]
```

**Tips for adding questions:**
- Include multiple acceptable answer formats in the answer list
- Keep answers simple and clear
- Use lowercase in the answer list (the game handles case conversion)

### Example Question Entry:
```python
{"question": "What is the largest ocean?", "answer": ["pacific", "pacific ocean"]}
```

## 🏗️ Code Structure

The game is built using object-oriented programming with the following key components:

- **`QuizGame` class**: Main game logic and state management
- **`check_answer()`**: Flexible answer validation
- **`ask_question()`**: Individual question handling with progress tracking
- **`display_results()`**: Comprehensive score reporting with grades
- **`get_yes_no_input()`**: Robust user input handling

## 🎯 Scoring System

| Percentage | Grade | Feedback |
|------------|-------|----------|
| 90-100% | A | 🏆 Excellent work! You're a quiz master! |
| 80-89% | B | 🎉 Great job! Well done! |
| 70-79% | C | 👍 Good effort! Keep it up! |
| 60-69% | D | 📚 Not bad! A little more study and you'll improve! |
| Below 60% | F | 💪 Keep practicing! You'll get better! |

## 🚀 Future Enhancements

Potential improvements for future versions:
- [ ] **Multiple Categories**: Separate question banks by topic (Science, History, Sports, etc.)
- [ ] **Difficulty Levels**: Easy, Medium, Hard question sets
- [ ] **Timed Mode**: Add optional time limits for questions
- [ ] **High Score Tracking**: Save and display best scores
- [ ] **Question Import**: Load questions from external files (JSON, CSV)
- [ ] **Multiplayer Mode**: Support for multiple players taking turns
- [ ] **Hints System**: Optional hints for difficult questions
- [ ] **Statistics**: Track performance over time

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Add Questions**: Submit new questions covering different topics
2. **Report Bugs**: Found an issue? Please report it
3. **Suggest Features**: Have ideas for improvements? Let me know
4. **Code Improvements**: Submit pull requests for enhancements

### How to Contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-questions`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add science questions'`)
5. Push to the branch (`git push origin feature/new-questions`)
6. Open a Pull Request

## 📋 Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎮 Have Fun!

Enjoy testing your knowledge and learning new facts. Challenge your friends and see who can get the highest score!

---

**Made with ❤️ and Python**

*If you enjoy this quiz game, please consider giving it a ⭐ on GitHub!*
