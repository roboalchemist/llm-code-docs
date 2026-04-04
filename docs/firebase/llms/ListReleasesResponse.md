# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/ListReleasesResponse.md.txt

# ListReleasesResponse

|                                                                        JSON representation                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "releases": [ { object (https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases#Release) } ], "nextPageToken": string } ``` |

|                                                                                                         Fields                                                                                                         ||
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `releases[]`    | `object (`[Release](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases#Release)`)` The list of hashes of files that still need to be uploaded, if any exist.     |
| `nextPageToken` | `string` The pagination token, if more results exist beyond the ones in this response. Include this token in your next call to `releases.list`. Page tokens are short-lived and should not be stored. |