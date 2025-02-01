import employee as em
from employee import Employee, Department

def get_emp():
    # import employee as em
    emp=em.Employee(101,'Sonu')
    # from employee import Employee
    emp=Employee(101,'Sonu')
    dep=em.Department()
    
    #print(emp.emp_data())
    emp.emp_data()
    