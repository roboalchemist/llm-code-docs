# Source: https://docs.aimlapi.com/api-references/service-endpoints/account-balance.md

# Account Balance

## Get account balance info

You can query your account balance and other billing details through this API.\
To make a request, you only need your AIMLAPI key obtained from your [account dashboard](https://aimlapi.com/app/keys).<br>

## GET /v1/billing/balance

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/billing/balance":{"get":{"operationId":"_v1_billing_balance","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"–","title":"–"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"balance":{"type":"number","description":"The total credits associated with the provided API key."},"lowBalance":{"type":"boolean","description":"True if the balance is below the threshold."},"lowBalanceThreshold":{"type":"number","description":"Threshold for switching to low balance status."},"lastUpdated":{"type":"string","format":"date-time","description":"The date of the request — i.e., the current date."},"autoDebitStatus":{"type":"string","description":"Indicates whether auto top-up is enabled for the plan."},"status":{"type":"string","description":"The status of the plan associated with the provided API key."},"statusExplanation":{"type":"string","description":"A more detailed explanation of the plan status."}},"required":["balance","lowBalance","lowBalanceThreshold","lastUpdated","autoDebitStatus","status","statusExplanation"]}}}}}}}}}
```
