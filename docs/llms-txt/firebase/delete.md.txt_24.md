# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/delete.md.txt

# Method: sites.channels.delete

Deletes the specified channel of the specified site.

The `live` channel cannot be deleted.

### HTTP request

`DELETE https://firebasehosting.googleapis.com/v1beta1/{name=sites/*/channels/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. The fully-qualified resource name for the channel, in the format: `sites/SITE_ID/channels/CHANNEL_ID` |

### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).