# Source: https://developer.mixpanel.com/reference/list-all-schemas-for-project.md

# List Schemas

List all schemas in a project

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Lexicon Schemas API",
    "description": "Use schemas to sync your data dictionary with Mixpanel. Schemas can be used to populate Lexicon and provide additional context for your data.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com/api/app",
      "description": "Mixpanel's application API server.",
      "variables": {
        "regionAndDomain": {
          "default": "mixpanel",
          "enum": [
            "mixpanel",
            "eu.mixpanel",
            "in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `mixpanel` - The default (US) servers used for most projects\n  * `eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "ServiceAccount": []
    }
  ],
  "tags": [
    {
      "name": "Retrieve Schemas",
      "description": "Get additional information about schemas"
    }
  ],
  "paths": {
    "/projects/{projectId}/schemas": {
      "parameters": [
        {
          "$ref": "#/components/parameters/projectId"
        }
      ],
      "get": {
        "operationId": "list-all-schemas-for-project",
        "tags": [
          "Retrieve Schemas"
        ],
        "summary": "List Schemas",
        "description": "List all schemas in a project",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListSchemasResponse"
                }
              }
            }
          },
          "401": {
            "$ref": "#/components/responses/401Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/403Forbidden"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      }
    },
    "schemas": {
      "SchemaEntityType": {
        "type": "string",
        "enum": [
          "event",
          "profile"
        ]
      },
      "Schema": {
        "type": "object",
        "description": "The schema for the entity",
        "properties": {
          "description": {
            "type": "string",
            "description": "The entity description"
          },
          "properties": {
            "type": "object",
            "description": "The list of properties that should be included on an instance of this entity",
            "additionalProperties": {
              "type": "object",
              "description": "The name and definition for a property. E.g. \"item_id\"",
              "required": [
                "type"
              ],
              "properties": {
                "type": {
                  "enum": [
                    "array",
                    "boolean",
                    "integer",
                    "null",
                    "number",
                    "object",
                    "string"
                  ]
                },
                "description": {
                  "type": "string",
                  "description": "The property description"
                },
                "metadata": {
                  "type": "object",
                  "properties": {
                    "com.mixpanel": {
                      "type": "object",
                      "description": "Metadata that is specific to Mixpanel",
                      "properties": {
                        "displayName": {
                          "type": "string",
                          "description": "If set, this name will be used in the Mixpanel UI instead of the entity name"
                        },
                        "hidden": {
                          "type": "boolean",
                          "description": "If true, this property will be hidden in the Mixpanel UI",
                          "default": false
                        },
                        "dropped": {
                          "type": "boolean",
                          "description": "[Events only] If true, the property will be dropped at ingestion time.",
                          "default": false
                        }
                      },
                      "additionalProperties": false
                    }
                  }
                }
              },
              "additionalProperties": false
            }
          },
          "metadata": {
            "type": "object",
            "properties": {
              "com.mixpanel": {
                "type": "object",
                "description": "Metadata about this entity that is specific to Mixpanel",
                "properties": {
                  "$source": {
                    "type": "string",
                    "description": "The source of this schema. Used by partners to identify themselves"
                  },
                  "displayName": {
                    "type": "string",
                    "description": "If set, this name will be used in the Mixpanel UI instead of the entity name"
                  },
                  "tags": {
                    "type": "array",
                    "description": "A list of tags to associate to this entity that can be used in the Mixpanel UI for filtering",
                    "items": {
                      "type": "string"
                    }
                  },
                  "hidden": {
                    "type": "boolean",
                    "description": "If true, this entity will be hidden in the Mixpanel UI",
                    "default": false
                  },
                  "dropped": {
                    "type": "boolean",
                    "description": "[Events only] If true, the event will be dropped at ingestion time.",
                    "default": false
                  },
                  "contacts": {
                    "type": "array",
                    "description": "A list of emails belonging to users responsible for this entity.",
                    "items": {
                      "type": "string",
                      "additionalProperties": false
                    }
                  },
                  "teamContacts": {
                    "type": "array",
                    "description": "A list of team names responsible for this entity.",
                    "items": {
                      "type": "string"
                    }
                  }
                },
                "additionalProperties": false
              }
            }
          }
        }
      },
      "SchemaEntry": {
        "type": "object",
        "properties": {
          "entityType": {
            "$ref": "#/components/schemas/SchemaEntityType"
          },
          "name": {
            "type": "string",
            "description": "The entity name (eg: Added To Cart)"
          },
          "schemaJson": {
            "$ref": "#/components/schemas/Schema"
          }
        },
        "required": [
          "name",
          "entityType",
          "schemaJson"
        ],
        "additionalProperties": false
      },
      "ListSchemasResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SchemaEntry"
            }
          },
          "status": {
            "type": "string",
            "enum": [
              "ok"
            ]
          }
        }
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Details about the error that occurred"
          },
          "status": {
            "type": "string",
            "enum": [
              "error"
            ]
          }
        }
      }
    },
    "responses": {
      "401Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "403Forbidden": {
        "description": "Forbidden",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      }
    }
  },
  "x-explorer-enabled": true,
  "x-proxy-enabled": true,
  "x-samples-enabled": true,
  "x-samples-languages": [
    "curl",
    "node",
    "ruby",
    "javascript",
    "python"
  ]
}
```