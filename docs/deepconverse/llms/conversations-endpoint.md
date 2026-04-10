# Source: https://docs.deepconverse.com/product-docs/analytics/export-api/conversations-endpoint.md

# Conversations Endpoint

The Conversations endpoint returns data about the Conversations your bot has with your customers. Conversation data includes the following fields.

| **Conversation ID** (\_id)                       | Unique id for the conversation                                                                        |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Start Time** (startTime)                       | The conversation's start time.                                                                        |
| **Last conversation action time** (lastActionAt) | The time of last conversation update.                                                                 |
| **Locale** (locale)                              | Locale of the conversation                                                                            |
| **Tags** (tags)                                  | List of the tags added to the conversation such as resolved, informed, liveChat etc.                  |
| **Metadata** (metadata)                          | All the metadata stored as part of the conversation. This will include system and user set parameters |

Here is a sample request for the conversations endpoint

````python
```python
import requests

url = "https://api.converseapps.com/conversations/export/v1/conversations"

params={
  'start_time': 1696118400,
  'end_time': 1696550400,
  'bot_name': 'r3-218210',
  'per_page': 1000
}
headers = {
  'x-api-key': '<api_key>',
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```
````

To iterate through the results pass the `cursor` value till the cursor returned by the API is `null`
