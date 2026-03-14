# Source: https://docs.acceldata.io/api/schema-drift-policy---schema.md

# Schema Drift Policy - Schema

This schema represents the **Schema Drift policy** object returned by:

- [Create and List Schema Drift Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-schema-drift-policy)
- [Manage Schema Drift Policy by ID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-schema-drift-by-id)
- [Manage Schema Drift Policy by Name](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-schema-drift-policy-by-name)

Execution and result endpoints use separate schemas.

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `rule` | object | Core Schema Drift policy metadata and configuration (asset, thresholds, notification settings). | 
| `segments` | array or null | Segment information used internally for drift analysis; often `null` in responses. | 


**Key nested properties (high-level):**

- `rule.id` (integer) – Unique policy ID.
- `rule.name` (string) – Policy name (often `<asset>-schema-drift-policy-<id>-auto-created`).
- `rule.type` (string) – Always `SCHEMA_DRIFT`.
- `rule.backingAsset.tableAssetId` (integer) – Asset monitored for schema changes.
- `rule.thresholdLevel.success` / `warning` (integer/null) – Thresholds for schema drift alerts.
- `rule.tags` (array) – Tags associated with policy.

## Example JSON

```json
{
  "segments": null,
  "rule": {
    "archivalReason": null,
    "archived": false,
    "assemblyId": null,
    "autoCreated": false,
    "backingAsset": {
      "customQuery": null,
      "customTableAssetIds": null,
      "id": 13838,
      "marker": null,
      "ruleId": 13552,
      "tableAlias": null,
      "tableAssetId": 7456771,
      "tableAssetUid": null
    },
    "createdAt": "2024-05-04T23:50:27.016Z",
    "createdBy": "system/torch-catalog-server",
    "description": "Auto created schema drift policy from data source settings",
    "enabled": true,
    "id": 13552,
    "lastUpdatedBy": "system/torch-catalog-server",
    "name": "PATIENTRECORDS-SNOWFLAKE-schema-drift-policy-7456771-auto-created",
    "notificationChannels": null,
    "policyGroups": [],
    "sparkResourceConfig": null,
    "tags": [],
    "tenantId": "demo",
    "thresholdLevel": {
      "success": 100,
      "warning": null
    },
    "type": "SCHEMA_DRIFT",
    "updatedAt": "2024-05-04T23:50:27.016Z",
    "version": 1
  }
}
```

