n = int(input("Enter your number: "))

def fibonacci(n):
    if (n<2):
        print("Number must be greater than 2.")
        return "Number must be greater than 2." , None
    
    numbers = []
    a,b = 0,1
    
    for k in range(n):
        numbers.append(a)
        a,b = b, a+b

    return numbers
    
sequence = fibonacci(n)
print(sequence)