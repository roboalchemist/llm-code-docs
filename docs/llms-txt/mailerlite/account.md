# Source: https://developers-classic.mailerlite.com/reference/account.md

# Account

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "V2 production",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.mailerlite.com/api/v2"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "X-MailerLite-ApiKey",
        "in": "header",
        "x-default": "your api key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/me": {
      "get": {
        "summary": "Account",
        "description": "",
        "operationId": "account",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"account\": {\n        \"email\": \"dummy@mailerlite.com\",\n        \"from\": \"dummy@mailerlite.com\",\n        \"id\": 1,\n        \"name\": \"Dummy\",\n        \"subdomain\": \"dummy\",\n        \"timezone\": {\n            \"gmt\": \"+02:00\",\n            \"id\": 101,\n            \"time\": 120,\n            \"timezone\": \"\",\n            \"title\": \"\"\n        }\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "account": {
                      "type": "object",
                      "properties": {
                        "email": {
                          "type": "string",
                          "example": "dummy@mailerlite.com"
                        },
                        "from": {
                          "type": "string",
                          "example": "dummy@mailerlite.com"
                        },
                        "id": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "name": {
                          "type": "string",
                          "example": "Dummy"
                        },
                        "subdomain": {
                          "type": "string",
                          "example": "dummy"
                        },
                        "timezone": {
                          "type": "object",
                          "properties": {
                            "gmt": {
                              "type": "string",
                              "example": "+02:00"
                            },
                            "id": {
                              "type": "integer",
                              "example": 101,
                              "default": 0
                            },
                            "time": {
                              "type": "integer",
                              "example": 120,
                              "default": 0
                            },
                            "timezone": {
                              "type": "string",
                              "example": ""
                            },
                            "title": {
                              "type": "string",
                              "example": ""
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
          "401": {
            "description": "401",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": {\n        \"code\": 302,\n        \"message\": \"API-Key Unauthorized\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "code": {
                          "type": "integer",
                          "example": 302,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "API-Key Unauthorized"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl -v https://api.mailerlite.com/api/v2/me \\\n-H \"X-MailerLite-ApiKey: apikey\""
            }
          ],
          "samples-languages": [
            "curl"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [
      {
        "key": "X-MailerLite-ApiDocs",
        "value": "true"
      }
    ],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true,
  "_id": "58b53b141065f9c438aa1afe:590c1b2ea160210f00b64318"
}
```