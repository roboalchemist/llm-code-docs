# Source: https://developers.smtp2go.com/reference/sms-summary.md

# SMS Summary

Retrieve a summary of SMS messages within a certain time range.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "SMTP2GO API v3.0.3",
    "version": "3.0.3"
  },
  "servers": [
    {
      "url": "https://api.smtp2go.com/v3",
      "description": "Regionless"
    },
    {
      "url": "https://us-api.smtp2go.com/v3",
      "description": "US Region"
    },
    {
      "url": "https://eu-api.smtp2go.com/v3",
      "description": "EU Region"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "X-Smtp2go-Api-Key",
        "x-default": ""
      }
    }
  },
  "tags": [
    {
      "name": "SMS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/sms/summary": {
      "post": {
        "tags": [
          "SMS"
        ],
        "summary": "SMS Summary",
        "description": "Retrieve a summary of SMS messages within a certain time range.",
        "operationId": "sms-summary",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults to current date at midnight. The range will be inclusive of start_date and exclusive of end_date. Timezone is UTC.",
                    "format": "date"
                  },
                  "end_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime which defaults to now. Timezone is UTC.",
                    "format": "date"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Summary of SMS activity",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "data": {
                        "total_messages": 123,
                        "total_units": 156,
                        "total_cost": 10.456
                      },
                      "request_id": "4b661d88-6b2d-11eb-8bb3-f23c92bb31d2"
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "required": [
                    "data",
                    "request_id"
                  ],
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "total_messages": {
                          "type": "integer",
                          "example": 123,
                          "description": "The total number of SMS messages sent within the passed time range"
                        },
                        "total_units": {
                          "type": "integer",
                          "example": 156,
                          "description": "The total number of SMS units used to send the messages within the passed time range"
                        },
                        "total_cost": {
                          "type": "number",
                          "example": 10.456,
                          "description": "The total cost of the SMS messages within the passed time range"
                        }
                      }
                    },
                    "request_id": {
                      "type": "string",
                      "example": "4b661d88-6b2d-11eb-8bb3-f23c92bb31d2"
                    }
                  }
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
                    "value": {
                      "request_id": "22e5acba-43bf-11e6-ae42-408d5cce2644",
                      "data": {
                        "error": "You do not have permission to access this API endpoint",
                        "error_code": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "22e5acba-43bf-11e6-ae42-408d5cce2644"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "error": {
                          "type": "string",
                          "example": "You do not have permission to access this API endpoint"
                        },
                        "error_code": {
                          "type": "string",
                          "example": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                        }
                      }
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
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "explorer-enabled": true,
    "proxy-enabled": true,
    "samples-enabled": true
  }
}
```