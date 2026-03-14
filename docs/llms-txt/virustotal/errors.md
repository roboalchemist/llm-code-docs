# Source: https://virustotal.readme.io/reference/errors.md

# Errors

The VirusTotal API follows the conventional HTTP response codes to indicate success or failure. Codes in the `2xx` range indicate success. Codes in the `4xx` range indicate an error in the request (e.g. a missing parameter, a resource was not found). Codes in the `5xx` range indicate an error in VirusTotal's servers and should be rare.

Unsuccessful requests return additional information about the error in JSON format.

```json
{
  "error": {
    "code": "<error code>",
    "message": "<a message describing the error>"
  }
}
```
```json
{
  "error": {
    "code": "NotFoundError",
    "message": "URL \"thisurlidmakesnosenseatall\" not found"
  }
}
```
```json
{
  "error": {
    "code": "AuthenticationRequiredError",
    "message": "X-Apikey header is missing"
  }
}
```

[block:textarea]
{
  "text": "The error `code` is a string with one of the values provided in the table below. The `message` usually provides a little more information about the error.",
  "sidebar": true
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "HTTP Code",
    "h-1": "Error code",
    "h-2": "Description",
    "0-0": "400",
    "0-1": "BadRequestError",
    "0-2": "The API request is invalid or malformed. The message usually provides details about why the request is not valid.",
    "1-0": "400",
    "1-1": "InvalidArgumentError",
    "1-2": "Some of the provided arguments are incorrect.",
    "2-0": "400",
    "2-1": "NotAvailableYet",
    "2-2": "The resource is not available yet, but will become available later.",
    "3-0": "400",
    "3-1": "UnselectiveContentQueryError",
    "3-2": "Content search query is not selective enough.",
    "4-0": "400",
    "4-1": "UnsupportedContentQueryError",
    "4-2": "Unsupported content search query.",
    "5-0": "401",
    "5-1": "AuthenticationRequiredError",
    "5-2": "The operation requires an authenticated user. Verify that you have provided your API key.",
    "6-0": "401",
    "6-1": "UserNotActiveError",
    "6-2": "The user account is not active. Make sure you properly activated your account by following the link sent to your email.",
    "7-0": "401",
    "7-1": "WrongCredentialsError",
    "7-2": "The provided API key is incorrect.",
    "8-0": "403",
    "8-1": "ForbiddenError",
    "8-2": "You are not allowed to perform the requested operation.",
    "9-0": "404",
    "9-1": "NotFoundError",
    "9-2": "The requested resource was not found.",
    "10-0": "409",
    "10-1": "AlreadyExistsError",
    "10-2": "The resource already exists.",
    "11-0": "424",
    "11-1": "FailedDependencyError",
    "11-2": "The request depended on another request and that request failed.",
    "12-0": "429",
    "12-1": "QuotaExceededError",
    "12-2": "You have exceeded one of your quotas (minute, daily or monthly). Daily quotas are reset every day at 00:00 UTC.  \nYou may have run out of disk space and/or number of files on your VirusTotal Monitor account.",
    "13-0": "429",
    "13-1": "TooManyRequestsError",
    "13-2": "Too many requests.",
    "14-0": "503",
    "14-1": "TransientError",
    "14-2": "Transient server error.  Retry might work.",
    "15-0": "504",
    "15-1": "DeadlineExceededError",
    "15-2": "The operation took too long to complete."
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]