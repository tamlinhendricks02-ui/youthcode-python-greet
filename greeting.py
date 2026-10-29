def greet ():
    print("Hello, World!")


greet()



def greet(name):
    return f"Hello, {name}!"
greeting = greet("Tamlin")
print(greeting)



def square(number):
    return number * number

result = square(5)
print(result)



def rectangle_area(length, width):
    return length * width 

result = rectangle_area(4, 5)
print(result)





def apply_operation(func, number):
    return func(number)

def double(number):
    return number * 2


def double(x):
    return x * 2

def apply_operation(func, num):
    return func(num)

result = apply_operation(double,7)

print(result)

def square(x):
    return x ** 2

def apply_operation(operation, number):
    return operation(number)

result = apply_operation(square, 3)
print(result)






    