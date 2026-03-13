# Source: https://virustotal.readme.io/reference/create-hunting-ruleset.md

# Create a new Livehunt ruleset

This endpoint creates a new VT Hunting Livehunt ruleset. The request's body must have the following structure:

```json Example request
{
  "data": {
    "type": "hunting_ruleset",
    "attributes": {
      "name": "foobar",
      "enabled": true,
      "limit": 100,
      "rules": "rule foobar { strings: $ = \"foobar\" condition: all of them }",
      "notification_emails": ["wcoyte@acme.com", "rrunner@acme.com"],
      "match_object_type": "file"
    }
  }
}
```

Use the `match_object_type` to specify the expected entity kind to match with this ruleset. Allowed values are `file`, `url`, `domain` and `ip`.

The `name` and `rules` attributes are required, the remaining ones are optional.

```json Example response
{
  "type": "hunting_ruleset",
  "id": "{id}",
  "links": {
    "self": "https://www.virustotal.com/api/v3/intelligence/hunting_ruleset/{id}"
  },
  "data": {
    "attributes": {
      "name": "foobar",
      "enabled": true,
      "limit": 100,
      "creation_date": 1521016318,
      "modification_date": 1521016318,
      "number_of_rules": 1,
      "rules": "rule foobar { strings: $ = \"foobar\" condition: all of them }",
      "notification_emails": ["notifications@acme.com"],
      "match_object_type": "file"
    }
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
    "/intelligence/hunting_rulesets": {
      "post": {
        "summary": "Create a new Livehunt ruleset",
        "description": "",
        "operationId": "create-hunting-ruleset",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A Malware Hunting ruleset",
                    "default": "{     \"type\": \"hunting_ruleset\",     \"attributes\": {       \"name\": \"Test ruleset\",       \"enabled\": true,       \"limit\": 100,       \"rules\": \"rule foobar { strings: $ = \\\"foobar\\\" condition: all of them }\",       \"notification_emails\": [],       \"match_object_type\": \"file\"     }   }",
                    "format": "json"
                  }
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