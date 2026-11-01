# 04 · Running Sum
# Write your answer inside solve(), then run this file.


def solve(nums: list[int]) -> list[int]:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([1, 2, 3, 4])
print("✅" if result == [1, 3, 6, 10] else "❌", 'solve([1, 2, 3, 4])', "->", result, "| expected [1, 3, 6, 10]")

result = solve([3, 1, 2, 10, 1])
print("✅" if result == [3, 4, 6, 16, 17] else "❌", 'solve([3, 1, 2, 10, 1])', "->", result, "| expected [3, 4, 6, 16, 17]")

result = solve([5])
print("✅" if result == [5] else "❌", 'solve([5])', "->", result, "| expected [5]")

result = solve([-1, -2, 3])
print("✅" if result == [-1, -3, 0] else "❌", 'solve([-1, -2, 3])', "->", result, "| expected [-1, -3, 0]")
