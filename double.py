def double(func):
    def wrapper():
        func()
        print("Let's try that again!")
        func()
    return wrapper

"""
from double import double

@double
def greet():
    print("Hello World!")

def main():
    greet()

main()

Output:
Hello World!
Let's try that again!
Hello World!

"""