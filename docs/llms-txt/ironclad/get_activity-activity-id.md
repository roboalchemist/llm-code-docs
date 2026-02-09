# Source: https://clickwrap-developer.ironcladapp.com/reference/get_activity-activity-id.md

# Retrieve an Activity

Retrieve a Clickwrap Action by ID.

###📘 Apply Site Settings
Append `?expand=site` as a query parameter to the request to view and apply your site settings.


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
    "/activity/{activity_id}": {
      "get": {
        "description": "Retrieve a Clickwrap Action by ID.\n\n###📘 Apply Site Settings\nAppend `?expand=site` as a query parameter to the request to view and apply your site settings.\n",
        "summary": "Retrieve an Activity",
        "tags": [
          "Activity"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "activity_id",
            "required": true,
            "description": "The ID of the Activity.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "A Clickwrap Action",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "uuid": {
                      "type": "string",
                      "example": "55e0820564a5846a5a0387c4"
                    },
                    "version": {
                      "type": "string",
                      "example": "55dccf164e10cbd8454d7951"
                    },
                    "custom_data": {
                      "type": "object"
                    },
                    "connection_data": {
                      "type": "object",
                      "properties": {
                        "page_title": {
                          "type": "string",
                          "example": "Responsive website template for products"
                        },
                        "page_url": {
                          "type": "string",
                          "example": "http://localhost/demos/ilawnow/signup.html?__ps-agreements=false"
                        },
                        "page_domain": {
                          "type": "string",
                          "example": "localhost:8888"
                        },
                        "page_path": {
                          "type": "string",
                          "example": "/demos/ilawnow/signup.html"
                        },
                        "page_query": {
                          "type": "string",
                          "example": "foo"
                        },
                        "hostname": {
                          "type": "string",
                          "example": "response.pactsafe.com"
                        },
                        "referrer": {
                          "type": "string",
                          "example": "http://localhost:8888/demos/ilawnow/signup.html?__ps-agreements=false"
                        },
                        "browser_timezone": {
                          "type": "string",
                          "example": "4"
                        },
                        "browser_locale": {
                          "type": "string",
                          "example": "en-us"
                        },
                        "user_agent": {
                          "type": "string",
                          "example": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
                        },
                        "device_fingerprint": {
                          "type": "string",
                          "example": "foo"
                        },
                        "operating_system": {
                          "type": "string",
                          "example": "MacOS"
                        },
                        "environment": {
                          "type": "string",
                          "example": "desktop"
                        },
                        "screen_color_depth": {
                          "type": "string",
                          "example": "24-bit"
                        },
                        "screen_resolution": {
                          "type": "string",
                          "example": "1680x1050"
                        },
                        "cookies": {
                          "type": "string",
                          "example": "foo"
                        },
                        "remote_address": {
                          "type": "string",
                          "example": "172.31.43.73"
                        }
                      }
                    },
                    "site": {
                      "readOnly": true,
                      "type": "integer"
                    },
                    "account": {
                      "readOnly": true,
                      "type": "integer"
                    },
                    "signer_id": {
                      "type": "string",
                      "example": "ironclad@example.com"
                    },
                    "group": {
                      "type": "integer"
                    },
                    "contract": {
                      "type": "integer"
                    },
                    "event_type": {
                      "enum": [
                        "agreed",
                        "disagreed",
                        "displayed"
                      ],
                      "title": "EventType",
                      "type": "string"
                    },
                    "batch": {
                      "type": "string",
                      "example": "1442324122234"
                    },
                    "created_time": {
                      "type": "string",
                      "example": "2020-07-21T15:34:30.051Z",
                      "description": "ISO 8601 formatted."
                    },
                    "id": {
                      "readOnly": true,
                      "type": "string",
                      "example": "55f81e9a949601b976734da9"
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