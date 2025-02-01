# print('functions in Python')

# int addNums(int i, int j) {
#     return i + j;
# }

# def fun(): 
#     print('fun function')
    
# fun()

# def add_nums(i, j):
#     return i + j 

# sum = add_nums() # TypeError: add_nums() missing 2 required positional arguments: 'i' and 'j'
# # sum = add_nums(10)
# # sum = add_nums(10, 20) # this works 
# # sum = add_nums(10, 20, 30) # TypeError: add_nums() takes 2 positional arguments but 3 were given
# print(sum)


# def print_data(name, salary):
#     print(f'My name is {name} and my salary is {salary}.')

# print_data('Sonu', 10.25) # positional arguments 
# print_data(name = 'Sonu', salary = 10.25) # keyword arguments == kwargs 
# print_data(salary = 12.50, name = 'Monu') # keyword arguments kwargs / named arguments 

# default arguments 
# def print_data(name = 'Sonu', salary = 10.25):
#     print(f'My name is {name} and my salary is {salary}.')

# print_data() 
# print_data(name = 'Tonu')
# print_data(salary = 25.50)
# print_data(salary = 12.50, name = 'Monu') 

# # *varargs == variable length arguments 
# def add_nums(*nums):
#     print(sum(nums))

# add_nums(10, 20)
# add_nums(10, 20, 30)
# add_nums(10, 20, 30, 40)


# **kwargs == variable length arguments 
def details(**data):
    print(data)

details(name = 'Sonu', salary = 10.25)
details(name = 'Monu', salary = 12.50, city = 'Pune')