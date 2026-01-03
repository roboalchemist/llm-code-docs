# Source: https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final.md

# Validations Service

Mailgun Email Validation service with RESTful JSON HTTP API for performing email validation. This service also manages list
and CSV ingestion used in bulk validation processing.

Version: 1.0.0

## Servers

US Mailgun
```
https://api.mailgun.net
```

EU Mailgun
```
https://api.eu.mailgun.net
```

## Security

### basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

## Download OpenAPI description

[Validations Service](https://documentation.mailgun.com/_spec/docs/validate/oas/openapi-validate-final.yaml)

## Validations

This API provides functionality to validate single addresses, and managing thresholds.

### Validate Address V4

 - [GET /v4/address/validate](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/validations/get-v4-address-validate.md): A single email address to validate.

## Bulk Validations

This API provides functionality to upload and manage bulk validation lists and previews.

### Create Bulk Job

 - [POST /v4/address/validate/bulk/{list_id}](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/bulk-validations/post-v4-address-validate-bulk--list-id-.md): Validate a full list of addresses.

### Get Job V4

 - [GET /v4/address/validate/bulk/{list_id}](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/bulk-validations/api.initv4api.(*apihelpers).isfreeorfishy.func2-9.md): Gets a selected job by list ID.

### Delete Job V4

 - [DELETE /v4/address/validate/bulk/{list_id}](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/bulk-validations/api.initv4api.(*apihelpers).isfreeorfishy.func1-8.md): Cancels a selected job by list ID.

### List Jobs V4

 - [GET /v4/address/validate/bulk](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/bulk-validations/api.initv4api.(*apihelpers).isfreeorfishy.func4-11.md): Returns all jobs.

### Get Job V3

 - [GET /v3/lists/{list_id}/validate](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/bulk-validations/api.initv3api.(*apihelpers).isfreeorfishy.func2-13.md): Gets a selected job by list ID.

### Create Job V3

 - [POST /v3/lists/{list_id}/validate](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/bulk-validations/api.initv3api.(*apihelpers).isfreeorfishy.func3-14.md): Starts a V3 list validation job.

### Delete Job V3

 - [DELETE /v3/lists/{list_id}/validate](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/bulk-validations/api.initv3api.(*apihelpers).isfreeorfishy.func1-12.md): Cancels a selected job by list ID.

## List Health Preview

### Get List Health Preview Job

 - [GET /v4/address/validate/preview/{list_id}](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/list-health-preview/get-v4-address-validate-preview--list-id-.md): A single list health preview job by ID.

### Promote List Health Preview Job

 - [PUT /v4/address/validate/preview/{list_id}](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/list-health-preview/put-v4-address-validate-preview--list-id-.md): A currently running list health preview job can be promoted to a full bulk validations job, which will validate all addresses in the list.

### Create a List Health Preview Job

 - [POST /v4/address/validate/preview/{list_id}](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/list-health-preview/post-v4-address-validate-preview--list-id-.md): Start a list health preview job from a list of addresses. We will sample the list and run validations on a small percentage.

### Delete List Health Preview Job

 - [DELETE /v4/address/validate/preview/{list_id}](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/list-health-preview/delete-v4-address-validate-preview--list-id-.md): Deletes a single list health previewk job by ID.

### List List Health Preview Jobs

 - [GET /v4/address/validate/preview](https://documentation.mailgun.com/docs/validate/oas/openapi-validate-final/list-health-preview/get-v4-address-validate-preview.md): All list health preview jobs you have started.

