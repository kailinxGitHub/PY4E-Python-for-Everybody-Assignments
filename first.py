hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("oops, try numbers")
    quit()

x = 0
y = 0

if h > 40:
    x = 40*r
    y = (h-40)*(r*1.5)

print(x+y)
