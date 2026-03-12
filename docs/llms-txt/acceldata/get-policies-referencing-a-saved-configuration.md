# Source: https://docs.acceldata.io/api/get-policies-referencing-a-saved-configuration.md

# Get Policies Referencing a Saved Configuration

Lists all policies that reference a specific persistence configuration.

### Endpoint

```bash
GET /catalog-server/api/persistence/configs/{id}/referencing-policies
```



### Path Parameters

| **Parameter** | **Description** | 
| ---- | ---- | 
| id | Configuration ID | 


### Sample Request

```bash
curl -X GET "https://{HOST}/catalog-server/api/persistence/configs/26/referencing-policies" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



### Response (200 OK)

```json
{
    "policies": [
        {
            "id": 63,
            "name": "employee_dq_EMPLOYEE4_2opNA1ji",
            "ruleType": "DATA_QUALITY",
            "version": 6
        }
    ]
}
```

