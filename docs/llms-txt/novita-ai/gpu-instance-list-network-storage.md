# Source: https://novita.ai/docs/api-reference/gpu-instance-list-network-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Network Storage

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="pageNo" type="integer" required={false} />

<ParamField query="pageSize" type="integer" required={false} />

<ParamField query="storageName" type="string" required={false} />

<ParamField query="storageId" type="string" required={false} />

## Response

<ResponseField name="data" type="object[]" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="storageId" type="string" required={false} />

    <ResponseField name="storageName" type="string" required={false} />

    <ResponseField name="storageSize" type="integer" required={false} />

    <ResponseField name="clusterId" type="string" required={false} />

    <ResponseField name="clusterName" type="string" required={false} />

    <ResponseField name="price" type="string" required={false} />
  </Expandable>
</ResponseField>

<ResponseField name="total" type="integer" required={false} />

## Example

Request

```bash  theme={"system"}
curl --request GET \
  --url 'https://api.novita.ai/gpu-instance/openapi/v1/networkstorages/list' \
  --header 'Authorization: Bearer {{API Key}}'
```

Response

```json  theme={"system"}
{
  "data": [
    {
      "storageId": "d4e82677-3f80-4020-a731-d15b1c589aa8",
      "storageName": "123",
      "storageSize": 10,
      "clusterId": "5",
      "clusterName": "EU-01",
      "price": "100"
    },
    {
      "storageId": "082383c6-bc28-4bfa-a3b3-b6d6511bdf64",
      "storageName": "123",
      "storageSize": 10,
      "clusterId": "5",
      "clusterName": "EU-01",
      "price": "100"
    }
  ],
  "total": 2
}
```


Built with [Mintlify](https://mintlify.com).