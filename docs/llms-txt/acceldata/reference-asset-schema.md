# Source: https://docs.acceldata.io/api/reference-asset-schema.md

# Reference Asset Schema

Returned by [Reference Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/api/reference-assets).

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| jobId | string | Validation job ID | 
| status | string | Job status | 
| assets | array | Reference assets list | 


## Example JSON

```json
{ 
  "jobId": "job-123", 
  "status": "SUCCESSFUL", 
  "assets": 
  	[
      { "id": 12616 
      }
    ] 
}
```

