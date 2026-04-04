# --- Hotel Agent ---
hotel_agent = LlmAgent(
    name="BudgetHotelFinderAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, use real-time data to find budget-friendly hotels in the destination city.

Use the following input:
{{travel_inputs}}

Recommend 3–5 options that are affordable, clean, and well-reviewed. Include hotel name, price range, and a short note on location or features.
""",
    description="Finds affordable and well-rated hotels for the destination.",
    tools=[real_time_travel_plan],
    output_key="hotel_recommendations"
)
```

## 📅 Itinerary Generator Agent

Synthesizes the final multi-day itinerary using real-time insights from weather, restaurants, and hotels.

```python  theme={null}
from google.adk.agents import LlmAgent
from datetime import datetime

GEMINI_MODEL = "gemini-2.0-flash"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")