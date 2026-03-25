# Source: https://virustotal.readme.io/reference/list-collections.md

# 🔒 List collections

> 🚧 Deprecated endpoint. This has been replaced by Google Threat Intelligence
>
> We are gearing up to the transition into Google Threat Intelligence! The endpoints are documented at [**Threat Landscape** -> **Threat Actors, Malware & Tools, Campaigns, IoC Collections** section](https://gtidocs.virustotal.com/reference/threat-actors-malware-tools-campaigns-ioc-collections). Note that when upgrading to Google Threat Intelligence you will enjoy a much larger knowledge base of IoC collections, threat actors, malware, toolkits and campaigns.
>
> * For **listing IoC collections**, refer to [`/collections` endpoint documented here](https://gtidocs.virustotal.com/reference/list-threats).
> * Find the **new IoC collection object** definition [here](https://gtidocs.virustotal.com/reference/ioc-collection-object).
> * Find additional information related to the new endpoints [here](https://gtidocs.virustotal.com/reference/threat-actors-malware-tools-campaigns-ioc-collections).

> 🚧 Special privileges required
>
> This endpoint is only available to users with the [Threat Landscape module](https://www.virustotal.com/gui/threat-landscape-overview).

Returns a list of [Collections](https://virustotal.readme.io/reference/collections-object) objects.

Allowed filters:

* Text without modifiers: Collection's name, description or tag.
* `creation_date`: Collection's creation date.
* `description`: Collection's description. You can search for word or expressions (full-text search).
* `name`: Collection's name.
* `owner`: Collection's owner.
* `source_region`: Collections's source region. You can use [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes, the ISO or the full country name.
* `tag`: Collection's tag.
* `targeted_industry`: Collections's targeted industry.
* `targeted_region`: Collections's targeted region. Same use as `source_region`.
* `threat_category`: Collection's threat category.

Allowed orders:

* `creation_date`: Collection's creation date.
* `creation_day`: Collection's creation day. Collections created within the same day are sorted by relevance.
* `domains`: Number of domains in the collection.
* `files`: Number of files in the collection.
* `ip_addresses`: Number of IP addresses in the collection.
* `last_modification_date`: Collection's last modification date.
* `last_modification_day`: Collection's last modification day. Collections modified within the same day are sorted by relevance.
* `references`: Number of references in the collection.
* `urls`: Number of URLs in the collection.

Some examples:\
`GET /api/v3/collections?filter=source_region:US&order=files-`\
`GET /api/v3/collections?filter=targeted_industry:government&order:creation_day-`

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
    "/collections": {
      "get": {
        "summary": "🔒 List collections",
        "description": "",
        "operationId": "list-collections",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of collections to retrieve (max 40)",
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
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Filter collections by different properties",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Sorting order",
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
                    "value": "{\n\"meta\": {\n  \"cursor\": <string>\n},\n\"data\": [\n  <COLLECTION_OBJ>,\n  <COLLECTION_OBJ>,\n  ...\n],\n\"links\": {\n  \"self\": <string>,\n  \"next\": <string>\n}"
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