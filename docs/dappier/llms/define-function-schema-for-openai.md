# Define function schema for OpenAI
functions = [
    {
        "name": "fetch_financial_news",
        "description": "Fetch the latest financial news based on a topic.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The financial topic to search for (e.g., earnings, tech stocks)"
                }
            },
            "required": ["query"]
        }
    }
]