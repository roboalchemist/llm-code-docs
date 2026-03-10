# Print the content of the response
print(chat_response.choices[0].message.content)

```
  </TabItem>
  <TabItem value="typescript" label="typescript">

```typescript


const apiKey = process.env["MISTRAL_API_KEY"];

const client = new Mistral({ apiKey: apiKey });

const chatResponse = await client.chat.complete({
  model: "pixtral-12b",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        {
          type: "image_url",
          imageUrl: "https://tripfixers.com/wp-content/uploads/2019/11/eiffel-tower-with-snow.jpeg",
        },
      ],
    },
  ],
});

console.log("JSON:", chatResponse.choices[0].message.content);
```

  </TabItem>
  <TabItem value="curl" label="curl">

```bash
curl https://api.mistral.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -d '{
    "model": "pixtral-12b-2409",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": "https://tripfixers.com/wp-content/uploads/2019/11/eiffel-tower-with-snow.jpeg"
          }
        ]
      }
    ],
    "max_tokens": 300
  }'
```
  </TabItem>
</Tabs>

## Passing a Base64 Encoded Image
If you have an image or a set of images stored locally, you can pass them to the model in base64 encoded format. Base64 encoding is a common method for converting binary data into a text format that can be easily transmitted over the internet. This is particularly useful when you need to include images in API requests.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```py


from mistralai import Mistral

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None