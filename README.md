# π§© DSA for Beginners in Python

Short, beginner-friendly problems on arrays, strings and hash maps, to build the habit of **thinking in loops, indices, pointers and lookups** before moving on to harder data structures and algorithms.

Every problem has a ready-to-run practice file that checks your answer, a hint if you get stuck, and a hidden solution with an explanation.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Problems](https://img.shields.io/badge/problems-10-blue)
![Level](https://img.shields.io/badge/level-beginner-brightgreen)

---

## π€ How to use this repo

1. **Clone it**
   ```bash
   git clone https://github.com/dimkarapidakis/DSA-for-beginners-in-python.git
   cd DSA-for-beginners-in-python
   ```
2. **Pick a problem** from the table below and read its page.
3. **Open `practice.py`** in that folder and write your code inside `solve()`.
4. **Run it**
   ```bash
   python problems/01-find-maximum/practice.py
   ```
   Every β… is a passed test. Fix the β ones and run again.
5. **Stuck?** Open the π’΅ hint on the problem page. Still stuck after a real attempt? Open the β… solution.

> **Try before you peek.** You learn far more from 20 minutes of struggling than from 2 minutes of reading a solution.

---

## π“‹ Problems

| # | Problem | Difficulty | Topic | Solution |
|:-:|---|:-:|---|:-:|
| 01 | [Find Maximum](problems/01-find-maximum) | πΆ Easy | Linear scan | β… |
| 02 | [Count Target](problems/02-count-target) | πΆ Easy | Counting | β… |
| 03 | [First Index of Target](problems/03-first-index-of-target) | πΆ Easy | Linear search | β… |
| 04 | [Running Sum](problems/04-running-sum) | πΆ Easy | Prefix sums | β… |
| 05 | [Reverse Array](problems/05-reverse-array) | πΆ Easy | Two pointers | β… |
| 06 | [Valid Palindrome](problems/06-valid-palindrome) | πΆ Easy | Two pointers Β· Strings | π” |
| 07 | [Character Frequency](problems/07-character-frequency) | πΆ Easy | Hash maps | π” |
| 08 | [Contains Duplicate](problems/08-contains-duplicate) | πΆ Easy | Sets | π” |
| 09 | [Pair Exists](problems/09-pair-exists) | πΆ Easy | Brute force β†’ Sets | π” |
| 10 | [Find Pair Indices](problems/10-find-pair-indices) | π΅ Easy+ | Hash maps | π” |

β… = solution published Β· π” = coming soon. More problems are added regularly, so β­ star the repo to follow along.

---

## π“ Structure

```text
problems/
β””β”€β”€ 01-find-maximum/
    β”β”€β”€ README.md     β† problem, examples, constraints, hint and hidden solution
    β””β”€β”€ practice.py   β† write your answer here and run it
```

## π§  Rules of the game

- No built-ins that solve the whole problem for you (`max()`, `.count()`, `.index()`, `reversed()`, `[::-1]`, `Counter`β€¦), unless the problem says otherwise.
- Think about **edge cases**: one element, negative numbers, a target that isn't there, repeated values.
- After solving, ask yourself: *how many times does my loop run?* That is the time complexity. Then look at the π€ follow-up, if there is one.

