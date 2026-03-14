# Source: https://virustotal.readme.io/reference/graphs-check-editor.md

# Check if a user or group can edit a graph

This endpoint returns true if the user or group has `Editor` access to the graph.

```json
{
    "data": false
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
    "/graphs/{id}/relationships/editors/{user_or_group_id}": {
      "get": {
        "summary": "Check if a user or group can edit a graph",
        "description": "",
        "operationId": "graphs-check-editor",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "description": "A 65 char length id which uniquely identify the graph.",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "user_or_group_id",
            "in": "path",
            "description": "User or group ID",
            "schema": {
              "type": "string"
            },
            "required": true
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