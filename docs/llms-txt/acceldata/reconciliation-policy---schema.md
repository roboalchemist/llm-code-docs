# Source: https://docs.acceldata.io/api/reconciliation-policy---schema.md

# Reconciliation Policy - Schema

This schema represents the **Reconciliation policy** object returned by:

- [Create and List Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-and-list-reconciliation-policies)
- [Manage Reconciliation Policy by ID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-reconciliation-policy-by-id)
- [Manage Reconciliation Policy by Name](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-reconciliation-policy-by-name)

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `rule` | object | Core reconciliation policy definition including source/sink assets, match type, thresholds, and notifications. | 


**Key nested properties (high-level)**:

- `rule.id` (integer) – Unique policy ID.
- `rule.name` (string) – Policy name.
- `rule.type` (string) – Always `RECONCILIATION`.
- `rule.leftBackingAsset` / `rightBackingAsset` (object) – Source and sink assets to be compared.
- `rule.thresholdLevel.success` / `warning` (integer) – Pass/fail thresholds for reconciliation.
- `rule.labels` (array) – Labels associated with the policy.
- `rule.notificationChannels` (object) – Alert settings.

## Example JSON

```json
{
  "rule": {
    "archived": false,
    "autoCreated": false,
    "createdAt": "2024-05-13T09:41:43.063Z",
    "createdBy": "user@company.com",
    "description": "Hashed data equality between source and sink tables",
    "enabled": true,
    "executionTimeoutInMinutes": null,
    "id": 282143,
    "isProtectedResource": false,
    "labels": [],
    "lastUpdatedBy": "user@company.com",
    "leftBackingAsset": {
      "customQuery": null,
      "customTableAssetIds": null,
      "id": 349870,
      "marker": null,
      "ruleId": 282143,
      "tableAlias": null,
      "tableAssetId": 3845235,
      "tableAssetUid": null
    },
    "name": "SNOWFLAKE_automation_Hashed_Data_Equality_3_success",
    "notificationChannels": null,
    "policyGroups": [],
    "rightBackingAsset": {
      "customQuery": null,
      "customTableAssetIds": null,
      "id": 349871,
      "marker": null,
      "ruleId": 282143,
      "tableAlias": null,
      "tableAssetId": 3845233,
      "tableAssetUid": null
    },
    "schedule": null,
    "scheduled": false,
    "sparkResourceConfig": null,
    "tags": [],
    "tenantId": "twosevenzero",
    "thresholdLevel": {
      "success": 100,
      "warning": null
    },
    "timeSecondsOffset": 0,
    "timeZone": "GMT",
    "type": "RECONCILIATION",
    "updatedAt": "2024-05-13T09:41:43.063Z",
    "version": 1
  }
}
```

