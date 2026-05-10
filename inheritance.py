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