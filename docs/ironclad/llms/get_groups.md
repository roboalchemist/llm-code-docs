# Source: https://clickwrap-developer.ironcladapp.com/reference/get_groups.md

# List all Groups

List all groups available to the current user

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
    "/groups": {
      "get": {
        "summary": "List all Groups",
        "description": "List all groups available to the current user",
        "tags": [
          "Groups"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "expand",
            "description": "Expands objects that only return an ID. Works up to 2 levels deep.",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "fields",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "filter",
            "description": "Filter activities by the various fields. Note the use of 'and' between the fields. Example: `event_type==agreed and signer_id==claddy@ironcladapp.com`.\n",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "description": "Page number to offset results for pagination. Defaults to 1.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "per_page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "sort",
            "description": "Sort the results of your call by a field in the Request.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "allOf": [
                    {
                      "properties": {
                        "count": {
                          "type": "integer"
                        },
                        "has_more": {
                          "type": "boolean"
                        },
                        "page": {
                          "type": "integer"
                        },
                        "per_page": {
                          "type": "integer"
                        },
                        "total_count": {
                          "type": "integer"
                        }
                      },
                      "title": "Collection",
                      "type": "object"
                    },
                    {
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
                            "title": "Group",
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "integer",
                                "readOnly": true,
                                "default": 0,
                                "example": 1
                              },
                              "account": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 1
                              },
                              "site": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 1
                              },
                              "created_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 5
                              },
                              "created_time": {
                                "type": "string",
                                "readOnly": true,
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted."
                              },
                              "updated_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 5
                              },
                              "updated_time": {
                                "type": "string",
                                "readOnly": true,
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted."
                              },
                              "deleted": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "deleted_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 5
                              },
                              "deleted_time": {
                                "type": "string",
                                "readOnly": true,
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted."
                              },
                              "published": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "published_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 5
                              },
                              "published_time": {
                                "type": "string",
                                "readOnly": true,
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted."
                              },
                              "paused": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "paused_by": {
                                "type": "integer",
                                "readOnly": true,
                                "example": 5
                              },
                              "paused_time": {
                                "type": "string",
                                "readOnly": true,
                                "example": "2020-07-21T15:34:30.051Z",
                                "description": "ISO 8601 formatted."
                              },
                              "pending_changes": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "name": {
                                "type": "string",
                                "example": "Login Terms"
                              },
                              "key": {
                                "type": "string",
                                "example": "group-0rsabrt5a"
                              },
                              "description": {
                                "type": "string",
                                "example": "This is a description of the Login Terms group."
                              },
                              "tags": {
                                "type": "array",
                                "description": "The tags to uniquely identify or easily filter from other groups.",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "type": {
                                "title": "GroupType",
                                "type": "string",
                                "enum": [
                                  "browsewrap",
                                  "clickwrap",
                                  "form",
                                  "policy"
                                ]
                              },
                              "style": {
                                "title": "GroupStyle",
                                "type": "string",
                                "enum": [
                                  "floating",
                                  "full",
                                  "scroll",
                                  "checkbox",
                                  "combined",
                                  "embedded"
                                ]
                              },
                              "custom_styles": {
                                "type": "string",
                                "description": "Custom CSS styles to apply to the embedded clickwrap group."
                              },
                              "rendered_by_user": {
                                "type": "boolean"
                              },
                              "expect_agreed_click": {
                                "type": "boolean"
                              },
                              "expect_disagreed": {
                                "type": "boolean"
                              },
                              "container_selector": {
                                "type": "string",
                                "description": "The CSS selector for the group container element."
                              },
                              "signer_id_selector": {
                                "type": "string",
                                "description": "The CSS selector for the input element containing the signer ID value."
                              },
                              "form_selector": {
                                "type": "string",
                                "description": "The CSS selector for the form element the group belongs to."
                              },
                              "block_submission": {
                                "type": "boolean",
                                "default": true
                              },
                              "force_scroll": {
                                "type": "boolean",
                                "default": false
                              },
                              "auto_run": {
                                "type": "boolean",
                                "default": true
                              },
                              "display_all": {
                                "type": "boolean",
                                "default": true
                              },
                              "alert_message": {
                                "type": "string",
                                "default": "Before you can submit this form, you must accept all of our legal contracts."
                              },
                              "acceptance_language": {
                                "type": "string",
                                "description": "The language to display alongside the group checkbox."
                              },
                              "confirmation_email": {
                                "type": "boolean",
                                "default": false
                              },
                              "hide_record_summary": {
                                "type": "boolean",
                                "default": false
                              },
                              "opt_out_language": {
                                "type": "string"
                              },
                              "target_jurisdictions": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "target_selector": {
                                "type": "string"
                              },
                              "position": {
                                "title": "BrowsewrapPosition",
                                "type": "string",
                                "enum": [
                                  "auto",
                                  "left",
                                  "right",
                                  "center"
                                ]
                              },
                              "open_legal_center": {
                                "type": "boolean",
                                "default": true
                              },
                              "always_visible": {
                                "type": "boolean",
                                "default": false
                              },
                              "badge_text": {
                                "type": "string",
                                "description": "The text to display on the floating browsewrap badge."
                              },
                              "instructions": {
                                "type": "string"
                              },
                              "protected_url": {
                                "type": "boolean"
                              },
                              "redirect_url": {
                                "type": "string"
                              },
                              "contracts": {
                                "type": "array",
                                "items": {
                                  "title": "Contract",
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "readOnly": true,
                                      "type": "integer",
                                      "example": 2
                                    },
                                    "account": {
                                      "readOnly": true,
                                      "type": "integer",
                                      "example": 2
                                    },
                                    "site": {
                                      "readOnly": true,
                                      "type": "integer",
                                      "example": 2
                                    },
                                    "created_by": {
                                      "type": "integer",
                                      "readOnly": true,
                                      "example": 2
                                    },
                                    "created_time": {
                                      "type": "string",
                                      "example": "2020-07-21T15:34:30.051Z",
                                      "description": "ISO 8601 formatted.",
                                      "readOnly": true
                                    },
                                    "updated_by": {
                                      "type": "integer",
                                      "readOnly": true,
                                      "example": 2
                                    },
                                    "updated_time": {
                                      "type": "string",
                                      "example": "2020-07-21T15:34:30.051Z",
                                      "description": "ISO 8601 formatted.",
                                      "readOnly": true
                                    },
                                    "deleted": {
                                      "type": "boolean",
                                      "readOnly": true
                                    },
                                    "deleted_by": {
                                      "type": "integer",
                                      "readOnly": true,
                                      "example": 2
                                    },
                                    "deleted_time": {
                                      "type": "string",
                                      "example": "2020-07-21T15:34:30.051Z",
                                      "description": "ISO 8601 formatted.",
                                      "readOnly": true
                                    },
                                    "archived": {
                                      "type": "boolean",
                                      "readOnly": true
                                    },
                                    "archived_by": {
                                      "type": "integer",
                                      "readOnly": true,
                                      "example": 2
                                    },
                                    "archived_time": {
                                      "type": "string",
                                      "example": "2020-07-21T15:34:30.051Z",
                                      "description": "ISO 8601 formatted.",
                                      "readOnly": true
                                    },
                                    "published": {
                                      "type": "boolean",
                                      "readOnly": true
                                    },
                                    "published_by": {
                                      "type": "integer",
                                      "readOnly": true,
                                      "example": 2
                                    },
                                    "published_time": {
                                      "type": "string",
                                      "example": "2020-07-21T15:34:30.051Z",
                                      "description": "ISO 8601 formatted.",
                                      "readOnly": true
                                    },
                                    "protected": {
                                      "type": "boolean",
                                      "readOnly": true
                                    },
                                    "private": {
                                      "type": "boolean",
                                      "readOnly": true
                                    },
                                    "public": {
                                      "type": "boolean",
                                      "description": "The status of allowing the contract to be published to a legal center or be added to a Group.",
                                      "default": false
                                    },
                                    "shared": {
                                      "type": "boolean"
                                    },
                                    "title": {
                                      "type": "string",
                                      "description": "The title of the contract.",
                                      "example": "Portal Terms of Use"
                                    },
                                    "key": {
                                      "type": "string",
                                      "example": "template-0rnbcrv3g"
                                    },
                                    "description": {
                                      "type": "string",
                                      "example": "This is a description of the Terms of Use"
                                    },
                                    "classification": {
                                      "type": "string",
                                      "example": "privacy_policy"
                                    },
                                    "clm_record_sync": {
                                      "title": "CLMRecordSync",
                                      "type": "object",
                                      "properties": {
                                        "enabled": {
                                          "type": "boolean"
                                        },
                                        "record_type": {
                                          "type": "string",
                                          "example": "clickwrap"
                                        }
                                      }
                                    },
                                    "countries": {
                                      "type": "array",
                                      "items": {
                                        "type": "string"
                                      },
                                      "example": [
                                        "RU"
                                      ]
                                    },
                                    "locales": {
                                      "type": "array",
                                      "items": {
                                        "type": "string"
                                      },
                                      "example": [
                                        "ru-RU"
                                      ]
                                    },
                                    "download_endpoint": {
                                      "type": "string",
                                      "example": "s/3652e4b9-a327-430c-8ceb-c8f68a2bbd24/contracts/491263.pdf",
                                      "readOnly": true
                                    },
                                    "type": {
                                      "allOf": [
                                        {
                                          "title": "ContractType",
                                          "type": "string",
                                          "enum": [
                                            "html",
                                            "pdf"
                                          ]
                                        }
                                      ],
                                      "readOnly": true
                                    },
                                    "tags": {
                                      "type": "array",
                                      "description": "The tags to uniquely identify or easily filter from other contracts.",
                                      "items": {
                                        "type": "string"
                                      }
                                    },
                                    "latest_version": {
                                      "type": "string",
                                      "example": "55dccf164e10cbd8454d7951",
                                      "readOnly": true
                                    },
                                    "published_version": {
                                      "type": "string",
                                      "example": "55dccf164e10cbd8454d7951",
                                      "readOnly": true
                                    },
                                    "render_data": {
                                      "type": "object"
                                    },
                                    "language_direction": {
                                      "title": "ContractLanguageDirection",
                                      "type": "string",
                                      "enum": [
                                        "auto",
                                        "rtl"
                                      ]
                                    },
                                    "used_in": {
                                      "type": "array",
                                      "items": {
                                        "title": "ContractUsedIn",
                                        "type": "string",
                                        "enum": [
                                          "embedded_contract",
                                          "standardized_contract",
                                          "personalized_contract",
                                          "legal_center"
                                        ]
                                      }
                                    }
                                  },
                                  "required": [
                                    "title"
                                  ]
                                }
                              },
                              "validate_unique_classifications": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "dynamic": {
                                "type": "boolean",
                                "default": false
                              },
                              "render_data": {
                                "type": "object"
                              },
                              "notification_email": {
                                "type": "string",
                                "description": "The email address to send internal notifications to when a group is accepted."
                              },
                              "published_endpoint": {
                                "type": "string",
                                "description": "The URL to the published group.",
                                "readOnly": true
                              },
                              "snapshots_enabled": {
                                "type": "boolean"
                              },
                              "snapshot_config": {
                                "type": "string"
                              },
                              "snapshot": {
                                "title": "GroupSnapshot",
                                "type": "object",
                                "properties": {
                                  "image_path": {
                                    "type": "string"
                                  },
                                  "last_captured_time": {
                                    "type": "string",
                                    "example": "2020-07-21T15:34:30.051Z",
                                    "description": "ISO 8601 formatted."
                                  },
                                  "latest": {
                                    "type": "string"
                                  }
                                }
                              },
                              "snapshot_locations": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "is_associated_with_location": {
                                "type": "boolean",
                                "readOnly": true
                              },
                              "download_contracts": {
                                "type": "boolean",
                                "default": false
                              }
                            }
                          }
                        }
                      }
                    }
                  ]
                }
              }
            },
            "description": "An array of Groups"
          },
          "400": {
            "description": "Bad request."
          },
          "401": {
            "description": "The requester is unauthorized."
          }
        }
      }
    }
  }
}
```