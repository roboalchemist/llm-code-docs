# Source: https://developer.mixpanel.com/reference/identity-merge.md

# Merge Identities

<Callout icon="📘" theme="info">
  The `$merge` event payload is only useful for projects using the Original ID Merge system; it has no functionality in other ID management systems. Please review [this section of our documentation](https://docs.mixpanel.com/docs/tracking-methods/id-management#identity-merge-apis) for more information.
</Callout>

<Callout icon="❗️" theme="error">
  Merging identities is irreversible

  `$merge` is a very powerful tool, so we will only accept `$merge` events that are sent via `https://api.mixpanel.com/import`, which is protected by the project api secret. You **cannot** unmerge `distinct_id`.
</Callout>

**Merge Criteria:**

<Image alt="960" border={false} src="https://files.readme.io/be66940-merge_.png" title="Identity Management - Merge" />

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Identity API",
    "description": "APIs to identify anonymous user IDs to their canonical user ID.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "1.0.0",
    "contact": {
      "url": "https://mixpanel.com/get-support"
    }
  },
  "servers": [
    {
      "url": "https://{region}.mixpanel.com",
      "description": "Mixpanel's data collection server.",
      "variables": {
        "region": {
          "default": "api",
          "enum": [
            "api",
            "api-eu",
            "api-in"
          ],
          "description": "The server location to be used:\n  * `api` - The default (US) servers used for most projects\n  * `api-eu` - EU servers if you are enrolled in EU Data Residency\n  * `api-in` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Identities",
      "description": "Register or merge users with a new identity."
    }
  ],
  "paths": {
    "/import": {
      "post": {
        "tags": [
          "Identities"
        ],
        "summary": "Merge Identities",
        "operationId": "identity-merge",
        "description": "",
        "security": [
          {
            "ServiceAccount": []
          },
          {
            "ProjectSecret": []
          },
          {
            "OAuthToken": []
          }
        ],
        "parameters": [
          {
            "in": "query",
            "name": "strict",
            "required": true,
            "schema": {
              "type": "string",
              "default": "1",
              "enum": [
                "0",
                "1"
              ]
            },
            "description": "When set to 1 (recommended), Mixpanel will validate the batch and return errors per event that failed."
          },
          {
            "in": "query",
            "name": "project_id",
            "required": false,
            "schema": {
              "type": "string"
            },
            "description": "The Mixpanel project_id, used to authenticate service account credentials (do not provide if using secret auth)."
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "event",
                    "properties"
                  ],
                  "properties": {
                    "event": {
                      "type": "string",
                      "title": "event",
                      "description": "This is the name of the event. If you're loading data from a data warehouse, we recommend using the name of the table as the name of the event.",
                      "default": "$merge"
                    },
                    "properties": {
                      "type": "object",
                      "title": "properties",
                      "required": [
                        "$distinct_ids",
                        "token"
                      ],
                      "properties": {
                        "$distinct_ids": {
                          "type": "array",
                          "minItems": 2,
                          "maxItems": 2,
                          "items": {
                            "type": "string"
                          },
                          "description": "The two distinct_ids to merge together."
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/StrictReceived"
          },
          "400": {
            "$ref": "#/components/responses/StrictInvalid"
          },
          "401": {
            "$ref": "#/components/responses/StrictUnauthorized"
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
      },
      "ProjectSecret": {
        "type": "http",
        "scheme": "basic",
        "description": "Project Secret"
      },
      "OAuthToken": {
        "type": "http",
        "scheme": "bearer",
        "description": "OAuth Token"
      }
    },
    "responses": {
      "StrictReceived": {
        "description": "A 200 response indicates all events were successfully ingested.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "num_records_imported": {
                  "type": "integer"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 200,
                "num_records_imported": 2000,
                "status": "OK"
              }
            }
          }
        }
      },
      "StrictInvalid": {
        "description": "A 400 response indicates that some events failed validation.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "error": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                },
                "num_records_imported": {
                  "type": "integer"
                },
                "failed_records": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "index": {
                        "type": "number"
                      },
                      "insert_id": {
                        "type": "string"
                      },
                      "field": {
                        "type": "string"
                      },
                      "message": {
                        "type": "string"
                      }
                    }
                  }
                }
              },
              "example": {
                "code": 400,
                "num_records_imported": 999,
                "status": "Bad Request",
                "failed_records": [
                  {
                    "index": 0,
                    "insert_id": "13c0b661-f48b-51cd-ba54-97c5999169c0",
                    "field": "properties.time",
                    "message": "'properties.time' is invalid: must be specified as seconds since epoch"
                  }
                ]
              }
            }
          }
        }
      },
      "StrictUnauthorized": {
        "description": "A 401 response indicates invalid service account credentials.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "error": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 401,
                "error": "Invalid service account credentials",
                "status": "Unauthorized"
              }
            }
          }
        }
      }
    }
  },
  "x-readme-deploy-id": "identity",
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