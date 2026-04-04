# Source: https://firebase.google.com/docs/reference/firebase-management/rest.md.txt

# Firebase Management API

The Firebase Management API enables programmatic setup and management of Firebase projects, including a project's Firebase resources and Firebase apps.

## Workflows: Set up and manage a Firebase project using the REST API

**For a step-by-step example of the workflow to set up and manage Firebase
projects, visit
[Workflow: Set up and manage a project](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project).**

> [!NOTE]
> You can try out calling a Firebase Management REST API method on live
> data using the embedded API Explorer. This API Explorer allows you to see
> the API request and response without leaving the API's reference
> documentation.
>
> Find the embedded explorer in the side-panel of each method's reference page
> (click any method in the tables below).

## Service: firebase.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebase.googleapis.com/$discovery/rest?version=v1beta1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebase.googleapis.com`

## REST Resource: [v1beta1.availableProjects](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/availableProjects)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/availableProjects/list` | `GET /v1beta1/availableProjects` Lists each [Google Cloud `Project`](https://cloud.google.com/resource-manager/reference/rest/v1/projects) that can have Firebase resources added and Firebase services enabled. |

## REST Resource: [v1beta1.operations](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations/get` | `GET /v1beta1/{name=operations/**}` Gets the latest state of a long-running operation. |

## REST Resource: [v1beta1.projects](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase` | `POST /v1beta1/{project=projects/*}:addFirebase` Adds Firebase resources and enables Firebase services in the specified existing [Google Cloud `Project`](https://cloud.google.com/resource-manager/reference/rest/v1/projects). |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addGoogleAnalytics` | `POST /v1beta1/{parent=projects/*}:addGoogleAnalytics` Links the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` with an existing [Google Analytics account](http://www.google.com/analytics/). |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/get` | `GET /v1beta1/{name=projects/*}` Gets the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAdminSdkConfig` | `GET /v1beta1/{name=projects/*/adminSdkConfig}` Gets the configuration artifact associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`, which can be used by servers to simplify initialization. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAnalyticsDetails` | `GET /v1beta1/{name=projects/*/analyticsDetails}` Gets the Google Analytics details currently associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/list` | `GET /v1beta1/projects` Lists each `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` accessible to the caller. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/patch` | `PATCH /v1beta1/{project.name=projects/*}` Updates the attributes of the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/removeAnalytics` | `POST /v1beta1/{parent=projects/*}:removeAnalytics` Unlinks the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` from its Google Analytics account. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/searchApps` | `GET /v1beta1/{parent=projects/*}:searchApps` Lists all available Apps for the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |

## REST Resource: [v1beta1.projects.androidApps](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/create` | `POST /v1beta1/{parent=projects/*}/androidApps` Requests the creation of a new `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp` in the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/get` | `GET /v1beta1/{name=projects/*/androidApps/*}` Gets the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/getConfig` | `GET /v1beta1/{name=projects/*/androidApps/*/config}` Gets the configuration artifact associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/list` | `GET /v1beta1/{parent=projects/*}/androidApps` Lists each `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp` associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/patch` | `PATCH /v1beta1/{app.name=projects/*/androidApps/*}` Updates the attributes of the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/remove` | `POST /v1beta1/{name=projects/*/androidApps/*}:remove` Removes the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp` from the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/undelete` | `POST /v1beta1/{name=projects/*/androidApps/*}:undelete` Restores the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp` to the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |

## REST Resource: [v1beta1.projects.androidApps.sha](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/create` | `POST /v1beta1/{parent=projects/*/androidApps/*}/sha` Adds a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate` to the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/delete` | `DELETE /v1beta1/{name=projects/*/androidApps/*/sha/*}` Removes a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha#ShaCertificate` from the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps.sha/list` | `GET /v1beta1/{parent=projects/*/androidApps/*}/sha` Lists the SHA-1 and SHA-256 certificates for the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp`. |

## REST Resource: [v1beta1.projects.availableLocations](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list (deprecated)` | `GET /v1beta1/{parent=projects/*}/availableLocations` **DECOMMISSIONED.** **If called, this endpoint will return a 404 error.** *Instead, use the applicable resource-specific REST API (or associated documentation, as needed) to determine valid locations for each resource used in your Project.* Lists the valid ["locations for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location) for the specified Project (including a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`). |

## REST Resource: [v1beta1.projects.defaultLocation](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize (deprecated)` | `POST /v1beta1/{parent=projects/*}/defaultLocation:finalize` **DECOMMISSIONED.** **If called, this endpoint will return a 404 error.** *Instead, use the applicable resource-specific REST API to set the location for each resource used in your Project.* Sets the ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location) for the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |

## REST Resource: [v1beta1.projects.iosApps](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/create` | `POST /v1beta1/{parent=projects/*}/iosApps` Requests the creation of a new `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp` in the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/get` | `GET /v1beta1/{name=projects/*/iosApps/*}` Gets the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/getConfig` | `GET /v1beta1/{name=projects/*/iosApps/*/config}` Gets the configuration artifact associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/list` | `GET /v1beta1/{parent=projects/*}/iosApps` Lists each `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp` associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/patch` | `PATCH /v1beta1/{app.name=projects/*/iosApps/*}` Updates the attributes of the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/remove` | `POST /v1beta1/{name=projects/*/iosApps/*}:remove` Removes the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp` from the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/undelete` | `POST /v1beta1/{name=projects/*/iosApps/*}:undelete` Restores the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps#IosApp` to the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |

## REST Resource: [v1beta1.projects.webApps](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/create` | `POST /v1beta1/{parent=projects/*}/webApps` Requests the creation of a new `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` in the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/get` | `GET /v1beta1/{name=projects/*/webApps/*}` Gets the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/getConfig` | `GET /v1beta1/{name=projects/*/webApps/*/config}` Gets the configuration artifact associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/list` | `GET /v1beta1/{parent=projects/*}/webApps` Lists each `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` associated with the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/patch` | `PATCH /v1beta1/{app.name=projects/*/webApps/*}` Updates the attributes of the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/remove` | `POST /v1beta1/{name=projects/*/webApps/*}:remove` Removes the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` from the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |
| `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/undelete` | `POST /v1beta1/{name=projects/*/webApps/*}:undelete` Restores the specified `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp` to the `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. |