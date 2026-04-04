# Source: https://developers.google.com/youtube/v3/live/docs/liveCuepoints/insert.md.txt

# LiveCuepoints: insert

This method has been deprecated and replaced by the
[liveBroadcasts.cuepoint](https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/cuepoint) method.
Inserts a cuepoint into a live broadcast. Currently, requests to this
method must be authorized by an account associated with a YouTube
Content Owner.

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/partner/v1/liveCuepoints
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/live/authentication)).

|                      Scope                       |
|--------------------------------------------------|
| `https://www.googleapis.com/auth/youtubepartner` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                        Parameters                                                                        ||
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                     |||
| `channelId`              | `string` The **channelId** parameter identifies the channel that owns the broadcast into which the cuepoint is being inserted. |
| `onBehalfOfContentOwner` | `string` The **onBehalfOfContentOwner** parameter identifies the content owner that the user is acting on behalf of.           |

### Request body

Provide a [liveCuepoint resource](https://developers.google.com/youtube/v3/live/docs/liveCuepoints#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `broadcastId`
  - `settings.cueType`

  <br />

- You can set values for these properties:

  <br />

  - `settings.offsetTimeMs`
  - `settings.walltime`
  - `settings.durationSecs`

  <br />

## Response

If successful, this method returns a [liveCuepoint resource](https://developers.google.com/youtube/v3/live/docs/liveCuepoints#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|      Error type      |      Error detail       |                         Description                         |
|----------------------|-------------------------|-------------------------------------------------------------|
| `invalidValue (400)` | `conflictingTimeFields` | Only one of `offsetTimeMs` and `walltime` may be specified. |