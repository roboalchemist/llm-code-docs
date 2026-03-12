# Source: https://docs.acceldata.io/api/manage-policies-by-id.md

# Manage Policies by ID

Use this endpoint when you already know the **policy ID** and want to:

- View the configuration of a specific Data Freshness policy
- Confirm its thresholds, assets, notification settings, and status
- Programmatically inspect or debug a particular policy

This is typically used after creating a policy (from the API or UI), or when syncing policy definitions into an external catalog or automation.

## Endpoint

```http
GET /catalog-server/api/rules/data-cadence/:id
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| id | string | Yes | Unique identifier of the Data Freshness policy to retrieve. | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/rules/data-cadence/14718" \
  -H "accessKey: <YOUR_ACCESS_KEY>" \
  -H "secretKey: <YOUR_SECRET_KEY>" \
  -H "Accept: application/json"
```



The response contains the `rule` and `details` objects for the Data Freshness policy, including fields such as `id`, `name`, `type: DATA_CADENCE`, `thresholdLevel`, `notificationChannels`, `backingAsset`, and timestamps.