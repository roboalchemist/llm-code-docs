# Source: https://developers.activecampaign.com/reference/delete-variable.md

# Delete a Variable

Delete a personalization variable

> 📘 Duplicate personalization variables will have a `_X`number appended to the tag
>
> If a personalization is created with this json body:
>
> ```json
> {
>     "personalization": {
>         "tag": "brand new tag",
>         "name": "brand new name",
>         "format": "text",
>         "content": "Hello World!",
>         "listids": "2,3,4,5"
>     }
> }
> ```
>
> ... but the tag `brand new tag`already exists, the API response below shows how a personalization variable will be created, but will have a underscore and a number appended to the `tag`end:
>
> ```json
> {
>     "personalization": {
>         "tag": "brand-new-tag_1",
>         "name": "brand new name",
>         "format": "text",
>         "content": "Hello World!",
>         "listids": "2,3,4,5",
>         "userid": "1",
>         "links": [],
>         "id": "12"
>     }
> }
> ```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/personalizations/{variableID}": {
      "delete": {
        "summary": "Delete a Variable",
        "description": "Delete a personalization variable",
        "operationId": "delete-variable",
        "parameters": [
          {
            "name": "variableID",
            "in": "path",
            "description": "ID (int) of personalization/variable",
            "schema": {
              "type": "integer",
              "format": "int32"
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
                    "value": "{\n    \"message\": \"No Result found for Personalization with id 22\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "No Result found for Personalization with id 22"
                    }
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
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```