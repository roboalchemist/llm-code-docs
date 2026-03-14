# Source: https://virustotal.readme.io/reference/private-scanning-get-zip-file.md

# Check a ZIP file’s status

This endpoint returns information about a ZIP file.

```json
{
  "data": {
    "type": "zip_file",
    "id": "4939392292",
    "attributes": {
      "status": "creating",
      "progress": 45,
      "files_ok": 3,
      "files_error": 0
    }  
  }
}
```

The `status` attribute contains one of the following statuses:

* `starting`
* `creating`
* `finished`
* `timeout`
* `error-starting`
* `error-creating`

When the status is `finished` you may proceed to download the file.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-private-scanning",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/zip_files/{id}": {
      "get": {
        "summary": "Check a ZIP file’s status",
        "description": "",
        "operationId": "private-scanning-get-zip-file",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ZIP file identifier",
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
              "application/json": {
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
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
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