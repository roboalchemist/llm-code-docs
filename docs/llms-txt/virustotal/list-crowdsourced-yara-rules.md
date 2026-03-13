# Source: https://virustotal.readme.io/reference/list-crowdsourced-yara-rules.md

# List Crowdsourced YARA Rules

This endpoint lists the different VT's Crowdsourced YARA rules.

```json Example response
{
	"meta": {
		"cursor": "Ck8KDwoCbG0SCQjdvIy9kdv-AhI4ahFzfnZpcnVzdG90YWxjbG91ZHIjCxIIWWFyYVJ1bGUiFTAwM2UxYzUxZWZ8UEtfQVhBX2Z1bgwYACAB"
	},
	"data": [
		{
			"attributes": {
				"name": "PK_AXA_fun",
				"tags": [
					"AXA"
				],
				"matches": 0,
				"author": "Thomas Damonneville",
				"enabled": true,
				"rule": "rule PK_AXA_fun : AXA\n{\n    meta:\n        description = \"Phishing Kit impersonating AXA banque\"\n        licence = \"GPL-3.0\"\n        author = \"Thomas Damonneville\"\n        reference = \"\"\n        date = \"2023-05-02\"\n        comment = \"Phishing Kit - AXA - using a fun.php page\"\n\n    strings:\n        // the zipfile working on\n        $zip_file = { 50 4b 03 04 }\n        $spec_dir = \"css\"\n        $spec_dir2 = \"images\"\n        // specific file found in PhishingKit\n        $spec_file = \"detail.html\"\n        $spec_file2 = \"fun.php\"\n        $spec_file3 = \"fin.html\"\n        $spec_file4 = \"axa_pp_blanc.min.css\"\n\n    condition:\n        // look for the ZIP header\n        uint32(0) == 0x04034b50 and\n        // make sure we have a local file header\n        $zip_file and\n        // check for file\n        all of ($spec_file*) and\n        all of ($spec_dir*)\n}",
				"creation_date": 1682985600,
				"meta": [
					{
						"key": "description",
						"value": "Phishing Kit impersonating AXA banque"
					},
					{
						"key": "licence",
						"value": "GPL-3.0"
					},
					{
						"key": "author",
						"value": "Thomas Damonneville"
					},
					{
						"key": "reference",
						"value": ""
					},
					{
						"key": "date",
						"value": "2023-05-02"
					},
					{
						"key": "comment",
						"value": "Phishing Kit - AXA - using a fun.php page"
					}
				],
				"last_modification_date": 1683185194
			},
			"type": "yara_rule",
			"id": "003e1c51ef|PK_AXA_fun",
			"links": {
				"self": "https://www.virustotal.com/api/v3/yara_rules/003e1c51ef|PK_AXA_fun"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/yara_rules?limit=1",
		"next": "https://www.virustotal.com/api/v3/yara_rules?cursor=Ck8KDwoCbG0SCQjdvIy9kdv-AhI4ahFzfnZpcnVzdG90YWxjbG91ZHIjCxIIWWFyYVJ1bGUiFTAwM2UxYzUxZWZ8UEtfQVhBX2Z1bgwYACAB&limit=1"
	}
}
```

The `filter` parameter allows to filter the rules according to the values of certain attributes. For example you can get only the enabled rules with `enabled:true`. With `name:foo` and `foo` you can search for rules having the word "foo" in their names or in their meta values. Notice however that this only works with full words (words delimited by non-alphanumeric characters), if the rule's name is "foobar" it won't appear if you filter with `name:foo`. You can combine multiple filters separating them with spaces, for example: `filter=enabled:true name:foo`.

All the accepted filters are: `author`, `creation_date`, `enabled`, `included_date`, `last_modification_date`, `name`, `tag`, `threat_category`.

The `order` parameters control the order in which rulesets are returned, accepted orders are: `matches`, `creation_date`, `included_date` and `modification_date`. You can prepend `+` and `-` suffixes to specify ascending and descending orders (examples: `name-`, `creation_date+`, ). If not suffix is specified the order is ascending by default.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/yara_rules": {
      "get": {
        "summary": "List Crowdsourced YARA Rules",
        "description": "",
        "operationId": "list-crowdsourced-yara-rules",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of rules to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Return the rules matching the given criteria only",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Sort order",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```