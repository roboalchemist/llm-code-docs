# Source: https://virustotal.readme.io/reference/groups-relationships.md

# Get objects related to a group

Group objects have relationships to other objects. As mentioned in the  [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

The relationships supported by group objects are described in the [Group object section](https://virustotal.readme.io/reference/group-object).

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-enterprise",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [],
  "paths": {
    "/groups/{id}/{relationship}": {
      "get": {
        "summary": "Get objects related to a group",
        "description": "",
        "operationId": "groups-relationships",
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
            "description": "Group ID.",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/group-object#relationships))",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of related objects to retrieve",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "integer",
              "format": "int32"
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