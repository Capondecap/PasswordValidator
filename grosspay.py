hrs = input("Enter Hours: ")
rts = input("Enter rates: ")
h = float(hrs)
r = float(rts)
normpay = 40*r
if h > 40:
    print(normpay+((h-40)*(1.5*r)))
else:
    print("no overtime hour ")