# Source: https://virustotal.readme.io/reference/revoke-saved-searches-access.md

# Revoke access to a Saved Search

Use this endpoint to revoke [saved search](https://virustotal.readme.io/reference/saved-search-object)  access for a specific user or the owner's entire group.

This endpoint is **restricted** to use by the **owner** and **editors** of the saved search only.

<Callout icon="🚧" theme="warn">
  **Important:** This endpoint requires a request body, even when utilizing the **DELETE** method.
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

# Examples

Revoke viewer privileges for all members of my group from the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

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
response = requests.delete(url, json=payload, headers=headers)
```

Revoke editor privileges for ana and alex from the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

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
response = requests.delete(url, json=payload, headers=headers)
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
      "delete": {
        "summary": "Revoke access to a Saved Search",
        "description": "",
        "operationId": "revoke-saved-searches-access",
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
            "name": "access",
            "in": "path",
            "description": "Access level. Options: viewers, editors",
            "schema": {
              "type": "string"
            },
            "required": true
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
                    "description": "Payload to identify user/group identifier."
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