class Account:
    def __init__(self,balance, account_no):
        self.balance=balance
        self.account_no =account_no


    #debit method
    def debit(self,amount):
       self.balance -= amount 
       print("Rs." , amount , "was debited")

     #credit method
    def credit(self,amount):
       self.balance += amount 
       print("Rs." , amount , "was credited")

    def get_balance(self):
        return self.balance
    
         
acc1 = Account(100000, 77777)
print(acc1.balance)
print(acc1.account_no)

acc1.debit(10)
acc1.credit(200000)

print(acc1.balance)
