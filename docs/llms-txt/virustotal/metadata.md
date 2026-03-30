# Source: https://virustotal.readme.io/reference/metadata.md

# Get VirusTotal metadata

This endpoint returns a dictionary with metadata related to VirusTotal, which includes a full list of engines in use, a list of existing privileges, etc.

```json
{
  "data": {
    "engines": {
      "ALYac": {},
      "APEX": {},
      "AVG": {},
      "AVware": {},
      "Acronis": {},
      "Ad-Aware": {},
      "AegisLab": {},
      "AhnLab-V3": {},
      "Alibaba": {},
      "Antiy-AVL": {},
      "Arcabit": {},
      "Avast": {},
      "Avast-Mobile": {},
      "Avira": {},
      "Babable": {},
      "Baidu": {}
    },
    "privileges": [
      "cases",
      "click_to_accept",
      "creditcards",
      "dogfooder",
      "file-behaviour-feed",
      "downloads-tier-1",
      "downloads-tier-2"
    ],
    "relationships": {
      "analysis": [
        {
          "description": "File or URL the analysis belongs to.",
          "name": "item"
        }
      ],
      "async_search_job": [
        {
          "description": "Objects that match the search.",
          "name": "matches"
        }
      ],
      "case": [
        {
          "description": "Returns the files objects in the case.",
          "name": "files"
        },
        {
          "description": "Returns the graphs objects in the case.",
          "name": "graphs"
        }
      ],
      "code_block": [
        {
          "description": "Files that contain the code block.",
          "name": "files"
        }
      ],
      "comment": [
        {
          "description": "Object to which the comment belongs to.",
          "name": "item"
        },
        {
          "description": "User who wrote the comment.",
          "name": "author"
        }
      ],
      "domain": [
        {
          "description": "Votes for the file/URL.",
          "name": "votes"
        },
        {
          "description": "Comments for the Domain or IP's related entities.",
          "name": "related_comments"
        },
        {
          "description": "Parent domain.",
          "name": "parent"
        }
      ]
    }
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
    "/metadata": {
      "get": {
        "summary": "Get VirusTotal metadata",
        "description": "",
        "operationId": "metadata",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key.",
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