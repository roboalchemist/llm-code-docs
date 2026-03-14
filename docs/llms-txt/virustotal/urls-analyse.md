# Source: https://virustotal.readme.io/reference/urls-analyse.md

# Request a URL rescan (re-analyze)

> 📘
>
> See [URL identifiers](https://virustotal.readme.io/reference/url#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

Returns a [Analysis](https://virustotal.readme.io/reference/analyses-object) object descriptor which can be used in the [GET/analyses/{id}](https://virustotal.readme.io/reference/analysis) API endpoint to get further information about the analysis status.

```json
{
    "data": {
        "id": "u-a354494a73382ea0b4bc47f4c9e8d6c578027cd4598196dc88f05a22b5817293-1604933101",
        "type": "analysis"
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
    "/urls/{id}/analyse": {
      "post": {
        "summary": "Request a URL rescan (re-analyze)",
        "description": "",
        "operationId": "urls-analyse",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "URL identifier",
            "schema": {
              "type": "string"
            },
            "required": true
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