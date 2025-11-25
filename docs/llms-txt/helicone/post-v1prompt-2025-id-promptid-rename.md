# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025-id-promptid-rename.md

# Rename Prompt

> Rename an existing prompt

Updates the name of an existing prompt.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt to rename
</ParamField>

### Request Body

<ParamField body="name" type="string" required>
  The new name for the prompt
</ParamField>

### Response

Returns `null` on successful rename.

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025/id/prompt_123/rename" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "Updated Customer Support Bot"
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/id/prompt_123/rename', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: "Updated Customer Support Bot"
    }),
  });
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  null
  ```
</ResponseExample>
