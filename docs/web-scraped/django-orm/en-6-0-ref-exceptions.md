# Source: https://docs.djangoproject.com/en/6.0/ref/exceptions/

Title: Django Exceptions | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/exceptions/

Markdown Content:
Django raises some of its own exceptions as well as standard Python exceptions.

Django Core Exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#module-django.core.exceptions "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

Django core exception classes are defined in `django.core.exceptions`.

### `AppRegistryNotReady`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#appregistrynotready "Link to this heading")

_exception_ AppRegistryNotReady[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L16)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.AppRegistryNotReady "Link to this definition")
This exception is raised when attempting to use models before the [app loading process](https://docs.djangoproject.com/en/6.0/ref/applications/#app-loading-process), which initializes the ORM, is complete.

### `ObjectDoesNotExist`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#objectdoesnotexist "Link to this heading")

_exception_ ObjectDoesNotExist[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L22)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist "Link to this definition")
The base class for [`Model.DoesNotExist`](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.DoesNotExist "django.db.models.Model.DoesNotExist") exceptions. A `try/except` for `ObjectDoesNotExist` will catch [`DoesNotExist`](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.DoesNotExist "django.db.models.Model.DoesNotExist") exceptions for all models.

See [`get()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get").

### `ObjectNotUpdated`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#objectnotupdated "Link to this heading")

New in Django 6.0.

_exception_ ObjectNotUpdated[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L28)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ObjectNotUpdated "Link to this definition")
The base class for [`Model.NotUpdated`](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.NotUpdated "django.db.models.Model.NotUpdated") exceptions. A `try/except` for `ObjectNotUpdated` will catch [`NotUpdated`](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.NotUpdated "django.db.models.Model.NotUpdated") exceptions for all models.

See [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save").

### `EmptyResultSet`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#emptyresultset "Link to this heading")

_exception_ EmptyResultSet[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L244)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.EmptyResultSet "Link to this definition")
`EmptyResultSet` may be raised during query generation if a query won’t return any results. Most Django projects won’t encounter this exception, but it might be useful for implementing custom lookups and expressions.

### `FullResultSet`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#fullresultset "Link to this heading")

_exception_ FullResultSet[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L250)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.FullResultSet "Link to this definition")
`FullResultSet` may be raised during query generation if a query will match everything. Most Django projects won’t encounter this exception, but it might be useful for implementing custom lookups and expressions.

### `FieldDoesNotExist`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#fielddoesnotexist "Link to this heading")

_exception_ FieldDoesNotExist[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L10)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.FieldDoesNotExist "Link to this definition")
The `FieldDoesNotExist` exception is raised by a model’s `_meta.get_field()` method when the requested field does not exist on the model or on the model’s parents.

### `MultipleObjectsReturned`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#multipleobjectsreturned "Link to this heading")

_exception_ MultipleObjectsReturned[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L32)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.MultipleObjectsReturned "Link to this definition")
The base class for [`Model.MultipleObjectsReturned`](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.MultipleObjectsReturned "django.db.models.Model.MultipleObjectsReturned") exceptions. A `try/except` for `MultipleObjectsReturned` will catch [`MultipleObjectsReturned`](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.MultipleObjectsReturned "django.db.models.Model.MultipleObjectsReturned") exceptions for all models.

See [`get()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get").

### `SuspiciousOperation`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#suspiciousoperation "Link to this heading")

_exception_ SuspiciousOperation[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L38)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "Link to this definition")
The [`SuspiciousOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") exception is raised when a user has performed an operation that should be considered suspicious from a security perspective, such as tampering with a session cookie. Subclasses of `SuspiciousOperation` include:

*   `DisallowedHost`

*   `DisallowedModelAdminLookup`

*   `DisallowedModelAdminToField`

*   `DisallowedRedirect`

*   `InvalidSessionKey`

*   `RequestDataTooBig`

*   `SuspiciousFileOperation`

*   `SuspiciousMultipartForm`

*   `SuspiciousSession`

*   `TooManyFieldsSent`

*   `TooManyFilesSent`

If a `SuspiciousOperation` exception reaches the ASGI/WSGI handler level it is logged at the `Error` level and results in a [`HttpResponseBadRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponseBadRequest "django.http.HttpResponseBadRequest"). See the [logging documentation](https://docs.djangoproject.com/en/6.0/topics/logging/) for more information.

### `PermissionDenied`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#permissiondenied "Link to this heading")

_exception_ PermissionDenied[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L105)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.PermissionDenied "Link to this definition")
The [`PermissionDenied`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied") exception is raised when a user does not have permission to perform the action requested.

### `ViewDoesNotExist`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#viewdoesnotexist "Link to this heading")

_exception_ ViewDoesNotExist[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L111)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ViewDoesNotExist "Link to this definition")
The [`ViewDoesNotExist`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ViewDoesNotExist "django.core.exceptions.ViewDoesNotExist") exception is raised by [`django.urls`](https://docs.djangoproject.com/en/6.0/ref/urlresolvers/#module-django.urls "django.urls") when a requested view does not exist.

### `MiddlewareNotUsed`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#middlewarenotused "Link to this heading")

_exception_ MiddlewareNotUsed[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L117)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.MiddlewareNotUsed "Link to this definition")
The [`MiddlewareNotUsed`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.MiddlewareNotUsed "django.core.exceptions.MiddlewareNotUsed") exception is raised when a middleware is not used in the server configuration.

