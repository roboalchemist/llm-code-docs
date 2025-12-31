# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025.md

# Create Prompt

> Create a new prompt with initial version

Creates a new prompt with the specified name, tags, and initial prompt body. Returns the prompt ID and initial version ID.

### Request Body

<ParamField body="name" type="string" required>
  Name of the prompt
</ParamField>

<ParamField body="tags" type="string[]" required>
  Array of tags to associate with the prompt
</ParamField>

<ParamField body="promptBody" type="OpenAIChatRequest" required>
  The initial prompt body following OpenAI chat completion format
</ParamField>

### Response

<ResponseField name="id" type="string">
  Unique identifier of the created prompt
</ResponseField>

<ResponseField name="versionId" type="string">
  Unique identifier of the initial prompt version
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "Customer Support Bot",
      "tags": ["support", "chatbot"],
      "promptBody": {
        "model": "gpt-4",
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful customer support assistant."
          }
        ],
        "temperature": 0.7
      }
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: "Customer Support Bot",
      tags: ["support", "chatbot"],
      promptBody: {
        model: "gpt-4",
        messages: [
          {
            role: "system",
            content: "You are a helpful customer support assistant."
          }
        ],
        temperature: 0.7
      }
    }),
  });

  const result = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "id": "prompt_123",
    "versionId": "version_456"
  }
  ```
</ResponseExample>
