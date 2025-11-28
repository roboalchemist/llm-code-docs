# Source: https://developers.google.com/youtube/v3/live/docs/sponsors/list.md.txt

# Sponsors: list

Note: This method is deprecated as of March 31, 2020. It has been replaced by the [members.list](https://developers.google.com/youtube/v3/docs/members/list) method. You can find information about that method in the YouTube Data API documentation.  

The `sponsors.list` method will no longer be supported on or after September 30, 2020. API clients should update calls to the `sponsors.list` method to use the [members.list](https://developers.google.com/youtube/v3/docs/members/list) method instead.

Lists members (formerly known as "sponsors") for a channel. The API request must be authorized
by the channel owner.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/live/docs/sponsors/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/sponsors
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

|                                                                                                                                                                                                                    Parameters                                                                                                                                                                                                                     ||
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                              |||
| `part`       | `string` The **part** parameter specifies the `sponsor` resource parts that the API response will include. Supported values are `id` and `snippet`.                                                                                                                                                                                                                                                                                 |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                              |||
| `filter`     | `string` The **filter** parameter specifies which channel sponsors to return. The default value is `newest`. Acceptable values are: - **all** -- Return all sponsors, from newest to oldest. - **newest** -- Return one page of the most recent sponsors. Subsequent requests using the [nextPageToken](https://developers.google.com/youtube/v3/live/docs/sponsors/list#nextPageToken) retrieve newer subscribers as they sign up. |
| `maxResults` | `unsigned integer` The **maxResults** parameter specifies the maximum number of items that should be returned in the result set. Acceptable values are `0` to `50`, inclusive. The default value is `5`.                                                                                                                                                                                                                            |
| `pageToken`  | `string` The **pageToken** parameter identifies a specific page in the result set that should be returned. In an API response, the `nextPageToken` and `prevPageToken` properties identify other pages that could be retrieved.                                                                                                                                                                                                     |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#sponsorListResponse",
  "etag": etag,
  "nextPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    sponsor resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                      Properties                                                                       ||
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#sponsorListResponse`.                              |
| `etag`                    | `etag` The Etag of this resource.                                                                                          |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set. |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                         |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                   |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                              |
| `items[]`                 | `list` A list of sponsors that match the request criteria.                                                                 |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/live/docs/errors) documentation for more detail.

|      Error type      |            Error detail             |                                Description                                |
|----------------------|-------------------------------------|---------------------------------------------------------------------------|
| `forbidden (403)`    | `insufficientPermissions`           | You do not have the necessary permissions to view the channel's sponsors. |
| `invalidValue (400)` | `invalidValueInRequest`             | The request contains an invalid value.                                    |
| `invalidValue (400)` | `sponsorshipNotEnabledForChannelId` | The channel does not have sponsorships enabled.                           |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.