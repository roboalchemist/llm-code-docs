# Source: https://virustotal.readme.io/reference/monitor-statistics.md

# Retrieve statistics about analyses performed on your software collection

This endpoint returns information about your stored files, including quota consumption, detected files, top signatures, offending engines and oldest detections pending remediation.

A dictionary with data and meta properties is received, each data attributes will reflect past days statistics and meta realtime will reflect current detection counts. Data attributes also contains information about last day consumed storage (for realtime quota consumption user data should be check /ui/signin).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fe68e9f-Selection_183.png",
        "Selection_183.png",
        840,
        308,
        "#dcd4da"
      ]
    }
  ]
}
[/block]

```json
{"data": [
 {
  "attributes": {
  "date": 1517270400,
  "items_detected_count": 28,
  "increasing_detections_count": 6,
  "owner_id": "monitor_group",
  "period": "day",
  "storage_bytes_count": 166709820,
  "storage_files_count": 34,
  "top_age_items": [
   {
   "age": 7621121,
   "detections_count": 46,
   "monitor_key": "[MONITOR-ID]",
   "total_engines_count": 71
   }...
  ],
  "top_detected_items": [
   {
   "detections_count": 47,
   "monitor_key": "[MONITOR-ID]",
   "total_engines_count": 71
   }...
  ],
  "top_engines": [
   {
   "count": 20,
   "engine": "[ENGINE-NAME]"
   }...
  ],
  "top_signatures": [
   {
   "count": 20,
   "signature": "Unsafe"
   }...
  ]
  },
  "id": "monitor_group-day-2018-01-30",
  "type": "monitor_statistics"
 }...
 ],
 "meta": {
 "realtime": {
  "decreasing_detections_count": 0,
  "increasing_detections_count": 6,
  "items_detected_count": 28,
  "new_detections_count": 0,
  "solved_detections_count": 0,
  "swapped_detections_count": 0
 }
 }
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
    "/monitor/statistics": {
      "get": {
        "summary": "Retrieve statistics about analyses performed on your software collection",
        "description": "",
        "operationId": "monitor-statistics",
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
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
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