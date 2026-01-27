# Source: https://clickwrap-developer.ironcladapp.com/reference/delete_versions-version-id-fields-field-id.md

# Delete Field on a Version

Delete Field on a Version by Version ID

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "contact": {
      "email": "support@ironcladapp.com",
      "name": "Ironclad Support"
    },
    "title": "REST API",
    "version": "v1.1"
  },
  "security": [
    {
      "Bearer": []
    }
  ],
  "servers": [
    {
      "description": "Ironclad Clickwrap REST API",
      "url": "https://api.pactsafe.com/v1.1"
    }
  ],
  "components": {
    "securitySchemes": {
      "Bearer": {
        "scheme": "bearer",
        "type": "http"
      }
    }
  },
  "paths": {
    "/versions/{version_id}/fields/{field_id}": {
      "delete": {
        "summary": "Delete Field on a Version",
        "tags": [
          "Versions"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "version_id",
            "description": "The unique ID of the Contract Version.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "field_id",
            "description": "The unique ID of the Field on the Version.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Deleted Field",
            "content": {
              "application/json": {
                "schema": {
                  "title": "FormField",
                  "type": "object",
                  "required": [
                    "name",
                    "type",
                    "assignment_value"
                  ],
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "5e8c6ecc51289e1e22816d6c",
                      "readOnly": true
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of the field."
                    },
                    "label": {
                      "type": "string",
                      "description": "The label of the field."
                    },
                    "type": {
                      "title": "FormFieldType",
                      "description": "The type of field.",
                      "type": "string",
                      "enum": [
                        "text",
                        "checkbox",
                        "date",
                        "signature",
                        "dropdown",
                        "attachment",
                        "acceptance_date",
                        "initials"
                      ]
                    },
                    "required": {
                      "type": "boolean",
                      "description": "Whether the field is required to be filled prior to acceptance."
                    },
                    "input_value": {
                      "type": "string",
                      "readOnly": true
                    },
                    "options": {
                      "type": "string",
                      "readOnly": true
                    },
                    "locations": {
                      "type": "array",
                      "readOnly": true,
                      "items": {
                        "type": "object"
                      }
                    },
                    "assigned_to": {
                      "type": "string",
                      "readOnly": true
                    },
                    "complete": {
                      "type": "boolean",
                      "readOnly": true
                    },
                    "completed_time": {
                      "type": "string",
                      "example": "2020-07-21T15:34:30.051Z",
                      "description": "ISO 8601 formatted.",
                      "readOnly": true
                    },
                    "completed_value": {
                      "type": "string",
                      "readOnly": true
                    },
                    "default_value": {
                      "type": "string",
                      "description": "A default value that can be applied to the field."
                    },
                    "assignment_value": {
                      "title": "FormFieldAssignmentType",
                      "description": "Whether the field is assigned to the Sender or the Signer.",
                      "type": "string",
                      "enum": [
                        "signer",
                        "sender"
                      ]
                    },
                    "read_only": {
                      "type": "boolean",
                      "description": "Whether field field can be changed or not. This is typically only used in scenarios where the field has a default value."
                    },
                    "secure": {
                      "type": "boolean",
                      "readOnly": true
                    },
                    "secure_value": {
                      "type": "string",
                      "readOnly": true
                    },
                    "locked": {
                      "type": "boolean",
                      "readOnly": true
                    },
                    "persona": {
                      "description": "The Signer Role to use when creating the field.",
                      "type": "string"
                    },
                    "is_trigger": {
                      "type": "boolean"
                    },
                    "trigger_field": {
                      "type": "string",
                      "example": "5e8c6ecc51289e1e22816d6c"
                    },
                    "trigger_match_value": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad request."
          },
          "401": {
            "description": "The requester is unauthorized."
          },
          "404": {
            "description": "Not found."
          }
        }
      }
    }
  }
}
```