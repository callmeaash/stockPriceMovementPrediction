import requests
import csv
import os

# API to extract stocls historical data (got it from chukul)
API_URL = 'https://chukul.com/api/data/historydata/?symbol='

# Function to extract the raw data of the stocks
def fetch_stock_data():

    # Directory to store raw data
    raw_data_dir = os.path.join("data", "raw")
    os.makedirs(raw_data_dir, exist_ok=True)

    # Access stocks Symbols list
    stocks_file = os.path.join("stocks", "Hydropower.csv")

    scripts = []

    # Load all the symbols in a empty list
    with open(stocks_file, "r") as file:
        file.readline()
        for line in file:
            scripts.append(line.strip())

    headings = ["date", "symbol", "open", "high", "low", "close", "volume"]

    # Store all stocks historical data into a new file
    output_file = os.path.join(raw_data_dir, "data.csv")
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headings, extrasaction="ignore")
        writer.writeheader()

        for script in scripts:
            url = API_URL + script
            request = requests.get(url)
            response = request.json()

            for row in response[:200]:
                writer.writerow(row)


if __name__ == "__main__":
    fetch_stock_data()