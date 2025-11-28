# Source: https://developers.google.com/youtube/v3/docs/members/list.md.txt

# Members: list

Note: This endpoint can only be used by individual creators to make requests for their own, channel-memberships-enabled YouTube channel. Reach out to your Google or YouTube representative to request access.

Lists members (formerly known as "sponsors") for a channel. The API request must be authorized by
the channel owner.

**Quota impact:** A call to this method has a
[quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 2 units.

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/members
```

### Authorization

This request requires authorization with the following scope:

|                                 Scope                                 |
|-----------------------------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.channel-memberships.creator` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |||
| `part`                    | `string` The **part** parameter specifies the `member` resource properties that the API response will include. Set the parameter value to `snippet`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |||
| `mode`                    | `string` The **mode** parameter indicates which members will be included in the API response. Set the parameter value to one of the following values: - `all_current` (default) - List current members, from newest to oldest. When this value is used, the end of the list is reached when the API response does not contain a [nextPageToken](https://developers.google.com/youtube/v3/docs/members/list#nextPageToken). - `updates` - List only members that joined or upgraded since the previous API call. Note that the first call starts a new stream of updates but does not actually return any members. To start retrieving the membership updates, you need to poll the endpoint using the `nextPageToken` at your desired frequency. Note that when this value is used, the API response always contains a [nextPageToken](https://developers.google.com/youtube/v3/docs/members/list#nextPageToken). |
| `maxResults`              | `unsigned integer` The **maxResults** parameter specifies the maximum number of items that should be returned in the result set. Acceptable values are `0` to `1000`, inclusive. The default value is `5`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `pageToken`               | `string` The **pageToken** parameter identifies a specific page in the result set that should be returned. The token is specific to the [mode](https://developers.google.com/youtube/v3/docs/members/list#mode) used with the original API request, so you cannot use a page token retrieved with one mode to subsequently switch to a different mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `hasAccessToLevel`        | `string` The **hasAccessToLevel** parameter value is a level ID that specifies the minimum level that members in the result set should have.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `filterByMemberChannelId` | `string` The **filterByMemberChannelId** parameter specifies a comma-separated list of channel IDs that can be used to check the membership status of specific users. For example, `UC_1,UC_2,UC_3`. A maximum of 100 channels can be specified per call.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "https://developers.google.com/youtube/v3/docs/members/list#kind": "youtube#memberListResponse",
  "https://developers.google.com/youtube/v3/docs/members/list#etag": etag,
  "https://developers.google.com/youtube/v3/docs/members/list#nextPageToken": string,
  "https://developers.google.com/youtube/v3/docs/members/list#pageInfo": {
    "https://developers.google.com/youtube/v3/docs/members/list#totalResults": integer,
    "https://developers.google.com/youtube/v3/docs/members/list#resultsPerPage": integer
  },
  "https://developers.google.com/youtube/v3/docs/members/list#items": [
    member Resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                       Properties                                                                                                                                        ||
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#memberListResponse`.                                                                                                                                                                 |
| `etag`                    | `etag` The Etag of this resource.                                                                                                                                                                                                                            |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set. Page tokens can expire, and your application should drop the token and call the API without a `pageToken` to start a new request. |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                                                                                                                                                           |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                                                                                                                                                     |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                                                                                                                                                                |
| `items[]`                 | `list` A list of members that match the request criteria.                                                                                                                                                                                                    |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |           Error detail           |                                                                                                                                                              Description                                                                                                                                                               |
|--------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `channelMembershipsNotEnabled`   | The creator channel authorizing the request does not have channel memberships enabled.                                                                                                                                                                                                                                                 |
| `badRequest (400)` | `invalidMode`                    | The [mode](https://developers.google.com/youtube/v3/docs/members/list#mode) parameter value is invalid. This error might occur if the [pageToken](https://developers.google.com/youtube/v3/docs/members/list#pageToken) parameter specifies a token that was retrieved using a different mode than the one specified.                  |
| `badRequest (400)` | `invalidPageToken`               | The [pageToken](https://developers.google.com/youtube/v3/docs/members/list#pageToken) parameter value is invalid. This error can occur if the page token used in the request has expired or is not recognized.                                                                                                                         |
| `badRequest (400)` | `invalidHasAccessToLevel`        | The [hasAccessToLevel](https://developers.google.com/youtube/v3/docs/members/list#hasAccessToLevel) parameter value is invalid. There is no level with the specified [id](https://developers.google.com/youtube/v3/docs/membershipsLevels#id).                                                                                         |
| `badRequest (400)` | `invalidFilterByMemberChannelId` | The [filterByMemberChannelId](https://developers.google.com/youtube/v3/docs/members/list#filterByMemberChannelId) parameter value is invalid. This error occurs if the [filterByMemberChannelId](https://developers.google.com/youtube/v3/docs/members/list#filterByMemberChannelId) parameter value specifies more than 100 channels. |