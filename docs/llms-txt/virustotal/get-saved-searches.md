# Source: https://virustotal.readme.io/reference/get-saved-searches.md

# Get a Saved Search

This endpoint returns a [Saved Search](https://virustotal.readme.io/reference/saved-search-object) object.

# Examples

Get only the name, description and tags of the saved search 0a49acd622a44982b1986984ba31c15b.

```python
import requests

object_id = "0a49acd622a44982b1986984ba31c15b"
attributes = "name,description,tags"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}?attributes={attributes}"

headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Retrieve the saved search with ID 0a49acd622a44982b1986984ba31c15b, including its owner and all editors.

```python
import requests

object_id = "0a49acd622a44982b1986984ba31c15b"
relationships = "owner,editors"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}?relationships={relationships}"

headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
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
    "/saved_searches/{id}": {
      "get": {
        "summary": "Get a Saved Search",
        "description": "",
        "operationId": "get-saved-searches",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Saved Search's ID.",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "attributes",
            "in": "query",
            "description": "A comma-separated list of the [_saved search attributes_](https://virustotal.readme.io/reference/saved-search-object#object-attributes) to be returned. (All attributes are returned by default.)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "relationships",
            "in": "query",
            "description": "Provides additional information about the saved search as [_relationships_](https://virustotal.readme.io/reference/saved-search-object#relationships)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API Key.",
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