# Source: https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference.md

# Admin API reference

### INTRODUCTION

Nimble’s Admin API allows you to perform a number of key account functions, including:

* Create, list, update, and delete pipelines
* View account status and remaining credits
* View account-level and pipeline-level usage reports
* Manage authenticated IPs

### Authentication

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/login" method="post" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/login/refresh" method="post" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

## Generate a new API key

> This API uses JWT/Bearer authentication: To generate an API-KEY, make a request with the following body/payload: { "key\_name": "string"}<br>

```json
{"openapi":"3.0.3","info":{"title":"Nimbleway API","version":"1.0.0"},"servers":[{"url":"https://api.nimbleway.com"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"type":"http","scheme":"bearer","bearerFormat":"JWT"}},"schemas":{"Error":{"type":"object","properties":{"code":{"type":"string"},"message":{"type":"string"}}}}},"paths":{"/api/v1/account/api-key":{"post":{"summary":"Generate a new API key","description":"This API uses JWT/Bearer authentication: To generate an API-KEY, make a request with the following body/payload: { \"key_name\": \"string\"}\n","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","required":["key_name"],"properties":{"key_name":{"type":"string"}}}}}},"responses":{"201":{"description":"API key successfully created","content":{"application/json":{"schema":{"type":"object","properties":{"guid":{"type":"string"},"key_name":{"type":"string"},"key":{"type":"string"},"createdAt":{"type":"string","format":"date-time"},"created_by":{"type":"string"},"account_name":{"type":"string"}}}}}},"400":{"description":"Invalid or missing request payload","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Error"}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Error"}}}},"403":{"description":"Forbidden – no permission to create API key","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Error"}}}},"500":{"description":"Internal server error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Error"}}}}}}}}}
```

### Authenticated IPs

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/authenticatedips" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/authenticatedips" method="put" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/authenticatedips" method="delete" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

### Pipelines

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines" method="post" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}" method="patch" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/authenticatedips/portrange" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/authenticatedips/portrange" method="put" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/authenticatedips/portrange" method="delete" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/password" method="put" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/reports/daily-usage" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/reports/detailed-requests" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/spendlimit" method="post" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/pipelines/{pipelineName}/spendlimit" method="delete" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

### Account Status

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/remaining-credits" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/reports/daily-usage" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/reports/detailed-requests" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

### Global Preferences

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/timeout" method="post" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/timeout" method="delete" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/account/timeout/{port}" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}

### Location

{% openapi src="<https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json>" path="/v1/location/cities" method="get" %}
[nimble-swagger.json](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/7qqFaG0FK33cnHOvxIbp/nimble-swagger.json)
{% endopenapi %}
