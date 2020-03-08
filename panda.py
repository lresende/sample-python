import io
import requests
import time
import pandas as pd

def delay(seconds):
    time.sleep(seconds)

def df_from_url(url):
    data = requests.get(url).content
    df = pd.read_csv(io.StringIO(data.decode('utf-8')))
    return df

# Uncomment the lines below to sleep for a bit
# useful to demonstrate kernel startup on container environments
#delay(5)

# Sample panda code to manipulate the generated data frame 
# and calculate mean price per zipcode
df = df_from_url('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
df.groupby('zip')['price'].mean()    

