day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

# 1. Visitors who visited both days
both_days = day1.intersection(day2)
print("Visited both days:", both_days)

# 2. Visitors who visited only one day
one_day = day1.symmetric_difference(day2)
print("Visited only one day:", one_day)

# 3. Total unique visitors
total_visitors = day1.union(day2)
print("Total unique visitors:", total_visitors)

lst = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(lst))
print("List after removing duplicates:", unique_list)


s1 = {'Math', 'Physics', 'Chemistry'}
s2 = {'Physics', 'Biology', 'Math'}

# 1. Common subjects
common = s1.intersection(s2)
print("Common subjects:", common)

# 2. Subjects only first student
only_s1 = s1.difference(s2)
print("Only first student:", only_s1)

# 3. Subjects only second student
only_s2 = s2.difference(s1)
print("Only second student:", only_s2)

# 4. Total unique subjects
total_unique = s1.union(s2)
print("Total unique subjects:", total_unique)
