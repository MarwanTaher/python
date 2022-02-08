# functional programing
# map, filter, zip and reduce
mylist=[1,2,3]
your_list = [10,20,30]
def mult_by_2(item):
    return item * 2
    
def only_odd(item):
    return item % 2 != 0

print(list(zip(mylist,your_list)))
print(mylist) 