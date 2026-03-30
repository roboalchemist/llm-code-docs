# Source: https://firebase.google.com/docs/reference/app-distribution/rest.md.txt

# Firebase App Distribution API

The Firebase App Distribution API enables programmatic management of a project's App Distribution resources, including testers and releases.

- [REST Resource: upload.v1.projects.apps.releases](https://firebase.google.com/docs/reference/app-distribution/rest#upload.v1.projects.apps.releases)
- [REST Resource: v1.projects.apps](https://firebase.google.com/docs/reference/app-distribution/rest#v1.projects.apps)
- [REST Resource: v1.projects.apps.releases](https://firebase.google.com/docs/reference/app-distribution/rest#v1.projects.apps.releases)
- [REST Resource: v1.projects.apps.releases.feedbackReports](https://firebase.google.com/docs/reference/app-distribution/rest#v1.projects.apps.releases.feedbackReports)
- [REST Resource: v1.projects.apps.releases.operations](https://firebase.google.com/docs/reference/app-distribution/rest#v1.projects.apps.releases.operations)
- [REST Resource: v1.projects.groups](https://firebase.google.com/docs/reference/app-distribution/rest#v1.projects.groups)
- [REST Resource: v1.projects.testers](https://firebase.google.com/docs/reference/app-distribution/rest#v1.projects.testers)

## Service: firebaseappdistribution.googleapis.com

> [!NOTE]
> Explore API functionality by calling an App Distribution REST API method
> on live data using the embedded API Explorer. This API Explorer lets you
> see the API request and response within the API reference documentation.
>
> To use the embedded explorer, click any method in the following tables
> except for `upload`, which is not
> supported. The embedded explorer appears in the **Try this API** side
> panel.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebaseappdistribution.googleapis.com/$discovery/rest?version=v1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebaseappdistribution.googleapis.com`

## REST Resource: [upload.v1.projects.apps.releases](https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/upload.v1.projects.apps.releases/upload` | `POST /upload/v1/{app=projects/*/apps/*}/releases:upload` Uploads a binary. |

## REST Resource: [v1.projects.apps](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps/getAabInfo` | `GET /v1/{name=projects/*/apps/*/aabInfo}` Gets Android App Bundle (AAB) information for a Firebase app. |

## REST Resource: [v1.projects.apps.releases](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/batchDelete` | `POST /v1/{parent=projects/*/apps/*}/releases:batchDelete` Deletes releases. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/distribute` | `POST /v1/{name=projects/*/apps/*/releases/*}:distribute` Distributes a release to testers. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/get` | `GET /v1/{name=projects/*/apps/*/releases/*}` Gets a release. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/list` | `GET /v1/{parent=projects/*/apps/*}/releases` Lists releases. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases/patch` | `PATCH /v1/{release.name=projects/*/apps/*/releases/*}` Updates a release. |

## REST Resource: [v1.projects.apps.releases.feedbackReports](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/delete` | `DELETE /v1/{name=projects/*/apps/*/releases/*/feedbackReports/*}` Deletes a feedback report. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get` | `GET /v1/{name=projects/*/apps/*/releases/*/feedbackReports/*}` Gets a feedback report. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list` | `GET /v1/{parent=projects/*/apps/*/releases/*}/feedbackReports` Lists feedback reports. |

## REST Resource: [v1.projects.apps.releases.operations](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.operations/get` | `GET /v1/{name=projects/*/apps/*/releases/*/operations/*}` Gets the latest state of a long-running operation. |

## REST Resource: [v1.projects.groups](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchJoin` | `POST /v1/{group=projects/*/groups/*}:batchJoin` Batch adds members to a group. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/batchLeave` | `POST /v1/{group=projects/*/groups/*}:batchLeave` Batch removed members from a group. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/create` | `POST /v1/{parent=projects/*}/groups` Create a group. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/delete` | `DELETE /v1/{name=projects/*/groups/*}` Delete a group. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/get` | `GET /v1/{name=projects/*/groups/*}` Get a group. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/list` | `GET /v1/{parent=projects/*}/groups` List groups. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.groups/patch` | `PATCH /v1/{group.name=projects/*/groups/*}` Update a group. |

## REST Resource: [v1.projects.testers](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchAdd` | `POST /v1/{project=projects/*}/testers:batchAdd` Batch adds testers. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/batchRemove` | `POST /v1/{project=projects/*}/testers:batchRemove` Batch removes testers. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/list` | `GET /v1/{parent=projects/*}/testers` Lists testers and their resource ids. |
| `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.testers/patch` | `PATCH /v1/{tester.name=projects/*/testers/*}` Update a tester. |