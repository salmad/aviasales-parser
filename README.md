# Aviasales Flight Price Monitor

> **TL;DR**: Track flight prices over time by running one command. Data appends to CSV for trend analysis.

## Purpose

**What**: Tool that scrapes Aviasales flight prices and stores them in a CSV database.
**Why**: Monitor price changes for a route across days/weeks to find the best booking time.
**Who**: For anyone tracking a specific flight route.

## Quick Start

```bash
./monitor.sh
```

This captures current prices and appends them to `flight_prices.csv` with timestamp. Prices display in terminal.

## What You Get

### Immediate Output
- Formatted price list sorted low-to-high with airline, times, duration
- Price summary (cheapest, most expensive, average)
- Screenshot of the page for verification

### Data Files
- **`flight_prices.csv`** – All collected prices over time (main database)
- `api_responses_*.json` – Raw API responses
- `aviasales_screenshot_*.png` – Visual confirmation

### CSV Format
Each row is one ticket at one moment. Columns:
- `timestamp` – When data was collected
- `price` – Ticket price in rubles
- `route` – Full route display
- `origin`, `destination` – Airports
- `airline` – Airline name
- `departure_time`, `arrival_time` – Times
- `duration` – Flight duration
- `stops` – Number of stops

## Workflow

**Track price trends:**
1. Run `./monitor.sh` at different times (now, tomorrow, in a week)
2. Run `python view_prices.py` to see price history and trends
3. Open `flight_prices.csv` in Excel/Sheets to create charts and pivot tables

## Customization

### Change the Route
Edit `monitor_flight_prices.py` line ~120:
```python
url = "https://www.aviasales.ru/search/MOW1401CMB1"
#                                      ^^^^^^^^^^^^
```

Format: `ORIGIN[DATE]DESTINATION[DATE]`
- MOW = Moscow, CMB = Colombo, DXB = Dubai
- 1401 = January 14, 2002 = February 20

Example – Moscow to Dubai Feb 20:
```python
url = "https://www.aviasales.ru/search/MOW2002DXB1"
```

### Adjust Wait Time
If prices load slowly, edit `monitor_flight_prices.py` line ~120:
```python
asyncio.run(monitor_flight_prices(url, wait_time=45))  # Wait 45 seconds instead of 30
```

## Manual Commands

Run components separately:
```bash
source venv/bin/activate

# Capture only (no display)
python monitor_flight_prices.py

# Parse and display latest capture
python show_prices.py

# View price history
python view_prices.py
```

## Troubleshooting

**Prices not showing?**
1. Check `aviasales_screenshot_*.png` – did the page load?
2. Increase `wait_time` if connection is slow
3. Check `api_responses_*.json` – did the API respond?

**Setup already complete** – virtual environment and dependencies installed.
