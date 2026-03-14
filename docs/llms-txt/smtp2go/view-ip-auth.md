# Source: https://developers.smtp2go.com/reference/view-ip-auth.md

# View IP Auth

Retreive IP Auth information

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
    "/ip_auth/view": {
      "post": {
        "tags": [
          "IP AUTH"
        ],
        "summary": "View IP Auth",
        "description": "Returns a list of all IP Auth entries that are managed by this account, or details of a specific IP Auth, when you include the [ip_address] in your request. If no entries are available, this will return an empty list.",
        "operationId": "view-ip-auth",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "ip_address": {
                    "type": "string",
                    "description": "If passed, a valid ip address of an existing IP Auth entry that you wish to view"
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
            "description": "List of IP Auth entries",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "ae4a8446-63c6-11ed-95d3-f23c92160e3c",
                      "data": {
                        "results": [
                          {
                            "ip_address": "127.0.0.1",
                            "sending_allowed": true,
                            "custom_ratelimit": false,
                            "custom_ratelimit_value": null,
                            "custom_ratelimit_period": "0:00:00",
                            "description": "",
                            "feedback_enabled": false,
                            "feedback_domain": "default",
                            "feedback_html": "",
                            "feedback_text": "",
                            "archive_enabled": false,
                            "open_tracking_enabled": false,
                            "audit_email": null,
                            "bounce_notifications": "from",
                            "status": "allowed"
                          }
                        ],
                        "default_ratelimit_value": 0,
                        "default_ratelimit_period": "unlimited"
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
                      "example": "aa253464-0bd0-467a-b24b-6159dcd7be60"
                    },
                    "data": {
                      "type": "object",
                      "required": [
                        "results"
                      ],
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "required": [
                              "ip_addres",
                              "sending_allowed",
                              "custom_ratelimit"
                            ],
                            "properties": {
                              "comments": {
                                "type": "string",
                                "example": "Comment explaining how amazing this IP Auth entry is"
                              },
                              "ip_addres": {
                                "type": "string",
                                "example": "127.0.0.1"
                              },
                              "email_password": {
                                "type": "string",
                                "example": "H#8dkK2djs"
                              },
                              "sending_allowed": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "custom_ratelimit": {
                                "type": "boolean",
                                "example": true,
                                "default": true
                              },
                              "custom_ratelimit_value": {
                                "type": "integer",
                                "example": 100,
                                "default": 0,
                                "nullable": true
                              },
                              "custom_ratelimit_period": {
                                "type": "string",
                                "example": "1 day"
                              },
                              "default_ratelimit_value": {
                                "type": "string",
                                "example": 123,
                                "description": "The default limit of emails this IP Auth user can send in the period specified in <code>default_ratelimit_period</code>. <strong>Note:</strong> Used if <code>custom_ratelimit</code> is false."
                              },
                              "default_ratelimit_period": {
                                "type": "string",
                                "example": "unlimited",
                                "description": "The default period for which this IP Auth will be limited to the number of emails specified in <code>default_ratelimit_value</code>.<br><br><strong>Syntax:</strong> \"\\<n\\> [hour[s]|day[s]|week[s]|month[s]] [hh:mm:ss]\".<br><br><strong>Examples: </strong> \"0:30:00\", \"1 hour\", \"2 days\", \"3 months\", \"4 months 5:00:00\".<br><br><strong>Note:</strong> Used if <code>custom_ratelimit</code> is false."
                              },
                              "ippool": {
                                "type": "integer",
                                "example": 1234
                              },
                              "description": {
                                "type": "string"
                              },
                              "feedback_enabled": {
                                "type": "boolean",
                                "example": true
                              },
                              "feedback_domain": {
                                "type": "string",
                                "example": "default"
                              },
                              "feedback_html": {
                                "type": "string"
                              },
                              "feedback_text": {
                                "type": "string"
                              },
                              "archive_enabled": {
                                "type": "boolean",
                                "example": true
                              },
                              "open_tracking_enabled": {
                                "type": "boolean",
                                "example": true
                              },
                              "audit_email": {
                                "type": "string",
                                "nullable": true
                              },
                              "bounce_notifications": {
                                "type": "string",
                                "example": "from"
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