# Source: https://clickwrap-developer.ironcladapp.com/reference/post_sites-site-id-contract.md

# Create a contract

To create a Contract, you must specify a site ID, which will be part of the URL.

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
    "/sites/{site_id}/contract": {
      "post": {
        "summary": "Create a contract",
        "description": "To create a Contract, you must specify a site ID, which will be part of the URL.",
        "tags": [
          "Sites"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "site_id",
            "description": "The ID of your site.",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "integer"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateContractRequest",
                "allOf": [
                  {
                    "title": "Version",
                    "type": "object",
                    "properties": {
                      "id": {
                        "readOnly": true,
                        "type": "string",
                        "example": "5e8c6ecc51289e1e22816d6c"
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
                      "contract": {
                        "type": "integer",
                        "readOnly": true,
                        "example": 1
                      },
                      "version_number": {
                        "type": "integer",
                        "readOnly": true,
                        "example": 2
                      },
                      "minor_version_number": {
                        "type": "integer",
                        "readOnly": true,
                        "example": 1
                      },
                      "full_version_number": {
                        "type": "string",
                        "example": "1.0",
                        "readOnly": true
                      },
                      "is_major_version": {
                        "type": "boolean"
                      },
                      "major_version": {
                        "type": "string",
                        "readOnly": true,
                        "example": "5d8ba89039c713395bf0958b"
                      },
                      "created_by": {
                        "type": "integer",
                        "readOnly": true,
                        "example": 5
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
                        "example": 5
                      },
                      "updated_time": {
                        "type": "string",
                        "example": "2020-07-21T15:34:30.051Z",
                        "description": "ISO 8601 formatted.",
                        "readOnly": true
                      },
                      "editor_version": {
                        "title": "EditorVersion",
                        "type": "string",
                        "enum": [
                          "classic",
                          "override_classic",
                          "2_0"
                        ]
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
                        "example": 5
                      },
                      "published_time": {
                        "type": "string",
                        "example": "2020-07-21T15:34:30.051Z",
                        "description": "ISO 8601 formatted.",
                        "readOnly": true
                      },
                      "scheduled_time": {
                        "type": "string",
                        "example": "2020-07-21T15:34:30.051Z",
                        "description": "ISO 8601 formatted."
                      },
                      "scheduled_by": {
                        "type": "integer",
                        "readOnly": true,
                        "example": 5
                      },
                      "effective_time": {
                        "type": "string",
                        "example": "2020-07-21T15:34:30.051Z",
                        "description": "ISO 8601 formatted."
                      },
                      "deprecated_time": {
                        "type": "string",
                        "example": "2020-07-21T15:34:30.051Z",
                        "description": "ISO 8601 formatted.",
                        "readOnly": true
                      },
                      "effective_until_time": {
                        "type": "string",
                        "example": "2020-07-21T15:34:30.051Z",
                        "description": "ISO 8601 formatted."
                      },
                      "title": {
                        "type": "string",
                        "description": "The title of the Version.",
                        "example": "Portal Terms of Use"
                      },
                      "body": {
                        "type": "string",
                        "description": "The body of the Version. Note: accepts escaped HTML.\n",
                        "example": "<h1>Updated Terms of Use</h1><p>Agreement Content</p>"
                      },
                      "protected": {
                        "type": "boolean",
                        "readOnly": true
                      },
                      "location": {
                        "type": "string",
                        "example": "https://vault.pactsafe.io/s/25b2b173-632a-4227-9877-31d2109d8c98/versions/57e3ef5a26008d7c5c9c9171.pdf",
                        "readOnly": true
                      },
                      "download_endpoint": {
                        "type": "string",
                        "example": "s/3652e4b9-a327-430c-8ceb-c8f68a2bbd24/contracts/491263.pdf",
                        "readOnly": true
                      },
                      "type": {
                        "allOf": [
                          {
                            "title": "VersionType",
                            "type": "string",
                            "enum": [
                              "html",
                              "pdf"
                            ]
                          }
                        ],
                        "readOnly": true
                      },
                      "dynamic": {
                        "type": "boolean",
                        "readOnly": true
                      },
                      "status": {
                        "allOf": [
                          {
                            "title": "VersionStatus",
                            "type": "string",
                            "enum": [
                              "draft",
                              "translating",
                              "published",
                              "deprecated"
                            ]
                          }
                        ],
                        "readOnly": true
                      },
                      "processing": {
                        "type": "boolean",
                        "readOnly": true
                      },
                      "pages": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "change_summary": {
                        "type": "string",
                        "description": "An optional summary of changes made to the Version if necessary.",
                        "example": "Added an arbitration clause."
                      },
                      "notify_signers": {
                        "deprecated": true,
                        "type": "boolean"
                      },
                      "text": {
                        "type": "array",
                        "readOnly": true,
                        "items": {
                          "type": "string"
                        },
                        "example": [
                          "56380927e143dc236f15ea78",
                          "5637e914e143dc236f15ea57"
                        ]
                      },
                      "fields": {
                        "type": "array",
                        "description": "The fields that exist on the Version object.",
                        "items": {
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
                      },
                      "tokens": {
                        "type": "array",
                        "readOnly": true,
                        "items": {
                          "type": "string"
                        },
                        "example": [
                          "56380927e143dc236f15ea78",
                          "5637e914e143dc236f15ea57"
                        ]
                      },
                      "render_data": {
                        "type": "object",
                        "example": {
                          "testing": true
                        }
                      },
                      "merge_fields": {
                        "type": "array",
                        "readOnly": true,
                        "items": {
                          "type": "string"
                        },
                        "example": [
                          "56380927e143dc236f15ea78",
                          "5637e914e143dc236f15ea57"
                        ]
                      },
                      "merge_data": {
                        "type": "object",
                        "readOnly": true
                      },
                      "thumbnail_location": {
                        "type": "string",
                        "readOnly": true,
                        "example": "s/25b2b173-632a-4227-9877-31d2109d8c98/thumbnails/documents/4/versions/5639273be8e6284913a0c5b7/preview.png"
                      },
                      "classification": {
                        "type": "string",
                        "readOnly": true,
                        "example": "privacy_policy"
                      },
                      "countries": {
                        "type": "array",
                        "readOnly": true,
                        "items": {
                          "type": "string"
                        },
                        "example": [
                          "RU"
                        ]
                      },
                      "locales": {
                        "type": "array",
                        "readOnly": true,
                        "items": {
                          "type": "string"
                        },
                        "example": [
                          "ru-RU"
                        ]
                      },
                      "tags": {
                        "type": "array",
                        "readOnly": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      "language_direction": {
                        "type": "string",
                        "readOnly": true
                      },
                      "body_language": {
                        "type": "string",
                        "description": "ISO 639-1 locale code indicating the language of the contract text",
                        "example": "fr"
                      }
                    },
                    "required": [
                      "title"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "public": {
                        "type": "boolean",
                        "description": "The status of allowing the contract to be published to a legal center or be added to a Group.",
                        "default": false
                      },
                      "shared": {
                        "type": "boolean"
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
                      "tags": {
                        "type": "array",
                        "description": "The tags to uniquely identify or easily filter from other contracts.",
                        "items": {
                          "type": "string"
                        }
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
                    }
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created Contract.",
            "content": {
              "application/json": {
                "schema": {
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
              }
            }
          },
          "400": {
            "description": "Bad request."
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