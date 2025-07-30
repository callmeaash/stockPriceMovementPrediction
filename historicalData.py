import requests
import json
import pandas as pd
url = 'https://chukul.com/api/data/historydata/?symbol='
response = requests.get(url)
data = response.json()

with open("Hydropower.csv")

