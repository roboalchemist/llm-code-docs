# Source: https://firebase.google.com/docs/reference/rest/storage/rest/indexv1alpha.md.txt

# Cloud Storage for Firebase API

The Cloud Storage for Firebase API enables programmatic management of Cloud Storage buckets for use in Firebase projects

## Service: firebasestorage.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebasestorage.googleapis.com/$discovery/rest?version=v1alpha>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebasestorage.googleapis.com`

## REST Resource: [v1alpha.projects](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects)

|                                                                                                                        Methods                                                                                                                         ||
|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [deleteDefaultBucket](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects/deleteDefaultBucket) | `DELETE /v1alpha/{name=projects/*/defaultBucket}` Unlinks and deletes the default bucket for the specified Firebase project. |
| [getDefaultBucket](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects/getDefaultBucket)       | `GET /v1alpha/{name=projects/*/defaultBucket}` Gets the default bucket for the specified Firebase project.                   |

## REST Resource: [v1alpha.projects.buckets](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets)

|                                                                                                                                   Methods                                                                                                                                    ||
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [addFirebase](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/addFirebase)       | `POST /v1alpha/{bucket=projects/*/buckets/*}:addFirebase` Links a Google Cloud Storage bucket to the specified Firebase project.                     |
| [get](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/get)                       | `GET /v1alpha/{name=projects/*/buckets/*}` Gets the specified linked Cloud Storage for Firebase bucket.                                              |
| [list](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/list)                     | `GET /v1alpha/{parent=projects/*}/buckets` Lists the linked Cloud Storage for Firebase buckets for the specified Firebase project.                   |
| [removeFirebase](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/removeFirebase) | `POST /v1alpha/{bucket=projects/*/buckets/*}:removeFirebase` Unlinks a linked Cloud Storage for Firebase bucket from the specified Firebase project. |

## REST Resource: [v1alpha.projects.defaultBucket](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket)

|                                                                                                                         Methods                                                                                                                          ||
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [create](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create) | `POST /v1alpha/{parent=projects/*}/defaultBucket` Creates the default Cloud Storage bucket and links it to the specified Firebase project. |