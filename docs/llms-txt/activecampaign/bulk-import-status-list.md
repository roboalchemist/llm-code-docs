# Source: https://developers.activecampaign.com/reference/bulk-import-status-list.md

# Bulk import status list

> 🧠 Add a short delay between creating a bulk import and calling for it's status
>
> If this endpoint is called *immediately* (less than a second) after a bulk import call, the `status` in the return may be `false` (a boolean), because the system has not yet set a status on the batch.

After using the `POST` endpoint to send bulk data, you can use this endpoint to monitor progress. This endpoint only returns aggregate progress data.  The response is a JSON map of daily summaries of `outstanding` and `recentlyCompleted` batch jobs. Recently completed is a rolling window of the last seven days.

If you want specific details, register for a `callback` when sending the bulk job OR save the `batchId` and use the `info` endpoint.

```json GET /import/bulk_import (Example RESPONSE)
{
  "outstanding":[
    {"forDate":"2021-06-01","batches":"333","contacts":"83250"}
  ],
  "recentlyCompleted":[
    {"forDate":"2021-06-01","batches":"17","contacts":"4250"},
    {"forDate":"2021-06-02","batches":"50","contacts":"12500"}
  ]
}
```

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
    "/import/bulk_import": {
      "get": {
        "summary": "Bulk import status list",
        "description": "",
        "operationId": "bulk-import-status-list",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"outstanding\":[\n    {\"forDate\":\"2021-06-01\",\"batches\":\"333\",\"contacts\":\"83250\"}\n  ],\n  \"recentlyCompleted\":[\n    {\"forDate\":\"2021-06-01\",\"batches\":\"17\",\"contacts\":\"4250\"},\n    {\"forDate\":\"2021-06-02\",\"batches\":\"50\",\"contacts\":\"12500\"}\n  ]\n}"
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