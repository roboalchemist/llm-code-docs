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

// Encode the audio file in base64
const audio_file = fs.readFileSync('local_audio.mp3');
const audio_base64 = audio_file.toString('base64');

// Get the chat response
const chatResponse = await client.chat.complete({
  model: "voxtral-mini-latest",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "input_audio",
          input_audio: audio_base64,
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
console.log(chatResponse.choices[0].message.content);
```

  </TabItem>
  <TabItem value="curl" label="curl" default>

```bash
curl --location https://api.mistral.ai/v1/chat/completions \
  --header "Authorization: Bearer $MISTRAL_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "voxtral-mini-latest",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_audio",
            "input_audio": "<audio_base64>",
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

### Passing an Audio URL

You can also provide an url of a file.

<Tabs groupId="code">
  <TabItem value="python" label="python">

```python

from mistralai import Mistral