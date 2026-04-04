# Source: https://virustotal.readme.io/reference/monitorpartner-files-download-url.md

# Retrieve a download url for a file with a given sha256 hash

This endpoint allows you to get a download url for a file with a given sha256 hash. These URLs are ephemeral and have a one hour expiration date.

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor_partner/files/{sha256}/download_url"
response = session.get(url)
print(response.text)
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
    "/monitor_partner/files/{sha256}/download_url": {
      "get": {
        "summary": "Retrieve a download url for a file with a given sha256 hash",
        "description": "",
        "operationId": "monitorpartner-files-download-url",
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
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "sha256",
            "in": "path",
            "description": "Hash sha256",
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