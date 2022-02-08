# functional programing
# map, filter, zip and reduce
from functools import reduce
mylist=[1,2,3]

#lambda param: action(param)

print(list(map(lambda item: item*2,mylist)))
print(list(filter(lambda item: item%2!=0,mylist)))
print(reduce(lambda acc,item: acc + item,mylist))
print(mylist)    