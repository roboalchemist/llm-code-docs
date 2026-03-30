# Source: https://docs.acceldata.io/api/data-policy-templates.md

# Data Policy Templates

Data Policy Templates allow teams to define **reusable rule configurations** that can be applied when creating Data Quality or other reliability policies. A template may contain:

- A set of predefined rule items
- Conditions or expressions
- Standard thresholds
- Business logic reusable across multiple policies

This functionality is often used when teams want **standardized rule logic** across many policies (e.g., shared DQ checks for all PII tables).

## Available Endpoints

| Action | Endpoint | 
| ---- | ---- | 
| Create Template | `POST /catalog-server/api/rules/business-rules` | 
| List Template | `GET /catalog-server/api/rules/business-rules` | 
| Get Template by ID | `GET /catalog-server/api/rules/business-rules/:businessRuleId` | 
| Update Template | `DELETE /catalog-server/api/rules/business-rules/:businessRuleId` | 
| Delete Template | `DELETE /catalog-server/api/policy-templates/:id` | 
| Get Template Items | `GET /catalog-server/api/rules/business-rules/:businessRuleId/items` | 


## Path Parameter (GET Template)

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | string | Yes | Template ID | 


## Sample Requests

### Create Policy Template

```bash
curl -X POST "https://{{HOST}}/catalog-server/api/policy-templates" \
  -H "Content-Type: application/json" \
  -d '{ "name": "basic_null_checks", "items": [...] }'
```



### List Policy Template

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/policy-templates"
```



### Get Templates

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/policy-templates/42"
```



### Update Policy Template

```bash
curl -X PUT "https://{{HOST}}/catalog-server/api/policy-templates/42" \
  -H "Content-Type: application/json" \
  -d '{ "description": "Updated explanation" }'
```



### Delete Policy Template

```bash
curl -X DELETE "https://{{HOST}}/catalog-server/api/policy-templates/42"
```

