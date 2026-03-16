# Source: https://docs.picaos.com/api-reference/core/create-or-get-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or Get User

> Create a new user, or get an existing user by email

## Body Parameters

<ParamField body="email" type="string" required>
  The email address of the user to create
</ParamField>

## Response

<ResponseField name="id" type="string">
  The unique identifier for the user
</ResponseField>

<ResponseField name="email" type="string">
  The email address of the user
</ResponseField>

<ResponseField name="throughput" type="number">
  The rate limit throughput for the user
</ResponseField>

<ResponseField name="secrets" type="object">
  The API keys for the user

  <Expandable title="Secrets properties">
    <ResponseField name="live" type="string">
      The live environment API key
    </ResponseField>

    <ResponseField name="sandbox" type="string">
      The sandbox/test environment API key
    </ResponseField>
  </Expandable>
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X POST 'https://api.picaos.com/internal/v3/users/create-or-get' \
    -H 'x-pica-secret: YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "email": "test@example.com"
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
      "id": "526907ff-932e-4222-81ff-83f8adefad05",
      "email": "test@example.com",
      "throughput": 100,
      "secrets": {
        "live": "<USER_LIVE_KEY>",
        "sandbox": "<USER_SANDBOX_KEY>"
      }
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).