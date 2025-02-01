# numpy array of strings 

import requests as rq
import numpy as np

api_url = 'https://jsonplaceholder.typicode.com/posts'
response = rq.get(api_url)
data = response.json()
# print(data)

arr = np.array([d['title'] for d in data])

# for r in arr.tolist():
#     print(r)

# print(arr)
# print(arr.size)
# print(arr.shape)
# print(arr.dtype)
# print(np.char.upper(arr))
# print(np.char.find(arr, 'e'))
# print(np.char.split(arr, ' '))
# list(['at', 'nam', 'consequatur', 'ea', 'labore', 'ea', 'harum'])]
# print(np.sort(arr))
print(np.char.str_len(arr)) # langth of each string element 