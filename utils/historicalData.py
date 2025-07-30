import requests
import pandas as pd
import csv

api = 'https://chukul.com/api/data/historydata/?symbol='

scripts = []

with open("Hydropower.csv", "r") as file:
    file.readline()
    for line in file:
        scripts.append(line.strip())

headings = ["date", "symbol", "open", "high", "low", "close", "volume"]

with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headings, extrasaction="ignore")
    writer.writeheader()
        
    for script in scripts:
        url = api + script
        request = requests.get(url)
        response = request.json()

        for row in response[:200]:
            writer.writerow(row)

df = pd.read_csv("data.csv")
df["target"] = df.groupby("symbol")["close"].shift(1)
df = df.dropna(subset=["target"])
df.to_csv("dataset.csv", index=False)
