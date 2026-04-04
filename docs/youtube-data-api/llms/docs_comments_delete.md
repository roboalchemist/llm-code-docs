# Source: https://developers.google.com/youtube/v3/docs/comments/delete.md.txt

# Comments: delete

Deletes a comment.

**Quota impact:** A call to this method has a [quota cost](https://developers.google.com/youtube/v3/getting-started#quota) of 50 units.

## Common use cases

The list below shows common use cases for this method. Hover over a use case to see its description, or click on a use case to load sample parameter values in the APIs Explorer. You can open the [fullscreen APIs Explorer](https://developers.google.com/youtube/v3/docs/comments/delete#) to see code samples that dynamically update to reflect the parameter values entered in the Explorer.

The table below shows common use cases for this method. You can click on a use case name to load sample parameter values in the APIs Explorer. Or you can see code samples for a use case in the fullscreen APIs Explorer by clicking on the code icon below a use case name. In the fullscreen UI, you can update parameter and property values and the code samples will dynamically update to reflect the values you enter.  
This method has one common use case, which is described below. The buttons below the description populate the APIs Explorer with sample values or open the fullscreen APIs Explorer to show code samples that use those values. The code samples also dynamically update if you change the values.

<br />

## Request

### HTTP request

```
DELETE https://www.googleapis.com/youtube/v3/comments
```

### Authorization

This request requires authorization with at least one of the following scopes ([read more about authentication and authorization](https://developers.google.com/youtube/v3/guides/authentication)).

|                        Scope                        |
|-----------------------------------------------------|
| `https://www.googleapis.com/auth/youtube.force-ssl` |

### Parameters

The following table lists the parameters that this query supports. All of the parameters listed are query parameters.

|                                              Parameters                                              ||
|------|------------------------------------------------------------------------------------------------|---|
| **Required parameters**                                                                                 |||
| `id` | `string` The **id** parameter specifies the comment ID for the resource that is being deleted. |

### Request body

Do not provide a request body when calling this method.

## Response

If successful, this method returns an HTTP `204` response code (`No Content`).

## Errors

The following table identifies error messages that the API could return in response to a call to this method. Please see the [error message](https://developers.google.com/youtube/v3/docs/errors) documentation for more detail.

|     Error type     |    Error detail     |                                                                                        Description                                                                                        |
|--------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest (400)` | `processingFailure` | The API server failed to successfully process the request. While this can be a transient error, it usually indicates that the request's input is invalid.                                 |
| `forbidden (403)`  | `forbidden`         | The comment could not be deleted because of insufficient permissions. The request might not be properly authorized.                                                                       |
| `notFound (404)`   | `commentNotFound`   | The specified comment could not be found. Check the value of the request's [id](https://developers.google.com/youtube/v3/docs/comments/delete#id) parameter to ensure that it is correct. |

## Try it!

Use the APIs Explorer to call this API and see the API request and response.