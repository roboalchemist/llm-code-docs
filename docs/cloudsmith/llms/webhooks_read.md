# Source: https://help.cloudsmith.io/reference/webhooks_read.md

# Views for working with repository webhooks.

Views for working with repository webhooks.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/webhooks/{owner}/{repo}/{identifier}/": {
      "get": {
        "operationId": "webhooks_read",
        "summary": "Views for working with repository webhooks.",
        "description": "Views for working with repository webhooks.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryWebhook"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "webhooks"
        ]
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "repo",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "identifier",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "WebhookTemplate": {
        "required": [
          "event"
        ],
        "type": "object",
        "properties": {
          "event": {
            "title": "Event",
            "type": "string",
            "maxLength": 128,
            "minLength": 1
          },
          "template": {
            "title": "Template",
            "type": "string",
            "maxLength": 4096,
            "nullable": true
          }
        },
        "nullable": true
      },
      "RepositoryWebhook": {
        "required": [
          "events",
          "target_url",
          "templates"
        ],
        "type": "object",
        "properties": {
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "title": "Created by",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "created_by_url": {
            "title": "Created by url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "disable_reason": {
            "title": "Disable reason",
            "type": "integer",
            "enum": [
              0,
              1,
              2,
              3,
              4,
              5,
              6
            ],
            "readOnly": true
          },
          "disable_reason_str": {
            "title": "Disable reason str",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "events": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "*",
                "package.created",
                "package.deleted",
                "package.downloaded",
                "package.failed",
                "package.quarantined",
                "package.released",
                "package.restored",
                "package.security_scanned",
                "package.synced",
                "package.syncing",
                "package.tags_updated"
              ]
            },
            "nullable": true
          },
          "identifier": {
            "title": "Identifier",
            "description": "Deprecated (23-05-15): Please use 'slug_perm' instead. Previously: A monotonically increasing number that identified a webhook request within a repository.",
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "is_active": {
            "title": "Webhook Active",
            "description": "If enabled, the webhook will trigger on subscribed events and send payloads to the configured target URL.",
            "type": "boolean"
          },
          "is_last_response_bad": {
            "title": "Is last response bad",
            "type": "boolean",
            "readOnly": true
          },
          "last_response_status": {
            "title": "Last response status",
            "type": "integer",
            "readOnly": true
          },
          "last_response_status_str": {
            "title": "Last response status str",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "num_sent": {
            "title": "Num sent",
            "type": "integer",
            "readOnly": true
          },
          "package_query": {
            "title": "Package query",
            "description": "The package-based search query for webhooks to fire. This uses the same syntax as the standard search used for repositories, and also supports boolean logic operators such as OR/AND/NOT and parentheses for grouping. If a package does not match, the webhook will not fire.",
            "type": "string",
            "maxLength": 1024,
            "nullable": true
          },
          "request_body_format": {
            "title": "Payload Format",
            "description": "The format of the payloads for webhook requests. Valid options are: (0) JSON, (1) JSON array, (2) form encoded JSON and (3) Handlebars template.",
            "type": "integer",
            "enum": [
              0,
              1,
              2,
              3
            ]
          },
          "request_body_format_str": {
            "title": "Request body format str",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "request_body_template_format": {
            "title": "Payload Template Format",
            "description": "The format of the payloads for webhook requests. Valid options are: (0) Generic/user defined, (1) JSON and (2) XML.",
            "type": "integer",
            "enum": [
              0,
              1,
              2
            ]
          },
          "request_body_template_format_str": {
            "title": "Request body template format str",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "request_content_type": {
            "title": "Content Type Header Value",
            "description": "The value that will be sent for the 'Content Type' header. ",
            "type": "string",
            "maxLength": 128,
            "nullable": true
          },
          "secret_header": {
            "title": "Secret Header",
            "description": "The header to send the predefined secret in. This must be unique from existing headers or it won't be sent. You can use this as a form of authentication on the endpoint side.",
            "type": "string",
            "pattern": "^[-\\w]+$",
            "maxLength": 64,
            "nullable": true
          },
          "self_url": {
            "title": "Self url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "target_url": {
            "title": "Payload URL",
            "description": "The destination URL that webhook payloads will be POST'ed to.",
            "type": "string",
            "format": "uri",
            "maxLength": 2000,
            "minLength": 1
          },
          "templates": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/WebhookTemplate"
            },
            "nullable": true
          },
          "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_by": {
            "title": "Updated by",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "updated_by_url": {
            "title": "Updated by url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "verify_ssl": {
            "title": "Verify SSL Certificates",
            "description": "If enabled, SSL certificates is verified when webhooks are sent. It's recommended to leave this enabled as not verifying the integrity of SSL certificates leaves you susceptible to Man-in-the-Middle (MITM) attacks.",
            "type": "boolean"
          }
        }
      }
    }
  }
}
```