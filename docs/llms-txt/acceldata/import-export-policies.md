# Source: https://docs.acceldata.io/api/import-export-policies.md

# Import & Export Policy Definitions

Policy definitions represent the full configuration of Data Reliability policies—including Data Quality, Reconciliation, Drift, Freshness, and Anomaly rules—along with metadata such as tags, versions, schedules, and thresholds.

The Policy Definition Import/Export APIs allow users to:

- Backup or archive reliability policies
- Share standard policy definitions across teams
- Validate export/import compatibility before applying changes
- Bulk-import policies into a new tenant

These APIs mimic the Reliability Policy Import/Export features available in the ADOC UI and support safe, controlled migration workflows.

## Available Endpoints

| Action | Endpoint | 
| ---- | ---- | 
| Pre-check Export Compatibility | `GET /catalog-server/api/rules/export/policy-definitions/pre-check` | 
| Export Policy Definitions | `GET /catalog-server/api/rules/export/policy-definitions` | 
| Upload Exported Policy Definition ZIP | `POST /catalog-server/api/rules/import/policy-definitions/upload-config` | 
| Apply Policy Definition Configuration | `POST /catalog-server/api/rules/import/policy-definitions/apply-config` | 
