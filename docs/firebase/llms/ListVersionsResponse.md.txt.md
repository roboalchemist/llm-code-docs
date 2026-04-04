# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/ListVersionsResponse.md.txt

# ListVersionsResponse

Contains a paginated list of `https://firebase.google.com/docs/reference/remote-config/rest/v1/Version` of the RemoteConfig.

| JSON representation |
|---|
| ``` { "versions": [ { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/Version`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `versions[]` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/Version`)`` A list of version metadata objects, sorted in reverse chronological order. |
| `nextPageToken` | `string` Token to retrieve the next page of results, or empty if there are no more results in the list. |