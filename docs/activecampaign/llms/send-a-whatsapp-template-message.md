# Source: https://developers.activecampaign.com/reference/send-a-whatsapp-template-message.md

# Send a WhatsApp Template

Send a single WhatsApp message: select a template to use and call our endpoint with the recipient phone number and the variables the template needs. That's it!

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "WhatsApp API",
    "version": "1.0.0",
    "description": "All of the below API endpoints require API key authentication, get your token at https://app.hilos.io/dev/api-keys.\n\nTo use this token, send with every request an `Authorization: Token <your token>` header.\n\nProduction API server is located at api.hilos.io using HTTPS.\n\nNo versioning info is required for now."
  },
  "paths": {
    "/channel/whatsapp/channels/whatsapp/template/{id}/send": {
      "post": {
        "operationId": "Send a WhatsApp Template Message",
        "description": "Send a single WhatsApp message: select a template to use and call our endpoint with the recipient phone number and the variables the template needs. That's it!",
        "summary": "Send a WhatsApp Template",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "Template Id",
            "required": true,
            "examples": {
              "TheTemplateIdThatWeWantToSend": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "The Template Id that we want to send"
              }
            }
          }
        ],
        "tags": [
          "Templates"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WhatsAppTemplateSend"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/WhatsAppTemplateSend"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/WhatsAppTemplateSend"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "tokenAuth": []
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WhatsAppTemplateSendPublicResponse"
                },
                "examples": {
                  "WhatsAppTemplateSendPublicResponse": {
                    "value": {
                      "id": "a513da3a-8b73-42aa-a938-0eb1e0141533",
                      "conversation": "ee49ab6c-dfd8-4cb6-a512-5880f4385622"
                    },
                    "description": "Returns the Message Id and its Conversation Id."
                  }
                }
              }
            },
            "description": ""
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "WhatsAppTemplateSend": {
        "type": "object",
        "properties": {
          "variables": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "An array of variables to be used in the WhatsApp Template. Variables are taken in order HEADER, BODY and BUTTONs. (e.g. position 0 corresponds to the HEADER (if it exists) or variable {{1}}, position 1 to variable {{2}} and so on."
          },
          "phone": {
            "type": "string",
            "description": "The phone number to send the WhatsApp Template to.",
            "maxLength": 20
          }
        },
        "required": [
          "phone"
        ]
      },
      "WhatsAppTemplateSendPublicResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Message Id"
          },
          "conversation": {
            "type": "string",
            "format": "uuid",
            "description": "Message Conversation Id"
          }
        },
        "required": [
          "conversation",
          "id"
        ]
      }
    },
    "securitySchemes": {
      "tokenAuth": {
        "type": "apiKey",
        "in": "header",
        "name": "Token",
        "description": "Token-based authentication with required prefix \"Token\""
      }
    }
  },
  "x-tagGroups": [
    {
      "name": "Users",
      "tags": [
        "User"
      ]
    },
    {
      "name": "Channels",
      "tags": [
        "WhatsApp",
        "Broadcast"
      ]
    },
    {
      "name": "Flows",
      "tags": [
        "Flow Execution",
        "Flow Execution Contact"
      ]
    },
    {
      "name": "CRM",
      "tags": [
        "Contact",
        "Conversation"
      ]
    },
    {
      "name": "Integrations",
      "tags": [
        "Webhook Subscription"
      ]
    }
  ],
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "description": "Production Server"
    }
  ],
  "tags": [
    {
      "name": "Templates"
    }
  ]
}
```