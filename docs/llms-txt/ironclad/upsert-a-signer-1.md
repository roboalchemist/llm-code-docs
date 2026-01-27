# Source: https://clickwrap-developer.ironcladapp.com/reference/upsert-a-signer-1.md

# Upsert a Signer

You can pass **either** a single Signer JSON object or _an array_ of Signer objects with `additional_attributes` that will be attached to the Signer record in your account. Your response will be an Array of JSON objects corresponding to the data passed.

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
    "/sites/{site_id}/signers": {
      "post": {
        "summary": "Upsert a Signer",
        "description": "You can pass **either** a single Signer JSON object or _an array_ of Signer objects with `additional_attributes` that will be attached to the Signer record in your account. Your response will be an Array of JSON objects corresponding to the data passed.",
        "operationId": "upsert-a-signer",
        "tags": [
          "Signers"
        ],
        "parameters": [
          {
            "name": "site_id",
            "in": "path",
            "description": "ID of your site. Located here: https://app.pactsafe.com/settings/account",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "oneOf": [
                  {
                    "allOf": [
                      {
                        "type": "object",
                        "title": "Signer",
                        "required": [
                          "signer_id"
                        ],
                        "properties": {
                          "signer_id": {
                            "type": "string",
                            "example": "eric@pactsafe.com"
                          },
                          "test_mode": {
                            "type": "boolean",
                            "example": false
                          }
                        }
                      },
                      {
                        "title": "Signer",
                        "type": "object",
                        "properties": {
                          "uuid": {
                            "type": "string",
                            "example": "55e0820564a5846a5a0387c4",
                            "readOnly": true
                          },
                          "_id": {
                            "type": "string",
                            "readOnly": true
                          },
                          "account": {
                            "type": "integer",
                            "readOnly": true,
                            "example": 2,
                            "default": 0
                          },
                          "site": {
                            "type": "integer",
                            "readOnly": true,
                            "example": 2,
                            "default": 0
                          },
                          "name": {
                            "type": "string",
                            "example": "Eric Prugh"
                          },
                          "email": {
                            "type": "string",
                            "example": "eric@pactsafe.com"
                          },
                          "email_hash": {
                            "type": "string",
                            "example": "20a9d8f9c7d8415b58ece4621a6517ca",
                            "readOnly": true
                          },
                          "mobile_number": {
                            "type": "string",
                            "example": "(317) 403-7298"
                          },
                          "company_name": {
                            "type": "string",
                            "example": "PactSafe"
                          },
                          "title": {
                            "type": "string",
                            "example": "Person"
                          },
                          "sendable": {
                            "type": "boolean",
                            "example": true,
                            "default": true,
                            "readOnly": true
                          },
                          "deliverable": {
                            "title": "Deliverable",
                            "type": "object",
                            "readOnly": true,
                            "properties": {
                              "email": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "email_status": {
                                "enum": [
                                  "processed",
                                  "dropped",
                                  "delivered",
                                  "deferred",
                                  "bounce",
                                  "open",
                                  "dropped",
                                  "click",
                                  "spamreport",
                                  "unsubscribe",
                                  "group_unsubscribe",
                                  "group_resubscribe"
                                ],
                                "title": "EmailStatus",
                                "type": "string"
                              },
                              "mobile_number": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "mobile_number_status": {
                                "enum": [
                                  "failed",
                                  "delivered",
                                  "queued",
                                  "undelivered",
                                  "sent",
                                  "Opted out",
                                  "landline"
                                ],
                                "title": "MobileNumberStatus",
                                "type": "string"
                              }
                            }
                          },
                          "created_time": {
                            "type": "string",
                            "example": "2015-08-28T15:45:09.585Z",
                            "readOnly": true
                          },
                          "updated_time": {
                            "type": "string",
                            "example": "2015-08-28T15:45:09.585Z",
                            "readOnly": true
                          },
                          "latest_activity_time": {
                            "type": "string",
                            "default": null,
                            "example": "2015-08-28T15:45:09.585Z",
                            "readOnly": true
                          },
                          "additional_attributes": {
                            "type": "object",
                            "additionalProperties": true,
                            "properties": {
                              "city": {
                                "type": "string",
                                "example": "Indianapolis"
                              },
                              "mobile_number": {
                                "type": "string",
                                "example": "(317) 403-7298"
                              },
                              "email": {
                                "type": "string",
                                "example": "eric@pactsafe.com"
                              },
                              "first_name": {
                                "type": "string",
                                "example": "Eric"
                              },
                              "last_name": {
                                "type": "string",
                                "example": "Prugh"
                              },
                              "title": {
                                "type": "string",
                                "example": "Person"
                              },
                              "company": {
                                "type": "string",
                                "example": "PactSafe"
                              }
                            }
                          },
                          "last_action": {
                            "readOnly": true,
                            "type": "string",
                            "example": "58b8db7e379e242c5b189d7d"
                          },
                          "last_downloaded_time": {
                            "type": "string",
                            "default": null,
                            "example": "2015-08-28T15:45:09.585Z",
                            "readOnly": true
                          },
                          "last_downloaded_by": {
                            "readOnly": true,
                            "type": "integer",
                            "example": 1
                          },
                          "source": {
                            "enum": [
                              "manual",
                              "import",
                              "api",
                              "smartpact"
                            ],
                            "title": "SignerSource",
                            "type": "string",
                            "readOnly": true
                          },
                          "notify": {
                            "type": "boolean",
                            "example": true,
                            "default": true
                          },
                          "amber_road": {
                            "readOnly": true,
                            "type": "object",
                            "properties": {
                              "isValid": {
                                "type": "boolean"
                              },
                              "status": {
                                "type": "string"
                              },
                              "screened_date": {
                                "type": "string",
                                "example": "2015-08-28T15:45:09.585Z"
                              }
                            }
                          }
                        }
                      }
                    ]
                  },
                  {
                    "type": "object",
                    "title": "Signers",
                    "properties": {
                      "signers": {
                        "type": "array",
                        "items": {
                          "allOf": [
                            {
                              "type": "object",
                              "title": "Signer",
                              "required": [
                                "signer_id"
                              ],
                              "properties": {
                                "signer_id": {
                                  "type": "string",
                                  "example": "eric@pactsafe.com"
                                },
                                "test_mode": {
                                  "type": "boolean",
                                  "example": false
                                }
                              }
                            },
                            {
                              "title": "Signer",
                              "type": "object",
                              "properties": {
                                "uuid": {
                                  "type": "string",
                                  "example": "55e0820564a5846a5a0387c4",
                                  "readOnly": true
                                },
                                "_id": {
                                  "type": "string",
                                  "readOnly": true
                                },
                                "account": {
                                  "type": "integer",
                                  "readOnly": true,
                                  "example": 2,
                                  "default": 0
                                },
                                "site": {
                                  "type": "integer",
                                  "readOnly": true,
                                  "example": 2,
                                  "default": 0
                                },
                                "name": {
                                  "type": "string",
                                  "example": "Eric Prugh"
                                },
                                "email": {
                                  "type": "string",
                                  "example": "eric@pactsafe.com"
                                },
                                "email_hash": {
                                  "type": "string",
                                  "example": "20a9d8f9c7d8415b58ece4621a6517ca",
                                  "readOnly": true
                                },
                                "mobile_number": {
                                  "type": "string",
                                  "example": "(317) 403-7298"
                                },
                                "company_name": {
                                  "type": "string",
                                  "example": "PactSafe"
                                },
                                "title": {
                                  "type": "string",
                                  "example": "Person"
                                },
                                "sendable": {
                                  "type": "boolean",
                                  "example": true,
                                  "default": true,
                                  "readOnly": true
                                },
                                "deliverable": {
                                  "title": "Deliverable",
                                  "type": "object",
                                  "readOnly": true,
                                  "properties": {
                                    "email": {
                                      "type": "boolean",
                                      "example": true,
                                      "default": true
                                    },
                                    "email_status": {
                                      "enum": [
                                        "processed",
                                        "dropped",
                                        "delivered",
                                        "deferred",
                                        "bounce",
                                        "open",
                                        "dropped",
                                        "click",
                                        "spamreport",
                                        "unsubscribe",
                                        "group_unsubscribe",
                                        "group_resubscribe"
                                      ],
                                      "title": "EmailStatus",
                                      "type": "string"
                                    },
                                    "mobile_number": {
                                      "type": "boolean",
                                      "example": true,
                                      "default": true
                                    },
                                    "mobile_number_status": {
                                      "enum": [
                                        "failed",
                                        "delivered",
                                        "queued",
                                        "undelivered",
                                        "sent",
                                        "Opted out",
                                        "landline"
                                      ],
                                      "title": "MobileNumberStatus",
                                      "type": "string"
                                    }
                                  }
                                },
                                "created_time": {
                                  "type": "string",
                                  "example": "2015-08-28T15:45:09.585Z",
                                  "readOnly": true
                                },
                                "updated_time": {
                                  "type": "string",
                                  "example": "2015-08-28T15:45:09.585Z",
                                  "readOnly": true
                                },
                                "latest_activity_time": {
                                  "type": "string",
                                  "default": null,
                                  "example": "2015-08-28T15:45:09.585Z",
                                  "readOnly": true
                                },
                                "additional_attributes": {
                                  "type": "object",
                                  "additionalProperties": true,
                                  "properties": {
                                    "city": {
                                      "type": "string",
                                      "example": "Indianapolis"
                                    },
                                    "mobile_number": {
                                      "type": "string",
                                      "example": "(317) 403-7298"
                                    },
                                    "email": {
                                      "type": "string",
                                      "example": "eric@pactsafe.com"
                                    },
                                    "first_name": {
                                      "type": "string",
                                      "example": "Eric"
                                    },
                                    "last_name": {
                                      "type": "string",
                                      "example": "Prugh"
                                    },
                                    "title": {
                                      "type": "string",
                                      "example": "Person"
                                    },
                                    "company": {
                                      "type": "string",
                                      "example": "PactSafe"
                                    }
                                  }
                                },
                                "last_action": {
                                  "readOnly": true,
                                  "type": "string",
                                  "example": "58b8db7e379e242c5b189d7d"
                                },
                                "last_downloaded_time": {
                                  "type": "string",
                                  "default": null,
                                  "example": "2015-08-28T15:45:09.585Z",
                                  "readOnly": true
                                },
                                "last_downloaded_by": {
                                  "readOnly": true,
                                  "type": "integer",
                                  "example": 1
                                },
                                "source": {
                                  "enum": [
                                    "manual",
                                    "import",
                                    "api",
                                    "smartpact"
                                  ],
                                  "title": "SignerSource",
                                  "type": "string",
                                  "readOnly": true
                                },
                                "notify": {
                                  "type": "boolean",
                                  "example": true,
                                  "default": true
                                },
                                "amber_road": {
                                  "readOnly": true,
                                  "type": "object",
                                  "properties": {
                                    "isValid": {
                                      "type": "boolean"
                                    },
                                    "status": {
                                      "type": "string"
                                    },
                                    "screened_date": {
                                      "type": "string",
                                      "example": "2015-08-28T15:45:09.585Z"
                                    }
                                  }
                                }
                              }
                            }
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
          "200": {
            "description": "200",
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
                      "type": "object",
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
                            "allOf": [
                              {
                                "title": "Signer",
                                "type": "object",
                                "properties": {
                                  "uuid": {
                                    "type": "string",
                                    "example": "55e0820564a5846a5a0387c4",
                                    "readOnly": true
                                  },
                                  "_id": {
                                    "type": "string",
                                    "readOnly": true
                                  },
                                  "account": {
                                    "type": "integer",
                                    "readOnly": true,
                                    "example": 2,
                                    "default": 0
                                  },
                                  "site": {
                                    "type": "integer",
                                    "readOnly": true,
                                    "example": 2,
                                    "default": 0
                                  },
                                  "name": {
                                    "type": "string",
                                    "example": "Eric Prugh"
                                  },
                                  "email": {
                                    "type": "string",
                                    "example": "eric@pactsafe.com"
                                  },
                                  "email_hash": {
                                    "type": "string",
                                    "example": "20a9d8f9c7d8415b58ece4621a6517ca",
                                    "readOnly": true
                                  },
                                  "mobile_number": {
                                    "type": "string",
                                    "example": "(317) 403-7298"
                                  },
                                  "company_name": {
                                    "type": "string",
                                    "example": "PactSafe"
                                  },
                                  "title": {
                                    "type": "string",
                                    "example": "Person"
                                  },
                                  "sendable": {
                                    "type": "boolean",
                                    "example": true,
                                    "default": true,
                                    "readOnly": true
                                  },
                                  "deliverable": {
                                    "title": "Deliverable",
                                    "type": "object",
                                    "readOnly": true,
                                    "properties": {
                                      "email": {
                                        "type": "boolean",
                                        "example": true,
                                        "default": true
                                      },
                                      "email_status": {
                                        "enum": [
                                          "processed",
                                          "dropped",
                                          "delivered",
                                          "deferred",
                                          "bounce",
                                          "open",
                                          "dropped",
                                          "click",
                                          "spamreport",
                                          "unsubscribe",
                                          "group_unsubscribe",
                                          "group_resubscribe"
                                        ],
                                        "title": "EmailStatus",
                                        "type": "string"
                                      },
                                      "mobile_number": {
                                        "type": "boolean",
                                        "example": true,
                                        "default": true
                                      },
                                      "mobile_number_status": {
                                        "enum": [
                                          "failed",
                                          "delivered",
                                          "queued",
                                          "undelivered",
                                          "sent",
                                          "Opted out",
                                          "landline"
                                        ],
                                        "title": "MobileNumberStatus",
                                        "type": "string"
                                      }
                                    }
                                  },
                                  "created_time": {
                                    "type": "string",
                                    "example": "2015-08-28T15:45:09.585Z",
                                    "readOnly": true
                                  },
                                  "updated_time": {
                                    "type": "string",
                                    "example": "2015-08-28T15:45:09.585Z",
                                    "readOnly": true
                                  },
                                  "latest_activity_time": {
                                    "type": "string",
                                    "default": null,
                                    "example": "2015-08-28T15:45:09.585Z",
                                    "readOnly": true
                                  },
                                  "additional_attributes": {
                                    "type": "object",
                                    "additionalProperties": true,
                                    "properties": {
                                      "city": {
                                        "type": "string",
                                        "example": "Indianapolis"
                                      },
                                      "mobile_number": {
                                        "type": "string",
                                        "example": "(317) 403-7298"
                                      },
                                      "email": {
                                        "type": "string",
                                        "example": "eric@pactsafe.com"
                                      },
                                      "first_name": {
                                        "type": "string",
                                        "example": "Eric"
                                      },
                                      "last_name": {
                                        "type": "string",
                                        "example": "Prugh"
                                      },
                                      "title": {
                                        "type": "string",
                                        "example": "Person"
                                      },
                                      "company": {
                                        "type": "string",
                                        "example": "PactSafe"
                                      }
                                    }
                                  },
                                  "last_action": {
                                    "readOnly": true,
                                    "type": "string",
                                    "example": "58b8db7e379e242c5b189d7d"
                                  },
                                  "last_downloaded_time": {
                                    "type": "string",
                                    "default": null,
                                    "example": "2015-08-28T15:45:09.585Z",
                                    "readOnly": true
                                  },
                                  "last_downloaded_by": {
                                    "readOnly": true,
                                    "type": "integer",
                                    "example": 1
                                  },
                                  "source": {
                                    "enum": [
                                      "manual",
                                      "import",
                                      "api",
                                      "smartpact"
                                    ],
                                    "title": "SignerSource",
                                    "type": "string",
                                    "readOnly": true
                                  },
                                  "notify": {
                                    "type": "boolean",
                                    "example": true,
                                    "default": true
                                  },
                                  "amber_road": {
                                    "readOnly": true,
                                    "type": "object",
                                    "properties": {
                                      "isValid": {
                                        "type": "boolean"
                                      },
                                      "status": {
                                        "type": "string"
                                      },
                                      "screened_date": {
                                        "type": "string",
                                        "example": "2015-08-28T15:45:09.585Z"
                                      }
                                    }
                                  }
                                }
                              },
                              {
                                "type": "object",
                                "title": "Signer",
                                "properties": {
                                  "signer_id": {
                                    "type": "string",
                                    "example": "eric@pactsafe.com",
                                    "readOnly": true
                                  },
                                  "test_mode": {
                                    "type": "boolean",
                                    "example": false,
                                    "readOnly": true
                                  }
                                }
                              }
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
          "403": {
            "description": "Forbidden."
          },
          "404": {
            "description": "Not found."
          },
          "422": {
            "description": "Unprocessable."
          }
        },
        "deprecated": false
      }
    }
  }
}
```