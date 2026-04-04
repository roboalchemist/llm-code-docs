# Source: https://virustotal.readme.io/reference/get-hunting-notification-files.md

# Retrieve file objects for Livehunt notifications

> ❗️ Important
>
> Hunting notifications files are no longer showed in the web interface. Use the [/api/v3/ioc\_stream](https://virustotal.readme.io/reference/get-objects-from-the-ioc-stream) endpoint instead to retrieve objects from IoC-Stream notifications.

Each file object returned, *in addition to all the file details*, has a `context_attributes` property that contains information about the VT Hunting Livehunt notification tied to the file, this is an example:

```json Example context attributes for a matching file
"context_attributes": {
  "match_in_subfile": false,
  "notification_date": 1543301214,
  "notification_id": "961092289288866-4582222113734656-3c7f77cc43338e14824c111671beef30",
  "notification_snippet": "00 61 64 64 41 75 64 69 6F [...]",
  "notification_source_key": "b3190c38",
  "notification_tags": [
    "bozok",
    "rats",
    "a2d2906f7ad5265165c25baed76d342b48b8bc5f4d9db6004e9e6dd72eaea4e1"
  ],
  "ruleset_id": "5706526672224256",
  "ruleset_name": "rats",
  "rule_name": "Bozok",
  "rule_tags": [],
}
```

Other than that, the `filter` parameter allows to filter the matching files according to the VT Hunting Livehunt notification properties. You can filter by the name of the matching rule, match date, rule namespace, ruleset or file hash. Notice however that this only works with the exact keyword, not substrings of it.

For more information check the [user's hunting\_notification\_files relationship](https://virustotal.readme.io/reference/user-hunting_notification_files).

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
    "/intelligence/hunting_notification_files": {
      "get": {
        "summary": "Retrieve file objects for Livehunt notifications",
        "description": "",
        "operationId": "get-hunting-notification-files",
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
            "name": "limit",
            "in": "query",
            "description": "Maximum number of notifications to retrieve",
            "schema": {
              "type": "string",
              "default": "10"
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
            "description": "String to search with in the hunting notification tags",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "count_limit",
            "in": "query",
            "description": "Maximum number of notifications counted (meta.count in the response) 10,000 max",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 200
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