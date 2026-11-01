# 06 · Valid Palindrome

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Two pointers · Strings

## 📝 Problem

Given a string `s`, return `True` if `s` reads the same from left to right as from right to left, otherwise return `False`.

You may not use `[::-1]`.

## 🔍 Examples

**Example 1:**
```text
Input:  s = "radar"
Output: True
```
**Example 2:**
```text
Input:  s = "hello"
Output: False
Explanation: Reversed, it reads "olleh".
```
**Example 3:**
```text
Input:  s = "a"
Output: True
```

## 📏 Constraints

- `1 <= len(s) <= 10^5`
- `s` consists only of lowercase English letters.

## ✍️ Your turn

```python
def solve(s: str) -> bool:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/06-valid-palindrome/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

This is problem 05 again, but instead of swapping you only compare. The moment one pair doesn't match, you already know the answer.

</details>

<!--
SOLUTION: not published yet. This comment is invisible on GitHub.
When you have solved it, delete these comment lines and fill in the block below.

<details>
<summary><b>✅ Solution</b> (try it yourself first!)</summary>

<br>

```python
paste your solution here
```

**How it works.** one or two sentences

**Complexity:** Time **O(?)** · Space **O(?)**

</details>
-->

> ✅ *Solution coming soon.*

---

[⬅️ Back to all problems](../../README.md)
