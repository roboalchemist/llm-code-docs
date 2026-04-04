# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize.md.txt

# Method: projects.defaultLocation.finalize

| This item is deprecated!
**DECOMMISSIONED.** **If called, this endpoint will return a 404 error.** *Instead, use the applicable resource-specific REST API to set the location for each resource used in your Project.*

Sets the ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location) for the specified [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject).

This method creates a Google App Engine application with a [default Cloud Storage bucket](https://cloud.google.com/appengine/docs/standard/python/googlecloudstorageclient/setting-up-cloud-storage#activating_a_cloud_storage_bucket), located in the specified [`locationId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize#body.request_body.FIELDS.location_id). This location must be one of the available [App Engine locations](https://cloud.google.com/about/locations#region).

After the location for default Google Cloud resources is finalized, or if it was already set, it cannot be changed. The location for default Google Cloud resources for the specified `FirebaseProject` might already be set because either the underlying Google Cloud `Project` already has an App Engine application or `defaultLocation.finalize` was previously called with a specified `locationId`.

The result of this call is an [`Operation`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations), which can be used to track the provisioning process. The [`response`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.response) type of the `Operation` is [google.protobuf.Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty).

The `Operation` can be polled by its `name` using `operations.get` until `done` is true. When `done` is true, the `Operation` has either succeeded or failed. If the `Operation` has succeeded, its [`response`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation.FIELDS.response) will be set to a [google.protobuf.Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty); if the `Operation` has failed, its `error` will be set to a [google.rpc.Status](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Status). The `Operation` is automatically deleted after completion, so there is no need to call `operations.delete`.

All fields listed in the [request body](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize#request-body) are required.

To call `defaultLocation.finalize`, a member must be an Owner of the Project.

### HTTP request

`POST https://firebase.googleapis.com/v1beta1/{parent=projects/*}/defaultLocation:finalize`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                ||
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parent` | `string` The resource name of the [FirebaseProject](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject) for which the ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location) will be set, in the format: `projects/`<var translate="no">PROJECT_IDENTIFIER</var> Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. |

### Request body

The request body contains data with the following structure:

|       JSON representation        |
|----------------------------------|
| ``` { "locationId": string } ``` |

|                                                                                                                                                                                    Fields                                                                                                                                                                                     ||
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `location``Id` | `string` **DEPRECATED** The ID of the Project's ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location), which are resources associated with Google App Engine. The location must be one of the available [Google App Engine locations](https://cloud.google.com/about/locations#region). |

### Response body

If successful, the response body contains an instance of [Operation](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/operations#Operation).

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `
  https://www.googleapis.com/auth/firebase`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).