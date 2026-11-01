# 03 · First Index of Target
# Write your answer inside solve(), then run this file.


def solve(nums: list[int], target: int) -> int:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([5, 8, 3, 8], 8)
print("✅" if result == 1 else "❌", 'solve([5, 8, 3, 8], 8)', "->", result, "| expected 1")

result = solve([5, 8, 3, 8], 7)
print("✅" if result == -1 else "❌", 'solve([5, 8, 3, 8], 7)', "->", result, "| expected -1")

result = solve([], 3)
print("✅" if result == -1 else "❌", 'solve([], 3)', "->", result, "| expected -1")

result = solve([2, 2, 2], 2)
print("✅" if result == 0 else "❌", 'solve([2, 2, 2], 2)', "->", result, "| expected 0")
