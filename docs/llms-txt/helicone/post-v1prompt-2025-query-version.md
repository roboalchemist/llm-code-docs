# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025-query-version.md

# Get Prompt Version

> Retrieve a specific prompt version with its content

Retrieves detailed information about a specific prompt version, including the full prompt body content.

### Request Body

<ParamField body="promptVersionId" type="string" required>
  The unique identifier of the prompt version to retrieve
</ParamField>

### Response

<ResponseField name="id" type="string">
  Unique identifier of the prompt version
</ResponseField>

<ResponseField name="model" type="string">
  The model specified in the prompt
</ResponseField>

<ResponseField name="prompt_id" type="string">
  The ID of the parent prompt
</ResponseField>

<ResponseField name="major_version" type="number">
  The major version number
</ResponseField>

<ResponseField name="minor_version" type="number">
  The minor version number
</ResponseField>

<ResponseField name="commit_message" type="string">
  The commit message for this version
</ResponseField>

<ResponseField name="environment" type="string" optional>
  The environment this version is assigned to (e.g., "production", "staging")
</ResponseField>

<ResponseField name="created_at" type="string">
  ISO timestamp when the version was created
</ResponseField>

<ResponseField name="s3_url" type="string" optional>
  S3 URL where the prompt body is stored
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025/query/version" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "promptVersionId": "version_456"
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/query/version', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      promptVersionId: "version_456"
    }),
  });

  const version = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "id": "version_456",
    "model": "gpt-4",
    "prompt_id": "prompt_123",
    "major_version": 1,
    "minor_version": 2,
    "commit_message": "Updated system prompt for better responses",
    "environment": "production",
    "created_at": "2024-01-15T10:30:00Z",
    "s3_url": "https://s3.amazonaws.com/bucket/prompt-body.json"
  }
  ```
</ResponseExample>
