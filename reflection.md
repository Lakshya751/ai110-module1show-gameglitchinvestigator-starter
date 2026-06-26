# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game it looked normal — a title, a difficulty picker, and a box to type my guess. But once I started playing, the hints made no sense. For every input it says "Go Lower," so there has to be some problem. The range is between 1 to 100, but even when entering 1 it shows "Go Lower," so there is some glitch with the number — it's not taking the number or not recognizing it properly. I also noticed my score jumped up and down randomly when I guessed wrong, and the game always said "between 1 and 100" even after I switched to Easy mode (which should be 1 to 20).

Two concrete bugs I noticed right away:
- The hints were wrong/backwards — the direction it told me to go didn't match my guess.
- The score didn't behave consistently — sometimes a wrong guess lost points, sometimes it gained points.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 90 when the secret was 50 | Hint should say "Too High" / go lower | It told me to "Go Lower" (wrong direction) | none |
| Made several wrong guesses in a row | Score should change consistently | Score bounced up and down (sometimes +5, sometimes -5 for being wrong) | none |
| Switched difficulty to Easy and read the instructions | Should say "Guess a number between 1 and 20" | Still said "between 1 and 100" | none |

---

## 2. How did you use AI as a teammate?

I used an AI coding assistant inside VS Code to help me understand the code and walk through the fixes. The most helpful thing it got right was spotting that the secret number was being turned into text (`str(...)`) on every other turn, which is why comparing my guess to the secret kept breaking and the hints were always off. I checked this myself by removing that line and playing again with the Developer Debug Info open, and the hints finally matched my guesses, so I knew it was right.

One thing that was misleading at first: the project hints (and my early assumption) pointed me toward a "Streamlit state bug" where the secret number supposedly changed every time I clicked Submit. I spent a little time chasing that, but when I watched the Secret value in the Developer Debug Info box, it actually stayed the same between guesses — the real problem was the type conversion and the swapped high/low messages, not the secret resetting. So I learned not to take the first explanation at face value and to verify it against what the game actually did.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed in two ways: by running `pytest` and by playing the game with the Developer Debug Info open so I could see the secret and confirm the hint matched. I didn't want to trust the code just because it looked correct. One test I wrote was `test_wrong_guess_is_consistent`, which checks that a "Too High" guess on attempt 2 and on attempt 3 both lose the same 5 points. Before my fix, one of those would have added points instead, so this test directly catches the old score bug — and running it showed all 6 tests passing. AI helped me design this test by suggesting I check the same outcome on both an even and an odd attempt number, which is exactly the case that used to behave differently.

---

## 4. What did you learn about Streamlit and state?

Every time you click a button or type something, Streamlit re-runs the whole script from top to bottom, kind of like refreshing a web page. That means any normal variable gets wiped and created again from scratch on each click. `st.session_state` is like a backpack that survives the refresh — you put things like the secret number, the score, and the number of attempts inside it so they don't reset every time. So if you want something to be remembered between clicks, it has to live in session state instead of a regular variable.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is committing in small steps with clear messages and running the tests before each commit. It made it really easy to see what changed at each stage and I always knew the code still worked. One thing I'd do differently next time is write a quick test for a bug the moment I find it, before fixing it, so I can actually watch it go from failing to passing — this time I mostly fixed first and tested after. Overall this project changed how I think about AI-generated code: it can look clean and sound confident and still be quietly wrong, so I won't trust it until I've tested it and seen it work with my own eyes.
