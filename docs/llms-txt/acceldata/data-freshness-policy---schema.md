# Source: https://docs.acceldata.io/api/data-freshness-policy---schema.md

# Data Freshness Policy - Schema

This schema represents the **Data Freshness policy** object returned by:

- [Create and List Data Freshness Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/api/data-freshness)
- [Manage Data Freshness Policies by ID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-policies-by-id)
- [Get Data Freshness Policies by Asset ID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/get-policies-by-asset)

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `details` | object | Data Freshness–specific configuration for the asset and checks (backing asset, items, thresholds, etc.). | 
| `rule` | object | Core policy metadata (name, type, schedule, notification, thresholds, tags). | 


**Key nested properties (high-level):**

- `rule.id` (integer) – Policy ID.
- `rule.name` (string) – Policy name, typically tied to asset & freshness SLA.
- `rule.type` (string) – `DATA_FRESHNESS` (or equivalent in the spec).
- `rule.thresholdLevel.success` / `warning` (integer) – SLA thresholds for freshness.
- `details.backingAssetId` (integer) – Asset ID.
- `details.items[]` – Freshness checks (record count, file count, volume, etc.), with configured thresholds.

## Example JSON

```json
{
  "details": {
    "backingAssetId": 7456771,
    "continueExecutionOnFailure": false,
    "executionSequence": 1,
    "filter": null,
    "id": 22001,
    "isCompositeRule": false,
    "isSegmented": false,
    "items": [
      {
        "businessExplanation": "New data should arrive at least once every hour.",
        "columnName": null,
        "executionOrder": 1,
        "id": 33001,
        "measurementType": "DATA_FRESHNESS",
        "metric": "MAX_INGESTED_AT",
        "ruleId": 22001,
        "ruleVersion": 1,
        "thresholdLevelFieldMapping": {
          "success": 60,
          "warning": 90
        },
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
      "ruleId": 22001,
      "tableAlias": null,
      "tableAssetId": 7456771,
      "tableAssetUid": null
    },
    "createdAt": "2024-06-18T12:32:30.415Z",
    "createdBy": "user@company.com",
    "description": "Data freshness policy for the ORDERS stream",
    "enabled": true,
    "id": 22001,
    "interval": "1h",
    "lastUpdatedBy": "user@company.com",
    "name": "ORDERS-data-freshness-policy",
    "notificationChannels": {
      "alertsEnabled": true,
      "configuredNotificationGroupIds": [],
      "notifyOn": ["FAILURE"],
      "notifyOnSuccess": false,
      "reNotifyFactor": 0,
      "severity": "HIGH"
    },
    "policyGroups": [],
    "schedule": null,
    "scheduled": false,
    "sparkResourceConfig": null,
    "tags": [],
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
    "type": "DATA_FRESHNESS",
    "updatedAt": "2024-06-18T12:32:30.415Z",
    "version": 1
  }
}
```

