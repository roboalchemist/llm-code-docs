# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.md.txt

# REST Resource: projects.services

## Resource: Service

The enforcement configuration for a Firebase service supported by App Check.

|                                                        JSON representation                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "enforcementMode": enum (https://firebase.google.com/docs/reference/appcheck/rest/v1/EnforcementMode) } ``` |

|                                                                                                                                                                                                                                                             Fields                                                                                                                                                                                                                                                              ||
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`            | `string` Required. The relative resource name of the service configuration object, in the format: projects/{project_number}/services/{service_id} Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: - `firebasestorage.googleapis.com` (Cloud Storage for Firebase) - `firebasedatabase.googleapis.com` (Firebase Realtime Database) - `firestore.googleapis.com` (Cloud Firestore) - `oauth2.googleapis.com` (Google Identity for iOS) |
| `enforcementMode` | `enum (`[EnforcementMode](https://firebase.google.com/docs/reference/appcheck/rest/v1/EnforcementMode)`)` Required. The App Check enforcement mode for this service.                                                                                                                                                                                                                                                                                                                                         |

|                                                                                                                              ## Methods                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ### [batchUpdate](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/batchUpdate) | Atomically updates the specified [Service](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service) configurations.       |
| ### [get](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/get)                 | Gets the [Service](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service) configuration for the specified service name. |
| ### [list](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/list)               | Lists all [Service](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service) configurations for the specified project.    |
| ### [patch](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/patch)             | Updates the specified [Service](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service) configuration.                   |