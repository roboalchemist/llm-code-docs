# Source: https://virustotal.readme.io/reference/monitorpartner-comments-delete.md

# Remove a comment detection for a hash.

Remove a comment and reset confirmed detection for a hash.

This endpoint allows you to delete a comment and change *detection* to None so hash will appear over analysis listings if detected. More information about detection attribute could be found in [/hashes/'{'sha256'}'/comments](#monitorpartner-hashes-comments).

```python title="Python"
import requests

comment_id = '<comment-id>'

url = "https://www.virustotal.com/api/v3/monitor_partner/comments/{comment_id}" % comment_id

response = requests.request("DELETE", url)
print(response.text)
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
      "delete": {
        "summary": "Remove a comment detection for a hash.",
        "description": "Remove a comment and reset confirmed detection for a hash.",
        "operationId": "monitorpartner-comments-delete",
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