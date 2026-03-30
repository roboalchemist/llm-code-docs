# Source: https://virustotal.readme.io/reference/events.md

# Retrieve historical events about your software collection

This endpoint returns historical information about your stored files, including creation, deletion, detections, and clean-ups.

A dictionary with data, links, and meta properties is received.

Events will be listed in dictionary format with the following fields:

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-2": "Possible Values",
    "h-1": "Description",
    "0-0": "action",
    "1-0": "creator_id",
    "2-0": "details",
    "3-0": "level",
    "4-0": "monitor_key",
    "5-0": "owner_id",
    "6-0": "plaintext_description",
    "7-0": "source",
    "8-0": "subject",
    "9-0": "timestamp",
    "0-1": "A keyword describing the action that the event is describing",
    "0-2": "CLEAN\nCOMMENT\nDELETE\nDETECTED\nUPLOAD\nRESOLVED",
    "1-1": "Username. Who uploaded the file.",
    "2-1": "A list of strings detailing current and previous engine verdicts.",
    "2-2": "Composed of four parts with a ':' separator:\n\nengine\ncurrent | last\nsignature  | update | version | malicious | visible\n<value>\n\nFor example:\nengine:current:update:20191016\nengine:last:signature:<signature>",
    "3-1": "Severity level for the event.",
    "3-2": "0 (lowest) to 4 (highest)",
    "4-1": "The key of the monitor item.",
    "5-1": "The group that owns the monitor item.",
    "6-2": "Not always present",
    "6-1": "A space-separated collection of keywords containing sha256, detecting engines, and file names.",
    "7-1": "The action originating or triggering this event.",
    "7-2": "ANALYSIS\nFILE\nQUOTA",
    "8-1": "If applicable, the SHA256 of the file.",
    "9-1": "Timestamp in the format YYYYMMDDTHH:mm:ss"
  },
  "cols": 3,
  "rows": 10
}
[/block]

```json
{
  "data": [
    {
      action: "CLEAN",
      creator_id: "wcoyote",
      details: [
        {
          "v": "engine:current:clean"
        }
      ],
      level: "1",
      monitor_key: "abcdcdcedef928492384==",
      owner_id: "monitor_group_here",
      plaintext_description: "",
      source: "FILE",
      subject: "sha256_here",
      timestamp: "2019-12-31T23:58:58",
    },
    {
      action: "DETECTED",
      creator_id: "wcoyote",
      details: [
        {
          "v": "engine:current:malicious:ENGINE_ONE"
        },
        {
          "v": "engine:current:malicious:ENGINE_TWO"
        },
      ],
      level: "1",
      monitor_key: "abcdcdcedef928492384==",
      owner_id: "monitor_group_here",
      plaintext_description: "ENGINE_ONE <sha256> <filename>",
      source: "ANALYSIS",
      subject: "sha256_here",
      timestamp: "2019-12-31T23:58:58",
    }
  ],
  "links": {
  	"next": "https://www.virustotal.com/api/v3/monitor/events?cursor=ABCDE123456%3D%3D",
    "self": "https://www.virustotal.com/api/v3/monitor/events"
  },
  "meta": {
  	"cursor": "ABCDE123456==",
    "job_id": "foobar"
  }
}
```

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
    "/monitor/events": {
      "get": {
        "summary": "Retrieve historical events about your software collection",
        "description": "",
        "operationId": "events",
        "parameters": [
          {
            "name": "cursor",
            "in": "query",
            "description": "Continue returning results from this cursor on.",
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
          },
          {
            "name": "filter",
            "in": "query",
            "description": "A space-separated list of key:value accepting: 'action', 'creator_id', 'level<operator>', 'monitor_key', 'owner_id', 'source', 'timestamp<operator>', where operator is optional among '+', '-', and '='",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "job_id",
            "in": "query",
            "description": "Along with cursor, the corresponding job to continue returning results from.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "text/plain": {
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
        "security": [],
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/monitor/events \\\n  --header 'x-apikey: <your API key>'",
              "name": "cURL (simple)"
            },
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/monitor/events?filter=level:2+ \\\n  --header 'x-apikey: <your API key>'",
              "name": "cURL (with filter)"
            },
            {
              "language": "curl",
              "code": "curl --request GET \\\n  --url https://www.virustotal.com/api/v3/monitor/events?filter=level:0+%20monitor_key:<custom_monitor_key> \\\n  --header 'x-apikey: <your API key>'",
              "name": "cURL (complex filter)"
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
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```