### `ImproperlyConfigured`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#improperlyconfigured "Link to this heading")

_exception_ ImproperlyConfigured[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L123)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ImproperlyConfigured "Link to this definition")
The [`ImproperlyConfigured`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ImproperlyConfigured "django.core.exceptions.ImproperlyConfigured") exception is raised when Django is somehow improperly configured – for example, if a value in `settings.py` is incorrect or unparseable.

### `FieldError`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#fielderror "Link to this heading")

_exception_ FieldError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L129)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.FieldError "Link to this definition")
The [`FieldError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.FieldError "django.core.exceptions.FieldError") exception is raised when there is a problem with a model field. This can happen for several reasons:

*   A field in a model clashes with a field of the same name from an abstract base class

*   An infinite loop is caused by ordering

*   A keyword cannot be parsed from the filter parameters

*   A field cannot be determined from a keyword in the query parameters

*   A join is not permitted on the specified field

*   A field name is invalid

*   A query contains invalid order_by arguments

### `ValidationError`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#validationerror "Link to this heading")

_exception_ ValidationError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L138)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ValidationError "Link to this definition")
The [`ValidationError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") exception is raised when data fails form or model field validation. For more information about validation, see [Form and Field Validation](https://docs.djangoproject.com/en/6.0/ref/forms/validation/), [Model Field Validation](https://docs.djangoproject.com/en/6.0/ref/models/instances/#validating-objects) and the [Validator Reference](https://docs.djangoproject.com/en/6.0/ref/validators/).

#### `NON_FIELD_ERRORS`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#non-field-errors "Link to this heading")

NON_FIELD_ERRORS[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.NON_FIELD_ERRORS "Link to this definition")
`ValidationError`s that don’t belong to a particular field in a form or model are classified as `NON_FIELD_ERRORS`. This constant is used as a key in dictionaries that otherwise map fields to their respective list of errors.

### `BadRequest`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#badrequest "Link to this heading")

_exception_ BadRequest[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L99)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.BadRequest "Link to this definition")
The [`BadRequest`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.BadRequest "django.core.exceptions.BadRequest") exception is raised when the request cannot be processed due to a client error. If a `BadRequest` exception reaches the ASGI/WSGI handler level it results in a [`HttpResponseBadRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponseBadRequest "django.http.HttpResponseBadRequest").

### `RequestAborted`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#requestaborted "Link to this heading")

_exception_ RequestAborted[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L93)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.RequestAborted "Link to this definition")
The [`RequestAborted`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.RequestAborted "django.core.exceptions.RequestAborted") exception is raised when an HTTP body being read in by the handler is cut off midstream and the client connection closes, or when the client does not send data and hits a timeout where the server closes the connection.

It is internal to the HTTP handler modules and you are unlikely to see it elsewhere. If you are modifying HTTP handling code, you should raise this when you encounter an aborted request to make sure the socket is closed cleanly.

### `SynchronousOnlyOperation`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#synchronousonlyoperation "Link to this heading")

_exception_ SynchronousOnlyOperation[[source]](https://github.com/django/django/blob/stable/6.0.x/django/core/exceptions.py#L256)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SynchronousOnlyOperation "Link to this definition")
The [`SynchronousOnlyOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SynchronousOnlyOperation "django.core.exceptions.SynchronousOnlyOperation") exception is raised when code that is only allowed in synchronous Python code is called from an asynchronous context (a thread with a running asynchronous event loop). These parts of Django are generally heavily reliant on thread-safety to function and don’t work correctly under coroutines sharing the same thread.

