# Source: https://developers-classic.mailerlite.com/docs/response.md

# Response

API response is JSON formatted and it has `Content-Type: application/json` header.

[block:api-header]
{
  "type": "basic",
  "title": "HTTP status codes"
}
[/block]

MailerLite uses standard HTTP response codes.

[block:parameters]
{
  "data": {
    "h-0": "HTTP code",
    "h-1": "",
    "0-0": "200",
    "3-0": "400",
    "3-1": "Bad Request",
    "0-1": "OK",
    "4-0": "401",
    "4-1": "Unauthorized",
    "h-2": "Description",
    "3-2": "The request could not be understood by the server due to malformed syntax.",
    "4-2": "The request requires user authentication.",
    "0-2": "The request succeeded.",
    "h-3": "",
    "5-0": "404",
    "5-1": "Not Found",
    "3-3": "",
    "4-3": "",
    "5-2": "The server has not found anything matching the Request-URI. No indication is given of whether the condition is temporary or permanent.",
    "5-3": "",
    "1-0": "201",
    "2-0": "204",
    "1-1": "Created",
    "2-1": "No Content",
    "1-2": "The request was fulfilled and resulted in a new resource being created.",
    "2-2": "The server fulfilled the request but does not need to return an entity-body, i.e. when resource is deleted.",
    "6-0": "500",
    "6-1": "Internal Server Error",
    "6-2": "The server encountered an unexpected condition which prevented it from fulfilling the request."
  },
  "cols": 3,
  "rows": 7
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Response with error"
}
[/block]

Every error has the structure described below.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "0-0": "error",
    "0-1": "`Object`",
    "1-0": "error.code",
    "1-1": "`Integer`",
    "2-0": "error.message",
    "2-1": "`String`",
    "h-1": "Type",
    "h-2": "Description",
    "2-2": "Readable message about the error occurred",
    "1-2": "*Optional* Code of error",
    "0-2": "Object that contains data about error"
  },
  "cols": 3,
  "rows": 3
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"error\": {\n    \"code\": 123,\n    \"message\": \"Group not found\"\n  }\n}",
      "language": "json",
      "name": "Error Response Example"
    }
  ]
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "API error codes"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Error code",
    "h-1": "Message",
    "h-2": "Description",
    "2-0": "302",
    "2-1": "API-Key Unauthorized",
    "1-0": "2",
    "1-1": "Endpoint not found",
    "1-2": "The endpoint you are trying to use is non-existing",
    "2-2": "You are trying to use an invalid API key to authorize",
    "0-0": "1",
    "0-1": "Unauthorized",
    "0-2": "API key is required and is not provided",
    "3-0": "429",
    "3-1": "Too many requests",
    "3-2": "You reached the API rate limit"
  },
  "cols": 3,
  "rows": 4
}
[/block]