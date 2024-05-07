def my_decorator(func):
    def wrapper(a,b):
        print("Something is happening before the function is called.")
        print(func(a,b))
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(a,b):
    print("Hello!",a*b)

say_hello(8,2)