# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025-query-total-versions.md

# Get Prompt Version Counts

> Get version count statistics for a specific prompt

Retrieves statistics about the total number of versions and major versions for a specific prompt.

### Request Body

<ParamField body="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

### Response

<ResponseField name="totalVersions" type="number">
  Total number of versions (major and minor) for this prompt
</ResponseField>

<ResponseField name="majorVersions" type="number">
  Total number of major versions for this prompt
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025/query/total-versions" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "promptId": "prompt_123"
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/query/total-versions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      promptId: "prompt_123"
    }),
  });

  const versionCounts = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "totalVersions": 8,
    "majorVersions": 3
  }
  ```
</ResponseExample>
