# Source: https://docs.djangoproject.com/en/6.0/ref/settings/

Title: Settings | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/settings/

Markdown Content:
Settings | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/settings/#main-content)

[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.

Menu Main navigation
*   [Overview](https://www.djangoproject.com/start/overview/)
*   [Download](https://www.djangoproject.com/download/)
*   [Documentation](https://docs.djangoproject.com/)
*   [News](https://www.djangoproject.com/weblog/)
*   [Code](https://github.com/django/django)
*   [Issues](https://code.djangoproject.com/)
*   [Community](https://www.djangoproject.com/community/)
*   [Foundation](https://www.djangoproject.com/foundation/)
*   [♥ Donate](https://www.djangoproject.com/fundraising/)

Search Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

*   [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

*   Language: **en**
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/settings/)
*   [sv](https://docs.djangoproject.com/sv/6.0/ref/settings/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/settings/)
*   [pl](https://docs.djangoproject.com/pl/6.0/ref/settings/)
*   [ko](https://docs.djangoproject.com/ko/6.0/ref/settings/)
*   [ja](https://docs.djangoproject.com/ja/6.0/ref/settings/)
*   [it](https://docs.djangoproject.com/it/6.0/ref/settings/)
*   [id](https://docs.djangoproject.com/id/6.0/ref/settings/)
*   [fr](https://docs.djangoproject.com/fr/6.0/ref/settings/)
*   [es](https://docs.djangoproject.com/es/6.0/ref/settings/)
*   [el](https://docs.djangoproject.com/el/6.0/ref/settings/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/ref/settings/)
*   [5.2](https://docs.djangoproject.com/en/5.2/ref/settings/)
*   [5.1](https://docs.djangoproject.com/en/5.1/ref/settings/)
*   [5.0](https://docs.djangoproject.com/en/5.0/ref/settings/)
*   [4.2](https://docs.djangoproject.com/en/4.2/ref/settings/)
*   [4.1](https://docs.djangoproject.com/en/4.1/ref/settings/)
*   [4.0](https://docs.djangoproject.com/en/4.0/ref/settings/)
*   [3.2](https://docs.djangoproject.com/en/3.2/ref/settings/)
*   [3.1](https://docs.djangoproject.com/en/3.1/ref/settings/)
*   [3.0](https://docs.djangoproject.com/en/3.0/ref/settings/)
*   [2.2](https://docs.djangoproject.com/en/2.2/ref/settings/)
*   [2.1](https://docs.djangoproject.com/en/2.1/ref/settings/)
*   [2.0](https://docs.djangoproject.com/en/2.0/ref/settings/)
*   [1.11](https://docs.djangoproject.com/en/1.11/ref/settings/)
*   [1.10](https://docs.djangoproject.com/en/1.10/ref/settings/)
*   [1.8](https://docs.djangoproject.com/en/1.8/ref/settings/)

*   [](https://docs.djangoproject.com/en/6.0/ref/settings/#top)

Settings[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#settings "Link to this heading")
================================================================================================

*   [Core Settings](https://docs.djangoproject.com/en/6.0/ref/settings/#core-settings)

*   [Auth](https://docs.djangoproject.com/en/6.0/ref/settings/#auth)

*   [Messages](https://docs.djangoproject.com/en/6.0/ref/settings/#messages)

*   [Sessions](https://docs.djangoproject.com/en/6.0/ref/settings/#sessions)

*   [Sites](https://docs.djangoproject.com/en/6.0/ref/settings/#sites)

*   [Static Files](https://docs.djangoproject.com/en/6.0/ref/settings/#static-files)

*   [Core Settings Topical Index](https://docs.djangoproject.com/en/6.0/ref/settings/#core-settings-topical-index)

Warning

Be careful when you override settings, especially when the default value is a non-empty list or dictionary, such as [`STATICFILES_FINDERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATICFILES_FINDERS). Make sure you keep the components required by the features of Django you wish to use.

[Core Settings](https://docs.djangoproject.com/en/6.0/ref/settings/#id14)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#core-settings "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here’s a list of settings available in Django core and their default values. Settings provided by contrib apps are listed below, followed by a topical index of the core settings. For introductory material, see the [settings topic guide](https://docs.djangoproject.com/en/6.0/topics/settings/).

### `ABSOLUTE_URL_OVERRIDES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#absolute-url-overrides "Link to this heading")

Default: `{}` (Empty dictionary)

A dictionary mapping `"app_label.model_name"` strings to functions that take a model object and return its URL. This is a way of inserting or overriding `get_absolute_url()` methods on a per-installation basis. Example:

ABSOLUTE_URL_OVERRIDES = {
    "blogs.blog": lambda o: "/blogs/%s/" % o.slug,
    "news.story": lambda o: "/stories/%s/%s/" % (o.pub_year, o.slug),
}

The model name used in this setting should be all lowercase, regardless of the case of the actual model class name.

### `ADMINS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#admins "Link to this heading")

Default: `[]` (Empty list)

A list of all the people who get code error notifications. When [`DEBUG=False`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) and [`AdminEmailHandler`](https://docs.djangoproject.com/en/6.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") is configured in [`LOGGING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LOGGING) (done by default), Django emails these people the details of exceptions raised in the request/response cycle.

Each item in the list should be an email address string. Example:

ADMINS = ["john@example.com", '"Ng, Mary" <mary@example.com>']

Changed in Django 6.0:
In older versions, required a list of (name, address) tuples.

### `ALLOWED_HOSTS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#allowed-hosts "Link to this heading")

Default: `[]` (Empty list)

A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent [HTTP Host header attacks](https://docs.djangoproject.com/en/6.0/topics/security/#host-headers-virtual-hosting), which are possible even under many seemingly-safe web server configurations.

Values in this list can be fully qualified names (e.g. `'www.example.com'`), in which case they will be matched against the request’s `Host` header exactly (case-insensitive, not including port). A value beginning with a period can be used as a subdomain wildcard: `'.example.com'` will match `example.com`, `www.example.com`, and any other subdomain of `example.com`. A value of `'*'` will match anything; in this case you are responsible to provide your own validation of the `Host` header (perhaps in a middleware; if so this middleware must be listed first in [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIDDLEWARE)).

Django also allows the [fully qualified domain name (FQDN)](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) of any entries. Some browsers include a trailing dot in the `Host` header which Django strips when performing host validation.

If the `Host` header (or `X-Forwarded-Host` if [`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST) is enabled) does not match any value in this list, the [`django.http.HttpRequest.get_host()`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") method will raise [`SuspiciousOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation").

When [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is `True` and `ALLOWED_HOSTS` is empty, the host is validated against `['.localhost', '127.0.0.1', '[::1]']`.

`ALLOWED_HOSTS` is also [checked when running tests](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/#topics-testing-advanced-multiple-hosts).

This validation only applies via [`get_host()`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host"); if your code accesses the `Host` header directly from `request.META` you are bypassing this security protection.

### `APPEND_SLASH`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#append-slash "Link to this heading")

Default: `True`

When set to `True`, if the request URL does not match any of the patterns in the URLconf and it doesn’t end in a slash, an HTTP redirect is issued to the same URL with a slash appended. Note that the redirect may cause any data submitted in a POST request to be lost.

The [`APPEND_SLASH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-APPEND_SLASH) setting is only used if [`CommonMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware") is installed (see [Middleware](https://docs.djangoproject.com/en/6.0/topics/http/middleware/)). See also [`PREPEND_WWW`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PREPEND_WWW).

### `CACHES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#caches "Link to this heading")

Default:

{
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

A dictionary containing the settings for all caches to be used with Django. It is a nested dictionary whose contents maps cache aliases to a dictionary containing the options for an individual cache.

The [`CACHES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHES) setting must configure a `default` cache; any number of additional caches may also be specified. If you are using a cache backend other than the local memory cache, or you need to define multiple caches, other options will be required. The following cache options are available.

#### `BACKEND`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#backend "Link to this heading")

Default: `''` (Empty string)

The cache backend to use. The built-in cache backends are:

*   `'django.core.cache.backends.db.DatabaseCache'`

*   `'django.core.cache.backends.dummy.DummyCache'`

*   `'django.core.cache.backends.filebased.FileBasedCache'`

*   `'django.core.cache.backends.locmem.LocMemCache'`

*   `'django.core.cache.backends.memcached.PyMemcacheCache'`

*   `'django.core.cache.backends.memcached.PyLibMCCache'`

*   `'django.core.cache.backends.redis.RedisCache'`

You can use a cache backend that doesn’t ship with Django by setting [`BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHES-BACKEND) to a fully-qualified path of a cache backend class (i.e. `mypackage.backends.whatever.WhateverCache`).

#### `KEY_FUNCTION`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#key-function "Link to this heading")

A string containing a dotted path to a function (or any callable) that defines how to compose a prefix, version and key into a final cache key. The default implementation is equivalent to the function:

def make_key(key, key_prefix, version):
    return ":".join([key_prefix, str(version), key])

You may use any key function you want, as long as it has the same argument signature.

See the [cache documentation](https://docs.djangoproject.com/en/6.0/topics/cache/#cache-key-transformation) for more information.

#### `KEY_PREFIX`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#key-prefix "Link to this heading")

Default: `''` (Empty string)

A string that will be automatically included (prepended by default) to all cache keys used by the Django server.

See the [cache documentation](https://docs.djangoproject.com/en/6.0/topics/cache/#cache-key-prefixing) for more information.

#### `LOCATION`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#location "Link to this heading")

Default: `''` (Empty string)

The location of the cache to use. This might be the directory for a file system cache, a host and port for a memcache server, or an identifying name for a local memory cache. e.g.:

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

#### `OPTIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#options "Link to this heading")

Default: `None`

Extra parameters to pass to the cache backend. Available parameters vary depending on your cache backend.

Some information on available parameters can be found in the [cache arguments](https://docs.djangoproject.com/en/6.0/topics/cache/#cache-arguments) documentation. For more information, consult your backend module’s own documentation.

#### `TIMEOUT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#timeout "Link to this heading")

Default: `300`

The number of seconds before a cache entry is considered stale. If the value of this setting is `None`, cache entries will not expire. A value of `0` causes keys to immediately expire (effectively “don’t cache”).

#### `VERSION`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#version "Link to this heading")

Default: `1`

The default version number for cache keys generated by the Django server.

See the [cache documentation](https://docs.djangoproject.com/en/6.0/topics/cache/#cache-versioning) for more information.

### `CACHE_MIDDLEWARE_ALIAS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#cache-middleware-alias "Link to this heading")

Default: `'default'`

The cache connection to use for the [cache middleware](https://docs.djangoproject.com/en/6.0/topics/cache/#the-per-site-cache).

### `CACHE_MIDDLEWARE_KEY_PREFIX`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#cache-middleware-key-prefix "Link to this heading")

Default: `''` (Empty string)

A string which will be prefixed to the cache keys generated by the [cache middleware](https://docs.djangoproject.com/en/6.0/topics/cache/#the-per-site-cache). This prefix is combined with the [`KEY_PREFIX`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHES-KEY_PREFIX) setting; it does not replace it.

See [Django’s cache framework](https://docs.djangoproject.com/en/6.0/topics/cache/).

### `CACHE_MIDDLEWARE_SECONDS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#cache-middleware-seconds "Link to this heading")

Default: `600`

The default integer number of seconds to cache a page for the [cache middleware](https://docs.djangoproject.com/en/6.0/topics/cache/#the-per-site-cache).

See [Django’s cache framework](https://docs.djangoproject.com/en/6.0/topics/cache/).

### `CSRF_COOKIE_AGE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-age "Link to this heading")

Default: `31449600` (approximately 1 year, in seconds)

The age of CSRF cookies, in seconds.

The reason for setting a long-lived expiration time is to avoid problems in the case of a user closing a browser or bookmarking a page and then loading that page from a browser cache. Without persistent cookies, the form submission would fail in this case.

Some browsers (specifically Internet Explorer) can disallow the use of persistent cookies or can have the indexes to the cookie jar corrupted on disk, thereby causing CSRF protection checks to (sometimes intermittently) fail. Change this setting to `None` to use session-based CSRF cookies, which keep the cookies in-memory instead of on persistent storage.

### `CSRF_COOKIE_DOMAIN`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-domain "Link to this heading")

Default: `None`

The domain to be used when setting the CSRF cookie. This can be useful for easily allowing cross-subdomain requests to be excluded from the normal cross site request forgery protection. It should be set to a string such as `".example.com"` to allow a POST request from a form on one subdomain to be accepted by a view served from another subdomain.

Please note that the presence of this setting does not imply that Django’s CSRF protection is safe from cross-subdomain attacks by default - please see the [CSRF limitations](https://docs.djangoproject.com/en/6.0/ref/csrf/#csrf-limitations) section.

### `CSRF_COOKIE_HTTPONLY`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-httponly "Link to this heading")

Default: `False`

Whether to use `HttpOnly` flag on the CSRF cookie. If this is set to `True`, client-side JavaScript will not be able to access the CSRF cookie.

Designating the CSRF cookie as `HttpOnly` doesn’t offer any practical protection because CSRF is only to protect against cross-domain attacks. If an attacker can read the cookie via JavaScript, they’re already on the same domain as far as the browser knows, so they can do anything they like anyway. (XSS is a much bigger hole than CSRF.)

Although the setting offers little practical benefit, it’s sometimes required by security auditors.

If you enable this and need to send the value of the CSRF token with an AJAX request, your JavaScript must pull the value [from a hidden CSRF token form input](https://docs.djangoproject.com/en/6.0/howto/csrf/#acquiring-csrf-token-from-html) instead of [from the cookie](https://docs.djangoproject.com/en/6.0/howto/csrf/#acquiring-csrf-token-from-cookie).

See [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) for details on `HttpOnly`.

### `CSRF_COOKIE_NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-name "Link to this heading")

Default: `'csrftoken'`

The name of the cookie to use for the CSRF authentication token. This can be whatever you want (as long as it’s different from the other cookie names in your application). See [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/6.0/ref/csrf/).

### `CSRF_COOKIE_PATH`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-path "Link to this heading")

Default: `'/'`

The path set on the CSRF cookie. This should either match the URL path of your Django installation or be a parent of that path.

This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths, and each instance will only see its own CSRF cookie.

### `CSRF_COOKIE_SAMESITE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-samesite "Link to this heading")

Default: `'Lax'`

The value of the [SameSite](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#samesitesamesite-value) flag on the CSRF cookie. This flag prevents the cookie from being sent in cross-site requests.

See [`SESSION_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SESSION_COOKIE_SAMESITE) for details about `SameSite`.

### `CSRF_COOKIE_SECURE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-secure "Link to this heading")

Default: `False`

Whether to use a secure cookie for the CSRF cookie. If this is set to `True`, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent with an HTTPS connection.

### `CSRF_USE_SESSIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-use-sessions "Link to this heading")

Default: `False`

Whether to store the CSRF token in the user’s session instead of in a cookie. It requires the use of [`django.contrib.sessions`](https://docs.djangoproject.com/en/6.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects.").

Storing the CSRF token in a cookie (Django’s default) is safe, but storing it in the session is common practice in other web frameworks and therefore sometimes demanded by security auditors.

Since the [default error views](https://docs.djangoproject.com/en/6.0/ref/views/#error-views) require the CSRF token, [`SessionMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware") must appear in [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIDDLEWARE) before any middleware that may raise an exception to trigger an error view (such as [`PermissionDenied`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied")) if you’re using `CSRF_USE_SESSIONS`. See [Middleware ordering](https://docs.djangoproject.com/en/6.0/ref/middleware/#middleware-ordering).

### `CSRF_FAILURE_VIEW`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-failure-view "Link to this heading")

Default: `'django.views.csrf.csrf_failure'`

A dotted path to the view function to be used when an incoming request is rejected by the [CSRF protection](https://docs.djangoproject.com/en/6.0/ref/csrf/). The function should have this signature:

def csrf_failure(request, reason=""): ...

where `reason` is a short message (intended for developers or logging, not for end users) indicating the reason the request was rejected. It should return an [`HttpResponseForbidden`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponseForbidden "django.http.HttpResponseForbidden").

`django.views.csrf.csrf_failure()` accepts an additional `template_name` parameter that defaults to `'403_csrf.html'`. If a template with that name exists, it will be used to render the page.

### `CSRF_HEADER_NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-header-name "Link to this heading")

Default: `'HTTP_X_CSRFTOKEN'`

The name of the request header used for CSRF authentication.

As with other HTTP headers in `request.META`, the header name received from the server is normalized by converting all characters to uppercase, replacing any hyphens with underscores, and adding an `'HTTP_'` prefix to the name. For example, if your client sends a `'X-XSRF-TOKEN'` header, the setting should be `'HTTP_X_XSRF_TOKEN'`.

### `CSRF_TRUSTED_ORIGINS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-trusted-origins "Link to this heading")

Default: `[]` (Empty list)

A list of trusted origins for unsafe requests (e.g. `POST`).

For requests that include the `Origin` header, Django’s CSRF protection requires that header match the origin present in the `Host` header.

For a [`secure`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.is_secure "django.http.HttpRequest.is_secure") unsafe request that doesn’t include the `Origin` header, the request must have a `Referer` header that matches the origin present in the `Host` header.

These checks prevent, for example, a `POST` request from `subdomain.example.com` from succeeding against `api.example.com`. If you need cross-origin unsafe requests, continuing the example, add `'https://subdomain.example.com'` to this list (and/or `http://...` if requests originate from an insecure page).

The setting also supports subdomains, so you could add `'https://*.example.com'`, for example, to allow access from all subdomains of `example.com`.

### `DATABASES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#databases "Link to this heading")

Default: `{}` (Empty dictionary)

A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database.

The [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) setting must configure a `default` database; any number of additional databases may also be specified.

The simplest possible settings file is for a single-database setup using SQLite. This can be configured using the following:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}

When connecting to other database backends, such as MariaDB, MySQL, Oracle, or PostgreSQL, additional connection parameters will be required. See the [`ENGINE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-ENGINE) setting below on how to specify other database types. This example is for PostgreSQL:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

The following inner options that may be required for more complex configurations are available:

#### `ATOMIC_REQUESTS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#atomic-requests "Link to this heading")

Default: `False`

Set this to `True` to wrap each view in a transaction on this database. See [Tying transactions to HTTP requests](https://docs.djangoproject.com/en/6.0/topics/db/transactions/#tying-transactions-to-http-requests).

#### `AUTOCOMMIT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#autocommit "Link to this heading")

Default: `True`

Set this to `False` if you want to [disable Django’s transaction management](https://docs.djangoproject.com/en/6.0/topics/db/transactions/#deactivate-transaction-management) and implement your own.

#### `ENGINE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#engine "Link to this heading")

Default: `''` (Empty string)

The database backend to use. The built-in database backends are:

*   `'django.db.backends.postgresql'`

*   `'django.db.backends.mysql'`

*   `'django.db.backends.sqlite3'`

*   `'django.db.backends.oracle'`

You can use a database backend that doesn’t ship with Django by setting `ENGINE` to a fully-qualified path (i.e. `mypackage.backends.whatever`).

#### `HOST`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#host "Link to this heading")

Default: `''` (Empty string)

Which host to use when connecting to the database. An empty string means localhost. Not used with SQLite.

If this value starts with a forward slash (`'/'`) and you’re using MySQL, MySQL will connect via a Unix socket to the specified socket. For example:

"HOST": "/var/run/mysql"

If you’re using MySQL and this value _doesn’t_ start with a forward slash, then this value is assumed to be the host.

If you’re using PostgreSQL, by default (empty [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST)), the connection to the database is done through UNIX domain sockets (‘local’ lines in `pg_hba.conf`). If your UNIX domain socket is not in the standard location, use the same value of `unix_socket_directory` from `postgresql.conf`. If you want to connect through TCP sockets, set [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST) to ‘localhost’ or ‘127.0.0.1’ (‘host’ lines in `pg_hba.conf`). On Windows, you should always define [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST), as UNIX domain sockets are not available.

#### `NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#name "Link to this heading")

Default: `''` (Empty string)

The name of the database to use. For SQLite, it’s the full path to the database file. When specifying the path, always use forward slashes, even on Windows (e.g. `C:/homes/user/mysite/sqlite3.db`).

#### `CONN_MAX_AGE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#conn-max-age "Link to this heading")

Default: `0`

The lifetime of a database connection, as an integer of seconds. Use `0` to close database connections at the end of each request — Django’s historical behavior — and `None` for unlimited [persistent database connections](https://docs.djangoproject.com/en/6.0/ref/databases/#persistent-database-connections).

#### `CONN_HEALTH_CHECKS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#conn-health-checks "Link to this heading")

Default: `False`

If set to `True`, existing [persistent database connections](https://docs.djangoproject.com/en/6.0/ref/databases/#persistent-database-connections) will be health checked before they are reused in each request performing database access. If the health check fails, the connection will be reestablished without failing the request when the connection is no longer usable but the database server is ready to accept and serve new connections (e.g. after database server restart closing existing connections).

#### `OPTIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS "Link to this heading")

Default: `{}` (Empty dictionary)

Extra parameters to use when connecting to the database. Available parameters vary depending on your database backend.

Some information on available parameters can be found in the [Database Backends](https://docs.djangoproject.com/en/6.0/ref/databases/) documentation. For more information, consult your backend module’s own documentation.

#### `PASSWORD`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#password "Link to this heading")

Default: `''` (Empty string)

The password to use when connecting to the database. Not used with SQLite.

#### `PORT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#port "Link to this heading")

Default: `''` (Empty string)

The port to use when connecting to the database. An empty string means the default port. Not used with SQLite.

#### `TIME_ZONE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#time-zone "Link to this heading")

Default: `None`

A string representing the time zone for this database connection or `None`. This inner option of the [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) setting accepts the same values as the general [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) setting.

When [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, reading datetimes from the database returns aware datetimes with the timezone set to this option’s value if not `None`, or to UTC otherwise.

When [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `False`, it is an error to set this option.

*   If the database backend doesn’t support time zones (e.g. SQLite, MySQL, Oracle), Django reads and writes datetimes in local time according to this option if it is set and in UTC if it isn’t.

Changing the connection time zone changes how datetimes are read from and written to the database.

    *   If Django manages the database and you don’t have a strong reason to do otherwise, you should leave this option unset. It’s best to store datetimes in UTC because it avoids ambiguous or nonexistent datetimes during daylight saving time changes. Also, receiving datetimes in UTC keeps datetime arithmetic simple — there’s no need to consider potential offset changes over a DST transition.

    *   If you’re connecting to a third-party database that stores datetimes in a local time rather than UTC, then you must set this option to the appropriate time zone. Likewise, if Django manages the database but third-party systems connect to the same database and expect to find datetimes in local time, then you must set this option.

*   If the database backend supports time zones (e.g., PostgreSQL), then the database connection’s time zone is set to this value.

Although setting the `TIME_ZONE` option is very rarely needed, there are situations where it becomes necessary. Specifically, it’s recommended to match the general [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) setting when dealing with raw queries involving date/time functions like PostgreSQL’s `date_trunc()` or `generate_series()`, especially when generating time-based series that transition daylight savings.

This value can be changed at any time, the database will handle the conversion of datetimes to the configured time zone.

However, this has a downside: receiving all datetimes in local time makes datetime arithmetic more tricky — you must account for possible offset changes over DST transitions.

Consider converting to local time explicitly with `AT TIME ZONE` in raw SQL queries instead of setting the `TIME_ZONE` option.

#### `DISABLE_SERVER_SIDE_CURSORS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#disable-server-side-cursors "Link to this heading")

Default: `False`

Set this to `True` if you want to disable the use of server-side cursors with [`QuerySet.iterator()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.iterator "django.db.models.query.QuerySet.iterator"). [Transaction pooling and server-side cursors](https://docs.djangoproject.com/en/6.0/ref/databases/#transaction-pooling-server-side-cursors) describes the use case.

This is a PostgreSQL-specific setting.

#### `USER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#user "Link to this heading")

Default: `''` (Empty string)

The username to use when connecting to the database. Not used with SQLite.

#### `TEST`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#test "Link to this heading")

Default: `{}` (Empty dictionary)

A dictionary of settings for test databases; for more details about the creation and use of test databases, see [The test database](https://docs.djangoproject.com/en/6.0/topics/testing/overview/#the-test-database).

Here’s an example with a test database configuration:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": "mydatabaseuser",
        "NAME": "mydatabase",
        "TEST": {
            "NAME": "mytestdatabase",
        },
    },
}

The following keys in the `TEST` dictionary are available:

##### `CHARSET`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#charset "Link to this heading")

Default: `None`

The character set encoding used to create the test database. The value of this string is passed directly through to the database, so its format is backend-specific.

Supported by the [PostgreSQL](https://www.postgresql.org/docs/current/multibyte.html) (`postgresql`) and [MySQL](https://dev.mysql.com/doc/refman/en/charset-charsets.html) (`mysql`) backends.

##### `COLLATION`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#collation "Link to this heading")

Default: `None`

The collation order to use when creating the test database. This value is passed directly to the backend, so its format is backend-specific.

Only supported for the `mysql` backend (see the [MySQL manual](https://dev.mysql.com/doc/refman/en/charset-charsets.html) for details).

##### `DEPENDENCIES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#dependencies "Link to this heading")

Default: `['default']`, for all databases other than `default`, which has no dependencies.

The creation-order dependencies of the database. See the documentation on [controlling the creation order of test databases](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/#topics-testing-creation-dependencies) for details.

##### `MIGRATE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#migrate "Link to this heading")

Default: `True`

When set to `False`, migrations won’t run when creating the test database. This is similar to setting `None` as a value in [`MIGRATION_MODULES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIGRATION_MODULES), but for all apps.

##### `MIRROR`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#mirror "Link to this heading")

Default: `None`

The alias of the database that this database should mirror during testing. It depends on transactions and therefore must be used within [`TransactionTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") instead of [`TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase").

This setting exists to allow for testing of primary/replica (referred to as master/slave by some databases) configurations of multiple databases. See the documentation on [testing primary/replica configurations](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/#topics-testing-primaryreplica) for details.

##### `NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_NAME "Link to this heading")

Default: `None`

The name of database to use when running the test suite.

If the default value (`None`) is used with the SQLite database engine, the tests will use a memory resident database. For all other database engines the test database will use the name `'test_' + DATABASE_NAME`.

See [The test database](https://docs.djangoproject.com/en/6.0/topics/testing/overview/#the-test-database).

##### `TEMPLATE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#template "Link to this heading")

This is a PostgreSQL-specific setting.

The name of a [template](https://www.postgresql.org/docs/current/sql-createdatabase.html) (e.g. `'template0'`) from which to create the test database.

##### `CREATE_DB`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#create-db "Link to this heading")

Default: `True`

This is an Oracle-specific setting.

If it is set to `False`, the test tablespaces won’t be automatically created at the beginning of the tests or dropped at the end.

##### `CREATE_USER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#create-user "Link to this heading")

Default: `True`

This is an Oracle-specific setting.

If it is set to `False`, the test user won’t be automatically created at the beginning of the tests and dropped at the end.

##### `USER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_USER "Link to this heading")

Default: `None`

This is an Oracle-specific setting.

The username to use when connecting to the Oracle database that will be used when running tests. If not provided, Django will use `'test_' + USER`.

##### `PASSWORD`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_PASSWD "Link to this heading")

Default: `None`

This is an Oracle-specific setting.

The password to use when connecting to the Oracle database that will be used when running tests. If not provided, Django will generate a random password.

##### `ORACLE_MANAGED_FILES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#oracle-managed-files "Link to this heading")

Default: `False`

This is an Oracle-specific setting.

If set to `True`, Oracle Managed Files (OMF) tablespaces will be used. [`DATAFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATAFILE) and [`DATAFILE_TMP`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATAFILE_TMP) will be ignored.

##### `TBLSPACE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#tblspace "Link to this heading")

Default: `None`

This is an Oracle-specific setting.

The name of the tablespace that will be used when running tests. If not provided, Django will use `'test_' + USER`.

##### `TBLSPACE_TMP`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#tblspace-tmp "Link to this heading")

Default: `None`

This is an Oracle-specific setting.

The name of the temporary tablespace that will be used when running tests. If not provided, Django will use `'test_' + USER + '_temp'`.

##### `DATAFILE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile "Link to this heading")

Default: `None`

This is an Oracle-specific setting.

The name of the datafile to use for the TBLSPACE. If not provided, Django will use `TBLSPACE + '.dbf'`.

##### `DATAFILE_TMP`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp "Link to this heading")

Default: `None`

This is an Oracle-specific setting.

The name of the datafile to use for the TBLSPACE_TMP. If not provided, Django will use `TBLSPACE_TMP + '.dbf'`.

##### `DATAFILE_MAXSIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-maxsize "Link to this heading")

Default: `'500M'`

This is an Oracle-specific setting.

The maximum size that the DATAFILE is allowed to grow to.

##### `DATAFILE_TMP_MAXSIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp-maxsize "Link to this heading")

Default: `'500M'`

This is an Oracle-specific setting.

The maximum size that the DATAFILE_TMP is allowed to grow to.

##### `DATAFILE_SIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-size "Link to this heading")

Default: `'50M'`

This is an Oracle-specific setting.

The initial size of the DATAFILE.

##### `DATAFILE_TMP_SIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp-size "Link to this heading")

Default: `'50M'`

This is an Oracle-specific setting.

The initial size of the DATAFILE_TMP.

##### `DATAFILE_EXTSIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-extsize "Link to this heading")

Default: `'25M'`

This is an Oracle-specific setting.

The amount by which the DATAFILE is extended when more space is required.

##### `DATAFILE_TMP_EXTSIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp-extsize "Link to this heading")

Default: `'25M'`

This is an Oracle-specific setting.

The amount by which the DATAFILE_TMP is extended when more space is required.

### `DATA_UPLOAD_MAX_MEMORY_SIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#data-upload-max-memory-size "Link to this heading")

Default: `2621440` (i.e. 2.5 MB).

The maximum size in bytes that a request body may be before a [`SuspiciousOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") (`RequestDataTooBig`) is raised. The check is done when accessing `request.body` or `request.POST` and is calculated against the total request size excluding any file upload data. You can set this to `None` to disable the check. Applications that are expected to receive unusually large form posts should tune this setting.

The amount of request data is correlated to the amount of memory needed to process the request and populate the GET and POST dictionaries. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don’t typically perform deep request inspection, it’s not possible to perform a similar check at that level.

See also [`FILE_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_MAX_MEMORY_SIZE).

### `DATA_UPLOAD_MAX_NUMBER_FIELDS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#data-upload-max-number-fields "Link to this heading")

Default: `1000`

The maximum number of parameters that may be received via GET or POST before a [`SuspiciousOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") (`TooManyFields`) is raised. You can set this to `None` to disable the check. Applications that are expected to receive an unusually large number of form fields should tune this setting.

The number of request parameters is correlated to the amount of time needed to process the request and populate the GET and POST dictionaries. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don’t typically perform deep request inspection, it’s not possible to perform a similar check at that level.

### `DATA_UPLOAD_MAX_NUMBER_FILES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#data-upload-max-number-files "Link to this heading")

Default: `100`

The maximum number of files that may be received via POST in a `multipart/form-data` encoded request before a [`SuspiciousOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") (`TooManyFiles`) is raised. You can set this to `None` to disable the check. Applications that are expected to receive an unusually large number of file fields should tune this setting.

The number of accepted files is correlated to the amount of time and memory needed to process the request. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don’t typically perform deep request inspection, it’s not possible to perform a similar check at that level.

### `DATABASE_ROUTERS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#database-routers "Link to this heading")

Default: `[]` (Empty list)

The list of routers that will be used to determine which database to use when performing a database query.

See the documentation on [automatic database routing in multi database configurations](https://docs.djangoproject.com/en/6.0/topics/db/multi-db/#topics-db-multi-db-routing).

### `DATE_FORMAT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#date-format "Link to this heading")

Default: `'N j, Y'` (e.g. `Feb. 4, 2003`)

The default formatting to use for displaying date fields in any part of the system. Note that the locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date).

See also [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_FORMAT) and [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATE_FORMAT).

### `DATE_INPUT_FORMATS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#date-input-formats "Link to this heading")

Default:

[
    "%Y-%m-%d",  # '2006-10-25'
    "%m/%d/%Y",  # '10/25/2006'
    "%m/%d/%y",  # '10/25/06'
    "%b %d %Y",  # 'Oct 25 2006'
    "%b %d, %Y",  # 'Oct 25, 2006'
    "%d %b %Y",  # '25 Oct 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%B %d %Y",  # 'October 25 2006'
    "%B %d, %Y",  # 'October 25, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
]

A list of formats that will be accepted when inputting data on a date field. Formats will be tried in order, using the first valid one. Note that these format strings use Python’s [datetime module syntax](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior "(in Python v3.14)"), not the format strings from the [`date`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date) template filter.

The locale-dictated format has higher precedence and will be applied instead.

See also [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_INPUT_FORMATS) and [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_INPUT_FORMATS).

### `DATETIME_FORMAT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datetime-format "Link to this heading")

Default: `'N j, Y, P'` (e.g. `Feb. 4, 2003, 4 p.m.`)

The default formatting to use for displaying datetime fields in any part of the system. Note that the locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date).

See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_FORMAT) and [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATETIME_FORMAT).

### `DATETIME_INPUT_FORMATS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#datetime-input-formats "Link to this heading")

Default:

[
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '10/25/2006 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '10/25/2006 14:30:59.000200'
    "%m/%d/%Y %H:%M",  # '10/25/2006 14:30'
    "%m/%d/%y %H:%M:%S",  # '10/25/06 14:30:59'
    "%m/%d/%y %H:%M:%S.%f",  # '10/25/06 14:30:59.000200'
    "%m/%d/%y %H:%M",  # '10/25/06 14:30'
]

A list of formats that will be accepted when inputting data on a datetime field. Formats will be tried in order, using the first valid one. Note that these format strings use Python’s [datetime module syntax](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior "(in Python v3.14)"), not the format strings from the [`date`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date) template filter. Date-only formats are not included as datetime fields will automatically try [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_INPUT_FORMATS) in last resort.

The locale-dictated format has higher precedence and will be applied instead.

See also [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_INPUT_FORMATS) and [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_INPUT_FORMATS).

### `DEBUG`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#debug "Link to this heading")

Default: `False`

A boolean that turns on/off debug mode.

Never deploy a site into production with [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) turned on.

One of the main features of debug mode is the display of detailed error pages. If your app raises an exception when [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is `True`, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from `settings.py`).

As a security measure, Django will _not_ include settings that might be sensitive, such as [`SECRET_KEY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY). Specifically, it will exclude any setting whose name includes any of the following:

*   `'API'`

*   `'KEY'`

*   `'PASS'`

*   `'SECRET'`

*   `'SIGNATURE'`

*   `'TOKEN'`

Note that these are _partial_ matches. `'PASS'` will also match PASSWORD, just as `'TOKEN'` will also match TOKENIZED and so on.

Still, note that there are always going to be sections of your debug output that are inappropriate for public consumption. File paths, configuration options and the like all give attackers extra information about your server.

It is also important to remember that when running with [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) turned on, Django will remember every SQL query it executes. This is useful when you’re debugging, but it’ll rapidly consume memory on a production server.

Finally, if [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is `False`, you also need to properly set the [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ALLOWED_HOSTS) setting. Failing to do so will result in all requests being returned as “Bad Request (400)”.

Note

The default `settings.py` file created by [``` django-admin startproject ```](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) sets `DEBUG = True` for convenience.

### `DEBUG_PROPAGATE_EXCEPTIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#debug-propagate-exceptions "Link to this heading")

Default: `False`

If set to `True`, Django’s exception handling of view functions ([`handler500`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.conf.urls.handler500 "django.conf.urls.handler500"), or the debug view if [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is `True`) and logging of 500 responses ([django.request](https://docs.djangoproject.com/en/6.0/ref/logging/#django-request-logger)) is skipped and exceptions propagate upward.

This can be useful for some test setups. It shouldn’t be used on a live site unless you want your web server (instead of Django) to generate “Internal Server Error” responses. In that case, make sure your server doesn’t show the stack trace or other sensitive information in the response.

### `DECIMAL_SEPARATOR`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#decimal-separator "Link to this heading")

Default: `'.'` (Dot)

Default decimal separator used when formatting decimal numbers.

Note that the locale-dictated format has higher precedence and will be applied instead.

See also [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NUMBER_GROUPING), [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) and [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR).

### `DEFAULT_AUTO_FIELD`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#default-auto-field "Link to this heading")

Default: `'`[`django.db.models.BigAutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.BigAutoField "django.db.models.BigAutoField")`'`

Default primary key field type to use for models that don’t have a field with [`primary_key=True`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.primary_key "django.db.models.Field.primary_key").

Changed in Django 6.0:
In older versions, the default value is [`django.db.models.AutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField").

Migrating auto-created through tables

The value of `DEFAULT_AUTO_FIELD` will be respected when creating new auto-created through tables for many-to-many relationships.

Unfortunately, the primary keys of existing auto-created through tables cannot currently be updated by the migrations framework.

This means that if you switch the value of `DEFAULT_AUTO_FIELD` and then generate migrations, the primary keys of the related models will be updated, as will the foreign keys from the through table, but the primary key of the auto-created through table will not be migrated.

In order to address this, you should add a [`RunSQL`](https://docs.djangoproject.com/en/6.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "django.db.migrations.operations.RunSQL") operation to your migrations to perform the required `ALTER TABLE` step. You can check the existing table name through `sqlmigrate`, `dbshell`, or with the field’s `remote_field.through._meta.db_table` property.

Explicitly defined through models are already handled by the migrations system.

Allowing automatic migrations for the primary key of existing auto-created through tables [may be implemented at a later date](https://code.djangoproject.com/ticket/32674).

### `DEFAULT_CHARSET`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#default-charset "Link to this heading")

Default: `'utf-8'`

Default charset to use for all `HttpResponse` objects, if a MIME type isn’t manually specified. Used when constructing the `Content-Type` header.

### `DEFAULT_EXCEPTION_REPORTER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#default-exception-reporter "Link to this heading")

Default: `'`[`django.views.debug.ExceptionReporter`](https://docs.djangoproject.com/en/6.0/howto/error-reporting/#django.views.debug.ExceptionReporter "django.views.debug.ExceptionReporter")`'`

Default exception reporter class to be used if none has been assigned to the [`HttpRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") instance yet. See [Custom error reports](https://docs.djangoproject.com/en/6.0/howto/error-reporting/#custom-error-reports).

### `DEFAULT_EXCEPTION_REPORTER_FILTER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#default-exception-reporter-filter "Link to this heading")

Default: `'`[`django.views.debug.SafeExceptionReporterFilter`](https://docs.djangoproject.com/en/6.0/howto/error-reporting/#django.views.debug.SafeExceptionReporterFilter "django.views.debug.SafeExceptionReporterFilter")`'`

Default exception reporter filter class to be used if none has been assigned to the [`HttpRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") instance yet. See [Filtering error reports](https://docs.djangoproject.com/en/6.0/howto/error-reporting/#filtering-error-reports).

### `DEFAULT_FROM_EMAIL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#default-from-email "Link to this heading")

Default: `'webmaster@localhost'`

Default email address for automated correspondence from the site manager(s). This address is used in the `From:` header of outgoing emails and can take any format valid in the chosen email sending protocol.

This doesn’t affect error messages sent to [`ADMINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ADMINS) and [`MANAGERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MANAGERS). See [`SERVER_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SERVER_EMAIL) for that.

### `DEFAULT_INDEX_TABLESPACE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#default-index-tablespace "Link to this heading")

Default: `''` (Empty string)

Default tablespace to use for indexes on fields that don’t specify one, if the backend supports it (see [Tablespaces](https://docs.djangoproject.com/en/6.0/topics/db/tablespaces/)).

### `DEFAULT_TABLESPACE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#default-tablespace "Link to this heading")

Default: `''` (Empty string)

Default tablespace to use for models that don’t specify one, if the backend supports it (see [Tablespaces](https://docs.djangoproject.com/en/6.0/topics/db/tablespaces/)).

### `DISALLOWED_USER_AGENTS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#disallowed-user-agents "Link to this heading")

Default: `[]` (Empty list)

List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page, systemwide. Use this for bots/crawlers. This is only used if `CommonMiddleware` is installed (see [Middleware](https://docs.djangoproject.com/en/6.0/topics/http/middleware/)).

### `EMAIL_BACKEND`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-backend "Link to this heading")

Default: `'`[`django.core.mail.backends.smtp.EmailBackend`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.backends.smtp.EmailBackend "django.core.mail.backends.smtp.EmailBackend")`'`

The backend to use for sending emails. For the list of available backends see [Email backends](https://docs.djangoproject.com/en/6.0/topics/email/#topic-email-backends).

### `EMAIL_FILE_PATH`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-file-path "Link to this heading")

Default: Not defined

The directory used by the [file email backend](https://docs.djangoproject.com/en/6.0/topics/email/#topic-email-file-backend) to store output files.

### `EMAIL_HOST`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-host "Link to this heading")

Default: `'localhost'`

The host to use for sending email.

See also [`EMAIL_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_PORT).

### `EMAIL_HOST_PASSWORD`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-host-password "Link to this heading")

Default: `''` (Empty string)

Password to use for the SMTP server defined in [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST). This setting is used in conjunction with [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_USER) when authenticating to the SMTP server. If either of these settings is empty, Django won’t attempt authentication.

See also [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_USER).

### `EMAIL_HOST_USER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-host-user "Link to this heading")

Default: `''` (Empty string)

Username to use for the SMTP server defined in [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST). If empty, Django won’t attempt authentication.

See also [`EMAIL_HOST_PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_PASSWORD).

### `EMAIL_PORT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-port "Link to this heading")

Default: `25`

Port to use for the SMTP server defined in [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST).

### `EMAIL_SUBJECT_PREFIX`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-subject-prefix "Link to this heading")

Default: `'[Django] '`

Subject-line prefix for email messages sent with `django.core.mail.mail_admins` or `django.core.mail.mail_managers`. You’ll probably want to include the trailing space.

### `EMAIL_USE_LOCALTIME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-use-localtime "Link to this heading")

Default: `False`

Whether to send the SMTP `Date` header of email messages in the local time zone (`True`) or in UTC (`False`).

### `EMAIL_USE_TLS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-use-tls "Link to this heading")

Default: `False`

Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587. If you are experiencing hanging connections, see the implicit TLS setting [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_SSL).

### `EMAIL_USE_SSL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-use-ssl "Link to this heading")

Default: `False`

Whether to use an implicit TLS (secure) connection when talking to the SMTP server. In most email documentation this type of TLS connection is referred to as SSL. It is generally used on port 465. If you are experiencing problems, see the explicit TLS setting [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_TLS).

Note that [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_TLS)/[`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_SSL) are mutually exclusive, so only set one of those settings to `True`.

### `EMAIL_SSL_CERTFILE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-ssl-certfile "Link to this heading")

Default: `None`

If [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_SSL) or [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_TLS) is `True` and the secure connection to the SMTP server requires client authentication, use this setting to specify the path to a PEM-formatted certificate chain file, which must be used in conjunction with [`EMAIL_SSL_KEYFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_KEYFILE).

`EMAIL_SSL_CERTFILE` should not be used with a self-signed server certificate or a certificate from a private certificate authority (CA). In such cases, the server’s certificate (or the root certificate of the private CA) should be installed into the system’s CA bundle. This can be done by following platform-specific instructions for installing a root CA certificate, or by using OpenSSL’s `SSL_CERT_FILE` or `SSL_CERT_DIR` environment variables to specify a custom certificate bundle (if modifying the system bundle is not possible or desired).

For more complex scenarios, the SMTP [`EmailBackend`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.backends.smtp.EmailBackend "django.core.mail.backends.smtp.EmailBackend") can be subclassed to add root certificates to its `ssl_context` using [`ssl.SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "(in Python v3.14)").

### `EMAIL_SSL_KEYFILE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-ssl-keyfile "Link to this heading")

Default: `None`

If [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_SSL) or [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_TLS) is `True`, you can optionally specify the path to a PEM-formatted private key file for client authentication of the SSL connection along with [`EMAIL_SSL_CERTFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_CERTFILE).

Note that setting [`EMAIL_SSL_CERTFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_CERTFILE) and [`EMAIL_SSL_KEYFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_KEYFILE) doesn’t result in any certificate checking. They’re passed to the underlying SSL connection. Please refer to the documentation of Python’s [`ssl.SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "(in Python v3.14)") function for details on how the certificate chain file and private key file are handled.

### `EMAIL_TIMEOUT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email-timeout "Link to this heading")

Default: `None`

Specifies a timeout in seconds for blocking operations like the connection attempt.

### `FILE_UPLOAD_HANDLERS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-handlers "Link to this heading")

Default:

[
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

A list of handlers to use for uploading. Changing this setting allows complete customization – even replacement – of Django’s upload process.

See [Managing files](https://docs.djangoproject.com/en/6.0/topics/files/) for details.

### `FILE_UPLOAD_MAX_MEMORY_SIZE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-max-memory-size "Link to this heading")

Default: `2621440` (i.e. 2.5 MB).

The maximum size (in bytes) that an upload will be before it gets streamed to the file system. See [Managing files](https://docs.djangoproject.com/en/6.0/topics/files/) for details.

See also [`DATA_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATA_UPLOAD_MAX_MEMORY_SIZE).

### `FILE_UPLOAD_DIRECTORY_PERMISSIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-directory-permissions "Link to this heading")

Default: `None`

The numeric mode to apply to directories created in the process of uploading files.

This setting also determines the default permissions for collected static directories when using the [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command. See [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) for details on overriding it.

This value mirrors the functionality and caveats of the [`FILE_UPLOAD_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_PERMISSIONS) setting.

### `FILE_UPLOAD_PERMISSIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-permissions "Link to this heading")

Default: `0o644`

The numeric mode (i.e. `0o644`) to set newly uploaded files to. For more information about what these modes mean, see the documentation for [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "(in Python v3.14)").

If `None`, you’ll get operating-system dependent behavior. On most platforms, temporary files will have a mode of `0o600`, and files saved from memory will be saved using the system’s standard umask.

For security reasons, these permissions aren’t applied to the temporary files that are stored in [`FILE_UPLOAD_TEMP_DIR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_TEMP_DIR).

This setting also determines the default permissions for collected static files when using the [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command. See [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) for details on overriding it.

Warning

**Always prefix the mode with**`0o`**.**

If you’re not familiar with file modes, please note that the `0o` prefix is very important: it indicates an octal number, which is the way that modes must be specified. If you try to use `644`, you’ll get totally incorrect behavior.

### `FILE_UPLOAD_TEMP_DIR`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-temp-dir "Link to this heading")

Default: `None`

The directory to store data to (typically files larger than [`FILE_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_MAX_MEMORY_SIZE)) temporarily while uploading files. If `None`, Django will use the standard temporary directory for the operating system. For example, this will default to `/tmp` on *nix-style operating systems.

See [Managing files](https://docs.djangoproject.com/en/6.0/topics/files/) for details.

### `FIRST_DAY_OF_WEEK`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#first-day-of-week "Link to this heading")

Default: `0` (Sunday)

A number representing the first day of the week. This is especially useful when displaying a calendar. This value is only used when not using format internationalization, or when a format cannot be found for the current locale.

The value must be an integer from 0 to 6, where 0 means Sunday, 1 means Monday and so on.

### `FIXTURE_DIRS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#fixture-dirs "Link to this heading")

Default: `[]` (Empty list)

List of directories searched for [fixture](https://docs.djangoproject.com/en/6.0/topics/db/fixtures/#fixtures-explanation) files, in addition to the `fixtures` directory of each application, in search order.

Note that these paths should use Unix-style forward slashes, even on Windows.

See [Provide data with fixtures](https://docs.djangoproject.com/en/6.0/howto/initial-data/#initial-data-via-fixtures) and [Fixture loading](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#topics-testing-fixtures).

### `FORCE_SCRIPT_NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#force-script-name "Link to this heading")

Default: `None`

If not `None`, this will be used as the value of the `SCRIPT_NAME` environment variable in any HTTP request. This setting can be used to override the server-provided value of `SCRIPT_NAME`, which may be a rewritten version of the preferred value or not supplied at all. It is also used by [`django.setup()`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.setup "django.setup") to set the URL resolver script prefix outside of the request/response cycle (e.g. in management commands and standalone scripts) to generate correct URLs when `FORCE_SCRIPT_NAME` is provided.

### `FORM_RENDERER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#form-renderer "Link to this heading")

Default: `'`[`django.forms.renderers.DjangoTemplates`](https://docs.djangoproject.com/en/6.0/ref/forms/renderers/#django.forms.renderers.DjangoTemplates "django.forms.renderers.DjangoTemplates")`'`

The class that renders forms and form widgets. It must implement [the low-level render API](https://docs.djangoproject.com/en/6.0/ref/forms/renderers/#low-level-widget-render-api). Included form renderers are:

*   `'`[`django.forms.renderers.DjangoTemplates`](https://docs.djangoproject.com/en/6.0/ref/forms/renderers/#django.forms.renderers.DjangoTemplates "django.forms.renderers.DjangoTemplates")`'`

*   `'`[`django.forms.renderers.Jinja2`](https://docs.djangoproject.com/en/6.0/ref/forms/renderers/#django.forms.renderers.Jinja2 "django.forms.renderers.Jinja2")`'`

*   `'`[`django.forms.renderers.TemplatesSetting`](https://docs.djangoproject.com/en/6.0/ref/forms/renderers/#django.forms.renderers.TemplatesSetting "django.forms.renderers.TemplatesSetting")`'`

### `FORMAT_MODULE_PATH`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#format-module-path "Link to this heading")

Default: `None`

A full Python path to a Python package that contains custom format definitions for project locales. If not `None`, Django will check for a `formats.py` file, under the directory named as the current locale, and will use the formats defined in this file.

The name of the directory containing the format definitions is expected to be named using [locale name](https://docs.djangoproject.com/en/6.0/topics/i18n/#term-locale-name) notation, for example `de`, `pt_BR`, `en_US`, etc.

For example, if [`FORMAT_MODULE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FORMAT_MODULE_PATH) is set to `mysite.formats`, and current language is `en` (English), Django will expect a directory tree like:

mysite/
    formats/
        __init__.py
        en/
            __init__.py
            formats.py

You can also set this setting to a list of Python paths, for example:

FORMAT_MODULE_PATH = [
    "mysite.formats",
    "some_app.formats",
]

When Django searches for a certain format, it will go through all given Python paths until it finds a module that actually defines the given format. This means that formats defined in packages farther up in the list will take precedence over the same formats in packages farther down.

Available formats are:

*   [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT)

*   [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_INPUT_FORMATS)

*   [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_FORMAT),

*   [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_INPUT_FORMATS)

*   [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DECIMAL_SEPARATOR)

*   [`FIRST_DAY_OF_WEEK`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FIRST_DAY_OF_WEEK)

*   [`MONTH_DAY_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MONTH_DAY_FORMAT)

*   [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NUMBER_GROUPING)

*   [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATE_FORMAT)

*   [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATETIME_FORMAT)

*   [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-THOUSAND_SEPARATOR)

*   [`TIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_FORMAT)

*   [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_INPUT_FORMATS)

*   [`YEAR_MONTH_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-YEAR_MONTH_FORMAT)

### `IGNORABLE_404_URLS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#ignorable-404-urls "Link to this heading")

Default: `[]` (Empty list)

List of compiled regular expression objects describing URLs that should be ignored when reporting HTTP 404 errors via email (see [How to manage error reporting](https://docs.djangoproject.com/en/6.0/howto/error-reporting/)). Regular expressions are matched against [`request's full paths`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.get_full_path "django.http.HttpRequest.get_full_path") (including query string, if any). Use this if your site does not provide a commonly requested file such as `favicon.ico` or `robots.txt`.

This is only used if [`BrokenLinkEmailsMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.common.BrokenLinkEmailsMiddleware "django.middleware.common.BrokenLinkEmailsMiddleware") is enabled (see [Middleware](https://docs.djangoproject.com/en/6.0/topics/http/middleware/)).

### `INSTALLED_APPS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#installed-apps "Link to this heading")

Default: `[]` (Empty list)

A list of strings designating all applications that are enabled in this Django installation. Each string should be a dotted Python path to:

*   an application configuration class (preferred), or

*   a package containing an application.

[Learn more about application configurations](https://docs.djangoproject.com/en/6.0/ref/applications/).

Use the application registry for introspection

Your code should never access [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) directly. Use [`django.apps.apps`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.apps "django.apps.apps") instead.

Application names and labels must be unique in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS)

Application [`names`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.AppConfig.name "django.apps.AppConfig.name") — the dotted Python path to the application package — must be unique. There is no way to include the same application twice, short of duplicating its code under another name.

Application [`labels`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.AppConfig.label "django.apps.AppConfig.label") — by default the final part of the name — must be unique too. For example, you can’t include both `django.contrib.auth` and `myproject.auth`. However, you can relabel an application with a custom configuration that defines a different [`label`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.AppConfig.label "django.apps.AppConfig.label").

These rules apply regardless of whether [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) references application configuration classes or application packages.

When several applications provide different versions of the same resource (template, static file, management command, translation), the application listed first in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) has precedence.

### `INTERNAL_IPS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#internal-ips "Link to this heading")

Default: `[]` (Empty list)

A list of IP addresses, as strings, that:

*   Allow the [`debug()`](https://docs.djangoproject.com/en/6.0/ref/templates/api/#django.template.context_processors.debug "django.template.context_processors.debug") context processor to add some variables to the template context.

*   Can use the [admindocs bookmarklets](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/admindocs/#admindocs-bookmarklets) even if not logged in as a staff user.

*   Are marked as “internal” (as opposed to “EXTERNAL”) in [`AdminEmailHandler`](https://docs.djangoproject.com/en/6.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") emails.

### `LANGUAGE_CODE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-code "Link to this heading")

Default: `'en-us'`

A string representing the language code for this installation. This should be in standard [language ID format](https://docs.djangoproject.com/en/6.0/topics/i18n/#term-language-code). For example, U.S. English is `"en-us"`. See also the [list of language identifiers](http://www.i18nguy.com/unicode/language-identifiers.html) and [Internationalization and localization](https://docs.djangoproject.com/en/6.0/topics/i18n/).

It serves three purposes:

*   If the locale middleware isn’t in use, it decides which translation is served to all users.

*   If the locale middleware is active, it provides a fallback language in case the user’s preferred language can’t be determined or is not supported by the website. It also provides the fallback translation when a translation for a given literal doesn’t exist for the user’s preferred language.

*   If localization is explicitly disabled via the [`unlocalize`](https://docs.djangoproject.com/en/6.0/topics/i18n/formatting/#std-templatefilter-unlocalize) filter or the [`{% localize off %}`](https://docs.djangoproject.com/en/6.0/topics/i18n/formatting/#std-templatetag-localize) tag, it provides fallback localization formats which will be applied instead. See [controlling localization in templates](https://docs.djangoproject.com/en/6.0/topics/i18n/formatting/#topic-l10n-templates) for details.

See [How Django discovers language preference](https://docs.djangoproject.com/en/6.0/topics/i18n/translation/#how-django-discovers-language-preference) for more details.

### `LANGUAGE_COOKIE_AGE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-age "Link to this heading")

Default: `None` (expires at browser close)

The age of the language cookie, in seconds.

### `LANGUAGE_COOKIE_DOMAIN`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-domain "Link to this heading")

Default: `None`

The domain to use for the language cookie. Set this to a string such as `"example.com"` for cross-domain cookies, or use `None` for a standard domain cookie.

Be cautious when updating this setting on a production site. If you update this setting to enable cross-domain cookies on a site that previously used standard domain cookies, existing user cookies that have the old domain will not be updated. This will result in site users being unable to switch the language as long as these cookies persist. The only safe and reliable option to perform the switch is to change the language cookie name permanently (via the [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_NAME) setting) and to add a middleware that copies the value from the old cookie to a new one and then deletes the old one.

### `LANGUAGE_COOKIE_HTTPONLY`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-httponly "Link to this heading")

Default: `False`

Whether to use `HttpOnly` flag on the language cookie. If this is set to `True`, client-side JavaScript will not be able to access the language cookie.

See [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) for details on `HttpOnly`.

### `LANGUAGE_COOKIE_NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-name "Link to this heading")

Default: `'django_language'`

The name of the cookie to use for the language cookie. This can be whatever you want (as long as it’s different from the other cookie names in your application). See [Internationalization and localization](https://docs.djangoproject.com/en/6.0/topics/i18n/).

### `LANGUAGE_COOKIE_PATH`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-path "Link to this heading")

Default: `'/'`

The path set on the language cookie. This should either match the URL path of your Django installation or be a parent of that path.

This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths and each instance will only see its own language cookie.

Be cautious when updating this setting on a production site. If you update this setting to use a deeper path than it previously used, existing user cookies that have the old path will not be updated. This will result in site users being unable to switch the language as long as these cookies persist. The only safe and reliable option to perform the switch is to change the language cookie name permanently (via the [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_NAME) setting), and to add a middleware that copies the value from the old cookie to a new one and then deletes the one.

### `LANGUAGE_COOKIE_SAMESITE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-samesite "Link to this heading")

Default: `None`

The value of the [SameSite](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#samesitesamesite-value) flag on the language cookie. This flag prevents the cookie from being sent in cross-site requests.

See [`SESSION_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SESSION_COOKIE_SAMESITE) for details about `SameSite`.

### `LANGUAGE_COOKIE_SECURE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-secure "Link to this heading")

Default: `False`

Whether to use a secure cookie for the language cookie. If this is set to `True`, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent under an HTTPS connection.

### `LANGUAGES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#languages "Link to this heading")

Default: A list of all available languages. This list is continually growing and including a copy here would inevitably become rapidly out of date. You can see the current list of translated languages by looking in [django/conf/global_settings.py](https://github.com/django/django/blob/main/django/conf/global_settings.py).

The list is a list of 2-tuples in the format ([language code](https://docs.djangoproject.com/en/6.0/topics/i18n/#term-language-code), `language name`) – for example, `('ja', 'Japanese')`. This specifies which languages are available for language selection. See [Internationalization and localization](https://docs.djangoproject.com/en/6.0/topics/i18n/).

Generally, the default value should suffice. Only set this setting if you want to restrict language selection to a subset of the Django-provided languages.

If you define a custom [`LANGUAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGES) setting, you can mark the language names as translation strings using the [`gettext_lazy()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.translation.gettext_lazy "django.utils.translation.gettext_lazy") function.

Here’s a sample settings file:

from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
]

### `LANGUAGES_BIDI`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#languages-bidi "Link to this heading")

Default: A list of all language codes that are written right-to-left. You can see the current list of these languages by looking in [django/conf/global_settings.py](https://github.com/django/django/blob/main/django/conf/global_settings.py).

The list contains [language codes](https://docs.djangoproject.com/en/6.0/topics/i18n/#term-language-code) for languages that are written right-to-left.

Generally, the default value should suffice. Only set this setting if you want to restrict language selection to a subset of the Django-provided languages. If you define a custom [`LANGUAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGES) setting, the list of bidirectional languages may contain language codes which are not enabled on a given site.

### `LOCALE_PATHS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#locale-paths "Link to this heading")

Default: `[]` (Empty list)

A list of directories where Django looks for translation files. See [How Django discovers translations](https://docs.djangoproject.com/en/6.0/topics/i18n/translation/#how-django-discovers-translations).

Example:

LOCALE_PATHS = [
    "/home/www/project/common_files/locale",
    "/var/local/translations/locale",
]

Django will look within each of these paths for the `<locale_code>/LC_MESSAGES` directories containing the actual translation files.

### `LOGGING`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#logging "Link to this heading")

Default: A logging configuration dictionary.

A data structure containing configuration information. When not-empty, the contents of this data structure will be passed as the argument to the configuration method described in [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LOGGING_CONFIG).

Among other things, the default logging configuration passes HTTP 500 server errors to an email log handler when [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG) is `False`. See also [Configuring logging](https://docs.djangoproject.com/en/6.0/topics/logging/#configuring-logging).

You can see the default logging configuration by looking in [django/utils/log.py](https://github.com/django/django/blob/main/django/utils/log.py).

### `LOGGING_CONFIG`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#logging-config "Link to this heading")

Default: `'logging.config.dictConfig'`

A path to a callable that will be used to configure logging in the Django project. Points at an instance of Python’s [dictConfig](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema "(in Python v3.14)") configuration method by default.

If you set [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LOGGING_CONFIG) to `None`, the logging configuration process will be skipped.

### `MANAGERS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#managers "Link to this heading")

Default: `[]` (Empty list)

A list in the same format as [`ADMINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ADMINS) that specifies who should get broken link notifications when [`BrokenLinkEmailsMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.common.BrokenLinkEmailsMiddleware "django.middleware.common.BrokenLinkEmailsMiddleware") is enabled.

Changed in Django 6.0:
In older versions, required a list of (name, address) tuples.

### `MEDIA_ROOT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#media-root "Link to this heading")

Default: `''` (Empty string)

Absolute filesystem path to the directory that will hold [user-uploaded files](https://docs.djangoproject.com/en/6.0/topics/files/).

Example: `"/var/www/example.com/media/"`

See also [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL).

Warning

[`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) and [`STATIC_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_ROOT) must have different values. Before [`STATIC_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_ROOT) was introduced, it was common to rely or fallback on [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) to also serve static files; however, since this can have serious security implications, there is a validation check to prevent it.

### `MEDIA_URL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#media-url "Link to this heading")

Default: `''` (Empty string)

URL that handles the media served from [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT), used for [managing stored files](https://docs.djangoproject.com/en/6.0/topics/files/). It must end in a slash if set to a non-empty value. You will need to [configure these files to be served](https://docs.djangoproject.com/en/6.0/howto/static-files/#serving-uploaded-files-in-development) in both development and production environments.

If you want to use `{{ MEDIA_URL }}` in your templates, add `'django.template.context_processors.media'` in the `'context_processors'` option of [`TEMPLATES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES).

Example: `"https://media.example.com/"`

Warning

There are security risks if you are accepting uploaded content from untrusted users! See the security guide’s topic on [User-uploaded content](https://docs.djangoproject.com/en/6.0/topics/security/#user-uploaded-content-security) for mitigation details.

Warning

[`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL) and [`STATIC_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_URL) must have different values. See [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) for more details.

Note

If [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL) is a relative path, then it will be prefixed by the server-provided value of `SCRIPT_NAME` (or `/` if not set). This makes it easier to serve a Django application in a subpath without adding an extra configuration to the settings.

### `MIDDLEWARE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#middleware "Link to this heading")

Default: `None`

A list of middleware to use. See [Middleware](https://docs.djangoproject.com/en/6.0/topics/http/middleware/).

### `MIGRATION_MODULES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#migration-modules "Link to this heading")

Default: `{}` (Empty dictionary)

A dictionary specifying the package where migration modules can be found on a per-app basis. The default value of this setting is an empty dictionary, but the default package name for migration modules is `migrations`.

Example:

{"blog": "blog.db_migrations"}

In this case, migrations pertaining to the `blog` app will be contained in the `blog.db_migrations` package.

If you provide the `app_label` argument, [`makemigrations`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-makemigrations) will automatically create the package if it doesn’t already exist.

When you supply `None` as a value for an app, Django will consider the app as an app without migrations regardless of an existing `migrations` submodule. This can be used, for example, in a test settings file to skip migrations while testing (tables will still be created for the apps’ models). To disable migrations for all apps during tests, you can set the [`MIGRATE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_MIGRATE) to `False` instead. If `MIGRATION_MODULES` is used in your general project settings, remember to use the [`migrate --run-syncdb`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#cmdoption-migrate-run-syncdb) option if you want to create tables for the app.

### `MONTH_DAY_FORMAT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#month-day-format "Link to this heading")

Default: `'F j'`

The default formatting to use for date fields on Django admin change-list pages – and, possibly, by other parts of the system – in cases when only the month and day are displayed.

For example, when a Django admin change-list page is being filtered by a date drilldown, the header for a given day displays the day and month. Different locales have different formats. For example, U.S. English would say “January 1,” whereas Spanish might say “1 Enero.”

Note that the corresponding locale-dictated format has higher precedence and will be applied instead.

See [`allowed date format strings`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date). See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT), [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_FORMAT) and [`YEAR_MONTH_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-YEAR_MONTH_FORMAT).

### `NUMBER_GROUPING`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#number-grouping "Link to this heading")

Default: `0`

Number of digits grouped together on the integer part of a number.

Common use is to display a thousand separator. If this setting is `0`, then no grouping will be applied to the number. If this setting is greater than `0`, then [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) will be used as the separator between those groups.

Some locales use non-uniform digit grouping, e.g. `10,00,00,000` in `en_IN`. For this case, you can provide a sequence with the number of digit group sizes to be applied. The first number defines the size of the group preceding the decimal delimiter, and each number that follows defines the size of preceding groups. If the sequence is terminated with `-1`, no further grouping is performed. If the sequence terminates with a `0`, the last group size is used for the remainder of the number.

Example tuple for `en_IN`:

NUMBER_GROUPING = (3, 2, 0)

Note that the locale-dictated format has higher precedence and will be applied instead.

See also [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DECIMAL_SEPARATOR), [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) and [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR).

### `PREPEND_WWW`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#prepend-www "Link to this heading")

Default: `False`

Whether to prepend the “www.” subdomain to URLs that don’t have it. This is only used if [`CommonMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware") is installed (see [Middleware](https://docs.djangoproject.com/en/6.0/topics/http/middleware/)). See also [`APPEND_SLASH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-APPEND_SLASH).

### `ROOT_URLCONF`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#root-urlconf "Link to this heading")

Default: Not defined

A string representing the full Python import path to your root URLconf, for example `"mydjangoapps.urls"`. Can be overridden on a per-request basis by setting the attribute `urlconf` on the incoming `HttpRequest` object. See [How Django processes a request](https://docs.djangoproject.com/en/6.0/topics/http/urls/#how-django-processes-a-request) for details.

### `SECRET_KEY`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secret-key "Link to this heading")

Default: `''` (Empty string)

A secret key for a particular Django installation. This is used to provide [cryptographic signing](https://docs.djangoproject.com/en/6.0/topics/signing/), and should be set to a unique, unpredictable value.

[`django-admin startproject`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) automatically adds a randomly-generated `SECRET_KEY` to each new project.

Uses of the key shouldn’t assume that it’s text or bytes. Every use should go through [`force_str()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.encoding.force_str "django.utils.encoding.force_str") or [`force_bytes()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.encoding.force_bytes "django.utils.encoding.force_bytes") to convert it to the desired type.

Django will refuse to start if [`SECRET_KEY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY) is not set.

Warning

**Keep this value secret.**

Running Django with a known [`SECRET_KEY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY) defeats many of Django’s security protections, and can lead to privilege escalation and remote code execution vulnerabilities.

The secret key is used for:

*   All [sessions](https://docs.djangoproject.com/en/6.0/topics/http/sessions/) if you are using any other session backend than `django.contrib.sessions.backends.cache`, or are using the default [`get_session_auth_hash()`](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash").

*   All [messages](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/) if you are using [`CookieStorage`](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#django.contrib.messages.storage.cookie.CookieStorage "django.contrib.messages.storage.cookie.CookieStorage") or [`FallbackStorage`](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#django.contrib.messages.storage.fallback.FallbackStorage "django.contrib.messages.storage.fallback.FallbackStorage").

*   All [`PasswordResetView`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.views.PasswordResetView "django.contrib.auth.views.PasswordResetView") tokens.

*   Any usage of [cryptographic signing](https://docs.djangoproject.com/en/6.0/topics/signing/), unless a different key is provided.

When a secret key is no longer set as [`SECRET_KEY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY) or contained within [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) all of the above will be invalidated. When rotating your secret key, you should move the old key to [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) temporarily. Secret keys are not used for passwords of users and key rotation will not affect them.

Note

The default `settings.py` file created by [``` django-admin startproject ```](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) creates a unique `SECRET_KEY` for convenience.

### `SECRET_KEY_FALLBACKS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secret-key-fallbacks "Link to this heading")

Default: `[]`

A list of fallback secret keys for a particular Django installation. These are used to allow rotation of the `SECRET_KEY`.

In order to rotate your secret keys, set a new `SECRET_KEY` and move the previous value to the beginning of `SECRET_KEY_FALLBACKS`. Then remove the old values from the end of the `SECRET_KEY_FALLBACKS` when you are ready to expire the sessions, password reset tokens, and so on, that make use of them.

Note

Signing operations are computationally expensive. Having multiple old key values in `SECRET_KEY_FALLBACKS` adds additional overhead to all checks that don’t match an earlier key.

As such, fallback values should be removed after an appropriate period, allowing for key rotation.

Uses of the secret key values shouldn’t assume that they are text or bytes. Every use should go through [`force_str()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.encoding.force_str "django.utils.encoding.force_str") or [`force_bytes()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.encoding.force_bytes "django.utils.encoding.force_bytes") to convert it to the desired type.

### `SECURE_CONTENT_TYPE_NOSNIFF`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-content-type-nosniff "Link to this heading")

Default: `True`

If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [X-Content-Type-Options: nosniff](https://docs.djangoproject.com/en/6.0/ref/middleware/#x-content-type-options) header on all responses that do not already have it.

### `SECURE_CROSS_ORIGIN_OPENER_POLICY`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-cross-origin-opener-policy "Link to this heading")

Default: `'same-origin'`

Unless set to `None`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [Cross-Origin Opener Policy](https://docs.djangoproject.com/en/6.0/ref/middleware/#cross-origin-opener-policy) header on all responses that do not already have it to the value provided.

### `SECURE_CSP`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-csp "Link to this heading")

New in Django 6.0.

Default: `{}`

This setting defines the directives used by the [`ContentSecurityPolicyMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.csp.ContentSecurityPolicyMiddleware "django.middleware.csp.ContentSecurityPolicyMiddleware"), which generates and adds a [Content-Security-Policy](https://docs.djangoproject.com/en/6.0/ref/csp/#csp-overview) (CSP) header to all responses that do not already include one.

The `Content-Security-Policy` header instructs browsers to restrict which resources a page is allowed to load. A properly configured CSP can block content that violates defined rules, helping prevent cross-site scripting (XSS) and other content injection attacks by explicitly declaring trusted sources for content such as scripts, styles, images, fonts, and more.

The setting must be a mapping (typically a dictionary) of directive names to their values. Each key should be a valid CSP directive such as `default-src` or `script-src`. The corresponding value can be a list, tuple, or set of source expressions or URLs to allow for that directive. If a set is used, it will be automatically sorted to ensure consistent output in the generated headers.

This example illustrates the expected structure, using the constants defined in [CSP constants](https://docs.djangoproject.com/en/6.0/ref/csp/#csp-constants):

from django.utils.csp import CSP

SECURE_CSP = {
    "default-src": [CSP.SELF],
    "img-src": ["data:", CSP.SELF, "https://images.example.com"],
    "frame-src": [CSP.NONE],
}

Directives validation

Django’s CSP middleware helps construct and send the appropriate header based on your settings, but it does **not validate** that the directives and values conform to the CSP specification. It is your responsibility to ensure that the configuration is syntactically and semantically correct. Use browser developer tools or external CSP validators during development.

For a list of available directives and their values, refer to the [MDN documentation on CSP directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy#directives).

### `SECURE_CSP_REPORT_ONLY`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-csp-report-only "Link to this heading")

New in Django 6.0.

Default: `{}`

This setting is just like [`SECURE_CSP`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_CSP), but instead of enforcing the policy, it instructs the [`ContentSecurityPolicyMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.csp.ContentSecurityPolicyMiddleware "django.middleware.csp.ContentSecurityPolicyMiddleware") to apply a `Content-Security-Policy-Report-Only` header to responses, which allows browsers to monitor and report policy violations without blocking content. This is useful for testing and refining a policy before enforcement.

Most browsers log CSP violations to the developer console and can optionally send them to a reporting endpoint. To collect these reports, the `report-uri` directive must be defined (see [Policy violation reports](https://docs.djangoproject.com/en/6.0/ref/csp/#csp-reports) for more details).

As noted in the [MDN documentation on Content-Security-Policy-Report-Only](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy-Report-Only), the `report-uri` directive must be specified for reports to be sent; otherwise, the header has no reporting effect (other than logging to the browser’s developer tools console).

Following the example from the [`SECURE_CSP`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_CSP) setting:

from django.utils.csp import CSP

SECURE_CSP_REPORT_ONLY = {
    "default-src": [CSP.SELF],
    "img-src": ["data:", CSP.SELF, "https://images.example.com"],
    "frame-src": [CSP.NONE],
    "report-uri": "/my-site/csp/reports/",
}

### `SECURE_HSTS_INCLUDE_SUBDOMAINS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-hsts-include-subdomains "Link to this heading")

Default: `False`

If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") adds the `includeSubDomains` directive to the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/6.0/ref/middleware/#http-strict-transport-security) header. It has no effect unless [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS) is set to a non-zero value.

Warning

Setting this incorrectly can irreversibly (for the value of [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS)) break your site. Read the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/6.0/ref/middleware/#http-strict-transport-security) documentation first.

### `SECURE_HSTS_PRELOAD`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-hsts-preload "Link to this heading")

Default: `False`

If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") adds the `preload` directive to the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/6.0/ref/middleware/#http-strict-transport-security) header. It has no effect unless [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS) is set to a non-zero value.

### `SECURE_HSTS_SECONDS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-hsts-seconds "Link to this heading")

Default: `0`

If set to a non-zero integer value, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/6.0/ref/middleware/#http-strict-transport-security) header on all responses that do not already have it.

Warning

Setting this incorrectly can irreversibly (for some time) break your site. Read the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/6.0/ref/middleware/#http-strict-transport-security) documentation first.

### `SECURE_PROXY_SSL_HEADER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-proxy-ssl-header "Link to this heading")

Default: `None`

A tuple representing an HTTP header/value combination that signifies a request is secure. This controls the behavior of the request object’s `is_secure()` method.

By default, `is_secure()` determines if a request is secure by confirming that a requested URL uses `https://`. This method is important for Django’s CSRF protection, and it may be used by your own code or third-party apps.

If your Django app is behind a proxy, though, the proxy may be “swallowing” whether the original request uses HTTPS or not. If there is a non-HTTPS connection between the proxy and Django then `is_secure()` would always return `False` – even for requests that were made via HTTPS by the end user. In contrast, if there is an HTTPS connection between the proxy and Django then `is_secure()` would always return `True` – even for requests that were made originally via HTTP.

In this situation, configure your proxy to set a custom HTTP header that tells Django whether the request came in via HTTPS, and set `SECURE_PROXY_SSL_HEADER` so that Django knows what header to look for.

Set a tuple with two elements – the name of the header to look for and the required value. For example:

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

This tells Django to trust the `X-Forwarded-Proto` header that comes from our proxy and that the request is guaranteed to be secure (i.e., it originally came in via HTTPS) when:

*   the header value is `'https'`, or

*   its initial, leftmost value is `'https'` in the case of a comma-separated list of protocols (e.g. `'https,http,http'`).

You should _only_ set this setting if you control your proxy or have some other guarantee that it sets/strips this header appropriately.

Note that the header needs to be in the format as used by `request.META` – all caps and likely starting with `HTTP_`. (Remember, Django automatically adds `'HTTP_'` to the start of x-header names before making the header available in `request.META`.)

Warning

**Modifying this setting can compromise your site’s security. Ensure you fully understand your setup before changing it.**

Make sure ALL of the following are true before setting this (assuming the values from the example above):

*   Your Django app is behind a proxy.

*   Your proxy strips the `X-Forwarded-Proto` header from all incoming requests, even when it contains a comma-separated list of protocols. In other words, if end users include that header in their requests, the proxy will discard it.

*   Your proxy sets the `X-Forwarded-Proto` header and sends it to Django, but only for requests that originally come in via HTTPS.

If any of those are not true, you should keep this setting set to `None` and find another way of determining HTTPS, perhaps via custom middleware.

### `SECURE_REDIRECT_EXEMPT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-redirect-exempt "Link to this heading")

Default: `[]` (Empty list)

If a URL path matches a regular expression in this list, the request will not be redirected to HTTPS. The [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") strips leading slashes from URL paths, so patterns shouldn’t include them, e.g. `SECURE_REDIRECT_EXEMPT = [r'^no-ssl/$', …]`. If [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) is `False`, this setting has no effect.

### `SECURE_REFERRER_POLICY`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-referrer-policy "Link to this heading")

Default: `'same-origin'`

If configured, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [Referrer Policy](https://docs.djangoproject.com/en/6.0/ref/middleware/#referrer-policy) header on all responses that do not already have it to the value provided.

### `SECURE_SSL_HOST`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-ssl-host "Link to this heading")

Default: `None`

If a string (e.g. `secure.example.com`), all SSL redirects will be directed to this host rather than the originally-requested host (e.g. `www.example.com`). If [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) is `False`, this setting has no effect.

### `SECURE_SSL_REDIRECT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-ssl-redirect "Link to this heading")

Default: `False`

If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware")[redirects](https://docs.djangoproject.com/en/6.0/ref/middleware/#ssl-redirect) all non-HTTPS requests to HTTPS (except for those URLs matching a regular expression listed in [`SECURE_REDIRECT_EXEMPT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_REDIRECT_EXEMPT)).

Note

If turning this to `True` causes infinite redirects, it probably means your site is running behind a proxy and can’t tell which requests are secure and which are not. Your proxy likely sets a header to indicate secure requests; you can correct the problem by finding out what that header is and configuring the [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER) setting accordingly.

### `SERIALIZATION_MODULES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#serialization-modules "Link to this heading")

Default: Not defined

A dictionary of modules containing serializer definitions (provided as strings), keyed by a string identifier for that serialization type. For example, to define a YAML serializer, use:

SERIALIZATION_MODULES = {"yaml": "path.to.yaml_serializer"}

### `SERVER_EMAIL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#server-email "Link to this heading")

Default: `'root@localhost'`

The email address that error messages come from, such as those sent to [`ADMINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ADMINS) and [`MANAGERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MANAGERS). This address is used in the `From:` header and can take any format valid in the chosen email sending protocol.

Why are my emails sent from a different address?

This address is used only for error messages. It is _not_ the address that regular email messages sent with [`send_mail()`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") come from; for that, see [`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_FROM_EMAIL).

### `SHORT_DATE_FORMAT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#short-date-format "Link to this heading")

Default: `'m/d/Y'` (e.g. `12/31/2003`)

An available formatting that can be used for displaying date fields on templates. Note that the corresponding locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date).

See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT) and [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATETIME_FORMAT).

### `SHORT_DATETIME_FORMAT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#short-datetime-format "Link to this heading")

Default: `'m/d/Y P'` (e.g. `12/31/2003 4 p.m.`)

An available formatting that can be used for displaying datetime fields on templates. Note that the corresponding locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date).

See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT) and [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATE_FORMAT).

### `SIGNING_BACKEND`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#signing-backend "Link to this heading")

Default: `'django.core.signing.TimestampSigner'`

The backend used for signing cookies and other data.

See also the [Cryptographic signing](https://docs.djangoproject.com/en/6.0/topics/signing/) documentation.

### `SILENCED_SYSTEM_CHECKS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#silenced-system-checks "Link to this heading")

Default: `[]` (Empty list)

A list of identifiers of messages generated by the system check framework (i.e. `["models.W001"]`) that you wish to permanently acknowledge and ignore. Silenced checks will not be output to the console.

See also the [System check framework](https://docs.djangoproject.com/en/6.0/ref/checks/) documentation.

### `STORAGES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#storages "Link to this heading")

Default:

{
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

A dictionary containing the settings for all storages to be used with Django. It is a nested dictionary whose contents map a storage alias to a dictionary containing the options for an individual storage.

Storages can have any alias you choose. However, there are two aliases with special significance:

*   `default` for [managing files](https://docs.djangoproject.com/en/6.0/topics/files/). `'`[`django.core.files.storage.FileSystemStorage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage "django.core.files.storage.FileSystemStorage")`'` is the default storage engine.

*   `staticfiles` for [managing static files](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/). `'`[`django.contrib.staticfiles.storage.StaticFilesStorage`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.StaticFilesStorage "django.contrib.staticfiles.storage.StaticFilesStorage")`'` is the default storage engine.

The following is an example `settings.py` snippet defining a custom file storage called `example`:

STORAGES = {
    # ...
    "example": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": "/example",
            "base_url": "/example/",
        },
    },
}

`OPTIONS` are passed to the `BACKEND` on initialization in `**kwargs`.

A ready-to-use instance of the storage backends can be retrieved from [`django.core.files.storage.storages`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.storages "django.core.files.storage.storages"). Use a key corresponding to the backend definition in [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES).

Is my value merged with the default value?

Defining this setting overrides the default value and is _not_ merged with it.

### `TASKS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#tasks "Link to this heading")

New in Django 6.0.

Default:

{
    "default": {
        "BACKEND": "django.tasks.backends.immediate.ImmediateBackend",
    }
}

A dictionary containing the settings for all Task backends to be used with Django. It is a nested dictionary whose contents maps backend aliases to a dictionary containing the options for each backend.

The [`TASKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TASKS) setting must configure a `default` backend; any number of additional backends may also be specified. Depending on which backend is used, other options may be required. The following options are available as standard.

#### `BACKEND`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TASKS-BACKEND "Link to this heading")

Default: `''` (Empty string)

The Tasks backend to use. The built-in backends are:

*   `'django.tasks.backends.dummy.DummyBackend'`

*   `'django.tasks.backends.immediate.ImmediateBackend'`

You can use a backend that doesn’t ship with Django by setting [`BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TASKS-BACKEND) to a fully-qualified path of a backend class (i.e. `mypackage.backends.whatever.WhateverBackend`).

#### `QUEUES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#queues "Link to this heading")

Default: `["default"]`

Specify the queue names supported by the backend. This can be used to ensure Tasks aren’t enqueued to queues which do not exist.

To disable queue name validation, set to an empty list (`[]`).

#### `OPTIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TASKS-OPTIONS "Link to this heading")

Default: `{}`

Extra parameters to pass to the Task backend. Available parameters vary depending on the Task backend.

### `TEMPLATES`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#templates "Link to this heading")

Default: `[]` (Empty list)

A list containing the settings for all template engines to be used with Django. Each item of the list is a dictionary containing the options for an individual engine.

Here’s a setup that tells the Django template engine to load templates from the `templates` subdirectory inside each installed application:

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

The following options are available for all backends.

#### `BACKEND`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-BACKEND "Link to this heading")

Default: Not defined

The template backend to use. The built-in template backends are:

*   `'django.template.backends.django.DjangoTemplates'`

*   `'django.template.backends.jinja2.Jinja2'`

You can use a template backend that doesn’t ship with Django by setting `BACKEND` to a fully-qualified path (i.e. `'mypackage.whatever.Backend'`).

#### `NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-NAME "Link to this heading")

Default: see below

The alias for this particular template engine. It’s an identifier that allows selecting an engine for rendering. Aliases must be unique across all configured template engines.

It defaults to the name of the module defining the engine class, i.e. the next to last piece of [`BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-BACKEND), when it isn’t provided. For example if the backend is `'mypackage.whatever.Backend'` then its default name is `'whatever'`.

#### `DIRS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#dirs "Link to this heading")

Default: `[]` (Empty list)

Directories where the engine should look for template source files, in search order.

#### `APP_DIRS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#app-dirs "Link to this heading")

Default: `False`

Whether the engine should look for template source files inside installed applications.

Note

The default `settings.py` file created by [``` django-admin startproject ```](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) sets `'APP_DIRS': True`.

#### `OPTIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-OPTIONS "Link to this heading")

Default: `{}` (Empty dict)

Extra parameters to pass to the template backend. Available parameters vary depending on the template backend. See [`DjangoTemplates`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") and [`Jinja2`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.backends.jinja2.Jinja2 "django.template.backends.jinja2.Jinja2") for the options of the built-in backends.

### `TEST_RUNNER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#test-runner "Link to this heading")

Default: `'django.test.runner.DiscoverRunner'`

The name of the class to use for starting the test suite. See [Using different testing frameworks](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/#other-testing-frameworks).

### `TEST_NON_SERIALIZED_APPS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#test-non-serialized-apps "Link to this heading")

Default: `[]` (Empty list)

In order to restore the database state between tests for `TransactionTestCase`s and database backends without transactions, Django will [serialize the contents of all apps](https://docs.djangoproject.com/en/6.0/topics/testing/overview/#test-case-serialized-rollback) when it starts the test run so it can then reload from that copy before running tests that need it.

This slows down the startup time of the test runner; if you have apps that you know don’t need this feature, you can add their full names in here (e.g. `'django.contrib.contenttypes'`) to exclude them from this serialization process.

### `THOUSAND_SEPARATOR`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#thousand-separator "Link to this heading")

Default: `','` (Comma)

Default thousand separator used when formatting numbers. This setting is used only when [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR) is `True` and [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NUMBER_GROUPING) is greater than `0`.

Note that the locale-dictated format has higher precedence and will be applied instead.

See also [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NUMBER_GROUPING), [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DECIMAL_SEPARATOR) and [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR).

### `TIME_FORMAT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#time-format "Link to this heading")

Default: `'P'` (e.g. `4 p.m.`)

The default formatting to use for displaying time fields in any part of the system. Note that the locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date).

See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT) and [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_FORMAT).

### `TIME_INPUT_FORMATS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#time-input-formats "Link to this heading")

Default:

[
    "%H:%M:%S",  # '14:30:59'
    "%H:%M:%S.%f",  # '14:30:59.000200'
    "%H:%M",  # '14:30'
]

A list of formats that will be accepted when inputting data on a time field. Formats will be tried in order, using the first valid one. Note that these format strings use Python’s [datetime module syntax](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior "(in Python v3.14)"), not the format strings from the [`date`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date) template filter.

The locale-dictated format has higher precedence and will be applied instead.

See also [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_INPUT_FORMATS) and [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_INPUT_FORMATS).

### `TIME_ZONE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE "Link to this heading")

Default: `'America/Chicago'`

A string representing the time zone for this installation. See the [list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

Note

Since Django was first released with the [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) set to `'America/Chicago'`, the global setting (used if nothing is defined in your project’s `settings.py`) remains `'America/Chicago'` for backwards compatibility. New project templates default to `'UTC'`.

Note that this isn’t necessarily the time zone of the server. For example, one server may serve multiple Django-powered sites, each with a separate time zone setting.

When [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `False`, this is the time zone in which Django will store all datetimes. When [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, this is the default time zone that Django will use to display datetimes in templates and to interpret datetimes entered in forms.

On Unix environments (where [`time.tzset()`](https://docs.python.org/3/library/time.html#time.tzset "(in Python v3.14)") is implemented), Django sets the `os.environ['TZ']` variable to the time zone you specify in the [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) setting. Thus, all your views and models will automatically operate in this time zone. However, Django won’t set the `TZ` environment variable if you’re using the manual configuration option as described in [manually configuring settings](https://docs.djangoproject.com/en/6.0/topics/settings/#settings-without-django-settings-module). If Django doesn’t set the `TZ` environment variable, it’s up to you to ensure your processes are running in the correct environment.

Note

Django cannot reliably use alternate time zones in a Windows environment. If you’re running Django on Windows, [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) must be set to match the system time zone.

### `USE_I18N`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#use-i18n "Link to this heading")

Default: `True`

A boolean that specifies whether Django’s translation system should be enabled. This provides a way to turn it off, for performance. If this is set to `False`, Django will make some optimizations so as not to load the translation machinery.

See also [`LANGUAGE_CODE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_CODE) and [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ).

Note

The default `settings.py` file created by [``` django-admin startproject ```](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) includes `USE_I18N = True` for convenience.

### `USE_THOUSAND_SEPARATOR`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#use-thousand-separator "Link to this heading")

Default: `False`

A boolean that specifies whether to display numbers using a thousand separator. When set to `True`, Django will format numbers using the [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NUMBER_GROUPING) and [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) settings. The latter two settings may also be dictated by the locale, which takes precedence.

See also [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DECIMAL_SEPARATOR), [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NUMBER_GROUPING) and [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-THOUSAND_SEPARATOR).

### `USE_TZ`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#use-tz "Link to this heading")

Default: `True`

A boolean that specifies if datetimes will be timezone-aware by default or not. If this is set to `True`, Django will use timezone-aware datetimes internally.

When `USE_TZ` is False, Django will use naive datetimes in local time, except when parsing ISO 8601 formatted strings, where timezone information will always be retained if present.

See also [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) and [`USE_I18N`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_I18N).

### `USE_X_FORWARDED_HOST`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#use-x-forwarded-host "Link to this heading")

Default: `False`

A boolean that specifies whether to use the `X-Forwarded-Host` header in preference to the `Host` header. This should only be enabled if a proxy which sets this header is in use.

This setting takes priority over [`USE_X_FORWARDED_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_X_FORWARDED_PORT). Per [**RFC 7239 Section 5.3**](https://datatracker.ietf.org/doc/html/rfc7239.html#section-5.3), the `X-Forwarded-Host` header can include the port number, in which case you shouldn’t use [`USE_X_FORWARDED_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_X_FORWARDED_PORT).

### `USE_X_FORWARDED_PORT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#use-x-forwarded-port "Link to this heading")

Default: `False`

A boolean that specifies whether to use the `X-Forwarded-Port` header in preference to the `SERVER_PORT``META` variable. This should only be enabled if a proxy which sets this header is in use.

[`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST) takes priority over this setting.

### `URLIZE_ASSUME_HTTPS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#urlize-assume-https "Link to this heading")

New in Django 6.0.

Deprecated since version 6.0.

Default: `False`

Set this transitional setting to `True` to opt into using HTTPS as the default protocol when none is provided in URLs processed by the [`urlize`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-urlize) and [`urlizetrunc`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-urlizetrunc) template filters during the Django 6.x release cycle.

### `WSGI_APPLICATION`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#wsgi-application "Link to this heading")

Default: `None`

The full Python path of the WSGI application object that Django’s built-in servers (e.g. [`runserver`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-runserver)) will use. The [``` django-admin startproject ```](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) management command will create a standard `wsgi.py` file with an `application` callable in it, and point this setting to that `application`.

If not set, the return value of `django.core.wsgi.get_wsgi_application()` will be used. In this case, the behavior of [`runserver`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-runserver) will be identical to previous Django versions.

### `YEAR_MONTH_FORMAT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#year-month-format "Link to this heading")

Default: `'F Y'`

The default formatting to use for date fields on Django admin change-list pages – and, possibly, by other parts of the system – in cases when only the year and month are displayed.

For example, when a Django admin change-list page is being filtered by a date drilldown, the header for a given month displays the month and the year. Different locales have different formats. For example, U.S. English would say “January 2006,” whereas another locale might say “2006/January.”

Note that the corresponding locale-dictated format has higher precedence and will be applied instead.

See [`allowed date format strings`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date). See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT), [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_FORMAT) and [`MONTH_DAY_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MONTH_DAY_FORMAT).

### `X_FRAME_OPTIONS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#x-frame-options "Link to this heading")

Default: `'DENY'`

The default value for the X-Frame-Options header used by [`XFrameOptionsMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.clickjacking.XFrameOptionsMiddleware "django.middleware.clickjacking.XFrameOptionsMiddleware"). See the [clickjacking protection](https://docs.djangoproject.com/en/6.0/ref/clickjacking/) documentation.

[Auth](https://docs.djangoproject.com/en/6.0/ref/settings/#id15)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#auth "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

Settings for [`django.contrib.auth`](https://docs.djangoproject.com/en/6.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework.").

### `AUTHENTICATION_BACKENDS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#authentication-backends "Link to this heading")

Default: `['django.contrib.auth.backends.ModelBackend']`

A list of authentication backend classes (as strings) to use when attempting to authenticate a user. See the [authentication backends documentation](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#authentication-backends) for details.

### `AUTH_USER_MODEL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#auth-user-model "Link to this heading")

Default: `'auth.User'`

The model to use to represent a User. See [Substituting a custom User model](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#auth-custom-user).

Warning

You cannot change the AUTH_USER_MODEL setting during the lifetime of a project (i.e. once you have made and migrated models that depend on it) without serious effort. It is intended to be set at the project start, and the model it refers to must be available in the first migration of the app that it lives in. See [Substituting a custom User model](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#auth-custom-user) for more details.

### `LOGIN_REDIRECT_URL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#login-redirect-url "Link to this heading")

Default: `'/accounts/profile/'`

The URL or [named URL pattern](https://docs.djangoproject.com/en/6.0/topics/http/urls/#naming-url-patterns) where requests are redirected after login when the [`LoginView`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.views.LoginView "django.contrib.auth.views.LoginView") doesn’t get a `next` GET parameter.

### `LOGIN_URL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#login-url "Link to this heading")

Default: `'/accounts/login/'`

The URL or [named URL pattern](https://docs.djangoproject.com/en/6.0/topics/http/urls/#naming-url-patterns) where requests are redirected for login when using the [`login_required()`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.decorators.login_required "django.contrib.auth.decorators.login_required") decorator, [`LoginRequiredMixin`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.mixins.LoginRequiredMixin "django.contrib.auth.mixins.LoginRequiredMixin"), [`AccessMixin`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.mixins.AccessMixin "django.contrib.auth.mixins.AccessMixin"), or when [`LoginRequiredMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.contrib.auth.middleware.LoginRequiredMiddleware "django.contrib.auth.middleware.LoginRequiredMiddleware") is installed.

### `LOGOUT_REDIRECT_URL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#logout-redirect-url "Link to this heading")

Default: `None`

The URL or [named URL pattern](https://docs.djangoproject.com/en/6.0/topics/http/urls/#naming-url-patterns) where requests are redirected after logout if [`LogoutView`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.views.LogoutView "django.contrib.auth.views.LogoutView") doesn’t have a `next_page` attribute.

If `None`, no redirect will be performed and the logout view will be rendered.

### `PASSWORD_RESET_TIMEOUT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#password-reset-timeout "Link to this heading")

Default: `259200` (3 days, in seconds)

The number of seconds a password reset link is valid for.

Used by the [`PasswordResetConfirmView`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.views.PasswordResetConfirmView "django.contrib.auth.views.PasswordResetConfirmView").

Note

Reducing the value of this timeout doesn’t make any difference to the ability of an attacker to brute-force a password reset token. Tokens are designed to be safe from brute-forcing without any timeout.

This timeout exists to protect against some unlikely attack scenarios, such as someone gaining access to email archives that may contain old, unused password reset tokens.

### `PASSWORD_HASHERS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#password-hashers "Link to this heading")

See [How Django stores passwords](https://docs.djangoproject.com/en/6.0/topics/auth/passwords/#auth-password-storage).

Default:

[
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

### `AUTH_PASSWORD_VALIDATORS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators "Link to this heading")

Default: `[]` (Empty list)

The list of validators that are used to check the strength of user’s passwords. See [Password validation](https://docs.djangoproject.com/en/6.0/topics/auth/passwords/#password-validation) for more details. By default, no validation is performed and all passwords are accepted.

[Messages](https://docs.djangoproject.com/en/6.0/ref/settings/#id16)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#messages "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Settings for [`django.contrib.messages`](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#module-django.contrib.messages "django.contrib.messages: Provides cookie- and session-based temporary message storage.").

### `MESSAGE_LEVEL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#message-level "Link to this heading")

Default: `messages.INFO`

Sets the minimum message level that will be recorded by the messages framework. See [message levels](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#message-level) for more details.

Avoiding circular imports

If you override `MESSAGE_LEVEL` in your settings file and rely on any of the built-in constants, you must import the constants module directly to avoid the potential for circular imports, e.g.:

from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.DEBUG

If desired, you may specify the numeric values for the constants directly according to the values in the above [constants table](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#message-level-constants).

### `MESSAGE_STORAGE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#message-storage "Link to this heading")

Default: `'django.contrib.messages.storage.fallback.FallbackStorage'`

Controls where Django stores message data. Valid values are:

*   `'django.contrib.messages.storage.fallback.FallbackStorage'`

*   `'django.contrib.messages.storage.session.SessionStorage'`

*   `'django.contrib.messages.storage.cookie.CookieStorage'`

See [message storage backends](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#message-storage-backends) for more details.

The backends that use cookies – [`CookieStorage`](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#django.contrib.messages.storage.cookie.CookieStorage "django.contrib.messages.storage.cookie.CookieStorage") and [`FallbackStorage`](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#django.contrib.messages.storage.fallback.FallbackStorage "django.contrib.messages.storage.fallback.FallbackStorage") – use the value of [`SESSION_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SESSION_COOKIE_DOMAIN), [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SESSION_COOKIE_SECURE) and [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) when setting their cookies.

### `MESSAGE_TAGS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#message-tags "Link to this heading")

Default:

{
    messages.DEBUG: "debug",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "error",
}

This sets the mapping of message level to message tag, which is typically rendered as a CSS class in HTML. If you specify a value, it will extend the default. This means you only have to specify those values which you need to override. See [Displaying messages](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#message-displaying) above for more details.

Avoiding circular imports

If you override `MESSAGE_TAGS` in your settings file and rely on any of the built-in constants, you must import the `constants` module directly to avoid the potential for circular imports, e.g.:

from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {message_constants.INFO: ""}

If desired, you may specify the numeric values for the constants directly according to the values in the above [constants table](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#message-level-constants).

[Sessions](https://docs.djangoproject.com/en/6.0/ref/settings/#id17)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#sessions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Settings for [`django.contrib.sessions`](https://docs.djangoproject.com/en/6.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects.").

### `SESSION_CACHE_ALIAS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cache-alias "Link to this heading")

Default: `'default'`

If you’re using [cache-based session storage](https://docs.djangoproject.com/en/6.0/topics/http/sessions/#cached-sessions-backend), this selects the cache to use.

### `SESSION_COOKIE_AGE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-age "Link to this heading")

Default: `1209600` (2 weeks, in seconds)

The age of session cookies, in seconds.

### `SESSION_COOKIE_DOMAIN`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-domain "Link to this heading")

Default: `None`

The domain to use for session cookies. Set this to a string such as `"example.com"` for cross-domain cookies, or use `None` for a standard domain cookie.

To use cross-domain cookies with [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_USE_SESSIONS), you must include a leading dot (e.g. `".example.com"`) to accommodate the CSRF middleware’s referer checking.

Be cautious when updating this setting on a production site. If you update this setting to enable cross-domain cookies on a site that previously used standard domain cookies, existing user cookies will be set to the old domain. This may result in them being unable to log in as long as these cookies persist.

This setting also affects cookies set by [`django.contrib.messages`](https://docs.djangoproject.com/en/6.0/ref/contrib/messages/#module-django.contrib.messages "django.contrib.messages: Provides cookie- and session-based temporary message storage.").

### `SESSION_COOKIE_HTTPONLY`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-httponly "Link to this heading")

Default: `True`

Whether to use `HttpOnly` flag on the session cookie. If this is set to `True`, client-side JavaScript will not be able to access the session cookie.

[HttpOnly](https://owasp.org/www-community/HttpOnly) is a flag included in a Set-Cookie HTTP response header. It’s part of the [**RFC 6265 Section 4.1.2.6**](https://datatracker.ietf.org/doc/html/rfc6265.html#section-4.1.2.6) standard for cookies and can be a useful way to mitigate the risk of a client-side script accessing the protected cookie data.

This makes it less trivial for an attacker to escalate a cross-site scripting vulnerability into full hijacking of a user’s session. There aren’t many good reasons for turning this off. Your code shouldn’t read session cookies from JavaScript.

### `SESSION_COOKIE_NAME`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-name "Link to this heading")

Default: `'sessionid'`

The name of the cookie to use for sessions. This can be whatever you want (as long as it’s different from the other cookie names in your application).

### `SESSION_COOKIE_PATH`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-path "Link to this heading")

Default: `'/'`

The path set on the session cookie. This should either match the URL path of your Django installation or be parent of that path.

This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths, and each instance will only see its own session cookie.

### `SESSION_COOKIE_SAMESITE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-samesite "Link to this heading")

Default: `'Lax'`

The value of the [SameSite](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#samesitesamesite-value) flag on the session cookie. This flag prevents the cookie from being sent in cross-site requests thus preventing CSRF attacks and making some methods of stealing session cookie impossible.

Possible values for the setting are:

*   `'Strict'`: prevents the cookie from being sent by the browser to the target site in all cross-site browsing context, even when following a regular link.

For example, for a GitHub-like website this would mean that if a logged-in user follows a link to a private GitHub project posted on a corporate discussion forum or email, GitHub will not receive the session cookie and the user won’t be able to access the project. A bank website, however, most likely doesn’t want to allow any transactional pages to be linked from external sites so the `'Strict'` flag would be appropriate.

*   `'Lax'` (default): provides a balance between security and usability for websites that want to maintain user’s logged-in session after the user arrives from an external link.

In the GitHub scenario, the session cookie would be allowed when following a regular link from an external website and be blocked in CSRF-prone request methods (e.g. `POST`).

*   `'None'` (string): the session cookie will be sent with all same-site and cross-site requests.

*   `False`: disables the flag.

Note

Modern browsers provide a more secure default policy for the `SameSite` flag and will assume `Lax` for cookies without an explicit value set.

### `SESSION_COOKIE_SECURE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-secure "Link to this heading")

Default: `False`

Whether to use a secure cookie for the session cookie. If this is set to `True`, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent under an HTTPS connection.

Leaving this setting off isn’t a good idea because an attacker could capture an unencrypted session cookie with a packet sniffer and use the cookie to hijack the user’s session.

### `SESSION_ENGINE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-engine "Link to this heading")

Default: `'django.contrib.sessions.backends.db'`

Controls where Django stores session data. Included engines are:

*   `'django.contrib.sessions.backends.db'`

*   `'django.contrib.sessions.backends.file'`

*   `'django.contrib.sessions.backends.cache'`

*   `'django.contrib.sessions.backends.cached_db'`

*   `'django.contrib.sessions.backends.signed_cookies'`

See [Configuring the session engine](https://docs.djangoproject.com/en/6.0/topics/http/sessions/#configuring-sessions) for more details.

### `SESSION_EXPIRE_AT_BROWSER_CLOSE`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-expire-at-browser-close "Link to this heading")

Default: `False`

Whether to expire the session when the user closes their browser. See [Browser-length sessions vs. persistent sessions](https://docs.djangoproject.com/en/6.0/topics/http/sessions/#browser-length-vs-persistent-sessions).

### `SESSION_FILE_PATH`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-file-path "Link to this heading")

Default: `None`

If you’re using file-based session storage, this sets the directory in which Django will store session data. When the default value (`None`) is used, Django will use the standard temporary directory for the system.

### `SESSION_SAVE_EVERY_REQUEST`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-save-every-request "Link to this heading")

Default: `False`

Whether to save the session data on every request. If this is `False` (default), then the session data will only be saved if it has been modified – that is, if any of its dictionary values have been assigned or deleted. Empty sessions won’t be created, even if this setting is active.

### `SESSION_SERIALIZER`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#session-serializer "Link to this heading")

Default: `'django.contrib.sessions.serializers.JSONSerializer'`

Full import path of a serializer class to use for serializing session data. Included serializer is:

*   `'django.contrib.sessions.serializers.JSONSerializer'`

See [Session serialization](https://docs.djangoproject.com/en/6.0/topics/http/sessions/#session-serialization) for details.

[Sites](https://docs.djangoproject.com/en/6.0/ref/settings/#id18)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#sites "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

Settings for [`django.contrib.sites`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#module-django.contrib.sites "django.contrib.sites: Lets you operate multiple websites from the same database and Django project").

### `SITE_ID`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#site-id "Link to this heading")

Default: Not defined

The ID, as an integer, of the current site in the `django_site` database table. This is used so that application data can hook into specific sites and a single database can manage content for multiple sites.

[Static Files](https://docs.djangoproject.com/en/6.0/ref/settings/#id19)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#static-files "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Settings for [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.").

### `STATIC_ROOT`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#static-root "Link to this heading")

Default: `None`

The absolute path to the directory where [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) will collect static files for deployment.

Example: `"/var/www/example.com/static/"`

If the [staticfiles](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/) contrib app is enabled (as in the default project template), the [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command will collect static files into this directory. See the how-to on [managing static files](https://docs.djangoproject.com/en/6.0/howto/static-files/) for more details about usage.

Warning

This should be an initially empty destination directory for collecting your static files from their permanent locations into one directory for ease of deployment; it is **not** a place to store your static files permanently. You should do that in directories that will be found by [staticfiles](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/)’s [`finders`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATICFILES_FINDERS), which by default, are `'static/'` app sub-directories and any directories you include in [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATICFILES_DIRS)).

### `STATIC_URL`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#static-url "Link to this heading")

Default: `None`

URL to use when referring to static files located in [`STATIC_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_ROOT).

Example: `"static/"` or `"https://static.example.com/"`

If not `None`, this will be used as the base path for [asset definitions](https://docs.djangoproject.com/en/6.0/topics/forms/media/#form-asset-paths) (the `Media` class) and the [staticfiles app](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/).

It must end in a slash if set to a non-empty value.

You may need to [configure these files to be served in development](https://docs.djangoproject.com/en/6.0/howto/static-files/#serving-static-files-in-development) and will definitely need to do so [in production](https://docs.djangoproject.com/en/6.0/howto/static-files/deployment/).

Note

If [`STATIC_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_URL) is a relative path, then it will be prefixed by the server-provided value of `SCRIPT_NAME` (or `/` if not set). This makes it easier to serve a Django application in a subpath without adding an extra configuration to the settings.

### `STATICFILES_DIRS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#staticfiles-dirs "Link to this heading")

Default: `[]` (Empty list)

This setting defines the additional locations the staticfiles app will traverse if the `FileSystemFinder` finder is enabled, e.g. if you use the [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) or [`findstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-findstatic) management command or use the static file serving view.

This should be set to a list of strings that contain full paths to your additional files directory(ies) e.g.:

STATICFILES_DIRS = [
    "/home/special.polls.com/polls/static",
    "/home/polls.com/polls/static",
    "/opt/webfiles/common",
]

Note that these paths should use Unix-style forward slashes, even on Windows (e.g. `"C:/Users/user/mysite/extra_static_content"`).

#### Prefixes (optional)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#prefixes-optional "Link to this heading")

In case you want to refer to files in one of the locations with an additional namespace, you can **optionally** provide a prefix as `(prefix, path)` tuples, e.g.:

STATICFILES_DIRS = [
    # ...
    ("downloads", "/opt/webfiles/stats"),
]

For example, assuming you have [`STATIC_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_URL) set to `'static/'`, the [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command would collect the “stats” files in a `'downloads'` subdirectory of [`STATIC_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATIC_ROOT).

This would allow you to refer to the local file `'/opt/webfiles/stats/polls_20101022.tar.gz'` with `'/static/downloads/polls_20101022.tar.gz'` in your templates, e.g.:

<a href="{% static 'downloads/polls_20101022.tar.gz' %}">

### `STATICFILES_FINDERS`[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#staticfiles-finders "Link to this heading")

Default:

[
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

The list of finder backends that know how to find static files in various locations.

The default will find files stored in the [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATICFILES_DIRS) setting (using `django.contrib.staticfiles.finders.FileSystemFinder`) and in a `static` subdirectory of each app (using `django.contrib.staticfiles.finders.AppDirectoriesFinder`). If multiple files with the same name are present, the first file that is found will be used.

One finder is disabled by default: `django.contrib.staticfiles.finders.DefaultStorageFinder`. If added to your [`STATICFILES_FINDERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STATICFILES_FINDERS) setting, it will look for static files in the default file storage as defined by the `default` key in the [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES) setting.

Note

When using the `AppDirectoriesFinder` finder, make sure your apps can be found by staticfiles by adding the app to the [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) setting of your site.

Static file finders are currently considered a private interface, and this interface is thus undocumented.

[Core Settings Topical Index](https://docs.djangoproject.com/en/6.0/ref/settings/#id20)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#core-settings-topical-index "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Cache[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#cache "Link to this heading")

*   [`CACHES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHES)

*   [`CACHE_MIDDLEWARE_ALIAS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_ALIAS)

*   [`CACHE_MIDDLEWARE_KEY_PREFIX`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_KEY_PREFIX)

*   [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS)

### Database[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#database "Link to this heading")

*   [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES)

*   [`DATABASE_ROUTERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE_ROUTERS)

*   [`DEFAULT_INDEX_TABLESPACE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_INDEX_TABLESPACE)

*   [`DEFAULT_TABLESPACE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_TABLESPACE)

### Debugging[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#debugging "Link to this heading")

*   [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG)

*   [`DEBUG_PROPAGATE_EXCEPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEBUG_PROPAGATE_EXCEPTIONS)

### Email[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#email "Link to this heading")

*   [`ADMINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ADMINS)

*   [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_CHARSET)

*   [`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_FROM_EMAIL)

*   [`EMAIL_BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_BACKEND)

*   [`EMAIL_FILE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_FILE_PATH)

*   [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST)

*   [`EMAIL_HOST_PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_PASSWORD)

*   [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_HOST_USER)

*   [`EMAIL_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_PORT)

*   [`EMAIL_SSL_CERTFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_CERTFILE)

*   [`EMAIL_SSL_KEYFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SSL_KEYFILE)

*   [`EMAIL_SUBJECT_PREFIX`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_SUBJECT_PREFIX)

*   [`EMAIL_TIMEOUT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_TIMEOUT)

*   [`EMAIL_USE_LOCALTIME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_LOCALTIME)

*   [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_SSL)

*   [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-EMAIL_USE_TLS)

*   [`MANAGERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MANAGERS)

*   [`SERVER_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SERVER_EMAIL)

### Error reporting[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#error-reporting "Link to this heading")

*   [`DEFAULT_EXCEPTION_REPORTER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_EXCEPTION_REPORTER)

*   [`DEFAULT_EXCEPTION_REPORTER_FILTER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_EXCEPTION_REPORTER_FILTER)

*   [`IGNORABLE_404_URLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-IGNORABLE_404_URLS)

*   [`MANAGERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MANAGERS)

*   [`SILENCED_SYSTEM_CHECKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SILENCED_SYSTEM_CHECKS)

### File uploads[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#file-uploads "Link to this heading")

*   [`FILE_UPLOAD_HANDLERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_HANDLERS)

*   [`FILE_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_MAX_MEMORY_SIZE)

*   [`FILE_UPLOAD_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_PERMISSIONS)

*   [`FILE_UPLOAD_TEMP_DIR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FILE_UPLOAD_TEMP_DIR)

*   [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT)

*   [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL)

*   [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-STORAGES)

### Forms[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#forms "Link to this heading")

*   [`FORM_RENDERER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FORM_RENDERER)

### Globalization (`i18n`/`l10n`)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#globalization-i18n-l10n "Link to this heading")

#### Internationalization (`i18n`)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#internationalization-i18n "Link to this heading")

*   [`FIRST_DAY_OF_WEEK`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FIRST_DAY_OF_WEEK)

*   [`FORMAT_MODULE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FORMAT_MODULE_PATH)

*   [`LANGUAGE_COOKIE_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_AGE)

*   [`LANGUAGE_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_DOMAIN)

*   [`LANGUAGE_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_HTTPONLY)

*   [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_NAME)

*   [`LANGUAGE_COOKIE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_PATH)

*   [`LANGUAGE_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_SAMESITE)

*   [`LANGUAGE_COOKIE_SECURE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_SECURE)

*   [`LANGUAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGES)

*   [`LANGUAGES_BIDI`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGES_BIDI)

*   [`LOCALE_PATHS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LOCALE_PATHS)

*   [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE)

*   [`USE_I18N`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_I18N)

*   [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ)

#### Localization (`l10n`)[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#localization-l10n "Link to this heading")

*   [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_FORMAT)

*   [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATE_INPUT_FORMATS)

*   [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_FORMAT)

*   [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATETIME_INPUT_FORMATS)

*   [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DECIMAL_SEPARATOR)

*   [`LANGUAGE_CODE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_CODE)

*   [`MONTH_DAY_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MONTH_DAY_FORMAT)

*   [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NUMBER_GROUPING)

*   [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATE_FORMAT)

*   [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SHORT_DATETIME_FORMAT)

*   [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-THOUSAND_SEPARATOR)

*   [`TIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_FORMAT)

*   [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_INPUT_FORMATS)

*   [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR)

*   [`YEAR_MONTH_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-YEAR_MONTH_FORMAT)

### HTTP[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#http "Link to this heading")

*   [`DATA_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATA_UPLOAD_MAX_MEMORY_SIZE)

*   [`DATA_UPLOAD_MAX_NUMBER_FIELDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATA_UPLOAD_MAX_NUMBER_FIELDS)

*   [`DATA_UPLOAD_MAX_NUMBER_FILES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATA_UPLOAD_MAX_NUMBER_FILES)

*   [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_CHARSET)

*   [`DISALLOWED_USER_AGENTS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DISALLOWED_USER_AGENTS)

*   [`FORCE_SCRIPT_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FORCE_SCRIPT_NAME)

*   [`INTERNAL_IPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INTERNAL_IPS)

*   [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIDDLEWARE)

*   Security

    *   [`SECURE_CONTENT_TYPE_NOSNIFF`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_CONTENT_TYPE_NOSNIFF)

    *   [`SECURE_CROSS_ORIGIN_OPENER_POLICY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_CROSS_ORIGIN_OPENER_POLICY)

    *   [`SECURE_CSP`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_CSP)

    *   [`SECURE_CSP_REPORT_ONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_CSP_REPORT_ONLY)

    *   [`SECURE_HSTS_INCLUDE_SUBDOMAINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_HSTS_INCLUDE_SUBDOMAINS)

    *   [`SECURE_HSTS_PRELOAD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_HSTS_PRELOAD)

    *   [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS)

    *   [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER)

    *   [`SECURE_REDIRECT_EXEMPT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_REDIRECT_EXEMPT)

    *   [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_REFERRER_POLICY)

    *   [`SECURE_SSL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_SSL_HOST)

    *   [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT)

*   [`SIGNING_BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SIGNING_BACKEND)

*   [`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST)

*   [`USE_X_FORWARDED_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_X_FORWARDED_PORT)

*   [`WSGI_APPLICATION`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-WSGI_APPLICATION)

### Logging[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#id12 "Link to this heading")

*   [`LOGGING`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LOGGING)

*   [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LOGGING_CONFIG)

### Models[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#models "Link to this heading")

*   [`ABSOLUTE_URL_OVERRIDES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ABSOLUTE_URL_OVERRIDES)

*   [`FIXTURE_DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-FIXTURE_DIRS)

*   [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS)

### Security[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#security "Link to this heading")

*   Cross Site Request Forgery Protection

    *   [`CSRF_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_COOKIE_DOMAIN)

    *   [`CSRF_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_COOKIE_NAME)

    *   [`CSRF_COOKIE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_COOKIE_PATH)

    *   [`CSRF_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_COOKIE_SAMESITE)

    *   [`CSRF_COOKIE_SECURE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_COOKIE_SECURE)

    *   [`CSRF_FAILURE_VIEW`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_FAILURE_VIEW)

    *   [`CSRF_HEADER_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_HEADER_NAME)

    *   [`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_TRUSTED_ORIGINS)

    *   [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CSRF_USE_SESSIONS)

*   [`SECRET_KEY`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY)

*   [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS)

*   [`URLIZE_ASSUME_HTTPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-URLIZE_ASSUME_HTTPS)

*   [`X_FRAME_OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-X_FRAME_OPTIONS)

### Serialization[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#serialization "Link to this heading")

*   [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_CHARSET)

*   [`SERIALIZATION_MODULES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SERIALIZATION_MODULES)

### Templates[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#id13 "Link to this heading")

*   [`TEMPLATES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES)

### Testing[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#testing "Link to this heading")

*   Database: [`TEST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-TEST)

*   [`TEST_NON_SERIALIZED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_NON_SERIALIZED_APPS)

*   [`TEST_RUNNER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_RUNNER)

### URLs[¶](https://docs.djangoproject.com/en/6.0/ref/settings/#urls "Link to this heading")

*   [`APPEND_SLASH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-APPEND_SLASH)

*   [`PREPEND_WWW`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PREPEND_WWW)

*   [`ROOT_URLCONF`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ROOT_URLCONF)

Previous page and next page

[`SchemaEditor`](https://docs.djangoproject.com/en/6.0/ref/schema-editor/)

[Signals](https://docs.djangoproject.com/en/6.0/ref/signals/)

[Back to Top](https://docs.djangoproject.com/en/6.0/ref/settings/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [Jannis Leidel donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [Settings](https://docs.djangoproject.com/en/6.0/ref/settings/#)
    *   [Core Settings](https://docs.djangoproject.com/en/6.0/ref/settings/#core-settings)
        *   [`ABSOLUTE_URL_OVERRIDES`](https://docs.djangoproject.com/en/6.0/ref/settings/#absolute-url-overrides)
        *   [`ADMINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#admins)
        *   [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/6.0/ref/settings/#allowed-hosts)
        *   [`APPEND_SLASH`](https://docs.djangoproject.com/en/6.0/ref/settings/#append-slash)
        *   [`CACHES`](https://docs.djangoproject.com/en/6.0/ref/settings/#caches)
            *   [`BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#backend)
            *   [`KEY_FUNCTION`](https://docs.djangoproject.com/en/6.0/ref/settings/#key-function)
            *   [`KEY_PREFIX`](https://docs.djangoproject.com/en/6.0/ref/settings/#key-prefix)
            *   [`LOCATION`](https://docs.djangoproject.com/en/6.0/ref/settings/#location)
            *   [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#options)
            *   [`TIMEOUT`](https://docs.djangoproject.com/en/6.0/ref/settings/#timeout)
            *   [`VERSION`](https://docs.djangoproject.com/en/6.0/ref/settings/#version)

        *   [`CACHE_MIDDLEWARE_ALIAS`](https://docs.djangoproject.com/en/6.0/ref/settings/#cache-middleware-alias)
        *   [`CACHE_MIDDLEWARE_KEY_PREFIX`](https://docs.djangoproject.com/en/6.0/ref/settings/#cache-middleware-key-prefix)
        *   [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#cache-middleware-seconds)
        *   [`CSRF_COOKIE_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-age)
        *   [`CSRF_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-domain)
        *   [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-httponly)
        *   [`CSRF_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-name)
        *   [`CSRF_COOKIE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-path)
        *   [`CSRF_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-samesite)
        *   [`CSRF_COOKIE_SECURE`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-cookie-secure)
        *   [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-use-sessions)
        *   [`CSRF_FAILURE_VIEW`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-failure-view)
        *   [`CSRF_HEADER_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-header-name)
        *   [`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-trusted-origins)
        *   [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#databases)
            *   [`ATOMIC_REQUESTS`](https://docs.djangoproject.com/en/6.0/ref/settings/#atomic-requests)
            *   [`AUTOCOMMIT`](https://docs.djangoproject.com/en/6.0/ref/settings/#autocommit)
            *   [`ENGINE`](https://docs.djangoproject.com/en/6.0/ref/settings/#engine)
            *   [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#host)
            *   [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#name)
            *   [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#conn-max-age)
            *   [`CONN_HEALTH_CHECKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#conn-health-checks)
            *   [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-OPTIONS)
            *   [`PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#password)
            *   [`PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#port)
            *   [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#time-zone)
            *   [`DISABLE_SERVER_SIDE_CURSORS`](https://docs.djangoproject.com/en/6.0/ref/settings/#disable-server-side-cursors)
            *   [`USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#user)
            *   [`TEST`](https://docs.djangoproject.com/en/6.0/ref/settings/#test)
                *   [`CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#charset)
                *   [`COLLATION`](https://docs.djangoproject.com/en/6.0/ref/settings/#collation)
                *   [`DEPENDENCIES`](https://docs.djangoproject.com/en/6.0/ref/settings/#dependencies)
                *   [`MIGRATE`](https://docs.djangoproject.com/en/6.0/ref/settings/#migrate)
                *   [`MIRROR`](https://docs.djangoproject.com/en/6.0/ref/settings/#mirror)
                *   [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_NAME)
                *   [`TEMPLATE`](https://docs.djangoproject.com/en/6.0/ref/settings/#template)
                *   [`CREATE_DB`](https://docs.djangoproject.com/en/6.0/ref/settings/#create-db)
                *   [`CREATE_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#create-user)
                *   [`USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_USER)
                *   [`PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEST_PASSWD)
                *   [`ORACLE_MANAGED_FILES`](https://docs.djangoproject.com/en/6.0/ref/settings/#oracle-managed-files)
                *   [`TBLSPACE`](https://docs.djangoproject.com/en/6.0/ref/settings/#tblspace)
                *   [`TBLSPACE_TMP`](https://docs.djangoproject.com/en/6.0/ref/settings/#tblspace-tmp)
                *   [`DATAFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile)
                *   [`DATAFILE_TMP`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp)
                *   [`DATAFILE_MAXSIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-maxsize)
                *   [`DATAFILE_TMP_MAXSIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp-maxsize)
                *   [`DATAFILE_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-size)
                *   [`DATAFILE_TMP_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp-size)
                *   [`DATAFILE_EXTSIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-extsize)
                *   [`DATAFILE_TMP_EXTSIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#datafile-tmp-extsize)

        *   [`DATA_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#data-upload-max-memory-size)
        *   [`DATA_UPLOAD_MAX_NUMBER_FIELDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#data-upload-max-number-fields)
        *   [`DATA_UPLOAD_MAX_NUMBER_FILES`](https://docs.djangoproject.com/en/6.0/ref/settings/#data-upload-max-number-files)
        *   [`DATABASE_ROUTERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#database-routers)
        *   [`DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#date-format)
        *   [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#date-input-formats)
        *   [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#datetime-format)
        *   [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#datetime-input-formats)
        *   [`DEBUG`](https://docs.djangoproject.com/en/6.0/ref/settings/#debug)
        *   [`DEBUG_PROPAGATE_EXCEPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#debug-propagate-exceptions)
        *   [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#decimal-separator)
        *   [`DEFAULT_AUTO_FIELD`](https://docs.djangoproject.com/en/6.0/ref/settings/#default-auto-field)
        *   [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#default-charset)
        *   [`DEFAULT_EXCEPTION_REPORTER`](https://docs.djangoproject.com/en/6.0/ref/settings/#default-exception-reporter)
        *   [`DEFAULT_EXCEPTION_REPORTER_FILTER`](https://docs.djangoproject.com/en/6.0/ref/settings/#default-exception-reporter-filter)
        *   [`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#default-from-email)
        *   [`DEFAULT_INDEX_TABLESPACE`](https://docs.djangoproject.com/en/6.0/ref/settings/#default-index-tablespace)
        *   [`DEFAULT_TABLESPACE`](https://docs.djangoproject.com/en/6.0/ref/settings/#default-tablespace)
        *   [`DISALLOWED_USER_AGENTS`](https://docs.djangoproject.com/en/6.0/ref/settings/#disallowed-user-agents)
        *   [`EMAIL_BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-backend)
        *   [`EMAIL_FILE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-file-path)
        *   [`EMAIL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-host)
        *   [`EMAIL_HOST_PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-host-password)
        *   [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-host-user)
        *   [`EMAIL_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-port)
        *   [`EMAIL_SUBJECT_PREFIX`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-subject-prefix)
        *   [`EMAIL_USE_LOCALTIME`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-use-localtime)
        *   [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-use-tls)
        *   [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-use-ssl)
        *   [`EMAIL_SSL_CERTFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-ssl-certfile)
        *   [`EMAIL_SSL_KEYFILE`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-ssl-keyfile)
        *   [`EMAIL_TIMEOUT`](https://docs.djangoproject.com/en/6.0/ref/settings/#email-timeout)
        *   [`FILE_UPLOAD_HANDLERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-handlers)
        *   [`FILE_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-max-memory-size)
        *   [`FILE_UPLOAD_DIRECTORY_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-directory-permissions)
        *   [`FILE_UPLOAD_PERMISSIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-permissions)
        *   [`FILE_UPLOAD_TEMP_DIR`](https://docs.djangoproject.com/en/6.0/ref/settings/#file-upload-temp-dir)
        *   [`FIRST_DAY_OF_WEEK`](https://docs.djangoproject.com/en/6.0/ref/settings/#first-day-of-week)
        *   [`FIXTURE_DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#fixture-dirs)
        *   [`FORCE_SCRIPT_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#force-script-name)
        *   [`FORM_RENDERER`](https://docs.djangoproject.com/en/6.0/ref/settings/#form-renderer)
        *   [`FORMAT_MODULE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#format-module-path)
        *   [`IGNORABLE_404_URLS`](https://docs.djangoproject.com/en/6.0/ref/settings/#ignorable-404-urls)
        *   [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#installed-apps)
        *   [`INTERNAL_IPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#internal-ips)
        *   [`LANGUAGE_CODE`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-code)
        *   [`LANGUAGE_COOKIE_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-age)
        *   [`LANGUAGE_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-domain)
        *   [`LANGUAGE_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-httponly)
        *   [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-name)
        *   [`LANGUAGE_COOKIE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-path)
        *   [`LANGUAGE_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-samesite)
        *   [`LANGUAGE_COOKIE_SECURE`](https://docs.djangoproject.com/en/6.0/ref/settings/#language-cookie-secure)
        *   [`LANGUAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#languages)
        *   [`LANGUAGES_BIDI`](https://docs.djangoproject.com/en/6.0/ref/settings/#languages-bidi)
        *   [`LOCALE_PATHS`](https://docs.djangoproject.com/en/6.0/ref/settings/#locale-paths)
        *   [`LOGGING`](https://docs.djangoproject.com/en/6.0/ref/settings/#logging)
        *   [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/6.0/ref/settings/#logging-config)
        *   [`MANAGERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#managers)
        *   [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#media-root)
        *   [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#media-url)
        *   [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#middleware)
        *   [`MIGRATION_MODULES`](https://docs.djangoproject.com/en/6.0/ref/settings/#migration-modules)
        *   [`MONTH_DAY_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#month-day-format)
        *   [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/6.0/ref/settings/#number-grouping)
        *   [`PREPEND_WWW`](https://docs.djangoproject.com/en/6.0/ref/settings/#prepend-www)
        *   [`ROOT_URLCONF`](https://docs.djangoproject.com/en/6.0/ref/settings/#root-urlconf)
        *   [`SECRET_KEY`](https://docs.djangoproject.com/en/6.0/ref/settings/#secret-key)
        *   [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#secret-key-fallbacks)
        *   [`SECURE_CONTENT_TYPE_NOSNIFF`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-content-type-nosniff)
        *   [`SECURE_CROSS_ORIGIN_OPENER_POLICY`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-cross-origin-opener-policy)
        *   [`SECURE_CSP`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-csp)
        *   [`SECURE_CSP_REPORT_ONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-csp-report-only)
        *   [`SECURE_HSTS_INCLUDE_SUBDOMAINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-hsts-include-subdomains)
        *   [`SECURE_HSTS_PRELOAD`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-hsts-preload)
        *   [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-hsts-seconds)
        *   [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-proxy-ssl-header)
        *   [`SECURE_REDIRECT_EXEMPT`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-redirect-exempt)
        *   [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-referrer-policy)
        *   [`SECURE_SSL_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-ssl-host)
        *   [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-ssl-redirect)
        *   [`SERIALIZATION_MODULES`](https://docs.djangoproject.com/en/6.0/ref/settings/#serialization-modules)
        *   [`SERVER_EMAIL`](https://docs.djangoproject.com/en/6.0/ref/settings/#server-email)
        *   [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#short-date-format)
        *   [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#short-datetime-format)
        *   [`SIGNING_BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#signing-backend)
        *   [`SILENCED_SYSTEM_CHECKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#silenced-system-checks)
        *   [`STORAGES`](https://docs.djangoproject.com/en/6.0/ref/settings/#storages)
        *   [`TASKS`](https://docs.djangoproject.com/en/6.0/ref/settings/#tasks)
            *   [`BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TASKS-BACKEND)
            *   [`QUEUES`](https://docs.djangoproject.com/en/6.0/ref/settings/#queues)
            *   [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TASKS-OPTIONS)

        *   [`TEMPLATES`](https://docs.djangoproject.com/en/6.0/ref/settings/#templates)
            *   [`BACKEND`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-BACKEND)
            *   [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-NAME)
            *   [`DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#dirs)
            *   [`APP_DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#app-dirs)
            *   [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-OPTIONS)

        *   [`TEST_RUNNER`](https://docs.djangoproject.com/en/6.0/ref/settings/#test-runner)
        *   [`TEST_NON_SERIALIZED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#test-non-serialized-apps)
        *   [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#thousand-separator)
        *   [`TIME_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#time-format)
        *   [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/6.0/ref/settings/#time-input-formats)
        *   [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE)
        *   [`USE_I18N`](https://docs.djangoproject.com/en/6.0/ref/settings/#use-i18n)
        *   [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/6.0/ref/settings/#use-thousand-separator)
        *   [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#use-tz)
        *   [`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#use-x-forwarded-host)
        *   [`USE_X_FORWARDED_PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#use-x-forwarded-port)
        *   [`URLIZE_ASSUME_HTTPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#urlize-assume-https)
        *   [`WSGI_APPLICATION`](https://docs.djangoproject.com/en/6.0/ref/settings/#wsgi-application)
        *   [`YEAR_MONTH_FORMAT`](https://docs.djangoproject.com/en/6.0/ref/settings/#year-month-format)
        *   [`X_FRAME_OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/settings/#x-frame-options)

    *   [Auth](https://docs.djangoproject.com/en/6.0/ref/settings/#auth)
        *   [`AUTHENTICATION_BACKENDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#authentication-backends)
        *   [`AUTH_USER_MODEL`](https://docs.djangoproject.com/en/6.0/ref/settings/#auth-user-model)
        *   [`LOGIN_REDIRECT_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#login-redirect-url)
        *   [`LOGIN_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#login-url)
        *   [`LOGOUT_REDIRECT_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#logout-redirect-url)
        *   [`PASSWORD_RESET_TIMEOUT`](https://docs.djangoproject.com/en/6.0/ref/settings/#password-reset-timeout)
        *   [`PASSWORD_HASHERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#password-hashers)
        *   [`AUTH_PASSWORD_VALIDATORS`](https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators)

    *   [Messages](https://docs.djangoproject.com/en/6.0/ref/settings/#messages)
        *   [`MESSAGE_LEVEL`](https://docs.djangoproject.com/en/6.0/ref/settings/#message-level)
        *   [`MESSAGE_STORAGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#message-storage)
        *   [`MESSAGE_TAGS`](https://docs.djangoproject.com/en/6.0/ref/settings/#message-tags)

    *   [Sessions](https://docs.djangoproject.com/en/6.0/ref/settings/#sessions)
        *   [`SESSION_CACHE_ALIAS`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cache-alias)
        *   [`SESSION_COOKIE_AGE`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-age)
        *   [`SESSION_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-domain)
        *   [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-httponly)
        *   [`SESSION_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-name)
        *   [`SESSION_COOKIE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-path)
        *   [`SESSION_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-samesite)
        *   [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-cookie-secure)
        *   [`SESSION_ENGINE`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-engine)
        *   [`SESSION_EXPIRE_AT_BROWSER_CLOSE`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-expire-at-browser-close)
        *   [`SESSION_FILE_PATH`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-file-path)
        *   [`SESSION_SAVE_EVERY_REQUEST`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-save-every-request)
        *   [`SESSION_SERIALIZER`](https://docs.djangoproject.com/en/6.0/ref/settings/#session-serializer)

    *   [Sites](https://docs.djangoproject.com/en/6.0/ref/settings/#sites)
        *   [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#site-id)

    *   [Static Files](https://docs.djangoproject.com/en/6.0/ref/settings/#static-files)
        *   [`STATIC_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#static-root)
        *   [`STATIC_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#static-url)
        *   [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#staticfiles-dirs)
            *   [Prefixes (optional)](https://docs.djangoproject.com/en/6.0/ref/settings/#prefixes-optional)

        *   [`STATICFILES_FINDERS`](https://docs.djangoproject.com/en/6.0/ref/settings/#staticfiles-finders)

    *   [Core Settings Topical Index](https://docs.djangoproject.com/en/6.0/ref/settings/#core-settings-topical-index)
        *   [Cache](https://docs.djangoproject.com/en/6.0/ref/settings/#cache)
        *   [Database](https://docs.djangoproject.com/en/6.0/ref/settings/#database)
        *   [Debugging](https://docs.djangoproject.com/en/6.0/ref/settings/#debugging)
        *   [Email](https://docs.djangoproject.com/en/6.0/ref/settings/#email)
        *   [Error reporting](https://docs.djangoproject.com/en/6.0/ref/settings/#error-reporting)
        *   [File uploads](https://docs.djangoproject.com/en/6.0/ref/settings/#file-uploads)
        *   [Forms](https://docs.djangoproject.com/en/6.0/ref/settings/#forms)
        *   [Globalization (`i18n`/`l10n`)](https://docs.djangoproject.com/en/6.0/ref/settings/#globalization-i18n-l10n)
            *   [Internationalization (`i18n`)](https://docs.djangoproject.com/en/6.0/ref/settings/#internationalization-i18n)
            *   [Localization (`l10n`)](https://docs.djangoproject.com/en/6.0/ref/settings/#localization-l10n)

        *   [HTTP](https://docs.djangoproject.com/en/6.0/ref/settings/#http)
        *   [Logging](https://docs.djangoproject.com/en/6.0/ref/settings/#id12)
        *   [Models](https://docs.djangoproject.com/en/6.0/ref/settings/#models)
        *   [Security](https://docs.djangoproject.com/en/6.0/ref/settings/#security)
        *   [Serialization](https://docs.djangoproject.com/en/6.0/ref/settings/#serialization)
        *   [Templates](https://docs.djangoproject.com/en/6.0/ref/settings/#id13)
        *   [Testing](https://docs.djangoproject.com/en/6.0/ref/settings/#testing)
        *   [URLs](https://docs.djangoproject.com/en/6.0/ref/settings/#urls)

### Browse

*   Prev: [`SchemaEditor`](https://docs.djangoproject.com/en/6.0/ref/schema-editor/)
*   Next: [Signals](https://docs.djangoproject.com/en/6.0/ref/signals/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
        *   Settings

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)Try the FAQ — it's got answers to many common questions.[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)Handy when looking for specific information.[Django Discord Server](https://chat.djangoproject.com/)Join the Django Discord Community.[Official Django Forum](https://forum.djangoproject.com/)Join the community on the Django Forum.[Ticket tracker](https://code.djangoproject.com/)Report bugs with Django or Django documentation in our ticket tracker.
### Download:

Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) | [PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) | [ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)

 Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Image 2: JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

*   **JetBrains**
*   [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")

[![Image 3: Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

*   **Sentry**
*   [Monitor your Django Code Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![Image 4: Kraken Tech](https://media.djangoproject.com/cache/71/4b/714b3473ed0cf3665f6b894d3be9491e.png)](https://kraken.tech/ "Kraken Tech")

*   **Kraken Tech**
*   [Kraken is the most-loved operating system for energy. Powered by our Utility-Grade AI™ and deep industry know-how, we help utilities transform their technology and operations so they can lead the energy transition. Delivering better outcomes from generation through distribution to supply, Kraken powers 70+ million accounts worldwide, and is on a mission to make a big, green dent in the universe.](https://kraken.tech/ "Kraken Tech")

Django Links
------------

### Learn More

*   [About Django](https://www.djangoproject.com/start/overview/)
*   [Getting Started with Django](https://www.djangoproject.com/start/)
*   [Team Organization](https://www.djangoproject.com/foundation/teams/)
*   [Django Software Foundation](https://www.djangoproject.com/foundation/)
*   [Code of Conduct](https://www.djangoproject.com/conduct/)
*   [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

*   [Join a Group](https://www.djangoproject.com/community/)
*   [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
*   [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
*   [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
*   [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

*   [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
*   [Django Discord](https://chat.djangoproject.com/)
*   [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

*   [GitHub](https://github.com/django)
*   [X](https://x.com/djangoproject)
*   [Fediverse (Mastodon)](https://fosstodon.org/@django)
*   [Bluesky](https://bsky.app/profile/djangoproject.com)
*   [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
*   [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

*   [Sponsor Django](https://www.djangoproject.com/fundraising/)
*   [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
*   [Official merchandise store](https://django.threadless.com/)
*   [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

*   Hosting by[In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
*   Design by[Threespot](https://www.threespot.com/)&[andrevv](http://andrevv.com/)

© 2005-2026 [Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
