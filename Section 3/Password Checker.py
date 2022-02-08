user_name=input('what is your user name? ')
password=input('what is your password? ')
length=len(password)

password_as= length * '*'

print(f'{user_name},your password {password_as} is {length} letters')