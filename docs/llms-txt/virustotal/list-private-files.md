# Source: https://virustotal.readme.io/reference/list-private-files.md

# List private files

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Returns a list of previously analysed [private files](https://virustotal.readme.io/reference/private-files). The files are always ordered by SHA256.

```json /api/v3/private/files
{
  "meta": {
    "cursor": <string>,
    "count": <int>
  },
  "data": {
    <PRIVATE_FILE_OBJECT>,
    <PRIVATE_FILE_OBJECT>,
    ...
  },
  "links": {
    "self": <string>,
    "next": <string>
  }
}
```
```json
{
	"meta": {
		"cursor": "079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678",
		"count": 19
	},
	"data": [
		{
			"attributes": {
				"type_description": "Windows Installer",
        ...
      },
      "type": "private_file",
      "id": "079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678",
      "links": {
        "self": "https://www.virustotal.com/api/v3/private/files/079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678"
      }
    },
    ...
  ],
  "links": {
		"self": "https://www.virustotal.com/api/v3/private/files?limit=1",
		"next": "https://www.virustotal.com/api/v3/private/files?cursor=079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678&limit=1"
	}
}
```

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
    "/files": {
      "get": {
        "summary": "List private files",
        "description": "",
        "operationId": "list-private-files",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of files to retrieve (40 max)",
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