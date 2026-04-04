# Build a Real-Time Data Assistant
Source: https://docs.dappier.com/cookbook/recipes/dappier-real-time-data



Dappier’s Real Time Data model can help you access real-time google web search results including the latest news, weather, travel, deals and more.

You first need the API key to access this API. Please visit [Dappier Platform](https://platform.dappier.com) to sign up and create an API key under Settings > Profile > API Keys.

## Using Real Time Data API

Below is an example of an assistant that prints a good morning message by accessing the latest weather and news in a given location.

Using the Real Time Data API, you can access real-time data to enhance your application's functionality.

```python Python theme={null}
import requests
import json
import openai