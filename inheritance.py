class employee:#parent
        start="10 am "
        end="6 pm"
        def change_time(self,new_time):
         self.start=new_time
class teacher(employee):#child
    def __init__(self,subject):
        self.subject=subject    
class admin(employee):
    def __init__(self,role):
        self.role=role        
   
t1=teacher("maths")
t1.change_time("9 am")
admin=admin("manager")
print(t1.start,t1.end,t1.subject,admin.start,admin.role)
#multi level inheritence
class employee:#parent
        start="10 am "
        end="6 pm"
        def change_time(self,new_time):
         self.start=new_time   
class admin(employee):
    def __init__(self,role):
        self.role=role  
class accountant(admin):
    def __init__(self,salary,role):
        self.salary=salary
        self.role=role
acc=accountant(20_000,"ca")                      
   
t1=teacher("maths")
t1.change_time("9 am")
admin=admin("manager")
print(acc.start,acc.end,acc.start,acc.role)
# multiple inheritance
class teacher:
    def __init__(self,subject,salary):
        self.subject=subject
        self.salary=salary
class student:
    def __init__(self,gpa):
        self.gpa=gpa
class TA(teacher,student):
    def __init__(self,subject,salary,gpa,name):
        super().__init__(subject,salary)
        student.__init__(self,gpa)
        self.name=name
ta1=TA("maths",25_000,8.2,"ankit")        
print(ta1.subject,ta1.salary,ta1.name,ta1.gpa)
                