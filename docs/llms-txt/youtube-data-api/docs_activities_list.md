# Source: https://developers.google.com/youtube/v3/docs/activities/list.md.txt

# Activities: list

YouTube has deprecated the channel bulletin feature. The `activities.list` method does not still return channel bulletins, and the [activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert) method is no longer supported. For more details, please see the [YouTube Help Center](https://support.google.com/youtube?p=channel-bulletins).
Returns a list of channel activity events that match the request criteria. For example, you can retrieve events associated with a particular channel or with the user's own channel.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/activities/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/activities
```

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                    Parameters                                                                                                                                                                                                                                                                                                                                                    ||
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `part`            | `string` The **part** parameter specifies a comma-separated list of one or more `activity` resource properties that the API response will include. If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in an `activity` resource, the `snippet` property contains other properties that identify the type of activity, a display title for the activity, and so forth. If you set **part=snippet**, the API response will also contain all of those nested properties. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `id` - `snippet` |
| **Filters (specify exactly one of the following parameters)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |||
| `channelId`       | `string` The **channelId** parameter specifies a unique YouTube channel ID. The API will then return a list of that channel's activities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `home`            | `boolean` **Note:** This parameter has been deprecated. For requests that set this parameter, the API response contains items similar to those that a logged-out user would see on the YouTube home page. Note that this parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication).                                                                                                                                                                                                                                                                                                                                       |
| `mine`            | `boolean` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). Set this parameter's value to `true` to retrieve a feed of the authenticated user's activities.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |||
| `maxResults`      | `unsigned integer` The **maxResults** parameter specifies the maximum number of items that should be returned in the result set. Acceptable values are `0` to `50`, inclusive. The default value is `5`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `pageToken`       | `string` The **pageToken** parameter identifies a specific page in the result set that should be returned. In an API response, the `nextPageToken` and `prevPageToken` properties identify other pages that could be retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `publishedAfter`  | `datetime` The **publishedAfter** parameter specifies the earliest date and time that an activity could have occurred for that activity to be included in the API response. If the parameter value specifies a day, but not a time, then any activities that occurred that day will be included in the result set. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) (`YYYY-MM-DDThh:mm:ss.sZ`) format.                                                                                                                                                                                                                                                               |
| `publishedBefore` | `datetime` The **publishedBefore** parameter specifies the date and time before which an activity must have occurred for that activity to be included in the API response. If the parameter value specifies a day, but not a time, then any activities that occurred that day will be excluded from the result set. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) (`YYYY-MM-DDThh:mm:ss.sZ`) format.                                                                                                                                                                                                                                                              |
| `regionCode`      | `string` The **regionCode** parameter instructs the API to return results for the specified country. The parameter value is an [ISO 3166-1 alpha-2](http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm) country code. YouTube uses this value when the authorized user's previous activity on YouTube does not provide enough information to generate the activity feed.                                                                                                                                                                                                                                                                            |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#activityListResponse",
  "etag": etag,
  "nextPageToken": string,
  "prevPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    activity Resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                        Properties                                                                         ||
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `kind`                    | `string` Identifies the API resource's type. The value will be `youtube#activityListResponse`.                                 |
| `etag`                    | `etag` The Etag of this resource.                                                                                              |
| `nextPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the next page in the result set.     |
| `prevPageToken`           | `string` The token that can be used as the value of the `pageToken` parameter to retrieve the previous page in the result set. |
| `pageInfo`                | `object` The `pageInfo` object encapsulates paging information for the result set.                                             |
| pageInfo.`totalResults`   | `integer` The total number of results in the result set.                                                                       |
| pageInfo.`resultsPerPage` | `integer` The number of results included in the API response.                                                                  |
| `items[]`                 | `list` A list of activities, or events, that match the request criteria.                                                       |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|      Error type      |       Error detail        |                                                                            Description                                                                             |
|----------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden (403)`    | `forbidden`               | The request is not properly authorized.                                                                                                                            |
| `forbidden (403)`    | `homeParameterDeprecated` | The user's home page activity data is not available through this API. This error might occur if you set the `home` parameter to `true` in an unauthorized request. |
| `notFound (404)`     | `channelNotFound`         | The channel ID identified by the request's `channelId` parameter cannot be found.                                                                                  |
| `notFound (404)`     | `homeChannelNotFound`     | A YouTube home page feed cannot be found for the currently authenticated user.                                                                                     |
| `unauthorized (401)` | `authorizationRequired`   | The request uses the `home` parameter but is not properly authorized.                                                                                              |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.