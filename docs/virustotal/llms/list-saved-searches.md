# Source: https://virustotal.readme.io/reference/list-saved-searches.md

# List Saved Searches

Use this endpoint to list [Saved Searches](https://virustotal.readme.io/reference/saved-search-object) you have access to as owner, editor or viewer.

# Filters

Available filters for saved searches:

* `creation_date`: filters saved searches by their last modification date, accepting either the `YYYY-MM-DDTHH:MM:SS` format or an Epoch UTC timestamp format. E.g.:`creation_date:2025-10-27+`, `creation_date:2025-11-27T01:15:09`, `creation_date:2025-09-15-`, `creation_date:1764326675-`.
* `last_modification_date`: filters saved searches by their last modification date, accepting either the `YYYY-MM-DDTHH:MM:SS` format or an Epoch UTC timestamp format. E.g.:`last_modification_date:2025-10-28+`, `last_modification_date:2025-10-27T09:31:25`, `last_modification_date:2025-10-26-`, `last_modification_date:1763721875+`.
* `shared_with_me:true`: filters saved searches that were created by other users but shared with the current one. Note that this filter only supports the `true` value.
* `origin`: filters saved searches by their origin. Available options: **Crowdsourced** for those created by the community and **Partner** for those created by trusted partners. E.g.: `origin:Crowdsourced`, `origin:Partner`.
* `owner`: filters saved searches based on their creator/owner user identifier. It is particularly useful for listing saved searches created by users whose content you trust or want to follow. E.g.:`owner:<user_id>`.
* `editor`: filters saved searches editable by a specified user. E.g.:`editor:<user_id>`.
* `viewer`: Filters saved searches viewable by a specified user. E.g.:`viewer:<user_id>`.

# Orders

Available sorting options for saved searches:

* `creation_date`: sorts saved searches by their last modification date ascending (`+`) or descending (`-`). E.g.:`creation_date+`, `creation_date-`.
* `last_modification_date`: sorts saved searches by their last modification date ascending (`+`) or descending (`-`). E.g.:`last_modification_date+`, `last_modification_date-` (default order).
* `name`: sorts saved searches by their name ascending (`+`) or descending (`-`). E.g.:`name+`, `name-`.

# Examples

List all of my saved searches, including their editors, and display only the name and description.

```python
import requests
import urllib

filters = "shared_with_me:true"
relationships = "editors"
attributes = "name,description"

url = f"https://www.virustotal.com/api/v3/saved_searches?filter={urllib.parse.quote(filters)}&relationships={relationships}&attributes={attributes}"

headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Retrieve saved searches created by Ana during August and September 2025.

```python
import requests
import urllib

filters = "owner:ana creation_date:2025-08-01+ creation_date:2025-10-01+"

url = f"https://www.virustotal.com/api/v3/saved_searches?filter={urllib.parse.quote(filters)}"

headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

List all saved searches created by any Partner.

```python
import requests
import urllib

filters = "origin:Partner"

url = f"https://www.virustotal.com/api/v3/saved_searches?filter={urllib.parse.quote(filters)}"

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
    "/saved_searches": {
      "get": {
        "summary": "List Saved Searches",
        "description": "",
        "operationId": "list-saved-searches",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API Key.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Filter saved searches by different properties.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of saved searches to retrieve. The maximum value is 40.",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Sorting order.",
            "schema": {
              "type": "string",
              "default": "last_modification_date-"
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
            "name": "attributes",
            "in": "query",
            "description": "A comma-separated list of the [_saved search attributes_](https://virustotal.readme.io/reference/saved-search-object#object-attributes) to be returned. (All attributes are returned by default.)",
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