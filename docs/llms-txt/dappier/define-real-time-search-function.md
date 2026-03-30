# Define Real-Time Search Function
@function_tool
def dappier_real_time_search(query: str, ai_model_id: str) -> str:
    """Fetches real-time search results from Dappier based on the user's query.

    Args:
        query (str): The user's query for real-time data.
        ai_model_id (str): The AI model ID to use for the query, dynamically set by the agent.
            Possible values:
            - "am_01j0rzq4tvfscrgzwac7jv1p4c" (General real-time web search, including news, weather, and events.)
            - "am_01j749h8pbf7ns8r1bq9s2evrh" (Stock market data with real-time financial news and stock prices.)

    Returns:
        str: A response message containing the real-time data results.
    """
    print(Fore.RED + f"CALLING TOOL - dappier_real_time_search: {ai_model_id}\n" + Style.RESET_ALL)
    print(Fore.GREEN + f"Query: {query}\n" + Style.RESET_ALL)
    response = dappier_client.search_real_time_data(query=query, ai_model_id=ai_model_id)
    return response.message if response else "No real-time data found."
```

### Fetching AI-Powered Recommendations

This function fetches AI-powered content recommendations from Dappier based on the user's query

```python Python theme={null}