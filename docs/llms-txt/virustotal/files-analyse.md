# Source: https://virustotal.readme.io/reference/files-analyse.md

# Request a file rescan (re-analyze)

Reanalyse a file already in VirusTotal

> ❗️ Caution
>
> This API endpoint has the potential to produce a denial of service on the scanning infrastructure if abused. Please contact us if you are going to be rescanning more than 50K files per day.

Files that have been already uploaded to VirusTotal can be re-analysed without uploading them again, you can use this endpoint for that purpose. The response is an object descriptor for the new analysis as in the [POST /files](https://virustotal.readme.io/reference/files-scan) endpoint. The ID contained in the descriptor can be used with the [GET /analyses/{id}](https://virustotal.readme.io/reference/analysis) endpoint to get information about the analysis.

```json
{
  "data": {
    "type": "analysis",
    "id": "NjY0MjRlOTFjMDIyYTkyNWM0NjU2NWQzYWNlMzFmZmI6MTQ3NTA0ODI3Nw=="
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
    "/files/{id}/analyse": {
      "post": {
        "summary": "Request a file rescan (re-analyze)",
        "description": "Reanalyse a file already in VirusTotal",
        "operationId": "files-analyse",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "SHA-256, SHA-1 or MD5 identifying the file",
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