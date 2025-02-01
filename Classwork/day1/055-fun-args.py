
# def fun(a = 2, b = 3):
#     print(a + b)

# def fun(*args):
#     print(sum(args))

# fun(10, 20)
# fun(10)
# fun()

# # **args **kwargs 

# def fun(a = 2, b = 3):
#     print(a + b)

# fun()


# # regular function 
# def fun(a = 2, b = 3):
#     return a + b 

# # lamdba functions
# fun = lambda a, b : a + b
# # # fun = lambda a, b : return a + b

# # print(fun(10, 20))

# gst = lambda : 18
# print(gst())

# *args 

# adds = lambda *args : sum(args)
# print(adds(10, 20, 30))

# **kwargs 

# adds = lambda **kwargs : f'My name is {kwargs.get('name')}.'

# print(adds(name = 'Sonu'))


# fun = lambda a = 2, b = 2 : a + b

# print(fun(10, 20))
# print(fun())


# fun = lambda a, b : a + b

# print(fun(10, 20))

# num1 = 5
# num2 = 6
# num3 = fun(num1, num2)
# print(num3)

#  Anonymous functions 

# print((lambda a, b : a + b)(11, 22))


# dobs = [4, 17, 9, 22, 25, 31, 10]

# print(dobs) # print all 

# # print only even numbers 
dobs=[4,17,9,22,25,31,10]
for i in dobs:
    if(i%2==0):
        print(i)

# print([a for a in dobs if a % 2 == 0])

# filter, map, reduce, sort 

from functools import reduce 

dobs = [4, 17, 9, 22, 25, 31, 10]
print(dobs)

evens = list(filter(lambda d: d % 2 == 0, dobs))
print(evens)

dbl = list(map(lambda d: d * 2, evens))
print(dbl)

sum = reduce(lambda a, b : a + b, dbl) 
print(sum)

# Can you summarise filter map reduce , the diffrences