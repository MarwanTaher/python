# functional programing
# map, filter, zip and reduce
from functools import reduce
mylist=[1,2,3]
def mult_by_2(item):
    return item * 2
    
def only_odd(item):
    return item % 2 != 0

def accumulator(acc,item):
    return acc + item

print(reduce(accumulator,mylist,0))
print(mylist) 