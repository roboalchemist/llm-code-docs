# Source: https://docs.acceldata.io/api/data-drift-policy---schema.md

# Data Drift Policy - Schema

This schema represents the **Data Drift policy** object returned by:

- [Create and List Data Drift Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-data-drift-policy)
- [Manage Data Drift Policy by ID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-data-drift-policy-by-id)
- [Manage Data Drift Policy by Name](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-data-drift-policy-by-name)

## Top-level Fields

Depending on the endpoint, responses either wrap policies in a list or return a single policy object. The policy itself has:

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `rule` | object | Core Data Drift policy metadata and configuration (asset, thresholds, schedule, notifications, tags). | 


**Key nested properties (high-level):**

- `rule.id` (integer) – Unique policy ID.
- `rule.name` (string) – Policy name (`<asset>-data-drift-policy` pattern is common).
- `rule.type` (string) – Always `DATA_DRIFT`.
- `rule.backingAsset.tableAssetId` (integer) – Asset the policy is attached to.
- `rule.interval` (string) – Drift evaluation interval (for example `10d`).
- `rule.thresholdLevel.success` / `warning` (integer) – Percent thresholds for drift.
- `rule.tags` (array) – Tags associated with the drift policy.

## Example JSON

```json
{
  "rule": {
    "archived": false,
    "autoCreated": false,
    "backingAsset": {
      "customQuery": null,
      "customTableAssetIds": null,
      "id": 13838,
      "marker": null,
      "ruleId": 14716,
      "tableAlias": null,
      "tableAssetId": 7456771,
      "tableAssetUid": null
    },
    "createdAt": "2024-06-18T12:32:30.415Z",
    "createdBy": "user@acceldata.io",
    "description": "Data drift policy for the BLACKROCK_QUARANTINE_RAW table",
    "enabled": true,
    "id": 14716,
    "interval": "10d",
    "lastUpdatedBy": "user@acceldata.io",
    "name": "BLACKROCK_QUARANTINE_RAW-data-drift-policy",
    "notificationChannels": {
      "alertsEnabled": true,
      "configuredNotificationGroupIds": [],
      "notifyOn": [],
      "notifyOnSuccess": false,
      "reNotifyFactor": 0,
      "severity": null,
      "tags": null
    },
    "policyGroups": [],
    "schedule": null,
    "scheduled": false,
    "sparkResourceConfig": null,
    "tags": [
      {
        "id": 3170,
        "name": "raw_table",
        "ruleId": 14716,
        "tagId": 40723,
        "tenantId": ""
      }
    ],
    "tenantId": "demo",
    "thresholdLevel": {
      "success": 100,
      "warning": 70
    },
    "timeZone": "GMT",
    "type": "DATA_DRIFT",
    "updatedAt": "2024-06-18T12:32:30.415Z",
    "version": 1
  }
}
```

