# 08 · Contains Duplicate

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Sets

## 📝 Problem

Given an integer array `nums`, return `True` if any value appears **at least twice**, and `False` if every element is distinct.

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [1, 2, 3, 1]
Output: True
Explanation: 1 appears at indices 0 and 3.
```
**Example 2:**
```text
Input:  nums = [1, 2, 3, 4]
Output: False
```

## 📏 Constraints

- `1 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

**🚀 Follow-up:** The two-loop solution is O(n²). Can you do it in O(n) using a `set`?

## ✍️ Your turn

```python
def solve(nums: list[int]) -> bool:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/08-contains-duplicate/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

First get any correct answer, even with two loops. Then think: what if you remembered every number you had already walked past?

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
