# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This project is a Streamlit number guessing game that started with several AI-generated bugs and design problems. The goal was to investigate the broken behavior, identify the bugs, refactor the code into testable helper functions, and verify the repairs with pytest and manual testing.

The main bugs I found were incorrect hint behavior, difficulty settings that did not match the displayed range, inconsistent New Game resets, unstable state during reruns, and tests that did not match the real function behavior. I also noticed that the original difficulty design made Hard mode feel less logical than Normal mode because the ranges did not scale cleanly.

To fix the project, I moved reusable game logic into `logic_utils.py`, corrected the hint and parsing logic, fixed the range display and reset behavior in `app.py`, improved state handling with Streamlit session state, and updated the tests so they matched the actual helper function outputs. I verified the work by running `pytest` successfully and checking the game manually in the browser.

## 📸 Demo

- Insert a screenshot of the fixed winning game here.
- Optional: insert a screenshot of the passing pytest results here if your instructor wants proof of the tests.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
