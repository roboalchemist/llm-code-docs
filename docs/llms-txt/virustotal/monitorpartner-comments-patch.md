# Source: https://virustotal.readme.io/reference/monitorpartner-comments-patch.md

# Add a comment on a sha256 hash

Create a comment and if necessary confirm detection over a hash

This endpoint allows you to update a comment and change *detection* if necessary. More information about detection attribute could be found in [/hashes/'{'sha256'}'/comments](#get-sha256-hash-comments).

```python title="Python"
import requests

comment_id = '<comment-id>'

url = "https://www.virustotal.com/api/v3/monitor_partner/comments/{comment_id}" % comment_id
data = {
  'data': [{
    'attributes': {
      'comment': '[TEXT]',
      'detection': 'confirmed',
      'engine': '[ENGINE]',
      'sha256': '[HASH-SHA256]'
    },
    'id': comment_id,
    'type': 'monitor_hash_comment'
  }]
}

response = requests.request("POST", url, data=json.dumps(data))
print(response.text)
```

```json title="Example response"
{
  "data": [
    {
      "attributes": {
        "comment": "[TEXT]",
        "detection": "confirmed",
        "engine": "[ENGINE-ID]",
        "sha256": "[HASH-SHA256]"
      },
      "id": "[MONITOR-COMMENT-ID]",
      "type": "monitor_hash_comment"
    }
  ]
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
    "/monitor_partner/comments/{id}": {
      "patch": {
        "summary": "Add a comment on a sha256 hash",
        "description": "Create a comment and if necessary confirm detection over a hash",
        "operationId": "monitorpartner-comments-patch",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Comment identifier",
            "schema": {
              "type": "string"
            },
            "required": true
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A json object with a MonitorHashComment",
                    "default": "{\"data\": [{\"attributes\": {\"comment\": \"[TEXT]\", \"detection\": \"confirmed\", \"engine\": \"[ENGINE-ID]\", \"sha256\": \"[HASH-SHA256]\"}, \"type\": \"monitor_hash_comment\"}]}",
                    "format": "json"
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
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```