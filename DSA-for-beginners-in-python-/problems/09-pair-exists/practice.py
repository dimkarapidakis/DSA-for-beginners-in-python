# 09 · Pair Exists
# Write your answer inside solve(), then run this file.


def solve(nums: list[int], target: int) -> bool:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([2, 7, 11, 15], 9)
print("✅" if result == True else "❌", 'solve([2, 7, 11, 15], 9)', "->", result, "| expected True")

result = solve([3, 5], 6)
print("✅" if result == False else "❌", 'solve([3, 5], 6)', "->", result, "| expected False")

result = solve([3, 3], 6)
print("✅" if result == True else "❌", 'solve([3, 3], 6)', "->", result, "| expected True")

result = solve([1, 2, 3], 10)
print("✅" if result == False else "❌", 'solve([1, 2, 3], 10)', "->", result, "| expected False")
