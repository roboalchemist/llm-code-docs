# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get.md.txt

# Method: projects.apps.releases.feedbackReports.get

- [HTTP request](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get#body.response_body)
- [Authorization scopes](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get#body.aspect)
- [Try it!](https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports/get#try-it)

Gets a feedback report.

### HTTP request

`GET https://firebaseappdistribution.googleapis.com/v1/{name=projects/*/apps/*/releases/*/feedbackReports/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The name of the feedback report to retrieve. Format: projects/{projectNumber}/apps/{app}/releases/{release}/feedbackReports/{feedback_report} Authorization requires the following [IAM](https://firebase.google.com/docs/projects/iam/overview/) permission on the specified resource `name`: - `firebaseappdistro.releases.list` |

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/app-distribution/rest/v1/projects.apps.releases.feedbackReports#FeedbackReport`.

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).