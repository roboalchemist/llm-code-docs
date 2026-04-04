# init the client but point it to TGI
client = OpenAI(api_key="-", base_url="http://127.0.0.1:8080/v1")
chat_response = client.chat.completions.create(
    model="-",
    messages=[
      {"role": "user", "content": "What is deep learning?"}
    ]
)

print(chat_response)
```

  </TabItem>
  <TabItem value="curl" label="Using cURL" default>

```
curl http://127.0.0.1:8080/v1/chat/completions \
    -X POST \
    -d '{
  "model": "tgi",
  "messages": [
    {
      "role": "user",
      "content": "What is deep learning?"
    }
  ]
}' \
    -H 'Content-Type: application/json'
```

  </TabItem>
</Tabs>


### Using a generate endpoint

If you want more control over what you send to the server, you can use the `generate` endpoint. In this case, you're responsible of formatting the prompt with the correct template and stop tokens.

<Tabs>
  <TabItem value="python" label="Using Python" default>

```python