#  Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted
inp = input("Enter file: ")
file = open(inp)

time = {}
for i in file:
    i = i.strip()
    if i.startswith("From "):
        part = i.split()
        if len(part) > 5:
            hour = part[5]
            pe = hour.split(":")[0]
            time[pe] = time.get(pe,0) + 1
print(time)
for d in sorted(time):
    print(d,time[d])