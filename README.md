# Aviasales Flight Price Monitor

A Python tool to monitor and extract flight prices from Aviasales search pages.

## What it does

This tool:
1. Opens the Aviasales search page in a browser
2. Waits for prices to load (30 seconds by default)
3. Intercepts API calls to capture flight data
4. Parses and displays all available flight prices
5. Saves a screenshot for visual confirmation

## Setup

Already done! The virtual environment and dependencies are installed.

## Usage

### Quick Start

Simply run:
```bash
./monitor.sh
```

This will:
- Launch a browser (visible so you can see what's happening)
- Load the Moscow → Colombo flight search
- Wait for prices to load
- Display all found flights sorted by price
- Save a screenshot and raw API data

### Manual Usage

If you want to run components separately:

```bash
source venv/bin/activate

# Capture prices from Aviasales
python monitor_flight_prices.py

# Parse and display the captured data
python show_prices.py
```

### Customization

To monitor a different route, edit `monitor_flight_prices.py` and change the URL:

```python
url = "https://www.aviasales.ru/search/MOW1401CMB1"
```

To change wait time (if prices load slowly):

```python
asyncio.run(monitor_flight_prices(url, wait_time=45))  # Wait 45 seconds
```

## Output

The tool creates several files:

- `flight_prices.csv` - **Main output!** CSV table with all prices, timestamps, and flight details
- `api_responses_*.json` - Raw API responses with all flight data
- `aviasales_screenshot_*.png` - Screenshot of the loaded page
- Terminal output with formatted price list

### CSV Format

Each run appends new rows to `flight_prices.csv` with columns:
- `timestamp` - When the data was collected
- `price` - Ticket price in rubles
- `route` - Full route (e.g., "Внуково → Бандаранаике")
- `origin` - Departure airport/city
- `destination` - Arrival airport/city
- `airline` - Airline name
- `departure_time` - Departure time (HH:MM)
- `arrival_time` - Arrival time (HH:MM)
- `duration` - Flight duration
- `stops` - Number of stops

This allows you to track price changes over time!

## Example Output

```
================================================================================
💰 FLIGHT PRICES - Moscow (MOW) to Colombo (CMB)
   Found 20 flights
================================================================================

1. 16,710 ₽
   Внуково → Бандаранаике
   Победа
   13:05 → 22:45 (1d 9h 40m)
   Stops: 2

2. 17,182 ₽
   Внуково → Бандаранаике
   Победа
   12:55 → 22:45 (1d 9h 50m)
   Stops: 1

...

================================================================================
📊 PRICE SUMMARY
================================================================================
Cheapest:      16,710 ₽
Most expensive: 42,311 ₽
Average:       24,384 ₽
Total flights: 20
```

## Viewing Price History

To view saved price data and trends:

```bash
source venv/bin/activate
python view_prices.py
```

This will show:
- Total records collected
- Price ranges for each collection timestamp
- Price trends by airline
- Sample data from latest run

You can also open `flight_prices.csv` directly in Excel, Google Sheets, or any spreadsheet application.

## Files

- `monitor_flight_prices.py` - Main script that loads the page and captures API data
- `show_prices.py` - Parses the captured JSON and displays formatted prices
- `view_prices.py` - Analyzes and displays price history from CSV
- `monitor.sh` - Wrapper script that runs both steps
- `flight_prices.csv` - CSV database of all collected prices (appends each run)
- `requirements.txt` - Python dependencies (playwright)
- `venv/` - Python virtual environment

## Notes

- The browser window will open visibly so you can see the page loading
- Wait time can be adjusted if needed
- All captured data is saved locally for analysis
- This is for personal monitoring use only

## Troubleshooting

If prices aren't showing:
1. Check the screenshot to see if the page loaded correctly
2. Increase the wait_time if your connection is slow
3. Check api_responses_*.json to see what data was captured
