# i=0
# while(i<10):
#     i+=1
#     if(i%2==0):
#         continue
    
# word="artificial intelligence"
# count=0
# #to count number of i
# for i in word:
#     if i=='i':
#              count+=1
# print(count)
# word="hello"
# ct=0
# for ch in word:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         ct+=1
# print(ct)  
# n=int(input("enter number: "))
# sum=0
# for var in range(n):
#     sum+=(var+1)
# print(sum)
# def avg(a,b,c):
#     return float((a+b+c)/3)
# print(avg(2,4,6))
# sum= lambda a,b,c:a+b+c
# print(sum(2,3,4          ))
# def fact(n):
#     fac=1
#     for i in range(1,n+1,1):
#         fac*=i
#         if(i==n):
#             return fac
# n=int(input("enter number"))
# print(fact(n))
# word="python"
# print(word[1:4])
# a=5
# b=10
# sum=a+b
# # print("sum of {1} and {0} is {2} ".format(a,b,sum))
# # print("sum of {a} and {b} is {sum}".format(a=5,b=10,sum=a+b))
# print(f"sum of {a} and {b} is {a+b}")
# marks=[87,88,98,12.00]
# marks[2]=99
# print(marks[2])
# print(len(marks))
# print(marks)
# print(type(marks))
# print(marks[0:3])
# marks.append(57)
# marks.insert(2,83)
# marks.sort()
# marks.sort(reverse=True)
# marks.reverse()
# print(marks)
# x=12
# idx=0
# for val in marks:
#     if(val==x):
#         print(idx)
#         break
#     idx+=1
# dict={
# "name":"Ankit",
# "cg":7.82,
# "year":2,
# }   
# print(dict["cg"])  
# class student:
#     subject="python"
#     course="btech"
# st1=student()
# st2=student()    
# print(st1.subject,st2.course)
# class student:
#     def __init__(self,name,cg):                     
#         self.course="btech"
#         self.name=name
#         self.cg=cg
#     def get_cg(self):
#             return self.cg
# s1=student("Ankit",8.2)
# s2=student("vijay",8.6)
# s3=student("ajay",8.6)
# print(s1.get_cg())
# print(s1.name,s2.cg,s3.course)
# class laptop:
#     storage_type="ssd"
#     @classmethod
#     def get_storage_type(cls):
#         print(f"laptop has {cls.storage_type} storage type")
#     def __init__(self,ram,storage):
#         self.ram=ram
#         self.storage=storage
#     def info(self):
#         print(f"laptop has {self.ram}gb ram and {self.storage}gb {self.storage_type}") 
#     @staticmethod    
#     def calc_discount(price,discount):  
#         final_price=price-(price*discount)/100
#         print(f"final price of laptop is {final_price}")  
# l1=laptop(16,512)
# l2=laptop(8,256)
# l1.info()  
# l1.get_storage_type()
# l1.calc_discount(80_000,10)
class store:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        store.count+=1
    @classmethod
    def track(cls):
         print(f"the numbeer of products is {store.count}")
    @staticmethod
    def discount(price,discount):
         final_price=price-(price*discount/100)
         print(f"final price is {final_price}")
         def get_info(self):
              print(f"the price of {self.name} is {self.price}")
p1=store("laptop",50_000)
p2=store("phone",10_000)  
p3=store("pen",10) 
store.track()           
