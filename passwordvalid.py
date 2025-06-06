# a,b,c,d = 0,0,0,0
# inp = input("Enter your password: ")
# uppercase = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
# lowercase = uppercase.lower()
# num = "123456789"
# specialchar = "!@#$%^&*()|?>:;~`"

# if len(inp)>10:
#     for i in inp:
#         if i in uppercase:
#             a+=1
#         if i in lowercase:
#             b+=1
#         if i in num:
#             c+=1
#         if i in specialchar:
#             d+=1
            
# if (a >=1 and b >=1 and c >=1 and d >=1 and a+b+c+d  >= len(inp)) :
#     print("Password valid: ", inp)


# else:
#     print("Invalid, Please include" 
#     " 10 or more characters\n" 
#     "1 or more numbers, special characters, uppercase, lowercase")
a = b = c = d = 0
inp = input("Enter your password: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
num = "1234567890"
specialchar = "!@#$%^&*()|?>:;~`"

if len(inp) >= 10:
    for i in inp:
        if i in uppercase:
            a += 1
        elif i in lowercase:
            b += 1
        elif i in num:
            c += 1
        elif i in specialchar:
            d += 1

    missing = []
    if a == 0:
        missing.append("uppercase letter")
    if b == 0:
        missing.append("lowercase letter")
    if c == 0:
        missing.append("number")
    if d == 0:
        missing.append("special character")

    if not missing:
        print("Password valid:", inp)
    else:
        print("Invalid. Please include:", ", ".join(missing))
else:
    print("Invalid. Password must be at least 10 characters long.")
