# Print the content of the response
print(chat_response.choices[0].message.content)
```
  </TabItem>
  <TabItem value="typescript" label="typescript">

```typescript


// Retrieve the API key from environment variables
const apiKey = process.env["MISTRAL_API_KEY"];

// Initialize the Mistral client
const client = new Mistral({ apiKey: apiKey });

// Get the chat response
const chatResponse = await client.chat.complete({
  model: "voxtral-mini-latest",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "input_audio",
          input_audio: "https://download.samplelib.com/mp3/sample-15s.mp3",
        },
        {
          type: "text",
          text: "What's in this file?",
        },
      ],
    },
  ],
});

// Print the content of the response
console.log("JSON:", chatResponse.choices[0].message.content);
```

  </TabItem>
  <TabItem value="curl" label="curl" default>

```bash
curl --location https://api.mistral.ai/v1/chat/completions \
  --header "Authorization: Bearer $MISTRAL_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "voxtral-mini-2507",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_audio",
            "input_audio": "https://download.samplelib.com/mp3/sample-15s.mp3"
          },
          {
            "type": "text",
            "text": "What'\''s in this file?"
          }
        ]
      }
    ]
  }'
```
  </TabItem>
</Tabs>

### Passing an Uploaded Audio File

Alternatively, you can upload a local file to our cloud and then use a signed URL for the task.

<Tabs groupId="code">
  <TabItem value="python" label="python">

```python

from mistralai import Mistral