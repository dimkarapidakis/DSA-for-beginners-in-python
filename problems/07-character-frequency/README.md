# 07 · Character Frequency

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Hash maps

## 📝 Problem

Given a string `s`, return a `dict` where each key is a character of `s` and its value is the number of times that character appears.

You may not use `Counter` or `.count()`.

## 🔍 Examples

**Example 1:**
```text
Input:  s = "banana"
Output: {'b': 1, 'a': 3, 'n': 2}
```
**Example 2:**
```text
Input:  s = "abc"
Output: {'a': 1, 'b': 1, 'c': 1}
```

## 📏 Constraints

- `1 <= len(s) <= 10^5`
- `s` consists only of lowercase English letters.

## ✍️ Your turn

```python
def solve(s: str) -> dict:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/07-character-frequency/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

Start with an empty dict. For each character there are only two cases: you have seen it before, or this is the first time.

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
