# Source: https://virustotal.readme.io/reference/delete-notifications-from-the-ioc-stream.md

# Delete notifications from the IoC Stream

Uses the same filters than the IoC Stream ([GET /ioc\_stream](https://virustotal.readme.io/reference/get-objects-from-the-ioc-stream)) to delete all the matching notifications.

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
    "/ioc_stream": {
      "delete": {
        "summary": "Delete notifications from the IoC Stream",
        "description": "",
        "operationId": "delete-notifications-from-the-ioc-stream",
        "parameters": [
          {
            "name": "filter",
            "in": "query",
            "description": "Filter string",
            "schema": {
              "type": "string"
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
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            }
          },
          "429": {
            "description": "429",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"TooManyRequests\",\n    \"message\": \"Notifications already being deleted. Depending on volume this may take a while.\"\n}"
                  }
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