#!/bin/bash
# Flight Price Monitor - Simple wrapper script

set -e

cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

echo "Starting flight price monitor..."
echo ""

# Run the monitor to capture prices
python monitor_flight_prices.py

# Parse and display the results
echo ""
echo "Parsing captured prices..."
python show_prices.py

echo ""
echo "✅ Done!"
echo ""
echo "📊 Results saved to:"
echo "   - flight_prices.csv (main price database - appends each run)"
echo "   - aviasales_screenshot_*.png (visual confirmation)"
echo "   - api_responses_*.json (raw data)"
echo ""
echo "💡 View price history: source venv/bin/activate && python view_prices.py"
