# Source: https://docs.acceldata.io/api/manage-data-anomaly-policy-by-id.md

# Manage Policy by ID

These endpoints allow you to **retrieve, update, or delete a Data Anomaly policy** using its unique policy ID.
 Use these APIs in integrations, automated workflows, or when editing policies programmatically.

## Endpoints

| Method | Path | Description | 
| ---- | ---- | ---- | 
| GET | `/catalog-server/api/rules/profile-anomaly/:id` | Retrieve anomaly policy by ID | 
| PUT | `/catalog-server/api/rules/profile-anomaly/:id` | Update an anomaly policy | 
| DELETE | `/catalog-server/api/rules/profile-anomaly/:id` | Delete/archive an anomaly policy | 


## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `id` | integer | Yes | The ID of the anomaly policy. | 


## Sample Request

### Example: Get Policy

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/rules/profile-anomaly/12345" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}"
```



### Example: Update Policy

```bash
curl -X PUT "https://{{HOST}}/catalog-server/api/rules/profile-anomaly/12345" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}" \
  -H "Content-Type: application/json" \
  -d '{
    "rule": {
      "description": "Updated threshold logic",
      "enabled": false
    }
  }'
```

