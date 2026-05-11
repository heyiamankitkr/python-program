#function overriding
class employee:
    def get_designation(self):
     print("designation=employee")
class teacher:
   def get_designation(self):
     print("designation=teacher")
t1=teacher()
t1.get_designation()
e1=employee()
e1.get_designation() 
#duck typing (same hi hai syntax )
class employee:
    def get_designation(self):
     print("designation=employee")
class teacher:
   def get_designation(self):
     print("designation=teacher")
t1=teacher()
t1.get_designation()
e1=employee()
e1.get_designation()       