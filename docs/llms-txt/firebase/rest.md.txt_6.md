# Source: https://firebase.google.com/docs/reference/crashlytics/rest.md.txt

# Firebase Crashlytics API

This service provides an API for mobile app developers to request deletion of user's crash reports.

- [REST Resource: v1alpha.projects.apps.users](https://firebase.google.com/docs/reference/crashlytics/rest#v1alpha.projects.apps.users)

## Service: firebasecrashlytics.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebasecrashlytics.googleapis.com/$discovery/rest?version=v1alpha>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebasecrashlytics.googleapis.com`

## REST Resource: [v1alpha.projects.apps.users](https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/crashlytics/rest/v1alpha/projects.apps.users/deleteCrashReports` | `DELETE /v1alpha/{name=projects/*/apps/*/users/*/crashReports}` Enqueues a request to permanently remove crash reports associated with the specified user. |