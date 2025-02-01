# pip install matplotlib 
# pip3 install matplotlib 

import matplotlib.pyplot as plt 
import pandas as pd 

print('start')
data = {
    'name': ['Sonu', 'Monu', 'Tonu', 'Ponu'],
    'age': [17, 25, 31, 22]
}

df = pd.DataFrame(data)

df.plot(x= 'name', y = 'age', kind = 'line', title = 'Names and Ages')

# plt.savefig('names-and-ages.png')
plt.show()
print('end')