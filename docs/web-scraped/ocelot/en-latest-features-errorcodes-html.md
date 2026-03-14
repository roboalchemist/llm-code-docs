# Source: https://ocelot.readthedocs.io/en/latest/features/errorcodes.html

Title: Error Handling — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/errorcodes.html

Markdown Content:
Ocelot has custom error handling for `Exception` objects. Thus, we override the [standard error handling](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling) provided by ASP.NET Core, which is based on manipulating `Exception` objects.

Middleware[¶](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#middleware "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

The `ExceptionHandlerMiddleware` produces the following status codes, in fallback order, after setting the [Request ID](https://ocelot.readthedocs.io/en/latest/features/logging.html#lg-request-id):

1.   Native response status: Returned when no exception is present, or when a mapped error status is available (excluding `499` and `500`).

2.   [499 Client Closed Request](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status499clientclosedrequest): A custom Ocelot status returned when an `OperationCanceledException` occurs due to an aborted request. A warning is logged.

3.   [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/500): The standard status returned when a generic `Exception` occurs and Ocelot does not process or map the error. An error record is logged.

Ocelot returns HTTP status codes based on internal logic in specific cases of [Client Error Responses](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#eh-client-error-responses) and [Server Error Responses](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#eh-server-error-responses).

Client Error Responses[¶](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#client-error-responses "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

*   [401 Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/401): If the authentication middleware runs and the user is not authenticated.

*   [403 Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/403): If the authorization middleware runs and the user is unauthorized, if the claim value is not authorized, if the scope is not authorized, if the user does not have the required claim, or if the claim cannot be found.

*   [404 Not Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/404): If a downstream route cannot be found, or if Ocelot is unable to map an internal error code to an HTTP status code.

*   [499 Client Closed Request](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status499clientclosedrequest): If the request is canceled by the client.

According to Ocelot Core’s design, HTTP status code `499` is returned in the following `OperationCanceledException` scenarios:

    1.   By `ExceptionHandlerMiddleware`, if an `OperationCanceledException` is thrown and the context’s cancellation token is in the “cancellation requested” state. Ocelot logs a warning with the exception body. If the response has not started, the status code will be set to `499`.

    2.   By `ResponderMiddleware`, if the default `IErrorsToHttpStatusCodeMapper` service maps the detected [OcelotErrorCode.RequestCanceled](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20OcelotErrorCode.RequestCanceled&type=code) to status `499`. This error code is produced by the `IExceptionToErrorMapper` service when an `OperationCanceledException` is thrown by other middlewares.

Server Error Responses[¶](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#server-error-responses "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

*   [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/500): If unable to complete the HTTP request to the downstream service, and the exception is not `OperationCanceledException` or `HttpRequestException`.

*   [502 Bad Gateway](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/502): If unable to connect to the downstream service.

*   [503 Service Unavailable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/503): Returned when the downstream request times out.

According to Ocelot Core’s design, status code `503` is produced in the following `TimeoutException` scenarios:

    1.   By `TimeoutDelegatingHandler` from the `IMessageInvokerPool` service, when an `OperationCanceledException` is thrown and the context’s cancellation token is not in the “cancellation requested” state. Ocelot does not log an error with the exception body, but the `IExceptionToErrorMapper` service generates the internal [OcelotErrorCode.RequestTimedOutError](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20OcelotErrorCode.RequestTimedOutError&type=code).

    2.   By `ResponderMiddleware`, if the default `IErrorsToHttpStatusCodeMapper` service maps the detected [OcelotErrorCode.RequestTimedOutError](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20OcelotErrorCode.RequestTimedOutError&type=code) to status `503`. This error code is produced by the `IExceptionToErrorMapper` service when a `TimeoutException` is thrown by other middlewares—especially by `TimeoutDelegatingHandler`.

Error Mapper[¶](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#error-mapper "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Historically, Ocelot errors are implemented by the [Exception-to-Error mapper](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20HttpExceptionToErrorMapper&type=code). The `Map` method converts an `Exception` object to a native `Ocelot.Errors.Error` object.

We override HTTP status codes because of `Exception`-to-`Error` mapping. This can be confusing for the developer since the actual status code of the downstream service may be different and get lost. Please research and review all response headers of the upstream service. If you do not find status codes and/or required headers, then the [Headers Transformation](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html) feature should help.

We expect you to share your use case with us in the [Discussions](https://github.com/ThreeMammals/Ocelot/discussions) space of the repository. [![Image 1: octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)](https://github.githubassets.com/images/icons/emoji/octocat.png)
