# Source: https://developers.activecampaign.com/reference/list-whatsapp-templates.md

# List WhatsApp Templates

Lists WhatsApp Templates. You can search with the `name` and `status` fields using the `?seach=my-template-name` query parameter.

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "WhatsApp API",
    "version": "1.0.0",
    "description": "All of the below API endpoints require API key authentication, get your token at https://app.hilos.io/dev/api-keys.\n\nTo use this token, send with every request an `Authorization: Token <your token>` header.\n\nProduction API server is located at api.hilos.io using HTTPS.\n\nNo versioning info is required for now."
  },
  "paths": {
    "/channel/whatsapp/channels/whatsapp/template": {
      "get": {
        "operationId": "List WhatsApp Templates",
        "description": "Lists WhatsApp Templates. You can search with the `name` and `status` fields using the `?seach=my-template-name` query parameter.",
        "summary": "List WhatsApp Templates",
        "parameters": [
          {
            "in": "query",
            "name": "category",
            "schema": {
              "type": "string",
              "enum": [
                "ACCOUNT_UPDATE",
                "ALERT_UPDATE",
                "APPOINTMENT_UPDATE",
                "AUTHENTICATION",
                "AUTO_REPLY",
                "ISSUE_RESOLUTION",
                "MARKETING",
                "OTP",
                "PAYMENT_UPDATE",
                "PERSONAL_FINANCE_UPDATE",
                "RESERVATION_UPDATE",
                "SHIPPING_UPDATE",
                "TICKET_UPDATE",
                "TRANSACTIONAL",
                "TRANSPORTATION_UPDATE",
                "UTILITY"
              ]
            },
            "description": "* `ACCOUNT_UPDATE` - Account Update\n* `PAYMENT_UPDATE` - Payment Update\n* `PERSONAL_FINANCE_UPDATE` - Personal Finance Update\n* `SHIPPING_UPDATE` - Shipping Update\n* `RESERVATION_UPDATE` - Reservation Update\n* `ISSUE_RESOLUTION` - Issue Resolution\n* `APPOINTMENT_UPDATE` - Appointment Update\n* `TRANSPORTATION_UPDATE` - Transportation Update\n* `TICKET_UPDATE` - Ticket Update\n* `ALERT_UPDATE` - Alert Update\n* `AUTO_REPLY` - Auto Reply\n* `TRANSACTIONAL` - Transactional\n* `MARKETING` - Marketing\n* `OTP` - Otp\n* `AUTHENTICATION` - Authentication\n* `UTILITY` - Utility"
          },
          {
            "in": "query",
            "name": "category__in",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "description": "Multiple values may be separated by commas.",
            "explode": false,
            "style": "form"
          },
          {
            "in": "query",
            "name": "channel",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "channel__in",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "description": "Multiple values may be separated by commas.",
            "explode": false,
            "style": "form"
          },
          {
            "name": "ordering",
            "required": false,
            "in": "query",
            "description": "Which field to use when ordering the results.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "page",
            "required": false,
            "in": "query",
            "description": "A page number within the paginated result set.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "page_size",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "search",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "status",
            "schema": {
              "type": "string",
              "enum": [
                "approved",
                "deleted",
                "disabled",
                "draft",
                "in_appeal",
                "pending",
                "pending_deletion",
                "rejected",
                "submitted"
              ]
            },
            "description": "* `draft` - Draft\n* `approved` - Approved\n* `in_appeal` - In Appeal\n* `pending` - Pending\n* `rejected` - Rejected\n* `pending_deletion` - Pending Deletion\n* `deleted` - Deleted\n* `disabled` - Disabled\n* `submitted` - Submitted"
          },
          {
            "in": "query",
            "name": "status__in",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "description": "Multiple values may be separated by commas.",
            "explode": false,
            "style": "form"
          }
        ],
        "tags": [
          "Templates"
        ],
        "security": [
          {
            "tokenAuth": []
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedWhatsAppTemplateSimpleReadList"
                }
              }
            },
            "description": ""
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "CategoryEnum": {
        "enum": [
          "ACCOUNT_UPDATE",
          "PAYMENT_UPDATE",
          "PERSONAL_FINANCE_UPDATE",
          "SHIPPING_UPDATE",
          "RESERVATION_UPDATE",
          "ISSUE_RESOLUTION",
          "APPOINTMENT_UPDATE",
          "TRANSPORTATION_UPDATE",
          "TICKET_UPDATE",
          "ALERT_UPDATE",
          "AUTO_REPLY",
          "TRANSACTIONAL",
          "MARKETING",
          "OTP",
          "AUTHENTICATION",
          "UTILITY"
        ],
        "type": "string",
        "description": "* `ACCOUNT_UPDATE` - Account Update\n* `PAYMENT_UPDATE` - Payment Update\n* `PERSONAL_FINANCE_UPDATE` - Personal Finance Update\n* `SHIPPING_UPDATE` - Shipping Update\n* `RESERVATION_UPDATE` - Reservation Update\n* `ISSUE_RESOLUTION` - Issue Resolution\n* `APPOINTMENT_UPDATE` - Appointment Update\n* `TRANSPORTATION_UPDATE` - Transportation Update\n* `TICKET_UPDATE` - Ticket Update\n* `ALERT_UPDATE` - Alert Update\n* `AUTO_REPLY` - Auto Reply\n* `TRANSACTIONAL` - Transactional\n* `MARKETING` - Marketing\n* `OTP` - Otp\n* `AUTHENTICATION` - Authentication\n* `UTILITY` - Utility"
      },
      "ChannelProviderEnum": {
        "enum": [
          "META_CLOUD_API",
          "TECH_PROVIDER_CLOUD_API",
          "D360_CLOUD_API",
          "360DIALOG"
        ],
        "type": "string",
        "description": "* `META_CLOUD_API` - Meta Cloud Api\n* `TECH_PROVIDER_CLOUD_API` - Tech Provider Cloud Api\n* `D360_CLOUD_API` - D360 Cloud Api\n* `360DIALOG` - Dialog360"
      },
      "ChannelStatusEnum": {
        "enum": [
          "NEW",
          "ACTIVE",
          "INACTIVE"
        ],
        "type": "string",
        "description": "* `NEW` - New\n* `ACTIVE` - Active\n* `INACTIVE` - Inactive"
      },
      "ChannelTypeEnum": {
        "enum": [
          "WHATSAPP",
          "EMAIL",
          "INSTAGRAM",
          "FB_MESSENGER",
          "TELEGRAM",
          "SMS",
          "VOICE"
        ],
        "type": "string",
        "description": "* `WHATSAPP` - Whatsapp\n* `EMAIL` - Email\n* `INSTAGRAM` - Instagram\n* `FB_MESSENGER` - Fb Messenger\n* `TELEGRAM` - Telegram\n* `SMS` - Sms\n* `VOICE` - Voice"
      },
      "LanguageEnum": {
        "enum": [
          "af",
          "sq",
          "ar",
          "az",
          "bn",
          "bg",
          "ca",
          "zh_CN",
          "zh_HK",
          "zh_TW",
          "hr",
          "cs",
          "da",
          "nl",
          "en",
          "en_GB",
          "en_US",
          "et",
          "fil",
          "fi",
          "fr",
          "ka",
          "de",
          "el",
          "gu",
          "ha",
          "he",
          "hi",
          "hu",
          "id",
          "ga",
          "it",
          "ja",
          "kn",
          "kk",
          "rw_RW",
          "ko",
          "ky_KG",
          "lo",
          "lv",
          "lt",
          "mk",
          "ms",
          "ml",
          "mr",
          "nb",
          "fa",
          "pl",
          "pt_BR",
          "pt_PT",
          "pa",
          "ro",
          "ru",
          "sr",
          "sk",
          "sl",
          "es",
          "es_AR",
          "es_ES",
          "es_MX",
          "sw",
          "sv",
          "ta",
          "te",
          "th",
          "tr",
          "uk",
          "ur",
          "uz",
          "vi",
          "zu"
        ],
        "type": "string",
        "description": "* `af` - Afrikaans\n* `sq` - Albanian\n* `ar` - Arabic\n* `az` - Azerbaijani\n* `bn` - Bengali\n* `bg` - Bulgarian\n* `ca` - Catalan\n* `zh_CN` - Chinese (CHN)\n* `zh_HK` - Chinese (HKG)\n* `zh_TW` - Chinese (TAI)\n* `hr` - Croatian\n* `cs` - Czech\n* `da` - Danish\n* `nl` - Dutch\n* `en` - English\n* `en_GB` - English (UK)\n* `en_US` - English (US)\n* `et` - Estonian\n* `fil` - Filipino\n* `fi` - Finnish\n* `fr` - French\n* `ka` - Georgian\n* `de` - German\n* `el` - Greek\n* `gu` - Gujarati\n* `ha` - Hausa\n* `he` - Hebrew\n* `hi` - Hindi\n* `hu` - Hungarian\n* `id` - Indonesian\n* `ga` - Irish\n* `it` - Italian\n* `ja` - Japanese\n* `kn` - Kannada\n* `kk` - Kazakh\n* `rw_RW` - Kinyarwanda\n* `ko` - Korean\n* `ky_KG` - Kyrgyz (Kyrgyzstan)\n* `lo` - Lao\n* `lv` - Latvian\n* `lt` - Lithuanian\n* `mk` - Macedonian\n* `ms` - Malay\n* `ml` - Malayalam\n* `mr` - Marathi\n* `nb` - Norwegian\n* `fa` - Persian\n* `pl` - Polish\n* `pt_BR` - Portuguese (BR)\n* `pt_PT` - Portuguese (POR)\n* `pa` - Punjabi\n* `ro` - Romanian\n* `ru` - Russian\n* `sr` - Serbian\n* `sk` - Slovak\n* `sl` - Slovenian\n* `es` - Spanish\n* `es_AR` - Spanish (ARG)\n* `es_ES` - Spanish (SPA)\n* `es_MX` - Spanish (MEX)\n* `sw` - Swahili\n* `sv` - Swedish\n* `ta` - Tamil\n* `te` - Telugu\n* `th` - Thai\n* `tr` - Turkish\n* `uk` - Ukrainian\n* `ur` - Urdu\n* `uz` - Uzbek\n* `vi` - Vietnamese\n* `zu` - Zulu"
      },
      "PaginatedWhatsAppTemplateSimpleReadList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?page=4"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?page=2"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/WhatsAppTemplateSimpleRead"
            }
          }
        }
      },
      "SimpleChannel": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "channel_type": {
            "$ref": "#/components/schemas/ChannelTypeEnum"
          },
          "name": {
            "type": "string",
            "maxLength": 100
          },
          "channel_id": {
            "type": "string",
            "maxLength": 100
          },
          "status": {
            "$ref": "#/components/schemas/ChannelStatusEnum"
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "title": "Creado el"
          },
          "channel_provider": {
            "$ref": "#/components/schemas/ChannelProviderEnum"
          },
          "is_sandbox": {
            "type": "boolean"
          }
        },
        "required": [
          "channel_id",
          "id"
        ]
      },
      "WhatsAppTemplateSimpleRead": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "maxLength": 120
          },
          "language": {
            "$ref": "#/components/schemas/LanguageEnum"
          },
          "components": {
            "nullable": true
          },
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true,
            "description": "The UUID of the WhatsApp Template to be sent."
          },
          "category": {
            "$ref": "#/components/schemas/CategoryEnum"
          },
          "status": {
            "$ref": "#/components/schemas/WhatsAppTemplateStatusEnum"
          },
          "rejected_reason": {
            "type": "string",
            "nullable": true
          },
          "is_deleted": {
            "type": "boolean"
          },
          "channel": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SimpleChannel"
              }
            ],
            "description": "The ID of the WhatsApp Channel that the WhatsApp Template is for."
          },
          "show_in_sandbox": {
            "type": "boolean"
          }
        },
        "required": [
          "category",
          "channel",
          "id",
          "language",
          "name"
        ]
      },
      "WhatsAppTemplateStatusEnum": {
        "enum": [
          "draft",
          "approved",
          "in_appeal",
          "pending",
          "rejected",
          "pending_deletion",
          "deleted",
          "disabled",
          "submitted"
        ],
        "type": "string",
        "description": "* `draft` - Draft\n* `approved` - Approved\n* `in_appeal` - In Appeal\n* `pending` - Pending\n* `rejected` - Rejected\n* `pending_deletion` - Pending Deletion\n* `deleted` - Deleted\n* `disabled` - Disabled\n* `submitted` - Submitted"
      }
    },
    "securitySchemes": {
      "tokenAuth": {
        "type": "apiKey",
        "in": "header",
        "name": "Token",
        "description": "Token-based authentication with required prefix \"Token\""
      }
    }
  },
  "x-tagGroups": [
    {
      "name": "Users",
      "tags": [
        "User"
      ]
    },
    {
      "name": "Channels",
      "tags": [
        "WhatsApp",
        "Broadcast"
      ]
    },
    {
      "name": "Flows",
      "tags": [
        "Flow Execution",
        "Flow Execution Contact"
      ]
    },
    {
      "name": "CRM",
      "tags": [
        "Contact",
        "Conversation"
      ]
    },
    {
      "name": "Integrations",
      "tags": [
        "Webhook Subscription"
      ]
    }
  ],
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "description": "Production Server"
    }
  ],
  "tags": [
    {
      "name": "Templates"
    }
  ]
}
```