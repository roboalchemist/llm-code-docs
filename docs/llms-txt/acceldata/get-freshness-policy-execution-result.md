# Source: https://docs.acceldata.io/api/get-freshness-policy-execution-result.md

# Get Policy Execution Result

Use this endpoint when you want to retrieve the **result of a specific Data Freshness policy execution**, identified by `executionId`.

Typical use cases:

- Investigate why a freshness check failed (late data, low volume, missing files)
- Build external dashboards showing recent freshness runs and outcomes
- Automate notifications or workflows based on policy execution status and metrics

## Endpoint

```http
GET /catalog-server/api/rules/data-cadence/executions/:executionId/result
```



## Path Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| `executionId` | string | Yes | Unique identifier of the Data Freshness policy execution whose result you want to retrieve. | 


## Sample Request

```bash
curl -X GET "https://demo.acceldata.io/catalog-server/api/rules/data-cadence/executions/abcd1234-result-id/result" \
  -H "accessKey: <YOUR_ACCESS_KEY>" \
  -H "secretKey: <YOUR_SECRET_KEY>" \
  -H "Accept: application/json"
```



The response returns the **execution history, details, and summary** of that Data Freshness policy run, based on schema `Payloadc61ec3e1147b`.