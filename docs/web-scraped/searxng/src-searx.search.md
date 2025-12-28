# Source: https://docs.searxng.org/src/searx.search.html

[]

# Search[¶](#search "Link to this heading")

*[[class]][ ]*[[searx.search.models.]][[EngineRef]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[category]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/search/models.html#EngineRef)[¶](#searx.search.models.EngineRef "Link to this definition")

:   Reference by names to an engine and category

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[searx.search.models.]][[SearchQuery]][(]*[[query]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[engineref_list]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[EngineRef]](#searx.search.models.EngineRef "searx.search.models.EngineRef")[[\]]]]*, *[[lang]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'all\']]*, *[[safesearch]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[0]][[,]][ ][[1]][[,]][ ][[2]][[\]]]][ ][[=]][ ][[0]]*, *[[pageno]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[time_range]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'day\']][[,]][ ][[\'week\']][[,]][ ][[\'month\']][[,]][ ][[\'year\']][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[timeout_limit]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[external_bang]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[engine_data]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[redirect_to_first_result]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/searx/search/models.html#SearchQuery)[¶](#searx.search.models.SearchQuery "Link to this definition")

:   container for all the search parameters (query, language, etc...)

```
<!-- -->
```

*[[class]][ ]*[[searx.search.]][[Search]][(]*[[search_query]][[:]][ ][[[SearchQuery]](#searx.search.models.SearchQuery "searx.search.models.SearchQuery")]*[)][[[\[source\]]]](../_modules/searx/search.html#Search)[¶](#searx.search.Search "Link to this definition")

:   Search information container

    [[search_query]]*[[:]][ ][searx.search.SearchQuery]*[¶](#searx.search.Search.search_query "Link to this definition")

    :   

    [[result_container]]*[[:]][ ][searx.results.ResultContainer]*[¶](#searx.search.Search.result_container "Link to this definition")

    :   

    [[search]][(][)] [[→] [[searx.results.ResultContainer]]][[[\[source\]]]](../_modules/searx/search.html#Search.search)[¶](#searx.search.Search.search "Link to this definition")

    :   

```
<!-- -->
```

*[[class]][ ]*[[searx.search.]][[SearchWithPlugins]][(]*[[search_query]][[:]][ ][[[SearchQuery]](#searx.search.models.SearchQuery "searx.search.models.SearchQuery")]*, *[[request]][[:]][ ][[[SXNG_Request]](../dev/extended_types.html#searx.extended_types.SXNG_Request "searx.extended_types.SXNG_Request")]*, *[[user_plugins]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]*[)][[[\[source\]]]](../_modules/searx/search.html#SearchWithPlugins)[¶](#searx.search.SearchWithPlugins "Link to this definition")

:   Inherit from the Search class, add calls to the plugins.

    [[search_query]]*[[:]][ ][searx.search.SearchQuery]*[¶](#searx.search.SearchWithPlugins.search_query "Link to this definition")

    :   

    [[result_container]]*[[:]][ ][searx.results.ResultContainer]*[¶](#searx.search.SearchWithPlugins.result_container "Link to this definition")

    :   

    [[ordered_plugin_list]]*[[:]][ ][[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")*[¶](#searx.search.SearchWithPlugins.ordered_plugin_list "Link to this definition")

    :   

    [[request]]*[[:]][ ][flask.request]*[¶](#searx.search.SearchWithPlugins.request "Link to this definition")

    :   

    [[search]][(][)] [[→] [[searx.results.ResultContainer]]][[[\[source\]]]](../_modules/searx/search.html#SearchWithPlugins.search)[¶](#searx.search.SearchWithPlugins.search "Link to this definition")

    :