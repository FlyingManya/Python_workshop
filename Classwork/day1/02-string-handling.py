
# # string handling 

# # first_name = 'abcdefghij'
# # first_name = "Sonu Singh"
# # first_name = '''Sonu Singh'''

# # print(first_name)
# # print(first_name[0])
# # print(first_name[-1])

# # slicing 
# # print(first_name[2:4])
# # print(first_name[0:4:2])
# first_name = 'Sonu'
# last_name = 'Singh'
# full_name = first_name + ' ' + last_name

# # print(full_name)
# # print(first_name * 3)

# # print(first_name.upper())

# # print(first_name.swapcase())

# # search 

# text = 'abcdefghij'

# # print(text.find('d'))
# # print(text.find('z'))
# # print(text.replace('d', 'z'))
# text = '        asdf         '
# print(text)
# print(text.strip())

# employees = 'Sonu, Monu, Tonu'
# print(employees)

# names = employees.split(', ')
# print(names)

# emp = 'Sonu'


# string formatting 

name = 'Sonu'
salary = 10.25

# f-strings
# print('My name is {name} and my salary is {salary}.')
print(f'My name is {name} and my salary is {salary}.')

# % 
print('My name is %s and my salary is %f.' %(name, salary))