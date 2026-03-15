# Source: https://posthog.com/docs/open-api-spec/users_retrieve.md

# users_retrieve

## OpenAPI

```json GET /api/users/{uuid}/
{
  "paths": {
    "/api/users/{uuid}/": {
      "get": {
        "operationId": "users_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "uuid",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "users"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "user:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/User"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "User": {
        "type": "object",
        "properties": {
          "date_joined": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "pending_email": {
            "type": "string",
            "format": "email",
            "readOnly": true,
            "nullable": true,
            "title": "Pending email address awaiting verification"
          },
          "is_email_verified": {
            "type": "boolean",
            "readOnly": true,
            "nullable": true
          },
          "notification_settings": {
            "type": "object",
            "additionalProperties": {}
          },
          "anonymize_data": {
            "type": "boolean",
            "nullable": true
          },
          "allow_impersonation": {
            "type": "boolean",
            "nullable": true
          },
          "toolbar_mode": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/ToolbarModeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "has_password": {
            "type": "boolean",
            "readOnly": true
          },
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "is_staff": {
            "type": "boolean",
            "title": "Staff status",
            "description": "Designates whether the user can log into this admin site."
          },
          "is_impersonated": {
            "type": "boolean",
            "nullable": true,
            "readOnly": true
          },
          "is_impersonated_until": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "is_impersonated_read_only": {
            "type": "boolean",
            "nullable": true,
            "readOnly": true
          },
          "sensitive_session_expires_at": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "team": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TeamBasic"
              }
            ],
            "readOnly": true
          },
          "organization": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Organization"
              }
            ],
            "readOnly": true
          },
          "organizations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OrganizationBasic"
            },
            "readOnly": true
          },
          "set_current_organization": {
            "type": "string",
            "writeOnly": true
          },
          "set_current_team": {
            "type": "string",
            "writeOnly": true
          },
          "password": {
            "type": "string",
            "writeOnly": true,
            "maxLength": 128
          },
          "current_password": {
            "type": "string",
            "writeOnly": true
          },
          "events_column_config": {},
          "is_2fa_enabled": {
            "type": "boolean",
            "readOnly": true
          },
          "has_social_auth": {
            "type": "boolean",
            "readOnly": true
          },
          "has_sso_enforcement": {
            "type": "boolean",
            "readOnly": true
          },
          "has_seen_product_intro_for": {
            "nullable": true
          },
          "scene_personalisation": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ScenePersonalisationBasic"
            },
            "readOnly": true
          },
          "theme_mode": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/ThemeModeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "hedgehog_config": {
            "nullable": true
          },
          "allow_sidebar_suggestions": {
            "type": "boolean",
            "nullable": true
          },
          "shortcut_position": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/ShortcutPositionEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "role_at_organization": {
            "$ref": "#/components/schemas/RoleAtOrganizationEnum"
          },
          "passkeys_enabled_for_2fa": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether passkeys are enabled for 2FA authentication. Users can disable this to use only TOTP for 2FA while keeping passkeys for login."
          }
        },
        "required": [
          "date_joined",
          "distinct_id",
          "email",
          "has_password",
          "has_social_auth",
          "has_sso_enforcement",
          "id",
          "is_2fa_enabled",
          "is_email_verified",
          "is_impersonated",
          "is_impersonated_read_only",
          "is_impersonated_until",
          "organization",
          "organizations",
          "password",
          "pending_email",
          "scene_personalisation",
          "sensitive_session_expires_at",
          "team",
          "uuid"
        ]
      },
      "ToolbarModeEnum": {
        "enum": [
          "disabled",
          "toolbar"
        ],
        "type": "string",
        "description": "* `disabled` - disabled\n* `toolbar` - toolbar"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      },
      "TeamBasic": {
        "type": "object",
        "description": "Serializer for `Team` model with minimal attributes to speeed up loading and transfer times.\nAlso used for nested serializers.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "organization": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "project_id": {
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "format": "int64",
            "readOnly": true
          },
          "api_token": {
            "type": "string",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "completed_snippet_onboarding": {
            "type": "boolean",
            "readOnly": true
          },
          "has_completed_onboarding_for": {
            "readOnly": true,
            "nullable": true
          },
          "ingested_event": {
            "type": "boolean",
            "readOnly": true
          },
          "is_demo": {
            "type": "boolean",
            "readOnly": true
          },
          "timezone": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TimezoneEnum"
              }
            ],
            "readOnly": true
          },
          "access_control": {
            "type": "boolean",
            "readOnly": true
          }
        },
        "required": [
          "access_control",
          "api_token",
          "completed_snippet_onboarding",
          "has_completed_onboarding_for",
          "id",
          "ingested_event",
          "is_demo",
          "name",
          "organization",
          "project_id",
          "timezone",
          "uuid"
        ]
      },
      "Organization": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 64
          },
          "slug": {
            "type": "string",
            "readOnly": true,
            "pattern": "^[-a-zA-Z0-9_]+$"
          },
          "logo_media_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "membership_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MembershipLevelEnum"
              }
            ],
            "nullable": true,
            "readOnly": true
          },
          "plugins_access_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PluginsAccessLevelEnum"
              }
            ],
            "readOnly": true
          },
          "teams": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "readOnly": true
          },
          "projects": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "readOnly": true
          },
          "available_product_features": {
            "type": "array",
            "items": {},
            "readOnly": true,
            "nullable": true
          },
          "is_member_join_email_enabled": {
            "type": "boolean"
          },
          "metadata": {
            "type": "string",
            "readOnly": true
          },
          "customer_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "enforce_2fa": {
            "type": "boolean",
            "nullable": true
          },
          "members_can_invite": {
            "type": "boolean",
            "nullable": true
          },
          "members_can_use_personal_api_keys": {
            "type": "boolean"
          },
          "allow_publicly_shared_resources": {
            "type": "boolean"
          },
          "member_count": {
            "type": "string",
            "readOnly": true
          },
          "is_ai_data_processing_approved": {
            "type": "boolean",
            "nullable": true
          },
          "default_experiment_stats_method": {
            "nullable": true,
            "description": "Default statistical method for new experiments in this organization.\n\n* `bayesian` - Bayesian\n* `frequentist` - Frequentist",
            "oneOf": [
              {
                "$ref": "#/components/schemas/DefaultExperimentStatsMethodEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "default_anonymize_ips": {
            "type": "boolean",
            "description": "Default setting for 'Discard client IP data' for new projects in this organization."
          },
          "default_role_id": {
            "type": "string",
            "nullable": true,
            "description": "ID of the role to automatically assign to new members joining the organization"
          },
          "is_active": {
            "type": "boolean",
            "readOnly": true,
            "nullable": true,
            "title": "Active",
            "description": "Set this to 'No' to temporarily disable an organization."
          },
          "is_not_active_reason": {
            "type": "string",
            "readOnly": true,
            "nullable": true,
            "title": "De-activated reason",
            "description": "(optional) reason for why the organization has been de-activated. This will be displayed to users on the web app."
          }
        },
        "required": [
          "available_product_features",
          "created_at",
          "customer_id",
          "id",
          "is_active",
          "is_not_active_reason",
          "member_count",
          "membership_level",
          "metadata",
          "name",
          "plugins_access_level",
          "projects",
          "slug",
          "teams",
          "updated_at"
        ]
      },
      "OrganizationBasic": {
        "type": "object",
        "description": "Serializer for `Organization` model with minimal attributes to speeed up loading and transfer times.\nAlso used for nested serializers.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 64
          },
          "slug": {
            "type": "string",
            "maxLength": 48,
            "pattern": "^[-a-zA-Z0-9_]+$"
          },
          "logo_media_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "readOnly": true
          },
          "membership_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MembershipLevelEnum"
              }
            ],
            "nullable": true,
            "readOnly": true
          },
          "members_can_use_personal_api_keys": {
            "type": "boolean"
          },
          "is_active": {
            "type": "boolean",
            "nullable": true,
            "title": "Active",
            "description": "Set this to 'No' to temporarily disable an organization."
          },
          "is_not_active_reason": {
            "type": "string",
            "nullable": true,
            "title": "De-activated reason",
            "description": "(optional) reason for why the organization has been de-activated. This will be displayed to users on the web app.",
            "maxLength": 200
          }
        },
        "required": [
          "id",
          "logo_media_id",
          "membership_level",
          "name",
          "slug"
        ]
      },
      "ScenePersonalisationBasic": {
        "type": "object",
        "properties": {
          "scene": {
            "type": "string",
            "maxLength": 200
          },
          "dashboard": {
            "type": "integer",
            "nullable": true
          }
        },
        "required": [
          "scene"
        ]
      },
      "ThemeModeEnum": {
        "enum": [
          "light",
          "dark",
          "system"
        ],
        "type": "string",
        "description": "* `light` - Light\n* `dark` - Dark\n* `system` - System"
      },
      "ShortcutPositionEnum": {
        "enum": [
          "above",
          "below",
          "hidden"
        ],
        "type": "string",
        "description": "* `above` - Above\n* `below` - Below\n* `hidden` - Hidden"
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "TimezoneEnum": {
        "enum": [
          "Africa/Abidjan",
          "Africa/Accra",
          "Africa/Addis_Ababa",
          "Africa/Algiers",
          "Africa/Asmara",
          "Africa/Asmera",
          "Africa/Bamako",
          "Africa/Bangui",
          "Africa/Banjul",
          "Africa/Bissau",
          "Africa/Blantyre",
          "Africa/Brazzaville",
          "Africa/Bujumbura",
          "Africa/Cairo",
          "Africa/Casablanca",
          "Africa/Ceuta",
          "Africa/Conakry",
          "Africa/Dakar",
          "Africa/Dar_es_Salaam",
          "Africa/Djibouti",
          "Africa/Douala",
          "Africa/El_Aaiun",
          "Africa/Freetown",
          "Africa/Gaborone",
          "Africa/Harare",
          "Africa/Johannesburg",
          "Africa/Juba",
          "Africa/Kampala",
          "Africa/Khartoum",
          "Africa/Kigali",
          "Africa/Kinshasa",
          "Africa/Lagos",
          "Africa/Libreville",
          "Africa/Lome",
          "Africa/Luanda",
          "Africa/Lubumbashi",
          "Africa/Lusaka",
          "Africa/Malabo",
          "Africa/Maputo",
          "Africa/Maseru",
          "Africa/Mbabane",
          "Africa/Mogadishu",
          "Africa/Monrovia",
          "Africa/Nairobi",
          "Africa/Ndjamena",
          "Africa/Niamey",
          "Africa/Nouakchott",
          "Africa/Ouagadougou",
          "Africa/Porto-Novo",
          "Africa/Sao_Tome",
          "Africa/Timbuktu",
          "Africa/Tripoli",
          "Africa/Tunis",
          "Africa/Windhoek",
          "America/Adak",
          "America/Anchorage",
          "America/Anguilla",
          "America/Antigua",
          "America/Araguaina",
          "America/Argentina/Buenos_Aires",
          "America/Argentina/Catamarca",
          "America/Argentina/ComodRivadavia",
          "America/Argentina/Cordoba",
          "America/Argentina/Jujuy",
          "America/Argentina/La_Rioja",
          "America/Argentina/Mendoza",
          "America/Argentina/Rio_Gallegos",
          "America/Argentina/Salta",
          "America/Argentina/San_Juan",
          "America/Argentina/San_Luis",
          "America/Argentina/Tucuman",
          "America/Argentina/Ushuaia",
          "America/Aruba",
          "America/Asuncion",
          "America/Atikokan",
          "America/Atka",
          "America/Bahia",
          "America/Bahia_Banderas",
          "America/Barbados",
          "America/Belem",
          "America/Belize",
          "America/Blanc-Sablon",
          "America/Boa_Vista",
          "America/Bogota",
          "America/Boise",
          "America/Buenos_Aires",
          "America/Cambridge_Bay",
          "America/Campo_Grande",
          "America/Cancun",
          "America/Caracas",
          "America/Catamarca",
          "America/Cayenne",
          "America/Cayman",
          "America/Chicago",
          "America/Chihuahua",
          "America/Ciudad_Juarez",
          "America/Coral_Harbour",
          "America/Cordoba",
          "America/Costa_Rica",
          "America/Creston",
          "America/Cuiaba",
          "America/Curacao",
          "America/Danmarkshavn",
          "America/Dawson",
          "America/Dawson_Creek",
          "America/Denver",
          "America/Detroit",
          "America/Dominica",
          "America/Edmonton",
          "America/Eirunepe",
          "America/El_Salvador",
          "America/Ensenada",
          "America/Fort_Nelson",
          "America/Fort_Wayne",
          "America/Fortaleza",
          "America/Glace_Bay",
          "America/Godthab",
          "America/Goose_Bay",
          "America/Grand_Turk",
          "America/Grenada",
          "America/Guadeloupe",
          "America/Guatemala",
          "America/Guayaquil",
          "America/Guyana",
          "America/Halifax",
          "America/Havana",
          "America/Hermosillo",
          "America/Indiana/Indianapolis",
          "America/Indiana/Knox",
          "America/Indiana/Marengo",
          "America/Indiana/Petersburg",
          "America/Indiana/Tell_City",
          "America/Indiana/Vevay",
          "America/Indiana/Vincennes",
          "America/Indiana/Winamac",
          "America/Indianapolis",
          "America/Inuvik",
          "America/Iqaluit",
          "America/Jamaica",
          "America/Jujuy",
          "America/Juneau",
          "America/Kentucky/Louisville",
          "America/Kentucky/Monticello",
          "America/Knox_IN",
          "America/Kralendijk",
          "America/La_Paz",
          "America/Lima",
          "America/Los_Angeles",
          "America/Louisville",
          "America/Lower_Princes",
          "America/Maceio",
          "America/Managua",
          "America/Manaus",
          "America/Marigot",
          "America/Martinique",
          "America/Matamoros",
          "America/Mazatlan",
          "America/Mendoza",
          "America/Menominee",
          "America/Merida",
          "America/Metlakatla",
          "America/Mexico_City",
          "America/Miquelon",
          "America/Moncton",
          "America/Monterrey",
          "America/Montevideo",
          "America/Montreal",
          "America/Montserrat",
          "America/Nassau",
          "America/New_York",
          "America/Nipigon",
          "America/Nome",
          "America/Noronha",
          "America/North_Dakota/Beulah",
          "America/North_Dakota/Center",
          "America/North_Dakota/New_Salem",
          "America/Nuuk",
          "America/Ojinaga",
          "America/Panama",
          "America/Pangnirtung",
          "America/Paramaribo",
          "America/Phoenix",
          "America/Port-au-Prince",
          "America/Port_of_Spain",
          "America/Porto_Acre",
          "America/Porto_Velho",
          "America/Puerto_Rico",
          "America/Punta_Arenas",
          "America/Rainy_River",
          "America/Rankin_Inlet",
          "America/Recife",
          "America/Regina",
          "America/Resolute",
          "America/Rio_Branco",
          "America/Rosario",
          "America/Santa_Isabel",
          "America/Santarem",
          "America/Santiago",
          "America/Santo_Domingo",
          "America/Sao_Paulo",
          "America/Scoresbysund",
          "America/Shiprock",
          "America/Sitka",
          "America/St_Barthelemy",
          "America/St_Johns",
          "America/St_Kitts",
          "America/St_Lucia",
          "America/St_Thomas",
          "America/St_Vincent",
          "America/Swift_Current",
          "America/Tegucigalpa",
          "America/Thule",
          "America/Thunder_Bay",
          "America/Tijuana",
          "America/Toronto",
          "America/Tortola",
          "America/Vancouver",
          "America/Virgin",
          "America/Whitehorse",
          "America/Winnipeg",
          "America/Yakutat",
          "America/Yellowknife",
          "Antarctica/Casey",
          "Antarctica/Davis",
          "Antarctica/DumontDUrville",
          "Antarctica/Macquarie",
          "Antarctica/Mawson",
          "Antarctica/McMurdo",
          "Antarctica/Palmer",
          "Antarctica/Rothera",
          "Antarctica/South_Pole",
          "Antarctica/Syowa",
          "Antarctica/Troll",
          "Antarctica/Vostok",
          "Arctic/Longyearbyen",
          "Asia/Aden",
          "Asia/Almaty",
          "Asia/Amman",
          "Asia/Anadyr",
          "Asia/Aqtau",
          "Asia/Aqtobe",
          "Asia/Ashgabat",
          "Asia/Ashkhabad",
          "Asia/Atyrau",
          "Asia/Baghdad",
          "Asia/Bahrain",
          "Asia/Baku",
          "Asia/Bangkok",
          "Asia/Barnaul",
          "Asia/Beirut",
          "Asia/Bishkek",
          "Asia/Brunei",
          "Asia/Calcutta",
          "Asia/Chita",
          "Asia/Choibalsan",
          "Asia/Chongqing",
          "Asia/Chungking",
          "Asia/Colombo",
          "Asia/Dacca",
          "Asia/Damascus",
          "Asia/Dhaka",
          "Asia/Dili",
          "Asia/Dubai",
          "Asia/Dushanbe",
          "Asia/Famagusta",
          "Asia/Gaza",
          "Asia/Harbin",
          "Asia/Hebron",
          "Asia/Ho_Chi_Minh",
          "Asia/Hong_Kong",
          "Asia/Hovd",
          "Asia/Irkutsk",
          "Asia/Istanbul",
          "Asia/Jakarta",
          "Asia/Jayapura",
          "Asia/Jerusalem",
          "Asia/Kabul",
          "Asia/Kamchatka",
          "Asia/Karachi",
          "Asia/Kashgar",
          "Asia/Kathmandu",
          "Asia/Katmandu",
          "Asia/Khandyga",
          "Asia/Kolkata",
          "Asia/Krasnoyarsk",
          "Asia/Kuala_Lumpur",
          "Asia/Kuching",
          "Asia/Kuwait",
          "Asia/Macao",
          "Asia/Macau",
          "Asia/Magadan",
          "Asia/Makassar",
          "Asia/Manila",
          "Asia/Muscat",
          "Asia/Nicosia",
          "Asia/Novokuznetsk",
          "Asia/Novosibirsk",
          "Asia/Omsk",
          "Asia/Oral",
          "Asia/Phnom_Penh",
          "Asia/Pontianak",
          "Asia/Pyongyang",
          "Asia/Qatar",
          "Asia/Qostanay",
          "Asia/Qyzylorda",
          "Asia/Rangoon",
          "Asia/Riyadh",
          "Asia/Saigon",
          "Asia/Sakhalin",
          "Asia/Samarkand",
          "Asia/Seoul",
          "Asia/Shanghai",
          "Asia/Singapore",
          "Asia/Srednekolymsk",
          "Asia/Taipei",
          "Asia/Tashkent",
          "Asia/Tbilisi",
          "Asia/Tehran",
          "Asia/Tel_Aviv",
          "Asia/Thimbu",
          "Asia/Thimphu",
          "Asia/Tokyo",
          "Asia/Tomsk",
          "Asia/Ujung_Pandang",
          "Asia/Ulaanbaatar",
          "Asia/Ulan_Bator",
          "Asia/Urumqi",
          "Asia/Ust-Nera",
          "Asia/Vientiane",
          "Asia/Vladivostok",
          "Asia/Yakutsk",
          "Asia/Yangon",
          "Asia/Yekaterinburg",
          "Asia/Yerevan",
          "Atlantic/Azores",
          "Atlantic/Bermuda",
          "Atlantic/Canary",
          "Atlantic/Cape_Verde",
          "Atlantic/Faeroe",
          "Atlantic/Faroe",
          "Atlantic/Jan_Mayen",
          "Atlantic/Madeira",
          "Atlantic/Reykjavik",
          "Atlantic/South_Georgia",
          "Atlantic/St_Helena",
          "Atlantic/Stanley",
          "Australia/ACT",
          "Australia/Adelaide",
          "Australia/Brisbane",
          "Australia/Broken_Hill",
          "Australia/Canberra",
          "Australia/Currie",
          "Australia/Darwin",
          "Australia/Eucla",
          "Australia/Hobart",
          "Australia/LHI",
          "Australia/Lindeman",
          "Australia/Lord_Howe",
          "Australia/Melbourne",
          "Australia/NSW",
          "Australia/North",
          "Australia/Perth",
          "Australia/Queensland",
          "Australia/South",
          "Australia/Sydney",
          "Australia/Tasmania",
          "Australia/Victoria",
          "Australia/West",
          "Australia/Yancowinna",
          "Brazil/Acre",
          "Brazil/DeNoronha",
          "Brazil/East",
          "Brazil/West",
          "CET",
          "CST6CDT",
          "Canada/Atlantic",
          "Canada/Central",
          "Canada/Eastern",
          "Canada/Mountain",
          "Canada/Newfoundland",
          "Canada/Pacific",
          "Canada/Saskatchewan",
          "Canada/Yukon",
          "Chile/Continental",
          "Chile/EasterIsland",
          "Cuba",
          "EET",
          "EST",
          "EST5EDT",
          "Egypt",
          "Eire",
          "Etc/GMT",
          "Etc/GMT+0",
          "Etc/GMT+1",
          "Etc/GMT+10",
          "Etc/GMT+11",
          "Etc/GMT+12",
          "Etc/GMT+2",
          "Etc/GMT+3",
          "Etc/GMT+4",
          "Etc/GMT+5",
          "Etc/GMT+6",
          "Etc/GMT+7",
          "Etc/GMT+8",
          "Etc/GMT+9",
          "Etc/GMT-0",
          "Etc/GMT-1",
          "Etc/GMT-10",
          "Etc/GMT-11",
          "Etc/GMT-12",
          "Etc/GMT-13",
          "Etc/GMT-14",
          "Etc/GMT-2",
          "Etc/GMT-3",
          "Etc/GMT-4",
          "Etc/GMT-5",
          "Etc/GMT-6",
          "Etc/GMT-7",
          "Etc/GMT-8",
          "Etc/GMT-9",
          "Etc/GMT0",
          "Etc/Greenwich",
          "Etc/UCT",
          "Etc/UTC",
          "Etc/Universal",
          "Etc/Zulu",
          "Europe/Amsterdam",
          "Europe/Andorra",
          "Europe/Astrakhan",
          "Europe/Athens",
          "Europe/Belfast",
          "Europe/Belgrade",
          "Europe/Berlin",
          "Europe/Bratislava",
          "Europe/Brussels",
          "Europe/Bucharest",
          "Europe/Budapest",
          "Europe/Busingen",
          "Europe/Chisinau",
          "Europe/Copenhagen",
          "Europe/Dublin",
          "Europe/Gibraltar",
          "Europe/Guernsey",
          "Europe/Helsinki",
          "Europe/Isle_of_Man",
          "Europe/Istanbul",
          "Europe/Jersey",
          "Europe/Kaliningrad",
          "Europe/Kiev",
          "Europe/Kirov",
          "Europe/Kyiv",
          "Europe/Lisbon",
          "Europe/Ljubljana",
          "Europe/London",
          "Europe/Luxembourg",
          "Europe/Madrid",
          "Europe/Malta",
          "Europe/Mariehamn",
          "Europe/Minsk",
          "Europe/Monaco",
          "Europe/Moscow",
          "Europe/Nicosia",
          "Europe/Oslo",
          "Europe/Paris",
          "Europe/Podgorica",
          "Europe/Prague",
          "Europe/Riga",
          "Europe/Rome",
          "Europe/Samara",
          "Europe/San_Marino",
          "Europe/Sarajevo",
          "Europe/Saratov",
          "Europe/Simferopol",
          "Europe/Skopje",
          "Europe/Sofia",
          "Europe/Stockholm",
          "Europe/Tallinn",
          "Europe/Tirane",
          "Europe/Tiraspol",
          "Europe/Ulyanovsk",
          "Europe/Uzhgorod",
          "Europe/Vaduz",
          "Europe/Vatican",
          "Europe/Vienna",
          "Europe/Vilnius",
          "Europe/Volgograd",
          "Europe/Warsaw",
          "Europe/Zagreb",
          "Europe/Zaporozhye",
          "Europe/Zurich",
          "GB",
          "GB-Eire",
          "GMT",
          "GMT+0",
          "GMT-0",
          "GMT0",
          "Greenwich",
          "HST",
          "Hongkong",
          "Iceland",
          "Indian/Antananarivo",
          "Indian/Chagos",
          "Indian/Christmas",
          "Indian/Cocos",
          "Indian/Comoro",
          "Indian/Kerguelen",
          "Indian/Mahe",
          "Indian/Maldives",
          "Indian/Mauritius",
          "Indian/Mayotte",
          "Indian/Reunion",
          "Iran",
          "Israel",
          "Jamaica",
          "Japan",
          "Kwajalein",
          "Libya",
          "MET",
          "MST",
          "MST7MDT",
          "Mexico/BajaNorte",
          "Mexico/BajaSur",
          "Mexico/General",
          "NZ",
          "NZ-CHAT",
          "Navajo",
          "PRC",
          "PST8PDT",
          "Pacific/Apia",
          "Pacific/Auckland",
          "Pacific/Bougainville",
          "Pacific/Chatham",
          "Pacific/Chuuk",
          "Pacific/Easter",
          "Pacific/Efate",
          "Pacific/Enderbury",
          "Pacific/Fakaofo",
          "Pacific/Fiji",
          "Pacific/Funafuti",
          "Pacific/Galapagos",
          "Pacific/Gambier",
          "Pacific/Guadalcanal",
          "Pacific/Guam",
          "Pacific/Honolulu",
          "Pacific/Johnston",
          "Pacific/Kanton",
          "Pacific/Kiritimati",
          "Pacific/Kosrae",
          "Pacific/Kwajalein",
          "Pacific/Majuro",
          "Pacific/Marquesas",
          "Pacific/Midway",
          "Pacific/Nauru",
          "Pacific/Niue",
          "Pacific/Norfolk",
          "Pacific/Noumea",
          "Pacific/Pago_Pago",
          "Pacific/Palau",
          "Pacific/Pitcairn",
          "Pacific/Pohnpei",
          "Pacific/Ponape",
          "Pacific/Port_Moresby",
          "Pacific/Rarotonga",
          "Pacific/Saipan",
          "Pacific/Samoa",
          "Pacific/Tahiti",
          "Pacific/Tarawa",
          "Pacific/Tongatapu",
          "Pacific/Truk",
          "Pacific/Wake",
          "Pacific/Wallis",
          "Pacific/Yap",
          "Poland",
          "Portugal",
          "ROC",
          "ROK",
          "Singapore",
          "Turkey",
          "UCT",
          "US/Alaska",
          "US/Aleutian",
          "US/Arizona",
          "US/Central",
          "US/East-Indiana",
          "US/Eastern",
          "US/Hawaii",
          "US/Indiana-Starke",
          "US/Michigan",
          "US/Mountain",
          "US/Pacific",
          "US/Samoa",
          "UTC",
          "Universal",
          "W-SU",
          "WET",
          "Zulu"
        ],
        "type": "string",
        "description": "* `Africa/Abidjan` - Africa/Abidjan\n* `Africa/Accra` - Africa/Accra\n* `Africa/Addis_Ababa` - Africa/Addis_Ababa\n* `Africa/Algiers` - Africa/Algiers\n* `Africa/Asmara` - Africa/Asmara\n* `Africa/Asmera` - Africa/Asmera\n* `Africa/Bamako` - Africa/Bamako\n* `Africa/Bangui` - Africa/Bangui\n* `Africa/Banjul` - Africa/Banjul\n* `Africa/Bissau` - Africa/Bissau\n* `Africa/Blantyre` - Africa/Blantyre\n* `Africa/Brazzaville` - Africa/Brazzaville\n* `Africa/Bujumbura` - Africa/Bujumbura\n* `Africa/Cairo` - Africa/Cairo\n* `Africa/Casablanca` - Africa/Casablanca\n* `Africa/Ceuta` - Africa/Ceuta\n* `Africa/Conakry` - Africa/Conakry\n* `Africa/Dakar` - Africa/Dakar\n* `Africa/Dar_es_Salaam` - Africa/Dar_es_Salaam\n* `Africa/Djibouti` - Africa/Djibouti\n* `Africa/Douala` - Africa/Douala\n* `Africa/El_Aaiun` - Africa/El_Aaiun\n* `Africa/Freetown` - Africa/Freetown\n* `Africa/Gaborone` - Africa/Gaborone\n* `Africa/Harare` - Africa/Harare\n* `Africa/Johannesburg` - Africa/Johannesburg\n* `Africa/Juba` - Africa/Juba\n* `Africa/Kampala` - Africa/Kampala\n* `Africa/Khartoum` - Africa/Khartoum\n* `Africa/Kigali` - Africa/Kigali\n* `Africa/Kinshasa` - Africa/Kinshasa\n* `Africa/Lagos` - Africa/Lagos\n* `Africa/Libreville` - Africa/Libreville\n* `Africa/Lome` - Africa/Lome\n* `Africa/Luanda` - Africa/Luanda\n* `Africa/Lubumbashi` - Africa/Lubumbashi\n* `Africa/Lusaka` - Africa/Lusaka\n* `Africa/Malabo` - Africa/Malabo\n* `Africa/Maputo` - Africa/Maputo\n* `Africa/Maseru` - Africa/Maseru\n* `Africa/Mbabane` - Africa/Mbabane\n* `Africa/Mogadishu` - Africa/Mogadishu\n* `Africa/Monrovia` - Africa/Monrovia\n* `Africa/Nairobi` - Africa/Nairobi\n* `Africa/Ndjamena` - Africa/Ndjamena\n* `Africa/Niamey` - Africa/Niamey\n* `Africa/Nouakchott` - Africa/Nouakchott\n* `Africa/Ouagadougou` - Africa/Ouagadougou\n* `Africa/Porto-Novo` - Africa/Porto-Novo\n* `Africa/Sao_Tome` - Africa/Sao_Tome\n* `Africa/Timbuktu` - Africa/Timbuktu\n* `Africa/Tripoli` - Africa/Tripoli\n* `Africa/Tunis` - Africa/Tunis\n* `Africa/Windhoek` - Africa/Windhoek\n* `America/Adak` - America/Adak\n* `America/Anchorage` - America/Anchorage\n* `America/Anguilla` - America/Anguilla\n* `America/Antigua` - America/Antigua\n* `America/Araguaina` - America/Araguaina\n* `America/Argentina/Buenos_Aires` - America/Argentina/Buenos_Aires\n* `America/Argentina/Catamarca` - America/Argentina/Catamarca\n* `America/Argentina/ComodRivadavia` - America/Argentina/ComodRivadavia\n* `America/Argentina/Cordoba` - America/Argentina/Cordoba\n* `America/Argentina/Jujuy` - America/Argentina/Jujuy\n* `America/Argentina/La_Rioja` - America/Argentina/La_Rioja\n* `America/Argentina/Mendoza` - America/Argentina/Mendoza\n* `America/Argentina/Rio_Gallegos` - America/Argentina/Rio_Gallegos\n* `America/Argentina/Salta` - America/Argentina/Salta\n* `America/Argentina/San_Juan` - America/Argentina/San_Juan\n* `America/Argentina/San_Luis` - America/Argentina/San_Luis\n* `America/Argentina/Tucuman` - America/Argentina/Tucuman\n* `America/Argentina/Ushuaia` - America/Argentina/Ushuaia\n* `America/Aruba` - America/Aruba\n* `America/Asuncion` - America/Asuncion\n* `America/Atikokan` - America/Atikokan\n* `America/Atka` - America/Atka\n* `America/Bahia` - America/Bahia\n* `America/Bahia_Banderas` - America/Bahia_Banderas\n* `America/Barbados` - America/Barbados\n* `America/Belem` - America/Belem\n* `America/Belize` - America/Belize\n* `America/Blanc-Sablon` - America/Blanc-Sablon\n* `America/Boa_Vista` - America/Boa_Vista\n* `America/Bogota` - America/Bogota\n* `America/Boise` - America/Boise\n* `America/Buenos_Aires` - America/Buenos_Aires\n* `America/Cambridge_Bay` - America/Cambridge_Bay\n* `America/Campo_Grande` - America/Campo_Grande\n* `America/Cancun` - America/Cancun\n* `America/Caracas` - America/Caracas\n* `America/Catamarca` - America/Catamarca\n* `America/Cayenne` - America/Cayenne\n* `America/Cayman` - America/Cayman\n* `America/Chicago` - America/Chicago\n* `America/Chihuahua` - America/Chihuahua\n* `America/Ciudad_Juarez` - America/Ciudad_Juarez\n* `America/Coral_Harbour` - America/Coral_Harbour\n* `America/Cordoba` - America/Cordoba\n* `America/Costa_Rica` - America/Costa_Rica\n* `America/Creston` - America/Creston\n* `America/Cuiaba` - America/Cuiaba\n* `America/Curacao` - America/Curacao\n* `America/Danmarkshavn` - America/Danmarkshavn\n* `America/Dawson` - America/Dawson\n* `America/Dawson_Creek` - America/Dawson_Creek\n* `America/Denver` - America/Denver\n* `America/Detroit` - America/Detroit\n* `America/Dominica` - America/Dominica\n* `America/Edmonton` - America/Edmonton\n* `America/Eirunepe` - America/Eirunepe\n* `America/El_Salvador` - America/El_Salvador\n* `America/Ensenada` - America/Ensenada\n* `America/Fort_Nelson` - America/Fort_Nelson\n* `America/Fort_Wayne` - America/Fort_Wayne\n* `America/Fortaleza` - America/Fortaleza\n* `America/Glace_Bay` - America/Glace_Bay\n* `America/Godthab` - America/Godthab\n* `America/Goose_Bay` - America/Goose_Bay\n* `America/Grand_Turk` - America/Grand_Turk\n* `America/Grenada` - America/Grenada\n* `America/Guadeloupe` - America/Guadeloupe\n* `America/Guatemala` - America/Guatemala\n* `America/Guayaquil` - America/Guayaquil\n* `America/Guyana` - America/Guyana\n* `America/Halifax` - America/Halifax\n* `America/Havana` - America/Havana\n* `America/Hermosillo` - America/Hermosillo\n* `America/Indiana/Indianapolis` - America/Indiana/Indianapolis\n* `America/Indiana/Knox` - America/Indiana/Knox\n* `America/Indiana/Marengo` - America/Indiana/Marengo\n* `America/Indiana/Petersburg` - America/Indiana/Petersburg\n* `America/Indiana/Tell_City` - America/Indiana/Tell_City\n* `America/Indiana/Vevay` - America/Indiana/Vevay\n* `America/Indiana/Vincennes` - America/Indiana/Vincennes\n* `America/Indiana/Winamac` - America/Indiana/Winamac\n* `America/Indianapolis` - America/Indianapolis\n* `America/Inuvik` - America/Inuvik\n* `America/Iqaluit` - America/Iqaluit\n* `America/Jamaica` - America/Jamaica\n* `America/Jujuy` - America/Jujuy\n* `America/Juneau` - America/Juneau\n* `America/Kentucky/Louisville` - America/Kentucky/Louisville\n* `America/Kentucky/Monticello` - America/Kentucky/Monticello\n* `America/Knox_IN` - America/Knox_IN\n* `America/Kralendijk` - America/Kralendijk\n* `America/La_Paz` - America/La_Paz\n* `America/Lima` - America/Lima\n* `America/Los_Angeles` - America/Los_Angeles\n* `America/Louisville` - America/Louisville\n* `America/Lower_Princes` - America/Lower_Princes\n* `America/Maceio` - America/Maceio\n* `America/Managua` - America/Managua\n* `America/Manaus` - America/Manaus\n* `America/Marigot` - America/Marigot\n* `America/Martinique` - America/Martinique\n* `America/Matamoros` - America/Matamoros\n* `America/Mazatlan` - America/Mazatlan\n* `America/Mendoza` - America/Mendoza\n* `America/Menominee` - America/Menominee\n* `America/Merida` - America/Merida\n* `America/Metlakatla` - America/Metlakatla\n* `America/Mexico_City` - America/Mexico_City\n* `America/Miquelon` - America/Miquelon\n* `America/Moncton` - America/Moncton\n* `America/Monterrey` - America/Monterrey\n* `America/Montevideo` - America/Montevideo\n* `America/Montreal` - America/Montreal\n* `America/Montserrat` - America/Montserrat\n* `America/Nassau` - America/Nassau\n* `America/New_York` - America/New_York\n* `America/Nipigon` - America/Nipigon\n* `America/Nome` - America/Nome\n* `America/Noronha` - America/Noronha\n* `America/North_Dakota/Beulah` - America/North_Dakota/Beulah\n* `America/North_Dakota/Center` - America/North_Dakota/Center\n* `America/North_Dakota/New_Salem` - America/North_Dakota/New_Salem\n* `America/Nuuk` - America/Nuuk\n* `America/Ojinaga` - America/Ojinaga\n* `America/Panama` - America/Panama\n* `America/Pangnirtung` - America/Pangnirtung\n* `America/Paramaribo` - America/Paramaribo\n* `America/Phoenix` - America/Phoenix\n* `America/Port-au-Prince` - America/Port-au-Prince\n* `America/Port_of_Spain` - America/Port_of_Spain\n* `America/Porto_Acre` - America/Porto_Acre\n* `America/Porto_Velho` - America/Porto_Velho\n* `America/Puerto_Rico` - America/Puerto_Rico\n* `America/Punta_Arenas` - America/Punta_Arenas\n* `America/Rainy_River` - America/Rainy_River\n* `America/Rankin_Inlet` - America/Rankin_Inlet\n* `America/Recife` - America/Recife\n* `America/Regina` - America/Regina\n* `America/Resolute` - America/Resolute\n* `America/Rio_Branco` - America/Rio_Branco\n* `America/Rosario` - America/Rosario\n* `America/Santa_Isabel` - America/Santa_Isabel\n* `America/Santarem` - America/Santarem\n* `America/Santiago` - America/Santiago\n* `America/Santo_Domingo` - America/Santo_Domingo\n* `America/Sao_Paulo` - America/Sao_Paulo\n* `America/Scoresbysund` - America/Scoresbysund\n* `America/Shiprock` - America/Shiprock\n* `America/Sitka` - America/Sitka\n* `America/St_Barthelemy` - America/St_Barthelemy\n* `America/St_Johns` - America/St_Johns\n* `America/St_Kitts` - America/St_Kitts\n* `America/St_Lucia` - America/St_Lucia\n* `America/St_Thomas` - America/St_Thomas\n* `America/St_Vincent` - America/St_Vincent\n* `America/Swift_Current` - America/Swift_Current\n* `America/Tegucigalpa` - America/Tegucigalpa\n* `America/Thule` - America/Thule\n* `America/Thunder_Bay` - America/Thunder_Bay\n* `America/Tijuana` - America/Tijuana\n* `America/Toronto` - America/Toronto\n* `America/Tortola` - America/Tortola\n* `America/Vancouver` - America/Vancouver\n* `America/Virgin` - America/Virgin\n* `America/Whitehorse` - America/Whitehorse\n* `America/Winnipeg` - America/Winnipeg\n* `America/Yakutat` - America/Yakutat\n* `America/Yellowknife` - America/Yellowknife\n* `Antarctica/Casey` - Antarctica/Casey\n* `Antarctica/Davis` - Antarctica/Davis\n* `Antarctica/DumontDUrville` - Antarctica/DumontDUrville\n* `Antarctica/Macquarie` - Antarctica/Macquarie\n* `Antarctica/Mawson` - Antarctica/Mawson\n* `Antarctica/McMurdo` - Antarctica/McMurdo\n* `Antarctica/Palmer` - Antarctica/Palmer\n* `Antarctica/Rothera` - Antarctica/Rothera\n* `Antarctica/South_Pole` - Antarctica/South_Pole\n* `Antarctica/Syowa` - Antarctica/Syowa\n* `Antarctica/Troll` - Antarctica/Troll\n* `Antarctica/Vostok` - Antarctica/Vostok\n* `Arctic/Longyearbyen` - Arctic/Longyearbyen\n* `Asia/Aden` - Asia/Aden\n* `Asia/Almaty` - Asia/Almaty\n* `Asia/Amman` - Asia/Amman\n* `Asia/Anadyr` - Asia/Anadyr\n* `Asia/Aqtau` - Asia/Aqtau\n* `Asia/Aqtobe` - Asia/Aqtobe\n* `Asia/Ashgabat` - Asia/Ashgabat\n* `Asia/Ashkhabad` - Asia/Ashkhabad\n* `Asia/Atyrau` - Asia/Atyrau\n* `Asia/Baghdad` - Asia/Baghdad\n* `Asia/Bahrain` - Asia/Bahrain\n* `Asia/Baku` - Asia/Baku\n* `Asia/Bangkok` - Asia/Bangkok\n* `Asia/Barnaul` - Asia/Barnaul\n* `Asia/Beirut` - Asia/Beirut\n* `Asia/Bishkek` - Asia/Bishkek\n* `Asia/Brunei` - Asia/Brunei\n* `Asia/Calcutta` - Asia/Calcutta\n* `Asia/Chita` - Asia/Chita\n* `Asia/Choibalsan` - Asia/Choibalsan\n* `Asia/Chongqing` - Asia/Chongqing\n* `Asia/Chungking` - Asia/Chungking\n* `Asia/Colombo` - Asia/Colombo\n* `Asia/Dacca` - Asia/Dacca\n* `Asia/Damascus` - Asia/Damascus\n* `Asia/Dhaka` - Asia/Dhaka\n* `Asia/Dili` - Asia/Dili\n* `Asia/Dubai` - Asia/Dubai\n* `Asia/Dushanbe` - Asia/Dushanbe\n* `Asia/Famagusta` - Asia/Famagusta\n* `Asia/Gaza` - Asia/Gaza\n* `Asia/Harbin` - Asia/Harbin\n* `Asia/Hebron` - Asia/Hebron\n* `Asia/Ho_Chi_Minh` - Asia/Ho_Chi_Minh\n* `Asia/Hong_Kong` - Asia/Hong_Kong\n* `Asia/Hovd` - Asia/Hovd\n* `Asia/Irkutsk` - Asia/Irkutsk\n* `Asia/Istanbul` - Asia/Istanbul\n* `Asia/Jakarta` - Asia/Jakarta\n* `Asia/Jayapura` - Asia/Jayapura\n* `Asia/Jerusalem` - Asia/Jerusalem\n* `Asia/Kabul` - Asia/Kabul\n* `Asia/Kamchatka` - Asia/Kamchatka\n* `Asia/Karachi` - Asia/Karachi\n* `Asia/Kashgar` - Asia/Kashgar\n* `Asia/Kathmandu` - Asia/Kathmandu\n* `Asia/Katmandu` - Asia/Katmandu\n* `Asia/Khandyga` - Asia/Khandyga\n* `Asia/Kolkata` - Asia/Kolkata\n* `Asia/Krasnoyarsk` - Asia/Krasnoyarsk\n* `Asia/Kuala_Lumpur` - Asia/Kuala_Lumpur\n* `Asia/Kuching` - Asia/Kuching\n* `Asia/Kuwait` - Asia/Kuwait\n* `Asia/Macao` - Asia/Macao\n* `Asia/Macau` - Asia/Macau\n* `Asia/Magadan` - Asia/Magadan\n* `Asia/Makassar` - Asia/Makassar\n* `Asia/Manila` - Asia/Manila\n* `Asia/Muscat` - Asia/Muscat\n* `Asia/Nicosia` - Asia/Nicosia\n* `Asia/Novokuznetsk` - Asia/Novokuznetsk\n* `Asia/Novosibirsk` - Asia/Novosibirsk\n* `Asia/Omsk` - Asia/Omsk\n* `Asia/Oral` - Asia/Oral\n* `Asia/Phnom_Penh` - Asia/Phnom_Penh\n* `Asia/Pontianak` - Asia/Pontianak\n* `Asia/Pyongyang` - Asia/Pyongyang\n* `Asia/Qatar` - Asia/Qatar\n* `Asia/Qostanay` - Asia/Qostanay\n* `Asia/Qyzylorda` - Asia/Qyzylorda\n* `Asia/Rangoon` - Asia/Rangoon\n* `Asia/Riyadh` - Asia/Riyadh\n* `Asia/Saigon` - Asia/Saigon\n* `Asia/Sakhalin` - Asia/Sakhalin\n* `Asia/Samarkand` - Asia/Samarkand\n* `Asia/Seoul` - Asia/Seoul\n* `Asia/Shanghai` - Asia/Shanghai\n* `Asia/Singapore` - Asia/Singapore\n* `Asia/Srednekolymsk` - Asia/Srednekolymsk\n* `Asia/Taipei` - Asia/Taipei\n* `Asia/Tashkent` - Asia/Tashkent\n* `Asia/Tbilisi` - Asia/Tbilisi\n* `Asia/Tehran` - Asia/Tehran\n* `Asia/Tel_Aviv` - Asia/Tel_Aviv\n* `Asia/Thimbu` - Asia/Thimbu\n* `Asia/Thimphu` - Asia/Thimphu\n* `Asia/Tokyo` - Asia/Tokyo\n* `Asia/Tomsk` - Asia/Tomsk\n* `Asia/Ujung_Pandang` - Asia/Ujung_Pandang\n* `Asia/Ulaanbaatar` - Asia/Ulaanbaatar\n* `Asia/Ulan_Bator` - Asia/Ulan_Bator\n* `Asia/Urumqi` - Asia/Urumqi\n* `Asia/Ust-Nera` - Asia/Ust-Nera\n* `Asia/Vientiane` - Asia/Vientiane\n* `Asia/Vladivostok` - Asia/Vladivostok\n* `Asia/Yakutsk` - Asia/Yakutsk\n* `Asia/Yangon` - Asia/Yangon\n* `Asia/Yekaterinburg` - Asia/Yekaterinburg\n* `Asia/Yerevan` - Asia/Yerevan\n* `Atlantic/Azores` - Atlantic/Azores\n* `Atlantic/Bermuda` - Atlantic/Bermuda\n* `Atlantic/Canary` - Atlantic/Canary\n* `Atlantic/Cape_Verde` - Atlantic/Cape_Verde\n* `Atlantic/Faeroe` - Atlantic/Faeroe\n* `Atlantic/Faroe` - Atlantic/Faroe\n* `Atlantic/Jan_Mayen` - Atlantic/Jan_Mayen\n* `Atlantic/Madeira` - Atlantic/Madeira\n* `Atlantic/Reykjavik` - Atlantic/Reykjavik\n* `Atlantic/South_Georgia` - Atlantic/South_Georgia\n* `Atlantic/St_Helena` - Atlantic/St_Helena\n* `Atlantic/Stanley` - Atlantic/Stanley\n* `Australia/ACT` - Australia/ACT\n* `Australia/Adelaide` - Australia/Adelaide\n* `Australia/Brisbane` - Australia/Brisbane\n* `Australia/Broken_Hill` - Australia/Broken_Hill\n* `Australia/Canberra` - Australia/Canberra\n* `Australia/Currie` - Australia/Currie\n* `Australia/Darwin` - Australia/Darwin\n* `Australia/Eucla` - Australia/Eucla\n* `Australia/Hobart` - Australia/Hobart\n* `Australia/LHI` - Australia/LHI\n* `Australia/Lindeman` - Australia/Lindeman\n* `Australia/Lord_Howe` - Australia/Lord_Howe\n* `Australia/Melbourne` - Australia/Melbourne\n* `Australia/NSW` - Australia/NSW\n* `Australia/North` - Australia/North\n* `Australia/Perth` - Australia/Perth\n* `Australia/Queensland` - Australia/Queensland\n* `Australia/South` - Australia/South\n* `Australia/Sydney` - Australia/Sydney\n* `Australia/Tasmania` - Australia/Tasmania\n* `Australia/Victoria` - Australia/Victoria\n* `Australia/West` - Australia/West\n* `Australia/Yancowinna` - Australia/Yancowinna\n* `Brazil/Acre` - Brazil/Acre\n* `Brazil/DeNoronha` - Brazil/DeNoronha\n* `Brazil/East` - Brazil/East\n* `Brazil/West` - Brazil/West\n* `CET` - CET\n* `CST6CDT` - CST6CDT\n* `Canada/Atlantic` - Canada/Atlantic\n* `Canada/Central` - Canada/Central\n* `Canada/Eastern` - Canada/Eastern\n* `Canada/Mountain` - Canada/Mountain\n* `Canada/Newfoundland` - Canada/Newfoundland\n* `Canada/Pacific` - Canada/Pacific\n* `Canada/Saskatchewan` - Canada/Saskatchewan\n* `Canada/Yukon` - Canada/Yukon\n* `Chile/Continental` - Chile/Continental\n* `Chile/EasterIsland` - Chile/EasterIsland\n* `Cuba` - Cuba\n* `EET` - EET\n* `EST` - EST\n* `EST5EDT` - EST5EDT\n* `Egypt` - Egypt\n* `Eire` - Eire\n* `Etc/GMT` - Etc/GMT\n* `Etc/GMT+0` - Etc/GMT+0\n* `Etc/GMT+1` - Etc/GMT+1\n* `Etc/GMT+10` - Etc/GMT+10\n* `Etc/GMT+11` - Etc/GMT+11\n* `Etc/GMT+12` - Etc/GMT+12\n* `Etc/GMT+2` - Etc/GMT+2\n* `Etc/GMT+3` - Etc/GMT+3\n* `Etc/GMT+4` - Etc/GMT+4\n* `Etc/GMT+5` - Etc/GMT+5\n* `Etc/GMT+6` - Etc/GMT+6\n* `Etc/GMT+7` - Etc/GMT+7\n* `Etc/GMT+8` - Etc/GMT+8\n* `Etc/GMT+9` - Etc/GMT+9\n* `Etc/GMT-0` - Etc/GMT-0\n* `Etc/GMT-1` - Etc/GMT-1\n* `Etc/GMT-10` - Etc/GMT-10\n* `Etc/GMT-11` - Etc/GMT-11\n* `Etc/GMT-12` - Etc/GMT-12\n* `Etc/GMT-13` - Etc/GMT-13\n* `Etc/GMT-14` - Etc/GMT-14\n* `Etc/GMT-2` - Etc/GMT-2\n* `Etc/GMT-3` - Etc/GMT-3\n* `Etc/GMT-4` - Etc/GMT-4\n* `Etc/GMT-5` - Etc/GMT-5\n* `Etc/GMT-6` - Etc/GMT-6\n* `Etc/GMT-7` - Etc/GMT-7\n* `Etc/GMT-8` - Etc/GMT-8\n* `Etc/GMT-9` - Etc/GMT-9\n* `Etc/GMT0` - Etc/GMT0\n* `Etc/Greenwich` - Etc/Greenwich\n* `Etc/UCT` - Etc/UCT\n* `Etc/UTC` - Etc/UTC\n* `Etc/Universal` - Etc/Universal\n* `Etc/Zulu` - Etc/Zulu\n* `Europe/Amsterdam` - Europe/Amsterdam\n* `Europe/Andorra` - Europe/Andorra\n* `Europe/Astrakhan` - Europe/Astrakhan\n* `Europe/Athens` - Europe/Athens\n* `Europe/Belfast` - Europe/Belfast\n* `Europe/Belgrade` - Europe/Belgrade\n* `Europe/Berlin` - Europe/Berlin\n* `Europe/Bratislava` - Europe/Bratislava\n* `Europe/Brussels` - Europe/Brussels\n* `Europe/Bucharest` - Europe/Bucharest\n* `Europe/Budapest` - Europe/Budapest\n* `Europe/Busingen` - Europe/Busingen\n* `Europe/Chisinau` - Europe/Chisinau\n* `Europe/Copenhagen` - Europe/Copenhagen\n* `Europe/Dublin` - Europe/Dublin\n* `Europe/Gibraltar` - Europe/Gibraltar\n* `Europe/Guernsey` - Europe/Guernsey\n* `Europe/Helsinki` - Europe/Helsinki\n* `Europe/Isle_of_Man` - Europe/Isle_of_Man\n* `Europe/Istanbul` - Europe/Istanbul\n* `Europe/Jersey` - Europe/Jersey\n* `Europe/Kaliningrad` - Europe/Kaliningrad\n* `Europe/Kiev` - Europe/Kiev\n* `Europe/Kirov` - Europe/Kirov\n* `Europe/Kyiv` - Europe/Kyiv\n* `Europe/Lisbon` - Europe/Lisbon\n* `Europe/Ljubljana` - Europe/Ljubljana\n* `Europe/London` - Europe/London\n* `Europe/Luxembourg` - Europe/Luxembourg\n* `Europe/Madrid` - Europe/Madrid\n* `Europe/Malta` - Europe/Malta\n* `Europe/Mariehamn` - Europe/Mariehamn\n* `Europe/Minsk` - Europe/Minsk\n* `Europe/Monaco` - Europe/Monaco\n* `Europe/Moscow` - Europe/Moscow\n* `Europe/Nicosia` - Europe/Nicosia\n* `Europe/Oslo` - Europe/Oslo\n* `Europe/Paris` - Europe/Paris\n* `Europe/Podgorica` - Europe/Podgorica\n* `Europe/Prague` - Europe/Prague\n* `Europe/Riga` - Europe/Riga\n* `Europe/Rome` - Europe/Rome\n* `Europe/Samara` - Europe/Samara\n* `Europe/San_Marino` - Europe/San_Marino\n* `Europe/Sarajevo` - Europe/Sarajevo\n* `Europe/Saratov` - Europe/Saratov\n* `Europe/Simferopol` - Europe/Simferopol\n* `Europe/Skopje` - Europe/Skopje\n* `Europe/Sofia` - Europe/Sofia\n* `Europe/Stockholm` - Europe/Stockholm\n* `Europe/Tallinn` - Europe/Tallinn\n* `Europe/Tirane` - Europe/Tirane\n* `Europe/Tiraspol` - Europe/Tiraspol\n* `Europe/Ulyanovsk` - Europe/Ulyanovsk\n* `Europe/Uzhgorod` - Europe/Uzhgorod\n* `Europe/Vaduz` - Europe/Vaduz\n* `Europe/Vatican` - Europe/Vatican\n* `Europe/Vienna` - Europe/Vienna\n* `Europe/Vilnius` - Europe/Vilnius\n* `Europe/Volgograd` - Europe/Volgograd\n* `Europe/Warsaw` - Europe/Warsaw\n* `Europe/Zagreb` - Europe/Zagreb\n* `Europe/Zaporozhye` - Europe/Zaporozhye\n* `Europe/Zurich` - Europe/Zurich\n* `GB` - GB\n* `GB-Eire` - GB-Eire\n* `GMT` - GMT\n* `GMT+0` - GMT+0\n* `GMT-0` - GMT-0\n* `GMT0` - GMT0\n* `Greenwich` - Greenwich\n* `HST` - HST\n* `Hongkong` - Hongkong\n* `Iceland` - Iceland\n* `Indian/Antananarivo` - Indian/Antananarivo\n* `Indian/Chagos` - Indian/Chagos\n* `Indian/Christmas` - Indian/Christmas\n* `Indian/Cocos` - Indian/Cocos\n* `Indian/Comoro` - Indian/Comoro\n* `Indian/Kerguelen` - Indian/Kerguelen\n* `Indian/Mahe` - Indian/Mahe\n* `Indian/Maldives` - Indian/Maldives\n* `Indian/Mauritius` - Indian/Mauritius\n* `Indian/Mayotte` - Indian/Mayotte\n* `Indian/Reunion` - Indian/Reunion\n* `Iran` - Iran\n* `Israel` - Israel\n* `Jamaica` - Jamaica\n* `Japan` - Japan\n* `Kwajalein` - Kwajalein\n* `Libya` - Libya\n* `MET` - MET\n* `MST` - MST\n* `MST7MDT` - MST7MDT\n* `Mexico/BajaNorte` - Mexico/BajaNorte\n* `Mexico/BajaSur` - Mexico/BajaSur\n* `Mexico/General` - Mexico/General\n* `NZ` - NZ\n* `NZ-CHAT` - NZ-CHAT\n* `Navajo` - Navajo\n* `PRC` - PRC\n* `PST8PDT` - PST8PDT\n* `Pacific/Apia` - Pacific/Apia\n* `Pacific/Auckland` - Pacific/Auckland\n* `Pacific/Bougainville` - Pacific/Bougainville\n* `Pacific/Chatham` - Pacific/Chatham\n* `Pacific/Chuuk` - Pacific/Chuuk\n* `Pacific/Easter` - Pacific/Easter\n* `Pacific/Efate` - Pacific/Efate\n* `Pacific/Enderbury` - Pacific/Enderbury\n* `Pacific/Fakaofo` - Pacific/Fakaofo\n* `Pacific/Fiji` - Pacific/Fiji\n* `Pacific/Funafuti` - Pacific/Funafuti\n* `Pacific/Galapagos` - Pacific/Galapagos\n* `Pacific/Gambier` - Pacific/Gambier\n* `Pacific/Guadalcanal` - Pacific/Guadalcanal\n* `Pacific/Guam` - Pacific/Guam\n* `Pacific/Honolulu` - Pacific/Honolulu\n* `Pacific/Johnston` - Pacific/Johnston\n* `Pacific/Kanton` - Pacific/Kanton\n* `Pacific/Kiritimati` - Pacific/Kiritimati\n* `Pacific/Kosrae` - Pacific/Kosrae\n* `Pacific/Kwajalein` - Pacific/Kwajalein\n* `Pacific/Majuro` - Pacific/Majuro\n* `Pacific/Marquesas` - Pacific/Marquesas\n* `Pacific/Midway` - Pacific/Midway\n* `Pacific/Nauru` - Pacific/Nauru\n* `Pacific/Niue` - Pacific/Niue\n* `Pacific/Norfolk` - Pacific/Norfolk\n* `Pacific/Noumea` - Pacific/Noumea\n* `Pacific/Pago_Pago` - Pacific/Pago_Pago\n* `Pacific/Palau` - Pacific/Palau\n* `Pacific/Pitcairn` - Pacific/Pitcairn\n* `Pacific/Pohnpei` - Pacific/Pohnpei\n* `Pacific/Ponape` - Pacific/Ponape\n* `Pacific/Port_Moresby` - Pacific/Port_Moresby\n* `Pacific/Rarotonga` - Pacific/Rarotonga\n* `Pacific/Saipan` - Pacific/Saipan\n* `Pacific/Samoa` - Pacific/Samoa\n* `Pacific/Tahiti` - Pacific/Tahiti\n* `Pacific/Tarawa` - Pacific/Tarawa\n* `Pacific/Tongatapu` - Pacific/Tongatapu\n* `Pacific/Truk` - Pacific/Truk\n* `Pacific/Wake` - Pacific/Wake\n* `Pacific/Wallis` - Pacific/Wallis\n* `Pacific/Yap` - Pacific/Yap\n* `Poland` - Poland\n* `Portugal` - Portugal\n* `ROC` - ROC\n* `ROK` - ROK\n* `Singapore` - Singapore\n* `Turkey` - Turkey\n* `UCT` - UCT\n* `US/Alaska` - US/Alaska\n* `US/Aleutian` - US/Aleutian\n* `US/Arizona` - US/Arizona\n* `US/Central` - US/Central\n* `US/East-Indiana` - US/East-Indiana\n* `US/Eastern` - US/Eastern\n* `US/Hawaii` - US/Hawaii\n* `US/Indiana-Starke` - US/Indiana-Starke\n* `US/Michigan` - US/Michigan\n* `US/Mountain` - US/Mountain\n* `US/Pacific` - US/Pacific\n* `US/Samoa` - US/Samoa\n* `UTC` - UTC\n* `Universal` - Universal\n* `W-SU` - W-SU\n* `WET` - WET\n* `Zulu` - Zulu"
      },
      "MembershipLevelEnum": {
        "enum": [
          1,
          8,
          15
        ],
        "type": "integer"
      },
      "PluginsAccessLevelEnum": {
        "enum": [
          0,
          3,
          6,
          9
        ],
        "type": "integer",
        "description": "* `0` - none\n* `3` - config\n* `6` - install\n* `9` - root"
      },
      "DefaultExperimentStatsMethodEnum": {
        "enum": [
          "bayesian",
          "frequentist"
        ],
        "type": "string",
        "description": "* `bayesian` - Bayesian\n* `frequentist` - Frequentist"
      }
    }
  }
}
```
