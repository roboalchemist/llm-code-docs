# Source: https://docs.djangoproject.com/en/6.0/ref/views/

Title: Built-in Views | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/views/

Markdown Content:
Several of Django’s built-in views are documented in [Writing views](https://docs.djangoproject.com/en/6.0/topics/http/views/) as well as elsewhere in the documentation.

Serving files in development[¶](https://docs.djangoproject.com/en/6.0/ref/views/#serving-files-in-development "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

static.serve(_request_, _path_, _document\_root_, _show\_indexes=False_)[¶](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.static.serve "Link to this definition")
There may be files other than your project’s static assets that, for convenience, you’d like to have Django serve for you in local development. The [`serve()`](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.static.serve "django.views.static.serve") view can be used to serve any directory you give it. (This view is **not** hardened for production use and should be used only as a development aid; you should serve these files in production using a real front-end web server).

The most likely example is user-uploaded content in [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT). `django.contrib.staticfiles` is intended for static assets and has no built-in handling for user-uploaded files, but you can have Django serve your [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) by appending something like this to your URLconf:

from django.conf import settings
from django.urls import re_path
from django.views.static import serve

# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]

Note, the snippet assumes your [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL) has a value of `'media/'`. This will call the [`serve()`](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.static.serve "django.views.static.serve") view, passing in the path from the URLconf and the (required) `document_root` parameter.

Since it can become a bit cumbersome to define this URL pattern, Django ships with a small URL helper function [`static()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.conf.urls.static.static "django.conf.urls.static.static") that takes as parameters the prefix such as [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL) and a dotted path to a view, such as `'django.views.static.serve'`. Any other function parameter will be transparently passed to the view.

Error views[¶](https://docs.djangoproject.com/en/6.0/ref/views/#error-views "Link to this heading")
---------------------------------------------------------------------------------------------------

Django comes with a few views by default for handling HTTP errors. To override these with your own custom views, see [Customizing error views](https://docs.djangoproject.com/en/6.0/topics/http/views/#customizing-error-views).

### The 404 (page not found) view[¶](https://docs.djangoproject.com/en/6.0/ref/views/#the-404-page-not-found-view "Link to this heading")

defaults.page_not_found(_request_, _exception_, _template\_name='404.html'_)[¶](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.defaults.page_not_found "Link to this definition")
When you raise [`Http404`](https://docs.djangoproject.com/en/6.0/topics/http/views/#django.http.Http404 "django.http.Http404") from within a view, Django loads a special view devoted to handling 404 errors. By default, it’s the view [`django.views.defaults.page_not_found()`](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.defaults.page_not_found "django.views.defaults.page_not_found"), which either produces a “Not Found” message or loads and renders the template `404.html` if you created it in your root template directory.

The default 404 view will pass two variables to the template: `request_path`, which is the URL that resulted in the error, and `exception`, which is a useful representation of the exception that triggered the view (e.g. containing any message passed to a specific `Http404` instance).

Three things to note about 404 views:

*   The 404 view is also called if Django doesn’t find a match after checking every regular expression in the URLconf.

*   The 404 view is passed a [`RequestContext`](https://docs.djangoproject.com/en/6.0/ref/templates/api/#django.template.RequestContext "django.template.RequestContext") and will have access to variables supplied by your template context processors (e.g. `MEDIA_URL`).

*   If [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is set to `True` (in your settings module), then your 404 view will never be used, and your URLconf will be displayed instead, with some debug information.

### The 500 (server error) view[¶](https://docs.djangoproject.com/en/6.0/ref/views/#the-500-server-error-view "Link to this heading")

defaults.server_error(_request_, _template\_name='500.html'_)[¶](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.defaults.server_error "Link to this definition")
Similarly, Django executes special-case behavior in the case of runtime errors in view code. If a view results in an exception, Django will, by default, call the view `django.views.defaults.server_error`, which either produces a “Server Error” message or loads and renders the template `500.html` if you created it in your root template directory.

The default 500 view passes no variables to the `500.html` template and is rendered with an empty `Context` to lessen the chance of additional errors.

If [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is set to `True` (in your settings module), then your 500 view will never be used, and the traceback will be displayed instead, with some debug information.

### The 403 (HTTP Forbidden) view[¶](https://docs.djangoproject.com/en/6.0/ref/views/#the-403-http-forbidden-view "Link to this heading")

defaults.permission_denied(_request_, _exception_, _template\_name='403.html'_)[¶](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.defaults.permission_denied "Link to this definition")
In the same vein as the 404 and 500 views, Django has a view to handle 403 Forbidden errors. If a view results in a 403 exception then Django will, by default, call the view `django.views.defaults.permission_denied`.

This view loads and renders the template `403.html` in your root template directory, or if this file does not exist, instead serves the text “403 Forbidden”, as per [**RFC 9110 Section 15.5.4**](https://datatracker.ietf.org/doc/html/rfc9110.html#section-15.5.4) (the HTTP 1.1 Specification). The template context contains `exception`, which is the string representation of the exception that triggered the view.

`django.views.defaults.permission_denied` is triggered by a [`PermissionDenied`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied") exception. To deny access in a view you can use code like this:

from django.core.exceptions import PermissionDenied

def edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    # ...

### The 400 (bad request) view[¶](https://docs.djangoproject.com/en/6.0/ref/views/#the-400-bad-request-view "Link to this heading")

defaults.bad_request(_request_, _exception_, _template\_name='400.html'_)[¶](https://docs.djangoproject.com/en/6.0/ref/views/#django.views.defaults.bad_request "Link to this definition")
Similarly, Django has a view to handle 400 Bad Request errors.

This view either produces a “Bad Request” message or loads and renders the template `400.html` if you created it in your root template directory. It returns with status code 400 indicating that the error condition was the result of a client operation. By default, nothing related to the exception that triggered the view is passed to the template context, as the exception message might contain sensitive information like filesystem paths.

`django.views.defaults.bad_request` is triggered by a [`BadRequest`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.BadRequest "django.core.exceptions.BadRequest") exception. Also, when a [`SuspiciousOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") is raised in Django, it may be handled by a component of Django (for example resetting the session data). If not specifically handled, Django will consider the current request a ‘bad request’ instead of a server error, and handle it with `bad_request`.

`bad_request` views are also only used when [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is `False`.
