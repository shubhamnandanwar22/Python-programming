#reverse number program in c in hindi
num = int(input("Enter the number"))
sum = 0
while(num>0):
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10
print(sum)
