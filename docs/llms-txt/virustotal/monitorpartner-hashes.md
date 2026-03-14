# Source: https://virustotal.readme.io/reference/monitorpartner-hashes.md

# Get a list of MonitorHashes detected by an engine

In some cases your user may have access to analyses of more than one engine, in this case you can provide a filter query with one engine name. To retrieve your preconfigured engine names you need to access the preferences/monitor\_partner/engines property calling /groups/{group_id}, in case you do not know your monitor\_partner group\_id, it can be obtained from privileges/monitor-partner/inherited\_from property calling /users/{your_user_id}.

To display the latest hash analyses for a specific engine use the filter parameter with the modifier:

* engine: (String: <engine-name>)

To display ignored hashes (detection confirmed ones [/hashes/{sha256}/comments](https://virustotal.readme.io/reference/monitorpartner-hashes-comments)):

* tag:ignored

Here you can see an example:

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor_partner/hashes"
querystring = {"filter": "engine:<engine-name>"}

response = session.get(url, params=querystring)
print(response.text)
```

```json
{
 "data": [
  {
   "attributes": {
    "last_analysis_date": 1517433370,
    "last_analysis_results": {
     "[ENGINE-NAME]": {
      "category": "undetected",
      "engine_name": "[ENGINE-NAME]",
      "engine_update": "20180131",
      "engine_version": "1.1.1.3",
      "method": "blacklist",
      "result": null
     }...
    },
    "last_detections_count": 1,
    "md5": "432fb4158186f0c8268813741939239a",
    "sha1": "6d06bba4f7625409e8a2f7e201c38b1b5925609a",
    "sha256": "29037cca6156dbf44a80a0c785f2b9d5c205cecd3bf7b044d99b462149bc5ae8",
    "size": 16384
   },
   "id": "29037cca6156dbf44a80a0c785f2b9d5c205cecd3bf7b044d99b462149bc5ae8",
   "type": "monitor_hash"
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
    "/monitor_partner/hashes": {
      "get": {
        "summary": "Get a list of MonitorHashes detected by an engine",
        "description": "",
        "operationId": "monitorpartner-hashes",
        "parameters": [
          {
            "name": "filter",
            "in": "query",
            "description": "Retrieve hashes matching this condition, refer to the right block of the documentation",
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
            "description": "Maximum number of items to retrieve (max: 40)",
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