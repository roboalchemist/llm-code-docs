# Source: https://developers.activecampaign.com/reference/create-a-task-reminder.md

# Create a task reminder

Create a new task reminder

<br />

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
    "/taskNotifications": {
      "post": {
        "summary": "Create a task reminder",
        "description": "Create a new task reminder",
        "operationId": "create-a-task-reminder",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "dealTask",
                  "interval"
                ],
                "properties": {
                  "dealTask": {
                    "type": "string",
                    "description": "ID of task"
                  },
                  "interval": {
                    "type": "integer",
                    "description": "Amount of time in minutes that a reminder will be sent to a task assignee ahead of task's due date.",
                    "format": "int32"
                  }
                }
              },
              "examples": {
                "Request Example": {
                  "value": {
                    "taskNotification": {
                      "dealTask": "1",
                      "interval": "123"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            }
          },
          "422": {
            "description": "422",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
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