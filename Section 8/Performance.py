from time import time

def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f'the function took aprox. {t2-t1} S')
        return result
    return wrapper

@performance
def long_func():
    for i in range(100000000):
        i*5

long_func()        
