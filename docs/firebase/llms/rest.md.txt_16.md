# Source: https://firebase.google.com/docs/reference/fcm/rest.md.txt

# Firebase Cloud Messaging API

FCM send API that provides a cross-platform messaging solution to reliably deliver messages.

## Service: fcm.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://fcm.googleapis.com/$discovery/rest?version=v1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://fcm.googleapis.com`

## REST Resource: [v1.projects.messages](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send` | `POST /v1/{parent=projects/*}/messages:send` Send a message to specified target (a registration token, topic or condition). |