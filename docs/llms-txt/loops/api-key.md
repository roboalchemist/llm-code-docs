# Source: https://loops.so/docs/api-reference/api-key.md

# API key

> Test that an API key is valid.

## Request

No parameters.

## Response

### Success

<ResponseField name="success" type="boolean" required />

<ResponseField name="teamName" type="string" required>
  The name of the team the API key belongs to.
</ResponseField>

### Error

A `401 Forbidden` will be returned if the API key is invalid.

<Info>
  Deprecated fields will be removed in the future so avoid using them in your code.
</Info>

<ResponseField name="success" type="boolean" required />

<ResponseField name="message" type="string" required>
  "Invalid API key"
</ResponseField>

<ResponseField name="error" type="string" deprecated>
  "Invalid API key"
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  {
    "success": true,
    "teamName": "My team"
  }
  ```

  ```json 401 response theme={"dark"}
  {
    "success": false,
    "message": "Invalid API key",
    "error": "Invalid API key"
  }
  ```
</ResponseExample>
