# 02 · Count Target

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Counting

## 📝 Problem

Given an integer array `nums` and an integer `target`, return the **number of times** `target` appears in `nums`.

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [1, 2, 2, 3, 2], target = 2
Output: 3
Explanation: 2 appears at indices 1, 2 and 4.
```
**Example 2:**
```text
Input:  nums = [4, 5, 6], target = 7
Output: 0
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
python problems/02-count-target/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

Use a counter that starts at 0 and goes up by one every time you meet the target.

</details>

<details>
<summary><b>✅ Solution</b> (try it yourself first!)</summary>

<br>

```python
def solve(nums, target):
    count = 0
    for i in nums:
        if i == target:
            count += 1
    return count
```

**How it works.** One pass over the list. Every element equal to `target` adds 1 to the counter. If the target never appears, the counter simply stays at 0.

**Complexity:** Time **O(n)** · Space **O(1)**

</details>

---

[⬅️ Back to all problems](../../README.md)
