# Source: https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions.md.txt

# firebase_admin.exceptions module

Firebase Exceptions module.

This module defines the base types for exceptions and the platform-wide error codes as outlined in
<https://cloud.google.com/apis/design/errors>.

[FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") is the parent class of all exceptions raised by the Admin SDK. It contains
the code, http_response and cause properties common to all Firebase exception types.
Each exception also carries a message that outlines what went wrong. This can be logged for
audit or debugging purposes.

When calling an Admin SDK API, developers can catch the parent FirebaseError and
inspect its code to implement fine-grained error handling. Alternatively, developers can
catch one or more subtypes of FirebaseError. Under normal conditions, any given API can raise
only a small subset of the available exception subtypes. However, the SDK also exposes rare error
conditions like connection timeouts and other I/O errors as instances of FirebaseError.
Therefore it is always a good idea to have a handler specified for FirebaseError, after all the
subtype error handlers.

## Exceptions

|                                                                 ### AbortedError *exception* firebase_admin.exceptions.AbortedError(*message* , *cause=None* , *http_response=None* )                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Concurrency conflict, such as read-modify-write conflict. |

|                                                           ### AlreadyExistsError *exception* firebase_admin.exceptions.AlreadyExistsError(*message* , *cause=None* , *http_response=None* )                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") The resource that a client tried to create already exists. |

|                                                  ### CancelledError *exception* firebase_admin.exceptions.CancelledError(*message* , *cause=None* , *http_response=None* )                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Request cancelled by the client. |

|                                                                ### ConflictError *exception* firebase_admin.exceptions.ConflictError(*message* , *cause=None* , *http_response=None* )                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Concurrency conflict, such as read-modify-write conflict. |

|                                                         ### DataLossError *exception* firebase_admin.exceptions.DataLossError(*message* , *cause=None* , *http_response=None* )                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Unrecoverable data loss or data corruption. |

|                                                                                                                                                             ### DeadlineExceededError *exception* firebase_admin.exceptions.DeadlineExceededError(*message* , *cause=None* , *http_response=None* )                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Request deadline exceeded. This will happen only if the caller sets a deadline that is shorter than the method's default deadline (i.e. requested deadline is not enough for the server to process the request) and the request did not finish within the deadline. |

|                                                                         ### FailedPreconditionError *exception* firebase_admin.exceptions.FailedPreconditionError(*message* , *cause=None* , *http_response=None* )                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Request can not be executed in the current system state, such as deleting a non-empty directory. |

|                                                                                                                                                                                                                                                                                                                                                                               ### FirebaseError *exception* firebase_admin.exceptions.FirebaseError(*code* , *message* , *cause=None* , *http_response=None* )                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: Exception Base class for all errors raised by the Admin SDK. Parameters: : - **code** -- A string error code that represents the type of the exception. Possible error codes are defined in <https://cloud.google.com/apis/design/errors#handling_errors>. - **message** -- A human-readable error message string. - **cause** -- The exception that caused this error (optional). - **http_response** -- If this error was caused by an HTTP error response, this property is set to the requests.Response object that represents the HTTP response (optional). See <https://docs.python-requests.org/en/master/api/#requests.Response> for details of this object. | *property* cause | |------------------| |                  | | *property* code | |-----------------| |                 | | *property* http_response | |--------------------------| |                          | |

|                                              ### InternalError *exception* firebase_admin.exceptions.InternalError(*message* , *cause=None* , *http_response=None* )                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Internal server error. |

|                                               ### InvalidArgumentError *exception* firebase_admin.exceptions.InvalidArgumentError(*message* , *cause=None* , *http_response=None* )                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Client specified an invalid argument. |

|                                                                                         ### NotFoundError *exception* firebase_admin.exceptions.NotFoundError(*message* , *cause=None* , *http_response=None* )                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") A specified resource is not found, or the request is rejected by undisclosed reasons, such as whitelisting. |

|                                                  ### OutOfRangeError *exception* firebase_admin.exceptions.OutOfRangeError(*message* , *cause=None* , *http_response=None* )                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Client specified an invalid range. |

|                                                                                                                                   ### PermissionDeniedError *exception* firebase_admin.exceptions.PermissionDeniedError(*message* , *cause=None* , *http_response=None* )                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Client does not have sufficient permission. This can happen because the OAuth token does not have the right scopes, the client doesn't have permission, or the API has not been enabled for the client project. |

|                                                      ### ResourceExhaustedError *exception* firebase_admin.exceptions.ResourceExhaustedError(*message* , *cause=None* , *http_response=None* )                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Either out of resource quota or reaching rate limiting. |

|                                                                 ### UnauthenticatedError *exception* firebase_admin.exceptions.UnauthenticatedError(*message* , *cause=None* , *http_response=None* )                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Request not authenticated due to missing, invalid, or expired OAuth token. |

|                                                         ### UnavailableError *exception* firebase_admin.exceptions.UnavailableError(*message* , *cause=None* , *http_response=None* )                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Service unavailable. Typically the server is down. |

|                                               ### UnknownError *exception* firebase_admin.exceptions.UnknownError(*message* , *cause=None* , *http_response=None* )                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: [FirebaseError](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") Unknown server error. |

## Constants

| ### ABORTED firebase_admin.exceptions.ABORTED*= 'ABORTED'* |
|------------------------------------------------------------|
| Error code for AbortedError type.                          |

| ### ALREADY_EXISTS firebase_admin.exceptions.ALREADY_EXISTS*= 'ALREADY_EXISTS'* |
|---------------------------------------------------------------------------------|
| Error code for AlreadyExistsError type.                                         |

| ### CANCELLED firebase_admin.exceptions.CANCELLED*= 'CANCELLED'* |
|------------------------------------------------------------------|
| Error code for CancelledError type.                              |

| ### CONFLICT firebase_admin.exceptions.CONFLICT*= 'CONFLICT'* |
|---------------------------------------------------------------|
| Error code for ConflictError type.                            |

| ### DATA_LOSS firebase_admin.exceptions.DATA_LOSS*= 'DATA_LOSS'* |
|------------------------------------------------------------------|
| Error code for DataLossError type.                               |

| ### DEADLINE_EXCEEDED firebase_admin.exceptions.DEADLINE_EXCEEDED*= 'DEADLINE_EXCEEDED'* |
|------------------------------------------------------------------------------------------|
| Error code for DeadlineExceededError type.                                               |

| ### FAILED_PRECONDITION firebase_admin.exceptions.FAILED_PRECONDITION*= 'FAILED_PRECONDITION'* |
|------------------------------------------------------------------------------------------------|
| Error code for FailedPreconditionError type.                                                   |

| ### INTERNAL firebase_admin.exceptions.INTERNAL*= 'INTERNAL'* |
|---------------------------------------------------------------|
| Error code for InternalError type.                            |

| ### INVALID_ARGUMENT firebase_admin.exceptions.INVALID_ARGUMENT*= 'INVALID_ARGUMENT'* |
|---------------------------------------------------------------------------------------|
| Error code for InvalidArgumentError type.                                             |

| ### NOT_FOUND firebase_admin.exceptions.NOT_FOUND*= 'NOT_FOUND'* |
|------------------------------------------------------------------|
| Error code for NotFoundError type.                               |

| ### OUT_OF_RANGE firebase_admin.exceptions.OUT_OF_RANGE*= 'OUT_OF_RANGE'* |
|---------------------------------------------------------------------------|
| Error code for OutOfRangeError type.                                      |

| ### PERMISSION_DENIED firebase_admin.exceptions.PERMISSION_DENIED*= 'PERMISSION_DENIED'* |
|------------------------------------------------------------------------------------------|
| Error code for PermissionDeniedError type.                                               |

| ### RESOURCE_EXHAUSTED firebase_admin.exceptions.RESOURCE_EXHAUSTED*= 'RESOURCE_EXHAUSTED'* |
|---------------------------------------------------------------------------------------------|
| Error code for ResourceExhaustedError type.                                                 |

| ### UNAUTHENTICATED firebase_admin.exceptions.UNAUTHENTICATED*= 'UNAUTHENTICATED'* |
|------------------------------------------------------------------------------------|
| Error code for UnauthenticatedError type.                                          |

| ### UNAVAILABLE firebase_admin.exceptions.UNAVAILABLE*= 'UNAVAILABLE'* |
|------------------------------------------------------------------------|
| Error code for UnavailableError type.                                  |

| ### UNKNOWN firebase_admin.exceptions.UNKNOWN*= 'UNKNOWN'* |
|------------------------------------------------------------|
| Error code for UnknownError type.                          |