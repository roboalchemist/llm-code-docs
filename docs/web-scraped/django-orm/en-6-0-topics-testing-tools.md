# Source: https://docs.djangoproject.com/en/6.0/topics/testing/tools/

Title: Testing tools | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/topics/testing/tools/

Markdown Content:
Django provides a small set of tools that come in handy when writing tests.

The test client[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#the-test-client "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

The test client is a Python class that acts as a dummy web browser, allowing you to test your views and interact with your Django-powered application programmatically.

Some of the things you can do with the test client are:

*   Simulate GET and POST requests on a URL and observe the response – everything from low-level HTTP (result headers and status codes) to page content.

*   See the chain of redirects (if any) and check the URL and status code at each step.

*   Test that a given request is rendered by a given Django template, with a template context that contains certain values.

Note that the test client is not intended to be a replacement for [Selenium](https://www.selenium.dev/) or other “in-browser” frameworks. Django’s test client has a different focus. In short:

*   Use Django’s test client to establish that the correct template is being rendered and that the template is passed the correct context data.

*   Use [`RequestFactory`](https://docs.djangoproject.com/en/6.0/topics/testing/advanced/#django.test.RequestFactory "django.test.RequestFactory") to test view functions directly, bypassing the routing and middleware layers.

*   Use in-browser frameworks like [Selenium](https://www.selenium.dev/) to test _rendered_ HTML and the _behavior_ of web pages, namely JavaScript functionality. Django also provides special support for those frameworks; see the section on [`LiveServerTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.LiveServerTestCase "django.test.LiveServerTestCase") for more details.

A comprehensive test suite should use a combination of all of these test types.

### Overview and a quick example[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#overview-and-a-quick-example "Link to this heading")

To use the test client, instantiate `django.test.Client` and retrieve web pages:

>>> from django.test import Client
>>> c = Client()
>>> response = c.post("/login/", {"username": "john", "password": "smith"})
>>> response.status_code
200
>>> response = c.get("/customer/details/")
>>> response.content
b'<!DOCTYPE html...'

As this example suggests, you can instantiate `Client` from within a session of the Python interactive interpreter.

Note a few important things about how the test client works:

*   The test client does _not_ require the web server to be running. In fact, it will run just fine with no web server running at all! That’s because it avoids the overhead of HTTP and deals directly with the Django framework. This helps make the unit tests run quickly.

*   When retrieving pages, remember to specify the _path_ of the URL, not the whole domain. For example, this is correct:

>>> c.get("/login/") 
This is incorrect:

>>> c.get("https://www.example.com/login/") 
The test client is not capable of retrieving web pages that are not powered by your Django project. If you need to retrieve other web pages, use a Python standard library module such as [`urllib`](https://docs.python.org/3/library/urllib.html#module-urllib "(in Python v3.14)").

*   To resolve URLs, the test client uses whatever URLconf is pointed-to by your [`ROOT_URLCONF`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-ROOT_URLCONF) setting.

*   Although the above example would work in the Python interactive interpreter, some of the test client’s functionality, notably the template-related functionality, is only available _while tests are running_.

The reason for this is that Django’s test runner performs a bit of black magic in order to determine which template was loaded by a given view. This black magic (essentially a patching of Django’s template system in memory) only happens during test running.

*   By default, the test client will disable any CSRF checks performed by your site.

If, for some reason, you _want_ the test client to perform CSRF checks, you can create an instance of the test client that enforces CSRF checks. To do this, pass in the `enforce_csrf_checks` argument when you construct your client:

>>> from django.test import Client
>>> csrf_client = Client(enforce_csrf_checks=True) 

### Making requests[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#making-requests "Link to this heading")

Use the `django.test.Client` class to make requests.

_class_ Client(_enforce\_csrf\_checks=False_, _raise\_request\_exception=True_, _json\_encoder=DjangoJSONEncoder_, _*_, _headers=None_, _query\_params=None_, _**defaults_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1028)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client "Link to this definition")
A testing HTTP client. Takes several arguments that can customize behavior.

`headers` allows you to specify default headers that will be sent with every request. For example, to set a `User-Agent` header:

client = Client(headers={"user-agent": "curl/7.79.1"})

`query_params` allows you to specify the default query string that will be set on every request.

Arbitrary keyword arguments in `**defaults` set WSGI [**environ variables**](https://peps.python.org/pep-3333/#environ-variables). For example, to set the script name:

client = Client(SCRIPT_NAME="/app/")

Note

Keyword arguments starting with a `HTTP_` prefix are set as headers, but the `headers` parameter should be preferred for readability.

The values from the `headers`, `query_params`, and `extra` keyword arguments passed to [`get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get"), [`post()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.post "django.test.Client.post"), etc. have precedence over the defaults passed to the class constructor.

The `enforce_csrf_checks` argument can be used to test CSRF protection (see above).

The `raise_request_exception` argument allows controlling whether or not exceptions raised during the request should also be raised in the test. Defaults to `True`.

The `json_encoder` argument allows setting a custom JSON encoder for the JSON serialization that’s described in [`post()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.post "django.test.Client.post").

Once you have a `Client` instance, you can call any of the following methods:

get(_path_, _data=None_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1110)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "Link to this definition")
Makes a GET request on the provided `path` and returns a `Response` object, which is documented below.

The key-value pairs in the `query_params` dictionary are used to set query strings. For example:

>>> c = Client()
>>> c.get("/customers/details/", query_params={"name": "fred", "age": 7})

…will result in the evaluation of a GET request equivalent to:

/customers/details/?name=fred&age=7

It is also possible to pass these parameters into the `data` parameter. However, `query_params` is preferred as it works for any HTTP method.

The `headers` parameter can be used to specify headers to be sent in the request. For example:

>>> c = Client()
>>> c.get(
...     "/customers/details/",
...     query_params={"name": "fred", "age": 7},
...     headers={"accept": "application/json"},
... )

…will send the HTTP header `HTTP_ACCEPT` to the details view, which is a good way to test code paths that use the [`django.http.HttpRequest.accepts()`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.accepts "django.http.HttpRequest.accepts") method.

Arbitrary keyword arguments set WSGI [**environ variables**](https://peps.python.org/pep-3333/#environ-variables). For example, headers to set the script name:

>>> c = Client()
>>> c.get("/", SCRIPT_NAME="/app/")

If you already have the GET arguments in URL-encoded form, you can use that encoding instead of using the data argument. For example, the previous GET request could also be posed as:

>>> c = Client()
>>> c.get("/customers/details/?name=fred&age=7")

If you provide a URL with both an encoded GET data and either a query_params or data argument these arguments will take precedence.

If you set `follow` to `True` the client will follow any redirects and a `redirect_chain` attribute will be set in the response object containing tuples of the intermediate urls and status codes.

If you had a URL `/redirect_me/` that redirected to `/next/`, that redirected to `/final/`, this is what you’d see:

>>> response = c.get("/redirect_me/", follow=True)
>>> response.redirect_chain
[('http://testserver/next/', 302), ('http://testserver/final/', 302)]

If you set `secure` to `True` the client will emulate an HTTPS request.

post(_path_, _data=None_, _content\_type=MULTIPART\_CONTENT_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1138)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.post "Link to this definition")
Makes a POST request on the provided `path` and returns a `Response` object, which is documented below.

The key-value pairs in the `data` dictionary are used to submit POST data. For example:

>>> c = Client()
>>> c.post("/login/", {"name": "fred", "passwd": "secret"})

…will result in the evaluation of a POST request to this URL:

/login/

…with this POST data:

name=fred&passwd=secret

If you provide `content_type` as _application/json_, the `data` is serialized using [`json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps "(in Python v3.14)") if it’s a dict, list, or tuple. Serialization is performed with [`DjangoJSONEncoder`](https://docs.djangoproject.com/en/6.0/topics/serialization/#django.core.serializers.json.DjangoJSONEncoder "django.core.serializers.json.DjangoJSONEncoder") by default, and can be overridden by providing a `json_encoder` argument to [`Client`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client "django.test.Client"). This serialization also happens for [`put()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.put "django.test.Client.put"), [`patch()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.patch "django.test.Client.patch"), and [`delete()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.delete "django.test.Client.delete") requests.

If you provide any other `content_type` (e.g. _text/xml_ for an XML payload), the contents of `data` are sent as-is in the POST request, using `content_type` in the HTTP `Content-Type` header.

If you don’t provide a value for `content_type`, the values in `data` will be transmitted with a content type of _multipart/form-data_. In this case, the key-value pairs in `data` will be encoded as a multipart message and used to create the POST data payload.

To submit multiple values for a given key – for example, to specify the selections for a `<select multiple>` – provide the values as a list or tuple for the required key. For example, this value of `data` would submit three selected values for the field named `choices`:

{"choices": ["a", "b", "d"]}

Submitting files is a special case. To POST a file, you need only provide the file field name as a key, and a file handle to the file you wish to upload as a value. For example, if your form has fields `name` and `attachment`, the latter a [`FileField`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.FileField "django.forms.FileField"):

>>> c = Client()
>>> with open("wishlist.doc", "rb") as fp:
...     c.post("/customers/wishes/", {"name": "fred", "attachment": fp})
...

You may also provide any file-like object (e.g., [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "(in Python v3.14)") or [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "(in Python v3.14)")) as a file handle. If you’re uploading to an [`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField"), the object needs a `name` attribute that passes the [`validate_image_file_extension`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.validate_image_file_extension "django.core.validators.validate_image_file_extension") validator. For example:

>>> from io import BytesIO
>>> img = BytesIO(
...     b"GIF89a\x01\x00\x01\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00"
...     b"\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x00\x00"
... )
>>> img.name = "myimage.gif"

Note that if you wish to use the same file handle for multiple `post()` calls then you will need to manually reset the file pointer between posts. The easiest way to do this is to manually close the file after it has been provided to `post()`, as demonstrated above.

You should also ensure that the file is opened in a way that allows the data to be read. If your file contains binary data such as an image, this means you will need to open the file in `rb` (read binary) mode.

The `headers`, `query_params`, and `extra` parameters acts the same as for [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

If the URL you request with a POST contains encoded parameters, these parameters will be made available in the request.GET data. For example, if you were to make the request:

>>> c.post(
...     "/login/", {"name": "fred", "passwd": "secret"}, query_params={"visitor": "true"}
... )

… the view handling this request could interrogate request.POST to retrieve the username and password, and could interrogate request.GET to determine if the user was a visitor.

If you set `follow` to `True` the client will follow any redirects and a `redirect_chain` attribute will be set in the response object containing tuples of the intermediate urls and status codes.

If you set `secure` to `True` the client will emulate an HTTPS request.

head(_path_, _data=None_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1173)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.head "Link to this definition")
Makes a HEAD request on the provided `path` and returns a `Response` object. This method works just like [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get"), including the `follow`, `secure`, `headers`, `query_params`, and `extra` parameters, except it does not return a message body.

options(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1201)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.options "Link to this definition")
Makes an OPTIONS request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.

The `follow`, `secure`, `headers`, `query_params`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

put(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1236)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.put "Link to this definition")
Makes a PUT request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.

The `follow`, `secure`, `headers`, `query_params`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

patch(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1271)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.patch "Link to this definition")
Makes a PATCH request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

The `follow`, `secure`, `headers`, `query_params`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

delete(_path_, _data=''_, _content\_type='application/octet-stream'_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1306)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.delete "Link to this definition")
Makes a DELETE request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.

When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.

The `follow`, `secure`, `headers`, `query_params`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

trace(_path_, _follow=False_, _secure=False_, _*_, _headers=None_, _query\_params=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1341)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.trace "Link to this definition")
Makes a TRACE request on the provided `path` and returns a `Response` object. Useful for simulating diagnostic probes.

Unlike the other request methods, `data` is not provided as a keyword parameter in order to comply with [**RFC 9110 Section 9.3.8**](https://datatracker.ietf.org/doc/html/rfc9110.html#section-9.3.8), which mandates that TRACE requests must not have a body.

The `follow`, `secure`, `headers`, `query_params`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").

login(_**credentials_)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.login "Link to this definition")alogin(_**credentials_)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.alogin "Link to this definition")
_Asynchronous version_: `alogin()`

If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/6.0/topics/auth/) and you deal with logging in users, you can use the test client’s `login()` method to simulate the effect of a user logging into the site.

After you call this method, the test client will have all the cookies and session data required to pass any login-based tests that may form part of a view.

The format of the `credentials` argument depends on which [authentication backend](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#authentication-backends) you’re using (which is configured by your [`AUTHENTICATION_BACKENDS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-AUTHENTICATION_BACKENDS) setting). If you’re using the standard authentication backend provided by Django (`ModelBackend`), `credentials` should be the user’s username and password, provided as keyword arguments:

>>> c = Client()
>>> c.login(username="fred", password="secret")

# Now you can access a view that's only available to logged-in users.

If you’re using a different authentication backend, this method may require different credentials. It requires whichever credentials are required by your backend’s `authenticate()` method.

`login()` returns `True` if it the credentials were accepted and login was successful.

Finally, you’ll need to remember to create user accounts before you can use this method. As we explained above, the test runner is executed using a test database, which contains no users by default. As a result, user accounts that are valid on your production site will not work under test conditions. You’ll need to create users as part of the test suite – either manually (using the Django model API) or with a test fixture. Remember that if you want your test user to have a password, you can’t set the user’s password by setting the password attribute directly – you must use the [`set_password()`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.User.set_password "django.contrib.auth.models.User.set_password") function to store a correctly hashed password. Alternatively, you can use the [`create_user()`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user "django.contrib.auth.models.UserManager.create_user") helper method to create a new user with a correctly hashed password.

force_login(_user_, _backend=None_)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.force_login "Link to this definition")aforce_login(_user_, _backend=None_)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.aforce_login "Link to this definition")
_Asynchronous version_: `aforce_login()`

If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/6.0/topics/auth/), you can use the `force_login()` method to simulate the effect of a user logging into the site. Use this method instead of [`login()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.login "django.test.Client.login") when a test requires a user be logged in and the details of how a user logged in aren’t important.

Unlike `login()`, this method skips the authentication and verification steps: inactive users ([`is_active=False`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.User.is_active "django.contrib.auth.models.User.is_active")) are permitted to login and the user’s credentials don’t need to be provided.

The user will have its `backend` attribute set to the value of the `backend` argument (which should be a dotted Python path string), or to `settings.AUTHENTICATION_BACKENDS[0]` if a value isn’t provided. The [`authenticate()`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.authenticate "django.contrib.auth.authenticate") function called by [`login()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.login "django.test.Client.login") normally annotates the user like this.

This method is faster than `login()` since the expensive password hashing algorithms are bypassed. Also, you can speed up `login()` by [using a weaker hasher while testing](https://docs.djangoproject.com/en/6.0/topics/testing/overview/#speeding-up-tests-auth-hashers).

logout()[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.logout "Link to this definition")alogout()[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.alogout "Link to this definition")
_Asynchronous version_: `alogout()`

If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/6.0/topics/auth/), the `logout()` method can be used to simulate the effect of a user logging out of your site.

After you call this method, the test client will have all the cookies and session data cleared to defaults. Subsequent requests will appear to come from an [`AnonymousUser`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser "django.contrib.auth.models.AnonymousUser").

### Testing responses[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#testing-responses "Link to this heading")

The `get()` and `post()` methods both return a `Response` object. This `Response` object is _not_ the same as the `HttpResponse` object returned by Django views; the test response object has some additional data useful for test code to verify.

Specifically, a `Response` object has the following attributes:

_class_ Response[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response "Link to this definition")client[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.client "Link to this definition")
The test client that was used to make the request that resulted in the response.

content[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.content "Link to this definition")
The body of the response, as a bytestring. This is the final page content as rendered by the view, or any error message.

context[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.context "Link to this definition")
The template `Context` instance that was used to render the template that produced the response content.

If the rendered page used multiple templates, then `context` will be a list of `Context` objects, in the order in which they were rendered.

Regardless of the number of templates used during rendering, you can retrieve context values using the `[]` operator. For example, the context variable `name` could be retrieved using:

>>> response = client.get("/foo/")
>>> response.context["name"]
'Arthur'

Not using Django templates?

This attribute is only populated when using the [`DjangoTemplates`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") backend. If you’re using another template engine, [`context_data`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.context_data "django.template.response.SimpleTemplateResponse.context_data") may be a suitable alternative on responses with that attribute.

exc_info[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.exc_info "Link to this definition")
A tuple of three values that provides information about the unhandled exception, if any, that occurred during the view.

The values are (type, value, traceback), the same as returned by Python’s [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "(in Python v3.14)"). Their meanings are:

*   _type_: The type of the exception.

*   _value_: The exception instance.

*   _traceback_: A traceback object which encapsulates the call stack at the point where the exception originally occurred.

If no exception occurred, then `exc_info` will be `None`.

json(_**kwargs_)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.json "Link to this definition")
The body of the response, parsed as JSON. Extra keyword arguments are passed to [`json.loads()`](https://docs.python.org/3/library/json.html#json.loads "(in Python v3.14)"). For example:

>>> response = client.get("/foo/")
>>> response.json()["name"]
'Arthur'

If the `Content-Type` header is not `"application/json"`, then a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") will be raised when trying to parse the response.

request[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.request "Link to this definition")
The request data that stimulated the response.

wsgi_request[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.wsgi_request "Link to this definition")
The `WSGIRequest` instance generated by the test handler that generated the response.

status_code[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.status_code "Link to this definition")
The HTTP status of the response, as an integer. For a full list of defined codes, see the [IANA status code registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml).

templates[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.templates "Link to this definition")
A list of `Template` instances used to render the final content, in the order they were rendered. For each template in the list, use `template.name` to get the template’s file name, if the template was loaded from a file. (The name is a string such as `'admin/index.html'`.)

Not using Django templates?

This attribute is only populated when using the [`DjangoTemplates`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") backend. If you’re using another template engine, [`template_name`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.template_name "django.template.response.SimpleTemplateResponse.template_name") may be a suitable alternative if you only need the name of the template used for rendering.

resolver_match[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.resolver_match "Link to this definition")
An instance of [`ResolverMatch`](https://docs.djangoproject.com/en/6.0/ref/urlresolvers/#django.urls.ResolverMatch "django.urls.ResolverMatch") for the response. You can use the [`func`](https://docs.djangoproject.com/en/6.0/ref/urlresolvers/#django.urls.ResolverMatch.func "django.urls.ResolverMatch.func") attribute, for example, to verify the view that served the response:

# my_view here is a function based view.
self.assertEqual(response.resolver_match.func, my_view)

# Class-based views need to compare the view_class, as the
# functions generated by as_view() won't be equal.
self.assertIs(response.resolver_match.func.view_class, MyView)

If the given URL is not found, accessing this attribute will raise a [`Resolver404`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.urls.Resolver404 "django.urls.Resolver404") exception.

As with a normal response, you can also access the headers through [`HttpResponse.headers`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse.headers "django.http.HttpResponse.headers"). For example, you could determine the content type of a response using `response.headers['Content-Type']`.

### Exceptions[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#exceptions "Link to this heading")

If you point the test client at a view that raises an exception and `Client.raise_request_exception` is `True`, that exception will be visible in the test case. You can then use a standard `try ... except` block or [`assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "(in Python v3.14)") to test for exceptions.

The only exceptions that are not visible to the test client are [`Http404`](https://docs.djangoproject.com/en/6.0/topics/http/views/#django.http.Http404 "django.http.Http404"), [`PermissionDenied`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied"), [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "(in Python v3.14)"), and [`SuspiciousOperation`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation"). Django catches these exceptions internally and converts them into the appropriate HTTP response codes. In these cases, you can check `response.status_code` in your test.

If `Client.raise_request_exception` is `False`, the test client will return a 500 response as would be returned to a browser. The response has the attribute [`exc_info`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response.exc_info "django.test.Response.exc_info") to provide information about the unhandled exception.

### Persistent state[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#persistent-state "Link to this heading")

The test client is stateful. If a response returns a cookie, then that cookie will be stored in the test client and sent with all subsequent `get()` and `post()` requests.

Expiration policies for these cookies are not followed. If you want a cookie to expire, either delete it manually or create a new `Client` instance (which will effectively delete all cookies).

A test client has attributes that store persistent state information. You can access these properties as part of a test condition.

Client.cookies[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.cookies "Link to this definition")
A Python [`SimpleCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.SimpleCookie "(in Python v3.14)") object, containing the current values of all the client cookies. See the documentation of the [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "(in Python v3.14)") module for more.

Client.session[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.session "Link to this definition")
A dictionary-like object containing session information. See the [session documentation](https://docs.djangoproject.com/en/6.0/topics/http/sessions/) for full details.

To modify the session and then save it, it must be stored in a variable first (because a new `SessionStore` is created every time this property is accessed):

def test_something(self):
    session = self.client.session
    session["somekey"] = "test"
    session.save()

Client.asession()[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.asession "Link to this definition")
This is similar to the [`session`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.session "django.test.Client.session") attribute but it works in async contexts.

### Setting the language[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#setting-the-language "Link to this heading")

When testing applications that support internationalization and localization, you might want to set the language for a test client request. The method for doing so depends on whether or not the [`LocaleMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.middleware.locale.LocaleMiddleware "django.middleware.locale.LocaleMiddleware") is enabled.

If the middleware is enabled, the language can be set by creating a cookie with a name of [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LANGUAGE_COOKIE_NAME) and a value of the language code:

from django.conf import settings

def test_language_using_cookie(self):
    self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: "fr"})
    response = self.client.get("/")
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

or by including the `Accept-Language` HTTP header in the request:

def test_language_using_header(self):
    response = self.client.get("/", headers={"accept-language": "fr"})
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

Note

When using these methods, ensure to reset the active language at the end of each test:

def tearDown(self):
    translation.activate(settings.LANGUAGE_CODE)

More details are in [How Django discovers language preference](https://docs.djangoproject.com/en/6.0/topics/i18n/translation/#how-django-discovers-language-preference).

If the middleware isn’t enabled, the active language may be set using [`translation.override()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.translation.override "django.utils.translation.override"):

from django.utils import translation

def test_language_using_override(self):
    with translation.override("fr"):
        response = self.client.get("/")
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

More details are in [Explicitly setting the active language](https://docs.djangoproject.com/en/6.0/topics/i18n/translation/#explicitly-setting-the-active-language).

### Example[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#example "Link to this heading")

The following is a unit test using the test client:

import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get("/customer/details/")

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context["customers"]), 5)

Provided test case classes[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#provided-test-case-classes "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Normal Python unit test classes extend a base class of [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.14)"). Django provides a few extensions of this base class:

[![Image 1: Hierarchy of Django unit testing classes (TestCase subclasses)](https://docs.djangoproject.com/en/6.0/_images/django_unittest_classes_hierarchy.svg)](https://docs.djangoproject.com/en/6.0/_images/django_unittest_classes_hierarchy.svg)

Hierarchy of Django unit testing classes[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#id4 "Link to this image")

You can convert a normal [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.14)") to any of the subclasses: change the base class of your test from `unittest.TestCase` to the subclass. All of the standard Python unit test functionality will be available, and it will be augmented with some useful additions as described in each section below.

### `SimpleTestCase`[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#simpletestcase "Link to this heading")

_class_ SimpleTestCase[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L195)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase "Link to this definition")
A subclass of [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.14)") that adds this functionality:

*   Some useful assertions like:

    *   Checking that a callable [`raises a certain exception`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "django.test.SimpleTestCase.assertRaisesMessage").

    *   Checking that a callable [`triggers a certain warning`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertWarnsMessage "django.test.SimpleTestCase.assertWarnsMessage").

    *   Testing form field [`rendering and error treatment`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertFieldOutput "django.test.SimpleTestCase.assertFieldOutput").

    *   Testing [`HTML responses for the presence/lack of a given fragment`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertContains "django.test.SimpleTestCase.assertContains").

    *   Verifying that a template [``` has/hasn't been used to generate a given response content ```](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "django.test.SimpleTestCase.assertTemplateUsed").

    *   Verifying that two [`URLs`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertURLEqual "django.test.SimpleTestCase.assertURLEqual") are equal.

    *   Verifying an HTTP [`redirect`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertRedirects "django.test.SimpleTestCase.assertRedirects") is performed by the app.

    *   Robustly testing two [`HTML fragments`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for equality/inequality or [`containment`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertInHTML "django.test.SimpleTestCase.assertInHTML").

    *   Robustly testing two [`XML fragments`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "django.test.SimpleTestCase.assertXMLEqual") for equality/inequality.

    *   Robustly testing two [`JSON fragments`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "django.test.SimpleTestCase.assertJSONEqual") for equality.

*   The ability to run tests with [modified settings](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#overriding-settings).

*   Using the [`client`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.client "django.test.SimpleTestCase.client")[`Client`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client "django.test.Client").

If your tests make any database queries, use subclasses [`TransactionTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") or [`TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase").

SimpleTestCase.databases[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.databases "Link to this definition")
[`SimpleTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase") disallows database queries by default. This helps to avoid executing write queries which will affect other tests since each `SimpleTestCase` test isn’t run in a transaction. If you aren’t concerned about this problem, you can disable this behavior by setting the `databases` class attribute to `'__all__'` on your test class.

Warning

`SimpleTestCase` and its subclasses (e.g. `TestCase`, …) rely on `setUpClass()` and `tearDownClass()` to perform some class-wide initialization (e.g. overriding settings). If you need to override those methods, don’t forget to call the `super` implementation:

class MyTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        ...

    @classmethod
    def tearDownClass(cls):
        ...
        super().tearDownClass()

Be sure to account for Python’s behavior if an exception is raised during `setUpClass()`. If that happens, neither the tests in the class nor `tearDownClass()` are run. In the case of [`django.test.TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase"), this will leak the transaction created in `super()` which results in various symptoms including a segmentation fault on some platforms (reported on macOS). If you want to intentionally raise an exception such as [`unittest.SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "(in Python v3.14)") in `setUpClass()`, be sure to do it before calling `super()` to avoid this.

### `TransactionTestCase`[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#transactiontestcase "Link to this heading")

_class_ TransactionTestCase[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1103)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "Link to this definition")
`TransactionTestCase` inherits from [`SimpleTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase") to add some database-specific features:

*   Resetting the database to a known state at the end of each test to ease testing and using the ORM.

*   Database [`fixtures`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "django.test.TransactionTestCase.fixtures").

*   Test [skipping based on database backend features](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#skipping-tests).

*   The remaining specialized [`assert*`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerySetEqual "django.test.TransactionTestCase.assertQuerySetEqual") methods.

Django’s [`TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") class is a more commonly used subclass of `TransactionTestCase` that makes use of database transaction facilities to speed up the process of resetting the database to a known state at the end of each test. A consequence of this, however, is that some database behaviors cannot be tested within a Django `TestCase` class. For instance, you cannot test that a block of code is executing within a transaction, as is required when using [`select_for_update()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.select_for_update "django.db.models.query.QuerySet.select_for_update"). In those cases, you should use `TransactionTestCase`.

`TransactionTestCase` and `TestCase` are identical except for the manner in which the database is reset to a known state and the ability for test code to test the effects of commit and rollback:

*   A `TransactionTestCase` resets the database after the test runs by truncating all tables. A `TransactionTestCase` may call commit and rollback and observe the effects of these calls on the database.

*   A `TestCase`, on the other hand, does not truncate tables after a test. Instead, it encloses the test code in a database transaction that is rolled back at the end of the test. This guarantees that the rollback at the end of the test restores the database to its initial state.

Warning

`TestCase` running on a database that does not support rollback (e.g. MySQL with the MyISAM storage engine), and all instances of `TransactionTestCase`, will roll back at the end of the test by deleting all data from the test database.

Apps [will not see their data reloaded](https://docs.djangoproject.com/en/6.0/topics/testing/overview/#test-case-serialized-rollback); if you need this functionality (for example, third-party apps should enable this) you can set `serialized_rollback = True` inside the `TestCase` body.

### `TestCase`[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#testcase "Link to this heading")

_class_ TestCase[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1375)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "Link to this definition")
This is the most common class to use for writing tests in Django. It inherits from [`TransactionTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") (and by extension [`SimpleTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase")). If your Django application doesn’t use a database, use [`SimpleTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase").

The class:

*   Wraps the tests within two nested [`atomic()`](https://docs.djangoproject.com/en/6.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") blocks: one for the whole class and one for each test. Therefore, if you want to test some specific database transaction behavior, use [`TransactionTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase").

*   Checks deferrable database constraints at the end of each test.

It also provides an additional method:

_classmethod_ TestCase.setUpTestData()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1459)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase.setUpTestData "Link to this definition")
The class-level `atomic` block described above allows the creation of initial data at the class level, once for the whole `TestCase`. This technique allows for faster tests as compared to using `setUp()`.

For example:

from django.test import TestCase

class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.foo = Foo.objects.create(bar="Test")
        ...

    def test1(self):
        # Some test using self.foo
        ...

    def test2(self):
        # Some other test using self.foo
        ...

Note that if the tests are run on a database with no transaction support (for instance, MySQL with the MyISAM engine), `setUpTestData()` will be called before each test, negating the speed benefits.

Objects assigned to class attributes in `setUpTestData()` must support creating deep copies with [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "(in Python v3.14)") in order to isolate them from alterations performed by each test methods.

_classmethod_ TestCase.captureOnCommitCallbacks(_using=DEFAULT\_DB\_ALIAS_, _execute=False_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1508)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase.captureOnCommitCallbacks "Link to this definition")
Returns a context manager that captures [`transaction.on_commit()`](https://docs.djangoproject.com/en/6.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") callbacks for the given database connection. It returns a list that contains, on exit of the context, the captured callback functions. From this list you can make assertions on the callbacks or call them to invoke their side effects, emulating a commit.

`using` is the alias of the database connection to capture callbacks for.

If `execute` is `True`, all the callbacks will be called as the context manager exits, if no exception occurred. This emulates a commit after the wrapped block of code.

For example:

from django.core import mail
from django.test import TestCase

class ContactTests(TestCase):
    def test_post(self):
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/contact/",
                {"message": "I like your site"},
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(callbacks), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Contact Form")
        self.assertEqual(mail.outbox[0].body, "I like your site")

### `LiveServerTestCase`[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#liveservertestcase "Link to this heading")

_class_ LiveServerTestCase[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1790)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.LiveServerTestCase "Link to this definition")
`LiveServerTestCase` does basically the same as [`TransactionTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") with one extra feature: it launches a live Django server in the background on setup, and shuts it down on teardown. This allows the use of automated test clients other than the [Django dummy client](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#test-client) such as, for example, the [Selenium](https://www.selenium.dev/) client, to execute a series of functional tests inside a browser and simulate a real user’s actions.

The live server listens on `localhost` and binds to port 0 which uses a free port assigned by the operating system. The server’s URL can be accessed with `self.live_server_url` during the tests.

To demonstrate how to use `LiveServerTestCase`, let’s write a Selenium test. First of all, you need to install the [selenium](https://pypi.org/project/selenium/) package:

/ 

$ python -m pip install "selenium >= 4.23.0"

...\> py -m pip install "selenium >= 4.23.0"

Then, add a `LiveServerTestCase`-based test to your app’s tests module (for example: `myapp/tests.py`). For this example, we’ll assume you’re using the [`staticfiles`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") app and want to have static files served during the execution of your tests similar to what we get at development time with `DEBUG=True`, i.e. without having to collect them using [`collectstatic`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django-admin-collectstatic). We’ll use the [`StaticLiveServerTestCase`](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/#django.contrib.staticfiles.testing.StaticLiveServerTestCase "django.contrib.staticfiles.testing.StaticLiveServerTestCase") subclass which provides that functionality. Replace it with `django.test.LiveServerTestCase` if you don’t need that.

The code for this test may look as follows:

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["user-data.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("myuser")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("secret")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

Finally, you may run the test as follows:

/ 

$ ./manage.py test myapp.tests.MySeleniumTests.test_login

...\> manage.py test myapp.tests.MySeleniumTests.test_login

This example will automatically open Firefox then go to the login page, enter the credentials and press the “Log in” button. Selenium offers other drivers in case you do not have Firefox installed or wish to use another browser. The example above is just a tiny fraction of what the Selenium client can do; check out the [full reference](https://selenium-python.readthedocs.io/api.html) for more details.

Note

When using an in-memory SQLite database to run the tests, the same database connection will be shared by two threads in parallel: the thread in which the live server is run and the thread in which the test case is run. It’s important to prevent simultaneous database queries via this shared connection by the two threads, as that may sometimes randomly cause the tests to fail. So you need to ensure that the two threads don’t access the database at the same time. In particular, this means that in some cases (for example, just after clicking a link or submitting a form), you might need to check that a response is received by Selenium and that the next page is loaded before proceeding with further test execution. Do this, for example, by making Selenium wait until the `<body>` HTML tag is found in the response (requires Selenium > 2.13):

def test_login(self):
    from selenium.webdriver.support.wait import WebDriverWait

    timeout = 2
    ...
    self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()
    # Wait until the response is received
    WebDriverWait(self.selenium, timeout).until(
        lambda driver: driver.find_element(By.TAG_NAME, "body")
    )

The tricky thing here is that there’s really no such thing as a “page load,” especially in modern web apps that generate HTML dynamically after the server generates the initial document. So, checking for the presence of `<body>` in the response might not necessarily be appropriate for all use cases. Please refer to the [Selenium FAQ](https://web.archive.org/web/20160129132110/http://code.google.com/p/selenium/wiki/FrequentlyAskedQuestions#Q:_WebDriver_fails_to_find_elements_/_Does_not_block_on_page_loa) and [Selenium documentation](https://www.selenium.dev/documentation/webdriver/waits/#explicit-waits) for more information.

Test cases features[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#test-cases-features "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

### Default test client[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#default-test-client "Link to this heading")

SimpleTestCase.client[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.client "Link to this definition")
Every test case in a `django.test.*TestCase` instance has access to an instance of a Django test client. This client can be accessed as `self.client`. This client is recreated for each test, so you don’t have to worry about state (such as cookies) carrying over from one test to another.

This means, instead of instantiating a `Client` in each test:

import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get("/customer/details/")
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        client = Client()
        response = client.get("/customer/index/")
        self.assertEqual(response.status_code, 200)

…you can refer to `self.client`, like so:

from django.test import TestCase

class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get("/customer/details/")
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get("/customer/index/")
        self.assertEqual(response.status_code, 200)

### Customizing the test client[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#customizing-the-test-client "Link to this heading")

SimpleTestCase.client_class[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.client_class "Link to this definition")
If you want to use a different `Client` class (for example, a subclass with customized behavior), use the [`client_class`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.client_class "django.test.SimpleTestCase.client_class") class attribute:

from django.test import Client, TestCase

class MyTestClient(Client):
    # Specialized methods for your environment
    ...

class MyTest(TestCase):
    client_class = MyTestClient

    def test_my_stuff(self):
        # Here self.client is an instance of MyTestClient...
        call_some_test_code()

### Fixture loading[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#fixture-loading "Link to this heading")

TransactionTestCase.fixtures[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "Link to this definition")
A test case class for a database-backed website isn’t much use if there isn’t any data in the database. Tests are more readable and it’s more maintainable to create objects using the ORM, for example in [`TestCase.setUpTestData()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase.setUpTestData "django.test.TestCase.setUpTestData"), however, you can also use [fixtures](https://docs.djangoproject.com/en/6.0/topics/db/fixtures/#fixtures-explanation).

A fixture is a collection of data that Django knows how to import into a database. For example, if your site has user accounts, you might set up a fixture of fake user accounts in order to populate your database during tests.

The most straightforward way of creating a fixture is to use the [`manage.py dumpdata`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-dumpdata) command. This assumes you already have some data in your database. See the [``` dumpdata documentation ```](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-dumpdata) for more details.

Once you’ve created a fixture and placed it in a `fixtures` directory in one of your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS), you can use it in your unit tests by specifying a `fixtures` class attribute on your [`django.test.TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") subclass:

from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    fixtures = ["mammals.json", "birds"]

    def setUp(self):
        # Test definitions as before.
        call_setup_methods()

    def test_fluffy_animals(self):
        # A test that uses the fixtures.
        call_some_test_code()

Here’s specifically what will happen:

*   During `setUpClass()`, all the named fixtures are installed. In this example, Django will install any JSON fixture named `mammals`, followed by any fixture named `birds`. See the [Fixtures](https://docs.djangoproject.com/en/6.0/topics/db/fixtures/#fixtures-explanation) topic for more details on defining and installing fixtures.

For most unit tests using [`TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase"), Django doesn’t need to do anything else, because transactions are used to clean the database after each test for performance reasons. But for [`TransactionTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase"), the following actions will take place:

*   At the end of each test Django will flush the database, returning the database to the state it was in directly after [`migrate`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-migrate) was called.

*   For each subsequent test, the fixtures will be reloaded before `setUp()` is run.

In any case, you can be certain that the outcome of a test will not be affected by another test or by the order of test execution.

By default, fixtures are only loaded into the `default` database. If you are using multiple databases and set [`TransactionTestCase.databases`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.databases "django.test.TransactionTestCase.databases"), fixtures will be loaded into all specified databases.

Changed in Django 5.2:

For [`TransactionTestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase"), fixtures were made available during `setUpClass()`.

### URLconf configuration[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#urlconf-configuration "Link to this heading")

If your application provides views, you may want to include tests that use the test client to exercise those views. However, an end user is free to deploy the views in your application at any URL of their choosing. This means that your tests can’t rely upon the fact that your views will be available at a particular URL. Decorate your test class or test method with `@override_settings(ROOT_URLCONF=...)` for URLconf configuration.

### Multi-database support[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#multi-database-support "Link to this heading")

TransactionTestCase.databases[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.databases "Link to this definition")
Django sets up a test database corresponding to every database that is defined in the [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) definition in your settings and referred to by at least one test through `databases`.

However, a big part of the time taken to run a Django `TestCase` is consumed by the call to `flush` that ensures that you have a clean database at the end of each test run. If you have multiple databases, multiple flushes are required (one for each database), which can be a time consuming activity – especially if your tests don’t need to test multi-database activity.

As an optimization, Django only flushes the `default` database at the end of each test run. If your setup contains multiple databases, and you have a test that requires every database to be clean, you can use the `databases` attribute on the test suite to request extra databases to be flushed.

For example:

class TestMyViews(TransactionTestCase):
    databases = {"default", "other"}

    def test_index_page_view(self):
        call_some_test_code()

This test case class will flush the `default` and `other` test databases after running `test_index_page_view`. You can also use `'__all__'` to specify that all of the test databases must be flushed.

The `databases` flag also controls which databases the [`TransactionTestCase.fixtures`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "django.test.TransactionTestCase.fixtures") are loaded into. By default, fixtures are only loaded into the `default` database.

Queries against databases not in `databases` will give assertion errors to prevent state leaking between tests.

TestCase.databases[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase.databases "Link to this definition")
By default, only the `default` database will be wrapped in a transaction during a `TestCase`’s execution and attempts to query other databases will result in assertion errors to prevent state leaking between tests.

Use the `databases` class attribute on the test class to request transaction wrapping against non-`default` databases.

For example:

class OtherDBTests(TestCase):
    databases = {"other"}

    def test_other_db_query(self): ...

This test will only allow queries against the `other` database. Just like for [`SimpleTestCase.databases`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.databases "django.test.SimpleTestCase.databases") and [`TransactionTestCase.databases`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.databases "django.test.TransactionTestCase.databases"), the `'__all__'` constant can be used to specify that the test should allow queries to all databases.

### Overriding settings[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#overriding-settings "Link to this heading")

Warning

Use the functions below to temporarily alter the value of settings in tests. Don’t manipulate `django.conf.settings` directly as Django won’t restore the original values after such manipulations.

SimpleTestCase.settings()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L393)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.settings "Link to this definition")
For testing purposes it’s often useful to change a setting temporarily and revert to the original value after running the testing code. For this use case Django provides a standard Python context manager (see [**PEP 343**](https://peps.python.org/pep-0343/)) called [`settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.settings "django.test.SimpleTestCase.settings"), which can be used like this:

from django.test import TestCase

class LoginTestCase(TestCase):
    def test_login(self):
        # First check for the default behavior
        response = self.client.get("/sekrit/")
        self.assertRedirects(response, "/accounts/login/?next=/sekrit/")

        # Then override the LOGIN_URL setting
        with self.settings(LOGIN_URL="/other/login/"):
            response = self.client.get("/sekrit/")
            self.assertRedirects(response, "/other/login/?next=/sekrit/")

This example will override the [`LOGIN_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-LOGIN_URL) setting for the code in the `with` block and reset its value to the previous state afterward.

SimpleTestCase.modify_settings()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L400)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.modify_settings "Link to this definition")
It can prove unwieldy to redefine settings that contain a list of values. In practice, adding or removing values is often sufficient. Django provides the [`modify_settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.modify_settings "django.test.SimpleTestCase.modify_settings") context manager for easier settings changes:

from django.test import TestCase

class MiddlewareTestCase(TestCase):
    def test_cache_middleware(self):
        with self.modify_settings(
            MIDDLEWARE={
                "append": "django.middleware.cache.FetchFromCacheMiddleware",
                "prepend": "django.middleware.cache.UpdateCacheMiddleware",
                "remove": [
                    "django.contrib.sessions.middleware.SessionMiddleware",
                    "django.contrib.auth.middleware.AuthenticationMiddleware",
                    "django.contrib.messages.middleware.MessageMiddleware",
                ],
            }
        ):
            response = self.client.get("/")
            # ...

For each action, you can supply either a list of values or a string. When the value already exists in the list, `append` and `prepend` have no effect; neither does `remove` when the value doesn’t exist.

override_settings(_**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/utils.py#L470)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.override_settings "Link to this definition")
In case you want to override a setting for a test method, Django provides the [`override_settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.override_settings "django.test.override_settings") decorator (see [**PEP 318**](https://peps.python.org/pep-0318/)). It’s used like this:

from django.test import TestCase, override_settings

class LoginTestCase(TestCase):
    @override_settings(LOGIN_URL="/other/login/")
    def test_login(self):
        response = self.client.get("/sekrit/")
        self.assertRedirects(response, "/other/login/?next=/sekrit/")

The decorator can also be applied to [`TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") classes:

from django.test import TestCase, override_settings

@override_settings(LOGIN_URL="/other/login/")
class LoginTestCase(TestCase):
    def test_login(self):
        response = self.client.get("/sekrit/")
        self.assertRedirects(response, "/other/login/?next=/sekrit/")

modify_settings(_*args_, _**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/utils.py#L555)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.modify_settings "Link to this definition")
Likewise, Django provides the [`modify_settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") decorator:

from django.test import TestCase, modify_settings

class MiddlewareTestCase(TestCase):
    @modify_settings(
        MIDDLEWARE={
            "append": "django.middleware.cache.FetchFromCacheMiddleware",
            "prepend": "django.middleware.cache.UpdateCacheMiddleware",
        }
    )
    def test_cache_middleware(self):
        response = self.client.get("/")
        # ...

The decorator can also be applied to test case classes:

from django.test import TestCase, modify_settings

@modify_settings(
    MIDDLEWARE={
        "append": "django.middleware.cache.FetchFromCacheMiddleware",
        "prepend": "django.middleware.cache.UpdateCacheMiddleware",
    }
)
class MiddlewareTestCase(TestCase):
    def test_cache_middleware(self):
        response = self.client.get("/")
        # ...

Note

When given a class, these decorators modify the class directly and return it; they don’t create and return a modified copy of it. So if you try to tweak the above examples to assign the return value to a different name than `LoginTestCase` or `MiddlewareTestCase`, you may be surprised to find that the original test case classes are still equally affected by the decorator. For a given class, [`modify_settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") is always applied after [`override_settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.override_settings "django.test.override_settings").

Warning

The settings file contains some settings that are only consulted during initialization of Django internals. If you change them with `override_settings`, the setting is changed if you access it via the `django.conf.settings` module, however, Django’s internals access it differently. Effectively, using [`override_settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.override_settings "django.test.override_settings") or [`modify_settings()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") with these settings is probably not going to do what you expect it to do.

We do not recommend altering the [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) setting. Altering the [`CACHES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHES) setting is possible, but a bit tricky if you are using internals that make using of caching, like [`django.contrib.sessions`](https://docs.djangoproject.com/en/6.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects."). For example, you will have to reinitialize the session backend in a test that uses cached sessions and overrides [`CACHES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-CACHES).

Finally, avoid aliasing your settings as module-level constants as `override_settings()` won’t work on such values since they are only evaluated the first time the module is imported.

You can also simulate the absence of a setting by deleting it after settings have been overridden, like this:

@override_settings()
def test_something(self):
    del settings.LOGIN_URL
    ...

When overriding settings, make sure to handle the cases in which your app’s code uses a cache or similar feature that retains state even if the setting is changed. Django provides the [`django.test.signals.setting_changed`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.test.signals.setting_changed "django.test.signals.setting_changed") signal that lets you register callbacks to clean up and otherwise reset state when settings are changed.

Django itself uses this signal to reset various data:

| Overridden settings | Data reset |
| --- | --- |
| USE_TZ, TIME_ZONE | Databases timezone |
| TEMPLATES | Template engines |
| FORM_RENDERER | Default renderer |
| SERIALIZATION_MODULES | Serializers cache |
| LOCALE_PATHS, LANGUAGE_CODE | Default translation and loaded translations |
| STATIC_ROOT, STATIC_URL, STORAGES | Storages configuration |

### Isolating apps[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#isolating-apps "Link to this heading")

utils.isolate_apps(_*app\_labels_, _attr\_name=None_, _kwarg\_name=None_)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.utils.isolate_apps "Link to this definition")
Registers the models defined within a wrapped context into their own isolated [`apps`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.apps "django.apps.apps") registry. This functionality is useful when creating model classes for tests, as the classes will be cleanly deleted afterward, and there is no risk of name collisions.

The app labels which the isolated registry should contain must be passed as individual arguments. You can use `isolate_apps()` as a decorator or a context manager. For example:

from django.db import models
from django.test import SimpleTestCase
from django.test.utils import isolate_apps

class MyModelTests(SimpleTestCase):
    @isolate_apps("app_label")
    def test_model_definition(self):
        class TestModel(models.Model):
            pass

        ...

… or:

with isolate_apps("app_label"):

    class TestModel(models.Model):
        pass

    ...

The decorator form can also be applied to classes.

Two optional keyword arguments can be specified:

*   `attr_name`: attribute assigned the isolated registry if used as a class decorator.

*   `kwarg_name`: keyword argument passing the isolated registry if used as a function decorator.

The temporary `Apps` instance used to isolate model registration can be retrieved as an attribute when used as a class decorator by using the `attr_name` parameter:

@isolate_apps("app_label", attr_name="apps")
class TestModelDefinition(SimpleTestCase):
    def test_model_definition(self):
        class TestModel(models.Model):
            pass

        self.assertIs(self.apps.get_model("app_label", "TestModel"), TestModel)

… or alternatively as an argument on the test method when used as a method decorator by using the `kwarg_name` parameter:

class TestModelDefinition(SimpleTestCase):
    @isolate_apps("app_label", kwarg_name="apps")
    def test_model_definition(self, apps):
        class TestModel(models.Model):
            pass

        self.assertIs(apps.get_model("app_label", "TestModel"), TestModel)

### Emptying the test outbox[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#emptying-the-test-outbox "Link to this heading")

If you use any of Django’s custom `TestCase` classes, the test runner will clear the contents of the test email outbox at the start of each test case.

For more detail on email services during tests, see [Email services](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#email-services) below.

### Assertions[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#assertions "Link to this heading")

As Python’s normal [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "(in Python v3.14)") class implements assertion methods such as [`assertTrue()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "(in Python v3.14)") and [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "(in Python v3.14)"), Django’s custom [`TestCase`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") class provides a number of custom assertion methods that are useful for testing web applications:

The failure messages given by most of these assertion methods can be customized with the `msg_prefix` argument. This string will be prefixed to any failure message generated by the assertion. This allows you to provide additional details that may help you to identify the location and cause of a failure in your test suite.

SimpleTestCase.assertRaisesMessage(_expected\_exception_, _expected\_message_, _callable_, _*args_, _**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L863)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "Link to this definition")SimpleTestCase.assertRaisesMessage(_expected\_exception_, _expected\_message_)
Asserts that execution of `callable` raises `expected_exception` and that `expected_message` is found in the exception’s message. Any other outcome is reported as a failure. It’s a simpler version of [`unittest.TestCase.assertRaisesRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "(in Python v3.14)") with the difference that `expected_message` isn’t treated as a regular expression.

If only the `expected_exception` and `expected_message` parameters are given, returns a context manager so that the code being tested can be written inline rather than as a function:

with self.assertRaisesMessage(ValueError, "invalid literal for int()"):
    int("a")

SimpleTestCase.assertWarnsMessage(_expected\_warning_, _expected\_message_, _callable_, _*args_, _**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L885)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertWarnsMessage "Link to this definition")SimpleTestCase.assertWarnsMessage(_expected\_warning_, _expected\_message_)
Analogous to [`SimpleTestCase.assertRaisesMessage()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "django.test.SimpleTestCase.assertRaisesMessage") but for [`assertWarnsRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "(in Python v3.14)") instead of [`assertRaisesRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "(in Python v3.14)").

SimpleTestCase.assertFieldOutput(_fieldclass_, _valid_, _invalid_, _field\_args=None_, _field\_kwargs=None_, _empty\_value=''_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L899)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertFieldOutput "Link to this definition")
Asserts that a form field behaves correctly with various inputs.

Parameters:
*   **fieldclass** – the class of the field to be tested.

*   **valid** – a dictionary mapping valid inputs to their expected cleaned values.

*   **invalid** – a dictionary mapping invalid inputs to one or more raised error messages.

*   **field_args** – the args passed to instantiate the field.

*   **field_kwargs** – the kwargs passed to instantiate the field.

*   **empty_value** – the expected clean output for inputs in `empty_values`.

For example, the following code tests that an `EmailField` accepts `a@a.com` as a valid email address, but rejects `aaa` with a reasonable error message:

self.assertFieldOutput(
    EmailField, {"a@a.com": "a@a.com"}, {"aaa": ["Enter a valid email address."]}
)

SimpleTestCase.assertFormError(_form_, _field_, _errors_, _msg\_prefix=''_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L695)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertFormError "Link to this definition")
Asserts that a field on a form raises the provided list of errors.

`form` is a `Form` instance. The form must be [bound](https://docs.djangoproject.com/en/6.0/ref/forms/api/#ref-forms-api-bound-unbound) but not necessarily validated (`assertFormError()` will automatically call `full_clean()` on the form).

`field` is the name of the field on the form to check. To check the form’s [`non-field errors`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.non_field_errors "django.forms.Form.non_field_errors"), use `field=None`.

`errors` is a list of all the error strings that the field is expected to have. You can also pass a single error string if you only expect one error which means that `errors='error message'` is the same as `errors=['error message']`.

SimpleTestCase.assertFormSetError(_formset_, _form\_index_, _field_, _errors_, _msg\_prefix=''_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L710)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertFormSetError "Link to this definition")
Asserts that the `formset` raises the provided list of errors when rendered.

`formset` is a `FormSet` instance. The formset must be bound but not necessarily validated (`assertFormSetError()` will automatically call the `full_clean()` on the formset).

`form_index` is the number of the form within the `FormSet` (starting from 0). Use `form_index=None` to check the formset’s non-form errors, i.e. the errors you get when calling `formset.non_form_errors()`. In that case you must also use `field=None`.

`field` and `errors` have the same meaning as the parameters to `assertFormError()`.

SimpleTestCase.assertContains(_response_, _text_, _count=None_, _status\_code=200_, _msg\_prefix=''_, _html=False_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L593)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertContains "Link to this definition")
Asserts that a [`response`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") produced the given [`status_code`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code") and that `text` appears in its [`content`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse.content "django.http.HttpResponse.content"). If `count` is provided, `text` must occur exactly `count` times in the response.

Set `html` to `True` to handle `text` as HTML. The comparison with the response content will be based on HTML semantics instead of character-by-character equality. Whitespace is ignored in most cases, attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

SimpleTestCase.assertNotContains(_response_, _text_, _status\_code=200_, _msg\_prefix=''_, _html=False_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L627)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertNotContains "Link to this definition")
Asserts that a [`response`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") produced the given [`status_code`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code") and that `text` does _not_ appear in its [`content`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse.content "django.http.HttpResponse.content").

Set `html` to `True` to handle `text` as HTML. The comparison with the response content will be based on HTML semantics instead of character-by-character equality. Whitespace is ignored in most cases, attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

SimpleTestCase.assertTemplateUsed(_response_, _template\_name_, _msg\_prefix=''_, _count=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L796)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "Link to this definition")
Asserts that the template with the given name was used in rendering the response.

`response` must be a response instance returned by the [`test client`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Response "django.test.Response").

`template_name` should be a string such as `'admin/index.html'`.

The `count` argument is an integer indicating the number of times the template should be rendered. Default is `None`, meaning that the template should be rendered one or more times.

You can use this as a context manager, like this:

with self.assertTemplateUsed("index.html"):
    render_to_string("index.html")
with self.assertTemplateUsed(template_name="index.html"):
    render_to_string("index.html")

SimpleTestCase.assertTemplateNotUsed(_response_, _template\_name_, _msg\_prefix=''_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L817)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateNotUsed "Link to this definition")
Asserts that the template with the given name was _not_ used in rendering the response.

You can use this as a context manager in the same way as [`assertTemplateUsed()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "django.test.SimpleTestCase.assertTemplateUsed").

SimpleTestCase.assertURLEqual(_url1_, _url2_, _msg\_prefix=''_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L526)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertURLEqual "Link to this definition")
Asserts that two URLs are the same, ignoring the order of query string parameters except for parameters with the same name. For example, `/path/?x=1&y=2` is equal to `/path/?y=2&x=1`, but `/path/?a=1&a=2` isn’t equal to `/path/?a=2&a=1`.

SimpleTestCase.assertRedirects(_response_, _expected\_url_, _status\_code=302_, _target\_status\_code=200_, _msg\_prefix=''_, _fetch\_redirect\_response=True_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L407)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertRedirects "Link to this definition")
Asserts that the [`response`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") returned a [`status_code`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code") redirect status, redirected to `expected_url` (including any `GET` data), and that the final page was received with `target_status_code`.

If your request used the `follow` argument, the `expected_url` and `target_status_code` will be the url and status code for the final point of the redirect chain.

If `fetch_redirect_response` is `False`, the final page won’t be loaded. Since the test client can’t fetch external URLs, this is particularly useful if `expected_url` isn’t part of your Django app.

Scheme is handled correctly when making comparisons between two URLs. If there isn’t any scheme specified in the location where we are redirected to, the original request’s scheme is used. If present, the scheme in `expected_url` is the one used to make the comparisons to.

SimpleTestCase.assertHTMLEqual(_html1_, _html2_, _msg=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L952)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "Link to this definition")
Asserts that the strings `html1` and `html2` are equal. The comparison is based on HTML semantics. The comparison takes following things into account:

*   Whitespace before and after HTML tags is ignored.

*   All types of whitespace are considered equivalent.

*   All open tags are closed implicitly, e.g. when a surrounding tag is closed or the HTML document ends.

*   Empty tags are equivalent to their self-closing version.

*   The ordering of attributes of an HTML element is not significant.

*   Boolean attributes (like `checked`) without an argument are equal to attributes that equal in name and value (see the examples).

*   Text, character references, and entity references that refer to the same character are equivalent.

The following examples are valid tests and don’t raise any `AssertionError`:

self.assertHTMLEqual(
    "<p>Hello <b>&#x27;world&#x27;!</p>",
 """<p>
 Hello <b>&#39;world&#39;! </b>
 </p>""",
)
self.assertHTMLEqual(
    '<input type="checkbox" checked="checked" id="id_accept_terms" />',
    '<input id="id_accept_terms" type="checkbox" checked>',
)

`html1` and `html2` must contain HTML. An `AssertionError` will be raised if one of them cannot be parsed.

Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertHTMLNotEqual(_html1_, _html2_, _msg=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L976)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLNotEqual "Link to this definition")
Asserts that the strings `html1` and `html2` are _not_ equal. The comparison is based on HTML semantics. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for details.

`html1` and `html2` must contain HTML. An `AssertionError` will be raised if one of them cannot be parsed.

Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertXMLEqual(_xml1_, _xml2_, _msg=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1060)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "Link to this definition")
Asserts that the strings `xml1` and `xml2` are equal. The comparison is based on XML semantics. Similarly to [`assertHTMLEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual"), the comparison is made on parsed content, hence only semantic differences are considered, not syntax differences. When invalid XML is passed in any parameter, an `AssertionError` is always raised, even if both strings are identical.

XML declaration, document type, processing instructions, and comments are ignored. Only the root element and its children are compared.

Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertXMLNotEqual(_xml1_, _xml2_, _msg=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1083)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLNotEqual "Link to this definition")
Asserts that the strings `xml1` and `xml2` are _not_ equal. The comparison is based on XML semantics. See [`assertXMLEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "django.test.SimpleTestCase.assertXMLEqual") for details.

Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertInHTML(_needle_, _haystack_, _count=None_, _msg\_prefix=''_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L989)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertInHTML "Link to this definition")
Asserts that the HTML fragment `needle` is contained in the `haystack` once.

If the `count` integer argument is specified, then additionally the number of `needle` occurrences will be strictly verified.

Whitespace in most cases is ignored, and attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

SimpleTestCase.assertNotInHTML(_needle_, _haystack_, _msg\_prefix=''_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1023)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertNotInHTML "Link to this definition")
Asserts that the HTML fragment `needle` is _not_ contained in the `haystack`.

Whitespace in most cases is ignored, and attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

SimpleTestCase.assertJSONEqual(_raw_, _expected\_data_, _msg=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1026)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "Link to this definition")
Asserts that the JSON fragments `raw` and `expected_data` are equal. Usual JSON non-significant whitespace rules apply as the heavyweight is delegated to the [`json`](https://docs.python.org/3/library/json.html#module-json "(in Python v3.14)") library.

Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertJSONNotEqual(_raw_, _expected\_data_, _msg=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1043)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONNotEqual "Link to this definition")
Asserts that the JSON fragments `raw` and `expected_data` are _not_ equal. See [`assertJSONEqual()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "django.test.SimpleTestCase.assertJSONEqual") for further details.

Output in case of error can be customized with the `msg` argument.

TransactionTestCase.assertQuerySetEqual(_qs_, _values_, _transform=None_, _ordered=True_, _msg=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1285)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerySetEqual "Link to this definition")
Asserts that a queryset `qs` matches a particular iterable of values `values`.

If `transform` is provided, `values` is compared to a list produced by applying `transform` to each member of `qs`.

By default, the comparison is also ordering dependent. If `qs` doesn’t provide an implicit ordering, you can set the `ordered` parameter to `False`, which turns the comparison into a `collections.Counter` comparison. If the order is undefined (if the given `qs` isn’t ordered and the comparison is against more than one ordered value), a `ValueError` is raised.

Output in case of error can be customized with the `msg` argument.

TransactionTestCase.assertNumQueries(_num_, _func_, _*args_, _**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1301)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries "Link to this definition")
Asserts that when `func` is called with `*args` and `**kwargs` that `num` database queries are executed.

If a `"using"` key is present in `kwargs` it is used as the database alias for which to check the number of queries:

self.assertNumQueries(7, my_function, using="non_default_db")

If you wish to call a function with a `using` parameter you can do it by wrapping the call with a `lambda` to add an extra parameter:

self.assertNumQueries(7, lambda: my_function(using=7))

You can also use this as a context manager:

with self.assertNumQueries(2):
    Person.objects.create(name="Aaron")
    Person.objects.create(name="Daniel")

### Tagging tests[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#tagging-tests "Link to this heading")

You can tag your tests so you can easily run a particular subset. For example, you might label fast or slow tests:

from django.test import tag

class SampleTestCase(TestCase):
    @tag("fast")
    def test_fast(self): ...

    @tag("slow")
    def test_slow(self): ...

    @tag("slow", "core")
    def test_slow_but_core(self): ...

You can also tag a test case class:

@tag("slow", "core")
class SampleTestCase(TestCase): ...

Subclasses inherit tags from superclasses, and methods inherit tags from their class. Given:

@tag("foo")
class SampleTestCaseChild(SampleTestCase):
    @tag("bar")
    def test(self): ...

`SampleTestCaseChild.test` will be labeled with `'slow'`, `'core'`, `'bar'`, and `'foo'`.

Then you can choose which tests to run. For example, to run only fast tests:

/ 

$ ./manage.py test --tag=fast

...\> manage.py test --tag=fast

Or to run fast tests and the core one (even though it’s slow):

/ 

$ ./manage.py test --tag=fast --tag=core

...\> manage.py test --tag=fast --tag=core

You can also exclude tests by tag. To run core tests if they are not slow:

/ 

$ ./manage.py test --tag=core --exclude-tag=slow

...\> manage.py test --tag=core --exclude-tag=slow

[`test --exclude-tag`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#cmdoption-test-exclude-tag) has precedence over [`test --tag`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#cmdoption-test-tag), so if a test has two tags and you select one of them and exclude the other, the test won’t be run.

Testing asynchronous code[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#testing-asynchronous-code "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

If you merely want to test the output of your asynchronous views, the standard test client will run them inside their own asynchronous loop without any extra work needed on your part.

However, if you want to write fully-asynchronous tests for a Django project, you will need to take several things into account.

Firstly, your tests must be `async def` methods on the test class (in order to give them an asynchronous context). Django will automatically detect any `async def` tests and wrap them so they run in their own event loop.

If you are testing from an asynchronous function, you must also use the asynchronous test client. This is available as `django.test.AsyncClient`, or as `self.async_client` on any test.

_class_ AsyncClient(_enforce\_csrf\_checks=False_, _raise\_request\_exception=True_, _*_, _headers=None_, _query\_params=None_, _**defaults_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/client.py#L1397)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.AsyncClient "Link to this definition")
`AsyncClient` has the same methods and signatures as the synchronous (normal) test client, with the following exceptions:

*   In the initialization, arbitrary keyword arguments in `defaults` are added directly into the ASGI scope.

*   Headers passed as `extra` keyword arguments should not have the `HTTP_` prefix required by the synchronous client (see [`Client.get()`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get")). For example, here is how to set an HTTP `Accept` header:

>>> c = AsyncClient()
>>> c.get("/customers/details/", {"name": "fred", "age": 7}, ACCEPT="application/json") 

Using `AsyncClient` any method that makes a request must be awaited:

async def test_my_thing(self):
    response = await self.async_client.get("/some-url/")
    self.assertEqual(response.status_code, 200)

The asynchronous client can also call synchronous views; it runs through Django’s [asynchronous request path](https://docs.djangoproject.com/en/6.0/topics/async/), which supports both. Any view called through the `AsyncClient` will get an `ASGIRequest` object for its `request` rather than the `WSGIRequest` that the normal client creates.

Warning

If you are using test decorators, they must be async-compatible to ensure they work correctly. Django’s built-in decorators will behave correctly, but third-party ones may appear to not execute (they will “wrap” the wrong part of the execution flow and not your test).

If you need to use these decorators, then you should decorate your test methods with [`async_to_sync()`](https://docs.djangoproject.com/en/6.0/topics/async/#asgiref.sync.async_to_sync "asgiref.sync.async_to_sync")_inside_ of them instead:

from asgiref.sync import async_to_sync
from django.test import TestCase

class MyTests(TestCase):
    @mock.patch(...)
    @async_to_sync
    async def test_my_thing(self): ...

Email services[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#email-services "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

If any of your Django views send email using [Django’s email functionality](https://docs.djangoproject.com/en/6.0/topics/email/), you probably don’t want to send email each time you run a test using that view. For this reason, Django’s test runner automatically redirects all Django-sent email to a dummy outbox. This lets you test every aspect of sending email – from the number of messages sent to the contents of each message – without actually sending the messages.

The test runner accomplishes this by transparently replacing the normal email backend with a testing backend. (Don’t worry – this has no effect on any other email senders outside of Django, such as your machine’s mail server, if you’re running one.)

django.core.mail.outbox[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.core.mail.django.core.mail.outbox "Link to this definition")
During test running, each outgoing email is saved in `django.core.mail.outbox`. This is a list of all [`EmailMessage`](https://docs.djangoproject.com/en/6.0/topics/email/#django.core.mail.EmailMessage "django.core.mail.EmailMessage") instances that have been sent. The `outbox` attribute is a special attribute that is created _only_ when the `locmem` email backend is used. It doesn’t normally exist as part of the [`django.core.mail`](https://docs.djangoproject.com/en/6.0/topics/email/#module-django.core.mail "django.core.mail: Helpers to easily send email.") module and you can’t import it directly. The code below shows how to access this attribute correctly.

Here’s an example test that examines `django.core.mail.outbox` for length and contents:

from django.core import mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, "Subject here")

As noted [previously](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#emptying-test-outbox), the test outbox is emptied at the start of every test in a Django `*TestCase`. To empty the outbox manually, assign the empty list to `mail.outbox`:

from django.core import mail

# Empty the test outbox
mail.outbox = []

Management Commands[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#management-commands "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

Management commands can be tested with the [`call_command()`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django.core.management.call_command "django.core.management.call_command") function. The output can be redirected into a `StringIO` instance:

from io import StringIO
from django.core.management import call_command
from django.test import TestCase

class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command("closepoll", poll_ids=[1], stdout=out)
        self.assertIn('Successfully closed poll "1"', out.getvalue())

Skipping tests[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#skipping-tests "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

The unittest library provides the [`@skipIf`](https://docs.python.org/3/library/unittest.html#unittest.skipIf "(in Python v3.14)") and [`@skipUnless`](https://docs.python.org/3/library/unittest.html#unittest.skipUnless "(in Python v3.14)") decorators to allow you to skip tests if you know ahead of time that those tests are going to fail under certain conditions.

For example, if your test requires a particular optional library in order to succeed, you could decorate the test case with [`@skipIf`](https://docs.python.org/3/library/unittest.html#unittest.skipIf "(in Python v3.14)"). Then, the test runner will report that the test wasn’t executed and why, instead of failing the test or omitting the test altogether.

To supplement these test skipping behaviors, Django provides two additional skip decorators. Instead of testing a generic boolean, these decorators check the capabilities of the database, and skip the test if the database doesn’t support a specific named feature.

The decorators use a string identifier to describe database features. This string corresponds to attributes of the database connection features class. See [django.db.backends.base.features.BaseDatabaseFeatures class](https://github.com/django/django/blob/main/django/db/backends/base/features.py) for a full list of database features that can be used as a basis for skipping tests.

skipIfDBFeature(_*feature\_name\_strings_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1620)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.skipIfDBFeature "Link to this definition")
Skip the decorated test or `TestCase` if all of the named database features are supported.

For example, the following test will not be executed if the database supports transactions (e.g., it would _not_ run under PostgreSQL, but it would under MySQL with MyISAM tables):

class MyTests(TestCase):
    @skipIfDBFeature("supports_transactions")
    def test_transaction_behavior(self):
        # ... conditional test code
        pass

skipUnlessDBFeature(_*feature\_name\_strings_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/test/testcases.py#L1629)[¶](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.skipUnlessDBFeature "Link to this definition")
Skip the decorated test or `TestCase` if any of the named database features are _not_ supported.

For example, the following test will only be executed if the database supports transactions (e.g., it would run under PostgreSQL, but _not_ under MySQL with MyISAM tables):

class MyTests(TestCase):
    @skipUnlessDBFeature("supports_transactions")
    def test_transaction_behavior(self):
        # ... conditional test code
        pass
