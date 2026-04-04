# init the client but point it to TGI
client = MistralClient(api_key="-", endpoint="http://127.0.0.1:8080")
chat_response = client.chat(
    model="-",
    messages=[
      ChatMessage(role="user", content="What is the best French cheese?")
    ]
)

print(chat_response.choices[0].message.content)
```

  </TabItem>
  <TabItem value="openai" label="Using OpenAI Client" default>

```python
from openai import OpenAI