If you are trying to call code that is synchronous-only from an asynchronous thread, then create a synchronous thread and call it in that. You can accomplish this is with [`asgiref.sync.sync_to_async()`](https://docs.djangoproject.com/en/6.0/topics/async/#asgiref.sync.sync_to_async "asgiref.sync.sync_to_async").

URL Resolver exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#url-resolver-exceptions "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

URL Resolver exceptions are defined in `django.urls`.

### `Resolver404`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#resolver404 "Link to this heading")

_exception_ Resolver404[[source]](https://github.com/django/django/blob/stable/6.0.x/django/urls/exceptions.py#L4)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.urls.Resolver404 "Link to this definition")
The [`Resolver404`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.urls.Resolver404 "django.urls.Resolver404") exception is raised by [`resolve()`](https://docs.djangoproject.com/en/6.0/ref/urlresolvers/#django.urls.resolve "django.urls.resolve") if the path passed to `resolve()` doesn’t map to a view. It’s a subclass of [`django.http.Http404`](https://docs.djangoproject.com/en/6.0/topics/http/views/#django.http.Http404 "django.http.Http404").

### `NoReverseMatch`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#noreversematch "Link to this heading")

_exception_ NoReverseMatch[[source]](https://github.com/django/django/blob/stable/6.0.x/django/urls/exceptions.py#L8)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.urls.NoReverseMatch "Link to this definition")
The [`NoReverseMatch`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.urls.NoReverseMatch "django.urls.NoReverseMatch") exception is raised by [`django.urls`](https://docs.djangoproject.com/en/6.0/ref/urlresolvers/#module-django.urls "django.urls") when a matching URL in your URLconf cannot be identified based on the parameters supplied.

Database Exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#database-exceptions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

Database exceptions may be imported from `django.db`.

Django wraps the standard database exceptions so that your Django code has a guaranteed common implementation of these classes.

_exception_ Error[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L17)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.Error "Link to this definition")_exception_ InterfaceError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L21)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.InterfaceError "Link to this definition")_exception_ DatabaseError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L25)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.DatabaseError "Link to this definition")_exception_ DataError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L29)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.DataError "Link to this definition")_exception_ OperationalError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L33)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.OperationalError "Link to this definition")_exception_ IntegrityError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L37)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "Link to this definition")_exception_ InternalError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L41)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.InternalError "Link to this definition")_exception_ ProgrammingError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L45)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.ProgrammingError "Link to this definition")_exception_ NotSupportedError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/utils.py#L49)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.NotSupportedError "Link to this definition")
The Django wrappers for database exceptions behave exactly the same as the underlying database exceptions. See [**PEP 249**](https://peps.python.org/pep-0249/), the Python Database API Specification v2.0, for further information.

As per [**PEP 3134**](https://peps.python.org/pep-3134/), a `__cause__` attribute is set with the original (underlying) database exception, allowing access to any additional information provided.

_exception_ models.ProtectedError[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.models.ProtectedError "Link to this definition")
Raised to prevent deletion of referenced objects when using [`django.db.models.PROTECT`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PROTECT "django.db.models.PROTECT"). [`models.ProtectedError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.models.ProtectedError "django.db.models.ProtectedError") is a subclass of [`IntegrityError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError").

_exception_ models.RestrictedError[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.models.RestrictedError "Link to this definition")
Raised to prevent deletion of referenced objects when using [`django.db.models.RESTRICT`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.RESTRICT "django.db.models.RESTRICT"). [`models.RestrictedError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.models.RestrictedError "django.db.models.RestrictedError") is a subclass of [`IntegrityError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError").

HTTP Exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#http-exceptions "Link to this heading")
----------------------------------------------------------------------------------------------------------------

HTTP exceptions may be imported from `django.http`.

### `UnreadablePostError`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#unreadableposterror "Link to this heading")

_exception_ UnreadablePostError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/http/request.py#L39)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.http.UnreadablePostError "Link to this definition")
[`UnreadablePostError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.http.UnreadablePostError "django.http.UnreadablePostError") is raised when a user cancels an upload.

Sessions Exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#sessions-exceptions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

Sessions exceptions are defined in `django.contrib.sessions.exceptions`.

### `SessionInterrupted`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#sessioninterrupted "Link to this heading")

_exception_ SessionInterrupted[[source]](https://github.com/django/django/blob/stable/6.0.x/django/contrib/sessions/exceptions.py#L16)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.contrib.sessions.exceptions.SessionInterrupted "Link to this definition")
[`SessionInterrupted`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.contrib.sessions.exceptions.SessionInterrupted "django.contrib.sessions.exceptions.SessionInterrupted") is raised when a session is destroyed in a concurrent request. It’s a subclass of [`BadRequest`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.BadRequest "django.core.exceptions.BadRequest").

Transaction Exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#transaction-exceptions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

Transaction exceptions are defined in `django.db.transaction`.

### `TransactionManagementError`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#transactionmanagementerror "Link to this heading")

_exception_ TransactionManagementError[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/transaction.py#L12)[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.transaction.TransactionManagementError "Link to this definition")
[`TransactionManagementError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.transaction.TransactionManagementError "django.db.transaction.TransactionManagementError") is raised for any and all problems related to database transactions.

Testing Framework Exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#testing-framework-exceptions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Exceptions provided by the `django.test` package.

### `RedirectCycleError`[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#redirectcycleerror "Link to this heading")

_exception_ client.RedirectCycleError[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.test.client.RedirectCycleError "Link to this definition")
[`RedirectCycleError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.test.client.RedirectCycleError "django.test.client.RedirectCycleError") is raised when the test client detects a loop or an overly long chain of redirects.

Python Exceptions[¶](https://docs.djangoproject.com/en/6.0/ref/exceptions/#python-exceptions "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Django raises built-in Python exceptions when appropriate as well. See the Python documentation for further information on the [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions "(in Python v3.14)").
