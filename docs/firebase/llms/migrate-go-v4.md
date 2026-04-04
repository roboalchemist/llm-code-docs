# Source: https://firebase.google.com/docs/admin/migrate-go-v4.md.txt

<br />

Starting from version 4.0.0, theFirebaseAdmin SDKfor Go has opted into[Go modules](https://github.com/golang/go/wiki/Modules). Also, there are breaking changes in[error handling](https://firebase.google.com/docs/reference/admin/error-handling)and semantics.

## Installation changes

Conforming to[modules best practices](https://github.com/golang/go/wiki/Modules#semantic-import-versioning), the SDK's major version has been appended to the package name. This change results in the following package name updates:

- firebase.google.com/go â firebase.google.com/go/v4
- firebase.google.com/go/auth â firebase.google.com/go/v4/auth
- firebase.google.com/go/db â firebase.google.com/go/v4/db
- firebase.google.com/go/iid â firebase.google.com/go/v4/iid
- firebase.google.com/go/messaging â firebase.google.com/go/v4/messaging

| **Note:** Developers who are already using Go modules**must**use the new versioned package name when installing and importing the SDK.

### Developers already using modules

Use the versioned package name to install the latest version of the SDK.  

    # Install the latest version:
    go install firebase.google.com/go/v4@latest

    # Or install a specific version:
    go install firebase.google.com/go/v4@4.18.0

The same versioned package name must be used in the source code when importing the SDK.  

    package helloworld

    import (
            "firebase.google.com/go/v4"
            "firebase.google.com/go/v4/auth"
            "firebase.google.com/go/v4/messaging"
    )

To install an earlier version, use the old (unversioned) package name with an explicit version qualifier.  

    # Notice the @v3 suffix.
    # This instructs Go tools to fetch the latest v3.x release of the SDK.
    go get firebase.google.com/go@v3

### Developers not currently using modules

Developers who haven't opted into modules yet can continue to install the SDK using the unversioned package name.  

    go get firebase.google.com/go

Note, however, that this fetches the latest version of the SDK (v4 or later) which contains other breaking API changes.

## General error handling changes

The v4 SDK introduces a new`errorutils`package that provides functions for handling platform-level error conditions. In the event an error was caused by a backend service error, you can access the original error response by calling the new function`errorutils.HTTPResponse()`. You can use the functions in this package with errors returned by any API in the SDK.

## AuthenticationAPI changes

- Added new error handling functions to be used in conjunction with`VerifyIDToken()`and`VerifySessionCookie()`APIs:
  - `IsIDTokenInvalid()`
  - `IsIDTokenExpired()`
  - `IsSessionCookieInvalid()`
  - `IsSessionCookieExpired()`
  - `IsCertificateFetchFailed()`
- Deprecated:
  - `IsProjectNotFound()`
  - `IsUnknown()`
  - `IsInsufficientPermission()`
  - `IsInvalidEmail()`

## FCMAPI changes

- Renamed the type`messaging.WebpushFCMOptions`to`messaging.WebpushFcmOptions`.
- Added:
  - `IsThirdPartyAuthError()`
  - `IsQuotaExceeded()`
  - `IsSenderIDMismatch()`
  - `IsUnregistered()`
  - `IsUnavailable()`
- Deprecated:
  - `IsInvalidAPNSCredentials()`
  - `IsMessageRateExceeded()`
  - `IsMismatchedCredential()`
  - `IsRegistrationTokenNotRegistered()`
  - `IsServerUnavailable()`
  - `IsTooManyTopics()`
  - `IsUnknown()`

## IID API changes

All error handling functions currently available in the`iid`package are now deprecated. Use the corresponding error handling functions provided in the`errorutils`package instead.