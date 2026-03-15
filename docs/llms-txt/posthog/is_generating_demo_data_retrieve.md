# Source: https://posthog.com/docs/open-api-spec/is_generating_demo_data_retrieve.md

# is_generating_demo_data_retrieve

## OpenAPI

```json GET /api/organizations/{organization_id}/projects/{id}/is_generating_demo_data/
{
  "paths": {
    "/api/organizations/{organization_id}/projects/{id}/is_generating_demo_data/": {
      "get": {
        "operationId": "is_generating_demo_data_retrieve",
        "description": "Projects for the current organization.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer",
              "maximum": 9223372036854776000,
              "minimum": -9223372036854776000,
              "format": "int64"
            },
            "description": "A unique value identifying this project.",
            "required": true
          },
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "projects"
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProjectBackwardCompat"
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
      "ProjectBackwardCompat": {
        "type": "object",
        "description": "Like `ProjectBasicSerializer`, but also works as a drop-in replacement for `TeamBasicSerializer` by way of\npassthrough fields. This allows the meaning of `Team` to change from \"project\" to \"environment\" without breaking\nbackward compatibility of the REST API.\nDo not use this in greenfield endpoints!",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "organization": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 200,
            "minLength": 1
          },
          "product_description": {
            "type": "string",
            "nullable": true,
            "maxLength": 1000
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "effective_membership_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EffectiveMembershipLevelEnum"
              }
            ],
            "nullable": true,
            "readOnly": true
          },
          "has_group_types": {
            "type": "boolean",
            "readOnly": true
          },
          "group_types": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "readOnly": true
          },
          "live_events_token": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "api_token": {
            "type": "string",
            "readOnly": true
          },
          "app_urls": {
            "type": "array",
            "items": {
              "type": "string",
              "nullable": true,
              "maxLength": 200
            }
          },
          "slack_incoming_webhook": {
            "type": "string",
            "nullable": true,
            "maxLength": 500
          },
          "anonymize_ips": {
            "type": "boolean"
          },
          "completed_snippet_onboarding": {
            "type": "boolean"
          },
          "ingested_event": {
            "type": "boolean",
            "readOnly": true
          },
          "test_account_filters": {},
          "test_account_filters_default_checked": {
            "type": "boolean",
            "nullable": true
          },
          "path_cleaning_filters": {
            "nullable": true
          },
          "is_demo": {
            "type": "boolean"
          },
          "timezone": {
            "$ref": "#/components/schemas/TimezoneEnum"
          },
          "data_attributes": {},
          "person_display_name_properties": {
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 400
            },
            "nullable": true
          },
          "correlation_config": {
            "nullable": true
          },
          "autocapture_opt_out": {
            "type": "boolean",
            "nullable": true
          },
          "autocapture_exceptions_opt_in": {
            "type": "boolean",
            "nullable": true
          },
          "autocapture_web_vitals_opt_in": {
            "type": "boolean",
            "nullable": true
          },
          "autocapture_web_vitals_allowed_metrics": {
            "nullable": true
          },
          "autocapture_exceptions_errors_to_ignore": {
            "nullable": true
          },
          "capture_console_log_opt_in": {
            "type": "boolean",
            "nullable": true
          },
          "capture_performance_opt_in": {
            "type": "boolean",
            "nullable": true
          },
          "session_recording_opt_in": {
            "type": "boolean"
          },
          "session_recording_sample_rate": {
            "type": "string",
            "format": "decimal",
            "pattern": "^-?\\d{0,1}(?:\\.\\d{0,2})?$",
            "nullable": true
          },
          "session_recording_minimum_duration_milliseconds": {
            "type": "integer",
            "maximum": 30000,
            "minimum": 0,
            "nullable": true
          },
          "session_recording_linked_flag": {
            "nullable": true
          },
          "session_recording_network_payload_capture_config": {
            "nullable": true
          },
          "session_recording_masking_config": {
            "nullable": true
          },
          "session_replay_config": {
            "nullable": true
          },
          "survey_config": {
            "nullable": true
          },
          "access_control": {
            "type": "boolean"
          },
          "week_start_day": {
            "nullable": true,
            "minimum": -32768,
            "maximum": 32767,
            "oneOf": [
              {
                "$ref": "#/components/schemas/WeekStartDayEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "primary_dashboard": {
            "type": "integer",
            "nullable": true
          },
          "live_events_columns": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          },
          "recording_domains": {
            "type": "array",
            "items": {
              "type": "string",
              "nullable": true,
              "maxLength": 200
            },
            "nullable": true
          },
          "person_on_events_querying_enabled": {
            "type": "string",
            "readOnly": true
          },
          "inject_web_apps": {
            "type": "boolean",
            "nullable": true
          },
          "extra_settings": {
            "nullable": true
          },
          "modifiers": {
            "nullable": true
          },
          "default_modifiers": {
            "type": "string",
            "readOnly": true
          },
          "has_completed_onboarding_for": {
            "nullable": true
          },
          "surveys_opt_in": {
            "type": "boolean",
            "nullable": true
          },
          "heatmaps_opt_in": {
            "type": "boolean",
            "nullable": true
          },
          "product_intents": {
            "type": "string",
            "readOnly": true
          },
          "flags_persistence_default": {
            "type": "boolean",
            "nullable": true
          },
          "secret_api_token": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "secret_api_token_backup": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "receive_org_level_activity_logs": {
            "type": "boolean",
            "nullable": true
          },
          "business_model": {
            "nullable": true,
            "description": "Whether this project serves B2B or B2C customers, used to optimize the UI layout.\n\n* `b2b` - B2B\n* `b2c` - B2C\n* `other` - Other",
            "oneOf": [
              {
                "$ref": "#/components/schemas/BusinessModelEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "conversations_enabled": {
            "type": "boolean",
            "nullable": true
          },
          "conversations_settings": {
            "nullable": true
          },
          "logs_settings": {
            "nullable": true
          },
          "proactive_tasks_enabled": {
            "type": "boolean",
            "nullable": true
          },
          "available_setup_task_ids": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AvailableSetupTaskIdsEnum"
            },
            "readOnly": true
          }
        },
        "required": [
          "api_token",
          "available_setup_task_ids",
          "created_at",
          "default_modifiers",
          "effective_membership_level",
          "group_types",
          "has_group_types",
          "id",
          "ingested_event",
          "live_events_token",
          "organization",
          "person_on_events_querying_enabled",
          "product_intents",
          "secret_api_token",
          "secret_api_token_backup",
          "updated_at",
          "uuid"
        ]
      },
      "EffectiveMembershipLevelEnum": {
        "enum": [
          1,
          8,
          15
        ],
        "type": "integer"
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
      "WeekStartDayEnum": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "description": "* `0` - Sunday\n* `1` - Monday"
      },
      "NullEnum": {
        "enum": [
          null
        ]
      },
      "BusinessModelEnum": {
        "enum": [
          "b2b",
          "b2c",
          "other"
        ],
        "type": "string",
        "description": "* `b2b` - B2B\n* `b2c` - B2C\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "AvailableSetupTaskIdsEnum": {
        "enum": [
          "ingest_first_event",
          "set_up_reverse_proxy",
          "create_first_insight",
          "create_first_dashboard",
          "track_custom_events",
          "define_actions",
          "set_up_cohorts",
          "explore_trends_insight",
          "create_funnel",
          "explore_retention_insight",
          "explore_paths_insight",
          "explore_stickiness_insight",
          "explore_lifecycle_insight",
          "add_authorized_domain",
          "set_up_web_vitals",
          "review_web_analytics_dashboard",
          "filter_web_analytics",
          "set_up_web_analytics_conversion_goals",
          "visit_web_vitals_dashboard",
          "setup_session_recordings",
          "watch_session_recording",
          "configure_recording_settings",
          "create_recording_playlist",
          "enable_console_logs",
          "create_feature_flag",
          "implement_flag_in_code",
          "update_feature_flag_release_conditions",
          "create_multivariate_flag",
          "set_up_flag_payloads",
          "set_up_flag_evaluation_runtimes",
          "create_experiment",
          "implement_experiment_variants",
          "launch_experiment",
          "review_experiment_results",
          "create_survey",
          "launch_survey",
          "collect_survey_responses",
          "connect_source",
          "run_first_query",
          "join_external_data",
          "create_saved_view",
          "enable_error_tracking",
          "upload_source_maps",
          "view_first_error",
          "resolve_first_error",
          "ingest_first_llm_event",
          "view_first_trace",
          "track_costs",
          "set_up_llm_evaluation",
          "run_ai_playground",
          "enable_revenue_analytics_viewset",
          "connect_revenue_source",
          "set_up_revenue_goal",
          "enable_log_capture",
          "view_first_logs",
          "create_first_workflow",
          "set_up_first_workflow_channel",
          "configure_workflow_trigger",
          "add_workflow_action",
          "launch_workflow",
          "create_first_endpoint",
          "configure_endpoint",
          "test_endpoint",
          "create_early_access_feature",
          "update_feature_stage"
        ],
        "type": "string",
        "description": "* `ingest_first_event` - ingest_first_event\n* `set_up_reverse_proxy` - set_up_reverse_proxy\n* `create_first_insight` - create_first_insight\n* `create_first_dashboard` - create_first_dashboard\n* `track_custom_events` - track_custom_events\n* `define_actions` - define_actions\n* `set_up_cohorts` - set_up_cohorts\n* `explore_trends_insight` - explore_trends_insight\n* `create_funnel` - create_funnel\n* `explore_retention_insight` - explore_retention_insight\n* `explore_paths_insight` - explore_paths_insight\n* `explore_stickiness_insight` - explore_stickiness_insight\n* `explore_lifecycle_insight` - explore_lifecycle_insight\n* `add_authorized_domain` - add_authorized_domain\n* `set_up_web_vitals` - set_up_web_vitals\n* `review_web_analytics_dashboard` - review_web_analytics_dashboard\n* `filter_web_analytics` - filter_web_analytics\n* `set_up_web_analytics_conversion_goals` - set_up_web_analytics_conversion_goals\n* `visit_web_vitals_dashboard` - visit_web_vitals_dashboard\n* `setup_session_recordings` - setup_session_recordings\n* `watch_session_recording` - watch_session_recording\n* `configure_recording_settings` - configure_recording_settings\n* `create_recording_playlist` - create_recording_playlist\n* `enable_console_logs` - enable_console_logs\n* `create_feature_flag` - create_feature_flag\n* `implement_flag_in_code` - implement_flag_in_code\n* `update_feature_flag_release_conditions` - update_feature_flag_release_conditions\n* `create_multivariate_flag` - create_multivariate_flag\n* `set_up_flag_payloads` - set_up_flag_payloads\n* `set_up_flag_evaluation_runtimes` - set_up_flag_evaluation_runtimes\n* `create_experiment` - create_experiment\n* `implement_experiment_variants` - implement_experiment_variants\n* `launch_experiment` - launch_experiment\n* `review_experiment_results` - review_experiment_results\n* `create_survey` - create_survey\n* `launch_survey` - launch_survey\n* `collect_survey_responses` - collect_survey_responses\n* `connect_source` - connect_source\n* `run_first_query` - run_first_query\n* `join_external_data` - join_external_data\n* `create_saved_view` - create_saved_view\n* `enable_error_tracking` - enable_error_tracking\n* `upload_source_maps` - upload_source_maps\n* `view_first_error` - view_first_error\n* `resolve_first_error` - resolve_first_error\n* `ingest_first_llm_event` - ingest_first_llm_event\n* `view_first_trace` - view_first_trace\n* `track_costs` - track_costs\n* `set_up_llm_evaluation` - set_up_llm_evaluation\n* `run_ai_playground` - run_ai_playground\n* `enable_revenue_analytics_viewset` - enable_revenue_analytics_viewset\n* `connect_revenue_source` - connect_revenue_source\n* `set_up_revenue_goal` - set_up_revenue_goal\n* `enable_log_capture` - enable_log_capture\n* `view_first_logs` - view_first_logs\n* `create_first_workflow` - create_first_workflow\n* `set_up_first_workflow_channel` - set_up_first_workflow_channel\n* `configure_workflow_trigger` - configure_workflow_trigger\n* `add_workflow_action` - add_workflow_action\n* `launch_workflow` - launch_workflow\n* `create_first_endpoint` - create_first_endpoint\n* `configure_endpoint` - configure_endpoint\n* `test_endpoint` - test_endpoint\n* `create_early_access_feature` - create_early_access_feature\n* `update_feature_stage` - update_feature_stage"
      }
    }
  }
}
```
