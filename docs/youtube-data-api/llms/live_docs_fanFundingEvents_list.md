# Source: https://developers.google.com/youtube/v3/live/docs/fanFundingEvents/list.md.txt

# FanFundingEvents: list

**Note:** This is a deprecation announcement.  

The Fan Funding feature has been deprecated, and the Fan Funding API will be turned off on February 28, 2017. This deprecation announcement coincides with the release of YouTube's new [Super Chat](https://youtube.googleblog.com/2017/01/can-we-chat-hello-super-chat.html) feature.
Lists fan funding events for a channel. The API request must be authorized by the channel owner.

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/fanFundingEvents
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/live/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |
| `https://www.googleapis.com/auth/youtube.readonly`  |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                      Parameters                                                                                                                                                                                                                                                                       ||
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |||
| `part`       | `string` The **part** parameter specifies the `fanFundingEvent` resource parts that the API response will include. Supported values are `id` and `snippet`.                                                                                                                                                                                                                                                                                                                                                                             |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |||
| `hl`         | `string` The **hl** parameter instructs the API to retrieve a localized currency display string for a specific [application language that the YouTube website supports](https://developers.google.com/youtube/v3/docs/i18nLanguages). For example, in English, currency would be displayed as `$1.50`, but in French, it would be displayed as `1,50$`. The parameter value must be a language code included in the list returned by the [i18nLanguages.list](https://developers.google.com/youtube/v3/docs/i18nLanguages/list) method. |
| `maxResults` | `unsigned integer` The **maxResults** parameter specifies the maximum number of items that should be returned in the result set. Acceptable values are `0` to `50`, inclusive. The default value is `5`.                                                                                                                                                                                                                                                                                                                                |
| `pageToken`  | `string` The **pageToken** parameter identifies the specific page in the result set that the API server is being asked to return. In an API response, the `nextPageToken` property identifies the next page of results for the request.                                                                                                                                                                                                                                                                                                 |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#fanFundingEventListResponse",
  "etag": etag,
  "nextPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    fanFundingEvent resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                      Properties                                                                       ||
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#fanFundingEventListResponse`.                      |
| `etag`                    | `etag` The Etag of this resource.                                                                                          |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set. |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                         |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                   |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                              |
| `items[]`                 | `list` A list of fan funding events that match the request criteria.                                                       |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|      Error type      |            Error detail            |                                     Description                                     |
|----------------------|------------------------------------|-------------------------------------------------------------------------------------|
| `forbidden (403)`    | `insufficientPermissions`          | You do not have the necessary permissions to view the channel's Fan Funding events. |
| `invalidValue (400)` | `fanFundingNotEnabledForChannelId` | The channel does not have Fan Funding enabled.                                      |

## Try it!

Use the API Explorer to call this method on live data and see the API request and response.