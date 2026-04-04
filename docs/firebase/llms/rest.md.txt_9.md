# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest.md.txt

# Firebase Realtime Database Management API

The Firebase Realtime Database Management API enables programmatic provisioning and management of Realtime Database instances.

## Service: firebasedatabase.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebasedatabase.googleapis.com/$discovery/rest?version=v1beta>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebasedatabase.googleapis.com`

## REST Resource: [v1beta.projects.locations.instances](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/create` | `POST /v1beta/{parent=projects/*/locations/*}/instances` Requests that a new `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` be created. |
| `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/delete` | `DELETE /v1beta/{name=projects/*/locations/*/instances/*}` Marks a `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` to be deleted. |
| `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/disable` | `POST /v1beta/{name=projects/*/locations/*/instances/*}:disable` Disables a `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance`. |
| `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/get` | `GET /v1beta/{name=projects/*/locations/*/instances/*}` Gets the `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` identified by the specified resource name. |
| `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/list` | `GET /v1beta/{parent=projects/*/locations/*}/instances` Lists each `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` associated with the specified parent project. |
| `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/reenable` | `POST /v1beta/{name=projects/*/locations/*/instances/*}:reenable` Enables a `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance`. |
| `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/undelete` | `POST /v1beta/{name=projects/*/locations/*/instances/*}:undelete` Restores a `https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances#DatabaseInstance` that was previously marked to be deleted. |