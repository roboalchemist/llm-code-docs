# Source: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list.md.txt

# Method: projects.availableLocations.list

> [!WARNING]
> This item is deprecated!

**DECOMMISSIONED.** **If called, this endpoint will return a 404 error.** *Instead, use the applicable resource-specific REST API (or associated documentation, as needed) to determine valid locations for each resource used in your Project.*

Lists the valid ["locations for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location) for the specified Project (including a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`).

One of these locations can be selected as the Project's location for default Google Cloud resources, which is the geographical location where the Project's resources associated with Google App Engine (such as the default Cloud Firestore instance) will be provisioned by default. However, if the location for default Google Cloud resources has already been set for the Project, then this setting cannot be changed.

This call checks for any possible [location restrictions](https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations) for the specified Project and, thus, might return a subset of all possible locations. To list all locations (regardless of any restrictions), call the endpoint without specifying a unique project identifier (that is, `/v1beta1/{parent=projects/-}/listAvailableLocations`).

To call `availableLocations.list` with a specified project, a member must be at minimum a Viewer of the Project. Calls without a specified project do not require any specific project permissions.

### HTTP request

`GET https://firebase.googleapis.com/v1beta1/{parent=projects/*}/availableLocations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` The `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject` for which to list [locations for default Google Cloud resources](https://firebase.google.com/docs/projects/locations#default-cloud-location), in the format: `projects/PROJECT_IDENTIFIER` Refer to the `FirebaseProject` [`name`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.name) field for details about <var translate="no">PROJECT_IDENTIFIER</var> values. If no unique project identifier is specified (that is, `projects/-`), the returned list does not take into account org-specific or project-specific location restrictions. |

### Query parameters

| Parameters ||
|---|---|
| `pageToken` | `string` Token returned from a previous call to `availableLocations.list` indicating where in the list of locations to resume listing. |
| `pageSize` | `integer` The maximum number of locations to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. This value cannot be negative. |

### Request body

The request body must be empty.

### Response body

> [!WARNING]
> This item is deprecated!

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "locations": [ { object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list#Location`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `locations[]` | ``object (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list#Location`)`` One page of results from a call to `availableLocations.list`. |
| `nextPageToken` | `string` If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results and all available locations have been listed. This token can be used in a subsequent call to `availableLocations.list` to find more locations. Page tokens are short-lived and should not be persisted. |

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

## Location

> [!WARNING]
> This item is deprecated!

**DEPRECATED.** *This Location is no longer used to determine Firebase resource locations. Instead, consult product documentation to determine valid locations for each resource used in your Project.*

A ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location) that can be selected for a `https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject`. These are resources associated with Google App Engine.

| JSON representation |
|---|
| ``` { "locationId": string, "type": enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list#LocationType`), "features": [ enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list#LocationFeature`) ] } ``` |

| Fields ||
|---|---|
| `locationId` | `string` The ID of the Project's location for default Google Cloud resources. It will be one of the available [Google App Engine locations](https://cloud.google.com/about/locations#region). |
| `type` | ``enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list#LocationType`)`` Indicates whether the location for default Google Cloud resources is a [regional or multi-regional location](https://firebase.google.com/docs/projects/locations#types) for data replication. |
| `features[]` | ``enum (`https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list#LocationFeature`)`` Products and services that are available in the location for default Google Cloud resources. |

## LocationType

Specifies how data is replicated within the location for default Google Cloud resources. Learn more about the [types of locations](https://cloud.google.com/about/locations#region).

| Enums ||
|---|---|
| `LOCATION_TYPE_UNSPECIFIED` | Used internally for distinguishing unset values and is not intended for external use. |
| `REGIONAL` | The location is a regional location. Data in a regional location is replicated in multiple zones within a region. |
| `MULTI_REGIONAL` | The location is a multi-regional location. Data in a multi-region location is replicated in multiple regions. Within each region, data is replicated in multiple zones. |

## LocationFeature

Products and services that are available in the location for default Google Cloud resources.

| Enums ||
|---|---|
| `LOCATION_FEATURE_UNSPECIFIED` | Used internally for distinguishing unset values and is not intended for external use. |
| `FIRESTORE` | This location supports Cloud Firestore database instances. Google App Engine is available in this location, so it can be a Project's location for default Google Cloud resources. |
| `DEFAULT_STORAGE` | This location supports default Cloud Storage buckets. Google App Engine is available in this location, so it can be a Project's location for default Google Cloud resources. |
| `FUNCTIONS` | Cloud Functions for Firebase is available in this location. |