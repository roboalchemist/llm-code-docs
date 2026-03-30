# Source: https://developers.smtp2go.com/reference/view-sent-emails.md

# View and search sent emails

Retrieve a list of up to 5,000 sent emails matching the supplied parameters.<br><br>The filter_query field can be used to create complex filters to make your searching more efficient. Find full details in the Email and Email Archive Guide.<br><br><strong>Note:<strong> Allow around two minutes after delivery for recently sent emails to be included in a search result.<br /><br />This endpoint is deprecated and will not be accessible in future API versions. Please use the <a href='https://developers.smtp2go.com/reference/search-activity'>Activity Search</a> endpoint instead.<i>This endpoint is rate-limited to 20 requests per minute.</i>

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
    "/email/search": {
      "post": {
        "tags": [
          "EMAILS"
        ],
        "summary": "View and search sent emails",
        "description": "Retrieve a list of up to 5,000 sent emails matching the supplied parameters.<br><br>The filter_query field can be used to create complex filters to make your searching more efficient. Find full details in the Email and Email Archive Guide.<br><br><strong>Note:<strong> Allow around two minutes after delivery for recently sent emails to be included in a search result.<br /><br />This endpoint is deprecated and will not be accessible in future API versions. Please use the <a href='https://developers.smtp2go.com/reference/search-activity'>Activity Search</a> endpoint instead.<i>This endpoint is rate-limited to 20 requests per minute.</i>",
        "operationId": "view-sent-emails",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime. Results will be inclusive of this value. Timezone is UTC. Defaults to current date at midnight."
                  },
                  "end_date": {
                    "type": "string",
                    "description": "ISO-8601 formatted datetime. Results will be inclusive of this value. Timezone is UTC. Defaults to current time."
                  },
                  "limit": {
                    "type": "integer",
                    "description": "The maximum number of emails to return. Enter an integer between 1 and 5,000. Defaults to 5,000.",
                    "default": 5000,
                    "format": "int32"
                  },
                  "status_counts": {
                    "type": "boolean",
                    "description": "If true, will return an object with counts of each unique email status",
                    "default": false
                  },
                  "opened_only": {
                    "type": "boolean",
                    "description": "If true, will return emails that have been opened by at least one recipient.<br><br><strong>Note:</strong> Only returns information for emails sent from suitable accounts with Open Tracking enabled.  See more info at <a href=\"https://support.smtp2go.com/hc/en-gb/articles/360003124714\">Open Tracking</a>",
                    "default": false
                  },
                  "clicked_only": {
                    "type": "boolean",
                    "description": "If true, will return emails that have had a link clicked by at least one recipient.<br><br><strong>Note:</strong> Only returns information for emails sent from suitable accounts with Click Tracking enabled.  See more info at <a href=\"https://support.smtp2go.com/hc/en-gb/articles/900002237106-Click-Tracking\">Click Tracking</a>",
                    "default": false
                  },
                  "ignore_case": {
                    "type": "boolean",
                    "description": "If true, all string searches will be case insensitive",
                    "default": false
                  },
                  "filter_query": {
                    "type": "string",
                    "description": "If passed, will return results filtered by these search parameters. The query format is documented below",
                    "default": "null"
                  },
                  "email_id": {
                    "type": "array",
                    "description": "If passed, will only return emails with an ID contained within this array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "username": {
                    "type": "string",
                    "description": "If passed, will only return emails sent by this user"
                  },
                  "headers": {
                    "type": "array",
                    "description": "If passed, will return the specified email header values",
                    "default": [
                      "[]"
                    ],
                    "items": {
                      "type": "string"
                    }
                  },
                  "continue_token": {
                    "type": "string",
                    "description": "If passed, the resulting query will paginate from the previous query"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "List of sent emails",
            "content": {
              "application/json": {
                "examples": {
                  "Example": {
                    "value": {
                      "request_id": "84fe4a7e-1487-4ddf-92cb-4c6f8e6b2070",
                      "data": {
                        "count": 1,
                        "emails": [
                          {
                            "sender": "test@example.com",
                            "email_id": "1u0SwL-B9zBpi9ffUq-JAB2",
                            "smtpcode": 250,
                            "response": "250 2.0.0 OK 1466989602 87si22895035pfn.73 - gsmtp",
                            "process_status": "completed",
                            "host": "gmail-smtp-in.l.google.com [74.125.200.27]",
                            "recipient": "test2@example.com",
                            "delivered_at": "2016-06-27 01:06:42.668336+00:00",
                            "opens": [
                              {
                                "user_agent": "Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36",
                                "opened_at": "2018-04-02 19:26:53.010729+00:00",
                                "read_secs": "10",
                                "recipient": "test2@example.com",
                                "ip_address": "x.x.x.x"
                              }
                            ],
                            "total_opens": 1,
                            "status": "delivered",
                            "email_ts": "2016-06-27 01:06:37.039400+00:00"
                          }
                        ],
                        "continue_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0Njc4NTY4ODEsImRhdCI6eyJvZmYiOjUsInFpZCI6MX0sImlzcyI6ImFwaS5zbXRwMmdvLmNvbSIsImlhdCI6MTQ2Nzg1NjU4MX0.Pgl5rl7hsgFrVIa9TTFDyi7Y8o_mCHDPE227qNINQd3_rZwgfnPAhDRmsyQMGqQDJHfr5NNF_V9cPTpWNkXikUUDFaEHoXnFkbDxAqtb6n40KA3pVjG1D8QDKTjONGBqDs3zOujUSb_CR9oYkQXnnFRfy2K-ZXoJuMpqIB3A1gbg3KdZCLjzKHi0hkvIUBCnkERksq9pdAB15dnAkkDliEUHOB2SpA05brBEHTRF_H7az9NkrVm1STPX7x3hq5Qg6gZPWCuwpNKpdP-MnHhThmq67Y8LVL7kmR4dKkON1uamf4UxDK3BK8hef7fty1x1K9BSa8ils5BeolV_2BU0aw"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "84fe4a7e-1487-4ddf-92cb-4c6f8e6b2070"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "count": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "emails": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "sender": {
                                "type": "string",
                                "example": "test@example.com"
                              },
                              "email_id": {
                                "type": "string",
                                "example": "1u0SwL-B9zBpi9ffUq-JAB2"
                              },
                              "smtpcode": {
                                "type": "integer",
                                "example": 250,
                                "default": 0
                              },
                              "response": {
                                "type": "string",
                                "example": "250 2.0.0 OK 1466989602 87si22895035pfn.73 - gsmtp"
                              },
                              "process_status": {
                                "type": "string",
                                "example": "completed",
                                "description": "The current status in the deliver process. Can be completed, processing, or rejected."
                              },
                              "host": {
                                "type": "string",
                                "example": "gmail-smtp-in.l.google.com [74.125.200.27]"
                              },
                              "recipient": {
                                "type": "string",
                                "example": "test2@example.com"
                              },
                              "delivered_at": {
                                "type": "string",
                                "example": "2016-06-27 01:06:42.668336+00:00"
                              },
                              "opens": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "user_agent": {
                                      "type": "string",
                                      "example": "Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36"
                                    },
                                    "opened_at": {
                                      "type": "string",
                                      "example": "2018-04-02 19:26:53.010729+00:00"
                                    },
                                    "read_secs": {
                                      "type": "string",
                                      "example": "10"
                                    },
                                    "recipient": {
                                      "type": "string",
                                      "example": "test2@example.com"
                                    },
                                    "ip_address": {
                                      "type": "string",
                                      "example": "x.x.x.x"
                                    }
                                  }
                                }
                              },
                              "total_opens": {
                                "type": "integer",
                                "example": 1,
                                "default": 0
                              },
                              "status": {
                                "type": "string",
                                "example": "delivered",
                                "description": "The status of the email, can be any of [processed, bounce, delivered, unsubscribed, spam, deferred, opened, refused, cancelled]"
                              },
                              "email_ts": {
                                "type": "string",
                                "example": "2016-06-27 01:06:37.039400+00:00"
                              }
                            }
                          }
                        },
                        "continue_token": {
                          "type": "string",
                          "example": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0Njc4NTY4ODEsImRhdCI6eyJvZmYiOjUsInFpZCI6MX0sImlzcyI6ImFwaS5zbXRwMmdvLmNvbSIsImlhdCI6MTQ2Nzg1NjU4MX0.Pgl5rl7hsgFrVIa9TTFDyi7Y8o_mCHDPE227qNINQd3_rZwgfnPAhDRmsyQMGqQDJHfr5NNF_V9cPTpWNkXikUUDFaEHoXnFkbDxAqtb6n40KA3pVjG1D8QDKTjONGBqDs3zOujUSb_CR9oYkQXnnFRfy2K-ZXoJuMpqIB3A1gbg3KdZCLjzKHi0hkvIUBCnkERksq9pdAB15dnAkkDliEUHOB2SpA05brBEHTRF_H7az9NkrVm1STPX7x3hq5Qg6gZPWCuwpNKpdP-MnHhThmq67Y8LVL7kmR4dKkON1uamf4UxDK3BK8hef7fty1x1K9BSa8ils5BeolV_2BU0aw"
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
                  "Example": {
                    "value": {
                      "request_id": "22e5acba-43bf-11e6-ae42-408d5cce2644",
                      "data": {
                        "error_code": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED",
                        "error": "You do not have permission to access this API endpoint"
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
                        "error_code": {
                          "type": "string",
                          "example": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
                        },
                        "error": {
                          "type": "string",
                          "example": "You do not have permission to access this API endpoint"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": true
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