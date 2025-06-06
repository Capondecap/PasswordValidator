def computepay(h, r):
    print((40*r)+((h-40)*(r*1.5)))
    

hrs = input("Enter Hours:")
rts = input("Enter rates:")
h = float(hrs)
r = float(rts)

p = computepay(h, r)
print("Pay", p)