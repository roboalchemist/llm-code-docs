# Source: https://developers.google.com/youtube/v3/docs/i18nLanguages/list.md.txt

# I18nLanguages: list

Returns a list of application languages that the YouTube website supports.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 1 unit.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/i18nLanguages/list#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
GET https://www.googleapis.com/youtube/v3/i18nLanguages
```

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                             Parameters                                                                             ||
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                               |||
| `part` | `string` The **part** parameter specifies the `i18nLanguage` resource properties that the API response will include. Set the parameter value to `snippet`. |
| **Optional parameters**                                                                                                                                               |||
| `hl`   | `string` The **hl** parameter specifies the language that should be used for text values in the API response. The default value is `en_US`.                |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns a response body with the following structure:  

```objective-c
{
  "kind": "youtube#i18nLanguageListResponse",
  "etag": etag,
  "items": [
    i18nLanguage resource
  ]
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                             Properties                                                                              ||
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`    | `string` Identifies the API resource's type. The value will be `youtube#i18nLanguageListResponse`.                                                       |
| `etag`    | `etag` The Etag of this resource.                                                                                                                        |
| `items[]` | `list` A list of supported i18n languages. In this map, the i18n language ID is the map key, and its value is the corresponding `i18nLanguage` resource. |

## Errors

The API does not define any error messages that are unique to this API method. However, this method could still return general API errors listed in the [error message](https://developers.google.com/youtube/v3/docs/errors#general) documentation.

## Try it!

Use the APIs Explorer to call this API and see the API request and response.