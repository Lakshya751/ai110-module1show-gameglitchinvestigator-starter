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

- [x] **The game's purpose:** It's a number guessing game. The computer picks a secret number inside a range (the range depends on the difficulty you choose), and you keep guessing until you get it. After each guess it tells you if you're too high or too low, and you have a limited number of attempts.

- [x] **Bugs I found:**
  - The hints were wrong. No matter what I guessed, it kept telling me to "Go Lower," even when my guess was already above the secret. Two things were causing this: the high/low messages were swapped, and the code was secretly turning the secret number into text on every other turn, which broke the comparison.
  - The score didn't make sense. When I guessed wrong, sometimes it took away points and sometimes it actually gave me points, depending on the attempt number.
  - The instructions always said "Guess a number between 1 and 100" even when I picked Easy mode, where the real range is 1 to 20.
  - Bonus: the "New Game" button didn't fully reset things and ignored the difficulty range.

- [x] **Fixes I applied:**
  - Moved the game rules (`check_guess`, `parse_guess`, `update_score`, `get_range_for_difficulty`) out of `app.py` and into `logic_utils.py` so they're separate from the UI and easier to test.
  - Fixed `check_guess` so it compares real numbers and returns the right "Too High" / "Too Low" outcome, and made `app.py` show the matching hint.
  - Fixed `update_score` so a wrong guess always costs the same amount instead of randomly adding points.
  - Made the on-screen range use the actual difficulty range, and made "New Game" reset the score, status, history, and pick a secret from the correct range.

## 📸 Demo Walkthrough

Here's how the fixed game plays from start to finish (using Normal mode, range 1–100):

1. You start the game. It says "Guess a number between 1 and 100" and shows how many attempts you have left.
2. You type 40 and hit Submit. The secret is 63, so it correctly says "📈 Go HIGHER!"
3. You try 80. Now you're above the secret, so it correctly says "📉 Go LOWER!"
4. Each wrong guess takes 5 points off your score in the same, predictable way (you can watch the score in the Developer Debug Info box).
5. You guess 63. The game shows balloons, says "🎉 Correct!", reveals the secret, and shows your final score.
6. If you switch the difficulty in the sidebar (say to Easy), the instructions update to the correct range (1 to 20), and clicking "New Game" starts a fresh round with a reset score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: .../ai110-module1show-gameglitchinvestigator-starter
collected 6 items

tests/test_game_logic.py ......                                          [100%]

============================== 6 passed in 0.00s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
