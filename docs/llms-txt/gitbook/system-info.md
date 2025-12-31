# Source: https://gitbook.com/docs/developers/gitbook-api/api-reference/system-info.md

# System info

Use these endpoints to monitor the overall health of GitBook's infrastructure or to retrieve version information for debugging and compliance purposes.

## Get API information

> Access the release version and build date of the GitBook codebase.

```json
{"openapi":"3.0.3","info":{"title":"GitBook API","version":"0.0.1-beta"},"tags":[{"name":"system","description":"Use these endpoints to monitor the overall health of GitBook's infrastructure or to retrieve version information for debugging and compliance purposes.\n"}],"servers":[{"url":"{host}/v1","variables":{"host":{"default":"https://api.gitbook.com"}}}],"security":[{"user":[]},{"user-internal":[]},{"user-staff":[]},{"user-internal-or-staff":[]},{"integration":[]},{"integration-installation":[]}],"components":{"securitySchemes":{"user":{"type":"http","scheme":"bearer"},"user-internal":{"type":"http","scheme":"bearer"},"user-staff":{"type":"http","scheme":"bearer"},"user-internal-or-staff":{"type":"http","scheme":"bearer"},"integration":{"type":"http","scheme":"bearer"},"integration-installation":{"type":"http","scheme":"bearer"}},"schemas":{"ApiInformation":{"type":"object","properties":{"version":{"type":"string","description":"Current release of GitBook"},"build":{"type":"string","description":"Date of the latest release in ISO format"}},"required":["version","build"]}}},"paths":{"/":{"get":{"operationId":"getApiInformation","tags":["system"],"summary":"Get API information","description":"Access the release version and build date of the GitBook codebase.","responses":{"200":{"description":"OK","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ApiInformation"}}}}}}}}}
```
