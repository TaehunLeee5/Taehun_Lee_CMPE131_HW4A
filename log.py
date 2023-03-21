import time
def timestamp(func):
    def wrapper():
        print(time.ctime())
        func()
    return wrapper

"""
from log import timestamp

@timestamp
def hi():
    print("hi")

def main():
    hi()

main()

Output:
Mon Mar 20 04:00:18 2023
hi
"""