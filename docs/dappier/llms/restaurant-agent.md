# --- Restaurant Agent ---
restaurant_agent = LlmAgent(
    name="RestaurantDiscoveryAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, use real-time data to discover top-rated local restaurants at the destination.

Use the following input:
{{travel_inputs}}

Find a mix of cuisines and recommend restaurants suitable for breakfast, lunch, and dinner. Include name, cuisine type, and a one-line description.
""",
    description="Finds popular local restaurants for the travel destination.",
    tools=[real_time_travel_plan],
    output_key="restaurant_recommendations"
)
```

## 🏨 Budget Hotel Finder Agent

Finds affordable and well-rated hotels near the destination using real-time data.

```python  theme={null}
from google.adk.agents import LlmAgent
from datetime import datetime
from .tools import real_time_travel_plan

GEMINI_MODEL = "gemini-2.0-flash"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")