# Source: https://virustotal.readme.io/reference/monitorpartner-statistics.md

# Get a list of MonitorHashes detected by an engine

Statistics provide information about hashes detected and total hashes analyzed by your engine. In case you have more than one engine you can use `filter=engine:<engine-name>`

```json Example response
{
  "data": [
    {
      "attributes": {
        "date": 1517356800,
        "engine": "[ENGINE-NAME]",
        "hashes_count": 1840,
        "hashes_detected_count": 34,
        "items_count": 1840,
        "items_detected_count": 34,
        "period": "day"
      },
      "id": "[ENGINE-NAME]-day-2018-01-31",
      "links": {
        "self": "https://www.virustotal.com/api/v3/monitor_partner/statistics/[ENGINE-NAME]-day-2018-01-31"
      },
      "type": "monitor_partner_statistics"
    }...
  ]
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/monitor_partner/statistics": {
      "get": {
        "summary": "Get a list of MonitorHashes detected by an engine",
        "description": "",
        "operationId": "monitorpartner-statistics",
        "parameters": [
          {
            "name": "cursor",
            "in": "query",
            "description": "List after this date",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of statistic periods to return",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Filter parameters",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```