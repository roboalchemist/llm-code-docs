# Source: https://docs.acceldata.io/api/notification-settings.md

# Notification Settings

Notification settings determine **when alerts are triggered** and which teams receive them. These fields appear inside the `notificationChannels` object on every policy. 

Although there is **no dedicated notifications endpoint**, these fields are part of:

- Data Quality Policies
- Reconciliation Policies
- Drift Policies
- Freshness Policies
- Anomaly Policies

## Important Fields (shared across policy schemas)

| Field | Type | Description | 
| ---- | ---- | ---- | 
| `alertsEnabled` | boolean | Whether alerts are active | 
| `configuredNotificationGroupIds` | array | Notification groups to notify | 
| `severity` | string | CRITICAL / HIGH / MEDIUM / LOW | 
| `notifyOn` | array | Events that trigger alerts (FAILURE, WARNING, etc.) | 
| `notifyOnSuccess` | boolean | Whether to send alerts on success | 
| `reNotifyFactor` | integer | Escalation/resend multiplier | 


## Example Snippet

```json
{
  "notificationChannels": {
    "alertsEnabled": true,
    "configuredNotificationGroupIds": [4522],
    "notifyOn": ["FAILURE"],
    "notifyOnSuccess": false,
    "reNotifyFactor": 0,
    "severity": "HIGH"
  }
}
```

