# Function to call from OpenAI
def fetch_financial_news(query: str) -> str:
    """Fetch real-time financial news using Dappier SDK."""
    response = dappier_client.search_real_time_data(query=query, ai_model_id="am_01j749h8pbf7ns8r1bq9s2evrh")
    return response.message if response else "No financial news found."