# 01 · Find Maximum

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Linear scan

## 📝 Problem

Given an integer array `nums`, return the **largest** element in the array.

You may not use the built-in `max()` function.

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [3, 7, 2, 9, 4]
Output: 9
```
**Example 2:**
```text
Input:  nums = [-5, -2, -8]
Output: -2
Explanation: The largest negative number is the one closest to 0.
```

## 📏 Constraints

- `1 <= len(nums) <= 10^4`
- `-10^4 <= nums[i] <= 10^4`

## ✍️ Your turn

```python
def solve(nums: list[int]) -> int:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/01-find-maximum/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

Keep one variable that remembers the biggest number you have seen so far. What should it start as? (Careful: starting at 0 breaks Example 2.)

</details>

<details>
<summary><b>✅ Solution</b> (try it yourself first!)</summary>

<br>

```python
def solve(nums):
    biggest = nums[0]

    for i in nums:
        if i > biggest:
            biggest = i

    return biggest
```

**How it works.** Start with the first element as the current best, walk through the list once, and replace the best whenever a bigger number appears. Starting from `nums[0]` instead of `0` is what makes negative arrays work.

**Complexity:** Time **O(n)** · Space **O(1)**

</details>

---

[⬅️ Back to all problems](../../README.md)
