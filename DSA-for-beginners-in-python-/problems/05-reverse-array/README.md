# 05 · Reverse Array

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Two pointers

## 📝 Problem

Given an integer array `nums`, return the array **reversed**.

You may not use `[::-1]`, `reverse()` or `reversed()`.

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [1, 2, 3, 4]
Output: [4, 3, 2, 1]
```
**Example 2:**
```text
Input:  nums = [7]
Output: [7]
```

## 📏 Constraints

- `1 <= len(nums) <= 10^4`

**🚀 Follow-up:** Can you do it in-place, without creating a new list?

## ✍️ Your turn

```python
def solve(nums: list[int]) -> list[int]:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/05-reverse-array/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

Put one finger on the first element and one on the last. Swap them, move both fingers inward, repeat. When do you stop?

</details>

<details>
<summary><b>✅ Solution</b> (try it yourself first!)</summary>

<br>

```python
def solve(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
```

**How it works.** Two pointers start at both ends and swap their values, then walk toward the middle. The loop stops when they meet (`left < right` fails), so every pair is swapped exactly once.

Note: this reverses `nums` in place, without building a new list.

**Complexity:** Time **O(n)** · Space **O(1)**

</details>

---

[⬅️ Back to all problems](../../README.md)
