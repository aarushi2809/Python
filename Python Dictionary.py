#1.
##dict1 = {'a': 1, 'b': 2}
##dict2 = {'c': 3, 'd': 4}
##dict3 = {'e': 5, 'f': 6}
##
### Using the unpacking operator (Python 3.5+)
##dict4 = {**dict1, **dict2, **dict3}
##
##print("Concatenated Dictionary:", dict4)

#2.
##my_dict = {}
##
##if not my_dict:
##    print("The dictionary is empty.")
##else:
##    print("The dictionary is not empty.")

#3.
# List of employee data: (Dept_No, Roll_No, Salary)
##employees = [
##    (101, 1, 50000), (101, 2, 60000),
##    (102, 3, 45000), (102, 4, 70000),
##    (101, 5, 55000)
##]
##
##stats = {}
##
##for dept, roll, salary in employees:
##    if dept not in stats:
##        stats[dept] = {'min': salary, 'max': salary}
##    else:
##        stats[dept]['min'] = min(stats[dept]['min'], salary)
##        stats[dept]['max'] = max(stats[dept]['max'], salary)
##
##for dept, val in stats.items():
##    print(f"Dept {dept}: Min Salary = {val['min']}, Max Salary = {val['max']}")
##
##    
###4.
##user_input = input("Enter a string: ")
##frequency = {}
##
##for char in user_input:
##    frequency[char] = frequency.get(char, 0) + 1
##
##print("Character Frequencies:", frequency)
##
##
###5.
##prices = {'apple': 0.5, 'banana': 0.2, 'milk': 2.5, 'bread': 1.5}
##quantities = {'apple': 6, 'banana': 10, 'milk': 1}
##
##total_bill = 0
##
##for item, qty in quantities.items():
##    if item in prices:
##        cost = qty * prices[item]
##        total_bill += cost
##        print(f"{item.capitalize()}: {qty} x ${prices[item]} = ${cost}")
##
##print("-" * 20)
##print(f"Total Bill: ${total_bill}")
