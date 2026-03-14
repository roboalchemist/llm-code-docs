# Source: https://novita.ai/docs/api-reference/gpu-instance-create-network-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Network Storage

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="clusterId" type="string" required={true} />

<ParamField body="storageName" type="string" required={true} />

<ParamField body="storageSize" type="integer" required={true} />

## Example

Request

```bash  theme={"system"}
curl --request POST \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/networkstorage/create' \
  --header 'Authorization: Bearer {{API Key}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "clusterId": "string",
    "storageName": "string",
    "storageSize": 0
  }'
```

Response

```json  theme={"system"}
"<string>"
```


Built with [Mintlify](https://mintlify.com).