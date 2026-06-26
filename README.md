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

- [x] **The game's purpose:** It’s a number guessing game where the computer picks a secret number within a certain range, depending on the difficulty you choose. You keep guessing until you either get the number right or run out of attempts. After each guess, the game tells you whether your guess was too high or too low, so you can adjust your next guess.

- [x] **Bugs I found:**
  - The hints were not working correctly. No matter what I guessed, the game kept telling me to “Go Lower,” even when that didn’t make sense. I found out there were two problems behind this: the high and low messages were mixed up, and the code was also turning the secret number into text on every other turn, which messed up the comparison. 
  
  - The score was confusing too. When I guessed wrong, sometimes it took away points like it should, but other times it actually added points, depending on the attempt number.

   - The instructions did not match the difficulty setting. Even when I picked Easy mode, where the range should be 1 to 20, the game still said “Guess a number between 1 and 100.”
   
   - One extra issue I noticed was that the “New Game” button did not fully reset everything. It also did not always use the correct range for the difficulty I selected.

- [x] **Fixes I applied:**
- I moved the main game rules, like check_guess, parse_guess, update_score, and get_range_for_difficulty, out of app.py and into logic_utils.py. This made the code cleaner because the game logic was separated from the Streamlit UI, and it also made the functions easier to test.
- I fixed check_guess so it compares actual numbers instead of getting confused by text values. I also made sure app.py shows the correct hint, like “Too High” or “Too Low,” based on the result.
- I fixed update_score so wrong guesses always reduce the score in the same consistent way instead of sometimes adding points.
- I updated the on-screen instructions so the range changes based on the difficulty selected. I also fixed the “New Game” button so it resets the score, status, guess history, and secret number using the correct difficulty range.

## 📸 Demo Walkthrough

Here's how the fixed game plays from start to finish (using Normal mode, range 1–100):

- The game starts by telling the player to guess a number between 1 and 100, and it also shows how many attempts are left.
- I type 40 and click Submit. Since the secret number is 63, the game correctly tells me to go higher.
- Then I try 80. Since 80 is above the secret number, the game correctly tells me to go lower.
- Each wrong guess takes 5 points away from the score in a consistent way. I could also confirm this by watching the score in the Developer Debug Info box.
- When I guess 63, the game shows the celebration, says “Correct,” reveals the secret number, and shows the final score.
- If I switch the difficulty in the sidebar, like changing it to Easy, the instructions update to the correct range of 1 to 20. When I click “New Game,” it starts a fresh round with a reset score and a new secret number from the right range.

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
