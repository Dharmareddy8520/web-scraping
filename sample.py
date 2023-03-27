import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_excel("web.xlsx")

df['address'] = ''


for index, row in df.iterrows():
    website = row[" WEBSITE"]
    print("Website:", website)  
    try:
        response = requests.get(website, timeout=5, verify=False)

        soup = BeautifulSoup(response.content, 'html.parser')
        
        address_tag = soup.find('address')
        
        if address_tag:
            address = address_tag.get_text().strip()
            
            df.loc[index, 'Address'] = address
        else:
            print(f"No address found for {row['COLLEGE NAME']}")
    except Exception as e:
        print(f"Error getting address for {row['COLLEGE NAME']}: {e}")

df.to_excel('colleges_with_address.xlsx', index=False)



