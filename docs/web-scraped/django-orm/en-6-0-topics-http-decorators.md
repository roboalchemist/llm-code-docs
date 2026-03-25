# Source: https://docs.djangoproject.com/en/6.0/topics/http/decorators/

Title: View decorators | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/topics/http/decorators/

Markdown Content:
Django provides several decorators that can be applied to views to support various HTTP features.

See [Decorating the class](https://docs.djangoproject.com/en/6.0/topics/class-based-views/intro/#id1) for how to use these decorators with class-based views.

Allowed HTTP methods[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#allowed-http-methods "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

The decorators in [`django.views.decorators.http`](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#module-django.views.decorators.http "django.views.decorators.http") can be used to restrict access to views based on the request method. These decorators will return a [`django.http.HttpResponseNotAllowed`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponseNotAllowed "django.http.HttpResponseNotAllowed") if the conditions are not met.

require_http_methods(_request\_method\_list_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/http.py#L21)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.require_http_methods "Link to this definition")
Decorator to require that a view only accepts particular request methods. Usage:

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass

Note that request methods should be in uppercase.

require_GET()[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.require_GET "Link to this definition")
Decorator to require that a view only accepts the GET method.

require_POST()[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.require_POST "Link to this definition")
Decorator to require that a view only accepts the POST method.

require_safe()[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.require_safe "Link to this definition")
Decorator to require that a view only accepts the GET and HEAD methods. These methods are commonly considered “safe” because they should not have the significance of taking an action other than retrieving the requested resource.

Note

Web servers should automatically strip the content of responses to HEAD requests while leaving the headers unchanged, so you may handle HEAD requests exactly like GET requests in your views. Since some software, such as link checkers, rely on HEAD requests, you might prefer using `require_safe` instead of `require_GET`.

Conditional view processing[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#conditional-view-processing "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

The following decorators in [`django.views.decorators.http`](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#module-django.views.decorators.http "django.views.decorators.http") can be used to control caching behavior on particular views.

condition(_etag\_func=None_, _last\_modified\_func=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/http.py#L83)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.condition "Link to this definition")conditional_page()[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.conditional_page "Link to this definition")
This decorator provides the conditional GET operation handling of [`ConditionalGetMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.http.ConditionalGetMiddleware "django.middleware.http.ConditionalGetMiddleware") to a view.

etag(_etag\_func_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/http.py#L164)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.etag "Link to this definition")last_modified(_last\_modified\_func_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/http.py#L168)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.http.last_modified "Link to this definition")
These decorators can be used to generate `ETag` and `Last-Modified` headers; see [conditional view processing](https://docs.djangoproject.com/en/6.0/topics/conditional-view-processing/).

GZip compression[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#gzip-compression "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

The decorators in [`django.views.decorators.gzip`](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#module-django.views.decorators.gzip "django.views.decorators.gzip") control content compression on a per-view basis.

gzip_page()[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.gzip.gzip_page "Link to this definition")
This decorator compresses content if the browser allows gzip compression. It sets the `Vary` header accordingly, so that caches will base their storage on the `Accept-Encoding` header.

Vary headers[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#vary-headers "Link to this heading")
------------------------------------------------------------------------------------------------------------------

The decorators in [`django.views.decorators.vary`](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#module-django.views.decorators.vary "django.views.decorators.vary") can be used to control caching based on specific request headers.

vary_on_cookie(_func_)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.vary.vary_on_cookie "Link to this definition")vary_on_headers(_*headers_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/vary.py#L8)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.vary.vary_on_headers "Link to this definition")
The `Vary` header defines which request headers a cache mechanism should take into account when building its cache key.

See [using vary headers](https://docs.djangoproject.com/en/6.0/topics/cache/#using-vary-headers).

Caching[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#caching "Link to this heading")
--------------------------------------------------------------------------------------------------------

The decorators in [`django.views.decorators.cache`](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#module-django.views.decorators.cache "django.views.decorators.cache") control server and client-side caching.

cache_control(_**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/cache.py#L40)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.cache.cache_control "Link to this definition")
This decorator patches the response’s `Cache-Control` header by adding all of the keyword arguments to it. See [`patch_cache_control()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.cache.patch_cache_control "django.utils.cache.patch_cache_control") for the details of the transformation.

never_cache(_view\_func_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/cache.py#L63)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.cache.never_cache "Link to this definition")
This decorator adds an `Expires` header to the current date/time.

This decorator adds a 
```
Cache-Control: max-age=0, no-cache, no-store,
must-revalidate, private
```
 header to a response to indicate that a page should never be cached.

Each header is only added if it isn’t already set.

Common[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#common "Link to this heading")
------------------------------------------------------------------------------------------------------

The decorators in [`django.views.decorators.common`](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#module-django.views.decorators.common "django.views.decorators.common") allow per-view customization of [`CommonMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware") behavior.

no_append_slash()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/views/decorators/common.py#L6)[¶](https://docs.djangoproject.com/en/6.0/topics/http/decorators/#django.views.decorators.common.no_append_slash "Link to this definition")
This decorator allows individual views to be excluded from [`APPEND_SLASH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-APPEND_SLASH) URL normalization.
