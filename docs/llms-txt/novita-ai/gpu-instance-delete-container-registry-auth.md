# Source: https://novita.ai/docs/api-reference/gpu-instance-delete-container-registry-auth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Container Registry Auth

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="id" type="string" required={true} />

## Example

Request

```bash  theme={"system"}
curl --request POST \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/repository/auth/delete' \
  --header 'Authorization: Bearer {{API Key}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "id": "<string>"
  }'
```

Response

```json  theme={"system"}
{}
```


Built with [Mintlify](https://mintlify.com).