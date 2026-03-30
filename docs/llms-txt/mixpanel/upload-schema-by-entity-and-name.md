# Source: https://developer.mixpanel.com/reference/upload-schema-by-entity-and-name.md

# Create/Replace One

Upload a schema for a single entity. If a schema already exists for a specified entity, it will be replaced by the one you upload.

<Callout icon="🚧" theme="warn">
  Metadata merging behavior

  If the new schema is missing `metadata` properties that are currently set in the existing schema for that entity, those properties will be merged into the new schema. For example, if your current schema has `{"metadata": {"com.mixpanel": {"hidden": true}}}` and you upload a new schema without "hidden", we will merge `"hidden": true` to your uploaded schema's metadata. If you want to remove that property, set the value to `null`.
</Callout>

<Callout icon="📘" theme="info">
  Adding a schema for User Profiles

  To add a schema for your [User Profiles](https://help.mixpanel.com/hc/en-us/articles/115004501966-User-Profiles), specify the `entityType` as `profile` and the `name` as `$user`.
</Callout>

### Example POST Body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "description": "Tracked when a user adds an item to their cart.",
    "required": [
        "item_name",
        "item_id",
        "item_price"
    ],
    "additionalProperties": true,
    "metadata": {
        "com.mixpanel": {
            "tags": [
                "Shopping",
                "KPIs"
            ],
            "displayName": "Item Purchased",
            "hidden": false,
            "dropped": false,
            "contacts": [
              "first.last@mixpanel.com"
            ],
            "teamContacts": [
              "Analytics Team"
            ]
        }
    },
    "properties": {
        "item_name": {
            "type": "string",
            "description": "The name of the item",
            "examples": [
                "Blue Widget"
            ],
            "metadata": {
              "com.mixpanel": {
                "displayName": "Item Name"
              }
            }
        },
        "item_id": {
            "type": "integer",
            "description": "The internal id of the item",
            "examples": [
                12345
            ],
            "metadata": {
              "com.mixpanel": {
                "displayName": "Item ID"
              }
            }
        },
        "item_price": {
            "type": "number",
            "description": "The current price of the item",
            "examples": [
                25.35
            ],
            "metadata": {
              "com.mixpanel": {
                "displayName": "Price"
              }
            }
        },
        "promo_id": {
            "type": "integer",
            "description": "The id of any promo in progress for this item",
            "examples": [
                82523,
                18382
            ],
            "metadata": {
              "com.mixpanel": {
                "displayName": "Promo ID"
              }
            }
        },
        "date_added_to_catalog": {
            "type": "string",
            "format": "date-time",
            "description": "The date this item was added to the store catalog",
            "examples": [
                "2015-03-05T15:25:23"
            ],
            "metadata": {
              "com.mixpanel": {
                "displayName": "Date Added"
              }
            }
        }
    }
}
```

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
      "name": "Create Schemas",
      "description": "Operations to add schemas to a project"
    }
  ],
  "paths": {
    "/projects/{projectId}/schemas/{entityType}/{name}": {
      "parameters": [
        {
          "$ref": "#/components/parameters/projectId"
        },
        {
          "$ref": "#/components/parameters/schemaEntityType"
        },
        {
          "$ref": "#/components/parameters/schemaEntityName"
        }
      ],
      "post": {
        "operationId": "upload-schema-by-entity-and-name",
        "summary": "Create/Replace One",
        "tags": [
          "Create Schemas"
        ],
        "description": "",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Schema"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UploadSchemasResponse"
                }
              }
            }
          },
          "400": {
            "$ref": "#/components/responses/400BadRequest"
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
      "UploadSchemasResponse": {
        "type": "object",
        "properties": {
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
      },
      "400BadRequest": {
        "description": "Bad request",
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