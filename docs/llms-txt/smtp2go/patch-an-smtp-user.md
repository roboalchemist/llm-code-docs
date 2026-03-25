# Source: https://developers.smtp2go.com/reference/patch-an-smtp-user.md

# Patch an SMTP user

Patch an existing SMTP user ignoring missing properties

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
    "/users/smtp/edit": {
      "patch": {
        "tags": [
          "SMTP USERS"
        ],
        "summary": "Patch an SMTP user",
        "description": "Patch an existing SMTP user ignoring missing properties",
        "operationId": "patch-smtp-user",
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
                    "description": "A valid username of your existing SMTP User that you wish to edit",
                    "example": "my_user"
                  },
                  "email_password": {
                    "type": "string",
                    "description": "A valid SMTP2GO password for your existing SMTP User. <br><br>Must have an entropy of at least 64 bits. <a target='_blank' href='https://www.calculator.net/password-generator.html'>Consider using a password generator</a> or leave blank for an auto generated value."
                  },
                  "description": {
                    "type": "string",
                    "description": "A comment or description of the SMTP user",
                    "example": "test smtp user"
                  },
                  "custom_ratelimit": {
                    "type": "boolean",
                    "description": "If true, a custom rate limit will be enabled for this user, and defined by the <code>custom_ratelimit_value</code> and <code>custom_ratelimit_period</code>."
                  },
                  "custom_ratelimit_value": {
                    "type": "integer",
                    "description": "If passed, defines the limit of emails this user can send in the period specified in <code>custom_ratelimit_period</code>.<br><br><strong>Note:</strong> Only stores this value if <code>custom_ratelimit</code> is true."
                  },
                  "custom_ratelimit_period": {
                    "type": "string",
                    "example": "0:30:00",
                    "description": "If passed, defines the period for which this user will be limited to the number of emails specified in <code>custom_ratelimit_value</code>.<br><br><strong>Syntax:</strong> \"\\<n\\> [hour[s]|day[s]|week[s]|month[s]] [hh:mm:ss]\".<br><br><strong>Examples: </strong> \"0:30:00\", \"1 hour\", \"2 days\", \"3 months\", \"4 months 5:00:00\".<br><br><strong>Note:</strong> Only stores this value if <code>custom_ratelimit</code> is true."
                  },
                  "ip_pool": {
                    "type": "integer",
                    "description": "If passed, any emails sent with this API key will use dedicated IP's in this IP Pool, This value can be found on the <code>/v3/dedicated_ips/view</code> endpoint.",
                    "example": 1234
                  },
                  "feedback_enabled": {
                    "type": "boolean",
                    "description": "If true, custom feedback via the unsubscribe footer will be enabled and defined by the below settings.",
                    "default": null
                  },
                  "feedback_html": {
                    "type": "string",
                    "description": "The HTML content to insert into the custom feedback email body via the unsubscribe footer.<br><br><strong>System Variables (Only available here):</strong><ul><li>Unsubscribe URL = %%UNSUBSCRIBE%% </li><li>Email address = %%EMAIL%%</li></ul>",
                    "example": "test_html",
                    "default": null
                  },
                  "feedback_text": {
                    "type": "string",
                    "description": "The text content to insert into the custom feedback email body via the unsubscribe footer.<br><br><strong>System Variables (Only available here):</strong><ul><li>Unsubscribe URL = %%UNSUBSCRIBE%% </li><li>Email address = %%EMAIL%%</li></ul>",
                    "example": "test_text",
                    "default": null
                  },
                  "open_tracking_enabled": {
                    "type": "boolean",
                    "description": "If true, open tracking will be enabled for this SMTP user.",
                    "default": null
                  },
                  "click_tracking_enabled": {
                    "type": "boolean",
                    "description": "If true, click tracking will be enabled for this SMTP user.",
                    "default": null
                  },
                  "archive_enabled": {
                    "type": "boolean",
                    "description": "If true, archiving (available on paid plans) will be enabled for this SMTP user.",
                    "default": null
                  },
                  "audit_email": {
                    "type": "string",
                    "description": "If passed, this email will be BCC'd on all emails sent by this SMTP user."
                  },
                  "bounce_notifications": {
                    "type": "string",
                    "description": "If passed, will control how bounce notifications are handled. Must be one of [from, drop, or a valid email address]. [from] will return the email to sender, [drop] will discard the event, and the inclusion of an email address will send the event on to this account.",
                    "default": null
                  },
                  "status": {
                    "type": "string",
                    "description": "The initial status of the SMTP user, one of ['allowed', 'blocked', 'sandbox'].",
                    "default": null
                  },
                  "subaccount_id": {
                    "type": "string",
                    "description": "If you wish to make this API call on behalf of a subaccount then include its unique ID here."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully patched SMTP user",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": {
                      "request_id": "f3e50113-deb2-4e54-9675-2ea497c3732e",
                      "data": [
                        {
                          "username": "my_user",
                          "description": "test smtp user",
                          "feedback_enabled": true,
                          "feedback_html": "test_html",
                          "feedback_text": "test_text",
                          "ippool": 1234,
                          "bounce_notifications": "from",
                          "status": "allowed"
                        }
                      ]
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "required": [
                    "data",
                    "request_id"
                  ],
                  "properties": {
                    "data": {
                      "type": "array",
                      "description": "An array of SMTP user results",
                      "items": {
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
                            "properties": {
                              "username": {
                                "type": "string",
                                "example": "username",
                                "description": "The username of the SMTP user"
                              },
                              "description": {
                                "type": "string",
                                "description": "A comment or description of the SMTP user."
                              },
                              "custom_rate_limit": {
                                "type": "boolean",
                                "example": true,
                                "default": false,
                                "description": "If enabled will use the values of <code>custom_ratelimit_value</code> and <code>custom_ratelimit_period</code> for rate limiting."
                              },
                              "custom_ratelimit_value": {
                                "type": "integer",
                                "example": 123,
                                "description": "If passed, defines the limit of emails this SMTP user can send in the period specified in <code>custom_ratelimit_period</code>."
                              },
                              "custom_ratelimit_period": {
                                "type": "string",
                                "example": "0:30:00",
                                "description": "If passed, defines the period for which this user will be limited to the number of emails specified in <code>custom_ratelimit_value</code>.<br><br><strong>Syntax:</strong> \"\\<n\\> [hour[s]|day[s]|week[s]|month[s]] [hh:mm:ss]\".<br><br><strong>Examples: </strong> \"0:30:00\", \"1 hour\", \"2 days\", \"3 months\", \"4 months 5:00:00\".<br><br><strong>Note:</strong> Only stores this value if <code>custom_ratelimit</code> is true."
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
                              "feedback_enabled": {
                                "type": "boolean",
                                "description": "If true, custom feedback via the unsubscribe footer will be enabled and defined by the below settings.",
                                "default": false
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
                                "description": "If true, open tracking will be enabled for this SMTP user.",
                                "default": false
                              },
                              "click_tracking_enabled": {
                                "type": "boolean",
                                "description": "If true, click tracking will be enabled for this SMTP user.",
                                "default": false
                              },
                              "archive_enabled": {
                                "type": "boolean",
                                "description": "If true, archiving (available on paid plans) will be enabled for this SMTP user.",
                                "default": false
                              },
                              "audit_email": {
                                "type": "string",
                                "description": "If passed, this email will be BCC'd on all emails sent by this SMTP user."
                              },
                              "bounce_notifications": {
                                "type": "string",
                                "description": "If passed, will control how bounce notifications are handled. Must be one of [from, drop, or a valid email address]. [from] will return the email to sender, [drop] will discard the event, and the inclusion of an email address will send the event on to this account.",
                                "default": "from"
                              },
                              "status": {
                                "type": "string",
                                "description": "The initial status of the SMTP user, one of ['allowed', 'blocked', 'sandbox'].",
                                "default": "allowed"
                              }
                            }
                          }
                        }
                      }
                    },
                    "request_id": {
                      "type": "string",
                      "example": "4b661d88-6b2d-11eb-8bb3-f23c92bb31d2"
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