# Source: https://virustotal.readme.io/reference/monitor-items-filter.md

# Get a list of MonitorItem objects by path or tag

Items can be listed according to the parameters contained in **filter**:

* path: folder (String: /myfolder/)
* item: (MonitorItem ID describing a folder)
* tag: (One or more space separated tags from the following list)
  * detected: files flagged by at least one antivirus engine.
  * new-detections: files that have been flagged by at least one antivirus engine and were previously undetected.
  * decreasing-detections: files flagged by at least one antivirus engine that have less detections with respect to their previous analysis.
  * increasing-detections: files flagged by at least one antivirus engine that have more detections with respect to their pervious analysis.
  * solved-detections: files that are no longer detected by any antivirus engine and were previously detected.
  * swapped-detections: files that are detected by the same number of antivirus engines as their previous analysis but either the set of engines detecting the file or their detection labels have changed.
  * \[engine\_name]: files detected by the given antivirus engine.

Here you can see some examples for the most common operations:

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor/items"
querystring = {"filter": "tag:detected"}

response = session.get(url, params=querystring)
print(response.text)
```

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor/items"
querystring = {"filter": "tag:<av-name>"}

response = session.get(url, params=querystring)
print(response.text)
```

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor/items"
querystring = {"filter": "path:/"}

response = session.get(url, params=querystring)
print(response.text)
```

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor/items"
querystring = {"filter": "tag:new-detections"}

response = session.get(url, params=querystring)
print(response.text)
```

```json
{
  "data": [
    {
      "type": "monitor_item", 
      "id": "{id}", 
      "attributes": {
        "size": 2981888, 
        "sha1": "521a85a43fc8ccbe3409e39bd8ef7719c6d747d5", 
        "first_detection_date": 1510080120, 
        "tags": [
          "detected", 
          "{engine name 1}", 
          "{engine name 2}"
        ], 
        "last_analysis_date": 1517234132, 
        "creation_date": 1510079766, 
        "item_type": "file", 
        "creator_id": "fsantos", 
        "last_analysis_results": {
          "{engine name 1}": {
            "category": "undetected", 
            "engine_name": "[{engine name 1}", 
            "engine_version": "1.3.0.9466", 
            "result": null, 
            "method": "blacklist", 
            "engine_update": "20180129"
          },
          "{engine name 2}": { 
            ... 
          }
        }, 
        "details": "This is a windows go executable file", 
        "path": "/go1.7.4_pkg_tool_windows_386/addr2line.exe", 
        "sha256": "e9a08208ade9afb630f3bad01461b552086fc675e547214c73ac966aa7806847", 
        "last_detections_count": 2, 
        "md5": "a17b39a3a280c48a6b8b4b0b7982606c"
      },
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
    "/monitor/items": {
      "get": {
        "summary": "Get a list of MonitorItem objects by path or tag",
        "description": "",
        "operationId": "monitor-items-filter",
        "parameters": [
          {
            "name": "filter",
            "in": "query",
            "description": "Return the items matching the given criteria only",
            "schema": {
              "type": "string"
            }
          },
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
            "description": "Maximum number of items to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32"
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