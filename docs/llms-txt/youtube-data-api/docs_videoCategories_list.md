# Source: https://developers.google.com/youtube/v3/docs/videoCategories/list.md.txt

# VideoCategories: list

Returns a list of categories that can be associated with YouTube videos.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/videoCategories/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/videoCategories
```

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                 Parameters                                                                                                                                                  ||
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                        |||
| `part`       | `string` The **part** parameter specifies the `videoCategory` resource properties that the API response will include. Set the parameter value to `snippet`.                                                                                                                                   |
| **Filters (specify exactly one of the following parameters)**                                                                                                                                                                                                                                                  |||
| `id`         | `string` The **id** parameter specifies a comma-separated list of video category IDs for the resources that you are retrieving.                                                                                                                                                               |
| `regionCode` | `string` The **regionCode** parameter instructs the API to return the list of video categories available in the specified country. The parameter value is an [ISO 3166-1 alpha-2](http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm) country code. |
| **Optional parameters**                                                                                                                                                                                                                                                                                        |||
| `hl`         | `string` The **hl** parameter specifies the language that should be used for text values in the API response. The default value is `en_US`.                                                                                                                                                   |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#videoCategoryListResponse",
  "etag": etag,
  "nextPageToken": string,
  "prevPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    videoCategory resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                        Properties                                                                                                        ||
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#videoCategoryListResponse`.                                                                                           |
| `etag`                    | `etag` The Etag of this resource.                                                                                                                                                             |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set.                                                                    |
| `prevPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the previous page in the result set.                                                                |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                                                                                            |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                                                                                      |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                                                                                                 |
| `items[]`                 | `list` A list of video categories that can be associated with YouTube videos. In this map, the video category ID is the map key, and its value is the corresponding `videoCategory` resource. |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|    Error type    |      Error detail       |                                                                                                    Description                                                                                                     |
|------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `notFound (404)` | `videoCategoryNotFound` | The video category identified by the `id` parameter cannot be found. Use the [videoCategories.list](https://developers.google.com/youtube/v3/docs/videoCategories/list) method to retrieve a list of valid values. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.