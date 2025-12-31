# Source: https://developers.google.com/youtube/v3/docs/subscriptions/insert.md.txt

# Subscriptions: insert

Adds a subscription for the authenticated user's channel.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/subscriptions/insert#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
POST https://www.googleapis.com/youtube/v3/subscriptions
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtubepartner`    |
| `https://www.googleapis.com/auth/youtube`           |
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                                                                                                                                                            Parameters                                                                                                                                                                             ||
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                                                                                                                                                                                                                                                                              |||
| `part` | `string` The **part** parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. The following list contains the `part` names that you can include in the parameter value: - `contentDetails` - `id` - `snippet` - `subscriberSnippet` |

### Request body

Provide a [subscription resource](https://developers.google.com/youtube/v3/docs/subscriptions#resource) in the request body.
For that resource:

- You must specify a value for these properties:

  <br />

  - `snippet.resourceId`

  <br />

- You can set values for these properties:

  <br />

  - `snippet.resourceId`

  <br />

## Response

If successful, this method returns a [subscription resource](https://developers.google.com/youtube/v3/docs/subscriptions#resource) in the response body.

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |      Error detail       |                                                                    Description                                                                     |
|--------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `subscriptionDuplicate` | The subscription that you are trying to create already exists.                                                                                     |
| `badRequest (400)` | `subscriptionForbidden` | You have reached your maximum number of subscriptions.                                                                                             |
| `badRequest (400)` | `subscriptionForbidden` | Subscribing to your own channel is not supported.                                                                                                  |
| `badRequest (400)` | `subscriptionForbidden` | Too many recent subscriptions. Please try again in a few hours.                                                                                    |
| `forbidden (403)`  | `subscriptionForbidden` | The request is not properly authenticated or not supported for this channel.                                                                       |
| `notFound (404)`   | `publisherNotFound`     | The resource specified by the request's `snippet.resourceId` property cannot be found.                                                             |
| `notFound (404)`   | `subscriberNotFound`    | The subscriber identified with the request cannot be found.                                                                                        |
| `required (400)`   | `publisherRequired`     | The subscription resource specified in the request must use the `snippet.resourceId` property to identify the channel that is being subscribed to. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.