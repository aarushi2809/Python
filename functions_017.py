
def count_lower_upper(s):
    result = {'uppercase': 0, 'lowercase': 0}
    for ch in s:
        if ch.isupper():
            result['uppercase'] += 1
        elif ch.islower():
            result['lowercase'] += 1
    return result

text = "Hello World! Python IS Fun."
print("Program 1: count_lower_upper()")
print(count_lower_upper(text))
# Output: {'uppercase': 4, 'lowercase': 15}
print()


def compute(n):
    n1  = n
    n2  = int(str(n) * 2)
    n3  = int(str(n) * 3)
    n4  = int(str(n) * 4)
    return n1 + n2 + n3 + n4

print("Program 2: compute()")
for digit in range(4, 8):
    print(f"  compute({digit}) = {compute(digit)}")
# e.g. compute(4) = 4 + 44 + 444 + 4444 = 4936
print()




def create_array(rows, cols, depth, init_val):
    return [[[init_val for _ in range(depth)]
              for _ in range(cols)]
              for _ in range(rows)]

print("Program 3: create_array()")
arr = create_array(2, 3, 4, 0)
print(f"  Shape: {len(arr)} x {len(arr[0])} x {len(arr[0][0])}")
print(f"  arr[0][0] = {arr[0][0]}")
print()




def sum_avg(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    return total, average

print("Program 4: sum_avg()")
total, avg = sum_avg(85, 90, 78, 92, 88)
print(f"  Total = {total}, Average = {avg}")
print()



def ispangram(s):
    alpha_set = set('abcdefghijklmnopqrstuvwxyz')
    return alpha_set <= set(s.lower())

print("Program 5: ispangram()")
s1 = "The quick brown fox jumps over the lazy dog"
s2 = "Crazy Fredrick bought many very exquisite opal jewels"
s3 = "Hello World"
print(f"  '{s1}' → {ispangram(s1)}")
print(f"  '{s2}' → {ispangram(s2)}")
print(f"  '{s3}' → {ispangram(s3)}")
print()



def power_tuples(n):
    return [(x, x**2, x**3) for x in range(1, n + 1)]

print("Program 6: power_tuples()")
print(power_tuples(5))
# [(1,1,1), (2,4,8), (3,9,27), (4,16,64), (5,25,125)]
print()




def ispalindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print("Program 7: ispalindrome()")
print(f"  'madam'          → {ispalindrome('madam')}")
print(f"  'Race a car'     → {ispalindrome('Race a car')}")
print(f"  'A man a plan a canal Panama' → {ispalindrome('A man a plan a canal Panama')}")
print()


def convert(s):
    words = s.split()
    unique_sorted = sorted(set(words))
    return " ".join(unique_sorted)

print("Program 8: convert()")
s = "banana apple mango apple orange banana grape"
print(f"  Input : '{s}'")
print(f"  Output: '{convert(s)}'")
print()




def count_alpha_digits(s):
    result = {'alphabets': 0, 'digits': 0}
    for ch in s:
        if ch.isalpha():
            result['alphabets'] += 1
        elif ch.isdigit():
            result['digits'] += 1
    return result

print("Program 9: count_alpha_digits()")
s = "Hello123 World456!"
print(f"  '{s}' → {count_alpha_digits(s)}")
print()


def frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items()))

print("Program 10: frequency()")
s = "the cat sat on the mat the cat"
print(f"  '{s}'")
print(f"  → {frequency(s)}")
print()


def prime_factors(n, factor=2):
    if n <= 1:
        return []
    if n % factor == 0:
        return [factor] + prime_factors(n // factor, factor)
    else:
        return prime_factors(n, factor + 1)

print("Program 11: prime_factors() [Recursive]")
for num in [12, 56, 97, 100]:
    print(f"  prime_factors({num}) = {prime_factors(num)}")
print()


def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)

print("Program 12: to_binary() [Recursive]")
for num in [0, 5, 10, 45, 255]:
    print(f"  to_binary({num}) = {to_binary(num)}")
print()




