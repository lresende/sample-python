import io
import requests
import pandas as pd

def df_from_url(url):
    data = requests.get(url).content
    df = pd.read_csv(io.StringIO(data.decode('utf-8')))
    return df


df = df_from_url('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
df.groupby('zip')['price'].mean()