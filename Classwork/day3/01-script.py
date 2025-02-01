#operator overloading through magic methods
class Employee :
    
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
        
    def __eq__(self, value):
        return self.id==value.id and self.name==value.name
    
    def emp_data(self):
        print(self.id, self.name)
    
emp1 = Employee(101, 'Sonu')
emp2 = Employee(102, 'Monu')
print(emp2.id, emp2.name)
print(emp1==emp2);
