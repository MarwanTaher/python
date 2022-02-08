class user():
    def sign_in(self):
        print('logged in')

class wizard(user):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} is attacking with the power of {self.power}')  

class archer(user):
    def __init__(self,name,no_arrows):
        self.name = name
        self.no_arrows = no_arrows

    def attack(self):
        print(f'{self.name} is attacking with {self.no_arrows} arrows')       


wizard1 = wizard('Marwan',50)
archer1 = archer('Robin',100) 

archer1.attack()
wizard1.attack()       

