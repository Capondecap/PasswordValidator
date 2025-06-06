# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
#  When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
fhand = open("romeo.txt")
unique = list()
for i in fhand:
    i.rstrip()
    h = i.split()
    for word in h:
        if word not in unique:
            unique.append(word)

unique.sort()
print(unique)