# Source: https://docs.acceldata.io/api/get-configuration-by-id.md

# Get Configuration by ID

Retrieve a specific persistence configuration.

### Endpoint

```bash
GET /catalog-server/api/persistence/configs/{id}
```



### Path Parameters

| **Parameter** | **Description** | 
| ---- | ---- | 
| id | Configuration ID | 


### Sample Request

```bash
curl -X GET "https://{HOST}/catalog-server/api/persistence/configs/6" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



### Response (200 OK)

```json
{
    "id": 6,
    "tenantId": "acceldata2",
    "name": "my-custom-config-ii-updated-copy",
    "categoriesConfig": {
        "good": {
            "suffixTemplate": "{{POLICY_TYPE}}-{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/recordType={{RECORD_TYPE}}",
            "format": "PARQUET"
        },
        "bad": {
            "suffixTemplate": "{{POLICY_TYPE}}-{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
            "format": "PARQUET"
        },
        "metadata": {
            "suffixTemplate": "{{POLICY_TYPE}}-{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}"
        }
    },
    "description": "Custom config with RECORD_TYPE variable",
    "isDefault": false,
    "createdAt": 1766480019893,
    "updatedAt": 1770009538497,
    "createdBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "lastUpdatedBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "policyCount": null
}
```



### Error Response (404 Not Found)

```json
{
    "errors": [
        {
            "message": "Persistence storage config not found: 4",
            "status": 404,
            "details": null
        }
    ]
}
```

