# Source: https://virustotal.readme.io/reference/monitorpartner-detectionsbundle-download.md

# Download a daily detection bundle directly

Each day a CSV formatted list with hash detections is generated for each engine.

Each line contains an owner company, hash, analysis history link and a hash download url.

You should access each engine bundle pointing to /api/v3/monitor\_partner/detections\_bundle/{engine_name}/download

To download previous bundles you can use: /api/v3/monitor\_partner/detections\_bundle/{engine_name}/{date('%Y-%m-%d')}/download

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
    "/monitor_partner/detections_bundle/{engine_name}/download": {
      "get": {
        "summary": "Download a daily detection bundle directly",
        "description": "",
        "operationId": "monitorpartner-detectionsbundle-download",
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