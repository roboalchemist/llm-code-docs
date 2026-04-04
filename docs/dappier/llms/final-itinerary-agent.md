# --- Final Itinerary Agent ---
itinerary_generator_agent = LlmAgent(
    name="ItineraryGeneratorAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, generate a markdown-formatted travel itinerary using all the collected information.

Inputs:
{{travel_inputs}}
{{weather_summary}}
{{restaurant_recommendations}}
{{hotel_recommendations}}

Create a day-by-day itinerary including morning, afternoon, and evening activities. Recommend meals, include hotel check-in/check-out, and consider weather conditions when planning activities.

Output only the final markdown itinerary.
""",
    description="Generates a structured, multi-day itinerary based on all gathered insights.",
    output_key="markdown_itinerary"
)
```

## 🔁 Sequential Agent Pipeline

Defines the full multi-agent flow: collects inputs → fetches insights → generates itinerary.

```python  theme={null}
from google.adk.agents import SequentialAgent