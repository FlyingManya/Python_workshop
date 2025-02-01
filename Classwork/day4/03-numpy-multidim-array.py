
# python 03-numpy-multidim-array.py
# multi dimeltional arrays in NumPy 

# import requests as rq
# import numpy as np

# api_url = 'https://jsonplaceholder.typicode.com/posts'
# response = rq.get(api_url)
# data = response.json()
# print(data)

# arr = np.array([(d['userId'], d['id'], d['title'], d['body']) for d in data])
# print(f'{posts_array}')
# print(arr.size)
# print(arr.shape)

import numpy as np

# # 1d array 
# arr = np.array([10, 20, 30])
# print(arr)
# print(arr.size)
# print(arr.shape) # (3,)   == (1, 3)

# # 2d array 
# arr = np.array([[10, 20, 30], [40, 50, 60]])
# print(arr)
# print(arr.size)
# print(arr.shape)

# 3d array 
arr = np.array([[10, 20, 30, 90], [40, 50, 60, 50], [40, 20, 80, 10]])
print(arr)
# print(arr.size)
# print(arr.shape)
print(arr[1][2]) # classic style 
print(arr[1, 2]) # shrothand style 
