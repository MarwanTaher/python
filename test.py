#Comment
# name=input('please type your name: ')
# print('Hello '+ name.capitalize())
# output = f'Hello {name.capitalize()}'
# output = 'Hello {} '.format(name.capitalize()) 
# print (output)

# days_in_feb=28
# print(str(days_in_feb) + ' days in feb')
# from datetime import datetime, timedelta
# time=datetime.now()
# one_day=timedelta(days=1)
# yesterday=time-one_day
# birthday=input('please type your bd:')
# bd=datetime.strptime(birthday,'%d/%m/%Y')
# print ('Day: ' + str(bd.day) + ' Month: ' + str(bd.month)  + ' Year: ' + str(bd.year))
# print (str(yesterday.day))
# x=5
# y=0
# try:
#     x/y
# except ZeroDivisionError as error:
#     print('1')
# finally:
#     print('2')


#taxes 
# price=input('Please enter the value: ')
# price=float(price)

# if price >=5.00:
#     tax=0.7
# else:
#     tax=0
# print('tax=' + str(tax))   

#taxes in province
# province=input('please enter the province: ')
# if province in('cairo','alex'):
#     tax=2
# elif province == 'monof' or 'dahab':
#     tax=5
# print('tax is = ' + str(tax) + ' in ' + str(province))  
# 
# 
# GPA
# gpa=input('plaese enter gpa: ')
# lowestgrade=input('please enter lowest grade: ')
# if float(gpa)>= 0.85 and float(lowestgrade)>= 0.7:
#     honor=True 
# else:
#     honor=False

# if honor == True :   
#     print('congratulations')

###################################################################################################
# Dictionaries

# Christofer={}
# Christofer['first']='Christofer'
# Christofer['last']='Harrison'

# Susan={}
# Susan['first']='Susan'
# Susan['last']='Harrison'

# people=[]
# people.append(Christofer)
# people.append(Susan)

# print(people[1])
# print(Christofer['last'])

#####################################################################################################
#loops

# for index in range (0,6):
#     print(index)

# people=['chris','susan'] 

# for name in people:
#     print(name)

# #while

# index = 0
# while index <len(people):
#     print(people[index])
#     index=index+1

###############################################################################################
#Functions1

# from datetime import datetime

# def print_time(taskname):
#     print(taskname)
#     print('task completed')
#     print(datetime.now())
#     print()

# #print time stamps to see how long sections of code 
# first_name= 'Marwan'
# print(first_name)
# print_time('first_name')

# for x in range (0,10):
#     print(x)
#     print_time('for loop')

###############################################################################################
#Functions2

def get_intial(name,force_uppercase=True):
    if force_uppercase:
        intial= name[0:1].upper()
    else:
        intial= name[0:1]
    
    return intial

first_name= input('Enter your first name: ')
first_intial= get_intial(force_uppercase=False,name=first_name)

last_name= input('Enter your last name: ')
last_intial=get_intial(last_name)




print ('the Intials are: ' + first_intial + last_intial)

