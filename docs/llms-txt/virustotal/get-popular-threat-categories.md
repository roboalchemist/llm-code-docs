# Source: https://virustotal.readme.io/reference/get-popular-threat-categories.md

# Get a list of popular threat categories

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
    "/popular_threat_categories": {
      "get": {
        "summary": "Get a list of popular threat categories",
        "description": "",
        "operationId": "get-popular-threat-categories",
        "parameters": [
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
                    "value": "{\"data\": [\n  \"adware\", \"banker\", \"downloader\",\n  \"dropper\", \"fakeav\", \"hacktool\",\n  \"miner\", \"phising\", \"pua\",\n  \"ransomware\", \"spyware\", \"trojan\",\n  \"virus\", \"worm\"]}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "adware"
                      }
                    }
                  }
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
              "language": "shell",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/popular_threat_categories \\\n  --header 'x-apikey: <your API key>'"
            }
          ],
          "samples-languages": [
            "shell"
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