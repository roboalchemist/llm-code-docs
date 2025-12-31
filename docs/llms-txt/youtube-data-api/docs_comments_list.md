# Source: https://developers.google.com/youtube/v3/docs/comments/list.md.txt

# Comments: list

Returns a list of comments that match the API request parameters.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/comments/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/comments
```

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                            Parameters                                                                                                                                                                                             ||
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                              |||
| `part`       | `string` The **part** parameter specifies a comma-separated list of one or more `comment` resource properties that the API response will include. The following list contains the `part` names that you can include in the parameter value: - `id` - `snippet`                                                                                                                      |
| **Filters (specify exactly one of the following parameters)**                                                                                                                                                                                                                                                                                                                                        |||
| `id`         | `string` The **id** parameter specifies a comma-separated list of comment IDs for the resources that are being retrieved. In a `comment` resource, the `id` property specifies the comment's ID.                                                                                                                                                                                    |
| `parentId`   | `string` The **parentId** parameter specifies the ID of the comment for which replies should be retrieved. **Note:** YouTube currently supports replies only for top-level comments. However, replies to replies may be supported in the future.                                                                                                                                    |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                              |||
| `maxResults` | `unsigned integer` The **maxResults** parameter specifies the maximum number of items that should be returned in the result set. **Note:** This parameter is not supported for use in conjunction with the [id](https://developers.google.com/youtube/v3/docs/comments/list#id) parameter. Acceptable values are `1` to `100`, inclusive. The default value is `20`.                |
| `pageToken`  | `string` The **pageToken** parameter identifies a specific page in the result set that should be returned. In an API response, the `nextPageToken` property identifies the next page of the result that can be retrieved. **Note:** This parameter is not supported for use in conjunction with the [id](https://developers.google.com/youtube/v3/docs/comments/list#id) parameter. |
| `textFormat` | `string` This parameter indicates whether the API should return comments formatted as HTML or as plain text. The default value is `html`. Acceptable values are: - **html** -- Returns the comments in HTML format. This is the default value. - **plainText** -- Returns the comments in plain text format.                                                                        |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#commentListResponse",
  "etag": etag,
  "nextPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    comment Resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                      Properties                                                                       ||
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#commentListResponse`.                              |
| `etag`                    | `etag` The Etag of this resource.                                                                                          |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set. |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                         |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                   |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                              |
| `items[]`                 | `list` A list of comments that match the request criteria.                                                                 |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |      Error detail       |                                                                                                                                          Description                                                                                                                                           |
|--------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `operationNotSupported` | The id filter is only compatible with comments based on Google+.                                                                                                                                                                                                                               |
| `forbidden (403)`  | `forbidden`             | One or more of the requested comments cannot be retrieved due to insufficient permissions. The request might not be properly authorized.                                                                                                                                                       |
| `notFound (404)`   | `commentNotFound`       | One or more of the specified comments cannot be found. Check the values of the request's [id](https://developers.google.com/youtube/v3/docs/comments/list#id) and [parentId](https://developers.google.com/youtube/v3/docs/comments/list#parentId) parameters to ensure that they are correct. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.