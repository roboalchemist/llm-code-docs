# Source: https://virustotal.readme.io/reference/graphs-relationships.md

# Get objects related to a graph

Graph objects have number of relationships to other objects. As mentioned in the  [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Some relationships are accesible only to users who have access to VirusTotal Intelligence.

The relationships supported by graph objects are documented in the [Graph](https://virustotal.readme.io/reference/graph-object) API object page.

```json
{
    "data": {
        "attributes": {
            "first_name": "Richard",
            "last_name": "Hendricks",
            "profile_phrase": "CEO of Pied Piper",
            "reputation": 1,
            "status": "active",
            "user_since": 1528111032
        },
        "id": "hendricks",
        "links": {
            "self": "https://www.virustotal.com/api/v3/users/hendricks"
        },
        "type": "user"
    },
    "links": {
        "self": "https://www.virustotal.com/api/v3/graphs/g510b3e01190b9e6001f7ed7d14015558b11ca9d3e87367b6b809bbb402645bf2/owner"
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
    "/graphs/{id}/{relationship}": {
      "get": {
        "summary": "Get objects related to a graph",
        "description": "",
        "operationId": "graphs-relationships",
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
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/graph-object#relationships))",
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
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": ""
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