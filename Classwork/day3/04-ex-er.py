#exception and error handling
# print('start')

# nums = [25,31,22,9,17]
# try:
#     print(nums[5])
# except IndexError as e:
#     print(f'{e}')
# finally:
#     print('end')

#custom exceptions and handling

#custom exception class
#child of Exception Class
class InvalidAgeException(Exception):
    
    def __init__(self,age,message='An Exception Occured'):
        self.age = age
        self.message = message
        super().__init__(self.message)
        
#class in which  the custom exception is raised   
class Employee :
    
    def __init__(self, id, name,age):
        self.id = id 
        self.name = name 
        
        if age<18 or age>65:
            #raising an exception manually so that program halts
            raise InvalidAgeException(age,'age is invalid')
        else:
            self.age=age
            
    def emp_data(self):
        print(self.id, self.name,self.age)
        
#custom exception is handeled
try:
    emp1 = Employee(101, 'Sonu','16')

#catches the exception thrown by the exception(super class)
except InvalidAgeException as e:
    print(f'{e}')
    
else:
    print(emp1.id, emp1.name,emp1.age)