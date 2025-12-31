# Source: https://developers.google.com/youtube/v3/live/docs/superChatEvents/list.md.txt

# SuperChatEvents: list

List Super Chat events from a channel's live streams in the previous 30 days.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/superChatEvents/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/superChatEvents
```

### Authorization

This request requires authorization with at least one of the following scopes. To read more about authentication and authorization, see [Implementing OAuth 2.0 authentication](https://developers.google.com/youtube/v3/live/authentication).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |
| `https://www.googleapis.com/auth/youtube.readonly`  |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                                                                ||
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |||
| `part`       | `string` The **part** parameter specifies the `superChatEvent` resource parts that the API response will include. Supported values are `id` and `snippet`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |||
| `hl`         | `string` The **hl** parameter instructs the API server to format the [snippet.displayString](https://developers.google.com/youtube/v3/live/docs/superChatEvents#snippet.displayString) property value, which shows the purchase amount and currency of a Super Chat, according to the conventions of a particular language. The parameter value must be a language code included in the list returned by the [i18nLanguages.list](https://developers.google.com/youtube/v3/docs/i18nLanguages/list) method. The default value is `en`, which means that the default behavior is to format display strings as they would be used in English. For example, by default, a string is formatted as `$1.00` rather than `$1,00`. |
| `maxResults` | `unsigned integer` The **maxResults** parameter specifies the maximum number of items that should be returned in the result set. Acceptable values are `1` to `50`, inclusive. The default value is `5`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `pageToken`  | `string` The **pageToken** parameter identifies a specific page in the result set that should be returned. In an API response, the `nextPageToken` and `prevPageToken` properties identify other pages that could be retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#superChatEventListResponse",
  "etag": etag,
  "nextPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    superChatEvent resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                      Properties                                                                       ||
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#superChatEventListResponse`.                       |
| `etag`                    | `etag` The Etag of this resource.                                                                                          |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set. |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                         |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                   |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                              |
| `items[]`                 | `list` A list of Super Chat purchases that match the request criteria.                                                     |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|    Error type     |       Error detail        |                              Description                              |
|-------------------|---------------------------|-----------------------------------------------------------------------|
| `forbidden (403)` | `insufficientPermissions` | The request is not properly authorized to retrieve Super Chat events. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.