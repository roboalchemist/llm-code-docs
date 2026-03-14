# Source: https://docs.acceldata.io/api/policy-tags.md

# Policy Tags

Policy tags help you organize and group Data Reliability policies (Data Quality, Drift, Freshness, Reconciliation, Anomaly, etc.) for easier discovery and management. Tags are commonly used for:

- Team-based grouping (ex: “Finance”, “Marketing”)
- Domain grouping (“Customer360”, “Operational Data Store”)
- Sensitivity classification (“PII”, “Critical Asset”)
- Filter & search across hundreds of policies

These APIs allow you to list, add, and remove tags applied to policies.

## Available Endpoints

| Action | Endpoint | Description | 
| ---- | ---- | ---- | 
| List Tags | `GET /catalog-server/api/rules/tags` | List all existing policy tags | 
| Add Tags | `POST /catalog-server/api/rules/:id/tags` | Add one or more tags to a policy | 
| Remove Tags | `DELETE /catalog-server/api/rules/:id/tags/:tagId` | Remove a specific tag from a policy | 
