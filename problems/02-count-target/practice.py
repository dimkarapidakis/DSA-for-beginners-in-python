# 02 · Count Target
# Write your answer inside solve(), then run this file.


def solve(nums: list[int], target: int) -> int:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([1, 2, 2, 3, 2], 2)
print("✅" if result == 3 else "❌", 'solve([1, 2, 2, 3, 2], 2)', "->", result, "| expected 3")

result = solve([4, 5, 6], 7)
print("✅" if result == 0 else "❌", 'solve([4, 5, 6], 7)', "->", result, "| expected 0")

result = solve([], 1)
print("✅" if result == 0 else "❌", 'solve([], 1)', "->", result, "| expected 0")

result = solve([9, 9, 9], 9)
print("✅" if result == 3 else "❌", 'solve([9, 9, 9], 9)', "->", result, "| expected 3")
