#check whether the number is armstrong or not
num = int(input("Enter the number= "))
temp = num
res = 0
power = len(str(num))
#print(power)
while(num):
    digit = num % 10
    res += pow(digit,power)
    num //= 10

if res == temp:
    print("Armstrong Number ")
else:
    print("Not Armstrong Number )
