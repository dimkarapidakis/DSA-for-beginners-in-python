# 10 · Find Pair Indices
# Write your answer inside solve(), then run this file.


def solve(nums: list[int], target: int) -> list[int]:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve([2, 7, 11, 15], 9)
print("✅" if result is not None and sorted(result) == [0, 1] else "❌", 'solve([2, 7, 11, 15], 9)', "->", result, "| expected [0, 1] (any order)")

result = solve([3, 2, 4], 6)
print("✅" if result is not None and sorted(result) == [1, 2] else "❌", 'solve([3, 2, 4], 6)', "->", result, "| expected [1, 2] (any order)")

result = solve([3, 3], 6)
print("✅" if result is not None and sorted(result) == [0, 1] else "❌", 'solve([3, 3], 6)', "->", result, "| expected [0, 1] (any order)")

result = solve([-1, 8, 4, 1], 0)
print("✅" if result is not None and sorted(result) == [0, 3] else "❌", 'solve([-1, 8, 4, 1], 0)', "->", result, "| expected [0, 3] (any order)")
