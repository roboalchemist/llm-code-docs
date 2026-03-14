# Source: https://docs.acceldata.io/api/data-anomaly-policy---schema.md

# Data Anomaly Policy - Schema

**Data Anomaly (profile anomaly) policy**

- [Create or Update Data Anomaly Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/api/create-data-anomaly-policy)
- [Get Data Anomaly Policy by ID](https://docs.acceldata.io/acceldata-data-observability-cloud/api/manage-data-anomaly-policy-by-id)
- [Get Data Anomaly Policy by Asset](https://docs.acceldata.io/acceldata-data-observability-cloud/api/get-data-anomaly-policy-by-asset-id)

Execution result endpoints for anomaly detection use separate result schemas.

## Top-level Fields

Depending on the endpoint, anomaly policy responses carry configuration in one or both of:

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `details` | object | Rule-level details including policy items (metrics to monitor, thresholds, etc.). | 
| `assetConfiguration` | object | Asset-level configuration for anomaly detection (profiling type, schedule, owner/team, pattern settings). | 
| `manualProfilingTriggers` | array | Reasons and flags controlling when manual profiling is required or blocked. | 


**Key nested properties (high-level):**

- `details.backingAssetId` (integer) – Asset the anomaly policy is configured for.
- `details.items[]` – Individual anomaly checks (per metric/column).
- `assetConfiguration.profilingType` (string) – Type of profiling (for example distribution, volume, etc.).
- `assetConfiguration.schedule` / `scheduled` (string / boolean) – When anomaly profiling runs.
- `assetConfiguration.notificationChannels` (string or object, depending on shape) – High-level alerting configuration.
- `manualProfilingTriggers[].canTrigger` (boolean) – Whether manual profiling is allowed.
- `manualProfilingTriggers[].reason` (string) – Human-readable reason.
- `manualProfilingTriggers[].type` (string) – Trigger type.

## Example JSON

```json
{
  "details": {
    "backingAssetId": 7456771,
    "continueExecutionOnFailure": false,
    "executionSequence": 1,
    "filter": null,
    "id": 23001,
    "isCompositeRule": false,
    "isSegmented": false,
    "items": [
      {
        "businessExplanation": "Detect anomalies in daily order volume.",
        "columnName": "order_date",
        "executionOrder": 1,
        "id": 34001,
        "ruleId": 23001,
        "ruleVersion": 1,
        "weightage": 100
      }
    ]
  },
  "assetConfiguration": {
    "profilingType": "VOLUME",
    "owner": "data-team@company.com",
    "team": "Data Platform",
    "schedule": "0 * * * *",
    "scheduled": true,
    "timeZone": "Asia/Kolkata",
    "patternConfiguration": {
      "frequencyType": "DAILY",
      "maxPatterns": 10
    },
    "notificationChannels": "DEFAULT",
    "minimumRequiredHistoricalMetricsForAnomalyDetection": "7d",
    "referenceCheckConfiguration": "LATEST",
    "sparkResourceConfig": "DEFAULT",
    "persistencePath": "s3://bucket/path/anomaly-metrics",
    "updatedAt": "2024-06-18T12:32:30.415Z"
  },
  "manualProfilingTriggers": [
    {
      "canTrigger": false,
      "reason": "Insufficient historical data for anomaly detection.",
      "type": "HISTORICAL_DATA_INSUFFICIENT"
    }
  ]
}
```

