# Source: https://docs.acceldata.io/api/export-policies.md

# Export Policy Definitions

This API exports one or more reliability policy definitions based on the filters provided. The output is downloaded as a **ZIP file**, which contains policy metadata, rule definitions, and versioning information.

Use this endpoint to:

- Archive policies for version control
- Share reusable policies between teams
- Bulk export tagged policies (for example, “finance”, “PII”, etc.)

## Endpoint

```http
GET /catalog-server/api/rules/export/policy-definitions
```



## Query Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `policyIds` | array | No | Export specific policy IDs | 
| `tags` | array | No | Export policies containing these tags | 
| `policyTypes` | array | No | Filter by policy type | 
| `includeInactive` | boolean | No | Whether to include archived policies | 
| `version` | string | No | Export a specific policy version | 


## Sample Request

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/rules/export/policy-definitions?policyTypes=DATA_QUALITY&tags=critical" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}" \
  -o policies_export.zip
```



This will download a file named **policies_export.zip**.