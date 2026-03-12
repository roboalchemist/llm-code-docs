# Source: https://docs.acceldata.io/api/create-persistence-configuration.md

# Create Persistence Configuration

Creates a new persistence configuration for the tenant.

### Endpoint

```bash
POST /catalog-server/api/persistence/configs
```



### Request Body Parameters

| **Field** | **Type** | **Description** | 
| ---- | ---- | ---- | 
| name | string | Unique configuration name | 
| description | string | Optional description | 
| categoriesConfig | object | Template configuration for record categories | 


### Sample Request

```bash
curl -X POST "https://{HOST}/catalog-server/api/persistence/configs" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "team_a_config",
    "categoriesConfig": {
      "good": {
        "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
        "format": "PARQUET"
      },
      "bad": {
        "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
        "format": "PARQUET"
      },
      "metadata": {
        "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{REQUEST_ID}}/{{RECORD_TYPE}}"
      }
    }
  }'
```



### Response (201 Created)

```json
{
    "id": 29,
    "tenantId": "acceldata2",
    "name": "my-custom-config-5",
    "categoriesConfig": {
        "good": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
            "format": "PARQUET"
        },
        "bad": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
            "format": "PARQUET"
        },
        "metadata": {
            "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}"
        }
    },
    "description": "Custom config with RECORD_TYPE variable",
    "isDefault": false,
    "createdAt": 1770279775803,
    "updatedAt": 1770279775803,
    "createdBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "lastUpdatedBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
    "policyCount": null
}
```

