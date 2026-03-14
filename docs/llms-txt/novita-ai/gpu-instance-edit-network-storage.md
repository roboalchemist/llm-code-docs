# Source: https://novita.ai/docs/api-reference/gpu-instance-edit-network-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit Network Storage

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="storageId" type="string" required={true}>
  The unique identifier for the storage.
</ParamField>

<ParamField body="storageName" type="string" required={true}>
  The name of the storage.
</ParamField>

<ParamField body="storageSize" type="string" required={true}>
  The size of the storage in appropriate units.
</ParamField>

## Example

Request

```bash  theme={"system"}
curl --request POST \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/networkstorage/update' \
  --header 'Authorization: Bearer {{API Key}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "storageId": "string",
    "storageName": "string",
    "storageSize": "string"
  }'
```

Response

```json  theme={"system"}
{}
```


Built with [Mintlify](https://mintlify.com).