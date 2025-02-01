
import matplotlib.pyplot as plt 
import requests as rq 
import pandas as pd 

key_path = r'D:\VamanPro\Codes\oracle-jan-2025\keys\alpha-vantage-api-key.txt'

with open(key_path, 'r') as file:
    api_key = file.read()

symbol = 'SBIN'
market = 'BSE'
api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}.{market}&outputsize=full&apikey={api_key}'

response = rq.get(api_url)
data = response.json()
# print(data)


# show last ten records 

time_series = data.get("Time Series (Daily)", {}) 

df = pd.DataFrame.from_dict(time_series, orient="index")

df.columns = ["Open", "High", "Low", "Close", "Volume"]

df.index = pd.to_datetime(df.index)
df.index.name = "Date"

last_ten_records = df.sort_index().tail(10)
first_ten_records = df.sort_index().head(10)

print(last_ten_records)