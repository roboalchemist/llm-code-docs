# Source: https://docs.acceldata.io/api/list-persistence-configurations.md

# List Persistence Configurations

Retrieve all persistence configurations for the tenant.

### Endpoint

```bash
GET /catalog-server/api/persistence/configs
```



### Query Parameters

| **Parameter** | **Description** | 
| ---- | ---- | 
| page | Page number | 
| size | Number of records per page | 
| sortBy | Sort results | 
| name | Filter by configuration name | 
| includePolicyCount | Include number of policies referencing configuration | 


### Sample Request

```bash
curl -X GET "https://{HOST}/catalog-server/api/persistence/configs?page=0&size=2&includePolicyCount=true&sortBy=updatedAt:DESC" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



### Response (200 OK)

```json
{
    "data": [
        {
            "id": 27,
            "tenantId": "acceldata2",
            "name": "pc-saved",
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
            "description": "",
            "isDefault": false,
            "createdAt": 1770105057092,
            "updatedAt": 1770105057092,
            "createdBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
            "lastUpdatedBy": "b8f124d1-7701-4971-91ee-7538b7a244d4",
            "policyCount": 0
        },
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
            "policyCount": 1
        }
    ],
    "meta": {
        "count": 6,
        "page": 0,
        "size": 2
    }
}
```

