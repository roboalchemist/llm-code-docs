# --- Full Pipeline ---
sequential_pipeline_agent = SequentialAgent(
    name="DynamicTravelPlannerPipeline",
    sub_agents=[
        input_resolution_agent,
        weather_agent,
        restaurant_agent,
        hotel_agent,
        itinerary_generator_agent
    ],
    description="Orchestrates the travel planning flow from user input to final itinerary."
)