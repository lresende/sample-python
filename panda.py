import io
import requests
import pandas as pd

def df_from_url(url):
    data = requests.get(url).content
    df = pd.read_csv(io.StringIO(data.decode('utf-8')))
    return df

