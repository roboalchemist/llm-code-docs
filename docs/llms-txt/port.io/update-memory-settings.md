# Source: https://docs.port.io/api-reference/update-memory-settings.md

# Update memory settings

```
PUT 
/v1/memory/settings
```

This route allows organization administrators to update memory settings for their organization. When memory is disabled, the AI stops learning new preferences but existing memories are retained.

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 403

Successfully updated memory settings

Unauthorized

Forbidden - Admin permissions required
