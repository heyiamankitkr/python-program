#public 
class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
acc1=bank("rakesh",10_000)
# print(acc1.name,acc1.balance)
#protected
class bank:
    def __init__(self,name,balance):
        self.name=name
        self._balance=balance
acc1=bank("rakesh",10_000)
# print(acc1.name,acc1._balance)
#private
class bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
acc1=bank("rakesh",10_000)
# print(acc1.name,acc1.__balance)
# getter and setter func
class bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_balance):
        self.__balance=new_balance   
acc1=bank("rakesh",10_000)
acc1.set_balance(20_000)
print(acc1.name,acc1.get_balance()) #get_balance function call krne vkt   () ye lgao nhi to error aayega  
#M2 for accessing private variable 
print(acc1.name,acc1._bank__balance) #object name._class name__private variable name