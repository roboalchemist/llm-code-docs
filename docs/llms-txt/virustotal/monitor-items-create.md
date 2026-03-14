# Source: https://virustotal.readme.io/reference/monitor-items-create.md

# Upload a file or create a new folder

This endpoint can be used to create or overwrite an already existing file using a multipart/form-data encoded request. The file has to be smaller than 32MB, for bigger files use a URL returned by [/items/upload\_url](https://virustotal.readme.io/reference/monitor-items-upload-url).

The parameter `path` indicates the path relative to your monitor root folder where the file is going to be stored. This path must include the name of the file being uploaded. For example `/folder/myfile.exe`. You can also provide a [MonitorItemID](https://virustotal.readme.io/reference/monitoritem-description) representing a path to a file previously uploaded to VT Monitor and this will upload the new file to this path, overwriting the file referenced by the MonitorItemID.

To create a new folder just make a request with the desired `path` or `item` ending it with a slash (`/`), for example `/mynewfolder/`.

The [MonitorItemID](https://virustotal.readme.io/reference/monitoritem-description) returned in the response can be used at a later stage to operate with the given file or folder and request its analysis information.

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor/items"

files = {'file': ('filepath', open('<filename>', 'rb'), 'application/octet-stream')}
args = {'path': '<monitor-path>'}

response = session.post(url, files=files, data=args)
print(response.text)
```

```curl
curl --request POST \
  --url 'https://www.virustotal.com/api/v3/monitor/items' \
  --header 'X-Apikey: <api-key>' \
  --form 'path=<monitor-folder-ending-with-slash>' \
  
```

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor/items"
args = {'path': '<monitor-folder-ending-with-slash>'}

response = session.post(url, data=args)
print(response.text)
```

```json
{
 "data": {
  "type": "monitor_item", 
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
    "/monitor/items": {
      "post": {
        "summary": "Upload a file or create a new folder",
        "description": "",
        "operationId": "monitor-items-create",
        "parameters": [
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
                  "file"
                ],
                "properties": {
                  "file": {
                    "type": "string",
                    "description": "Encoded file",
                    "format": "binary"
                  },
                  "path": {
                    "type": "string",
                    "description": "A path relative to current monitor user root folder. In must include the filename at the end of the path or a / if it's a folder being created"
                  },
                  "item": {
                    "type": "string",
                    "description": "A Monitor ID describing group and path"
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