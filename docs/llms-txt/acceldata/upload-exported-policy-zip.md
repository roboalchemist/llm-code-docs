# Source: https://docs.acceldata.io/api/upload-exported-policy-zip.md

# Upload Exported Policy Definition ZIP

This endpoint uploads the exported ZIP file (from the Export API or UI) into the import pipeline. The uploaded file is validated, parsed, and prepared for application.

Use this step right before applying policies to a target environment.

## Endpoint

```http
POST /catalog-server/api/rules/import/policy-definitions/upload-config
```



## Request Form Data

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `file` | file | Yes | ZIP file containing exported policy definitions | 


## Sample Request

```bash
curl -X POST "https://{{HOST}}/catalog-server/api/rules/import/policy-definitions/upload-config" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}" \
  -F "file=@policies_export.zip"
```

