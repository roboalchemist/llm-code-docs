# Source: https://docs.acceldata.io/api/list-policy-tags.md

# List Tags of a Policy

Use this endpoint to return the tags associated with a particular policy.

## Endpoint

```http
POST /catalog-server/api/rules/:id/tags
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `id` | string | Yes | The ID of the policy to fetch tags. | 


## Sample Request

```bash
curl -X POST "https://{{HOST}}/catalog-server/api/rules/14716/tags" \
  -H "Content-Type: application/json" \
  -d '{ "tags": ["critical", "finance"] }'
```

