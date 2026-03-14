# Source: https://docs.acceldata.io/api/user-defined-templates--udf-udt-.md

# User Defined Templates (UDF/UDT)

User-Defined Templates (UDTs) and UDF Templates allow users to create reusable logic:
 custom expressions, validation logic, or transformation blocks used in Data Quality rules.

These APIs handle:

- Creating & managing templates
- Validating templates
- Retrieving validation results

## Available Endpoints

| Action | Endpoint | 
| ---- | ---- | 
| Create Template | `POST /catalog-server/api/udf-templates` | 
| Insert Template | `GET /catalog-server/api/udf-templates` | 
| Get Template | `GET /catalog-server/api/udf-templates/:id` | 
| Update Template | `PUT /catalog-server/api/udf-templates/:id` | 
| Validate Template | `POST /catalog-server/api/udf-templates/:id/validate` | 
| Get Validation Result | `GET /catalog-server/api/udf-templates/validation/:jobId` | 


## Sample Request (Create UDF Template)

```bash
curl -X POST "https://{{HOST}}/catalog-server/api/udf-templates" \
  -H "Content-Type: application/json" \
  -d '{ "name": "is_valid_email", "code": "REGEX_MATCH(email, ...)" }'
```

