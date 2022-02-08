
def fib(num):
    x=0
    y=1
    temp = 0
    for i in range(num):
        yield x
        temp=x
        x=y
        y=temp+y

def print_fib(number):
    for item in fib(number):
        print(item)    

print_fib(20)            