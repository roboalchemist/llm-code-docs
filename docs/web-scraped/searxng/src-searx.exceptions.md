# Source: https://docs.searxng.org/src/searx.exceptions.html

[][]

# SearXNG Exceptions[¶](#module-searx.exceptions "Link to this heading")

Exception types raised by SearXNG modules.

*[[exception]][ ]*[[searx.exceptions.]][[SearxException]][[[\[source\]]]](../_modules/searx/exceptions.html#SearxException)[¶](#searx.exceptions.SearxException "Link to this definition")

:   Base SearXNG exception.

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxParameterException]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[value]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/exceptions.html#SearxParameterException)[¶](#searx.exceptions.SearxParameterException "Link to this definition")

:   Raised when query miss a required parameter

```
<!-- -->
```

*[[final]][ ][[exception]][ ]*[[searx.exceptions.]][[SearxSettingsException]][(]*[[message]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[Exception]](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")]*, *[[filename]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/exceptions.html#SearxSettingsException)[¶](#searx.exceptions.SearxSettingsException "Link to this definition")

:   Error while loading the settings

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxEngineException]][[[\[source\]]]](../_modules/searx/exceptions.html#SearxEngineException)[¶](#searx.exceptions.SearxEngineException "Link to this definition")

:   Error inside an engine

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxXPathSyntaxException]][(]*[[xpath_spec]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][XPath]]*, *[[message]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/exceptions.html#SearxXPathSyntaxException)[¶](#searx.exceptions.SearxXPathSyntaxException "Link to this definition")

:   Syntax error in a XPATH

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxEngineResponseException]][[[\[source\]]]](../_modules/searx/exceptions.html#SearxEngineResponseException)[¶](#searx.exceptions.SearxEngineResponseException "Link to this definition")

:   Impossible to parse the result of an engine

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxEngineAPIException]][[[\[source\]]]](../_modules/searx/exceptions.html#SearxEngineAPIException)[¶](#searx.exceptions.SearxEngineAPIException "Link to this definition")

:   The website has returned an application error

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxEngineAccessDeniedException]][(]*[[suspended_time]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[message]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'Access] [denied\']]*[)][[[\[source\]]]](../_modules/searx/exceptions.html#SearxEngineAccessDeniedException)[¶](#searx.exceptions.SearxEngineAccessDeniedException "Link to this definition")

:   The website is blocking the access

    [[SUSPEND_TIME_SETTING]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[=]][ ][\'search.suspended_times.SearxEngineAccessDenied\']*[¶](#searx.exceptions.SearxEngineAccessDeniedException.SUSPEND_TIME_SETTING "Link to this definition")

    :   This settings contains the default suspended time (default 86400 sec / 1 day).

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxEngineCaptchaException]][(]*[[suspended_time]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[message]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'CAPTCHA\']]*[)][[[\[source\]]]](../_modules/searx/exceptions.html#SearxEngineCaptchaException)[¶](#searx.exceptions.SearxEngineCaptchaException "Link to this definition")

:   The website has returned a CAPTCHA.

    [[SUSPEND_TIME_SETTING]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[=]][ ][\'search.suspended_times.SearxEngineCaptcha\']*[¶](#searx.exceptions.SearxEngineCaptchaException.SUSPEND_TIME_SETTING "Link to this definition")

    :   This settings contains the default suspended time (default 86400 sec / 1 day).

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxEngineTooManyRequestsException]][(]*[[suspended_time]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[message]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'Too] [many] [request\']]*[)][[[\[source\]]]](../_modules/searx/exceptions.html#SearxEngineTooManyRequestsException)[¶](#searx.exceptions.SearxEngineTooManyRequestsException "Link to this definition")

:   The website has returned a Too Many Request status code

    By default, SearXNG stops sending requests to this engine for 1 hour.

    [[SUSPEND_TIME_SETTING]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[=]][ ][\'search.suspended_times.SearxEngineTooManyRequests\']*[¶](#searx.exceptions.SearxEngineTooManyRequestsException.SUSPEND_TIME_SETTING "Link to this definition")

    :   This settings contains the default suspended time (default 3660 sec / 1 hour).

```
<!-- -->
```

*[[exception]][ ]*[[searx.exceptions.]][[SearxEngineXPathException]][(]*[[xpath_spec]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][XPath]]*, *[[message]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/exceptions.html#SearxEngineXPathException)[¶](#searx.exceptions.SearxEngineXPathException "Link to this definition")

:   Error while getting the result of an XPath expression