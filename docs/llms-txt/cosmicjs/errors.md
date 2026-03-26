# Source: https://www.cosmicjs.com/docs/api/errors.md

# Errors

Learn how to handle errors with the Cosmic API.

## Status codes

The Cosmic API uses the following status codes:

| Status code        | Meaning                                                              |
| ------------------ | -------------------------------------------------------------------- |
| 200                | OK - Everything worked as expected.                                  |
| 400                | Bad Request - Your request is invalid.                               |
| 401                | Unauthorized - Your access key is incorrect.                         |
| 402                | Payment Required - Your Bucket needs to be upgraded to continue use. |
| 403                | Forbidden - You are not allowed to access this content.              |
| 404                | Not Found - The requested resource doesn't exist.                    |
| 429                | Too Many Requests - Too many requests hit the API too quickly.       |
| 500, 502, 503, 504 | Internal Server Error - Something went wrong on our end.             |

## Error response model

Here is the error response model that you can expect:

The status code from the table above.

A verbose error message that will try to hint at any possible issues with
the request.

## Error example

Error messages will attempt to be as specific as possible with what went wrong. For example, if there was an invalid property in a request the following format can be expected:
```json
{
  "status": 400,
  "message": "Metafield validation: invalid 'value' for metafield with key: 'number' and type: 'number'"
}

```