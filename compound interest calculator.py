#compound interest calculator
principle=0
rate=0
time=0
while principle<=0:
    principle=int(input("Enter the principle:"))
    if principle<=0:
     print("principle can't be less than zero or equal to zero")
while rate<=0:
    rate=float(input("Enter the rate:"))
    if rate<=0:
     print("rate can't be less than zero or equal to zero")
while time<=0:
    time=int(input("Enter the time:"))
    if time<=0:
     print("time can't be less than zero or equal to zero")
compound_interest= principle*pow(1 + rate/100,time)
print(f"Balance after {time} year/s will be {compound_interest:.2f} rupees")

