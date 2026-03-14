# Source: https://docs.acceldata.io/api/data-quality-policy---schema.md

# Data Quality Policy - Schema

This schema represents the **Data Quality policy** object returned by:

- [Create and List Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-and-list-policies)
- [Manage Policies by ID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-data-quality-by-id)
- [Manage Policies by Name](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-data-quality-by-name)

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `rule` | object | Core policy metadata and configuration (name, type, schedule, notification settings, thresholds, tags, backing asset). | 
| `details` | object | Data Quality–specific configuration for the backing asset and rule items (per-column checks, business explanations, weightages, etc.). | 
| `childRules` | array | Optional list of nested rules for composite policies. Often empty for simple policies. | 


**Key nested properties (high-level only):**

- `rule.id` (integer) – Unique policy ID.
- `rule.name` (string) – Policy name.
- `rule.type` (string) – Always `DATA_QUALITY` for DQ policies.
- `rule.enabled` (boolean) – Whether the policy is currently active.
- `rule.interval` (string) – Policy interval (for example `1d`).
- `rule.thresholdLevel.success` / `warning` (integer) – Overall success/warning threshold in percent.
- `rule.backingAsset.tableAssetId` (integer) – ID of the asset the policy is attached to.
- `details.backingAssetId` (integer) – Backing asset ID (mirrors `rule.backingAsset.tableAssetId`).
- `details.items[]` (array of objects) – Individual Data Quality checks within the policy (per column or table-level).

## Example JSON

```json
{
  "childRules": [],
  "details": {
    "backingAssetId": 7456771,
    "continueExecutionOnFailure": false,
    "executionSequence": 1,
    "filter": null,
    "id": 21001,
    "isCompositeRule": false,
    "isSegmented": false,
    "items": [
      {
        "businessExplanation": "Orders table should not be empty.",
        "columnName": null,
        "createdAt": "2024-06-18T12:32:30.415Z",
        "createdBy": "user@company.com",
        "executionOrder": 1,
        "id": 31001,
        "isLookup": false,
        "ruleId": 21001,
        "ruleVersion": 1,
        "weightage": 100
      }
    ]
  },
  "rule": {
    "archived": false,
    "autoCreated": false,
    "backingAsset": {
      "customQuery": null,
      "customTableAssetIds": null,
      "id": 13838,
      "marker": null,
      "ruleId": 21001,
      "tableAlias": null,
      "tableAssetId": 7456771,
      "tableAssetUid": null
    },
    "createdAt": "2024-06-18T12:32:30.415Z",
    "createdBy": "user@company.com",
    "description": "Data quality checks for the ORDERS table",
    "enabled": true,
    "id": 21001,
    "interval": "1d",
    "lastUpdatedBy": "user@company.com",
    "name": "ORDERS-data-quality-policy",
    "notificationChannels": {
      "alertsEnabled": true,
      "configuredNotificationGroupIds": [123],
      "notifyOn": ["FAILURE"],
      "notifyOnSuccess": false,
      "reNotifyFactor": 0,
      "severity": "HIGH"
    },
    "policyGroups": [],
    "schedule": null,
    "scheduled": false,
    "sparkResourceConfig": null,
    "tags": [
      {
        "id": 3170,
        "name": "critical",
        "ruleId": 21001,
        "tagId": 40723,
        "tenantId": "demo"
      }
    ],
    "tenantId": "demo",
    "thresholdLevel": {
      "type": "ABSOLUTE",
      "config": {
        "direction": "ABOVE",
        "success": 100,
        "warning": 70
      }
    },
    "timeZone": "GMT",
    "type": "DATA_QUALITY",
    "updatedAt": "2024-06-18T12:32:30.415Z",
    "version": 1
  }
}
```

