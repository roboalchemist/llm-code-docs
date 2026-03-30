# --- Weather Agent ---
weather_agent = LlmAgent(
    name="WeatherInsightsAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, use real-time data to fetch a weather forecast for the given city and travel date.

Use the following input:
{{travel_inputs}}

Provide a short weather summary for each day of the trip including temperature, conditions (e.g., sunny, rainy), and any alerts or recommendations.

Output format:
### Weather Forecast
- Day 1 (June 10): 28°C, Sunny
- Day 2 (June 11): 26°C, Light rain
- Day 3 (June 12): 27°C, Cloudy
""",
    description="Provides real-time weather forecast for the trip.",
    tools=[real_time_travel_plan],
    output_key="weather_summary"
)
```

## 🍽️ Restaurant Discovery Agent

Finds top local restaurants for the destination city using real-time data.

```python  theme={null}
from google.adk.agents import LlmAgent
from datetime import datetime
from .tools import real_time_travel_plan

GEMINI_MODEL = "gemini-2.0-flash"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")