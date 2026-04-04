# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025-query-versions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Prompt Versions

> Retrieve all versions of a specific prompt

Retrieves all versions of a specific prompt, optionally filtered by major version.

### Request Body

<ParamField body="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

<ParamField body="majorVersion" type="number" optional>
  Filter versions by specific major version number
</ParamField>

### Response

Returns an array of prompt version objects.

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

<ResponseField name="created_at" type="string">
  ISO timestamp when the version was created
</ResponseField>

<ResponseField name="s3_url" type="string" optional>
  S3 URL where the prompt body is stored (if applicable)
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025/query/versions" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "promptId": "prompt_123",
      "majorVersion": 1
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/query/versions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      promptId: "prompt_123",
      majorVersion: 1
    }),
  });

  const versions = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  [
    {
      "id": "version_456",
      "model": "gpt-4",
      "prompt_id": "prompt_123",
      "major_version": 1,
      "minor_version": 0,
      "commit_message": "Initial version",
      "created_at": "2024-01-14T10:30:00Z"
    },
    {
      "id": "version_789",
      "model": "gpt-4",
      "prompt_id": "prompt_123",
      "major_version": 1,
      "minor_version": 1,
      "commit_message": "Minor improvements to system prompt",
      "created_at": "2024-01-15T14:20:00Z"
    }
  ]
  ```
</ResponseExample>
