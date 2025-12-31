# Source: https://docs.deepconverse.com/product-docs/analytics/export-api/messages-endpoint.md

# Messages Endpoint

The Messages endpoint returns data about the messages within a Conversation. This will include information like the type, sender, the time the message was sent and message specific data.

| **Message ID** (\_id)                 | The message's unique ID.                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Time** (time)                       | The time the message was sent                                                                           |
| **Conversation ID** (conversationId)  | The unique ID of the conversation the message belongs to.                                               |
| **Type of the Message** (type)        | The type of message                                                                                     |
| **Message data** (outMsg)             | The details of the message sent by the chatbot                                                          |
| **User Action Type** (userActionType) | The type of action taken by the user. This value only exists for type **UserInput**                     |
| **User Input** (userInput)            | The value of userInput done by the customer. This can be the content of text, quick reply or form input |

Here is a sample request for the messages endpoint

```python
import requests

url = "https://api.converseapps.com/conversations/export/v1/messages"

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

To iterate through the results pass the `cursor` value till the cursor returned by the API is `null.`

Optional: You can use the `conversation_id` parameter to fetch messages for a specific conversation.
