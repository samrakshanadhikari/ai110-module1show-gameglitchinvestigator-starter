# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran the game, the interface loaded, but several parts of the game did not behave the way I expected. First, when I tried to start a new game, I expected everything to reset cleanly, but it did not seem to restart the way I expected. Second, I expected the difficulty levels to feel consistent, but the attempts and range did not seem to match the level I selected. Third, I expected the instructions to match the actual game settings, but the displayed number range was confusing and did not always line up with the chosen difficulty.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used Codex as my AI teammate during this project. One correct suggestion was moving the reusable game logic out of `app.py` and into `logic_utils.py` so the guessing, parsing, and score behavior could be tested separately from the Streamlit UI. I verified that suggestion by checking the updated imports, running `pytest`, and seeing the helper functions work through the tests and the live app. One misleading suggestion was treating the old difficulty setup as acceptable even though the design made Hard mode smaller than Normal mode at one point. I verified that problem by running the app, comparing the ranges shown for each difficulty, and then changing the ranges so they scale more logically from Easy to Hard.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I decided a bug was really fixed only after the code behavior matched both the tests and the app in the browser. I ran `pytest` and confirmed that all 7 tests passed, including tests for guess results, decimal input rejection, score behavior, and difficulty scaling. I also ran the Streamlit app and manually checked that Easy showed `1 to 20`, Normal showed `1 to 50`, and Hard showed `1 to 100`, with the correct attempts displayed for each level. AI helped me identify where to place fixes and what to test, but I still verified each change by reading the code, running pytest, and checking the game manually.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
I learned that the original app was unstable because Streamlit reruns the script after user interactions, so values can reset if they are not stored properly. The secret number kept changing because the app logic did not consistently preserve all of the game state across those reruns and reset paths. I would explain Streamlit reruns to a friend as the whole script being re-executed after each interaction, while `st.session_state` acts like memory that keeps important values alive between reruns. The change that finally made the game stable was resetting and reusing the secret number, attempts, score, and history through session state instead of letting the app rebuild them inconsistently.

---

## 5. Looking ahead: your developer habits
One habit I want to reuse is turning repeated game behavior into testable helper functions before trying to debug everything in the UI. I also want to keep using small commits and branches so I can separate one bug fix from the next and avoid losing track of what changed. Next time I work with AI on a coding task, I would ask for narrower suggestions and verify them sooner instead of assuming the first design proposal is good enough. This project changed the way I think about AI-generated code because it showed me that AI can speed up debugging, but it still needs human judgment, testing, and design review before the code is trustworthy.
- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
