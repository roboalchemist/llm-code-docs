# Source: https://virustotal.readme.io/reference/monitor-items-analyses.md

# Get the latest file analyses

Retrieve item analyses, use cursor and limit to retrieve older ones.

```json
{
  "data": [
    {
      "id": "d917dd47406322341cef40cf38091292962ba81d42983456aae4dc4f7967afb1-1517474700",
      "type": "monitor_analysis",
      "attributes": {
        "analysis_results": {
          "{engine name}": {
            "category": "undetected",
            "engine_name": "{engine name}",
            "engine_update": "20180201",
            "engine_version": "1.1.1.3",
            "method": "blacklist",
            "result": null
          }
        },
        "date": 1517474787,
        "detections_count": 1,
        "sha256": "d917dd47406322341cef40cf38091292962ba81d42983456aae4dc4f7967afb1",
        "tags": [
          "detected",
          "{engine name}"
        ]
      }
    }
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
    "/monitor/items/{id}/analyses": {
      "get": {
        "summary": "Get the latest file analyses",
        "description": "",
        "operationId": "monitor-items-analyses",
        "parameters": [
          {
            "name": "cursor",
            "in": "query",
            "description": "Continue listing after this offset",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of analyses to retrieve",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "description": "Monitor item identifier",
            "schema": {
              "type": "string"
            },
            "required": true
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