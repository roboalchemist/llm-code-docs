# Source: https://novita.ai/docs/api-reference/gpu-instance-list-container-registry-auth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Container Registry Auth

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseField name="data" type="object[]" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="id" type="string" required={false} />

    <ResponseField name="name" type="string" required={false} />

    <ResponseField name="username" type="string" required={false} />

    <ResponseField name="password" type="string" required={false} />
  </Expandable>
</ResponseField>

## Example

Request

```bash  theme={"system"}
curl --request GET \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/repository/auths' \
  --header 'Authorization: Bearer {{API Key}}'
```

Response

```json  theme={"system"}
{
  "data": [
    {
      "id": "75irlsvvsehnqdajg2r481mjk54ecodc",
      "name": "test",
      "username": "uuuu",
      "password": "1111"
    },
    {
      "id": "eih4rdk77avum5lyau291w1i54zd897w",
      "name": "test",
      "username": "uuuu",
      "password": "1111"
    }
  ]
}
```


Built with [Mintlify](https://mintlify.com).