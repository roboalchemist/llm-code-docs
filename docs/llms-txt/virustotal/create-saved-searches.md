# Source: https://virustotal.readme.io/reference/create-saved-searches.md

# Create a Saved Search

Use this endpoint to save a search or query and you will automatically become the **owner** of the [saved search](https://virustotal.readme.io/reference/saved-search-object). This is an example request body:

```json Request body example
{
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "saved search's name",
            "description": "saved search's description",
            "search_query": "saved search's query/logic",
            "private": true,
            "tags": ["saved search's associated tags"]
        }
    }
}
```

The `private` field determines the search's accessibility:

* if set to `false` (public), the saved search is viewable by all VirusTotal users.
* if set to `true` (private), access is restricted to the owner and any specific users/groups with whom the owner has individually shared the search.

To update the `private` field check out this [endpoint](https://virustotal.readme.io/reference/update-saved-searches) .

To share a saved search with certain users or the owner's entire group, check out this [endpoint](https://virustotal.readme.io/reference/share-saved-searches) .

# Examples

```python
import requests

url = f"https://www.virustotal.com/api/v3/saved_searches"
payload = {
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "Potential Gamaredon-related document activity",
            "description": "This Intelligence search query is designed to find files that match a specific set of characteristics, generally indicative of a particular type of malware or activity.",
            "search_query": "(type:document) and (behavior_processes:*.ru* and behavior_processes:*DavSetCookie* and behavior_processes:*http*) and (behavior_network:*.ru* or embedded_domain:*.ru* or embedded_url:*.ru*)",
            "private": True,
            "tags": ["FILE", "Gamaredon", "Behaviour"]
        }
    }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
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
    "/saved_searches": {
      "post": {
        "summary": "Create a Saved Search",
        "description": "",
        "operationId": "create-saved-searches",
        "parameters": [
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
            "description": "Your AP Key.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "Payload to post.",
                    "format": "json"
                  }
                }
              }
            }
          }
        },
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