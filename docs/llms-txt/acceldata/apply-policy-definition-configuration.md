# Source: https://docs.acceldata.io/api/apply-policy-definition-configuration.md

# Apply Policy Definition Configuration

This endpoint applies the uploaded policy definitions into the current environment.

This step:

- Creates new policies
- Updates existing policies
- Applies tags, versions, and schedules

This is the final step of the import workflow.

## Endpoint

```http
POST /catalog-server/api/rules/import/policy-definitions/apply-config
```



## Request Body

The request body requires a reference to the uploaded config (returned from `upload-config`).
 It may also include flags for overwriting behavior.

### Typical Body Structure

```json
{
  "configUploadId": "12345",
  "overwriteExisting": true
}
```



Structure depends on your schema; this matches the import pipeline behavior.

## Sample Request

```bash
curl -X POST "https://{{HOST}}/catalog-server/api/rules/import/policy-definitions/apply-config" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}" \
  -H "Content-Type: application/json" \
  -d '{
        "configUploadId": "12345",
        "overwriteExisting": true
      }'
```

