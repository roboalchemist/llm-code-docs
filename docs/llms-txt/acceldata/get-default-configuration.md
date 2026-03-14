# Source: https://docs.acceldata.io/api/get-default-configuration.md

# Get Default Configuration

Retrieve the tenant's default persistence configuration.

### Endpoint

```bash
GET /catalog-server/api/persistence/configs/default
```



### Sample Request

```bash
curl -X GET "https://{HOST}/catalog-server/api/persistence/configs/default" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



### Response (200 OK)

```json
{
    "id": 2,
    "tenantId": "acceldata2",
    "name": "Acceldata",
    "categoriesConfig": {
        "good": {
            "suffixTemplate": "{{POLICY_TYPE}}-{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
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
    "description": "Default persistence configuration",
    "isDefault": true,
    "createdAt": 1766474786472,
    "updatedAt": 1769750162451,
    "createdBy": "system/torch-catalog-server",
    "lastUpdatedBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "policyCount": null
}
```

