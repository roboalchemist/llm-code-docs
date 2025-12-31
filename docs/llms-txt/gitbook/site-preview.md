# Source: https://gitbook.com/docs/developers/gitbook-api/api-reference/docs-sites/site-preview.md

# Site preview

Quickly generate a preview of how your site's content and layout will appear once published, allowing for final checks and refinement prior to going live.

## Get a site preview URL

> Generate a URL to preview the published content of a site. The URL will be valid for 1 hour.

```json
{"openapi":"3.0.3","info":{"title":"GitBook API","version":"0.0.1-beta"},"tags":[{"name":"site-preview","description":"Quickly generate a preview of how your site's content and layout will appear once published, allowing for final checks and refinement prior to going live.\n"}],"servers":[{"url":"{host}/v1","variables":{"host":{"default":"https://api.gitbook.com"}}}],"security":[{"user":[]}],"components":{"securitySchemes":{"user":{"type":"http","scheme":"bearer"}},"parameters":{"organizationId":{"name":"organizationId","in":"path","required":true,"description":"The unique id of the organization","schema":{"type":"string"}},"siteId":{"name":"siteId","in":"path","required":true,"description":"The unique id of the site","schema":{"type":"string"}}},"schemas":{"URL":{"type":"string","format":"uri","maxLength":2048}},"responses":{"BadRequestError":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","required":["error"],"properties":{"error":{"type":"object","properties":{"code":{"type":"integer","format":"int32","enum":[400]},"message":{"type":"string"}},"required":["code","message"]}}}}}}}},"paths":{"/orgs/{organizationId}/sites/{siteId}/publishing/preview":{"get":{"operationId":"getSitePublishingPreviewById","summary":"Get a site preview URL","description":"Generate a URL to preview the published content of a site. The URL will be valid for 1 hour.","tags":["site-preview"],"parameters":[{"$ref":"#/components/parameters/organizationId"},{"$ref":"#/components/parameters/siteId"},{"name":"siteSpace","in":"query","description":"ID of the site-space to preview. If not provided, the default site-space will be used.","schema":{"type":"string"}},{"name":"claims","in":"query","description":"Rison encoded string of attributes/assertions about the visitor for which we want to preview the site.","schema":{"type":"string"}}],"responses":{"200":{"description":"OK","content":{"application/json":{"schema":{"type":"object","properties":{"url":{"$ref":"#/components/schemas/URL"}},"required":["url"]}}}},"400":{"$ref":"#/components/responses/BadRequestError"}}}}}}
```
