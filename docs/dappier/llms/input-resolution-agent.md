# --- Input Resolution Agent ---
input_resolution_agent = LlmAgent(
    name="TravelInputResolutionAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, extract the following structured information from the user's travel request:

1. City name or destination
2. Start date of travel (in YYYY-MM-DD format)
3. Number of days for the trip

If any of the above details are missing, ask the user for the missing information one by one in a natural and friendly tone.

Do not proceed until all three values are collected.

Once all values are available, return them as:
- city
- travel_date
- num_days

Example final output:
- city: Tokyo
- travel_date: 2024-06-15
- num_days: 3
""",
    description="Gathers and confirms city, date, and trip duration. Prompts for missing info if needed.",
    output_key="travel_inputs"
)
```

## ☀️ Weather Insights Agent

Fetches upcoming weather forecast for the destination using real-time data.

```python  theme={null}
from google.adk.agents import LlmAgent
from datetime import datetime
from .tools import real_time_travel_plan

GEMINI_MODEL = "gemini-2.0-flash"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")