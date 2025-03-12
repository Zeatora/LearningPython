print("""What arithnmatic operation would you like to perform?
1. Addition
2. Subtraction
3. Multiplication
4. Division""");

operation = input("Enter operation: ");

def add(a, b):
    return a + b;

def sub(a, b):
    return a - b;

def mult(a, b):
    return a * b;

def div(a, b):
    return a / b;


if operation :
    if operation == '1':
        var1 = int(input("Enter first number: "));
        var2 = int(input("Enter second number:"))
        print(add(var1, var2));
    elif operation == '2':
        var1 = int(input("Enter first number: "));
        var2 = int(input("Enter second number:"))
        print(sub(var1, var2));
    elif operation == '3':
        var1 = int(input("Enter first number: "));
        var2 = int(input("Enter second number:"))
        print(mult(var1, var2));
    elif operation == '4':
        var1 = int(input("Enter first number: "));
        var2 = int(input("Enter second number:"))
        print(div(var1, var2));
    else: 
        print("Invalid")