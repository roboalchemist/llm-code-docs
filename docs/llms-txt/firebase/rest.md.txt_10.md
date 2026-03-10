# Source: https://firebase.google.com/docs/reference/rules/rest.md.txt

# Firebase Rules API

Creates and manages rules that determine when a Firebase Security Rules-enabled service should permit a request.

- [REST Resource: v1.projects](https://firebase.google.com/docs/reference/rules/rest#v1.projects)
- [REST Resource: v1.projects.releases](https://firebase.google.com/docs/reference/rules/rest#v1.projects.releases)
- [REST Resource: v1.projects.rulesets](https://firebase.google.com/docs/reference/rules/rest#v1.projects.rulesets)

> [!NOTE]
> This reference documentation applies to managing Firebase Security Rules for Cloud Firestore and Cloud Storage for Firebase. For information about managing Firebase Realtime Database Security Rules, see [Managing
> Firebase Realtime Database Rules using REST](https://firebase.google.com/docs/database/rest/app-management).

**For a description of the tools you can use to manage your Security Rules, including this
REST API, see [Manage and deploy Firebase Security Rules](https://firebase.google.com/docs/rules/manage-deploy).**

> [!NOTE]
> You can try out calling a Security Rules REST API method on live data using
> the embedded API Explorer. This API Explorer allows you to see the API
> request and response without leaving the API's reference documentation.
>
> Find the embedded explorer in the side-panel of each method's reference
> page (click any method in the tables below).

## Overview


Firebase Security Rules is comprised of a language and an API. Developers write rules in the
language, publish them via the API, and then submit requests to Firebase Security Rules-enabled
services. Services evaluate requests using the provided ruleset and determine whether the
requests should be permitted.


The following terms are used in this reference documentation.

-
  `Source`: Domain-specific language containing rules scoped to a `service`
  and `path` describing the conditions when a specific `request`
  `operation` may be permitted.

-
  `Ruleset`: Persistent immutable copy `Source` content with a generated name.

-
  `Release`: Named reference to a `Ruleset`, which makes the
  `Ruleset` available for consumption and enforcement by Firebase Security
  Rules-enabled services.

## Service: firebaserules.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebaserules.googleapis.com/$discovery/rest?version=v1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebaserules.googleapis.com`

## REST Resource: [v1.projects](https://firebase.google.com/docs/reference/rules/rest/v1/projects)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects/test` | `POST /v1/{name=projects/**}:test` Test `Source` for syntactic and semantic correctness. |

## REST Resource: [v1.projects.releases](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/create` | `POST /v1/{name=projects/*}/releases` Create a `Release`. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/delete` | `DELETE /v1/{name=projects/*/releases/**}` Delete a `Release` by resource name. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/get` | `GET /v1/{name=projects/*/releases/**}` Get a `Release` by name. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/getExecutable` | `GET /v1/{name=projects/*/releases/**}:getExecutable` Get the `Release` executable to use when enforcing rules. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/list` | `GET /v1/{name=projects/*}/releases` List the `Release` values for a project. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases/patch` | `PATCH /v1/{name=projects/*/releases/**}` Update a `Release` via PATCH. |

## REST Resource: [v1.projects.rulesets](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/create` | `POST /v1/{name=projects/*}/rulesets` Create a `Ruleset` from `Source`. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/delete` | `DELETE /v1/{name=projects/*/rulesets/*}` Delete a `Ruleset` by resource name. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/get` | `GET /v1/{name=projects/*/rulesets/*}` Get a `Ruleset` by name including the full `Source` contents. |
| `https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets/list` | `GET /v1/{name=projects/*}/rulesets` List `Ruleset` metadata only and optionally filter the results by `Ruleset` name. |