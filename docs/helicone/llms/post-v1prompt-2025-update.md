# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Prompt

> Create a new version of an existing prompt

Creates a new version of an existing prompt with updated content. Can create either a major or minor version.

### Request Body

<ParamField body="promptId" type="string" required>
  The unique identifier of the prompt to update
</ParamField>

<ParamField body="promptVersionId" type="string" required>
  The unique identifier of the current prompt version to base the update on
</ParamField>

<ParamField body="newMajorVersion" type="boolean" required>
  Whether to create a new major version (true) or minor version (false)
</ParamField>

<ParamField body="environment" type="string">
  Optional environment to set for this new version (e.g., "production", "staging", "development")
</ParamField>

<ParamField body="commitMessage" type="string" required>
  A description of the changes made in this version
</ParamField>

<ParamField body="promptBody" type="OpenAIChatRequest" required>
  The updated prompt body following OpenAI chat completion format
</ParamField>

### Response

<ResponseField name="id" type="string">
  Unique identifier of the new prompt version
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025/update" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "promptId": "prompt_123",
      "promptVersionId": "version_456",
      "newMajorVersion": true,
      "environment": "production",
      "commitMessage": "Updated system prompt for better customer interactions",
      "promptBody": {
        "model": "gpt-4",
        "messages": [
          {
            "role": "system",
            "content": "You are an expert customer support assistant with deep knowledge of our products."
          }
        ],
        "temperature": 0.7
      }
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/update', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      promptId: "prompt_123",
      promptVersionId: "version_456",
      newMajorVersion: true,
      environment: "production",
      commitMessage: "Updated system prompt for better customer interactions",
      promptBody: {
        model: "gpt-4",
        messages: [
          {
            role: "system",
            content: "You are an expert customer support assistant with deep knowledge of our products."
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
    "id": "version_789"
  }
  ```
</ResponseExample>
