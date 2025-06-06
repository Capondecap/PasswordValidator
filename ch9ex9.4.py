name = input("Enter file:")
file = open(name,"r")
count = None
word = None
dic = {}
for i in file:
    i =  i.strip()
    if i.startswith("From: "):
        part = i.split()
        email = part[1]
        if len(email) > 1:
            dic[email]= dic.get(email,0) + 1
            for w,c in dic.items():
                if word is None or c > count:
                    word = w
                    count = c
print(word,count)
