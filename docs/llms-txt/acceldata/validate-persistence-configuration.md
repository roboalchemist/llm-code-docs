# Source: https://docs.acceldata.io/api/validate-persistence-configuration.md

# Validate Persistence Configuration

Validate a complete persistence configuration including all category templates before saving it. This endpoint checks for template syntax, uniqueness requirements, and path collisions between categories.

### Endpoint

```bash
POST /catalog-server/api/persistence/configs/validate
```



### Request Body

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `requireMetadata` | boolean | true for Spark policy (metadata required), false for Pushdown policy | 
| `categoriesConfig.good` | object | Configuration for good (passing) records | 
| `categoriesConfig.good.suffixTemplate` | string | Template for good records path | 
| `categoriesConfig.good.format` | string | Storage format: PARQUET, CSV, JSON, ORC | 
| `categoriesConfig.bad` | object | Configuration for bad (failing) records (same structure as good) | 
| `categoriesConfig.metadata` | object | Configuration for metadata. Required if requireMetadata is true | 
| `categoriesConfig.metadata.suffixTemplate` | string | Template for metadata path | 


### Sample Request

```bash
curl -X POST "https://{HOST}/catalog-server/api/persistence/configs/validate" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "requireMetadata": true,
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
    }
  }'
```



### Response (200 OK)

```json
{
  "valid": true
}
```



### Response (200 OK) - Invalid Template

```json
{
    "valid": false,
    "categoryErrors": {
        "good": "Template must contain at least one uniqueness variable: {{REQUEST_ID}} or {{EXECUTION_ID}}"
    }
}
```



### Response (200 OK) - Multiple Errors

```json
{
    "valid": false,
    "categoryErrors": {
        "good": "Template must contain at least one uniqueness variable: {{REQUEST_ID}} or {{EXECUTION_ID}}",
        "bad": "Template contains invalid characters in static text '$ABC': '$'. Allowed: Unicode letters, digits, _ - =",
        "metadata": "Template segment 'CON' is a Windows reserved name and cannot be used"
    }
}
```



### Response (200 OK) - Path Collision

```json
{
    "valid": false,
    "error": "Template collision detected: GOOD (good) and SUMMARY (metadata) records resolve to: 'data-quality/sample-policy/2026-02-04/data-quality-f64a6630-12de-4f89-88c1-2bf38066d91a'. Edit the category template in parentheses to resolve. Use {{RECORD_TYPE}} in your templates or make category templates distinct."
}
```

