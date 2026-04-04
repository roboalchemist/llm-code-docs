# Source: https://virustotal.readme.io/reference/collections-export-aggregations.md

# 🔒 Export aggregations from a collection

> 🚧 Deprecated endpoint. This has been replaced by Google Threat Intelligence
>
> We are gearing up to the transition into Google Threat Intelligence! The endpoints are documented at [**Threat Landscape** -> **Threat Actors, Malware & Tools, Campaigns, IoC Collections** section](https://gtidocs.virustotal.com/reference/threat-actors-malware-tools-campaigns-ioc-collections). Note that when upgrading to Google Threat Intelligence you will enjoy a much larger knowledge base of IoC collections, threat actors, malware, toolkits and campaigns.
>
> * For **exporting aggregations from an IoC's collection**, refer to [`/collections/{id}/aggregations/download/{format}` endpoint documented here](https://gtidocs.virustotal.com/reference/export-threat-aggregations).
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
    "/collections/{id}/aggregations/download/{format}": {
      "get": {
        "summary": "🔒 Export aggregations from a collection",
        "description": "",
        "operationId": "collections-export-aggregations",
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
            "description": "Export format (one of `json` or `csv`)",
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
                    "value": "{\n\t\"files\": {\n\t\t\"contacted_urls\": [\n\t\t\t{\n\t\t\t\t\"count\": 2,\n\t\t\t\t\"value\": \"http://ocsp.digicert.com/\"\n\t\t\t},\n\t\t\t{\n\t\t\t\t\"count\": 2,\n\t\t\t\t\"value\": \"http://crl3.digicert.com/Omniroot2025.crl\"\n\t\t\t}\n      ...\n\t\t],\n\t\t\"contacted_domains\": [\n\t\t\t{\n\t\t\t\t\"count\": 4,\n\t\t\t\t\"value\": \"nexusrules.officeapps.live.com\"\n\t\t\t},\n\t\t\t{\n\t\t\t\t\"count\": 4,\n\t\t\t\t\"value\": \"officeclient.microsoft.com\"\n\t\t\t},\n      ...\n\t\t],\n    ...\n\t},\n  ...\n}"
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