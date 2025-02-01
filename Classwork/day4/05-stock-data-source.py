

# documentation 
# https://www.alphavantage.co/documentation/
# get your key 
# https://www.alphavantage.co/support/#api-key
# sample api 
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey=demo

# example to get 20 years data of Reliance Industries on BSE 
import requests as rq 

key_path = r'D:\VamanPro\Codes\oracle-jan-2025\keys\alpha-vantage-api-key.txt'

with open(key_path, 'r') as file:
    api_key = file.read()

symbol = 'INFY'
market = 'BSE'
api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}.{market}&outputsize=full&apikey={api_key}'

response = rq.get(api_url)
data = response.json()
print(data)

# sample data output 
# '2005-01-28': {'1. open': '581.5000', '2. high': '629.8000', '3. low': '580.9000', '4. close': '622.7500', '5. volume': '34897898'} 
