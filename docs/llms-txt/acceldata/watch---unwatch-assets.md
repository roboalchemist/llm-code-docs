# Source: https://docs.acceldata.io/api/watch---unwatch-assets.md

# Watch / Unwatch Assets

Use this API to follow assets you care about most. Watching an asset ensures you are notified of changes or issues. For example, a product manager might watch the “active_users” table to be alerted whenever its schema changes, ensuring downstream dashboards are not broken.

> ⚠️ All endpoints require authentication. See [Authentication & Headers](https://docs.acceldata.io/acceldata-data-observability-cloud/api/authentication).

## Endpoint(s)

- `POST /catalog-server/api/assets/:id/watch`  - **Start Watching**
- `DELETE /catalog-server/api/assets/:id/watch`  - **Stop Watching**
- `POST /catalog-server/api/assets/byUid/:uid/watch` - **Watch by UID**
- `DELETE /catalog-server/api/assets/byUid/:uid/watch` - **Unwatch by UID**

## Path Parameters

| Parameter | Type | Required | Description | Example | 
| ---- | ---- | ---- | ---- | ---- | 
| id | integer | Yes | Asset ID | `12616` | 
| uid | string | Yes | Unique asset UID | `sales.table` | 


## Sample Request

```bash
curl -X POST "https://demo.acceldata.io/catalog-server/api/assets/12616/watch"
```



## Response Schema

See [Watched Asset Schema](https://docs.acceldata.io/acceldata-data-observability-cloud/api/watch-asset-schema).