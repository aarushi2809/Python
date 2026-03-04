import random

# ==========================================
# LIST OPERATIONS (FROM IMAGE 5)
# ==========================================

# 1. Random Odd/Even Lists, Replace, Flatten, and Sort
print("--- 1. List Manipulation ---")
odd_list = [random.randrange(1, 100, 2) for _ in range(5)]
print(f"Initial Odd List: {odd_list}")

even_list = [random.randrange(2, 100, 2) for _ in range(4)]
print(f"Initial Even List: {even_list}")

# Replace the third element (index 2) with the even_list
odd_list[2] = even_list
print(f"List after replacement at index 2: {odd_list}")

# Flatten the list (convert nested list to flat list)
flat_list = []
for item in odd_list:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)
print(f"Flattened List: {flat_list}")

flat_list.sort()
print(f"Sorted Final List: {flat_list}")


# 2. Generate 20 random integers and find all positions of a user-input number
print("\n--- 2. Find Occurrences ---")
random_20 = [random.randint(1, 10) for _ in range(20)]
print(f"Generated List: {random_20}")
search_val = int(input("Enter number to find positions of: "))
positions = [i for i, val in enumerate(random_20) if val == search_val]
print(f"Positions of {search_val}: {positions if positions else 'Not found'}")


# 3. Generate 50 random numbers (1-30) and remove duplicates
print("\n--- 3. Remove Duplicates ---")
random_50 = [random.randint(1, 30) for _ in range(50)]
unique_list = list(set(random_50)) # Using set to remove duplicates
print(f"Original Count: {len(random_50)}, Unique Count: {len(unique_list)}")
print(f"Unique List: {unique_list}")


# 4. Separate 30 random numbers into Positive and Negative lists
print("\n--- 4. Split Positive/Negative ---")
random_30 = [random.randint(-50, 50) for _ in range(30)]
pos_list = [n for n in random_30 if n >= 0]
neg_list = [n for n in random_30 if n < 0]
print(f"Positive Numbers: {pos_list}")
print(f"Negative Numbers: {neg_list}")


# 5. Convert list of 5 strings to uppercase
print("\n--- 5. Strings to Uppercase ---")
strings = ["apple", "banana", "cherry", "date", "elderberry"]
uppercased = [s.upper() for s in strings]
print(f"Original: {strings}\nUppercased: {uppercased}")


# 6. Convert Fahrenheit list
