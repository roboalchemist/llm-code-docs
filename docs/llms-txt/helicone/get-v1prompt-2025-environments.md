# Source: https://docs.helicone.ai/rest/prompts/get-v1prompt-2025-environments.md

# Get Environments

> Get all available environments across your prompts

Returns a list of all environment names that have been used across your prompt versions.

### Response

<ResponseField name="environments" type="string[]">
  Array of environment names (e.g., \["production", "staging", "development"])
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X GET "https://api.helicone.ai/v1/prompt-2025/environments" \
    -H "Authorization: Bearer $HELICONE_API_KEY"
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/environments', {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
    },
  });

  const environments = await response.json();
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  [
    "production",
    "staging",
    "development"
  ]
  ```
</ResponseExample>
