# Source: https://virustotal.readme.io/reference/monitor-items-config.md

# Configure a given VirusTotal Monitor item (file or folder)

Is possible to set some file information/metadata into a MonitorItem by setting its *details* attribute, this information will be shared with Monitor Partners and should be used to give more context to them about the file in case of false positive. Folders does not support *details*.

```python
import requests

item_id = '<item-id>'

url = "https://www.virustotal.com/api/v3/monitor/items/%s/config" % item_id
data = {'data': {
        'id': item_id,
        'type': 'monitoritem',
        'attributes': {
            'details': 'This is file metadata.'
       },
    }}

response = requests.request("PATCH", url, data=json.dumps(data))
print(response.text)
```

```json
{
 "data": {
  "attributes": {
   "size": 49676, 
   "sha1": "892392d4f28b2dbe8ae45115a38c079dbcb14e18", 
   "first_detection_date": 1504175079, 
   "sha256": "cb9f9c1b271daa19fc78138dfd9d37686b1edb35e381f205c0b59911d8a004e1", 
   "next_analysis_date": 1504781041, 
   "last_detections_count": 1, 
   "last_analysis_date": 1504694733, 
   "tags": [
    "detected", 
    "visible", 
    "[ENGINE-NAME]"
   ], 
   "creation_date": 1504174971, 
   "item_type": "file", 
   "creator_id": "fsantos", 
   "last_analysis_results": {
    "[ENGINE-NAME]": {
     "category": "undetected", 
     "engine_name": "[ENGINE-NAME]", 
     "engine_version": "1.3.0.9330", 
     "result": null, 
     "method": "blacklist", 
     "engine_update": "20170906"
    },...
   }, 
   "details": "This is the metadata.", 
   "path": "/test/tac.exe", 
   "md5": "02c526e8efd42a1f57a75aa203cfb27f"
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
    "/monitor/items/{id}/config": {
      "patch": {
        "summary": "Configure a given VirusTotal Monitor item (file or folder)",
        "description": "",
        "operationId": "monitor-items-config",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "MonitorItem obj",
                    "default": "{\"id\": \"[MONITOR-ID]\", \"type\": \"monitoritem\", \"attributes\": {\"details\": \"This is file metadata.\"}}",
                    "format": "json"
                  }
                }
              }
            }
          }
        },
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