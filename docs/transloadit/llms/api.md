# Source: https://transloadit.com/docs/api.md

# API endpoints

We offer ready-to-use [SDKs](/docs/sdks.md) for most major programming languages and platforms and generally recommend using those. However, if there is no suitable SDK for your situation, or perhaps you are building one, we explain all the details of our bare bones REST API here.

Transloadit provides a JSON REST API that can be used for:

* Creating, checking up on, or deleting Assemblies
* Replaying Assembly Notifications
* Creating, updating, checking up on, or deleting Templates
* Checking up on Billing

Here’s a complete overview of the available endpoints:

### Authentication

* [Create a bearer token](/docs/api/token-post.md)\
  POST`/token`

### Assemblies

* [Create a new Assembly](/docs/api/assemblies-post.md)\
  POST`/assemblies`
* [Retrieve an Assembly Status](/docs/api/assemblies-assembly-id-get.md)\
  GET`/assemblies/{ASSEMBLY_ID}`
* [Stream Assembly changes live](/docs/api/assemblies-assembly-id-stream-get.md)\
  GET`{UPDATE_STREAM_URL}`
* [Cancel a running Assembly](/docs/api/assemblies-assembly-id-delete.md)\
  DELETE`/assemblies/{ASSEMBLY_ID}`
* [Replay an Assembly](/docs/api/assemblies-assembly-id-replay-post.md)\
  POST`/assemblies/{ASSEMBLY_ID}/replay`
* [Retrieve list of Assemblies](/docs/api/assemblies-get.md)\
  GET`/assemblies?signature={SIGNATURE}&params={PARAMS}`

### Webhooks

* [Replay Assembly Notification](/docs/api/assembly-notifications-assembly-id-replay-post.md)\
  POST`/assembly_notifications/{ASSEMBLY_ID}/replay`

### Billing

* [Retrieve a month’s bill](/docs/api/bill-date-get.md)\
  GET`/bill/{DATE}?signature={SIGNATURE}`

### Queue

* [Retrieve currently used priority job slots](/docs/api/queues-job-slots-get.md)\
  GET`/queues/job_slots?signature={SIGNATURE}`

### Template Credentials

* [Create a new Template Credential](/docs/api/template-credentials-post.md)\
  POST`/template_credentials`
* [Retrieve a Template Credential](/docs/api/template-credentials-credentials-id-get.md)\
  GET`/template_credentials/{CREDENTIALS_ID_OR_NAME}?signature={SIGNATURE}&params={PARAMS}`
* [Edit a Template Credential](/docs/api/template-credentials-credentials-id-put.md)\
  PUT`/template_credentials/{CREDENTIALS_ID_OR_NAME}?signature={SIGNATURE}`
* [Delete a Template Credential](/docs/api/template-credentials-credentials-id-delete.md)\
  DELETE`/template_credentials/{CREDENTIALS_ID_OR_NAME}`
* [Retrieve list of Template Credentials](/docs/api/template-credentials-get.md)\
  GET`/template_credentials?signature={SIGNATURE}&params={PARAMS}`

### Templates

* [Create a new Template](/docs/api/templates-post.md)\
  POST`/templates`
* [Retrieve a Template](/docs/api/templates-template-id-get.md)\
  GET`/templates/{TEMPLATE_ID}?signature={SIGNATURE}&params={PARAMS}`
* [Edit a Template](/docs/api/templates-template-id-put.md)\
  PUT`/templates/{TEMPLATE_ID}`
* [Delete a Template](/docs/api/templates-template-id-delete.md)\
  DELETE`/templates/{TEMPLATE_ID}`
* [Retrieve list of Templates](/docs/api/templates-get.md)\
  GET`/templates?signature={SIGNATURE}&params={PARAMS}`
