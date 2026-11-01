# 07 · Character Frequency
# Write your answer inside solve(), then run this file.


def solve(s: str) -> dict:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve("banana")
print("✅" if result == {'b': 1, 'a': 3, 'n': 2} else "❌", 'solve("banana")', "->", result, "| expected {'b': 1, 'a': 3, 'n': 2}")

result = solve("abc")
print("✅" if result == {'a': 1, 'b': 1, 'c': 1} else "❌", 'solve("abc")', "->", result, "| expected {'a': 1, 'b': 1, 'c': 1}")

result = solve("zzz")
print("✅" if result == {'z': 3} else "❌", 'solve("zzz")', "->", result, "| expected {'z': 3}")
