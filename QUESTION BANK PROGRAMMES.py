
# 1 Remove prime numbers
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
def remove_primes(lst):
    return list(filter(lambda x: not is_prime(x), lst))
print(remove_primes(list(map(int,input().split()))))

# 2 Palindrome numbers
def palindrome_list(lst):
    return [x for x in lst if str(x)==str(x)[::-1]]
print(palindrome_list(list(map(int,input().split()))))

# 3 Reverse words
def reverse_words(s):
    return ' '.join(w[::-1] for w in s.split())
print(reverse_words(input()))

# 4 Vowels & consonants
def count_vc(s):
    v=sum(1 for c in s.lower() if c in "aeiou")
    c=sum(1 for c in s.lower() if c.isalpha() and c not in "aeiou")
    return v,c
print(count_vc(input()))

# 5 Prime factors
def prime_factors(n):
    f=[]; i=2
    while i<=n:
        if n%i==0:
            f.append(i); n//=i
        else: i+=1
    return f
print(prime_factors(int(input())))

# 6 Word frequency
def word_freq(s):
    d={}
    for w in s.split():
        d[w]=d.get(w,0)+1
    return d
print(word_freq(input()))

# 7 Remove duplicate words
def remove_dup_words(s):
    return list(dict.fromkeys(s.split()))
print(remove_dup_words(input()))

# 8 Divisible by k
def divisible(lst,k):
    return [x for x in lst if x%k==0]
lst=list(map(int,input().split())); k=int(input())
print(divisible(lst,k))

# 9 Factorial list (HOF)
from math import factorial
def fact_list(lst):
    return list(map(factorial,lst))
print(fact_list(list(map(int,input().split()))))

# 10 Common elements
def common(a,b):
    return list(set(a)&set(b))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(common(a,b))

# 11 Sum even
def sum_even(lst):
    return sum(x for x in lst if x%2==0)
print(sum_even(list(map(int,input().split()))))

# 12 Remove vowels
def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in "aeiou")
print(remove_vowels(input()))

# 13 Even digit numbers
def even_digits(lst):
    return [x for x in lst if len(str(abs(x)))%2==0]
print(even_digits(list(map(int,input().split()))))

# 14 Pair sum
def pairs(lst,t):
    return [(x,y) for i,x in enumerate(lst) for y in lst[i+1:] if x+y==t]
lst=list(map(int,input().split())); t=int(input())
print(pairs(lst,t))

# 15 Fibonacci recursive
def fib(n):
    return n if n<=1 else fib(n-1)+fib(n-2)
def fib_series(n):
    return [fib(i) for i in range(n)]
print(fib_series(int(input())))

# 16 Factorial recursive
def fact(n):
    return 1 if n<=1 else n*fact(n-1)
print(fact(int(input())))

# 17 Voting eligibility
def check_vote(age):
    return "Eligible to vote" if age>=18 else "Not eligible"
print(check_vote(int(input())))

# 18 Random numbers cube
import random
def random_cube():
    lst=[random.randint(1,10) for _ in range(10)]
    return lst,[x**3 for x in lst]
print(random_cube())

# 19 Slicing
def slicing(lst):
    return lst[:5], lst[-5:], lst[2:8], lst[::2]
print(slicing(list(range(1,11))))

# 20 Sum list
def total(lst):
    return sum(lst)
print(total(list(map(int,input().split()))))

# 21 Max Min
def max_min(lst):
    return max(lst),min(lst)
print(max_min(list(map(int,input().split()))))

# 22 Even odd count
def count_even_odd(lst):
    e=sum(1 for x in lst if x%2==0)
    return e,len(lst)-e
print(count_even_odd(list(map(int,input().split()))))

# 23 Remove duplicates list
def remove_dup_list(lst):
    return list(set(lst))
print(remove_dup_list(list(map(int,input().split()))))

# 24 Square list
def square(lst):
    return [x**2 for x in lst]
print(square(list(map(int,input().split()))))

# 25 Concatenate lists
def concat(a,b):
    return a+b
print(concat([1,2],[3,4]))

# 26 Frequency list
def freq(lst):
    d={}
    for x in lst:
        d[x]=d.get(x,0)+1
    return d
print(freq(list(map(int,input().split()))))

# 27 Sort list
def sort_list(lst):
    return sorted(lst)
print(sort_list(list(map(int,input().split()))))

# 28 Prime check
def check_prime(n):
    return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
print(check_prime(int(input())))

# 29 Count vowels
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
print(count_vowels(input()))

# 30 Power
def power(a,b):
    return a**b
print(power(int(input()),int(input())))

# 31 Celsius to Fahrenheit
def convert(c):
    return c*9/5+32
print(convert(float(input())))

# 32 Second largest
def second(lst):
    return sorted(set(lst))[-2]
print(second(list(map(int,input().split()))))

# 33 sum_avg
def sum_avg(lst):
    return sum(lst), sum(lst)/len(lst)
print(sum_avg(list(map(int,input().split()))))

# 34 filter() names
def filter_names(lst):
    return list(filter(lambda x: len(x)>5,lst))
print(filter_names(input().split()))

# 35 reduce() max
from functools import reduce
def max_reduce(lst):
    return reduce(lambda a,b:a if a>b else b,lst)
print(max_reduce(list(map(int,input().split()))))

# 36 Class: surface area & volume (cube example)
class Solid:
    def __init__(self,a): self.a=a
    def surface(self): return 6*self.a*self.a
    def volume(self): return self.a**3
s=Solid(int(input()))
print(s.surface(), s.volume())

# 37 Class: perimeter & area (circle)
class Shape:
    def __init__(self,r): self.r=r
    def perimeter(self): return 2*3.14*self.r
    def area(self): return 3.14*self.r*self.r
c=Shape(float(input()))
print(c.perimeter(), c.area())

# 38 Validate positive input
def get_positive():
    while True:
        try:
            n=int(input())
            if n>=0: return n
        except:
            pass
        print("Invalid input")
print(get_positive())

# 39 Copy file uppercase
def copy_upper(src,dst):
    with open(src) as f, open(dst,"w") as g:
        for line in f:
            g.write(line.upper())
copy_upper("a.txt","b.txt")

# 40 Merge files alternate
def merge_files(f1,f2,f3):
    a=open(f1).readlines()
    b=open(f2).readlines()
    with open(f3,"w") as f:
        for i in range(max(len(a),len(b))):
            if i<len(a): f.write(a[i])
            if i<len(b): f.write(b[i])
merge_files("a.txt","b.txt","c.txt")

# 41 Find prime numbers (HOF)
def primes_only(lst):
    return list(filter(is_prime,lst))
print(primes_only(list(map(int,input().split()))))

# 42 Character frequency
def char_freq(s):
    d={}
    for c in s:
        d[c]=d.get(c,0)+1
    return d
print(char_freq(input()))
