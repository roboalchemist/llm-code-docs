# Step 2: Call Dappier API for Weather
weather_query = f"What is the weather in {location} today?"
dappier_url = "https://api.dappier.com/app/aimodel/am_01j06ytn18ejftedz6dyhz2b15"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <YOUR_DAPPIER_API_KEY>'
}

weather_payload = json.dumps({"query": weather_query})
weather_response = requests.post(dappier_url, headers=headers, data=weather_payload)
weather_data = weather_response.json().get('results')