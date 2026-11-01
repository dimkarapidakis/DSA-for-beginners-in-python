# 09 · Pair Exists

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Brute force → Sets

## 📝 Problem

Given an integer array `nums` and an integer `target`, return `True` if there are **two elements at different indices** that add up to `target`, otherwise return `False`.

You may not use the same element twice.

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: True
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```
**Example 2:**
```text
Input:  nums = [3, 5], target = 6
Output: False
Explanation: 3 + 3 = 6, but there is only one 3.
```

## 📏 Constraints

- `2 <= len(nums) <= 10^4`
- `-10^9 <= nums[i], target <= 10^9`

## ✍️ Your turn

```python
def solve(nums: list[int], target: int) -> bool:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/09-pair-exists/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

Try every pair of positions `i` and `j`. How do you make sure `i` and `j` are never the same position, and that you don't check the same pair twice?

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
