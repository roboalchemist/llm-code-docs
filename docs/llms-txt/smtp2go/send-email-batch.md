# Source: https://developers.smtp2go.com/reference/send-email-batch.md

# Send a batch of emails

Send a batch of emails

This endpoint can send/schedule a batch of up to 1,000 emails. The format of the email object is the same
as the `/email/send` endpoint.

*Note - this endpoint queues emails by default, a total of 50,000 queued emails can be queued at any one time.*

An example of using templates when creating a batch which is useful for mailing list types sending.

```json
REQUEST
{
  "api_key": "<ommitted>",
  "emails": [
    {
      "to": "<recipient1>", 
      "sender": "<sender>", 
      "template_id": "tpl-001", 
      "template_data": {
        "name": "Recipient 1"
      }
    },
    {
      "to": "<recipient2>", 
      "sender": "<sender>", 
      "template_id": "tpl-001", 
      "template_data": {
        "name": "Recipient 2"
      }
    },
    {
      "to": "<recipient3>", 
      "sender": "<sender>", 
      "template_id": "tpl-001", 
      "template_data": {
        "name": "Recipient 3"
      },
      "schedule": "2026-01-01 12:00:00"
    },
    {
      "to": "<recipient4>", 
      "sender": "<sender>", 
      "template_id": "tpl-001", 
      "template_data": {
        "name": "Recipient 4"
      },
      "schedule": "2026-01-01 12:00:00"
    }
  ]
}

RESPONSE
{
  "request_id": "aa253464-0bd0-467a-b24b-6159dcd7be60",
  "data": [
    {
      "email_id": "123456-1234-12"
    },
    {
      "email_id": "123456-1234-13"
    },
    {
      "schedule_id": "789db207-5aba-4895-801b-4ebf1843721e"
    },
    {
      "schedule_id": "4cecd7a5-cb34-4eaa-9277-d2fcbea8d41a"
    }
  ]
}
```

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
    "/email/batch": {
      "post": {
        "tags": [
          "EMAILS"
        ],
        "summary": "Send a batch of emails",
        "description": "Send a batch of emails",
        "operationId": "send-email-batch",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "emails"
                ],
                "example": {
                  "emails": [
                    {
                      "to": [
                        "Jane Jones <jane@example.com>"
                      ],
                      "sender": "John Smith <john@example.com>",
                      "subject": "My Test Email #1",
                      "html_body": "<h1>Test <img src=\"cid:mypicture.jpg\" /></h1>",
                      "text_body": "Test",
                      "attachments": [
                        {
                          "filename": "report.pdf",
                          "mimetype": "application/pdf",
                          "fileblob": "bm90IGFjdHVhbGx5IGEgcGRm..."
                        }
                      ],
                      "inlines": [
                        {
                          "filename": "mypicture.jpg",
                          "mimetype": "image/jpeg",
                          "url": "https://myserver.com/mypicture.jpg"
                        }
                      ]
                    },
                    {
                      "to": [
                        "Jane Jones <jane@example.com>"
                      ],
                      "sender": "John Smith <john@example.com>",
                      "subject": "My Test Email #2",
                      "html_body": "<h1>Test <img src=\"cid:mypicture.jpg\" /></h1>",
                      "text_body": "Test",
                      "attachments": [
                        {
                          "filename": "report.pdf",
                          "mimetype": "application/pdf",
                          "fileblob": "bm90IGFjdHVhbGx5IGEgcGRm..."
                        }
                      ],
                      "inlines": [
                        {
                          "filename": "mypicture.jpg",
                          "mimetype": "image/jpeg",
                          "url": "https://myserver.com/mypicture.jpg"
                        }
                      ],
                      "schedule": "2026-01-01 12:00:00 +1300"
                    }
                  ]
                },
                "properties": {
                  "emails": {
                    "type": "array",
                    "description": "An array of email objects to schedule",
                    "items": {
                      "type": "object",
                      "required": [
                        "sender",
                        "to",
                        "subject"
                      ],
                      "properties": {
                        "sender": {
                          "type": "string",
                          "description": "The name and email address to send from, in the format `Name <name@example.com>`"
                        },
                        "to": {
                          "type": "array",
                          "description": "An array of names and email addresses (up to 100) to send to, in the format `Name <name@example.com>`",
                          "items": {
                            "type": "string"
                          }
                        },
                        "cc": {
                          "type": "array",
                          "description": "An array of names and email addresses (up to 100) to CC, in the format `Name <name@example.com>`",
                          "items": {
                            "type": "string"
                          }
                        },
                        "bcc": {
                          "type": "array",
                          "description": "An array of names and email addresses (up to 100) to BCC, in the format `Name <name@example.com>`",
                          "items": {
                            "type": "string"
                          }
                        },
                        "subject": {
                          "type": "string",
                          "description": "The subject of the email to be sent"
                        },
                        "html_body": {
                          "type": "string",
                          "description": "A HTML encoded email body. Either html_body or text_body is required if template_id is not passed.<br><br> <strong>Warning:</strong><ul><li>To correctly track clicking of URLs you must:  <ul><li>Enable click tracking for the API key</li>  <li>Insert a full anchor HTML element (not just the URL)</li> <li>Include \"https://\" at the start of the HREF property</li> </ul></ul>"
                        },
                        "text_body": {
                          "type": "string",
                          "description": "A plain text email body. Either html_body or text_body is required if template_id is not passed"
                        },
                        "custom_headers": {
                          "type": "array",
                          "description": "An array of custom header objects to be applied to the email. For example, a `Reply-To` email can be specified here, with header `Reply-To` and value `name@example.com`. For sending purposes the following headers are not allowed `Content-Type`, `Content-Transfer-Encoding` and `MIME-Version`.",
                          "items": {
                            "properties": {
                              "header": {
                                "type": "string",
                                "description": "Custom header to add to the email"
                              },
                              "value": {
                                "type": "string",
                                "description": "Custom header value to set"
                              }
                            },
                            "required": [
                              "header",
                              "value"
                            ],
                            "type": "object"
                          }
                        },
                        "attachments": {
                          "type": "array",
                          "description": "An array of attachment objects to be attached to the email",
                          "items": {
                            "properties": {
                              "filename": {
                                "type": "string",
                                "description": "The filename to use for this binary data"
                              },
                              "fileblob": {
                                "type": "string",
                                "description": "The Base64 encoded binary data of the file. Required if no url is specified."
                              },
                              "mimetype": {
                                "type": "string",
                                "description": "The mimetype of the binary data"
                              },
                              "url": {
                                "type": "string",
                                "description": "A URL pointing to the attachment data. The data is directly retrieved by our system, and cached for fast re-use for 24 hours. Required if no fileblob is specified"
                              }
                            },
                            "required": [
                              "filename"
                            ],
                            "type": "object"
                          }
                        },
                        "inlines": {
                          "type": "array",
                          "description": "An array of images to be inlined into the email. Use an image in content as `<img src=\"cid:filename\" />`",
                          "items": {
                            "properties": {
                              "filename": {
                                "type": "string",
                                "description": "The filename to use for this binary data"
                              },
                              "fileblob": {
                                "type": "string",
                                "description": "The Base64 encoded binary data of the file. Required if no url is specified."
                              },
                              "mimetype": {
                                "type": "string",
                                "description": "The mimetype of the binary data"
                              },
                              "url": {
                                "type": "string",
                                "description": "A URL pointing to the attachment data. The data is directly retrieved by our system, and cached for fast re-use for 24 hours. Required if no fileblob is specified"
                              }
                            },
                            "required": [
                              "filename"
                            ],
                            "type": "object"
                          }
                        },
                        "template_id": {
                          "type": "string",
                          "description": "The ID of the template you wish to use"
                        },
                        "template_data": {
                          "type": "string",
                          "description": "When a template_id is provided, include the pass-through values in the format `{\"variable1\": \"value1\", \"variable2\": \"value2\"}`",
                          "format": "json"
                        },
                        "schedule": {
                          "type": "string",
                          "description": "A timestamp that when passed allows you to schedule an email for sending. Must be in the future and within the next 3 days.<br />The api response will include a `schedule_id` property which can then be used alongside webhooks (An `X-Smtp2go-Schedule-Id` header is added to the sent email corresponds to this id)"
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
            "description": "An array of `email_id/schedule_id` values coinciding with the same order as the request payload.",
            "content": {
              "application/json": {
                "examples": {
                  "Example": {
                    "value": {
                      "request_id": "aa253464-0bd0-467a-b24b-6159dcd7be60",
                      "data": [
                        {
                          "email_id": "123456-1234-12"
                        },
                        {
                          "schedule_id": "188262b6-f6cc-4c98-bbe6-84c39d1c0ef4"
                        }
                      ]
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "request_id": {
                      "type": "string",
                      "example": "aa253464-0bd0-467a-b24b-6159dcd7be60"
                    },
                    "data": {
                      "type": "array",
                      "description": "An array of `email_id/schedule_id` information in the same order as the payload.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "email_id": {
                            "type": "string",
                            "description": "The email_id of the email"
                          },
                          "schedule_id": {
                            "type": "string",
                            "description": "The schedule_id of the email (if `schedule` was passed, used to search/remove scheduled emails)"
                          }
                        }
                      },
                      "example": [
                        {
                          "email_id": "123456-1234-12"
                        },
                        {
                          "schedule_id": "188262b6-f6cc-4c98-bbe6-84c39d1c0ef4"
                        },
                        {
                          "schedule_id": "789db207-5aba-4895-801b-4ebf1843721e"
                        }
                      ]
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