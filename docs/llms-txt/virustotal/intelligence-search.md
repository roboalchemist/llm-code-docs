# Source: https://virustotal.readme.io/reference/intelligence-search.md

# Advanced corpus search

> 📘 Quota consumption
>
> This endpoint consumes VirusTotal API quota if user has private/premium API or VirusTotal Intelligence quota if user only has VirusTotal Intelligence.

> 🚧 Special privileges required
>
> This endpoint is only available for users with premium privileges.

> 🚧
>
> Searches using a fuzzy hash (ssdeep, TLSH, ...) are throttled due to performance reasons. The typical throttler is 15 searches / minute.

This endpoint allows to search for files in the VirusTotal's dataset, using the same [query syntax](https://virustotal.readme.io/docs/virustotal-intelligence-introduction) that you would use in the VirusTotal Intelligence user interface, where you can use this [full list of modifiers](https://virustotal.readme.io/docs/search-modifiers-full-list). **URL Safe encoding must be used when using this endpoint programatically.**

The result from this endpoint is a collection of file objects that match the given query. If the `descriptors_only` parameter is set to `true`, the resulting collection will contain only the object descriptors. This is useful if you are interested in getting only the SHA-256 of the matching files. In those cases you better set `descriptors_only=true` for reducing the latency of your requests.

> 🚧 Content searches can not be sorted
>
> If your query contains content search the order parameter will make no effect.

The `order` parameter defines the order in which results are returned. They can be followed by a plus (`+`) or minus (`-`) sign for indicating ascending or descending order respectively (i.e: `<order>+`, `<order>-`). If no ascending/descending order is specified it's assumed to be ascending, so `<order>` and `<order>+` are equivalent. If the `order` parameter is not provided, items are returned in a default order. The following table shows supported and default orders for every kind of entity:

| Entity type | Supported orders                                                                     | Default order             |
| :---------- | :----------------------------------------------------------------------------------- | :------------------------ |
| file        | first\_submission\_date, last\_submission\_date, positives, times\_submitted, size   | last\_submission\_date-   |
| url         | first\_submission\_date, last\_submission\_date, positives, times\_submitted, status | last\_submission\_date-   |
| domain      | creation\_date, last\_modification\_date, last\_update\_date, positives              | last\_modification\_date- |
| ip          | ip, last\_modification\_date, positives                                              | last\_modification\_date- |

This request returns a list of API objects ([files](https://virustotal.readme.io/reference/files), [URLs](https://virustotal.readme.io/reference/url-object), [IP addresses](https://virustotal.readme.io/reference/ip-object) or [domains](https://virustotal.readme.io/reference/domains-object)).

Also, some context attributes are added in certain searches:

* When searching files by `content`. These context attributes are:
  * `confidence`: <*float*>  match confidence.
  * `match_in_subfile`: <*boolean*> whether the content match was found in a [subfile](https://virustotal.readme.io/reference/file-object-bundled-files) or not.
  * `snippet`: <*string*> snippet ID. This ID can be later used in `/intelligence/search/snippets/{id}` endpoint.

* When doing a hash similarity search:
  * `similarity_score`: <*float*> number between 0 and 1 indicating the percentage of the fuzzy hash that matched. For example, `1.0` indicates the hash is the same as the specified; `0.5` that half of the hash matches the one given.

```json Example response (search by file content)
{
  "data": [
    {
      "context_attributes": {
        "confidence": 1,
        "match_in_subfile": false,
        "snippet": "L3Z0c2FtcGxlcy8zODIzMzkzNjNhOTM2NDM2ZDM2MDM1MzFkM2IzOGEzMmUzMTUzNzM3MTM4MzY3MzBlM2Q2MzQ4MzY1M2MzYzNhfHw3MTg1Mzk2OjExfHwxNTk5NDY0OTQ3fHwzODIzMzkzNjNhOTM2NDM2ZDM2MDM1MzFkM2IzOGEzMmUzMTUzNzM3MTM4MzY3MzBlM2Q2MzQ4MzY1M2MzYzNh"
      },
      "id": "382339363a936436d3603531d3b38a32e315373713836730e3d63483653c3c3a",
      "type": "file"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/intelligence/search?cursor=H4sI...A&query=content%3A+%22hello+world%22&limit=1&descriptors_only=true",
    "self": "https://www.virustotal.com/api/v3/intelligence/search?query=content%3A%20%22hello%20world%22&descriptors_only=true&limit=1"
  },
  "meta": {
    "cursor": "H4sIAAA...",
    "days_back": 365
  }
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-enterprise",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [],
  "paths": {
    "/intelligence/search": {
      "get": {
        "summary": "Advanced corpus search",
        "description": "",
        "operationId": "intelligence-search",
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
            "name": "query",
            "in": "query",
            "description": "Search query using URL Safe encoding",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Sort order (see table in the description below)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of results per page (Max. 300)",
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
            "name": "descriptors_only",
            "in": "query",
            "description": "Whether to return full object information or just object descriptors.",
            "schema": {
              "type": "boolean",
              "default": false
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