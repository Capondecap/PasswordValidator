inp = input("Enter txt file: ")
file = open(inp)
top = {}
for i in file:
    i = i.strip()
    part = i.split()
    for w in part:
        top[w] = top.get(w,0) + 1


newlist = []
for k,v in top.items():
    tup = (v,k)
    newlist.append(tup)

sorter = sorted(newlist,reverse=True)
for v,k in sorter[:5]:
    print(k,v)