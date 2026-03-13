# Source: https://virustotal.readme.io/reference/graphs-add-viewer.md

# Grant users and groups permission to see a graph

This endpoint adds a user or group as a graph viewer.

```json Response example
{
    "data": [
        {
            "attributes": {
                "first_name": "Bertram",
                "last_name": "Gilfoyle",
                "profile_phrase": "",
                "reputation": 1,
                "status": "active",
                "user_since": 1530008602
            },
            "id": "gilfoyle",
            "links": {
                "self": "https://www.virustotal.com/api/v3/users/gilfoyle"
            },
            "type": "user"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/graphs/g5598743d5f3c699f1c90e76c2c2d541d41f1b56bd8114c06d181ed3f60cfcada/viewers?limit=10"
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
    "/graphs/{id}/relationships/viewers": {
      "post": {
        "summary": "Grant users and groups permission to see a graph",
        "description": "",
        "operationId": "graphs-add-viewer",
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