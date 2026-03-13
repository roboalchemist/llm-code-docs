# Source: https://virustotal.readme.io/reference/collections-export-iocs.md

# 🔒 Export IOCs from a collection

> 🚧 Deprecated endpoint. This has been replaced by Google Threat Intelligence
>
> We are gearing up to the transition into Google Threat Intelligence! The endpoints are documented at [**Threat Landscape** -> **Threat Actors, Malware & Tools, Campaigns, IoC Collections** section](https://gtidocs.virustotal.com/reference/threat-actors-malware-tools-campaigns-ioc-collections). Note that when upgrading to Google Threat Intelligence you will enjoy a much larger knowledge base of IoC collections, threat actors, malware, toolkits and campaigns.
>
> * For **exporting IoCs from a collection**, refer to [`/collections/{id}/download/{format}` endpoint documented here](https://gtidocs.virustotal.com/reference/export-threat-iocs).
> * Find the **new IoC collection object** definition [here](https://gtidocs.virustotal.com/reference/ioc-collection-object).
> * Find additional information related to the new endpoints [here](https://gtidocs.virustotal.com/reference/threat-actors-malware-tools-campaigns-ioc-collections).

> 🚧 Special privileges required
>
> This endpoint is only available to users with the [Threat Landscape module](https://www.virustotal.com/gui/threat-landscape-overview).

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
    "/collections/{id}/download/{format}": {
      "get": {
        "summary": "🔒 Export IOCs from a collection",
        "description": "",
        "operationId": "collections-export-iocs",
        "parameters": [
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
            "name": "id",
            "in": "path",
            "description": "Collection's ID",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "format",
            "in": "path",
            "description": "Export format (one of `json`, `csv`, or `stix`)",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"files\": [\n    \"009cc0f34f60467552ef79c3892c501043c972be55fe936efb30584975d45ec0\",\n    \"153117aa54492ca955b540ac0a8c21c1be98e9f7dd8636a36d73581ec1ddcf58\",\n    \"18479a93fc2d5acd7d71d596f27a5834b2b236b44219bb08f6ca06cf760b74f6\"\n  ],\n  \"threat_actors\": [\n    \"muddywater\"\n  ],\n  \"references\": [\n    \"153590cf5677a6ab5b5103382d41d4d8868a878a04104e86e936db63e4d186b8\"\n  ],\n  \"urls\": [\n    \"http://abrahamseed.co.za/db_template.php\",\n    \"http://absfinancialplanning.co.za/images/db_template.php\"\n  ]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "files": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "009cc0f34f60467552ef79c3892c501043c972be55fe936efb30584975d45ec0"
                      }
                    },
                    "threat_actors": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "muddywater"
                      }
                    },
                    "references": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "153590cf5677a6ab5b5103382d41d4d8868a878a04104e86e936db63e4d186b8"
                      }
                    },
                    "urls": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "http://abrahamseed.co.za/db_template.php"
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