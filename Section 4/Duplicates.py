list=['a','b','c','d','b','m','n','n']

duplicates=[]
for value in list:
    if list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)            
