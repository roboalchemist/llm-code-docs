# Source: https://docs.acceldata.io/api/create-and-list-policies.md

# Create and List Policies

Use the following APIs to create a new data quality policy or list the existing policies.

## Endpoint (s)

```none
GET  /catalog-server/api/rules/data-quality     (list)
POST /catalog-server/api/rules/data-quality     (create)
```



## Query Parameters

| Name | Type | Required | Description | 
| ---- | ---- | ---- | ---- | 
| page | integer | No | Page number to retrieve when listing policies (default: 0). | 
| size | integer | No | Page size for pagination (default: 25). | 
| onlyActive | boolean | No | If `true`, returns only active Data Quality policies. | 


Note 

- `POST` to this path is used to **create** a new Data Quality policy (no path or query parameters, body required).
- `GET` to this path is used to **list** Data Quality policies (with optional pagination params above).

## Sample Request

### List

```bash
curl -X GET "https://{HOST}/catalog-server/api/rules/data-quality?page=0&size=25"
```



### Create

```bash
curl -X POST "https://{HOST}/catalog-server/api/rules/data-quality" \
  -H "Authorization: Bearer $TOKEN" \
  -H "accessKey: $ACCESS_KEY" 
  -H "secretKey: $SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "rule":{
          "name":"CUSTOMER_DQ",
          "type":"DATA_QUALITY",
          "details":{"backingAssetId":12345},
          "thresholdLevel":"type": "ABSOLUTE",
      			"config": {
        		"direction": "ABOVE",
        		"success": 100,
        		"warning": 70
      		},
          "scheduled":false
        },
        "items":[
          {
          	"measurementType":"NULL_VALUES",
            "columnName":"email",
            "executionOrder":1
           },
           {"measurementType":"REGEX_MATCH",
            "columnName":"phone",
            "pattern":"^\\d{10}$",
            "executionOrder":2}
        ]
      }'
```

