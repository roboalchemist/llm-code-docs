# Source: https://virustotal.readme.io/reference/monitorpartner-hashes-analyses.md

# Get a list of analyses for a file

This endpoint allows you to retrieve all analyses performed on a certain sha256 hash using cursored listings.

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor_partner/hashes/<sha256>/analyses"
response = session.get(url)
print(response.text)
```

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
    "/monitor_partner/hashes/{sha256}/analyses": {
      "get": {
        "summary": "Get a list of analyses for a file",
        "description": "",
        "operationId": "monitorpartner-hashes-analyses",
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
            "description": "Maximum number of items to retrieve (max: 40)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "sha256",
            "in": "path",
            "description": "File's SHA256",
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