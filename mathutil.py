# Assuming the below code in this id a collection of functions

# defining a decorator
def is_int(func_obj):
    print("fun_obj - ", func_obj)
    
    def check(*args) :
        if all(map(lambda num : type(num) == int, args)):
            return func_obj(*args)
        else :
            return "Invalid"        
    return check

@is_int
def add(x, y=2) :
    return x+y

@is_int
def factorial(num) :
    fact = 1 
    for i in range(1, num+ 1):
        fact *= i 
    return fact

@is_int
def even_odd(num) :
    return "even" if num%2==0 else "odd"