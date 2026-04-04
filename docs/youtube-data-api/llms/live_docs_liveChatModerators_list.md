# Source: https://developers.google.com/youtube/v3/live/docs/liveChatModerators/list.md.txt

# LiveChatModerators: list

Lists moderators for a live chat. The request must be authorized by the owner of the live chat's channel.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/liveChatModerators/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/liveChat/moderators
```

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                        Parameters                                                                                                                         ||
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                      |||
| `liveChatId` | `string` The **liveChatId** parameter specifies the YouTube live chat for which the API should return moderators. The live chat ID associated with a broadcast is returned in the `liveBroadcast` resource's `snippet.liveChatId` property. |
| `part`       | `string` The **part** parameter specifies the `liveChatModerator` resource parts that the API response will include. Supported values are `id` and `snippet`.                                                                               |
| **Optional parameters**                                                                                                                                                                                                                                      |||
| `maxResults` | `unsigned integer` The **maxResults** parameter specifies the maximum number of items that should be returned in the result set. Acceptable values are `0` to `50`, inclusive. The default value is `5`.                                    |
| `pageToken`  | `string` The **pageToken** parameter identifies a specific page in the result set that should be returned. In an API response, the `nextPageToken` and `prevPageToken` properties identify other pages that could be retrieved.             |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#liveChatModeratorListResponse",
  "etag": etag,
  "prevPageToken": string,
  "nextPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    liveChatModerator Resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                        Properties                                                                         ||
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#liveChatModeratorListResponse`.                        |
| `etag`                    | `etag` The Etag of this resource.                                                                                              |
| `prevPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the previous page in the result set. |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set.     |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                             |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                       |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                                  |
| `items[]`                 | `list` A list of moderators that match the request criteria.                                                                   |

## Errors

The API does not define any error messages that are unique to this API method. However, this method could still return general API errors listed in the [error message](https://developers.google.com/youtube/v3/live/docs/errors#general) documentation.

## Try it!

Use the APIs Explorer to call this API and see the API request and response.