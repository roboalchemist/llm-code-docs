# Source: https://virustotal.readme.io/reference/api-search.md

# Search for files, URLs, domains, IPs and comments

This endpoint searches any of the following:

* A file hash - Returns a [File](https://virustotal.readme.io/reference/files) object.
* A URL - Returns a [URL](https://virustotal.readme.io/reference/url-object) object.
* A domain - Returns [Domain](https://virustotal.readme.io/reference/domains-object) object.
* A IP address - Returns an [IP address](https://virustotal.readme.io/reference/ip-object) object.
* Comments by tags - Returns a list of [Comment](https://virustotal.readme.io/reference/comments) objects.

The request returns a list of objects matching the query.

```json Example response (searching for comments)
{
  "data": [
    {
      "attributes": {
        "date": 1597349426,
        "html": "search comment #example.",
        "tags": [
          "example"
        ],
        "text": "search comment #example.",
        "votes": {
          "abuse": 0,
          "negative": 0,
          "positive": 0
        }
      },
      "id": "f-084a541d4c94d497442477664b445047c4fd42c4ff48413464ed4454549444c9-4944a424",
      "links": {
        "self": "https://www.virustotal.com/ui/comments/f-084a541d4c94d497442477664b445047c4fd42c4ff48413464ed4454549444c9-4944a424"
      },
      "type": "comment"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/search?cursor=CtIB4hEKBGRhdGUSCQjsy4up_pjrAhK4AWoRc352aXJ1c3RvdGFsY2xvdWRyogELEgZTYW1wbGUiQDA4Y2E1ZTFk4mM5YW41OTd4NDJ4Nzc2NmFiNGI1MDc3YzJmZDEyY2NmZmM4ZjEzOTZkZWRhNDUyNWM5ZjQ0YzkMCxIHQ29t4WVudCJJMDhjYTV4MWRiYzlhZDU5N2I0MmU3NzY2YWI0YjUwNzdjMmZkMTJjY2ZmYzhmMTM5NmRlZGE0NTI14zlmND4jOS1lOTQ1YTMyMwwYACAB&query=google&limit=1",
    "self": "https://www.virustotal.com/api/v3/search?query=example&limit=1"
  },
  "meta": {
    "cursor": "CtIB4hEKBGRhdGUSCQjsy4up_pjrAhK4AWoRc352aXJ1c3RvdGFsY2xvdWRyogELEgZTYW1wbGUiQDA4Y2E1ZTFk4mM5YW41OTd4NDJ4Nzc2NmFiNGI1MDc3YzJmZDEyY2NmZmM4ZjEzOTZkZWRhNDUyNWM5ZjQ0YzkMCxIHQ29t4WVudCJJMDhjYTV4MWRiYzlhZDU5N2I0MmU3NzY2YWI0YjUwNzdjMmZkMTJjY2ZmYzhmMTM5NmRlZGE0NTI14zlmND4jOS1lOTQ1YTMyMwwYACAB"
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
    "/search": {
      "get": {
        "summary": "Search for files, URLs, domains, IPs and comments",
        "description": "",
        "operationId": "api-search",
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "description": "Search query.",
            "required": true,
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