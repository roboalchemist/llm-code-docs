# Secure API Key Setup
os.environ["DAPPIER_API_KEY"] = getpass.getpass("Enter your Dappier API Key: ")
dappier_client = Dappier(api_key=os.environ["DAPPIER_API_KEY"])

@function_tool
def fetch_financial_news(query: str) -> str:
    """Fetches real-time financial news using Dappier SDK."""
    response = dappier_client.search_real_time_data(query=query, ai_model_id="am_01j749h8pbf7ns8r1bq9s2evrh")
    return response.message if response else "No financial news found."