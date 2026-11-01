# 08 · Contains Duplicate
# Write your answer inside solve(), then run this file.


def solve(nums: list[int]) -> bool:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([1, 2, 3, 1])
print("✅" if result == True else "❌", 'solve([1, 2, 3, 1])', "->", result, "| expected True")

result = solve([1, 2, 3, 4])
print("✅" if result == False else "❌", 'solve([1, 2, 3, 4])', "->", result, "| expected False")

result = solve([7])
print("✅" if result == False else "❌", 'solve([7])', "->", result, "| expected False")

result = solve([-1, 5, -1])
print("✅" if result == True else "❌", 'solve([-1, 5, -1])', "->", result, "| expected True")
