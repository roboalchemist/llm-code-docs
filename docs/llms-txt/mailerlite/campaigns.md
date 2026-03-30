# Source: https://developers-classic.mailerlite.com/reference/campaigns.md

# /campaigns

Create campaign where you will use your custom HTML template [Rate limited]

[block:callout]
{
  "type": "info",
  "title": "Email type of created campaign",
  "body": "Campaigns that are created using this endpoint require your own custom HTML templates to be added via API using /campaigns/:id/content endpoint or directly in MailerLite application."
}
[/block]

Here is more details about `ab_settings` object.

**All fields are required!**

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`values`",
    "0-1": "*array*",
    "0-2": "Must contain two values. It depends on `send_type`.\n\nFor example, if `send_type` equals to `sender` these values are used as sender names for AB test. \n\nIf `send_type` equals to `subject` these values are used as subjects for AB test.",
    "1-2": "Available values:\n\n- `sender`\n- `subject`",
    "2-2": "It defines how winner will be selected.\n\nAvailable values:\n\n- `opens`\n- `clicks`",
    "3-2": "It defines how long AB test is active.\n\nPay attention that this is only a number and type is defined as `winner_after_type`",
    "4-2": "Available values:\n\n- `d` - days\n- `h` - hours",
    "5-2": "It defines size of every test group in percents equally.\n\nAvailable range: 5-25",
    "1-0": "`send_type`",
    "2-0": "`ab_win_type`",
    "3-0": "`winner_after`",
    "4-0": "`winner_after_type`",
    "5-0": "`split_part`",
    "1-1": "*string*",
    "2-1": "*string*",
    "3-1": "*integer*",
    "4-1": "*string*",
    "5-1": "*integer*"
  },
  "cols": 3,
  "rows": 6
}
[/block]

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
    "/campaigns": {
      "post": {
        "summary": "/campaigns",
        "description": "Create campaign where you will use your custom HTML template [Rate limited]",
        "operationId": "campaigns",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "type",
                  "name",
                  "groups",
                  "segments"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "description": "Type of campaign. Available values: regular, ab.",
                    "default": "null"
                  },
                  "name": {
                    "type": "string",
                    "description": "The internal name for the campaign",
                    "default": "campaign name"
                  },
                  "groups": {
                    "type": "array",
                    "description": "IDs of groups. Required if segments are not specified.",
                    "default": [
                      null
                    ],
                    "items": {
                      "type": "integer",
                      "format": "int32"
                    }
                  },
                  "segments": {
                    "type": "array",
                    "description": "IDs of segments. Required if groups are not specified. If specified, groups are ignored. If you're using legacy subscriber management, this parameter will be ignored.",
                    "default": [
                      null
                    ],
                    "items": {
                      "type": "integer",
                      "format": "int32"
                    }
                  },
                  "subject": {
                    "type": "string",
                    "description": "Mail subject. Required if campaign type is regular."
                  },
                  "from": {
                    "type": "string",
                    "description": "Email of sender",
                    "default": "Account's default sender"
                  },
                  "from_name": {
                    "type": "string",
                    "description": "Name of sender",
                    "default": "Account's default sender"
                  },
                  "language": {
                    "type": "string",
                    "description": "Available languages and its code's: https://developers-classic.mailerlite.com/reference#language",
                    "default": "Account's default language code"
                  },
                  "ab_settings": {
                    "type": "object",
                    "description": "Required if campaign type is ab. More details are below.",
                    "properties": {}
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
                "examples": {
                  "Result": {
                    "value": "{\n  \"campaign_type\":\"regular\",\n  \"date\":\"2016-05-18 13:03:47\",\n  \"account_id\":441087,\n  \"id\":3043021,\n  \"mail_id\":3529037,\n  \"options\": {\n    \"current_step\":\"step3\",\n    \"send_type\":\"regular\",\n    \"campaign_type\":\"regular\",\n    \"date\":\"2016-05-18 13:03:47\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "campaign_type": {
                      "type": "string",
                      "example": "regular"
                    },
                    "date": {
                      "type": "string",
                      "example": "2016-05-18 13:03:47"
                    },
                    "account_id": {
                      "type": "integer",
                      "example": 441087,
                      "default": 0
                    },
                    "id": {
                      "type": "integer",
                      "example": 3043021,
                      "default": 0
                    },
                    "mail_id": {
                      "type": "integer",
                      "example": 3529037,
                      "default": 0
                    },
                    "options": {
                      "type": "object",
                      "properties": {
                        "current_step": {
                          "type": "string",
                          "example": "step3"
                        },
                        "send_type": {
                          "type": "string",
                          "example": "regular"
                        },
                        "campaign_type": {
                          "type": "string",
                          "example": "regular"
                        },
                        "date": {
                          "type": "string",
                          "example": "2016-05-18 13:03:47"
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
                    "value": "{\n  \"error\":{\n    \"code\":123,\n    \"message\":\"Array[ab_settings]: This field is missing. (code 2fa2158c-2a7f-484b-98aa-975522539ff8)\"\n  }\n}"
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
                          "example": 123,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "Array[ab_settings]: This field is missing. (code 2fa2158c-2a7f-484b-98aa-975522539ff8)"
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
              "code": "curl -X POST \"https://api.mailerlite.com/api/v2/campaigns\" \\\n-d '{\n    \"name\": \"campaign name\",\n    \"groups\": [2984475, 3237221],\n    \"type\": \"ab\",\n    \"ab_settings\": {\n        \"send_type\": \"subject\",\n        \"values\": [\"Email subject A\", \"Email subject B\"],\n        \"ab_win_type\": \"opens\",\n        \"winner_after\": 1,\n        \"winner_after_type\": \"h\",\n        \"split_part\": \"10\"\n    }}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\" \\",
              "name": "cURL - AB campaign"
            },
            {
              "language": "curl",
              "code": "curl -X POST \"https://api.mailerlite.com/api/v2/campaigns\" \\\n-d '{\n    \"subject\": \"Regular campaign subject\",\n    \"name\": \"campaign name\",\n    \"groups\": [2984475, 3237221],\n    \"type\": \"regular\"\n}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\" \\",
              "name": "cURL - Regular campaign"
            },
            {
              "language": "php",
              "code": "<?php\n$campaignsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->campaigns();\n\n$campaignData = [\n  'subject' => 'Regular Campaign Subject',\n  'type' => 'regular',\n  'groups' => [2984475, 3237221]\n];\n\n$campaign = $campaignsApi->create($campaignData); // returns created $campaign object"
            }
          ],
          "samples-languages": [
            "curl",
            "php"
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
  "_id": "58b53b141065f9c438aa1afe:5739cb580295e63200072b38"
}
```