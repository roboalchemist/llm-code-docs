# Source: https://docs.acceldata.io/api/add-tags-to-a-policy.md

# Add Tags to a Policy

Use this endpoint to add a tag to a specific policy by making an HTTP POST request to the provided URL.

## Endpoint

```http
POST /catalog-server/api/rules/:id/tag
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `id` | string | Yes | The ID of the policy to which the tag will be added. | 


## Example Request Body

```json
{
  "ruleTag": {
    "name": "critical"
  }
}
```



## Sample Request

```bash
curl -X POST "https://{{HOST}}/catalog-server/api/rules/14716/tag" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}" \
  -H "Content-Type: application/json" \
  -d '{
    "ruleTag": {
      "name": "critical"
    }
  }'
```

