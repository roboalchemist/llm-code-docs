# Source: https://virustotal.readme.io/reference/get-comments.md

# Get latest comments

This endpoint retrieves information about the latest comments added to VirusTotal.\
You can do some filtering over those comments, and get only those that contains a certain tag inside (e.g. filter=tag:malware).

```json
{
  "meta": {
    "cursor": "Cs8BChEKBGRhdGUSCQiCnsTiupvwAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgNVUkwiQDAxMTkxNTk0MmRiNTU2YmJhYjUxMzdmNzYxZWZlNjFmZWQyYjAwNTk4ZmVhOTAwMzYwYjgwMGIxOTNhN2JmMzEMCxIHQ29tbWVudCJJMDExOTE1OTQyZGI1NTZiYmFiNTEzN2Y3NjFlZmU2MWZlZDJiMDA1OThmZWE5MDAzNjBiODAwYjE5M2E3YmYzMS1kOTRkN2M4YQwYACAB"
  },
  "data": [
    {
      "attributes": {
        "votes": {
          "positive": 0,
          "abuse": 0,
          "negative": 0
        },
        "tags": [
          "_:api",
          "_:public",
          "aicc",
          "monitorapp",
          "malware"
        ],
        "text": "#aicc #monitorapp #malware",
        "html": "#aicc #monitorapp #malware",
        "date": 1619424604
      },
      "type": "comment",
      "id": "u-011915942db556bbab5137f761efe61fed2b00598fea900360b800b193a7bf31-d94d7c8a",
      "links": {
        "self": "https://www.virustotal.com/api/v3/comments/u-011915942db556bbab5137f761efe61fed2b00598fea900360b800b193a7bf31-d94d7c8a"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/comments?filter=tag%3Amalware&limit=1",
    "next": "https://www.virustotal.com/api/v3/comments?filter=tag%3Amalware&cursor=Cs8BChEKBGRhdGUSCQiCnsTiupvwAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgNVUkwiQDAxMTkxNTk0MmRiNTU2YmJhYjUxMzdmNzYxZWZlNjFmZWQyYjAwNTk4ZmVhOTAwMzYwYjgwMGIxOTNhN2JmMzEMCxIHQ29tbWVudCJJMDExOTE1OTQyZGI1NTZiYmFiNTEzN2Y3NjFlZmU2MWZlZDJiMDA1OThmZWE5MDAzNjBiODAwYjE5M2E3YmYzMS1kOTRkN2M4YQwYACAB&limit=1"
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
    "/comments": {
      "get": {
        "summary": "Get latest comments",
        "description": "",
        "operationId": "get-comments",
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
            "name": "limit",
            "in": "query",
            "description": "Number of items to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Filter returned elements",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
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