# Source: https://docs.acceldata.io/api/determine-data-plane-feature-support.md

# Determine Data Plane Feature Support

The following APIs help determine whether the data plane supports templated persistence configuration.

## Get Data Plane Features

This endpoint checks whether a data plane supports templated persistence.

### Endpoint

```bash
GET /catalog-server/api/analytics-pipelines/{id}/featuresEnabled
```



If response:

```json
{
  "TEMPLATED_PERSISTENCE_SUFFIX": {
    "enabled": true
  }
}
```



then the data plane supports the templated persistence configuration model.

### Path Parameter

| Parameter | Description | 
| ---- | ---- | 
| id | Data plane (analytics pipeline) ID | 


### Determining the Relevant Data Plane

The data plane associated with the policy depends on the policy type:

- **Data Quality Policies** → data plane associated with the asset’s datasource
- **Equality Policies** → data plane selected during policy creation

### Control Plane Behavior Changes (v26.3.0)

Starting with **Control Plane v26.3.0**:

- `persistentPathConfig` is **no longer supported**
- Result handling must use **categoriesResultHandlingConfig**
- Category names are **case-sensitive and must be lowercase** (`good`, `bad`)

Note This change is enforced immediately after the control plane upgrade, regardless of data plane version.

### Action Required

After upgrading to **Control Plane v26.3.0**:

1. **Stop** using `persistentPathConfig`
2. Use `categoriesResultHandlingConfig`
3. Ensure category names are **lowercase** (`good`, `bad`)

Persistence configuration must follow data plane compatibility:

| Data Plane Version | Required Configuration | 
| ---- | ---- | 
| **&lt;** v26.3.0 | Use `persistenceFolderPrefix` | 
| **≥** v26.3.0 | Use `categoriesPersistenceConfig` | 


---

## Get Asset Features

This endpoint returns the features supported for an asset.

### Endpoint

```bash
GET /catalog-server/api/assets/{id}/featuresEnabled
```



### Path Parameter

| Parameter | Description | 
| ---- | ---- | 
| id | Asset ID | 


### Sample Request

```bash
curl -X GET "https://{HOST}/catalog-server/api/assets/789/featuresEnabled" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



### Response (200 OK)

```json
{
    "CADENCE_ENABLED": {
        "enabled": true,
        "metricsSupported": [
            "DATA_FRESHNESS",
            "DATA_VOLUME_TOTAL",
            "DATA_VOLUME_DRIFT",
            "RECORD_COUNT_TOTAL",
            "RECORD_COUNT_DRIFT"
        ]
    },
    "FRESHNESS_ENABLED": {
        "enabled": true,
        "metricsSupported": [
            "DATA_FRESHNESS",
            "DATA_VOLUME_TOTAL",
            "DATA_VOLUME_DRIFT",
            "RECORD_COUNT_TOTAL",
            "RECORD_COUNT_DRIFT"
        ]
    },
    "LIMITED_SOURCED_COLUMNS_FEATURE": {
        "enabled": true
    },
    "LIMITED_SOURCED_COLUMNS_PROFILING_FEATURE": {
        "enabled": true
    },
    "COMPLETE_SQL_SUPPORT_FOR_FILES": {
        "enabled": true
    },
    "JDBC_SQL_GOOD_BAD_DATA_FEATURE": {
        "enabled": true
    },
    "TEMPLATED_PERSISTENCE_SUFFIX": {
        "enabled": false
    }
}
```

