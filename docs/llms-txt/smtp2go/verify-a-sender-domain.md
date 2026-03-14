# Source: https://developers.smtp2go.com/reference/verify-a-sender-domain.md

# Verify a sender domain

Verify a sender domain on your account removing the need to wait for the periodic verification every 7 minutes.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "SMTP2GO API v3.0.3",
    "version": "3.0.3"
  },
  "servers": [
    {
      "url": "https://api.smtp2go.com/v3",
      "description": "Regionless"
    },
    {
      "url": "https://us-api.smtp2go.com/v3",
      "description": "US Region"
    },
    {
      "url": "https://eu-api.smtp2go.com/v3",
      "description": "EU Region"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "X-Smtp2go-Api-Key",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/domain/verify": {
      "post": {
        "tags": [
          "SENDER DOMAINS"
        ],
        "summary": "Verify a sender domain",
        "description": "Verify a sender domain on your account removing the need to wait for the periodic verification every 7 minutes.",
        "operationId": "verify-a-sender-domain",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "domain"
                ],
                "properties": {
                  "domain": {
                    "type": "string",
                    "description": "Domain to attempt verification for"
                  },
                  "requisition_ssl": {
                    "type": "boolean",
                    "description": "If true, requisition an SSL certificate for the tracking domain once verification is complete",
                    "default": true
                  },
                  "subaccount_id": {
                    "type": "string",
                    "description": "If you wish to make this API call on behalf of a subaccount then include its unique ID here"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Sender domain verification",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "e023461c-8c86-11e9-b984-408d5cce2644",
                      "data": {
                        "domains": [
                          {
                            "domain": {
                              "fulldomain": "example.com",
                              "subdomain": null,
                              "domain": "example",
                              "suffix": "com",
                              "dkim_selector": "s123456",
                              "dkim_verified": true,
                              "dkim_status": "",
                              "dkim_value": "dkim.smtp2go.net",
                              "rpath_selector": "em744766",
                              "rpath_verified": true,
                              "rpath_status": "",
                              "rpath_value": "return.smtp2go.net"
                            },
                            "trackers": [
                              {
                                "fulldomain": "link.example.com",
                                "subdomain": "link",
                                "domain": "example",
                                "suffix": "com",
                                "cname_verified": false,
                                "cname_status": "",
                                "cname_value": "track.smtp2go.net",
                                "enabled": false
                              }
                            ]
                          }
                        ]
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "required": [
                    "request_id",
                    "data"
                  ],
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "e023461c-8c86-11e9-b984-408d5cce2644"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "domains"
                      ],
                      "properties": {
                        "domains": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "domain": {
                                "type": "object",
                                "required": [
                                  "dkim_value",
                                  "domain",
                                  "suffix",
                                  "rpath_status",
                                  "rpath_value",
                                  "dkim_status",
                                  "subdomain",
                                  "fulldomain",
                                  "dkim_selector"
                                ],
                                "properties": {
                                  "dkim_value": {
                                    "type": "string",
                                    "example": "dkim.smtp2go.net"
                                  },
                                  "domain": {
                                    "type": "string",
                                    "example": "example"
                                  },
                                  "suffix": {
                                    "type": "string",
                                    "example": "com"
                                  },
                                  "rpath_selector": {
                                    "type": "string",
                                    "example": ""
                                  },
                                  "rpath_status": {
                                    "type": "string",
                                    "example": ""
                                  },
                                  "rpath_verified": {
                                    "type": "boolean",
                                    "example": true,
                                    "default": true
                                  },
                                  "rpath_value": {
                                    "type": "string",
                                    "example": "return.smtp2go.net"
                                  },
                                  "dkim_status": {
                                    "type": "string",
                                    "example": ""
                                  },
                                  "dkim_verified": {
                                    "type": "boolean",
                                    "example": true,
                                    "default": true
                                  },
                                  "subdomain": {},
                                  "fulldomain": {
                                    "type": "string",
                                    "example": "example.com"
                                  },
                                  "dkim_selector": {
                                    "type": "string",
                                    "example": "s123456"
                                  }
                                }
                              },
                              "trackers": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "required": [
                                    "cname_value",
                                    "cname_status"
                                  ],
                                  "properties": {
                                    "cname_value": {
                                      "type": "string",
                                      "example": ""
                                    },
                                    "cname_status": {
                                      "type": "string",
                                      "example": ""
                                    },
                                    "cname_verified": {
                                      "type": "boolean",
                                      "example": false,
                                      "default": true
                                    },
                                    "domain": {
                                      "type": "string",
                                      "example": "example"
                                    },
                                    "suffix": {
                                      "type": "string",
                                      "example": "com"
                                    },
                                    "subdomain": {
                                      "type": "string",
                                      "example": "link"
                                    },
                                    "enabled": {
                                      "type": "boolean",
                                      "example": false,
                                      "default": true
                                    },
                                    "fulldomain": {
                                      "type": "string",
                                      "example": "link.example.com"
                                    }
                                  }
                                }
                              },
                              "subaccount_access": {
                                "type": "object",
                                "properties": {
                                  "subaccounts": {
                                    "type": "array",
                                    "description": "A list of subaccount IDs that were given access the sender domain."
                                  },
                                  "future_subaccounts": {
                                    "type": "boolean",
                                    "description": "If true, any new subaccounts added will automatically be given access.",
                                    "default": false
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "22e5acba-43bf-11e6-ae42-408d5cce2644",
                      "data": {
                        "error": "You do not have permission to access this API endpoint",
                        "error_code": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "22e5acba-43bf-11e6-ae42-408d5cce2644"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "error": {
                          "type": "string",
                          "example": "You do not have permission to access this API endpoint"
                        },
                        "error_code": {
                          "type": "string",
                          "example": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [
      {
        "key": "Content-Type",
        "value": "application/json"
      }
    ],
    "explorer-enabled": true,
    "proxy-enabled": true,
    "samples-enabled": true
  }
}
```