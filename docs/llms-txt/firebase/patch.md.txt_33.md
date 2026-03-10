# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels/patch.md.txt

# Method: sites.channels.patch

Updates information for the specified channel of the specified site.

Implicitly creates the channel if it doesn't already exist.

### HTTP request

`PATCH https://firebasehosting.googleapis.com/v1beta1/{channel.name=sites/*/channels/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `channel.name` | `string` The fully-qualified resource name for the channel, in the format: `sites/SITE_ID/channels/CHANNEL_ID` |

### Query parameters

| Parameters ||
|---|---|
| `updateMask` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask` format)`` A comma-separated list of fields to be updated in this request. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. |

### Request body

The request body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels#Channel`.

### Response body

If successful, the response body contains an instance of `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels#Channel`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/firebase.hosting`
- `
  https://www.googleapis.com/auth/firebase`
- `
  https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).