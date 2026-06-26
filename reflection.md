# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it looked normal at first. There was a title, a difficulty picker, and a place to type in my guess, so nothing seemed obviously wrong right away. But once I actually started playing, the hints didn’t make sense. No matter what number I entered, the game kept telling me to “Go Lower,” even when I guessed 1, which should not happen in a 1 to 100 range. I also noticed that the score was acting weird because sometimes a wrong guess made me lose points, but other times it added points, and the game still said “between 1 and 100” even after I switched to Easy mode.

Two concrete bugs I noticed right away:
- The hints were wrong or backwards, because the direction it gave me didn’t match my guess.
- The score was not consistent, because a wrong guess could either lose points or gain points.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 90 when the secret was 50 | Hint should say "Too High" / go lower | It told me to "Go Lower" (wrong direction) | none |
| Made several wrong guesses in a row | Score should change consistently | Score bounced up and down (sometimes +5, sometimes -5 for being wrong) | none |
| Switched difficulty to Easy and read the instructions | Should say "Guess a number between 1 and 20" | Still said "between 1 and 100" | none |

---

## 2. How did you use AI as a teammate?

I used an AI coding assistant inside VS Code to help me understand what was going wrong in the code and to talk through the fixes. The most helpful thing it noticed was that the secret number was being changed into text using str(...) on every other turn. That explained why the comparison between my guess and the secret number was breaking and why the hints were acting strange. I didn’t just accept that answer right away, though. I removed that line, played the game again with the Developer Debug Info open, and then the hints finally matched the guesses, so I knew that part was actually fixed.

One thing that confused me at first was that the project hints, and honestly my own first guess too, made it seem like the secret number was resetting every time I clicked Submit. I spent a little time looking into that, but when I watched the Secret value in the Developer Debug Info box, I saw that it was staying the same between guesses. So the real issue was not the secret number resetting. It was mostly the type conversion and the high/low messages being mixed up. That taught me that AI can point me in the right direction, but I still need to check the behavior myself instead of trusting the first explanation.
---

## 3. Debugging and testing your fixes

I decided a bug was fixed by doing two things: running pytest and also playing the game myself with the Developer Debug Info open. I wanted to actually see that the secret number, the guess, and the hint all matched correctly instead of just assuming the code was fine. One test I wrote was test_wrong_guess_is_consistent, which checks that a “Too High” guess on attempt 2 and attempt 3 both lose the same 5 points. Before the fix, one of those attempts would add points instead, so this test directly caught the old score problem. AI helped me think of testing both an even and odd attempt number, which was useful because that was exactly where the score bug was happening.


---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit re-runs the whole script every time you interact with the app, like when you click a button or enter something. It’s kind of like the page refreshes from the top each time. Because of that, regular variables don’t always keep their values the way I expected them to. st.session_state is what lets the app remember things between clicks, like the secret number, the score, and the number of attempts. So if something needs to stay saved while the user is playing, it should be stored in session state instead of only being kept as a normal variable.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is making small commits with clear messages and running tests before each commit. It made the project feel less messy because I could see exactly what changed at each step. Next time, I would like to write a test as soon as I find a bug, before I fix it, so I can actually see the test fail first and then pass after the fix. This project also changed how I think about AI-generated code. It can sound confident and look correct, but it can still be wrong, so I need to test it and confirm it myself before trusting it.
