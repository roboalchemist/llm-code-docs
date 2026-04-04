# Source: https://docs.acceldata.io/api/create-data-anomaly-policy.md

# Create Data Anomaly Policy

Use this endpoint to define a new **profile anomaly policy**. This policy will continuously evaluate profile metrics to detect abnormal changes.

## Endpoint

```http
POST /catalog-server/api/rules/profile-anomaly
```



## Path or Query Parameters

This endpoint has **no path or query parameters**.

## Sample Request

```bash
curl -X POST "https://{{HOST}}/catalog-server/api/rules/profile-anomaly" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}" \
  -H "Content-Type: application/json" \
  -d '{
    "rule": {
      "name": "orders_profile_anomaly",
      "description": "Detects anomalies for the Orders table profile",
      "type": "PROFILE_ANOMALY",
      "enabled": true,
      "tags": []
    },
    "details": {
      "backingAsset": { "profileId": 9623966 }
    }
  }'
```

