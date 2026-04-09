# Source: https://docs.djangoproject.com/en/6.0/ref/template-response/

Title: TemplateResponse and SimpleTemplateResponse | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/template-response/

Markdown Content:
Standard [`HttpResponse`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects are static structures. They are provided with a block of pre-rendered content at time of construction, and while that content can be modified, it isn’t in a form that makes it easy to perform modifications.

However, it can sometimes be beneficial to allow decorators or middleware to modify a response _after_ it has been constructed by the view. For example, you may want to change the template that is used, or put additional data into the context.

TemplateResponse provides a way to do just that. Unlike basic [`HttpResponse`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects, TemplateResponse objects retain the details of the template and context that was provided by the view to compute the response. The final output of the response is not computed until it is needed, later in the response process.

`SimpleTemplateResponse` objects[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#simpletemplateresponse-objects "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ SimpleTemplateResponse[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L10)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse "Link to this definition")
### Attributes[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#attributes "Link to this heading")

SimpleTemplateResponse.template_name[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.template_name "Link to this definition")
The name of the template to be rendered. Accepts a backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.

Example: `['foo.html', 'path/to/bar.html']`

SimpleTemplateResponse.context_data[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.context_data "Link to this definition")
The context data to be used when rendering the template. It must be a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)").

Example: `{'foo': 123}`

SimpleTemplateResponse.rendered_content[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L82)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.rendered_content "Link to this definition")
The current rendered value of the response content, using the current template and context data.

SimpleTemplateResponse.is_rendered[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L122)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.is_rendered "Link to this definition")
A boolean indicating whether the response content has been rendered.

### Methods[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#methods "Link to this heading")

SimpleTemplateResponse. __init__ (_template_, _context=None_, _content\_type=None_, _status=None_, _charset=None_, _using=None_, _headers=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L13)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.__init__ "Link to this definition")
Instantiates a [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") object with the given template, context, content type, HTTP status, and charset.

`template`
A backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.

`context`
A [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of values to add to the template context. By default, this is an empty dictionary.

`content_type`
The value included in the HTTP `Content-Type` header, including the MIME type specification and the character set encoding. If `content_type` is specified, then its value is used. Otherwise, `'text/html'` is used.

`status`
The HTTP status code for the response.

`charset`
The charset in which the response will be encoded. If not given it will be extracted from `content_type`, and if that is unsuccessful, the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting will be used.

`using`
The [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-NAME) of a template engine to use for loading the template.

`headers`
A [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of HTTP headers to add to the response.

SimpleTemplateResponse.resolve_context(_context_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L78)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.resolve_context "Link to this definition")
Preprocesses context data that will be used for rendering a template. Accepts a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of context data. By default, returns the same [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)").

Override this method in order to customize the context.

SimpleTemplateResponse.resolve_template(_template_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L69)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.resolve_template "Link to this definition")
Resolves the template instance to use for rendering. Accepts a backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.

Returns the backend-dependent template object instance to be rendered.

Override this method in order to customize template loading.

SimpleTemplateResponse.add_post_render_callback()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L94)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.add_post_render_callback "Link to this definition")
Add a callback that will be invoked after rendering has taken place. This hook can be used to defer certain processing operations (such as caching) until after rendering has occurred.

If the [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") has already been rendered, the callback will be invoked immediately.

When called, callbacks will be passed a single argument – the rendered [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") instance.

If the callback returns a value that is not `None`, this will be used as the response instead of the original response object (and will be passed to the next post rendering callback etc.)

SimpleTemplateResponse.render()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L105)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.render "Link to this definition")
Sets `response.content` to the result obtained by [`SimpleTemplateResponse.rendered_content`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.rendered_content "django.template.response.SimpleTemplateResponse.rendered_content"), runs all post-rendering callbacks, and returns the resulting response object.

`render()` will only have an effect the first time it is called. On subsequent calls, it will return the result obtained from the first call.

`TemplateResponse` objects[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#templateresponse-objects "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

_class_ TemplateResponse[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L147)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse "Link to this definition")
`TemplateResponse` is a subclass of [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") that knows about the current [`HttpRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest").

### Methods[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#id1 "Link to this heading")

