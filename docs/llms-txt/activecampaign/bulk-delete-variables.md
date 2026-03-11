# Source: https://developers.activecampaign.com/reference/bulk-delete-variables.md

# Bulk Delete Variables

Bulk delete personalization variables

> 📘 Variables that do not exist will not block bulk delete
>
> A http DELETE to `personalizations/bulkdelete?ids=11,12,13`will still delete the variables with ids `11` and `12` even if a variables with id `13` does not exist.
>
> This endpoint will always return "Delete successful" even if *none* of the variable ids provided actually exist.

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
    "/personalizations/bulkdelete": {
      "delete": {
        "summary": "Bulk Delete Variables",
        "description": "Bulk delete personalization variables",
        "operationId": "bulk-delete-variables",
        "parameters": [
          {
            "name": "ids",
            "in": "query",
            "description": "List of variables to be deleted, ie: 1,2,3",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": "Delete successful"
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