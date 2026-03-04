import math

# --- 1. Largest and smallest values out of two ---
num1 = float(input("1. Enter first number: "))
num2 = float(input("   Enter second number: "))
print(f"   Largest: {max(num1, num2)}, Smallest: {min(num1, num2)}")

# --- 2. Largest and smallest values out of three ---
n1 = float(input("\n2. Enter first number: "))
n2 = float(input("   Enter second number: "))
n3 = float(input("   Enter third number: "))
print(f"   Largest: {max(n1, n2, n3)}, Smallest: {min(n1, n2, n3)}")

# --- 3. Odd or Even ---
val = int(input("\n3. Enter a number to check Odd/Even: "))
print("   Even" if val % 2 == 0 else "   Odd")

# --- 4. Divisible by 10 or not ---
div_num = int(input("\n4. Enter a number to check divisibility by 10: "))
print("   Divisible by 10" if div_num % 10 == 0 else "   Not divisible by 10")

# --- 5. Age check: Minor or Major ---
age = int(input("\n5. Enter age: "))
print("   Major" if age >= 18 else "   Minor")

# --- 6. Number of digits in a number ---
digit_num = abs(int(input("\n6. Enter a number: ")))
print(f"   Number of digits: {len(str(digit_num))}")

# --- 7. Leap Year Check ---
year = int(input("\n7. Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("   Leap Year")
else:
    print("   Not a Leap Year")

# --- 8. Triangle Validity (Sum of angles) ---
a1 = float(input("\n8. Enter angle 1: "))
a2 = float(input("   Enter angle 2: "))
a3 = float(input("   Enter angle 3: "))
print("   Valid Triangle" if (a1 + a2 + a3 == 180) else "   Invalid Triangle")

# --- 9. Absolute Value ---
abs_num = float(input("\n9. Enter a number: "))
print(f"   Absolute value: {abs(abs_num)}")

# --- 10. Area vs Perimeter of Rectangle ---
length = float(input("\n10. Enter length: "))
breadth = float(input("    Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
    print(f"    Area ({area}) is greater than Perimeter ({perimeter})")
else:
    print(f"    Area ({area}) is not greater than Perimeter ({perimeter})")

# --- 11. Three points on a straight line (Collinear) ---
x1, y1 = map(float, input("\n11. Enter x1, y1 (comma separated): ").split(','))
x2, y2 = map(float, input("    Enter x2, y2 (comma separated): ").split(','))
x3, y3 = map(float, input("    Enter x3, y3 (comma separated): ").split(','))
# Formula: (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1)
if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("    Points are on a straight line")
else:
    print("    Points are not on a straight line")

# --- 12. Point position relative to Circle ---
cx, cy = map(float, input("\n12. Enter Circle Center x, y (comma separated): ").split(','))
r = float(input("    Enter Radius: "))
px, py = map(float, input("    Enter Point to check x, y (comma separated): ").split(','))

# Distance formula: sqrt((px-cx)^2 + (py-cy)^2)
distance = math.sqrt(math.pow(px - cx, 2) + math.pow(py - cy, 2))

if distance < r:
    print("    Point is inside the circle")
elif distance == r:
    print("    Point is on the circle")
else:
    print("    Point is outside the circle")
