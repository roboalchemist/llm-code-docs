# Source: https://docs.acceldata.io/api/asset-centric-reliability-view.md

# Asset-Centric Reliability View

This endpoint provides a **single, consolidated view of all policies** attached to an asset, along with the **latest execution** for each. 

## Endpoints

**By Asset ID**

```http
GET /catalog-server/api/assets/:id/rulesWithLatestExecution
```



**By Asset UID**

```http
GET /catalog-server/api/assets/byUid/:uid/rulesWithLatestExecution
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `id` | string | Yes | Asset ID | 
| `uid` | string | Yes | Asset UID | 


## Sample Request

```bash
curl -X GET "https://{{HOST}}/catalog-server/api/assets/1202692/rulesWithLatestExecution" \
  -H "accessKey: {{ACCESS_KEY}}" \
  -H "secretKey: {{SECRET_KEY}}"
```

