import requests
import csv


# List of URLs to loop through
urls = [
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1734130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1730530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1726930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1723330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1719730800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1716130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1712530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1708930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1705330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1701730800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1698130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1694530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1690930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1687330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1683730800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1680130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1676530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1672930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1669330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1665730800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1662130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1658530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1654930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1651330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1647730800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1644130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1640530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1636930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1633330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1629730800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1626130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1622530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1618930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1615330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1611730800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1608130800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1604530800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1600930800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1597330800000",
    "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1h&limit=1000&endTime=1593730800000",
]

# Output CSV file
output_csv = "ethusd_hourly_klines.csv"

# Header for CSV
header = ["timestamp", "open", "high", "low", "close", "volume"]

# Open the CSV file to write
with open(output_csv, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(header)

    # Loop through each URL and fetch the data
    for url in urls:
        try:
            # Make the API call
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()
            
            # Extract relevant fields and write them to the CSV
            for entry in data:
                row = [
                    entry[0],  # timestamp
                    entry[1],  # open
                    entry[2],  # high
                    entry[3],  # low
                    entry[4],  # close
                    entry[5],  # volume
                ]
                writer.writerow(row)
            print(f"Data fetched and written for URL: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data for URL {url}: {e}")
        except KeyError as e:
            print(f"Unexpected data structure for URL {url}: {e}")

print(f"Data saved to {output_csv}")
