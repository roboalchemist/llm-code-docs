# Source: https://docs.searxng.org/dev/extended_types.html

[][]

# Extended Types[¶](#module-searx.extended_types "Link to this heading")

This module implements the type extensions applied by SearXNG.

-   [[`flask.request`]](https://flask.palletsprojects.com/en/stable/api/#flask.request "(in Flask v3.1.x)") is replaced by [[`sxng_request`]](#searx.extended_types.sxng_request "searx.extended_types.sxng_request")

-   [[`flask.Request`]](https://flask.palletsprojects.com/en/stable/api/#flask.Request "(in Flask v3.1.x)") is replaced by [[`SXNG_Request`]](#searx.extended_types.SXNG_Request "searx.extended_types.SXNG_Request")

-   [`httpx.response`] is replaced by [[`SXNG_Response`]](#searx.extended_types.SXNG_Response "searx.extended_types.SXNG_Response")

------------------------------------------------------------------------

[[searx.extended_types.]][[sxng_request]]*[[:]][ ][[SXNG_Request]](#searx.extended_types.SXNG_Request "searx.extended_types.SXNG_Request")*[¶](#searx.extended_types.sxng_request "Link to this definition")

:   A replacement for [[`flask.request`]](https://flask.palletsprojects.com/en/stable/api/#flask.request "(in Flask v3.1.x)") with type cast [[`SXNG_Request`]](#searx.extended_types.SXNG_Request "searx.extended_types.SXNG_Request").

```
<!-- -->
```

*[[class]][ ]*[[searx.extended_types.]][[SXNG_Request]][(]*[[environ]][[:]][ ][[WSGIEnvironment]]*, *[[populate_request]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[shallow]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][[[\[source\]]]](../_modules/searx/extended_types.html#SXNG_Request)[¶](#searx.extended_types.SXNG_Request "Link to this definition")

:   SearXNG extends the class [[`flask.Request`]](https://flask.palletsprojects.com/en/stable/api/#flask.Request "(in Flask v3.1.x)") with properties from *this* class definition, see type cast [[`sxng_request`]](#searx.extended_types.sxng_request "searx.extended_types.sxng_request").

    [[user_plugins]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.extended_types.SXNG_Request.user_plugins "Link to this definition")

    :   list of searx.plugins.Plugin.id (the id of the plugins)

    [[preferences]]*[[:]][ ][searx.preferences.Preferences]*[¶](#searx.extended_types.SXNG_Request.preferences "Link to this definition")

    :   The preferences of the request.

    [[errors]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.extended_types.SXNG_Request.errors "Link to this definition")

    :   A list of errors (translated text) added by [`searx.webapp`] in case of errors.

    [[start_time]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#searx.extended_types.SXNG_Request.start_time "Link to this definition")

    :   Start time of the request, [[`timeit.default_timer`]](https://docs.python.org/3/library/timeit.html#timeit.default_timer "(in Python v3.14)") added by [`searx.webapp`] to calculate the total time of the request.

    [[render_time]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#searx.extended_types.SXNG_Request.render_time "Link to this definition")

    :   Duration of the rendering, calculated and added by [`searx.webapp`].

    [[timings]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][searx.results.Timing][[\]]]*[¶](#searx.extended_types.SXNG_Request.timings "Link to this definition")

    :   A list of [`searx.results.Timing`] of the engines, calculatid in and hold by [`searx.results.ResultContainer.timings`].

    [[remote_addr]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.extended_types.SXNG_Request.remote_addr "Link to this definition")

    :   The address of the client sending the request.

```
<!-- -->
```

*[[class]][ ]*[[searx.extended_types.]][[SXNG_Response]][(]*[[status_code]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[\*]]*, *[[headers]][[:]][ ][[Headers][ ][[\|]][ ][[Mapping]](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][ ][[\|]][ ][[Mapping]](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[\[]][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[,]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[\]]][ ][[\|]][ ][[Sequence]](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[\[]][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][[\]]][ ][[\|]][ ][[Sequence]](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[\[]][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[,]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[\]]][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[content]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[ ][[\|]][ ][[Iterable]](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[\[]][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[\]]][ ][[\|]][ ][[AsyncIterable]](https://docs.python.org/3/library/typing.html#typing.AsyncIterable "(in Python v3.14)")[[\[]][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[text]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[html]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[json]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[SyncByteStream][ ][[\|]][ ][AsyncByteStream][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[request]][[:]][ ][[Request][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[extensions]][[:]][ ][[[Mapping]](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[history]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][Response][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[default_encoding]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[\]]][[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\'utf-8\']]*[)][[[\[source\]]]](../_modules/searx/extended_types.html#SXNG_Response)[¶](#searx.extended_types.SXNG_Response "Link to this definition")

:   SearXNG extends the class [`httpx.Response`] with properties from *this* class (type cast of [`httpx.Response`]).

    ::: 
    ::: highlight
        response = httpx.get("https://example.org")
        response = typing.cast(SXNG_Response, response)
        if response.ok:
           ...
        query_was = search_params["query"]
    :::
    :::