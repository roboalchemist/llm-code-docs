# Define AI Recommendations Function
@function_tool
def dappier_ai_recommendations(query: str, data_model_id: str) -> str:
    """Fetches AI-powered content recommendations from Dappier based on the user's query.

    Args:
        query (str): The user's query for recommendations.
        data_model_id (str): The Data Model ID to use for the query, dynamically set by the agent.
            Possible values:
            - "dm_01j0pb465keqmatq9k83dthx34" (Sports news)
            - "dm_01j0q82s4bfjmsqkhs3ywm3x6y" (Lifestyle news)
            - "dm_01j1sz8t3qe6v9g8ad102kvmqn" (Dog care advice from iHeartDogs)
            - "dm_01j1sza0h7ekhaecys2p3y0vmj" (Cat care advice from iHeartCats)
            - "dm_01j5xy9w5sf49bm6b1prm80m27" (Eco-friendly content from GreenMonster)
            - "dm_01jagy9nqaeer9hxx8z1sk1jx6" (General news from WISH-TV)
            - "dm_01jhtt138wf1b9j8jwswye99y5" (Local news from 9 and 10 News)

    Returns:
        str: A formatted response containing AI-powered recommendations.
    """
    print(Fore.RED + f"CALLING TOOL: dappier_ai_recommendations: {data_model_id}\n" + Style.RESET_ALL)
    print(Fore.GREEN + f"Query: {query}\n" + Style.RESET_ALL)
    response = dappier_client.get_ai_recommendations(query=query, data_model_id=data_model_id, similarity_top_k=5)
    results = response.response.results
    formatted_text = ""
    for result in results:
        formatted_text += (f"Title: {result.title}\n"
                           f"Author: {result.author}\n"
                           f"Published on: {result.pubdate}\n"
                           f"URL: {result.source_url}\n"
                           f"Image URL: {result.image_url}\n"
                           f"Summary: {result.summary}\n\n")
    return formatted_text or "No recommendations found."
```

***

## Create AI Agent

This AI agent will **determine whether to fetch real-time search results or AI recommendations** based on the user's query.

```python Python theme={null}
agent = Agent(
    name="Dappier Assistant",
    instructions="""
    You analyze the user's query and determine whether to use real-time search or AI recommendations.
    If the query involves stocks, finance, or current events, use `dappier_real_time_search`.
    If the query is about recommendations (e.g., news, lifestyle, sports, pets), use `dappier_ai_recommendations`.
    You MUST provide `ai_model_id` or `data_model_id` as necessary.
    Format responses in structured Markdown.
    """,
    tools=[dappier_real_time_search, dappier_ai_recommendations],
)
```

***

## Generate Task Prompt

A **function to dynamically generate a task prompt** based on the user's travel details.

```python Python theme={null}
def generate_task_prompt(travel_city: str, travel_date: str, num_days: str) -> str:
    return f"""Generate a {num_days}-day travel itinerary for {travel_city}, tailored to the real-time weather forecast for the selected date: {travel_date}. Follow these steps:

        Determine Current Date and Travel Period:
        Use Dappier's real-time search to identify the current date and calculate the trip duration based on user input.

        Fetch LifeStyle News:
        Retrieve LifeStyle news using Dappier AI Recommendations API for the given date and provide insight to the user.

        Fetch Weather Data:
        Retrieve the weather forecast for {travel_city} during the selected dates to understand the conditions for each day.

        Fetch Live Events Data:
        Use Dappier's real-time search to find live events happening in {travel_city} during the trip dates.

        Fetch Hotel Deals Data:
        Use Dappier's real-time search to find the best hotel deals with booking links in {travel_city} during the trip dates.

        Design the Itinerary:
        Use the weather insights, live events, hotel deals to plan activities and destinations that suit the expected conditions. For each suggested location:

        Output:
        Present latest life style news at first then. Present a detailed {num_days}-day itinerary, including timing, activities, booking links, weather information for each day and travel considerations. Ensure the plan is optimized for convenience and enjoyment.
    """
```

***

## Get User Input and Run AI Agent

This function **collects user input dynamically**, generates the **task prompt**, and executes the AI agent **asynchronously**.

```python Python theme={null}
async def main():
    """Asks user for travel details dynamically and executes AI agent"""

    # Ask for travel details dynamically
    travel_city = input("Enter the city you want to travel to: ")
    travel_date = input("Enter the start date of your travel (YYYY-MM-DD): ")
    num_days = input("Enter the number of days for your trip: ")

    # Generate task prompt
    task_prompt = generate_task_prompt(travel_city, travel_date, num_days)

    print(Fore.BLUE + f"\nExecuting AI Agent with prompt:\n{task_prompt}" + Style.RESET_ALL)

    # Execute AI agent with streaming results
    result = Runner.run_streamed(agent, task_prompt)

    print("\n\n=== Streaming Start ===\n\n")

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

    print("\n\n=== Streaming Complete ===")