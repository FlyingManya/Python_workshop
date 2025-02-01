# # consume rest APIs 

# import requests

# print('start')

# api_url = 'https://jsonplaceholder.typicode.com/users/1'
# try:
#     response =  requests.get(api_url)
    
# except requests.exceptions.ConnectionError as e:
#     print(f'{e}')
    
# else:
#     data = response.json()
#     print(data['name'], data['email'])
    
# finally:
#     response.close()
#     print('end')

