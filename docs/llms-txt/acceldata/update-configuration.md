# Source: https://docs.acceldata.io/api/update-configuration.md

# Update Configuration

Update an existing persistence configuration.

### Endpoint

```bash
PUT /catalog-server/api/persistence/configs/{id}
```



### Path Parameter

| Parameter | Description | 
| ---- | ---- | 
| id | Configuration ID to update | 


### Sample Request

```bash
curl -X PUT "https://{HOST}/catalog-server/api/persistence/configs/29" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-updated-config",
    "categoriesConfig": {
        "good": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy/MM/dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
            "format": "CSV"
        },
        "bad": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy/MM/dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
            "format": "CSV"
        },
        "metadata": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy/MM/dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}"
        }
    },
    "description": "Updated config with different date format"
  }'
```



### Sample Response (200 OK)

```bash
{
    "id": 29,
    "tenantId": "acceldata2",
    "name": "my-updated-config",
    "categoriesConfig": {
        "good": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy/MM/dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
            "format": "CSV"
        },
        "bad": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy/MM/dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
            "format": "CSV"
        },
        "metadata": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy/MM/dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}"
        }
    },
    "description": "Updated config with different date format",
    "isDefault": false,
    "createdAt": 1770279775803,
    "updatedAt": 1770279827558,
    "createdBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "lastUpdatedBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "policyCount": null
}
```

