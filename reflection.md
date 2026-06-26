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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
