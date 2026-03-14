# Source: https://virustotal.readme.io/reference/share-saved-searches.md

# Share a Saved Search

Use this endpoint to grant **viewer** or **editor** permissions to a certain [saved search](https://virustotal.readme.io/reference/saved-search-object)  for:

* individual **users**
* owner's **group**

This endpoint is **restricted** to use by the **owner** and **editors** of the saved search only.

<Callout icon="🚧" theme="warn">
  Note that **editor** privileges can **only be granted to members belonging to the same group as the owner** of the saved search.
</Callout>

This is an example request body:

```json Request body example
{
    "data": [
        {
            "id": "user id",
            "type": "user"
        },
        {
            "id": "group id",
            "type": "group"
        }
    ]
}
```

To revoke the access to a saved search check out this [endpoint](https://virustotal.readme.io/reference/revoke-saved-searches-access).

# Examples

Grant view access to all members of my group for the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

```python
import requests
object_id = "f60631d600b44a91a8b20cef8c77aeac"
access = "viewers"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}/relationship/{access}"

payload = {
    "data": [
        {
            "id": "my_group_id",
            "type": "group"
        }
    ]
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
```

Grant edit access to ana and alex for the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

```python
import requests
object_id = "f60631d600b44a91a8b20cef8c77aeac"
access = "editors"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}/relationship/{access}"

payload = {
    "data": [
        {
            "id": "ana",
            "type": "user"
        },
        {
            "id": "alex",
            "type": "user"
        }
    ]
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
    "/saved_searches/{id}/relationship/{access}": {
      "post": {
        "summary": "Share a Saved Search",
        "description": "",
        "operationId": "share-saved-searches",
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
            "name": "id",
            "in": "path",
            "description": "Saved Search's ID.",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "access",
            "in": "path",
            "description": "Access level. Options: viewers, editors",
            "schema": {
              "type": "string"
            },
            "required": true
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