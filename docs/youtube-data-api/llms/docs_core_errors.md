# Source: https://developers.google.com/youtube/v3/docs/core_errors.md.txt

# Google APIs - Global domain errors

This document identifies some of the error codes and messages that Google APIs return. Specifically, the errors listed here are in the global, or default, domain for Google APIs. Many APIs also define their own domains, which identify API-specific errors that are not in the global domain. For those errors, the value of the `domain` property in the JSON response will be an API-specific value, such as `youtube.parameter`.

This page lists errors by their HTTP status codes as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6).

The sample JSON response below demonstrates how a global error is communicated:  

```transact-sql
{
 "error": {
  "errors": [
   {
    "domain": "global",
    "reason": "invalidParameter",
    "message": "Invalid string value: 'asdf'. Allowed values: [mostpopular]",
    "locationType": "parameter",
    "location": "chart"
   }
  ],
  "code": 400,
  "message": "Invalid string value: 'asdf'. Allowed values: [mostpopular]"
 }
}
```

## Errors

1. [MOVED_PERMANENTLY (301)](https://developers.google.com/youtube/v3/docs/core_errors#MOVED_PERMANENTLY)
2. [SEE_OTHER (303)](https://developers.google.com/youtube/v3/docs/core_errors#SEE_OTHER)
3. [NOT_MODIFIED (304)](https://developers.google.com/youtube/v3/docs/core_errors#NOT_MODIFIED)
4. [TEMPORARY_REDIRECT (307)](https://developers.google.com/youtube/v3/docs/core_errors#TEMPORARY_REDIRECT)
5. [BAD_REQUEST (400)](https://developers.google.com/youtube/v3/docs/core_errors#BAD_REQUEST)
6. [UNAUTHORIZED (401)](https://developers.google.com/youtube/v3/docs/core_errors#UNAUTHORIZED)
7. [PAYMENT_REQUIRED (402)](https://developers.google.com/youtube/v3/docs/core_errors#PAYMENT_REQUIRED)
8. [FORBIDDEN (403)](https://developers.google.com/youtube/v3/docs/core_errors#FORBIDDEN)
9. [NOT_FOUND (404)](https://developers.google.com/youtube/v3/docs/core_errors#NOT_FOUND)
10. [METHOD_NOT_ALLOWED (405)](https://developers.google.com/youtube/v3/docs/core_errors#METHOD_NOT_ALLOWED)
11. [CONFLICT (409)](https://developers.google.com/youtube/v3/docs/core_errors#CONFLICT)
12. [GONE (410)](https://developers.google.com/youtube/v3/docs/core_errors#GONE)
13. [PRECONDITION_FAILED (412)](https://developers.google.com/youtube/v3/docs/core_errors#PRECONDITION_FAILED)
14. [REQUEST_ENTITY_TOO_LARGE (413)](https://developers.google.com/youtube/v3/docs/core_errors#REQUEST_ENTITY_TOO_LARGE)
15. [REQUESTED_RANGE_NOT_SATISFIABLE (416)](https://developers.google.com/youtube/v3/docs/core_errors#REQUESTED_RANGE_NOT_SATISFIABLE)
16. [EXPECTATION_FAILED (417)](https://developers.google.com/youtube/v3/docs/core_errors#EXPECTATION_FAILED)
17. [PRECONDITION_REQUIRED (428)](https://developers.google.com/youtube/v3/docs/core_errors#PRECONDITION_REQUIRED)
18. [TOO_MANY_REQUESTS (429)](https://developers.google.com/youtube/v3/docs/core_errors#TOO_MANY_REQUESTS)
19. [INTERNAL_SERVER_ERROR (500)](https://developers.google.com/youtube/v3/docs/core_errors#INTERNAL_SERVER_ERROR)
20. [NOT_IMPLEMENTED (501)](https://developers.google.com/youtube/v3/docs/core_errors#NOT_IMPLEMENTED)
21. [SERVICE_UNAVAILABLE (503)](https://developers.google.com/youtube/v3/docs/core_errors#SERVICE_UNAVAILABLE)

### MOVED_PERMANENTLY (301)

|     Error code     |                                                                                         Description                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `movedPermanently` | This request and future requests for the same operation have to be sent to the URL specified in the `Location` header of this response instead of to the URL to which this request was sent. |

### SEE_OTHER (303)

|       Error code        |                                                              Description                                                              |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `seeOther`              | Your request was processed successfully. To obtain your response, send a `GET` request to the URL specified in the `Location` header. |
| `mediaDownloadRedirect` | Your request was processed successfully. To obtain your response, send a `GET` request to the URL specified in the `Location` header. |

### NOT_MODIFIED (304)

|  Error code   |                                                                                                                   Description                                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `notModified` | The condition set for an If-None-Match header was not met. This response indicates that the requested document has not been modified and that a cached response should be retrieved. Check the value of the `If-None-Match` HTTP request header. |

### TEMPORARY_REDIRECT (307)

|     Error code      |                                                Description                                                |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| `temporaryRedirect` | To have your request processed, resend it to the URL specified in the `Location` header of this response. |

### BAD_REQUEST (400)

|          Error code           |                                                                                                                                 Description                                                                                                                                  |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `badRequest`                  | The API request is invalid or improperly formed. Consequently, the API server could not understand the request.                                                                                                                                                              |
| `badBinaryDomainRequest`      | The binary domain request is invalid.                                                                                                                                                                                                                                        |
| `badContent`                  | The content type of the request data or the content type of a part of a multipart request is not supported.                                                                                                                                                                  |
| `badLockedDomainRequest`      | The locked domain request is invalid.                                                                                                                                                                                                                                        |
| `corsRequestWithXOrigin`      | The CORS request contains an XD3 X-Origin header, which is indicative of a bad CORS request.                                                                                                                                                                                 |
| `endpointConstraintMismatch`  | The request failed because it did not match the specified API. Check the value of the URL path to make sure it is correct.                                                                                                                                                   |
| `invalid`                     | The request failed because it contained an invalid value. The value could be a parameter value, a header value, or a property value.                                                                                                                                         |
| `invalidAltValue`             | The `alt` parameter value specifies an unknown output format.                                                                                                                                                                                                                |
| `invalidHeader`               | The request failed because it contained an invalid header.                                                                                                                                                                                                                   |
| `invalidParameter`            | The request failed because it contained an invalid parameter or parameter value. Review the API documentation to determine which parameters are valid for your request.                                                                                                      |
| `invalidQuery`                | The request is invalid. Check the API documentation to determine what parameters are supported for the request and to see if the request contains an invalid combination of parameters or an invalid parameter value. Check the value of the `q` request parameter.          |
| `keyExpired`                  | The API key provided in the request expired, which means the API server is unable to check the quota limit for the application making the request. Check the [Google Developers Console](https://console.developers.google.com) for more information or to obtain a new key. |
| `keyInvalid`                  | The API key provided in the request is invalid, which means the API server is unable to check the quota limit for the application making the request. Use the [Google Developers Console](https://console.developers.google.com) to find your API key or to obtain one.      |
| `lockedDomainCreationFailure` | The OAuth token was received in the query string, which this API forbids for response formats other than JSON or XML. If possible, try sending the OAuth token in the Authorization header instead.                                                                          |
| `notDownload`                 | Only media downloads requests can be sent to `/download/*` URL paths. Resend the request to the same path, but without the `/download` prefix.                                                                                                                               |
| `notUpload`                   | The request failed because it is not an upload request, and only upload requests can be sent to `/upload/*` URIs. Try resending the request to the same path, but without the `/upload` prefix.                                                                              |
| `parseError`                  | The API server cannot parse the request body.                                                                                                                                                                                                                                |
| `required`                    | The API request is missing required information. The required information could be a parameter or resource property.                                                                                                                                                         |
| `tooManyParts`                | The multipart request failed because it contains too many parts                                                                                                                                                                                                              |
| `unknownApi`                  | The API that the request is calling is not recognized.                                                                                                                                                                                                                       |
| `unsupportedMediaProtocol`    | The client is using an unsupported media protocol.                                                                                                                                                                                                                           |
| `unsupportedOutputFormat`     | The `alt` parameter value specifies an output format that is not supported for this service. Check the value of the `alt` request parameter.                                                                                                                                 |
| `wrongUrlForUpload`           | The request is an upload request, but it failed because it was not sent to the proper URI. Upload requests must be sent to URIs that contain the `/upload/*` prefix. Try resending the request to the same path, but with the `/upload` prefix.                              |

### UNAUTHORIZED (401)

|      Error code       |                                                           Description                                                           |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `unauthorized`        | The user is not authorized to make the request.                                                                                 |
| `authError`           | The authorization credentials provided for the request are invalid. Check the value of the `Authorization` HTTP request header. |
| `expired`             | Session Expired. Check the value of the `Authorization` HTTP request header.                                                    |
| `lockedDomainExpired` | The request failed because a previously valid locked domain has expired.                                                        |
| `required`            | The user must be logged in to make this API request. Check the value of the `Authorization` HTTP request header.                |

### PAYMENT_REQUIRED (402)

|       Error code        |                                                      Description                                                      |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `dailyLimitExceeded402` | A daily budget limit set by the developer has been reached.                                                           |
| `quotaExceeded402`      | The requested operation requires more resources than the quota allows. Payment is required to complete the operation. |
| `user402`               | The requested operation requires some kind of payment from the authenticated user.                                    |

### FORBIDDEN (403)

|             Error code             |                                                                                                                       Description                                                                                                                        |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `forbidden`                        | The requested operation is forbidden and cannot be completed.                                                                                                                                                                                            |
| `accessNotConfigured`              | Your project is not configured to access this API. Please use the [Google Developers Console](https://console.developers.google.com) to activate the API for your project.                                                                               |
| `accessNotConfigured`              | The project has been blocked due to abuse. See <http://support.google.com/code/go/developer_compliance>.                                                                                                                                                 |
| `accessNotConfigured`              | The project has been marked for deletion.                                                                                                                                                                                                                |
| `accountDeleted`                   | The user account associated with the request's authorization credentials has been deleted. Check the value of the `Authorization` HTTP request header.                                                                                                   |
| `accountDisabled`                  | The user account associated with the request's authorization credentials has been disabled. Check the value of the `Authorization` HTTP request header.                                                                                                  |
| `accountUnverified`                | The email address for the user making the request has not been verified. Check the value of the `Authorization` HTTP request header.                                                                                                                     |
| `concurrentLimitExceeded`          | The request failed because a concurrent usage limit has been reached.                                                                                                                                                                                    |
| `dailyLimitExceeded`               | A daily quota limit for the API has been reached.                                                                                                                                                                                                        |
| `dailyLimitExceeded`               | The daily quota limit has been reached, and the project has been blocked due to abuse. See the [Google APIs compliance support form](http://support.google.com/code/go/developer_compliance) to help resolve the issue.                                  |
| `dailyLimitExceededUnreg`          | The request failed because a daily limit for unauthenticated API use has been hit. Continued use of the API requires signup through the [Google Developers Console](https://console.developers.google.com).                                              |
| `downloadServiceForbidden`         | The API does not support a download service.                                                                                                                                                                                                             |
| `insufficientAudience`             | The request cannot be completed for this audience.                                                                                                                                                                                                       |
| `insufficientAuthorizedParty`      | The request cannot be completed for this application.                                                                                                                                                                                                    |
| `insufficientPermissions`          | The authenticated user does not have sufficient permissions to execute this request.                                                                                                                                                                     |
| `limitExceeded`                    | The request cannot be completed due to access or rate limitations.                                                                                                                                                                                       |
| `lockedDomainForbidden`            | This API does not support locked domains.                                                                                                                                                                                                                |
| `quotaExceeded`                    | The requested operation requires more resources than the quota allows.                                                                                                                                                                                   |
| `rateLimitExceeded`                | Too many requests have been sent within a given time span.                                                                                                                                                                                               |
| `rateLimitExceededUnreg`           | A rate limit has been exceeded and you must register your application to be able to continue calling the API. Please sign up using the [Google Developers Console](https://console.developers.google.com).                                               |
| `responseTooLarge`                 | The requested resource is too large to return.                                                                                                                                                                                                           |
| `servingLimitExceeded`             | The overall rate limit specified for the API has already been reached.                                                                                                                                                                                   |
| `sslRequired`                      | SSL is required to perform this operation.                                                                                                                                                                                                               |
| `unknownAuth`                      | The API server does not recognize the authorization scheme used for the request. Check the value of the `Authorization` HTTP request header.                                                                                                             |
| `userRateLimitExceeded`            | The request failed because a per-user rate limit has been reached.                                                                                                                                                                                       |
| `userRateLimitExceededUnreg`       | The request failed because a per-user rate limit has been reached, and the client developer was not identified in the request. Please use the Google Developer Console (https://console.developers.google.com) to create a project for your application. |
| `variableTermExpiredDailyExceeded` | The request failed because a variable term quota expired and a daily limit was reached.                                                                                                                                                                  |
| `variableTermLimitExceeded`        | The request failed because a variable term quota limit was reached.                                                                                                                                                                                      |

### NOT_FOUND (404)

|      Error code       |                                                                                  Description                                                                                  |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `notFound`            | The requested operation failed because a resource associated with the request could not be found.                                                                             |
| `notFound`            | A resource associated with the request could not be found. If you have not used this API in the last two weeks, please re-deploy the App Engine app and try calling it again. |
| `unsupportedProtocol` | The protocol used in the request is not supported.                                                                                                                            |

### METHOD_NOT_ALLOWED (405)

|       Error code       |                          Description                          |
|------------------------|---------------------------------------------------------------|
| `httpMethodNotAllowed` | The HTTP method associated with the request is not supported. |

### CONFLICT (409)

| Error code  |                                                                                                                                Description                                                                                                                                 |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `conflict`  | The API request cannot be completed because the requested operation would conflict with an existing item. For example, a request that tries to create a duplicate item would create a conflict, though duplicate items are typically identified with more specific errors. |
| `duplicate` | The requested operation failed because it tried to create a resource that already exists.                                                                                                                                                                                  |

### GONE (410)

| Error code |                                     Description                                      |
|------------|--------------------------------------------------------------------------------------|
| `deleted`  | The request failed because the resource associated with the request has been deleted |

### PRECONDITION_FAILED (412)

|    Error code     |                                                                                                                               Description                                                                                                                               |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `conditionNotMet` | The condition set in the request's `If-Match` or `If-None-Match` HTTP request header was not met. See the [ETag](https://tools.ietf.org/html/rfc7232#section-2.3) section of the HTTP specification for details. Check the value of the `If-Match` HTTP request header. |

### REQUEST_ENTITY_TOO_LARGE (413)

|        Error code        |                              Description                              |
|--------------------------|-----------------------------------------------------------------------|
| `backendRequestTooLarge` | The request is too large.                                             |
| `batchSizeTooLarge`      | The batch request contains too many elements.                         |
| `uploadTooLarge`         | The request failed because the data sent in the request is too large. |

### REQUESTED_RANGE_NOT_SATISFIABLE (416)

|           Error code           |                       Description                       |
|--------------------------------|---------------------------------------------------------|
| `requestedRangeNotSatisfiable` | The request specified a range that cannot be satisfied. |

### EXPECTATION_FAILED (417)

|     Error code      |                    Description                    |
|---------------------|---------------------------------------------------|
| `expectationFailed` | A client expectation cannot be met by the server. |

### PRECONDITION_REQUIRED (428)

|       Error code       |                                                                                 Description                                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `preconditionRequired` | The request requires a precondition that is not provided. For this request to succeed, you need to provide either an `If-Match` or `If-None-Match` header with the request. |

### TOO_MANY_REQUESTS (429)

|     Error code      |                        Description                         |
|---------------------|------------------------------------------------------------|
| `rateLimitExceeded` | Too many requests have been sent within a given time span. |

### INTERNAL_SERVER_ERROR (500)

|   Error code    |                 Description                  |
|-----------------|----------------------------------------------|
| `internalError` | The request failed due to an internal error. |

### NOT_IMPLEMENTED (501)

|     Error code      |                                    Description                                     |
|---------------------|------------------------------------------------------------------------------------|
| `notImplemented`    | The requested operation has not been implemented.                                  |
| `unsupportedMethod` | The request failed because it is trying to execute an unknown method or operation. |

### SERVICE_UNAVAILABLE (503)

|      Error code       |                   Description                   |
|-----------------------|-------------------------------------------------|
| `backendError`        | A backend error occurred.                       |
| `backendNotConnected` | The request failed due to a connection error.   |
| `notReady`            | The API server is not ready to accept requests. |