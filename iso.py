import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Script Started")

# loading the excel file
df = pd.read_excel("F:/standardsProject/standardsTask/stand1.xlsx")

# function to get status from excel
def get_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # adjusting the selector based on the website's structure
            status_tag = soup.find("strong")
            if status_tag:
                return status_tag.text.strip()
            else:
                return "Status not found"
        else:
            return "URL not accessible"
    except Exception as e:
        return str(e)
    
# applying the function to each row and adding a new column to store the result
df["CurrentStatus"] = df["Link1"].apply(get_status)

# save the updated data to a new excel file
df.to_excel("standards1_updated.xlsx", index=False)

print("Script Ended")