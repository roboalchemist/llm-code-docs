# Step 3: Call Dappier API for Latest News
news_query = f"What is the latest news in {location} today?"
news_payload = json.dumps({"query": news_query})
news_response = requests.post(dappier_url, headers=headers, data=news_payload)
news_data = news_response.json().get('results')