# Source: https://clickwrap-developer.ironcladapp.com/reference/update-your-account-details-1.md

# Update Your Account

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
    "/accounts/{account_id}": {
      "patch": {
        "summary": "Update Your Account",
        "description": "",
        "operationId": "update-your-account-details",
        "tags": [
          "Accounts"
        ],
        "parameters": [
          {
            "name": "account_id",
            "in": "path",
            "description": "The ID of the PactSafe Account.",
            "schema": {
              "type": "integer",
              "format": "integer"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "example": 1,
                    "default": 0,
                    "readOnly": true
                  },
                  "name": {
                    "type": "string",
                    "example": "iLawNow"
                  },
                  "key": {
                    "type": "string",
                    "example": "ilawnow"
                  },
                  "email_display_name": {
                    "type": "string",
                    "example": "iLawNow, Inc."
                  },
                  "email_reply_address": {
                    "type": "string",
                    "example": "team@ilawnow.com"
                  },
                  "created_by": {
                    "type": "integer",
                    "example": 1,
                    "default": 0,
                    "readOnly": true
                  },
                  "updated_by": {
                    "type": "integer",
                    "example": 1,
                    "default": 0,
                    "readOnly": true
                  },
                  "company_information": {
                    "type": "object",
                    "properties": {
                      "street": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "city": {
                        "type": "string"
                      },
                      "state": {
                        "type": "string"
                      },
                      "postal_code": {
                        "type": "string"
                      },
                      "phone": {
                        "type": "string"
                      }
                    }
                  },
                  "billing": {
                    "type": "object",
                    "properties": {
                      "first_name": {
                        "type": "string"
                      },
                      "last_name": {
                        "type": "string"
                      },
                      "email": {
                        "type": "string"
                      },
                      "notify": {
                        "type": "string"
                      },
                      "cc_emails": {
                        "type": "string"
                      },
                      "company_name": {
                        "type": "string"
                      },
                      "address": {
                        "type": "object"
                      },
                      "updated_time": {
                        "type": "string",
                        "readOnly": true
                      },
                      "updated_by": {
                        "type": "integer",
                        "readOnly": true
                      }
                    }
                  },
                  "subscription": {
                    "type": "object",
                    "properties": {
                      "plan": {
                        "type": "string",
                        "example": "developer",
                        "readOnly": true
                      },
                      "active": {
                        "type": "boolean",
                        "example": true,
                        "readOnly": true
                      },
                      "status": {
                        "type": "string",
                        "example": "active",
                        "readOnly": true
                      },
                      "term_start_date": {
                        "type": "string",
                        "example": "2015-07-12T21:28:39.000Z",
                        "readOnly": true
                      },
                      "term_end_date": {
                        "type": "string",
                        "example": "2015-07-12T21:28:39.000Z",
                        "readOnly": true
                      },
                      "total_cost": {
                        "type": "number",
                        "readOnly": true
                      },
                      "setup_cost": {
                        "type": "number",
                        "readOnly": true
                      },
                      "payment_interval": {
                        "type": "string",
                        "readOnly": true
                      },
                      "payment_method": {
                        "type": "string",
                        "readOnly": true
                      },
                      "is_customer": {
                        "type": "boolean",
                        "readOnly": true
                      },
                      "uuid": {
                        "type": "string",
                        "readOnly": true
                      },
                      "notes": {
                        "type": "string",
                        "readOnly": true
                      }
                    }
                  },
                  "usage": {
                    "type": "object",
                    "properties": {
                      "published_locations": {
                        "type": "integer",
                        "readOnly": true
                      }
                    }
                  },
                  "limits": {
                    "type": "object",
                    "readOnly": true,
                    "properties": {
                      "acceptances": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "signers": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "contracts": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "groups": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "requests_sent": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "users": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "sites": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "api_requests": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "published_locations": {
                        "type": "integer",
                        "readOnly": true
                      }
                    }
                  },
                  "enforce_limits": {
                    "type": "boolean",
                    "readOnly": true
                  },
                  "password_security": {
                    "type": "object",
                    "properties": {
                      "duration": {
                        "type": "integer",
                        "readOnly": true
                      },
                      "reuse": {
                        "type": "integer",
                        "readOnly": true
                      }
                    }
                  },
                  "reseller": {
                    "type": "boolean",
                    "example": false,
                    "default": true,
                    "readOnly": true
                  },
                  "updated_time": {
                    "type": "string",
                    "example": "2015-06-12T21:28:39.993Z",
                    "readOnly": true
                  },
                  "created_time": {
                    "type": "string",
                    "example": "2015-06-12T21:28:39.982Z",
                    "readOnly": true
                  }
                }
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
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "example": 1,
                          "default": 0,
                          "readOnly": true
                        },
                        "name": {
                          "type": "string",
                          "example": "iLawNow"
                        },
                        "key": {
                          "type": "string",
                          "example": "ilawnow"
                        },
                        "email_display_name": {
                          "type": "string",
                          "example": "iLawNow, Inc."
                        },
                        "email_reply_address": {
                          "type": "string",
                          "example": "team@ilawnow.com"
                        },
                        "created_by": {
                          "type": "integer",
                          "example": 1,
                          "default": 0,
                          "readOnly": true
                        },
                        "updated_by": {
                          "type": "integer",
                          "example": 1,
                          "default": 0,
                          "readOnly": true
                        },
                        "company_information": {
                          "type": "object",
                          "properties": {
                            "street": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "city": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            },
                            "postal_code": {
                              "type": "string"
                            },
                            "phone": {
                              "type": "string"
                            }
                          }
                        },
                        "billing": {
                          "type": "object",
                          "properties": {
                            "first_name": {
                              "type": "string"
                            },
                            "last_name": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "notify": {
                              "type": "string"
                            },
                            "cc_emails": {
                              "type": "string"
                            },
                            "company_name": {
                              "type": "string"
                            },
                            "address": {
                              "type": "object"
                            },
                            "updated_time": {
                              "type": "string",
                              "readOnly": true
                            },
                            "updated_by": {
                              "type": "integer",
                              "readOnly": true
                            }
                          }
                        },
                        "subscription": {
                          "type": "object",
                          "properties": {
                            "plan": {
                              "type": "string",
                              "example": "developer",
                              "readOnly": true
                            },
                            "active": {
                              "type": "boolean",
                              "example": true,
                              "readOnly": true
                            },
                            "status": {
                              "type": "string",
                              "example": "active",
                              "readOnly": true
                            },
                            "term_start_date": {
                              "type": "string",
                              "example": "2015-07-12T21:28:39.000Z",
                              "readOnly": true
                            },
                            "term_end_date": {
                              "type": "string",
                              "example": "2015-07-12T21:28:39.000Z",
                              "readOnly": true
                            },
                            "total_cost": {
                              "type": "number",
                              "readOnly": true
                            },
                            "setup_cost": {
                              "type": "number",
                              "readOnly": true
                            },
                            "payment_interval": {
                              "type": "string",
                              "readOnly": true
                            },
                            "payment_method": {
                              "type": "string",
                              "readOnly": true
                            },
                            "is_customer": {
                              "type": "boolean",
                              "readOnly": true
                            },
                            "uuid": {
                              "type": "string",
                              "readOnly": true
                            },
                            "notes": {
                              "type": "string",
                              "readOnly": true
                            }
                          }
                        },
                        "usage": {
                          "type": "object",
                          "properties": {
                            "published_locations": {
                              "type": "integer",
                              "readOnly": true
                            }
                          }
                        },
                        "limits": {
                          "type": "object",
                          "readOnly": true,
                          "properties": {
                            "acceptances": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "signers": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "contracts": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "groups": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "requests_sent": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "users": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "sites": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "api_requests": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "published_locations": {
                              "type": "integer",
                              "readOnly": true
                            }
                          }
                        },
                        "enforce_limits": {
                          "type": "boolean",
                          "readOnly": true
                        },
                        "password_security": {
                          "type": "object",
                          "properties": {
                            "duration": {
                              "type": "integer",
                              "readOnly": true
                            },
                            "reuse": {
                              "type": "integer",
                              "readOnly": true
                            }
                          }
                        },
                        "reseller": {
                          "type": "boolean",
                          "example": false,
                          "default": true,
                          "readOnly": true
                        },
                        "updated_time": {
                          "type": "string",
                          "example": "2015-06-12T21:28:39.993Z",
                          "readOnly": true
                        },
                        "created_time": {
                          "type": "string",
                          "example": "2015-06-12T21:28:39.982Z",
                          "readOnly": true
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Forbidden."
          }
        },
        "deprecated": false
      }
    }
  }
}
```