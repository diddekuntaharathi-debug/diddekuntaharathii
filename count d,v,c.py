s = "python$4128"

v = 0
c = 0
d = 0

for ch in s:
    if ch.isdigit():
        d = d + 1
    elif ch.lower() in "aeiou":
        v = v + 1
    elif ch.isalpha():
        c = c + 1

print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
