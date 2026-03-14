# Source: https://docs.acceldata.io/api/watch-asset-schema.md

# Watch Asset Schema

Returned by [Watch / Unwatch Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/api/watch---unwatch-assets).

## Top-level Fields

| Field | Type | Description | Example | 
| ---- | ---- | ---- | ---- | 
| id | integer | Watch record ID | 501 | 
| assetId | integer | Watched asset ID | 12616 | 
| userId | string | User who set watch | user1 | 
| createdAt | string | Creation time | 2025-09-01T12:00:00Z | 


## Example JSON

```json
{ 
  "id": 501, 
  "assetId": 12616, 
  "userId": "user1" 
}
```

