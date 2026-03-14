# Source: https://novita.ai/docs/api-reference/gpu-instance-create-container-registry-auth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Container Registry Authentication

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="name" type="string" required={true} />

<ParamField body="username" type="string" required={true} />

<ParamField body="password" type="string" required={true} />

## Example

Request

```bash  theme={"system"}
curl --request POST \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/repository/auth/save' \
  --header 'Authorization: Bearer {{API Key}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "<string>",
    "username": "<string>",
    "password": "<string>"
  }'
```

Response

```json  theme={"system"}
{}
```


Built with [Mintlify](https://mintlify.com).