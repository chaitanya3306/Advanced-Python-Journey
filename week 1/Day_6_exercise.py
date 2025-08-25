class Insufficintbalance(Exception):
    pass
class Invalidamount(Exception):
    pass
    


class Bankaccount():
    def __init__(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.balance=0
        
    def withdraw(self,amount):
        if amount < 0:
            raise Invalidamount()
        elif self.balance - amount < 0:
            raise Insufficintbalance()
        else:
            print(f"Amount {amount} Withdrawn ")
            self.balance -= amount
    def deposite(self,amount:int):
        if amount < 0:
            raise Invalidamount()
        else:
            print(f"Amount {amount} Deposited")
            self.balance += amount
            
    def checkbalance(self):
        print(f"you have {self.balance} rs left in your Acoount")
        
acc1=Bankaccount('chaitanya',23022112)
acc1.checkbalance()
acc1.deposite(1000)
acc1.checkbalance()
acc1.withdraw(100)
acc1.checkbalance()

        
            
        
        