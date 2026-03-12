# Source: https://docs.acceldata.io/api/pre-check-policy-exports.md

# Pre-Check Policy Definition Export

Use this endpoint to retrieve **export limitations and validation results** before exporting policy definitions.
 The pre-check evaluates provided filters (tags, rule types, versions, etc.) and returns what is eligible for export, what might be excluded, and any warnings.

This is helpful when teams manage hundreds of reliability policies and want to confirm what will be included in the export file.

## Endpoint

```http
GET /catalog-server/api/rules/export/policy-definitions/pre-check
```



## Query Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `policyIds` | array (comma-separated string) | No | Export specific policy IDs only | 
| `tags` | array (comma-separated string) | No | Filter by policy tags | 
| `policyTypes` | array (comma-separated string) | No | Filter by rule type (DATA_QUALITY, RECONCILIATION, etc.) | 
| `includeInactive` | boolean | No | Whether to include inactive policies | 
| `version` | string | No | Export only policies matching a specific version | 


These may vary depending on your implementation; the API supports flexible filtering.

## Sample Request

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/rules/export/policy-definitions/pre-check?policyTypes=DATA_QUALITY,RECONCILIATION&tags=finance,critical" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}" \
  -H "Accept: application/json"
```

