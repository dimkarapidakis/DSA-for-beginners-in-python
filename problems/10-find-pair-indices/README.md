# 10 · Find Pair Indices

**Difficulty:** 🟡 Easy+ &nbsp;·&nbsp; **Topic:** Hash maps

## 📝 Problem

Given an integer array `nums` and an integer `target`, return the **indices** of the two elements that add up to `target`.

You may assume that there is **exactly one** solution, and you may not use the same element twice. You can return the answer in any order.

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```
**Example 2:**
```text
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: Not [0, 0], because there is only one 3.
```

## 📏 Constraints

- `2 <= len(nums) <= 10^4`
- `-10^9 <= nums[i], target <= 10^9`
- Exactly one valid answer exists.

**🚀 Follow-up:** Can you do it in O(n) using a `dict`? *(This is Two Sum.)*

## ✍️ Your turn

```python
def solve(nums: list[int], target: int) -> list[int]:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/10-find-pair-indices/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

Start from your answer to problem 09, but return the positions instead of `True`. For the follow-up: when you stand on a number, which *other* number would you need to have seen already?

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
