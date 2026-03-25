# Source: https://virustotal.readme.io/reference/user.md

# Get a user object

This endpoint retrieves information about a user, including the privileges and quotas associated to the user. The user can be retrieved either by user ID or by API key, but the former only works if the requester is the user himself or an administrator of a group the user belongs to.

Returns an [User](https://virustotal.readme.io/reference/user-object) object.

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
    "/users/{id}": {
      "get": {
        "summary": "Get a user object",
        "description": "",
        "operationId": "user",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "User ID or API key",
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