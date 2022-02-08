def highest_even(li):
    highest_even_num=0
    for item in li:
         if item % 2 == 0:
             if item > highest_even_num:
                highest_even_num = item
             
    return highest_even_num

print(highest_even([10,2,5,8,3,1]))   
