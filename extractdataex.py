import re

file = open("regex_sum_2153318.txt")
total = 0
for i in file:
    
    p = re.findall("[0-9]+", i)
    for num in p:
        total += int(num)
print(total) 