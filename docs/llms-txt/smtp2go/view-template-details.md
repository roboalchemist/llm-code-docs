# Source: https://developers.smtp2go.com/reference/view-template-details.md

# View template details

Returns details of the email template with the specified ID.

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
      "name": "TEMPLATES"
    }
  ],
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/template/view": {
      "post": {
        "tags": [
          "TEMPLATES"
        ],
        "summary": "View template details",
        "description": "Returns details of the email template with the specified ID.",
        "operationId": "view-template-details",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "id"
                ],
                "properties": {
                  "id": {
                    "type": "string",
                    "description": "The case-sensitive ID of the email template that you wish to view"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Details of a template",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "b0107930-6410-11ed-b1a0-f23c9216bf47",
                      "data": {
                        "name": "Shiny new name",
                        "id": "testid",
                        "subject": "Shiny new Subject",
                        "tags": [
                          "tag1",
                          "tag2"
                        ],
                        "html_body": "",
                        "text_body": "",
                        "template_variables": {
                          "variable": "strawberries"
                        },
                        "last_updated": "2024-01-01 12:00:00"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "f00c0856-dde8-11eb-b4ce-1002b51e60a4"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "html_body",
                        "id",
                        "subject",
                        "tags",
                        "name",
                        "template_variables",
                        "text_body"
                      ],
                      "properties": {
                        "html_body": {
                          "type": "string",
                          "example": "Shiny HTML body. This is a {{ variable }}"
                        },
                        "id": {
                          "type": "string",
                          "example": "testid"
                        },
                        "subject": {
                          "type": "string",
                          "example": "Shiny new Subject"
                        },
                        "tags": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "tagged"
                          }
                        },
                        "name": {
                          "type": "string",
                          "example": "Shiny new name"
                        },
                        "template_variables": {
                          "type": "object",
                          "description": "The pass-through values required by the template in the format `{\"variable1\": \"value1\", \"variable2\": \"value2\"}`"
                        },
                        "text_body": {
                          "type": "string",
                          "example": "Shiny Text body"
                        },
                        "last_updated": {
                          "type": "string",
                          "example": "2024-01-01 12:00:00",
                          "description": "A timestamp indicating when this template was last updated"
                        }
                      }
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