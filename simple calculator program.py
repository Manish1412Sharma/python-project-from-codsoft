num1 = float(input("Enter first no. = "))

operator = input("enter operator (+ , - , / , * , % ) = ")

num2 = float(input("Enter second no. = "))

if operator == "+" :
    print(num1 + num2)

elif operator == "-" :
    print(num1 - num2)

elif operator == "*" :
    print(num1 * num2)

elif operator == "/" :
    print(num1 / num2)

elif operator == "%" :
    print(num1 % num2)

else :
    print("invalid input")