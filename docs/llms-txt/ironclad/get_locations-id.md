# Source: https://clickwrap-developer.ironcladapp.com/reference/get_locations-id.md

# Get a Snapshot location.

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
  "tags": [
    {
      "name": "Snapshots"
    }
  ],
  "paths": {
    "/locations/{id}": {
      "get": {
        "summary": "Get a Snapshot location.",
        "tags": [
          "Snapshots"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "A Snapshot location.",
            "content": {
              "application/json": {
                "schema": {
                  "properties": {
                    "data": {
                      "oneOf": [
                        {
                          "required": [
                            "platform",
                            "frequency",
                            "published",
                            "published_time",
                            "status",
                            "location_type",
                            "key",
                            "name",
                            "capture_url",
                            "created_time",
                            "updated_time",
                            "created_by",
                            "updated_by",
                            "site",
                            "account",
                            "id"
                          ],
                          "title": "WebLocationResponse",
                          "allOf": [
                            {
                              "properties": {
                                "account": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "archived": {
                                  "readOnly": true,
                                  "type": "boolean"
                                },
                                "archived_reason": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "created_by": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "created_time": {
                                  "description": "ISO 8601 formatted.",
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "description": {
                                  "type": "string"
                                },
                                "id": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "key": {
                                  "type": "string"
                                },
                                "last_acceptance": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "name": {
                                  "type": "string"
                                },
                                "published": {
                                  "readOnly": true,
                                  "type": "boolean"
                                },
                                "published_by": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "published_time": {
                                  "description": "ISO 8601 formatted.",
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "site": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "status": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "updated_by": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "updated_time": {
                                  "description": "ISO 8601 formatted.",
                                  "readOnly": true,
                                  "type": "string"
                                }
                              },
                              "title": "Location",
                              "type": "object"
                            }
                          ],
                          "properties": {
                            "capture_attempts": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "capture_url": {
                              "type": "string"
                            },
                            "error_message": {
                              "type": "string",
                              "readOnly": true
                            },
                            "frequency": {
                              "enum": [
                                "daily",
                                "weekly",
                                "monthly",
                                "never"
                              ],
                              "title": "Frequency",
                              "type": "string"
                            },
                            "location_type": {
                              "enum": [
                                "web"
                              ],
                              "title": "LocationTypeWeb",
                              "type": "string"
                            },
                            "platform": {
                              "enum": [
                                "desktop",
                                "ios",
                                "android"
                              ],
                              "title": "Platforms",
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        {
                          "required": [
                            "mobile_os",
                            "published",
                            "published_time",
                            "status",
                            "location_type",
                            "key",
                            "name",
                            "application_id",
                            "application_name",
                            "created_by",
                            "updated_by",
                            "site",
                            "account",
                            "created_time",
                            "updated_time",
                            "id"
                          ],
                          "title": "MobileLocationResponse",
                          "allOf": [
                            {
                              "properties": {
                                "account": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "archived": {
                                  "readOnly": true,
                                  "type": "boolean"
                                },
                                "archived_reason": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "created_by": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "created_time": {
                                  "description": "ISO 8601 formatted.",
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "description": {
                                  "type": "string"
                                },
                                "id": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "key": {
                                  "type": "string"
                                },
                                "last_acceptance": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "name": {
                                  "type": "string"
                                },
                                "published": {
                                  "readOnly": true,
                                  "type": "boolean"
                                },
                                "published_by": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "published_time": {
                                  "description": "ISO 8601 formatted.",
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "site": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "status": {
                                  "readOnly": true,
                                  "type": "string"
                                },
                                "updated_by": {
                                  "readOnly": true,
                                  "type": "integer"
                                },
                                "updated_time": {
                                  "description": "ISO 8601 formatted.",
                                  "readOnly": true,
                                  "type": "string"
                                }
                              },
                              "title": "Location",
                              "type": "object"
                            },
                            {
                              "properties": {
                                "application_id": {
                                  "type": "string"
                                },
                                "application_name": {
                                  "type": "string"
                                },
                                "mobile_os": {
                                  "description": "Default 'ios'",
                                  "enum": [
                                    "ios",
                                    "android"
                                  ],
                                  "title": "Mobile OS",
                                  "type": "string"
                                }
                              }
                            },
                            {
                              "properties": {
                                "location_type": {
                                  "enum": [
                                    "mobile_app"
                                  ],
                                  "title": "LocationTypeMobile",
                                  "type": "string"
                                }
                              }
                            }
                          ],
                          "type": "object"
                        }
                      ],
                      "type": "object"
                    }
                  },
                  "type": "object"
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
          "403": {
            "description": "Forbidden."
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