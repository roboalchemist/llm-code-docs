# Source: https://developers.smtp2go.com/reference/add-an-email-template.md

# Add an email template

Adds a new email template that you can use to format your emails.

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
    "/template/add": {
      "post": {
        "tags": [
          "TEMPLATES"
        ],
        "summary": "Add an email template",
        "description": "Adds a new email template that you can use to format your emails.",
        "operationId": "add-an-email-template",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "template_name",
                  "id",
                  "subject",
                  "html_body",
                  "text_body"
                ],
                "properties": {
                  "template_name": {
                    "type": "string",
                    "description": "The name of the email template. Min length: 1 Character. Max length: 64 Characters."
                  },
                  "id": {
                    "type": "string",
                    "description": "The case-sensitive ID of the email template. Min length: 5 Character. Max length: 24 Characters."
                  },
                  "subject": {
                    "type": "string",
                    "description": "The subject of the email template."
                  },
                  "html_body": {
                    "type": "string",
                    "description": "The HTML body of the email template."
                  },
                  "text_body": {
                    "type": "string",
                    "description": "The Plain Text body of the email template."
                  },
                  "template_variables": {
                    "type": "object",
                    "description": "The variables to use within this email template in the format `{\"variable1\": \"value1\", \"variable2\": \"value2\"}`"
                  },
                  "tags": {
                    "type": "array",
                    "description": "The list of Tags to associate to this email template",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Template added",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "f00c0856-dde8-11eb-b4ce-1002b51e60a4",
                      "data": {
                        "template_name": "Shiny new name",
                        "id": "testid",
                        "subject": "Shiny new Subject",
                        "html_body": "Shiny HTML body. This is a {{ variable }}",
                        "text_body": "Shiny Text body",
                        "template_variables": {
                          "variable": "strawberries"
                        },
                        "tags": [
                          "tagged"
                        ]
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
                        "id",
                        "subject",
                        "tags"
                      ],
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "5355878"
                        },
                        "name": {
                          "type": "string",
                          "example": "Order receipt",
                          "description": "This parameter is only returned in 'search' response"
                        },
                        "template_name": {
                          "type": "string",
                          "example": "Order receipt",
                          "description": "This parameter is not present in 'search' response"
                        },
                        "subject": {
                          "type": "string",
                          "example": "Order receipt for {{ product_name }}"
                        },
                        "tags": {
                          "type": "array",
                          "required": [
                            "types",
                            "example"
                          ],
                          "items": {
                            "type": "string",
                            "example": "one"
                          }
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