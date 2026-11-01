# 01 · Find Maximum
# Write your answer inside solve(), then run this file.


def solve(nums: list[int]) -> int:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([3, 7, 2, 9, 4])
print("✅" if result == 9 else "❌", 'solve([3, 7, 2, 9, 4])', "->", result, "| expected 9")

result = solve([-5, -2, -8])
print("✅" if result == -2 else "❌", 'solve([-5, -2, -8])', "->", result, "| expected -2")

result = solve([42])
print("✅" if result == 42 else "❌", 'solve([42])', "->", result, "| expected 42")

result = solve([1, 2, 3, 4, 5])
print("✅" if result == 5 else "❌", 'solve([1, 2, 3, 4, 5])', "->", result, "| expected 5")
