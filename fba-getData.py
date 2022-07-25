import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
# get asins from csv and add header
asins = pd.read_csv('./sheets/electronics.txt', sep=" ", header=None, names=["ASIN"])

# create a dataframe and append the asins to it
df = pd.DataFrame(asins)
df.head()

# create a new column and added a hyperlink for each asins
df['LINK'] = '=HYPERLINK("https://amazon.com/dp/' + df['ASIN'].map(str) + '", "AMZ LINK")'

# visit each link and pull additional data
url = 'https://www.amazon.com/dp/B09Y52HRF7'
# dfs = pd.read_html(url)

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())


# write data to excel
# df.to_excel('./sheets/electronics.xlsx',index=False)

# print(dfs)
# print('txt is written to Excel File successfully.')clear