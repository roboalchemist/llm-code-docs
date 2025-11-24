# Source: https://docs.apify.com/api/v2/actor-run-put.md

# Update status message


```
PUT 
https://api.apify.com/v2/actor-runs/:runId
```


You can set a single status message on your run that will be displayed in the Apify Console UI. During an Actor run, you will typically do this in order to inform users of your Actor about the Actor's progress.

The request body must contain `runId` and `statusMessage` properties. The `isStatusMessageTerminal` property is optional and it indicates if the status message is the very last one. In the absence of a status message, the platform will try to substitute sensible defaults.

## Request

## Responses

* 200

**Response Headers**

