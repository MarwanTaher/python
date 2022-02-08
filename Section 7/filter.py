# functional programing
# map, filter, zip and reduce
mylist=[1,2,3]
def mult_by_2(item):
    return item * 2
    
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd,mylist)))
print(mylist)    