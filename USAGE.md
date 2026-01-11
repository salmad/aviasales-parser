# Quick Usage Guide

## Collect Flight Prices

Run this command whenever you want to check prices:

```bash
./monitor.sh
```

This will:
1. Open a browser and load the Aviasales search page
2. Wait for prices to load
3. Extract all flight data
4. **Append results to `flight_prices.csv` with current timestamp**
5. Display prices in terminal
6. Save screenshot and raw data

## View Price History

After collecting data multiple times, view trends:

```bash
source venv/bin/activate
python view_prices.py
```

## CSV Output

**File:** `flight_prices.csv`

**Format:** Each row = one ticket at one point in time

**Columns:**
- `timestamp` - When collected (e.g., "2026-01-11 23:33:05")
- `price` - Ticket price in rubles
- `route` - Full route
- `origin` - Departure point
- `destination` - Arrival point
- `airline` - Airline name
- `departure_time` - Departure time
- `arrival_time` - Arrival time
- `duration` - Flight duration
- `stops` - Number of stops

**Important:** File grows with each run - this is intentional! It allows tracking price changes over time.

## Example Workflow

```bash
# Collect prices now
./monitor.sh

# Wait some time (e.g., 1 hour, 1 day)
# Then collect again
./monitor.sh

# View how prices changed
source venv/bin/activate
python view_prices.py
```

## Open CSV in Spreadsheet Apps

You can open `flight_prices.csv` in:
- **Excel:** File → Open → flight_prices.csv
- **Google Sheets:** File → Import → Upload → flight_prices.csv
- **LibreOffice Calc:** File → Open → flight_prices.csv

Then you can:
- Create pivot tables
- Make charts showing price trends
- Filter by airline, price range, etc.
- Sort by any column

## Tips

1. **Run regularly** - Set up a cron job or run manually at different times
2. **Same search** - Keep the URL the same to track the same route
3. **Different routes** - Edit URL in monitor_flight_prices.py for other routes
4. **Backup CSV** - Copy flight_prices.csv occasionally as backup

## Changing the Route

Edit `monitor_flight_prices.py` line ~120:

```python
url = "https://www.aviasales.ru/search/MOW1401CMB1"
#                                      ^^^^^^^^^^^^
#                                      Origin/Date/Dest/Date
```

Format: `ORIGIN[DATE]DESTINATION[DATE]`
- MOW = Moscow
- CMB = Colombo
- 1401 = January 14

Example for Moscow to Dubai on Feb 20:
```python
url = "https://www.aviasales.ru/search/MOW2002DXB1"
```
