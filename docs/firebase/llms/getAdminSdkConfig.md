# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/getAdminSdkConfig.md.txt

# Method: projects.getAdminSdkConfig

Gets the configuration artifact associated with the specified [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject), which can be used by servers to simplify initialization.

Typically, this configuration is used with the Firebase Admin SDK [initializeApp](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) command.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/{name=projects/*/adminSdkConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                            Parameters                                                                                                                                                                                                                                             ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` The resource name of the [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject), in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var>`/adminSdkConfig` Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

|                                          JSON representation                                          |
|-------------------------------------------------------------------------------------------------------|
| ``` { "projectId": string, "databaseURL": string, "storageBucket": string, "locationId": string } ``` |

|                                                                                                                                                                                                                                                                                                                                                     Fields                                                                                                                                                                                                                                                                                                                                                      ||
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project``Id`                    | `string` Immutable. A user-assigned unique identifier for the `FirebaseProject`. This identifier may appear in URLs or names for some Firebase resources associated with the Project, but it should generally be treated as a convenience alias to reference the Project.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `databaseURL` **(deprecated)**   | `string` | This item is deprecated! **DEPRECATED.** *Instead, find the URL of the default Realtime Database instance using the [list endpoint](https://firebase.google.com/docs/reference/rest/database/database-management/rest/v1beta/projects.locations.instances/list) within the Firebase Realtime Database REST API. If the default instance for the Project has not yet been provisioned, the return might not contain a default instance. Note that the config that's generated for the Firebase console or the Firebase CLI uses the Realtime Database endpoint to populate this value for that config.* The URL of the default Firebase Realtime Database instance. |
| `storageBucket` **(deprecated)** | `string` | This item is deprecated! **DEPRECATED.** *Instead, find the name of the default Cloud Storage for Firebase bucket using the [list endpoint](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/list) within the Cloud Storage for Firebase REST API. If the default bucket for the Project has not yet been provisioned, the return might not contain a default bucket. Note that the config that's generated for the Firebase console or the Firebase CLI uses the Cloud Storage for Firebase endpoint to populate this value for that config.* The name of the default Cloud Storage for Firebase bucket.                      |
| `locationId` **(deprecated)**    | `string` | This item is deprecated! **DEPRECATED.** *Instead, use product-specific REST APIs to find the location of each resource in a Project. This field may not be populated, especially for newly provisioned projects after October 30, 2024.* The ID of the Project's ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location), which are resources associated with Google App Engine. The location is one of the available [App Engine locations](https://cloud.google.com/about/locations#region). This field is omitted if the location for default Google Cloud resources has not been set.     |

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/cloud-platform.read-only`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).