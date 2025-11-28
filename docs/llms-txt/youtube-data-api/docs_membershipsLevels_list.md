# Source: https://developers.google.com/youtube/v3/docs/membershipsLevels/list.md.txt

# MembershipsLevels: list

Note: This endpoint can only be used by individual creators to make requests for their own, channel-memberships-enabled YouTube channel. Reach out to your Google or YouTube representative to request access.

Lists membership levels for the channel that authorized the request. Levels are returned in
implicit display order. API requests to this method yield one of the following responses:

- If the creator has enabled channel memberships and has pricing levels, then the API response contains the list of levels.
- If the creator has enabled channel memberships but has not defined pricing levels, then the API response contains an empty list.
- If the creator has not enabled channel memberships, the API returns a [channelMembershipsNotEnabled](https://developers.google.com/youtube/v3/docs/membershipsLevels/list#errors) error.

**Quota impact:** A call to this method has a
[quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/membershipsLevels
```
This request requires authorization with the following scope:

|                                 Scope                                 |
|-----------------------------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.channel-memberships.creator` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                   Parameters                                                                                                                                   ||
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                           |||
| `part` | `string` The **part** parameter specifies the `membershipsLevel` resource properties that the API response will include. The parameter value is a comma-separated list of resource parts. The following list shows the parts that can be retrieved: - `id` - `snippet` |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#membershipsLevelListResponse",
  "etag": etag,
  "items": [
    membershipsLevel Resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                    Properties                                                     ||
|-----------|--------------------------------------------------------------------------------------------------------|
| `kind`    | `string` Identifies the API resource's type. The value will be `youtube#membershipsLevelListResponse`. |
| `etag`    | `etag` The Etag of this resource.                                                                      |
| `items[]` | `list` A list of `membershipsLevel` resources owned by the channel that authorized the API request.    |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |          Error detail          |                                      Description                                       |
|--------------------|--------------------------------|----------------------------------------------------------------------------------------|
| `badRequest (400)` | `channelMembershipsNotEnabled` | The creator channel authorizing the request does not have channel memberships enabled. |