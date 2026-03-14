# Source: https://docs.acceldata.io/api/manage-data-quality-by-name.md

# Manage Policies by Name

These APIs let you manage an existing Data Quality policy using its **name** instead of the numeric ID.  

This is useful in automated workflows or CI/CD pipelines where the **policy name** is stable and easier to reference than its internal ID.

## Endpoint(s)

```none
GET    /catalog-server/api/rules/data-quality/byName/:name           (get)
PUT    /catalog-server/api/rules/data-quality/byName/:name           (update)
DELETE /catalog-server/api/rules/data-quality/byName/:name           (delete/archive)
POST   /catalog-server/api/rules/data-quality/byName/:name/unarchive (unarchive)
PUT    /catalog-server/api/rules/data-quality/byName/:name/schedule  (toggle schedule)
GET    /catalog-server/api/rules/data-quality/byName/:name/items     (list items)
GET    /catalog-server/api/rules/data-quality/byName/:name/executions (list executions)
POST   /catalog-server/api/rules/data-quality/byName/:name/executions (execute policy)
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| name | string | Yes | Unique **name** of the Data Quality policy. | 


### Sample Request

**Manage a Data Quality policy by name**

```bash
curl -X PUT "https://{HOST}/catalog-server/api/rules/data-quality/byName/Customer_DQ_Policy" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "accessKey: $ACCESS_KEY" \
  -H "secretKey: $SECRET_KEY" \
  -d '{
    "description": "Updated DQ policy to check for null values and pattern mismatches on critical columns.",
    "status": "ACTIVE",
    "scheduled": true,
    "schedule": "0 2 * * *",
    "rules": [
      {
        "columnName": "email",
        "measurementType": "NULL_VALUES",
        "threshold": 0
      },
      {
        "columnName": "email",
        "measurementType": "PATTERN_MISMATCH",
        "pattern": "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$"
      },
      {
        "columnName": "country_code",
        "measurementType": "REFERENCE_CHECK",
        "referenceDataset": "valid_country_codes"
      }
    ],
    "tags": ["customer", "critical", "data-quality"]
  }'
```



What this does:

- Updates an existing Data Quality policy named `Customer_DQ_Policy`.
- Schedules it to run daily at 2 AM (`0 2 * * *`).
- Adds multiple DQ rules including:

    - Null check
    - Pattern validation
    - Reference check

- Attaches descriptive tags.