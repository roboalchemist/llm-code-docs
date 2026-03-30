# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list.md.txt

# Method: projects.apps.releases.feedbackReports.list

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#body.ListFeedbackReportsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/list#try-it)

Lists feedback reports. By default, sorts by `createTime` in descending order.

### HTTP request

`GET https://firebaseappdistribution.googleapis.com/v1/{parent=projects/*/apps/*/releases/*}/feedbackReports`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The name of the release resource, which is the parent of the feedback report resources. Format: `projects/{projectNumber}/apps/{app}/releases/{release}` Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `parent`: - `firebaseappdistro.releases.list` |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of feedback reports to return. The service may return fewer than this value. The valid range is \[1-100\]; If unspecified (0), at most 25 feedback reports are returned. Values above 100 are coerced to 100. |
| `pageToken` | `string` A page token, received from a previous `feedbackReports.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `feedbackReports.list` must match the call that provided the page token. |

### Request body

The request body must be empty.

### Response body

The response message for `feedbackReports.list`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "feedbackReports": [ { object (`https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports#FeedbackReport`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `feedbackReports[]` | ``object (`https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports#FeedbackReport`)`` The feedback reports |
| `nextPageToken` | `string` A short-lived token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).