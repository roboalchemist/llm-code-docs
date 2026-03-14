# Source: https://developers.smtp2go.com/reference/add-an-smtp-user.md

# Add an SMTP user

Add a new SMTP user to your account. Full details of the available options for new user accounts can be found in the SMTP User Guide.

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
    "/users/smtp/add": {
      "post": {
        "tags": [
          "SMTP USERS"
        ],
        "summary": "Add an SMTP user",
        "description": "Add a new SMTP user to your account. Full details of the available options for new user accounts can be found in the SMTP User Guide.",
        "operationId": "add-an-smtp-user",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "username"
                ],
                "properties": {
                  "username": {
                    "type": "string",
                    "description": "A username to access the SMTP2GO service via SMTP.  Length = 5 to 100"
                  },
                  "email_password": {
                    "type": "string",
                    "description": "A valid password for your new SMTP User. <br><br>Must have an entropy of at least 64 bits. <a target='_blank' href='https://www.calculator.net/password-generator.html'>Consider using a password generator</a> or leave blank for an auto generated value. Ideally contain at least: 12 characters, 1 digit, symbol, uppercase letter, and lowercase letter."
                  },
                  "description": {
                    "type": "string",
                    "description": "A comment or description of your new SMTP User"
                  },
                  "custom_ratelimit": {
                    "type": "boolean",
                    "description": "If true, a custom rate limit will be enabled for this user, and defined by the <code>custom_ratelimit_value</code> and <code>custom_ratelimit_period</code>.  Default: false"
                  },
                  "custom_ratelimit_value": {
                    "type": "integer",
                    "description": "If passed, defines the limit of emails this user can send in the period specified in <code>custom_ratelimit_period</code>.<br><br><strong>Note:</strong> Only stores this value if <code>custom_ratelimit</code> is true.",
                    "format": "int32"
                  },
                  "custom_ratelimit_period": {
                    "type": "string",
                    "description": "If passed, defines the period for which this user will be limited to the number of emails specified in <code>custom_ratelimit_value</code>.<br><br><strong>Syntax:</strong> \"\\<n\\> [hour[s]|day[s]|week[s]|month[s]] [hh:mm:ss]\".<br><br><strong>Examples: </strong> \"0:30:00\", \"1 hour\", \"2 days\", \"3 months\", \"4 months 5:00:00\".<br><br><strong>Note:</strong> Only stores this value if <code>custom_ratelimit</code> is true."
                  },
                  "ip_pool": {
                    "type": "integer",
                    "description": "If passed, any emails sent with this SMTP user will use dedicated IP's in this IP Pool, This value can be found on the <code>/v3/dedicated_ips/view</code> endpoint.",
                    "example": 1234
                  },
                  "feedback_enabled": {
                    "type": "boolean",
                    "description": "If true, custom feedback via the unsubscribe footer will be enabled and defined by the below settings.  Default: false"
                  },
                  "feedback_domain": {
                    "type": "string",
                    "description": "The domain to insert into the custom feedback links via the unsubscribe footer. Default: blank<br><br><strong>Warning:</strong> <ul> <li>In order to use the SMTP2go feedback handling feature, this parameter needs to be set to \"default\"</li><li>Setting this value to anything other than \"default\", disables the ability for SMTP2go to correctly manage the feedback responses and should not normally be set to anything other than \"default\"</li><ul>",
                    "default": "default"
                  },
                  "feedback_html": {
                    "type": "string",
                    "description": "The HTML content to insert into the custom feedback email body via the unsubscribe footer.  Default: blank <br><br><strong>System Variables (Only available here):</strong><ul><li>Unsubscribe URL = %%UNSUBSCRIBE%% </li><li>Email address = %%EMAIL%%</li></ul>"
                  },
                  "feedback_text": {
                    "type": "string",
                    "description": "The text content to insert into the custom feedback email body via the unsubscribe footer.  Default: blank<br><br><strong>System Variables (Only available here):</strong><ul><li>Unsubscribe URL = %%UNSUBSCRIBE%% </li><li>Email address = %%EMAIL%%</li></ul>"
                  },
                  "open_tracking_enabled": {
                    "type": "boolean",
                    "description": "If true, open tracking will be enabled for this user.  Default: false"
                  },
                  "click_tracking_enabled": {
                    "type": "boolean",
                    "description": "If true, click tracking will be enabled for this user.  Default: false"
                  },
                  "archive_enabled": {
                    "type": "boolean",
                    "description": "If true, archiving (available on paid plans) will be enabled for this user.  Default: false."
                  },
                  "audit_email": {
                    "type": "string",
                    "description": "If passed, this email will be BCC'd on all emails sent by this SMTP User"
                  },
                  "bounce_notifications": {
                    "type": "string",
                    "description": "If passed, will control how bounce notifications are handled. Must be one of [from, drop, or a valid email address]. [from] will return the email to sender, [drop] will discard the event, and the inclusion of an email address will send the event on to this account. Default is [from]."
                  },
                  "status": {
                    "type": "string",
                    "description": "The initial status of the SMTP user, one of ['allowed', 'blocked', 'sandbox'], defaults to 'allowed'",
                    "default": "allowed"
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
            "description": "SMTP User added",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "1d95eb4c-63c2-11ed-a771-f23c9216ce11",
                      "data": {
                        "results": [
                          {
                            "username": "test@example.com",
                            "email_password": "aklkweiyasdaf",
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
                              "username",
                              "sending_allowed",
                              "custom_ratelimit"
                            ],
                            "properties": {
                              "comments": {
                                "type": "string",
                                "example": "Comment explaining how amazing this Test person is"
                              },
                              "username": {
                                "type": "string",
                                "example": "smtpuser@example.com"
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
                                "description": "The default limit of emails this SMTP user can send in the period specified in <code>default_ratelimit_period</code>. <strong>Note:</strong> Used if <code>custom_ratelimit</code> is false."
                              },
                              "default_ratelimit_period": {
                                "type": "string",
                                "example": "unlimited",
                                "description": "The default period for which this SMTP user will be limited to the number of emails specified in <code>default_ratelimit_value</code>.<br><br><strong>Syntax:</strong> \"\\<n\\> [hour[s]|day[s]|week[s]|month[s]] [hh:mm:ss]\".<br><br><strong>Examples: </strong> \"0:30:00\", \"1 hour\", \"2 days\", \"3 months\", \"4 months 5:00:00\".<br><br><strong>Note:</strong> Used if <code>custom_ratelimit</code> is false."
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