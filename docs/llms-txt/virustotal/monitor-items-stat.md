# Source: https://virustotal.readme.io/reference/monitor-items-stat.md

# Get attributes and metadata for a specific MonitorItem

```json
{
 "data": {
  "attributes": {
   "size": 8538624, 
   "sha1": "a9e2e47fd90b3552a072af482289532e878472fa", 
   "first_detection_date": 1502393426, 
   "next_analysis_date": 1504559882, 
   "last_analysis_date": 1504473518, 
   "tags": [
    "detected", 
    "new-detections", 
    "[ENGINE-NAME]"
   ], 
   "creation_date": 1501700980, 
   "item_type": "file", 
   "creator_id": "fsantos", 
   "last_analysis_results": {
    "[ENGINE-NAME]": {
     "category": "undetected", 
     "engine_name": "[ENGINE-NAME]", 
     "engine_version": "9.950.0.1006", 
     "result": null, 
     "method": "blacklist", 
     "engine_update": "20170903"
    }, 
    "[ENGINE-NAME]": {
     "category": "undetected", 
     "engine_name": "[ENGINE-NAME]", 
     "engine_version": "25.0.0.1", 
     "result": null, 
     "method": "blacklist", 
     "engine_update": "20170901"
    }
   }, 
   "path": "/go/bin/go.exe", 
   "sha256": "4db14737445edd2078a383520fabfd212f0979a31d0165dceac9f741fb1ab985", 
   "last_detections_count": 1, 
   "first_detection_date": 1504300116, 
   "md5": "3f389f88d18ba26e946a05883ea04130"
  }, 
  "type": "monitoritem", 
  "id": "[MONITOR-ID]"
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
    "/monitor/items/{id}": {
      "get": {
        "summary": "Get attributes and metadata for a specific MonitorItem",
        "description": "",
        "operationId": "monitor-items-stat",
        "parameters": [
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