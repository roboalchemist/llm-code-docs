# Source: https://developers.kit.com/api-reference/response-codes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API response codes

> Key response codes you may encounter while using the Kit API

## 401 | Unauthorized

We return the Unauthorized error in a variety of situations, including:

* the authentication method is configured incorrectly or not included on the call
* the incorrect authentication method is used (some endpoints require OAuth)
* an account no longer has access to apps (due to their trial lapsing, being on a free account, failed account payment etc.)

In order to troubleshoot this yourself, please check the error message, which will help you understand why access is not being granted. If this issue persists, please reach out to support.

## 413 | Too many bulk requests

If you try to enqueue too many bulk requests at once, you'll receive an error response with a `413` status code, which your code should gracefully handle. Details on [handling bulk processing can be found here](/api-reference/bulk-and-async-processing).

## 422 | Bad data

When you create or update a field, you may receive an error response with status code `422` if any fields contain bad data or required fields are missing.

## 429 | Rate limiting

We have different rate limits depending on the authentication strategy used:

* When using OAuth, no more than 600 requests over a rolling 60 second period for given access token.
* When using API Keys, no more than 120 requests over a rolling 60 second period for a given API Key.

If your request rate exceeds our limits, you will receive an error response with status code `429`, which your code should gracefully handle. We recommend spacing out your requests and performing an [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) to keep within the limit.

## 500 | Internal server errors

If the server is overloaded or you encounter a bug, you will receive a response with status code `500`. Try again after a short period, and if you continue to encounter an error, please raise the issue with support.


Built with [Mintlify](https://mintlify.com).