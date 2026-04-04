# Source: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases.md.txt

# REST Resource: sites.releases

## Resource: Release

A `Release` is a particular [collection of configurations and files](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions) that is set to be public at a particular time.

| JSON representation |
|---|
| ``` { "name": string, "version": { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`) }, "type": enum (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases#Release.Type`), "releaseTime": string, "releaseUser": { object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/ActingUser`) }, "message": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Output only. The unique identifier for the release, in either of the following formats: - <br /> `sites/SITE_ID/releases/RELEASE_ID` - `sites/SITE_ID/channels/CHANNEL_ID/releases/RELEASE_ID` <br /> This name is provided in the response body when you call [`releases.create`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/create) or [`channels.releases.create`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases/create). <br /> |
| `version` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#Version`)`` Output only. The configuration and content that was released. |
| `type` | ``enum (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels.releases#Release.Type`)`` Explains the reason for the release. Specify a value for this field only when creating a `SITE_DISABLE` type release. |
| `releaseTime` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp` format)`` Output only. The time at which the version is set to be public. A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`. |
| `releaseUser` | ``object (`https://firebase.google.com/docs/reference/hosting/rest/v1beta1/ActingUser`)`` Output only. Identifies the user who created the release. |
| `message` | `string` The deploy description when the release was created. The value can be up to 512 characters. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/create` | Creates a new release, which makes the content of the specified version actively display on the appropriate URL(s). |
| ### `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/get` | Gets the specified release for a site or channel. |
| ### `https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/list` | Lists the releases that have been created for the specified site or channel. |