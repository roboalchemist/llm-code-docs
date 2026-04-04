# Source: https://developers.google.com/youtube/v3/docs/guideCategories/list.md.txt

# GuideCategories: list

**Note:** This is a deprecation announcement.  

The `guideCategories` resource and the `guideCategories.list` method have both been deprecated as of September 9, 2020.
Returns a list of categories that can be associated with YouTube channels.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/guideCategories
```

### Parameters

The table below lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                 Parameters                                                                                                                                                  ||
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                        |||
| `part`       | `string` The **part** parameter specifies the `guideCategory` resource properties that the API response will include. Set the parameter value to `snippet`.                                                                                                                                   |
| **Filters (specify exactly one of the following parameters)**                                                                                                                                                                                                                                                  |||
| `id`         | `string` The **id** parameter specifies a comma-separated list of the YouTube channel category ID(s) for the resource(s) that are being retrieved. In a `guideCategory` resource, the `id` property specifies the YouTube channel category ID.                                                |
| `regionCode` | `string` The **regionCode** parameter instructs the API to return the list of guide categories available in the specified country. The parameter value is an [ISO 3166-1 alpha-2](http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm) country code. |
| **Optional parameters**                                                                                                                                                                                                                                                                                        |||
| `hl`         | `string` The **hl** parameter specifies the language that will be used for text values in the API response. The default value is `en-US`.                                                                                                                                                     |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#guideCategoryListResponse",
  "etag": etag,
  "nextPageToken": string,
  "prevPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    guideCategory resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                   Properties                                                                                                   ||
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#guideCategoryListResponse`.                                                                                 |
| `etag`                    | `etag` The Etag of this resource.                                                                                                                                                   |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set.                                                          |
| `prevPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the previous page in the result set.                                                      |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                                                                                  |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                                                                            |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                                                                                       |
| `items[]`                 | `list` A list of categories that can be associated with YouTube channels. In this map, the category ID is the map key, and its value is the corresponding `guideCategory` resource. |

## Errors

The table below identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|    Error type    | Error detail |                                                                                                    Description                                                                                                     |
|------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `notFound (404)` | `notFound`   | The guide category identified by the `id` parameter cannot be found. Use the [guideCategories.list](https://developers.google.com/youtube/v3/docs/guideCategories/list) method to retrieve a list of valid values. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.