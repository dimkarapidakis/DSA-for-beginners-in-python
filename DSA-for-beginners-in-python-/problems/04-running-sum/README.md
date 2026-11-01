# 04 · Running Sum

**Difficulty:** 🟢 Easy &nbsp;·&nbsp; **Topic:** Prefix sums

## 📝 Problem

Given an integer array `nums`, return an array where each position `i` contains the sum of all elements from index `0` up to and including index `i`.

That is: `result[i] = nums[0] + nums[1] + ... + nums[i]`

## 🔍 Examples

**Example 1:**
```text
Input:  nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: [1, 1+2, 1+2+3, 1+2+3+4]
```
**Example 2:**
```text
Input:  nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
```

## 📏 Constraints

- `1 <= len(nums) <= 1000`
- `-10^6 <= nums[i] <= 10^6`

**🚀 Follow-up:** Can you solve it in O(n)?

## ✍️ Your turn

```python
def solve(nums: list[int]) -> list[int]:
```

Open [`practice.py`](practice.py), write your code inside `solve()`, and run:

```bash
python problems/04-running-sum/practice.py
```

<details>
<summary><b>💡 Hint</b> (click to open)</summary>

<br>

You don't need to add everything again at each position. `result[i]` is just `result[i-1] + nums[i]`.

</details>

<details>
<summary><b>✅ Solution</b> (try it yourself first!)</summary>

<br>

```python
def solve(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums
```

**How it works.** Each position builds on the one before it: once `nums[i-1]` already holds the running total, adding `nums[i]` to it gives the next total. The loop starts at 1 because the first element is already its own sum.

Note: this version changes `nums` in place, so the original list is overwritten.

**Complexity:** Time **O(n)** · Space **O(1)** extra

</details>

---

[⬅️ Back to all problems](../../README.md)
