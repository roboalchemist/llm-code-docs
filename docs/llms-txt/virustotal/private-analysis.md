# Source: https://virustotal.readme.io/reference/private-analysis.md

# Get a private analysis

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

With this endpoint you can check the status of a private file analysis. It expects the analysis ID returned by the [POST /files](https://virustotal.readme.io/reference/upload-file-private-scanning) endpoint, and will return a private analysis object with information about the analysis.

```json Example response
{
  "meta": {
    "file_info": {
      "size": 5,
      "sha256": "11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772",
      "sha1": "7bae8076a5771865123be7112468b79e9d78a640",
      "md5": "e5828c564f71fea3a12dde8bd5d27063"
    }
  },
  "data": {
    "attributes": {
      "date": 1620127014,
      "status": "completed"
    },
    "type": "private_analysis",
    "id": "ZTU4MjhjNTY0ZjcxZmVhM2ExMmRkZThiZDVkMjcwNjM6MTYyMDEyNzAxNA==",
    "links": {
      "self": "https://virustotal.com/api/v3/private/analyses/ZTU4MjhjNTY0ZjcxZmVhM2ExMmRkZThiZDVkMjcwNjM6MTYyMDEyNzAxNA=="
    }
  }
}
```

The `status` attribute in the private analysis object can be either "queued" or "completed", once it gets completed, you can use the `sha256` in the `file_info` section with the [GET /files/{id}](https://virustotal.readme.io/reference/private-files-info) for getting all the information that VirusTotal has generated for the analysed file. Alternatively you could use [GET /analyses/{id}/item](https://virustotal.readme.io/reference/private-files-relationships) for the same purpose.

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
    "/analyses/{id}": {
      "get": {
        "summary": "Get a private analysis",
        "description": "",
        "operationId": "private-analysis",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Analysis identifier",
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