TemplateResponse. __init__ (_request_, _template_, _context=None_, _content\_type=None_, _status=None_, _charset=None_, _using=None_, _headers=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/template/response.py#L150)[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse.__init__ "Link to this definition")
Instantiates a [`TemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") object with the given request, template, context, content type, HTTP status, and charset.

`request`
An [`HttpRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") instance.

`template`
A backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.

`context`
A [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of values to add to the template context. By default, this is an empty dictionary.

`content_type`
The value included in the HTTP `Content-Type` header, including the MIME type specification and the character set encoding. If `content_type` is specified, then its value is used. Otherwise, `'text/html'` is used.

`status`
The HTTP status code for the response.

`charset`
The charset in which the response will be encoded. If not given it will be extracted from `content_type`, and if that is unsuccessful, the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting will be used.

`using`
The [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-NAME) of a template engine to use for loading the template.

`headers`
A [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of HTTP headers to add to the response.

The rendering process[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#the-rendering-process "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

Before a [`TemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") instance can be returned to the client, it must be rendered. The rendering process takes the intermediate representation of template and context, and turns it into the final byte stream that can be served to the client.

There are three circumstances under which a `TemplateResponse` will be rendered:

*   When the `TemplateResponse` instance is explicitly rendered, using the [`SimpleTemplateResponse.render()`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.render "django.template.response.SimpleTemplateResponse.render") method.

*   When the content of the response is explicitly set by assigning `response.content`.

*   After passing through template response middleware, but before passing through response middleware.

A `TemplateResponse` can only be rendered once. The first call to [`SimpleTemplateResponse.render()`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.SimpleTemplateResponse.render "django.template.response.SimpleTemplateResponse.render") sets the content of the response; subsequent rendering calls do not change the response content.

However, when `response.content` is explicitly assigned, the change is always applied. If you want to force the content to be re-rendered, you can reevaluate the rendered content, and assign the content of the response manually:

# Set up a rendered TemplateResponse
>>> from django.template.response import TemplateResponse
>>> t = TemplateResponse(request, "original.html", {})
>>> t.render()
>>> print(t.content)
Original content

# Re-rendering doesn't change content
>>> t.template_name = "new.html"
>>> t.render()
>>> print(t.content)
Original content

# Assigning content does change, no render() call required
>>> t.content = t.rendered_content
>>> print(t.content)
New content

### Post-render callbacks[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#post-render-callbacks "Link to this heading")

Some operations – such as caching – cannot be performed on an unrendered template. They must be performed on a fully complete and rendered response.

If you’re using middleware, you can do that. Middleware provides multiple opportunities to process a response on exit from a view. If you put behavior in the response middleware, it’s guaranteed to execute after template rendering has taken place.

However, if you’re using a decorator, the same opportunities do not exist. Any behavior defined in a decorator is handled immediately.

To compensate for this (and any other analogous use cases), [`TemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") allows you to register callbacks that will be invoked when rendering has completed. Using this callback, you can defer critical processing until a point where you can guarantee that rendered content will be available.

To define a post-render callback, define a function that takes a single argument – response – and register that function with the template response:

from django.template.response import TemplateResponse

def my_render_callback(response):
    # Do content-sensitive processing
    do_post_processing()

def my_view(request):
    # Create a response
    response = TemplateResponse(request, "mytemplate.html", {})
    # Register the callback
    response.add_post_render_callback(my_render_callback)
    # Return the response
    return response

`my_render_callback()` will be invoked after the `mytemplate.html` has been rendered, and will be provided the fully rendered [`TemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") instance as an argument.

If the template has already been rendered, the callback will be invoked immediately.

Using `TemplateResponse` and `SimpleTemplateResponse`[¶](https://docs.djangoproject.com/en/6.0/ref/template-response/#using-templateresponse-and-simpletemplateresponse "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A [`TemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") object can be used anywhere that a normal [`django.http.HttpResponse`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") can be used. It can also be used as an alternative to calling [`render()`](https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/#django.shortcuts.render "django.shortcuts.render").

For example, the following view returns a [`TemplateResponse`](https://docs.djangoproject.com/en/6.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") with a template and a context containing a queryset:

from django.template.response import TemplateResponse

def blog_index(request):
    return TemplateResponse(
        request, "entry_list.html", {"entries": Entry.objects.all()}
    )
