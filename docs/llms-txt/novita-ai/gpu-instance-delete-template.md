# Source: https://novita.ai/docs/api-reference/gpu-instance-delete-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Template

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="templateId" type="string" required={true}>
  The ID of the template to be deleted.
</ParamField>

## Response

<ResponseField name="templateId" type="string" required={false}>
  The ID of the deleted template.
</ResponseField>

## Example

Request

```bash  theme={"system"}
curl --request POST \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/template/delete' \
  --header 'Authorization: Bearer {{API Key}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "templateId": "<string>"
  }'
```

Response

```json  theme={"system"}
{
  "templateId": "<string>"
}
```


Built with [Mintlify](https://mintlify.com).