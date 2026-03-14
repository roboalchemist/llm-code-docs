# Source: https://virustotal.readme.io/reference/monitorpartner-detectionsbundle-download-url.md

# Get a daily detection bundle download URL

Refer to /detections\_bundle/download for additional options.

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
    "/monitor_partner/detections_bundle/{engine_name}/download_url": {
      "get": {
        "summary": "Get a daily detection bundle download URL",
        "description": "",
        "operationId": "monitorpartner-detectionsbundle-download-url",
        "parameters": [
          {
            "name": "engine_name",
            "in": "path",
            "description": "Name of your engine",
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