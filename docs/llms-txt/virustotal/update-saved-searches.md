# Source: https://virustotal.readme.io/reference/update-saved-searches.md

# Update a Saved Search

Use this endpoint to modify the attributes of an existing [saved search](https://virustotal.readme.io/reference/saved-search-object). This is an example request body:

```json Request body example
{
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "new saved search's name",
            "description": "new saved search's description",
            "search_query": "new saved search's query/logic",
            "private": false,
            "tags": ["saved search's associated tags"]
        }
    }
}
```

The `private` field determines the search's accessibility:

* if set to `false` (public), the saved search is viewable by all VirusTotal users.
* if set to `true` (private), access is restricted to the owner and any specific users/groups with whom the owner has individually shared the search.

<Callout icon="🚧" theme="warn">
  **Important Note on Updating Tags:** To modify the tag list using this endpoint (adding or removing a subset of tags), you must first  [_retrieve_](https://virustotal.readme.io/reference/get-saved-search) the current full list of tags.

* **To Delete All Tags:** use this endpoint with an empty list of tags (`[]`).
* **To Add a New Tags:** [*retrieve*](https://virustotal.readme.io/reference/get-saved-search) the current list, append the new tags, and submit the resulting list.
* **To Remove a Subset of Tags:** [*retrieve*](https://virustotal.readme.io/reference/get-saved-search) the current list, filter out the tags to be removed, and submit the remaining list.\ </Callout>

This endpoint is **restricted** to use by the **owner** and **editors** of the saved search only.

To share a saved search with certain users or the owner's entire group, check out this [endpoint](https://virustotal.readme.io/reference/share-saved-searches)

# Examples

Change the name and the description of the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

```python
import requests

object_id = "f60631d600b44a91a8b20cef8c77aeac"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}"

payload = {
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "This is the new name of the saved search",
            "description": "This is the new description of the saved search"
        }
    }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.patch(url, json=payload, headers=headers)
```

Share the saved search with ID f60631d600b44a91a8b20cef8c77aeac with the entire community.

```python
import requests

object_id = "f60631d600b44a91a8b20cef8c77aeac"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}"

payload = {
    "data": {
        "type": "saved_search",
        "attributes": {
            "private": False
        }
    }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.patch(url, json=payload, headers=headers)
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
      "patch": {
        "summary": "Update a Saved Search",
        "description": "",
        "operationId": "update-saved-searches",
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
                    "description": "Payload to patch."
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