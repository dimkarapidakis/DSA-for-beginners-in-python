# 05 · Reverse Array
# Write your answer inside solve(), then run this file.


def solve(nums: list[int]) -> list[int]:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([1, 2, 3, 4])
print("✅" if result == [4, 3, 2, 1] else "❌", 'solve([1, 2, 3, 4])', "->", result, "| expected [4, 3, 2, 1]")

result = solve([7])
print("✅" if result == [7] else "❌", 'solve([7])', "->", result, "| expected [7]")

result = solve([1, 2, 3])
print("✅" if result == [3, 2, 1] else "❌", 'solve([1, 2, 3])', "->", result, "| expected [3, 2, 1]")

result = solve([5, 5, 1])
print("✅" if result == [1, 5, 5] else "❌", 'solve([5, 5, 1])', "->", result, "| expected [1, 5, 5]")
