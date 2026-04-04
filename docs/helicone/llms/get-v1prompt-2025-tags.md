# Source: https://docs.helicone.ai/rest/prompts/get-v1prompt-2025-tags.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Prompt Tags

> Retrieve all available prompt tags

Retrieves a list of all unique tags used across all prompts in the organization.

### Response

Returns an array of unique tag strings.

<RequestExample>
  ```bash cURL theme={null}
  curl -X GET "https://api.helicone.ai/v1/prompt-2025/tags" \
    -H "Authorization: Bearer $HELICONE_API_KEY"
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/tags', {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
    },
  });

  const tags = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  [
    "support",
    "chatbot",
    "classification",
    "customer",
    "analytics",
    "qa"
  ]
  ```
</ResponseExample>
