'''
intVariable = 4

stringVariable = "Software 1 is fun"

print(intVariable)
print(floatVariable)
print(stringVariable)

print(type(intVariable))
print(type(floatVariable))
print(type(stringVariable))

#typecasting is fun
intVariable = int(floatVariable)
print("here is the int version of float variable", intVariable)

shareOfLoan = 500.50/3
print(shareOfLoan)
print(int(shareOfLoan))
print(type(shareOfLoan))
'''
floatVariable = 412.50894756345
num1 = int(input("Enter a number: "))
num2 = float(input("Enter another number: "))
sum = num1 + num2
print(sum)
name = input("Enter your name: ")
school = input("Enter your school: ")
print("you are: ", name, " and your school is: ", school)

print(f"your name is, {name}, and your school name is: {school}")

print(f"Your name is, {name}, and your float Variable is, {floatVariable}")
print(f"Your name is, {name}, and your float Variable is, {floatVariable:.2f}")