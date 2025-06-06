
fname = input("type in file name:  ")
try:
    file = open(fname)
except:
    print("File doesnt exist")
    quit()
count = 0
fread = file.read()
word = input("what word you want to find: ")
for i in fread.split():
    if i == word:
        print(count,i)
        count += 1
