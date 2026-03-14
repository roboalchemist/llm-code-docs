# Source: https://virustotal.readme.io/reference/list-hunting-rulesets.md

# Get Livehunt rulesets

This endpoint returns the VT Hunting Livehunt rulesets viewable by the user making the request. A ruleset is viewable by a user either if it was created by the user or if it was shared with him by someone else. This endpoint is equivalent to `GET /users/{user}/hunting_rulesets`, where `{user}` is the username of the user owning the API key. In fact, if you look carefully at the example response below you'll notice that the `self` and `next` links do not point to `/intelligence/hunting_rulesets` but to `/users/{user}/hunting_rulesets`

```json Example response
{
  "data": [
    {
      "type": "hunting_ruleset",
      "id": "{id}",
      "links": {
      	"self": "https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/{id}"
      },
      "attributes": {
        "creation_date": 1523635880,
        "enabled": true,
        "limit": 1000,
        "modification_date": 1525263069,
        "name": "foo",
        "notification_emails": [],
        "rules": "rule foo {condition: false}"
      }
    },
    { .. ruleset 2 .. },
    { .. ruleset 3 .. },
    { .. ruleset 4 .. },
  ],
  "meta": {
    "cursor": "Cu0FCsACCpIC9xuRl9v..."
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/users/{user}/hunting_rulesets",
    "next": "https://www.virustotal.com/api/v3/users/{user}/hunting_rulesets?cursor=Cu0FCsACCpIC9xuRl9v..."
  }
}
```

The `filter` parameter allows to filter the rulesets according to the values of certain attributes. For example you can get only the enabled rulesets with `enabled:true`. With `name:foo` and `rules:foo` you can search for rulesets having the word "foo" in their names or in the YARA rules respectively. Notice however that this only works with full words (words delimited by non-alphanumeric characters), if the ruleset's name is "foobar" it won't appear if you filter with `name:foo`. You can also filter the rulesets with the same tag, by using for example `filter=tag:auto`.

You can combine multiple filters separating them with spaces, for example: `filter=enabled:true name:foo`.

The `order` parameters control the order in which rulesets are returned, accepted orders are: `name`, `creation_date` and `modification_date`. You can prepend `+` and `-` suffixes to specify ascending and descending orders (examples: `name-`, `creation_date+`, ). If not suffix is specified the order is ascending by default.

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
    "/intelligence/hunting_rulesets": {
      "get": {
        "summary": "Get Livehunt rulesets",
        "description": "",
        "operationId": "list-hunting-rulesets",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of rulesets to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Return the rulesets matching the given criteria only",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Sort order",
            "schema": {
              "type": "string"
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