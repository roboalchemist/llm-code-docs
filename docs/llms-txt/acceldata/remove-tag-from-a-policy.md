# Source: https://docs.acceldata.io/api/remove-tag-from-a-policy.md

# Remove Tag from a Policy

Use this endpoint to **remove a single tag** from a policy.

## Endpoint

```http
DELETE /catalog-server/api/rules/:id/tag/:tagId
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `id` | string | Yes | ID of the policy | 
| `tagId` | string | Yes | ID of the tag to remove | 


## Sample Request

```bash
curl -X DELETE "https://{{HOST}}/catalog-server/api/rules/14716/tag/40723" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}"
```

