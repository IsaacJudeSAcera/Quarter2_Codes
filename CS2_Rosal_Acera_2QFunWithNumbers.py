age=int(input("Hi there! Please enter your age:"))
sum = 0
for i in range(1,age+1):
    sum+=i
print(f"The sum of all numbers 1 to {age} is: {sum}")