# Source: https://docs.helicone.ai/rest/prompts/post-v1prompt-2025-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Prompts

> Search and filter prompts with pagination

Retrieves a paginated list of prompts based on search criteria and tag filters.

### Request Body

<ParamField body="search" type="string" required>
  Search term to filter prompts by name
</ParamField>

<ParamField body="tagsFilter" type="string[]" required>
  Array of tags to filter prompts (shows prompts with any of these tags)
</ParamField>

<ParamField body="page" type="number" required>
  Page number for pagination (0-based)
</ParamField>

<ParamField body="pageSize" type="number" required>
  Number of prompts to return per page
</ParamField>

### Response

Returns an array of prompt objects matching the search criteria.

<ResponseField name="id" type="string">
  Unique identifier of the prompt
</ResponseField>

<ResponseField name="name" type="string">
  Name of the prompt
</ResponseField>

<ResponseField name="tags" type="string[]">
  Array of tags associated with the prompt
</ResponseField>

<ResponseField name="created_at" type="string">
  ISO timestamp when the prompt was created
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST "https://api.helicone.ai/v1/prompt-2025/query" \
    -H "Authorization: Bearer $HELICONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "search": "support",
      "tagsFilter": ["chatbot", "customer"],
      "page": 0,
      "pageSize": 10
    }'
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/query', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      search: "support",
      tagsFilter: ["chatbot", "customer"],
      page: 0,
      pageSize: 10
    }),
  });

  const prompts = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  [
    {
      "id": "prompt_123",
      "name": "Customer Support Bot",
      "tags": ["support", "chatbot"],
      "created_at": "2024-01-15T10:30:00Z"
    },
    {
      "id": "prompt_456",
      "name": "Support Ticket Classifier",
      "tags": ["support", "classification"],
      "created_at": "2024-01-14T09:15:00Z"
    }
  ]
  ```
</ResponseExample>
