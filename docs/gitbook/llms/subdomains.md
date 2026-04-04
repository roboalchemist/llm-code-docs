# Source: https://gitbook.com/docs/developers/gitbook-api/api-reference/subdomains.md

# Subdomains

Provide a branded subdomain for each organization to create a consistent user experience. This API supports subdomain creation, DNS checks, and more.

## The Subdomain object

```json
{"openapi":"3.0.3","info":{"title":"GitBook API","version":"0.0.1-beta"},"components":{"schemas":{"Subdomain":{"type":"object","properties":{"object":{"type":"string","enum":["subdomain"]},"subdomain":{"type":"string","description":"The GitBook subdomain, for example \"my-company\" in \"my-company.gitbook.io\"","pattern":"^[a-z0-9][a-z0-9-]{1,30}[a-z0-9]$","minLength":3,"maxLength":32},"target":{"oneOf":[{"$ref":"#/components/schemas/OrganizationPointer"}]},"isActive":{"type":"boolean"}},"required":["object","subdomain","target","isActive"]},"OrganizationPointer":{"type":"object","properties":{"type":{"type":"string","enum":["organization"]},"organization":{"type":"string","description":"Unique identifier for the organization"}},"required":["type","organization"]}}}}
```

## GET /subdomains/{subdomain}

> Get a subdomain

```json
{"openapi":"3.0.3","info":{"title":"GitBook API","version":"0.0.1-beta"},"tags":[{"name":"subdomains","description":"Provide a branded subdomain for each organization to create a consistent user experience. This API supports subdomain creation, DNS checks, and more.\n\n{% openapi-schemas spec=\"gitbook\" schemas=\"Subdomain\" grouped=\"false\" %}\n    The Subdomain object\n{% endopenapi-schemas %}\n"}],"servers":[{"url":"{host}/v1","variables":{"host":{"default":"https://api.gitbook.com"}}}],"security":[{"user":[]}],"components":{"securitySchemes":{"user":{"type":"http","scheme":"bearer"}},"parameters":{"subdomain":{"name":"subdomain","in":"path","required":true,"description":"The subdomain, for example \"my-company\" in \"my-company.gitbook.io\"","schema":{"type":"string","pattern":"^[a-z0-9][a-z0-9-]{1,30}[a-z0-9]$","minLength":3,"maxLength":32}}},"schemas":{"Subdomain":{"type":"object","properties":{"object":{"type":"string","enum":["subdomain"]},"subdomain":{"type":"string","description":"The GitBook subdomain, for example \"my-company\" in \"my-company.gitbook.io\"","pattern":"^[a-z0-9][a-z0-9-]{1,30}[a-z0-9]$","minLength":3,"maxLength":32},"target":{"oneOf":[{"$ref":"#/components/schemas/OrganizationPointer"}]},"isActive":{"type":"boolean"}},"required":["object","subdomain","target","isActive"]},"OrganizationPointer":{"type":"object","properties":{"type":{"type":"string","enum":["organization"]},"organization":{"type":"string","description":"Unique identifier for the organization"}},"required":["type","organization"]}}},"paths":{"/subdomains/{subdomain}":{"get":{"operationId":"getSubdomain","summary":"Get a subdomain","tags":["subdomains"],"parameters":[{"$ref":"#/components/parameters/subdomain"}],"responses":{"200":{"description":"OK","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Subdomain"}}}}}}}}}
```
