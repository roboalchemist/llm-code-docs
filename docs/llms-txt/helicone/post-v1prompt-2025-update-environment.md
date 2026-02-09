# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025-update-environment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Version Environment

> Set the environment for a specific prompt version

Updates the environment for a specific prompt version. Environments can be "production", "staging", "development", or any custom environment name.

### Request Body

<ParamField body="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

<ParamField body="promptVersionId" type="string" required>
  The unique identifier of the prompt version to update
</ParamField>

<ParamField body="environment" type="string" required>
  The environment to set for this version (e.g., "production", "staging", "development")
</ParamField>

### Response

Returns `null` on successful update.

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025/update/environment" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "promptId": "prompt_123",
      "promptVersionId": "version_789",
      "environment": "production"
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/update/environment', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      promptId: "prompt_123",
      promptVersionId: "version_789",
      environment: "production"
    }),
  });
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  null
  ```
</ResponseExample>
