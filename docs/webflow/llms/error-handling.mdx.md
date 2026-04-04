# Source: https://developers.webflow.com/data/reference/error-handling.mdx

***

title: Error handling
slug: reference/error-handling
hidden: false
-------------

The Webflow Data API uses standard HTTP status codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate a client-side error (e.g., a problem with the request), and codes in the `5xx` range indicate a server-side error.

## Error response body

When an error occurs, the API will return a JSON object with the following properties:

| Property            | Type     | Description                                 |
| :------------------ | :------- | :------------------------------------------ |
| `code`              | `string` | A machine-readable error code.              |
| `message`           | `string` | A human-readable error message.             |
| `externalReference` | `string` | A link to more information about the error. |
| `details`           | `array`  | An array of additional error details.       |

**Example error response body:**

```json
{
  "message": "Requested resource not found: The site cannot be found",
  "code": "resource_not_found",
  "externalReference": null,
  "details": []
}
```

## Handling rate limit errors

If your application exceeds the rate limit, you will receive a `429 Too Many Requests` error. When this happens, you should check the `Retry-After` header to see how long you should wait before making another request.

The [official Webflow SDKs](/data/reference/sdks) have built-in exponential backoff, which will automatically handle these retries for you. If you are not using one of our SDKs, you should implement your own retry logic.

For more information, see the [rate limits documentation](/data/reference/rate-limits).

## Common error codes

| Status Code | Code                 | Description                                                                                  |
| :---------- | :------------------- | :------------------------------------------------------------------------------------------- |
| `400`       | `bad_request`        | The request was malformed.                                                                   |
| `401`       | `not_authorized`     | The request lacks valid authentication credentials.                                          |
| `403`       | `forbidden`          | The authenticated user does not have permissions to perform the requested action.            |
| `404`       | `resource_not_found` | The requested resource was not found.                                                        |
| `409`       | `conflict`           | The request could not be completed due to a conflict with the current state of the resource. |
| `429`       | `too_many_requests`  | The user has sent too many requests in a given amount of time.                               |
| `500`       | `internal_error`     | An unexpected error occurred on our end.                                                     |
