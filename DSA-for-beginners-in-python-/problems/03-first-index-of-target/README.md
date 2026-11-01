# 03 · First Index of Target

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Linear search

## 📝 Problem

Given an integer array `nums` and an integer `target`, return the **index of the first occurrence** of `target`. If `target` is not in the array, return `-1`.

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [5, 8, 3, 8], target = 8
Output: 1
Explanation: 8 appears at indices 1 and 3. The first one is 1.
```
**Example 2:**
```text
Input:  nums = [5, 8, 3, 8], target = 7
Output: -1
```

## 📏 Constraints

- `0 <= len(nums) <= 10^4`
- `-10^4 <= nums[i], target <= 10^4`

## ✍️ Your turn

```python
def solve(nums: list[int], target: int) -> int:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/03-first-index-of-target/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

You need the position, not just the value, so loop over the indices. And you can stop as soon as you find it.

</details>

<details>
<summary><b>✅ Solution</b> (try it yourself first!)</summary>

<br>

```python
def solve(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
```

**How it works.** Loop over indices with `range(len(nums))`. The first match returns immediately, so later duplicates are never reached. If the loop finishes without a match, the target is missing and we return `-1`.

**Complexity:** Time **O(n)** · Space **O(1)**

</details>

---

[⬅️ Back to all problems](../../README.md)
