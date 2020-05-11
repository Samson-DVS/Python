num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

addition = float(num1) + float(num2)
sub = float(num1) - float(num2)
multi = float(num1) * float(num2)
divi = float(num1) / float(num2)

print(addition)
print(sub)
print(multi)
print(divi)

#Calculator improvements
num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")
