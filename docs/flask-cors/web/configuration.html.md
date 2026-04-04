# Flask-CORS Documentation
# Source: https://flask-cors.readthedocs.io/en/latest/configuration.html
# Path: configuration.html

[ Flask-Cors ](index.html)

latest

  * [Flask-CORS](index.html)
  * Configuration
    * Configuration options
    * Default values
    * Locations
      * Resource level settings
      * Keyword argument settings
      * App level configuration settings
      * Default settings
  * [API Docs](api.html)

__[Flask-Cors](index.html)

  * [Docs](index.html) »
  * Configuration
  * [ Edit on GitHub](https://github.com/corydolphin/flask-cors/blob/master/docs/configuration.rst)

* * *

# Configuration¶

Flask-CORS can be configured at four different locations. Configuration values
are determined in the following order:

>   1. Resource level settings (e.g when passed as a dictionary)
>   2. Keyword argument settings
>   3. App level configuration settings (e.g. CORS_*)
>   4. Default settings
>

See below for more information.

## Configuration options¶

Configuration options are consistently named across the various locations
where they can be set. A configuration option called _example_ can be set with
the resource dictionary key _example_ , as the keyword argument _example_ or
as the Flask app configuration key _CORS_EXAMPLE_.

The configuration options recognised by Flask-CORS are:

CORS_ALLOW_HEADERS
([`List`](https://docs.python.org/3/library/typing.html#typing.List "\(in
Python v3.11\)") or
[`str`](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)"))

    Headers to accept from the client. Headers in the [Access-Control-Request-Headers](http://www.w3.org/TR/cors/#access-control-request-headers-response-header) request header (usually part of the preflight OPTIONS request) matching headers in this list will be included in the [Access-Control-Allow-Headers](http://www.w3.org/TR/cors/#access-control-allow-headers-response-header) response header.
CORS_ALWAYS_SEND
([`bool`](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)"))

    

Usually, if a request doesn’t include an
[Origin](http://www.w3.org/TR/cors/#origin-request-header) header, the client
did not request CORS. This means we can ignore this request.

However, if this is true, a most-likely-to-be-correct value is still set.

CORS_AUTOMATIC_OPTIONS
([`bool`](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)"))

    Only applies to the [`flask_cors.cross_origin()`](api.html#flask_cors.cross_origin "flask_cors.cross_origin") decorator. If True, Flask-CORS will override Flask’s default OPTIONS handling to return CORS headers for OPTIONS requests.
CORS_EXPOSE_HEADERS
([`List`](https://docs.python.org/3/library/typing.html#typing.List "\(in
Python v3.11\)") or
[`str`](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)"))

    The CORS spec requires the server to give explicit permissions for the client to read headers in CORS responses (via the [Access-Control-Expose-Headers](http://www.w3.org/TR/cors/#access-control-expose-headers-response-header) header). This specifies the headers to include in this header.
CORS_INTERCEPT_EXCEPTIONS
([`bool`](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)"))

    Whether to deal with Flask exception handlers or leave them alone (with respect to CORS headers).
CORS_MAX_AGE
([`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta
"\(in Python v3.11\)"),
[`int`](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)") or [`str`](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)"))

    The maximum time for which this CORS request may be cached. This value is set as the [Access-Control-Max-Age](http://www.w3.org/TR/cors/#access-control-max-age-response-header) header.
CORS_METHODS
([`List`](https://docs.python.org/3/library/typing.html#typing.List "\(in
Python v3.11\)") or
[`str`](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)"))

    The method(s) which the allowed origins are allowed to access. These are included in the [Access-Control-Allow-Methods](http://www.w3.org/TR/cors/#access-control-allow-methods-response-header) response headers to the preflight OPTIONS requests.

CORS_ORIGINS
([`List`](https://docs.python.org/3/library/typing.html#typing.List "\(in
Python v3.11\)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") or `re.Pattern`)

    The origin(s) to allow requests from. An origin configured here that matches the value of the [Origin](http://www.w3.org/TR/cors/#origin-request-header) header in a preflight OPTIONS request is returned as the value of the [Access-Control-Allow-Origin](http://www.w3.org/TR/cors/#access-control-allow-origin-response-header) response header.
CORS_RESOURCES
([`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict "\(in
Python v3.11\)"),
[`List`](https://docs.python.org/3/library/typing.html#typing.List "\(in
Python v3.11\)") or
[`str`](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)"))

    

The series of regular expression and (optionally) associated CORS options to
be applied to the given resource path.

If the value is a dictionary, it’s keys must be regular expressions matching
resources, and the values must be another dictionary of configuration options,
as described in this section.

If the argument is a list, it is expected to be a list of regular expressions
matching resources for which the app-wide configured options are applied.

If the argument is a string, it is expected to be a regular expression
matching resources for which the app-wide configured options are applied.

CORS_SEND_WILDCARD
([`bool`](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)"))

    If CORS_ORIGINS is `"*"` and this is true, then the [Access-Control-Allow-Origin](http://www.w3.org/TR/cors/#access-control-allow-origin-response-header) response header’s value with be `"*"` as well, instead of the value of the [Origin](http://www.w3.org/TR/cors/#origin-request-header) request header.
CORS_SUPPORTS_CREDENTIALS
([`bool`](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)"))

    

Allows users to make authenticated requests. If true, injects the [Access-
Control-Allow-Credentials](http://www.w3.org/TR/cors/#access-control-allow-
credentials-response-header) header in responses. This allows cookies and
credentials to be submitted across domains.

note:| This option cannot be used in conjunction with a “*” origin  
---|---  
CORS_VARY_HEADER:
([`bool`](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)"))

    Enables or disables the injection of the [Vary](https://tools.ietf.org/html/rfc7231#section-7.1.4) response header is set to `Origin`. This informs clients that our CORS headers are dynamic and cannot be cached.

## Default values¶

  * CORS_ALLOW_HEADERS: “*”
  * CORS_ALWAYS_SEND: True
  * CORS_AUTOMATIC_OPTIONS: True
  * CORS_EXPOSE_HEADERS: None
  * CORS_INTERCEPT_EXCEPTIONS: True
  * CORS_MAX_AGE: None
  * CORS_METHODS: [”[GET](https://tools.ietf.org/html/rfc7231#section-4.3.1)”, “[HEAD](https://tools.ietf.org/html/rfc7231#section-4.3.2)”, “[POST](https://tools.ietf.org/html/rfc7231#section-4.3.3)”, “[OPTIONS](https://tools.ietf.org/html/rfc7231#section-4.3.7)”, “[PUT](https://tools.ietf.org/html/rfc7231#section-4.3.4)”, “[PATCH](https://tools.ietf.org/html/rfc5789#section-2)”, “[DELETE](https://tools.ietf.org/html/rfc7231#section-4.3.5)”]
  * CORS_ORIGINS: “*”
  * CORS_RESOURCES: r”/*”
  * CORS_SEND_WILDCARD: False
  * CORS_SUPPORTS_CREDENTIALS: False
  * CORS_VARY_HEADER: True

## Locations¶

### Resource level settings¶

You can specify CORS options on a resource level of granularity by passing a
dictionary as the _resources_ keyword argument when instantiating the
[`flask_cors.CORS`](api.html#flask_cors.CORS "flask_cors.CORS") object (or
when calling `init_app` on it), mapping paths to a set of options.

### Keyword argument settings¶

For options matching all resources, it’s also possible to simply set the
configuration options using keyword arguments when instantiating the
[`flask_cors.CORS`](api.html#flask_cors.CORS "flask_cors.CORS") object (or
when calling `init_app` on it).

### App level configuration settings¶

It’s good practice to keep your application configuration settings in one
place. This is also possible with Flask-CORS using the same configuration
options in the Flas application’s config object.

### Default settings¶

Finally, every setting has a default value as well.

[Next ](api.html "API Docs") [ Previous](index.html "Flask-CORS")

* * *

(C) Copyright 2013, Cory Dolphin  Revision `b2c4da1f`.

Built with [Sphinx](http://sphinx-doc.org/) using a
[theme](https://github.com/rtfd/sphinx_rtd_theme) provided by [Read the
Docs](https://readthedocs.org).

