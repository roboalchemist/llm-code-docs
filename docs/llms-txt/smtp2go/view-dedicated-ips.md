# Source: https://developers.smtp2go.com/reference/view-dedicated-ips.md

# View Dedicated IP Addresses

Retrieve a list of Dedicated IP addresses on this account

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
      "name": "DEDICATED IPS"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/dedicated_ips/view": {
      "post": {
        "tags": [
          "DEDICATED IPS"
        ],
        "summary": "View Dedicated IP Addresses",
        "description": "Retrieve a list of Dedicated IP addresses on this account",
        "operationId": "view-dedicated-ips",
        "responses": {
          "200": {
            "description": "Successfully retrieved Dedicated IP addresses",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "f3e50113-deb2-4e54-9675-2ea497c3732e",
                      "data": [
                        {
                          "id": 1234,
                          "name": "Main Pool",
                          "ip_addresses": [
                            "127.0.0.1"
                          ]
                        }
                      ]
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
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "description": "The id of the pool",
                            "example": "1234"
                          },
                          "name": {
                            "type": "string",
                            "description": "The name of the pool",
                            "example": "Main Pool"
                          },
                          "ip_addresses": {
                            "type": "array",
                            "description": "A list of dedicated IP addresses assigned to this pool",
                            "items": {
                              "description": "A dedicated IP address",
                              "example": "127.0.0.1"
                            }
                          }
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