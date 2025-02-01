#Decorators in python
def data_accessed(func):
    def wrapper(*args):
        print('emp data accessed.')
        return func(*args)
    return wrapper
    
class Employee :
    
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
    
    @data_accessed
    def emp_data(self):
        print(self.id, self.name)
    
emp1 = Employee(101, 'Sonu')
emp1.emp_data()