def count_vowels(s):
    if len(s) == 0:
        return 0
    return (1 if s[0].lower() in 'aeiou' else 0) + count_vowels(s[1:])

print("Program 13: count_vowels() [Recursive]")
print(f"  'Hello World'  → {count_vowels('Hello World')}")
print(f"  'Python'       → {count_vowels('Python')}")
print()


def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

print("Program 14: reverse_list() [Recursive]")
print(f"  [1,2,3,4,5] → {reverse_list([1, 2, 3, 4, 5])}")
print()




def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print("Program 15: power(a, b) [Recursive]")
print(f"  power(2, 10) = {power(2, 10)}")
print(f"  power(3, 5)  = {power(3, 5)}")
print()


def sanitize(lst):
    if len(lst) == 0:
        return []
    head = 0 if lst[0] < 0 else lst[0]
    return [head] + sanitize(lst[1:])

print("Program 16: sanitize() [Recursive]")
lst = [3, -5, 7, -2, 0, -9, 4]
print(f"  {lst} → {sanitize(lst)}")
print()




def list_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + list_sum(lst[1:])

def recursive_avg(lst):
    if len(lst) == 0:
        return 0
    return list_sum(lst) / len(lst)

print("Program 17: recursive_avg() [Recursive]")
lst = [10, 20, 30, 40, 50]
print(f"  avg of {lst} = {recursive_avg(lst)}")
print()




def create_list(lst1, lst2):
    return list(set(lst1) & set(lst2))

print("Program 18: create_list() - Intersection")
a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
print(f"  {a} ∩ {b} = {sorted(create_list(a, b))}")
print()



def str_length(s):
    if s == "":
        return 0
    return 1 + str_length(s[1:])

print("Program 19: str_length() [Recursive]")
print(f"  'Python' → {str_length('Python')}")
print(f"  'Hello World' → {str_length('Hello World')}")
print()



def fun():
    print("  fun executed")

def disp():
    print("  disp executed")

def msg():
    print("  msg executed")

print("FP Program 1: Functions stored in list and called in loop")
lst = [fun, disp, msg]
for f in lst:
    f()
print()




print("FP Program 2: Add corresponding elements using map + lambda")
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]
result = list(map(lambda a, b: a + b, list1, list2))
print(f"  {list1}")
print(f"+ {list2}")
print(f"= {result}")
print()


import random

print("FP Program 3: Random numbers and their squares")
random_nums = [random.randint(-15, 15) for _ in range(10)]
squares = list(map(lambda x: x * x, random_nums))
print(f"  Random : {random_nums}")
print(f"  Squares: {squares}")
print()




print("FP Program 4: Filter palindromes from a list")
lst = ['madam', 'Python', 'malayalam', 12321]

def is_palindrome_item(x):
    s = str(x)
    return s == s[::-1]

palindromes = list(filter(is_palindrome_item, lst))
print(f"  List      : {lst}")
print(f"  Palindromes: {palindromes}")
print()




print("FP Program 5: Filter faculty names with length > 8")
faculty = ["Ali", "Darshit", "Ramesh", "Elizabeth", "Priya", "Krishnaswamy", "Max"]
long_names = list(filter(lambda name: len(name) > 8, faculty))
print(f"  All names  : {faculty}")
print(f"  Long names : {long_names}")
print()


def greet():
    print("  Hello!")

def farewell():
    print("  Goodbye!")

def info():
    print("  Python Functional Programming")

print("FP Program 6 (Assignment): Functions in list, called in loop")
func_list = [greet, farewell, info]
for f in func_list:
    f()
print()




print("FP Program 7 (Assignment): map + lambda to add lists")
l1 = [1, 2, 3, 4, 5, 6]
l2 = [6, 5, 4, 3, 2, 1]
added = list(map(lambda a, b: a + b, l1, l2))
print(f"  {l1} + {l2} = {added}")
print()




print("FP Program 8 (Assignment): Random numbers and squares")
nums = [random.randint(-15, 15) for _ in range(10)]
sq = list(map(lambda x: x * x, nums))
print(f"  Random : {nums}")
print(f"  Squares: {sq}")
print()
