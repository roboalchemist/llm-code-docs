# Source: https://docs.acceldata.io/api/sample-data-schema.md

# Sample Data Schema

Returned by [Preview Sample Data](https://docs.acceldata.io/acceldata-data-observability-cloud/api/preview-sample-data).

## Top-level Fields

| Field | Type | Description | 
| ---- | ---- | ---- | 
| status | string | Job status | SUCCESSFUL | 
| requestId | string | Sample job ID | req-123 | 
| result | object | Preview schema & rows | 


## Nested: result

| Field | Type | Description | 
| ---- | ---- | ---- | 
| schema.fields[] | array | Column definitions | 
| data[] | array | Sample rows | 


## Example JSON

```json
{ 
  "status": "SUCCESSFUL", 
  "requestId": "req-123", 
  "result": 
  	{ "data": 
     	[
        { "id": 1 
        }
      ] 
    } 
}
```

