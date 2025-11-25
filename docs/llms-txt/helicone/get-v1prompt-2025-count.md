# Source: https://docs.helicone.ai/rest/prompts/get-v1prompt-2025-count.md

# Get Prompt Count

> Get the total number of prompts

Retrieves the total count of prompts in the organization.

### Response

Returns the total number of prompts as an integer.

<RequestExample>
  ```bash cURL theme={null}
  curl -X GET "https://api.helicone.ai/v1/prompt-2025/count" \
    -H "Authorization: Bearer $HELICONE_API_KEY"
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/count', {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
    },
  });

  const count = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  42
  ```
</ResponseExample>
