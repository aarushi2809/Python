import math

# ==========================================
# GENERAL LOGIC & MATH (FROM IMAGE 4)
# ==========================================

# 1. Print all alphabets in upper case and in lower case
print("1. Alphabets:")
print("   Upper:", "".join([chr(i) for i in range(65, 91)]))
print("   Lower:", "".join([chr(i) for i in range(97, 123)]))


# 2. Print a multiplication table of a given number
num2 = int(input("\n2. Enter number for table: "))
for i in range(1, 11):
    print(f"   {num2} x {i} = {num2 * i}")


# 3. Count no. of alphabets and no. of digits in any given string
text3 = input("\n3. Enter a string: ")
alphas = sum(1 for c in text3 if c.isalpha())
digits = sum(1 for c in text3 if c.isdigit())
print(f"   Alphabets: {alphas}, Digits: {digits}")


# 4. Check Prime, Perfect, Armstrong, Palindrome, and Automorphic
def check_number(n):
    # Prime
    is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    # Perfect (Sum of divisors == n)
    is_perfect = sum(i for i in range(1, n) if n % i == 0) == n
    # Armstrong (153 = 1^3 + 5^3 + 3^3)
    s_n = str(n)
    is_armstrong = sum(int(d)**len(s_n) for d in s_n) == n
    # Palindrome
    is_palindrome = s_n == s_n[::-1]
    # Automorphic (n^2 ends with n, e.g., 25^2 = 625)
    is_automorphic = str(n**2).endswith(s_n)
    
    return f"Prime: {is_prime}, Perfect: {is_perfect}, Armstrong: {is_armstrong}, Palindrome: {is_palindrome}, Automorphic: {is_automorphic}"

num4 = int(input("\n4. Enter number to check properties: "))
print(f"   Results: {check_number(num4)}")


# 5. Generate all Pythagorean Triplets with side length <= 30
print("\n5. Pythagorean Triplets (<= 30):")
for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if a**2 + b**2 == c**2:
                print(f"   ({a}, {b}, {c})", end=" ")


# 6. Print 24 hours of day with suffixes
print("\n\n6. 24 Hours of Day:")
for h in range(24):
    if h == 0: suffix = "12 Midnight"
    elif h == 12: suffix = "12 Noon"
    elif h < 12: suffix = f"{h} AM"
    else: suffix = f"{h-12} PM"
    print(suffix, end=" | ")
print()


# 7. Print nCr and nPr
n = int(input("\n7. Enter n: "))
r = int(input("   Enter r: "))
n_fact = math.factorial(n)
r_fact = math.factorial(r)
nmr_fact = math.factorial(n-r)
print(f"   nPr: {n_fact // nmr_fact}")
print(f"   nCr: {n_fact // (r_fact * nmr_fact)}")


# 8. Print factorial of a given number
num8 = int(input("\n8. Enter number for factorial: "))
print(f"   Factorial: {math.factorial(num8)}")


# 9. Print N natural nos. in reverse
n9 = int(input("\n9. Enter N: "))
print(f"   Reverse natural numbers: ", end="")
for i in range(n9, 0, -1):
    print(i, end=" ")
