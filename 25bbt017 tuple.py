###prbl 1
##name=["Riya",("Arjun",),"Sneha",("Kabir",),"Aarushi",("Baburao",)]
##boys=0
##girls=0
##for ele in name:
##    if isinstance(ele,tuple):
##        boys+=1
##    else:
##        girls+=1
##
##print("number of boys:",boys)
##print("number of girls:",girls)

#prbl 2
##students=[
##    (101, "Arjun", 18),
##    (102, "Riya", 19),
##    (103, "Aarushi", 18),
##    (104, "Sneha", 20)
##
##    ]
##roll_list=[]
##name_list=[]
##age_list=[]
##
##for student in students:
##    roll_list.append(student[0])
##    name_list.append(student[1])
##    age_list.append(student[2])
##
##print("roll nos.:", roll_list)
##print("names:",name_list)
##print("ages:",age_list)

#prbl 3
##from datetime import date
##date1=(10, 2, 2024)
##date2=(15, 1, 2026)
##
##d1=date(date1[2], date1[1], date1[0])
##d2=date(date2[2], date2[1], date2[0])
##
##difference=abs((d2-d1).days)
##print("number of days between the two dates:",difference)

#prbl 4
# Creating list of tuples
##food = [
##    ("Burger", 120),
##    ("Pizza", 250),
##    ("Sandwich", 80),
##    ("Pasta", 200)
##]
##
### Sorting in descending order by price
##food.sort(key=lambda x: x[1], reverse=True)
##
### Displaying result
##print("Sorted list in descending order by price:")
##print(food)

#prbl 5
##data = [(1, 2), (), (3, 4), (), (5,), ()]
##
##new_list = []
##
##for t in data:
##    if t != ():
##        new_list.append(t)
##
##print("List after removing empty tuples:", new_list)

#prbl 6
##t = (10, 20, 30)
##
### Modify second element (20 → 50)
##new_t = (t[0], 50, t[2])
##
##print("Original tuple:", t)
##print("Modified tuple:", new_t)

#prbl 7
##t = (10, 20, 30, 40)
##
##new_t = t[:1] + t[2:]
##
##print("Original tuple:", t)
##print("After deletion:", new_t)





