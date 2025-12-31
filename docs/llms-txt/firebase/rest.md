# Source: https://firebase.google.com/docs/reference/firebase-management/rest.md.txt

# Source: https://firebase.google.com/docs/reference/fcmdata/rest.md.txt

# Source: https://firebase.google.com/docs/reference/fcm/rest.md.txt

# Source: https://firebase.google.com/docs/reference/data-connect/rest.md.txt

# Source: https://firebase.google.com/docs/reference/apphosting/rest.md.txt

# Source: https://firebase.google.com/docs/reference/app-distribution/rest.md.txt

# Source: https://firebase.google.com/docs/reference/rules/rest.md.txt

# Source: https://firebase.google.com/docs/reference/rest/database/database-management/rest.md.txt

# Source: https://firebase.google.com/docs/reference/remote-config/rest.md.txt

# Source: https://firebase.google.com/docs/reference/hosting/rest.md.txt

# Source: https://firebase.google.com/docs/reference/crashlytics/rest.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest.md.txt

# Source: https://firebase.google.com/docs/dynamic-links/rest.md.txt

# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest.md.txt

# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest.md.txt

# Source: https://firebase.google.com/docs/reference/rest/storage/rest.md.txt

# Source: https://firebase.google.com/docs/firestore/reference/rest.md.txt

# Source: https://firebase.google.com/docs/dynamic-links/rest.md.txt

# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest.md.txt

# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest.md.txt

# Source: https://firebase.google.com/docs/reference/rest/storage/rest.md.txt

# Cloud Storage for Firebase API

The Cloud Storage for Firebase API enables programmatic management of Cloud Storage buckets for use in Firebase projects

## Service: firebasestorage.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebasestorage.googleapis.com/$discovery/rest?version=v1beta>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebasestorage.googleapis.com`

## REST Resource: [v1beta.projects.buckets](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets)

|                                                                                                                         Methods                                                                                                                          ||
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [addFirebase](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/addFirebase)       | `POST /v1beta/{bucket=projects/*/buckets/*}:addFirebase` Links a Google Cloud Storage bucket to a Firebase project.               |
| [get](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/get)                       | `GET /v1beta/{name=projects/*/buckets/*}` Gets a single linked storage bucket.                                                    |
| [list](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/list)                     | `GET /v1beta/{parent=projects/*}/buckets` Lists the linked storage buckets for a project.                                         |
| [removeFirebase](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/removeFirebase) | `POST /v1beta/{bucket=projects/*/buckets/*}:removeFirebase` Unlinks a linked Google Cloud Storage bucket from a Firebase project. |