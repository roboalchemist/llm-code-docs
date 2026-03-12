# Source: https://docs.acceldata.io/api/configure-policy-level-persistence.md

# Configure Policy-Level Persistence

The following APIs allow configuring how policy execution results are stored for a specific policy.

## Get Policy Persistence Configuration

Retrieves the persistence configuration associated with a policy.

### Endpoints

```bash
GET /catalog-server/api/rules/{policyId}/configuration           (By Policy ID)

GET /catalog-server/api/rules/byName/{policyName}/configuration  (By Policy Name)
```



### Path Parameters

| Parameter | Description | 
| ---- | ---- | 
| policyId | Unique identifier of the policy | 
| policyName | Name of the policy | 


### Sample Request

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/8/configuration" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



### Sample Response

```bash
{
  "id": 5,
  "ruleId": 8,
  "categoriesPersistenceConfig": {
    "type": "CUSTOM",
    "categoriesConfig": {
      "good": {
        "suffixTemplate": "{{POLICY_TYPE}}-{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
        "format": "CSV"
      },
      "bad": {
        "suffixTemplate": "{{POLICY_TYPE}}-{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}",
        "format": "CSV"
      },
      "metadata": {
        "suffixTemplate": "{{POLICY_TYPE}}-{{POLICY_NAME}}/{{TIME:yyyy-MM-dd}}/{{REQUEST_ID}}/{{RECORD_TYPE}}"
      }
    }
  },
  "categoriesResultHandlingConfig": {
    "good": {
      "storeResult": false,
      "sampleOnly": false
    },
    "bad": {
      "storeResult": true,
      "sampleOnly": true
    }
  }
}
```



---

## Update Policy Persistence Configuration

This endpoint updates the persistence configuration for a policy.

Note The **request body structure depends on the version and capabilities of the data plane associated with the policy**.

Starting with **Control Plane v26.3.0**, persistence configuration behavior changed. The control plane enforces new request structures and removes support for legacy configuration fields.

Users can determine whether a data plane supports templated persistence by either:

- Checking the data plane version or
- Calling the **Data plane Feature Support API**

### Endpoints

```bash
PUT /catalog-server/api/rules/{policyId}/configuration           (By Policy ID)

PUT /catalog-server/api/rules/byName/{policyName}/configuration  (By Policy Name)
```



### Data Plane v26.3.0 and Later

Data planes running **v26.3.0 or later require the templated persistence configuration model**.

**Requirements**

- `categoriesPersistenceConfig` **must be provided**
- `persistenceFolderPrefix` **is not supported**
- `persistentPathConfig` **is not supported**

**Request Body Parameters**

| **Field** | **Type** | **Description** | 
| ---- | ---- | ---- | 
| `categoriesPersistenceConfig.type` | string | Configuration type (DEFAULT, SAVED, CUSTOM) | 
| `categoriesPersistenceConfig.configId` | number | ID of saved configuration when type = SAVED | 
| `categoriesPersistenceConfig.categoriesConfig` | object | Template configuration when type = CUSTOM | 
| `categoriesResultHandlingConfig.good.storeResult` | boolean | Whether to persist passing records | 
| `categoriesResultHandlingConfig.good.sampleOnly` | boolean | Store only sample records | 
| `categoriesResultHandlingConfig.bad.storeResult` | boolean | Whether to persist failing records | 
| `categoriesResultHandlingConfig.bad.sampleOnly` | boolean | Store only sample records | 


Note For **Pushdown policies**, the metadata template is not required.

### Data Plane Versions Earlier Than v26.3.0 (Backward Compatibility)

Data planes running versions **earlier than v26.3.0 do not support templated persistence paths**.

**Requirements**

- `persistenceFolderPrefi`x **must be used**
- `categoriesPersistenceConfig` **is not supported**
- `persistentPathConfig` **is not supported**

### Request Body

```bash
curl -X PUT "https://{HOST}/catalog-server/api/rules/8/configuration" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "categoriesResultHandlingConfig": {
      "good": { "storeResult": false, "sampleOnly": false },
      "bad": { "storeResult": true, "sampleOnly": true }
    },
    "persistenceFolderPrefix": "policy_prefix"
  }'
```



---

## Optional: Check Data Plane Support for Templated Persistence via API

If you need to determine whether a data plane supports templated persistence programmatically, call the **Get data plane features API**: `GET /analytics-pipelines/{id}/featuresEnabled`

For more information, see [Determine Data Plane Feature Support](https://docs.acceldata.io/acceldata-data-observability-cloud/api/determine-data-plane-feature-support).