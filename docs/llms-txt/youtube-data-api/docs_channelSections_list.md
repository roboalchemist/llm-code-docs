# Source: https://developers.google.com/youtube/v3/docs/channelSections/list.md.txt

# ChannelSections: list

Returns a list of `channelSection` resources that match the API request criteria.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/channelSections/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/channelSections
```

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                                                                                                                                                                                                                                                                                Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `part`                   | `string` The **part** parameter specifies a comma-separated list of one or more `channelSection` resource properties that the API response will include. If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a `channelSection` resource, the `snippet` property contains other properties, such as a display title for the section. If you set **part=snippet**, the API response will also contain all of those nested properties. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `id` - `snippet`                                                                                                                                                                                  |
| **Filters (specify exactly one of the following parameters)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |||
| `channelId`              | `string` The **channelId** parameter specifies a YouTube channel ID. If a request specifies a value for this parameter, the API will only return the specified channel's sections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `id`                     | `string` The **id** parameter specifies a comma-separated list of IDs that uniquely identify the `channelSection` resources that are being retrieved. In a `channelSection` resource, the `id` property specifies the section's ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `mine`                   | `boolean` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). Set this parameter's value to `true` to retrieve a feed of the channel sections associated with the authenticated user's YouTube channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Optional parameters**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |||
| `hl`                     | `string` This parameter has been deprecated. The **hl** parameter provided support for retrieving localized metadata for a channel section. However, this functionality has been deprecated in YouTube Studio and in the YouTube app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `onBehalfOfContentOwner` | `string` This parameter can only be used in a properly [authorized request](https://developers.google.com/youtube/v3/guides/authentication). **Note:** This parameter is intended exclusively for YouTube content partners. The **onBehalfOfContentOwner** parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#channelSectionListResponse",
  "etag": etag,
  "items": [
    channelSection Resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                   Properties                                                    ||
|-----------|------------------------------------------------------------------------------------------------------|
| `kind`    | `string` Identifies the API resource's type. The value will be `youtube#channelSectionListResponse`. |
| `etag`    | `etag` The Etag of this resource.                                                                    |
| `items[]` | `list` A list of ChannelSections that match the request criteria.                                    |

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|      Error type      |       Error detail        |                                 Description                                 |
|----------------------|---------------------------|-----------------------------------------------------------------------------|
| `forbidden (403)`    | `channelSectionForbidden` | The requester is not allowed to access the requested channel sections.      |
| `invalidValue (400)` | `idInvalid`               | The request specifies an invalid channel section ID.                        |
| `invalidValue (400)` | `invalidCriteria`         | The request could not be completed because the filter criteria are invalid. |
| `notFound (404)`     | `channelNotFound`         | The channel associated with the request cannot be found.                    |
| `notFound (404)`     | `channelSectionNotFound`  | The channel section associated with the request cannot be found.            |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.