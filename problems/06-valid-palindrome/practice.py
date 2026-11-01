# 06 · Valid Palindrome
# Write your answer inside solve(), then run this file.


def solve(s: str) -> bool:
    # your code here
    pass


# ---- tests (no need to change anything below) ----

result = solve("radar")
print("✅" if result == True else "❌", 'solve("radar")', "->", result, "| expected True")

result = solve("hello")
print("✅" if result == False else "❌", 'solve("hello")', "->", result, "| expected False")

result = solve("a")
print("✅" if result == True else "❌", 'solve("a")', "->", result, "| expected True")

result = solve("abba")
print("✅" if result == True else "❌", 'solve("abba")', "->", result, "| expected True")

result = solve("ab")
print("✅" if result == False else "❌", 'solve("ab")', "->", result, "| expected False")
