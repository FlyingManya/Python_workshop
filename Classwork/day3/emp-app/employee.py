#operator overloading through magic methods
class Employee :
    
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
        
    def __eq__(self, value):
        return self.id==value.id and self.name==value.name
    
    def emp_data(self):
        print(self.id, self.name)
        
class Department:
    pass