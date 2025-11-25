# Source: https://docs.helicone.ai/rest/prompts/delete-v1prompt-2025-promptid-versionid.md

# Delete Prompt Version

> Delete a specific version of a prompt

Permanently deletes a specific version of a prompt while keeping the prompt and other versions intact.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

<ParamField path="versionId" type="string" required>
  The unique identifier of the prompt version to delete
</ParamField>

### Response

Returns `null` on successful deletion.

<RequestExample>
  ```bash cURL theme={null}
  curl -X DELETE "https://api.helicone.ai/v1/prompt-2025/prompt_123/version_456" \
    -H "Authorization: Bearer $HELICONE_API_KEY"
  ```

  ```typescript TypeScript theme={null}
  const response = await fetch('https://api.helicone.ai/v1/prompt-2025/prompt_123/version_456', {
    method: 'DELETE',
    headers: {
      'Authorization': `Bearer ${HELICONE_API_KEY}`,
    },
  });
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  null
  ```
</ResponseExample>
