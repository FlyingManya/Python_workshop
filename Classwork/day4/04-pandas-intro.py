
# import pandas as pd 
# dobs = [22, 9, 25, 31]
# names = ['Sonu', 'Monu', 'Tonu', 'Ponu']
# series = pd.Series(dobs, names)
# print(series)


# import pandas as pd 

# dobs = [22, 9, 25, 31]
# names = ['Sonu', 'Monu', 'Tonu', 'Ponu']
# cities = ['Pune', 'Mumbai', 'Hyderabad', 'Bengaluru']
# index = list((names, cities))  
# series = pd.Series(dobs, index=index)

# print(series)


import pandas as pd 
data = { 
        'name' : ['Sonu', 'Monu', 'Tonu', 'Ponu'], 
        'age' : [22, 9, 25, 31], 
        'city' : ['Pune', 'Mumbai', 'Hyderabad', 'Bengaluru'] 
        }

# print(data)

df = pd.DataFrame(data)
# print(df)
# print(df[['name', 'city']])
# sort 
print(df.sort_values(by='age'))