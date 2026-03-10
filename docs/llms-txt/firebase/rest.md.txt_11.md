# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest.md.txt

# Cloud Testing API

Allows developers to run automated tests for their mobile applications on Google infrastructure.

- [REST Resource: v1.applicationDetailService](https://firebase.google.com/docs/test-lab/reference/testing/rest#v1.applicationDetailService)
- [REST Resource: v1.projects.deviceSessions](https://firebase.google.com/docs/test-lab/reference/testing/rest#v1.projects.deviceSessions)
- [REST Resource: v1.projects.testMatrices](https://firebase.google.com/docs/test-lab/reference/testing/rest#v1.projects.testMatrices)
- [REST Resource: v1.testEnvironmentCatalog](https://firebase.google.com/docs/test-lab/reference/testing/rest#v1.testEnvironmentCatalog)

## Service: testing.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://testing.googleapis.com/$discovery/rest?version=v1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://testing.googleapis.com`

## REST Resource: [v1.applicationDetailService](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails` | `POST /v1/applicationDetailService/getApkDetails` Gets the details of an Android application APK. |

## REST Resource: [v1.projects.deviceSessions](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/cancel` | `POST /v1/{name=projects/*/deviceSessions/*}:cancel` POST /v1/projects/{project_id}/deviceSessions/{device_session_id}:cancel Changes the DeviceSession to state FINISHED and terminates all connections. |
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/create` | `POST /v1/{parent=projects/*}/deviceSessions` POST /v1/projects/{project_id}/deviceSessions |
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/get` | `GET /v1/{name=projects/*/deviceSessions/*}` GET /v1/projects/{project_id}/deviceSessions/{device_session_id} Return a DeviceSession, which documents the allocation status and whether the device is allocated. |
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/list` | `GET /v1/{parent=projects/*}/deviceSessions` GET /v1/projects/{project_id}/deviceSessions Lists device Sessions owned by the project user. |
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.deviceSessions/patch` | `PATCH /v1/{deviceSession.name=projects/*/deviceSessions/*}` PATCH /v1/projects/{projectId}/deviceSessions/deviceSessionId}:updateDeviceSession Updates the current device session to the fields described by the update_mask. |

## REST Resource: [v1.projects.testMatrices](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/cancel` | `POST /v1/projects/{projectId}/testMatrices/{testMatrixId}:cancel` Cancels unfinished test executions in a test matrix. |
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/create` | `POST /v1/projects/{projectId}/testMatrices` Creates and runs a matrix of tests according to the given specifications. |
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices/get` | `GET /v1/projects/{projectId}/testMatrices/{testMatrixId}` Checks the status of a test matrix and the executions once they are created. |

## REST Resource: [v1.testEnvironmentCatalog](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/testEnvironmentCatalog/get` | `GET /v1/testEnvironmentCatalog/{environmentType}` Gets the catalog of supported test environments. |