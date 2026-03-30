# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/introduction/errors.mdx

***

## stoplight-id: 675qkw45eqlou

# Errors

The Cash App Afterpay API uses conventional HTTP status codes and returns error responses in JSON format.

### HTTP status codes

| HTTP Status Codes | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| 200-299           | The request was processed successfully.                            |
| 400-499           | The request was not valid (e.g. a required parameter was missing). |
| 500-599           | The request could not be processed for an unexpected reason.       |

### Error fields

| Field          | Type    | Description                                                                                                                           |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| errorCode      | string  | The type of error returned. For example, `invalid_object`, `unsupported_currency`, or `invalid_token`.                                |
| errorId        | string  | A unique error ID.                                                                                                                    |
| message        | string  | A human-readable message which provides more details about the error. In most cases, these messages can be displayed to the customer. |
| httpStatusCode | integer | The HTTP status code.                                                                                                                 |

### Example errors

#### GET requests

With the exception of [Ping](/cash-app-afterpay/api-reference/reference/service-status/ping), which doesn't require authentication, all GET endpoints can return the following errors:

| HTTP status            | Error code           | Description                                                                                   |
| ---------------------- | -------------------- | --------------------------------------------------------------------------------------------- |
| 401 Unauthorized       | `unauthorized`       | Invalid merchant API credentials were passed in the `Authorization` header.                   |
| 405 Method Not Allowed | `method_not_allowed` | The request was made by a method other than `GET`, `HEAD`, or `OPTIONS`.                      |
| 406 Not Acceptable     | `error`              | The request included an `Accept` header for something other than `application/json` or `*/*`. |

#### POST / PUT requests

All PUT and POST endpoints can return any of the following errors:

| HTTP status                | Error code           | Description                                                                                                                          |
| -------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 400 Bad Request            | `invalid_json`       | The request body contains invalid or improperly formatted JSON.                                                                      |
| 401 Unauthorized           | `unauthorized`       | Invalid Merchant API credentials were passed in the `Authorization` header.                                                          |
| 405 Method Not Allowed     | `method_not_allowed` | The request used an unsupported HTTP method. Only `PUT` or `POST` may be allowed, depending on the endpoint. Use `OPTIONS` to check. |
| 406 Not Acceptable         | `error`              | The `Accept` header was not set to `application/json` or `*/*`.                                                                      |
| 415 Unsupported Media Type | `error`              | The request lacked a `Content-Type` header or used a value other than `application/json`.                                            |
| 500 Internal Server Error  | `error`              | Often caused by a missing or empty request body in `PUT` or `POST` requests.                                                         |
