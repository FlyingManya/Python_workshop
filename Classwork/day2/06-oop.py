
# OOP 
# class object 

# entity - attributes, functinalities 
# employee - id, name, salary, ... work(), write_code(), leave(), ... 


# employee = {'id': 101, 'name': 'Sonu'}

# class 
# fields, functions 

# class Employee :
#     pass
# emp1 = Employee()

# # simple class example 
# class Employee :
    
#     def emp_data(self):
#         print('employee class')
    

# emp1 = Employee()
# emp1.emp_data()


# # simple class example 
# class Employee :
    
#     # special method == constructor 
#     def __init__(self, id, name):
#         self.id = id 
#         self.name = name 
    
#     def emp_data(self):
#         print(self.id, self.name)
    
# # emp1 = Employee() # call to constructor - __init__(self):

# emp1 = Employee(101, 'Sonu')
# # emp1.emp_data()
# print(emp1.id, emp1.name)


# # simple class without a constructor 
# class Employee :
        
#     def emp_data(self):
#         print(self.id, self.name)
    
# # emp1 = Employee(101, 'Sonu')
# emp1 = Employee()
# emp1.id = 101
# emp1.name = 'Sonu'
# print(emp1.id, emp1.name)


# class Employee :
    
#     def __init__(self, id, name):
#         self.id = id 
#         self.name = name 
    
#     def emp_data(self):
#         print(self.id, self.name)
    
# emp1 = Employee(101, 'Sonu')
# print(emp1.id, emp1.name)

# emp2 = Employee(102, 'Monu')
# print(emp2.id, emp2.name)

# # Encapsulation 

# class Employee :
    
#     def __init__(self, id, name, salary):
#         self.id = id 
#         self.name = name 
#         self.__salary = salary # __private field 
        
#     def set_salary(self, salary): # setter 
#         self.__salary = salary
    
#     def get_salary(self): # getter 
#         return self.__salary 
    
#     def emp_data(self):
#         print(self.id, self.name)

# emp2 = Employee(102, 'Monu', 10.25)
# print(emp2.id, emp2.name, emp2.get_salary())
# # emp2.__salary = 12.50 # error 

# print(emp2._Employee__salary) # possible but not recommenred 
# emp2.set_salary(12.50)
# print(emp2.id, emp2.name, emp2.get_salary())

# # Inheritance  

# # sub class extends super class 
# class ContractualEmployee (Employee):
    
#     # subclass has access to properties of super class 
#     # subclass can create its own functions as well 
#     def show_bonus(self):
#         print(self.get_salary() + 10)
        
# # polymorphism - method overriding 
#     def emp_data(self):
#         print(self.id, self.name, self.get_salary())


# emp3 = ContractualEmployee(103, 'Ponu', 15.25)
# emp3.emp_data()
# emp3.show_bonus()

# Polymorphism 


# class Class:
#     def __init__(self, id, salary, name):
#         self.id = id # public field 
#         self._salary = salary # protected field - accessible in the child class 
#         self.__name = name # private field 

# class ChildClass (Class) :
#     pass 

# cls = Class(1, 10, 'a')

# # print(cls.__name) # not possible 
# # print(cls._Class__name) # name mangling, pollisble but mot recommended  
# # print(cls._salary) # pollisble but mot recommended  

# cls2 = ChildClass(2, 20, 'b')
# # print(cls2._salary) # pollisble but mot recommended  


# # __init__ (constructor)  __str__ (toString())  __gt__ __lt__ __eq__ 
# # double underscore methods == dunder methods == magic methods 

# class Employee:
    
#     def __init__(self, id, name, salary):
#         self.id = id 
#         self.name = name 
#         self.__salary = salary # __private field 
        
#     def set_salary(self, salary): # setter 
#         self.__salary = salary
    
#     def get_salary(self): # getter 
#         return self.__salary 
    
#     def __str__(self):
#         return f'The employee id is {self.id} name is {self.name} and salary is {self.__salary}.'
    
#     def emp_data(self):
#         print(self.id, self.name)

# emp2 = Employee(102, 'Monu', 10.25)
# # print(emp2)
# print(str(emp2)) # method call - str(object_name)


#salary = 10.25

#FINAL_FIELD = 10
