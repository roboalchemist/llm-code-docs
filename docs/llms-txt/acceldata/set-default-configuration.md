# Source: https://docs.acceldata.io/api/set-default-configuration.md

# Set Default Configuration

Set a configuration as the tenant’s default persistence configuration.

### Endpoint

```bash
POST /catalog-server/api/persistence/configs/{id}/set-default
```



### Path Parameter

| Parameter | Description | 
| ---- | ---- | 
| id | Configuration ID | 


### Sample Response (200 OK)

```json
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
    "isDefault": true,
    "createdAt": 1770279775803,
    "updatedAt": 1770279875546,
    "createdBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "lastUpdatedBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "policyCount": null
}
```

