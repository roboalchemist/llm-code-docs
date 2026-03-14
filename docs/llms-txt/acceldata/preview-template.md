# Source: https://docs.acceldata.io/api/preview-template.md

# Preview Template

This endpoint allows you to preview how a persistence path template will be resolved before saving the configuration. It replaces the template variables (such as policy name, execution time, request ID, and record type) with sample values to generate the final storage path.

You can use this endpoint to verify that the template structure and variables produce the expected output path for a specific record category (good, bad, or metadata). This helps ensure that policy execution results will be stored in the correct location and format before applying the configuration.

### Endpoint

```bash
POST /catalog-server/api/persistence/configs/preview/{recordCategory}
```



### Path Parameter

| Parameter | Description | 
| ---- | ---- | 
| recordCategory | good, bad, or metadata | 


### Sample Request

```bash
curl -X POST "https://{HOST}/catalog-server/api/persistence/configs/preview/good" \
-H "accessKey: {ACCESS_KEY}" \
-H "secretKey: {SECRET_KEY}" \
-H "Content-Type: application/json" \
-d '{
  "suffixTemplate": "{{POLICY_TYPE}}/{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}"
}'
```



### Request Body

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `suffixTemplate` | string | Template string with variables. Must contain `{{REQUEST_ID}}` or `{{EXECUTION_ID}}` for uniqueness. | 


### Response (200 OK)

```json
{
  "resolvedSuffix": "data-quality-policy/2026-02-04/request123/successrecords",
  "contextUsed": {
       "policyType": "data-quality",
       "policyName": "sample-policy",
       "policyId": 12345,
       "executionId": 98765,
       "executionDateTime": 1770210106836,
       "requestId": "data-quality-b190394b-01af-4cee-8038-fb235224fae9",
       "recordType": "GOOD",
       "assetName": "orders_table",
       "datasourceName": "prod-database"
   }
}
```



### Error Response (400 Bad Request) - Missing uniqueness variable:

```json
{
    "errors": [
        {
            "message": "Template must contain at least one uniqueness variable: {{REQUEST_ID}} or {{EXECUTION_ID}}",
            "status": 400,
            "details": null
        }
    ]
}
```

