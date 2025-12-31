# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md.txt

# AppOptions interface

Available options to pass to [initializeApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.md#initializeapp_2848fbd).

**Signature:**  

    export interface AppOptions 

## Properties

|                                                                           Property                                                                            |                                                           Type                                                            |                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptionscredential)                                     | [Credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credential_interface) | A [Credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credential_interface) object used to authenticate the Admin SDK.See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for detailed documentation and code samples.                                                                                                                                                                                                                                          |
| [databaseAuthVariableOverride](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptionsdatabaseauthvariableoverride) | object \| null                                                                                                            | The object to use as the [auth](https://firebase.google.com/docs/reference/security/database/#auth) variable in your Realtime Database Rules when the Admin SDK reads from or writes to the Realtime Database. This allows you to downscope the Admin SDK from its default full read and write privileges.You can pass `null` to act as an unauthenticated client.See [Authenticate with limited privileges](https://firebase.google.com/docs/database/admin/start#authenticate-with-limited-privileges) for detailed documentation and code samples. |
| [databaseURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptionsdatabaseurl)                                   | string                                                                                                                    | The URL of the Realtime Database from which to read and write data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [httpAgent](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptionshttpagent)                                       | Agent                                                                                                                     | An [HTTP Agent](https://nodejs.org/api/http.html#http_class_http_agent) to be used when making outgoing HTTP calls. This Agent instance is used by all services that make REST calls (e.g. `auth`, `messaging`, `projectManagement`).Realtime Database and Firestore use other means of communicating with the backend servers, so they do not use this HTTP Agent. `Credential` instances also do not use this HTTP Agent, but instead support specifying an HTTP Agent in the corresponding factory methods.                                        |
| [projectId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptionsprojectid)                                       | string                                                                                                                    | The ID of the Google Cloud project associated with the App.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [serviceAccountId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptionsserviceaccountid)                         | string                                                                                                                    | The ID of the service account to be used for signing custom tokens. This can be found in the `client_email` field of a service account JSON file.                                                                                                                                                                                                                                                                                                                                                                                                     |
| [storageBucket](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.appoptions.md#appoptionsstoragebucket)                               | string                                                                                                                    | The name of the Google Cloud Storage bucket used for storing application data. Use only the bucket name without any prefixes or additions (do \*not\* prefix the name with "gs://").                                                                                                                                                                                                                                                                                                                                                                  |

## AppOptions.credential

A [Credential](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credential_interface) object used to authenticate the Admin SDK.

See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for detailed documentation and code samples.

**Signature:**  

    credential?: Credential;

## AppOptions.databaseAuthVariableOverride

The object to use as the [auth](https://firebase.google.com/docs/reference/security/database/#auth) variable in your Realtime Database Rules when the Admin SDK reads from or writes to the Realtime Database. This allows you to downscope the Admin SDK from its default full read and write privileges.

You can pass `null` to act as an unauthenticated client.

See [Authenticate with limited privileges](https://firebase.google.com/docs/database/admin/start#authenticate-with-limited-privileges) for detailed documentation and code samples.

**Signature:**  

    databaseAuthVariableOverride?: object | null;

## AppOptions.databaseURL

The URL of the Realtime Database from which to read and write data.

**Signature:**  

    databaseURL?: string;

## AppOptions.httpAgent

An [HTTP Agent](https://nodejs.org/api/http.html#http_class_http_agent) to be used when making outgoing HTTP calls. This Agent instance is used by all services that make REST calls (e.g. `auth`, `messaging`, `projectManagement`).

Realtime Database and Firestore use other means of communicating with the backend servers, so they do not use this HTTP Agent. `Credential` instances also do not use this HTTP Agent, but instead support specifying an HTTP Agent in the corresponding factory methods.

**Signature:**  

    httpAgent?: Agent;

## AppOptions.projectId

The ID of the Google Cloud project associated with the App.

**Signature:**  

    projectId?: string;

## AppOptions.serviceAccountId

The ID of the service account to be used for signing custom tokens. This can be found in the `client_email` field of a service account JSON file.

**Signature:**  

    serviceAccountId?: string;

## AppOptions.storageBucket

The name of the Google Cloud Storage bucket used for storing application data. Use only the bucket name without any prefixes or additions (do \*not\* prefix the name with "gs://").

**Signature:**  

    storageBucket?: string;