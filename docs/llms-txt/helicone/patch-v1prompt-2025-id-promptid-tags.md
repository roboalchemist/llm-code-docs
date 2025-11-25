# Source: https://docs.helicone.ai/rest/prompts/patch-v1prompt-2025-id-promptid-tags.md

# Update Prompt Tags

> Update the tags for a prompt

Updates the tags associated with a prompt. This replaces all existing tags with the new set provided.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

### Request Body

<ParamField body="tags" type="string[]" required>
  Array of tag strings to set for the prompt
</ParamField>

### Response

<ResponseField name="tags" type="string[]">
  The updated array of tags
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X PATCH "https://api.helicone.ai/v1/prompt-2025/id/prompt_123/tags" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "tags": ["customer-support", "v2", "production"]
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/id/prompt_123/tags', {
    method: 'PATCH',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      tags: ["customer-support", "v2", "production"]
    }),
  });

  const result = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  [
    "customer-support",
    "v2",
    "production"
  ]
  ```
</ResponseExample>
