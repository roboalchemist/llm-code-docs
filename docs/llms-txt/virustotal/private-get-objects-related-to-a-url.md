# Source: https://virustotal.readme.io/reference/private-get-objects-related-to-a-url.md

# Get objects related to a private URL

> 📘
>
> See [URL identifiers](https://virustotal.readme.io/reference/url#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

URL objects have number of relationships to other URLs and objects. As mentioned in the [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Some relationships are accessible only to users who have access to VirusTotal Enterprise package.

The relationships supported by URL objects are documented in the [URL](https://virustotal.readme.io/reference/private-urls) API object page.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-private-scanning",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/urls/{id}/{relationship}": {
      "get": {
        "summary": "Get objects related to a private URL",
        "description": "",
        "operationId": "private-get-objects-related-to-a-url",
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
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/url-object#relationships))",
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
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of related objects to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
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
        "security": [],
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/urls/{id}/analyses \\\n  --header 'x-apikey: <your API key>'",
              "name": "analyses"
            },
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/urls/{id}/downloaded_files \\\n  --header 'x-apikey: <your API key>'",
              "name": "downloaded_files"
            },
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/urls/{id}/graphs \\\n  --header 'x-apikey: <your API key>'",
              "name": "graphs"
            },
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/urls/{id}/last_serving_ip_address \\\n  --header 'x-apikey: <your API key>'",
              "name": "last_serving_ip_address"
            },
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/urls/{id}/redirecting_urls \\\n  --header 'x-apikey: <your API key>'",
              "name": "redirecting_urls"
            },
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/urls/{id}/submissions \\\n  --header 'x-apikey: <your API key>'",
              "name": "submissions"
            }
          ],
          "samples-languages": [
            "curl"
          ]
        }
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