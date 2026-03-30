# Source: https://firebase.google.com/docs/reference/hosting/rest.md.txt

# Firebase Hosting API

The Firebase Hosting REST API enables programmatic and customizable management and deployments to your Firebase-hosted sites. Use this REST API to create and manage channels and sites as well as to deploy new or updated hosting configurations and content files.
**For a step-by-step example of the deploy workflow, visit
[Deploy using the REST API](https://firebase.google.com/docs/hosting/api-deploy).**

> [!NOTE]
> You can try out calling a Hosting REST API method on live data using
> the embedded API Explorer. This API Explorer allows you to see the API
> request and response without leaving the API's reference documentation.
>
> Find the embedded explorer in the side-panel of each method's reference
> page (click any method in the tables below).

## Service: firebasehosting.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebasehosting.googleapis.com/$discovery/rest?version=v1beta1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebasehosting.googleapis.com`

## REST Resource: [v1beta1.projects.operations](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.operations/get` | `GET /v1beta1/{name=projects/*/operations/*}` Gets the latest state of a long-running operation. |

## REST Resource: [v1beta1.projects.sites](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/create` | `POST /v1beta1/{parent=projects/*}/sites` Creates a new Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` in the specified parent Firebase project. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/delete` | `DELETE /v1beta1/{name=projects/*/sites/*}` Deletes the specified Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` from the specified parent Firebase project. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/get` | `GET /v1beta1/{name=projects/*/sites/*}` Gets the specified Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/list` | `GET /v1beta1/{parent=projects/*}/sites` Lists each Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site` associated with the specified parent Firebase project. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/patch` | `PATCH /v1beta1/{site.name=projects/*/sites/*}` Updates attributes of the specified Hosting `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites#Site`. |

## REST Resource: [v1beta1.projects.sites.customDomains](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/create` | `POST /v1beta1/{parent=projects/*/sites/*}/customDomains` Creates a `CustomDomain`. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/delete` | `DELETE /v1beta1/{name=projects/*/sites/*/customDomains/*}` Deletes the specified `CustomDomain`. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/get` | `GET /v1beta1/{name=projects/*/sites/*/customDomains/*}` Gets the specified `CustomDomain`. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/list` | `GET /v1beta1/{parent=projects/*/sites/*}/customDomains` Lists each `CustomDomain` associated with the specified parent Hosting site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/patch` | `PATCH /v1beta1/{customDomain.name=projects/*/sites/*/customDomains/*}` Updates the specified `CustomDomain`. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains/undelete` | `POST /v1beta1/{name=projects/*/sites/*/customDomains/*}:undelete` Undeletes the specified `CustomDomain` if it has been soft-deleted. |

## REST Resource: [v1beta1.projects.sites.customDomains.operations](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains.operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains.operations/get` | `GET /v1beta1/{name=projects/*/sites/*/customDomains/*/operations/*}` Gets the latest state of a long-running operation. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains.operations/list` | `GET /v1beta1/{name=projects/*/sites/*/customDomains/*}/operations` Lists operations that match the specified filter in the request. |

## REST Resource: [v1beta1.sites.channels](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/create` | `POST /v1beta1/{parent=sites/*}/channels` Creates a new channel in the specified site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/delete` | `DELETE /v1beta1/{name=sites/*/channels/*}` Deletes the specified channel of the specified site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/get` | `GET /v1beta1/{name=sites/*/channels/*}` Retrieves information for the specified channel of the specified site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/list` | `GET /v1beta1/{parent=sites/*}/channels` Lists the channels for the specified site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/patch` | `PATCH /v1beta1/{channel.name=sites/*/channels/*}` Updates information for the specified channel of the specified site. |

## REST Resource: [v1beta1.sites.channels.releases](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases/create` | `POST /v1beta1/{parent=sites/*/channels/*}/releases` Creates a new release, which makes the content of the specified version actively display on the appropriate URL(s). |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases/get` | `GET /v1beta1/{name=sites/*/channels/*/releases/*}` Gets the specified release for a site or channel. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases/list` | `GET /v1beta1/{parent=sites/*/channels/*}/releases` Lists the releases that have been created for the specified site or channel. |

## REST Resource: [v1beta1.sites.releases](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/create` | `POST /v1beta1/{parent=sites/*}/releases` Creates a new release, which makes the content of the specified version actively display on the appropriate URL(s). |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/get` | `GET /v1beta1/{name=sites/*/releases/*}` Gets the specified release for a site or channel. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/list` | `GET /v1beta1/{parent=sites/*}/releases` Lists the releases that have been created for the specified site or channel. |

## REST Resource: [v1beta1.sites.versions](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/clone` | `POST /v1beta1/{parent=sites/*}/versions:clone` Creates a new version on the specified target site using the content of the specified version. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/create` | `POST /v1beta1/{parent=sites/*}/versions` Creates a new version for the specified site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/delete` | `DELETE /v1beta1/{name=sites/*/versions/*}` Deletes the specified version. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/get` | `GET /v1beta1/{name=sites/*/versions/*}` Get the specified version that has been created for the specified site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/list` | `GET /v1beta1/{parent=sites/*}/versions` Lists the versions that have been created for the specified site. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/patch` | `PATCH /v1beta1/{version.name=sites/*/versions/*}` Updates the specified metadata for the specified version. |
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/populateFiles` | `POST /v1beta1/{parent=sites/*/versions/*}:populateFiles` Adds content files to the specified version. |

## REST Resource: [v1beta1.sites.versions.files](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions.files/list` | `GET /v1beta1/{parent=sites/*/versions/*}/files` Lists the remaining files to be uploaded for the specified version. |