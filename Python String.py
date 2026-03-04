# ==========================================
# STRING OPERATIONS (FROM IMAGE 3)
# ==========================================

# 1. Count how many vowels are there in a string
text1 = input("1. Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text1 if char in vowels)
print(f"   Total Vowels: {count}")


# 2. Manual functions for Lower, Upper, and Toggle case (Without built-in functions)
def manual_lower(s):
    res = ""
    for c in s:
        if 'A' <= c <= 'Z': res += chr(ord(c) + 32)
        else: res += c
    return res

def manual_upper(s):
    res = ""
    for c in s:
        if 'a' <= c <= 'z': res += chr(ord(c) - 32)
        else: res += c
    return res

def manual_toggle(s):
    res = ""
    for c in s:
        if 'a' <= c <= 'z': res += chr(ord(c) - 32)
        elif 'A' <= c <= 'Z': res += chr(ord(c) + 32)
        else: res += c
    return res

text2 = "Python PROG"
print(f"\n2. Original: {text2}")
print(f"   Lower: {manual_lower(text2)}, Upper: {manual_upper(text2)}, Toggle: {manual_toggle(text2)}")


# 3. Access elements in Forward and Reverse order using while loop
text3 = "Python"
print("\n3. Forward Order: ", end="")
i = 0
while i < len(text3):
    print(text3[i], end=" ")
    i += 1

print("\n   Reverse Order: ", end="")
i = len(text3) - 1
while i >= 0:
    print(text3[i], end=" ")
    i -= 1
print()


# 4. Print First, Last, and Middle character
text4 = input("\n4. Enter a string: ")
first = text4[0]
last = text4[-1]
middle = text4[len(text4)//2] if len(text4) % 2 != 0 else "N/A (Even length)"
print(f"   First: {first}, Last: {last}, Middle: {middle}")


# 5. Slicing with "PDEU College"
s = "PDEU College"
print(f"\n5. Extract 'PDEU': {s[:4]}")
print(f"   Extract 'College': {s[5:]}")
print(f"   Extract 'U Col': {s[3:8]}")
print(f"   Reverse String: {s[::-1]}")


# 6. Concatenate two strings and repeat n times
str1 = input("\n6. Enter first string: ")
str2 = input("   Enter second string: ")
n = int(input("   Enter number of repetitions (n): "))
result = (str1 + str2) * n
print(f"   Result: {result}")


# 7. Print Total length, Count of vowels, and Count of consonants
text7 = input("\n7. Enter string: ")
t_len = len(text7)
v_count = sum(1 for c in text7 if c.lower() in "aeiou")
# Consonants count (alphabets that are not vowels)
c_count = sum(1 for c in text7 if c.isalpha() and c.lower() not in "aeiou")
print(f"   Length: {t_len}, Vowels: {v_count}, Consonants: {c_count}")
