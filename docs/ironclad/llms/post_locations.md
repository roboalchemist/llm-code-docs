# Source: https://clickwrap-developer.ironcladapp.com/reference/post_locations.md

# Create a new Snapshot location

Requires **manage** permissions for Snapshots. A Snapshot Location can be either a `Mobile` or `Web` location depending on the `location_type` body parameter

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
    "/locations": {
      "post": {
        "description": "Requires **manage** permissions for Snapshots. A Snapshot Location can be either a `Mobile` or `Web` location depending on the `location_type` body parameter",
        "summary": "Create a new Snapshot location",
        "tags": [
          "Snapshots"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "oneOf": [
                  {
                    "required": [
                      "capture_url",
                      "location_type",
                      "key",
                      "name"
                    ],
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
                    "title": "WebLocation",
                    "type": "object"
                  },
                  {
                    "required": [
                      "key",
                      "name",
                      "application_id",
                      "application_name",
                      "location_type"
                    ],
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
                    "title": "MobileLocation",
                    "type": "object"
                  }
                ]
              },
              "examples": {
                "web": {
                  "summary": "Web Snapshot location.",
                  "value": {
                    "name": "example location",
                    "key": "example-key",
                    "capture_url": "https://example.com",
                    "description": "Example app login.",
                    "platform": "desktop",
                    "frequency": "weekly"
                  }
                },
                "mobile": {
                  "summary": "Mobile app Snapshot location.",
                  "value": {
                    "name": "example location",
                    "key": "example-key",
                    "description": "Example app login.",
                    "application_id": "example.app",
                    "application_name": "Example App",
                    "mobile_os": "ios"
                  }
                }
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "description": "Created.",
            "content": {
              "application/json": {
                "schema": {
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
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Bad request."
          },
          "403": {
            "description": "Forbidden."
          },
          "409": {
            "description": "Already exists."
          },
          "422": {
            "description": "Unprocessable."
          }
        }
      }
    }
  }
}
```