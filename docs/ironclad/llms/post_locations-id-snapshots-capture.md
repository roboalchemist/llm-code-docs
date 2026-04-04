# Source: https://clickwrap-developer.ironcladapp.com/reference/post_locations-id-snapshots-capture.md

# Trigger a Snapshot capture.

Requires **upload** or **manage** permissions.

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
    "/locations/{id}/snapshots/capture": {
      "post": {
        "tags": [
          "Snapshots"
        ],
        "summary": "Trigger a Snapshot capture.",
        "description": "Requires **upload** or **manage** permissions.",
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
            "description": "Success.",
            "content": {
              "application/json": {
                "schema": {
                  "properties": {
                    "data": {
                      "title": "Snapshot",
                      "type": "object",
                      "properties": {
                        "account": {
                          "readOnly": true,
                          "type": "integer"
                        },
                        "archived": {
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "archived_by": {
                          "readOnly": true,
                          "type": "integer"
                        },
                        "archived_reason": {
                          "type": "string"
                        },
                        "captured_time": {
                          "description": "ISO 8601 formatted.",
                          "type": "string"
                        },
                        "created_time": {
                          "description": "ISO 8601 formatted.",
                          "readOnly": true,
                          "type": "string"
                        },
                        "expiration_time": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "id": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "image_path": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "is_manual": {
                          "readOnly": true,
                          "type": "boolean"
                        },
                        "is_test": {
                          "type": "boolean"
                        },
                        "metadata": {
                          "oneOf": [
                            {
                              "type": "object",
                              "title": "SnapshotWebMetadata",
                              "properties": {
                                "captured_time": {
                                  "description": "ISO 8601 formatted.",
                                  "type": "string"
                                },
                                "page_url": {
                                  "type": "string"
                                },
                                "selector": {
                                  "type": "string"
                                },
                                "useragent": {
                                  "properties": {
                                    "browser": {
                                      "properties": {
                                        "major": {
                                          "type": "string"
                                        },
                                        "name": {
                                          "type": "string"
                                        }
                                      },
                                      "type": "object"
                                    },
                                    "os": {
                                      "properties": {
                                        "name": {
                                          "type": "string"
                                        },
                                        "version": {
                                          "type": "string"
                                        }
                                      },
                                      "type": "object"
                                    }
                                  },
                                  "type": "object"
                                },
                                "viewport": {
                                  "properties": {
                                    "height": {
                                      "type": "integer"
                                    },
                                    "width": {
                                      "type": "integer"
                                    }
                                  },
                                  "type": "object"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "title": "SnapshotMobileMetadata",
                              "properties": {
                                "app_name": {
                                  "type": "string"
                                },
                                "app_version": {
                                  "type": "string"
                                },
                                "captured_time": {
                                  "type": "string",
                                  "description": "ISO 8601 formatted."
                                },
                                "device_model": {
                                  "type": "string"
                                },
                                "device_os": {
                                  "type": "string"
                                },
                                "resolution": {
                                  "type": "string"
                                }
                              }
                            }
                          ],
                          "type": "object"
                        },
                        "site": {
                          "readOnly": true,
                          "type": "integer"
                        },
                        "snapshot_download_url": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "snapshot_location": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "source": {
                          "readOnly": true,
                          "enum": [
                            "triggered",
                            "automated",
                            "customer_provided"
                          ],
                          "type": "string"
                        },
                        "status": {
                          "readOnly": true,
                          "enum": [
                            "processing",
                            "success",
                            "failure"
                          ],
                          "type": "string"
                        },
                        "status_message": {
                          "readOnly": true,
                          "type": "string"
                        },
                        "updated_time": {
                          "description": "ISO 8601 formatted.",
                          "readOnly": true,
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "status",
                        "snapshot_location",
                        "account",
                        "site",
                        "is_manual",
                        "is_test",
                        "source",
                        "created_time",
                        "updated_time"
                      ]
                    }
                  }
                }
              }
            }
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