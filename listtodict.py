import re
file = open("mbox-short.txt","r")
# empty dict
count = {}
po = {}
# for loop the file
for lines in file:
   # deleting space
   lines = lines.strip()
   # check if the line starts with from: 
   if lines.startswith("From: "):
        #turn the txt into a list
        part = lines.split()
        # print out the list loop
        # print(part)
       #check if the list index is bigger than one as the list split format would follow From: email [From:[0], Email[1]]
        if len(part) > 1:
            #take only the email part
            email = part[1]
            # iterrate it by 1 everytime using get method, ex: count = {sdcdsc@dvs : 1}
            count[email] = count.get(email,0) + 1
            #now take the domain from email as email follow amcdskm@vsdvsd we want the last bit so split @ turns it to list [username[0],domain[1]]
            pe = email.split("@")
        #check if the list email format is bigger than one which usually is but safety
        if len(pe) > 1:
            #take only the domain part
            k = pe[1]
        #iterrate it
            po[k] = po.get(k,0) + 1
#print the dictionary in po once it has been calulcated
print(po.items())
#create none for loop through domain
a = None 
b =  None
#start domain count
print("domain count: ")
#for loop for domain
for w,c in po.items():
    #print the tuple of po emails dictionary
    print(w,c)
    #check if the a is none or c is bigger than max value of b, b = max, so if a value is placed in b than loop through list if a value of c is smaller than b then c remains false and loop 
    #next key value pair, a is always going to change even if it is false cause if the condition of c is true a will be changed if both is false than loop through next
    if a is None or c > b:
        a = w 
        b = c
#print the biggest domain once it has been looped
print("Biggest domain clone" ,a,b)
#same principle as domain
counts = None
word = None
for w,c in count.items():
    if word is None or c > counts:
        word = w 
        counts = c
print("Counts ", count)
print(word,counts)




