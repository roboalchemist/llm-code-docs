# responseformat

Source: https://developer.ui.com/site-manager/v1.0.0/responseformat

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

Response Format

All Site Manager API responses follow a consistent JSON structure to ensure predictable handling across different endpoints.

Success Response Structure

A successful API response will have the following format:

{
  // Response payload varies by endpoint. The data field can be either an array or an object.
  "data":  []/{},
  "httpStatusCode": 200,
  "traceId": "a7dc15e0eb4527142d7823515b15f87d"
}
The data object/array contains the actual response payload, which varies by endpoint.
The httpStatusCode field indicates the HTTP status of the response (usually 200 for success).
The traceId is a unique identifier for the request useful for troubleshooting.
Error Response Structure

All error responses follow this consistent format:

{
  "code": "NOT_FOUND",
  "httpStatusCode": 404,
  "message": "thing not found: 942A6F00301100000000074A6BA90000000007A3387E0000000063EC9853:714694",
  "traceId": "a7dc15e0eb4527142d7823515b15f87d"
}
code: A machine-readable error code (uppercase string)
httpStatusCode: The HTTP status code (as a number)
message: A detailed description of the error
traceId: A unique identifier for the request (useful for troubleshooting)
Common Error Codes
HTTP Status	Error Code	Description	Example Message
400	BAD_REQUEST	The request was improperly formatted or contained invalid parameters	"invalid request parameters"
401	UNAUTHORIZED	Authentication failed or credentials are missing	"unauthorized"
403	FORBIDDEN	The authenticated user lacks permission to access the resource	"insufficient permissions"
404	NOT_FOUND	The requested resource does not exist	"thing not found: {id}"
429	RATE_LIMIT	The request exceeds the rate limit	"rate limit exceeded, retry after 5.372786998s"
500	SERVER_ERROR	An unexpected error occurred on the server	"failed to get resource by ID"
502	BAD_GATEWAY	The server received an invalid response from an upstream server	"bad gateway"
Handling Errors

When handling errors from the API, we recommend:

Check the HTTP status code first to determine the general category of error
Parse the error code for programmatic handling of specific error conditions
Log the traceId for all errors to assist with troubleshooting
Implement retries with exponential backoff for 429 and 5xx errors
Extract retry information from the header for rate limit errors
Display user-friendly messages based on the error's message

For rate limit errors, parse the retry time from the header and wait at least that long before retrying.