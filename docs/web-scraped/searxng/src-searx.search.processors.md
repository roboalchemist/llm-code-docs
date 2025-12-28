# Source: https://docs.searxng.org/src/searx.search.processors.html

[]

# Search processors[¶](#search-processors "Link to this heading")

-   [Abstract processor class](#module-searx.search.processors.abstract)

-   [Offline processor](#module-searx.search.processors.offline)

-   [Online processor](#module-searx.search.processors.online)

-   [Online currency processor](#module-searx.search.processors.online_currency)

-   [Online dictionary processor](#module-searx.search.processors.online_dictionary)

-   [Online URL search processor](#module-searx.search.processors.online_url_search)

[]

## [Abstract processor class](#id1)[¶](#module-searx.search.processors.abstract "Link to this heading")

Abstract base classes for all engine processors.

*[[class]][ ]*[[searx.search.processors.abstract.]][[RequestParams]][[[\[source\]]]](../_modules/searx/search/processors/abstract.html#RequestParams)[¶](#searx.search.processors.abstract.RequestParams "Link to this definition")

:   Basic quantity of the Request parameters of all engine types.

    [[query]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.abstract.RequestParams.query "Link to this definition")

    :   Search term, stripped of search syntax arguments.

    [[category]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.abstract.RequestParams.category "Link to this definition")

    :   Current category, like [`general`].

        ::: 
        Hint

        This field is deprecated, don't use it in further implementations.
        :::

        This field is currently *arbitrarily* filled with the name of "one"" category (the name of the first category of the engine). In practice, however, it is not clear what this "one" category should be; in principle, multiple categories can also be activated in a search.

    [[pageno]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.search.processors.abstract.RequestParams.pageno "Link to this definition")

    :   Current page number, where the first page is [`1`].

    [[safesearch]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[0]][[,]][ ][[1]][[,]][ ][[2]][[\]]]*[¶](#searx.search.processors.abstract.RequestParams.safesearch "Link to this definition")

    :   Safe-Search filter (0:normal, 1:moderate, 2:strict).

    [[time_range]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'day\']][[,]][ ][[\'week\']][[,]][ ][[\'month\']][[,]][ ][[\'year\']][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[¶](#searx.search.processors.abstract.RequestParams.time_range "Link to this definition")

    :   Time-range filter.

    [[engine_data]]*[[:]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.search.processors.abstract.RequestParams.engine_data "Link to this definition")

    :   Allows the transfer of (engine specific) data to the next request of the client. In the case of the [`online`] engines, this data is delivered to the client via the HTML [`<form>`] in response.

        If the client then sends this form back to the server with the next request, this data will be available.

        This makes it possible to carry data from one request to the next without a session context, but this feature (is fragile) and should only be used in exceptional cases. See also [[engine_data_form]](../dev/templates.html#engine-data).

    [[searxng_locale]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.abstract.RequestParams.searxng_locale "Link to this definition")

    :   Language / locale filter from the search request, a string like 'all', 'en', 'en-US', 'zh-HK' .. and others, for more details see [[`searx.locales`]](searx.locales.html#module-searx.locales "searx.locales").

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.abstract.]][[SuspendedStatus]][[[\[source\]]]](../_modules/searx/search/processors/abstract.html#SuspendedStatus)[¶](#searx.search.processors.abstract.SuspendedStatus "Link to this definition")

:   Class to handle suspend state.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.abstract.]][[EngineProcessor]][(]*[[engine]][[:]][ ][[[Engine]](../dev/engines/enginelib.html#searx.enginelib.Engine "searx.enginelib.Engine")[ ][[\|]][ ][[types.ModuleType]](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/search/processors/abstract.html#EngineProcessor)[¶](#searx.search.processors.abstract.EngineProcessor "Link to this definition")

:   Base classes used for all types of request processors.

    [[initialize]][(]*[[callback]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[EngineProcessor]](#searx.search.processors.abstract.EngineProcessor "searx.search.processors.abstract.EngineProcessor")[[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]][[,]][ ][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[\]]]]*[)][[[\[source\]]]](../_modules/searx/search/processors/abstract.html#EngineProcessor.initialize)[¶](#searx.search.processors.abstract.EngineProcessor.initialize "Link to this definition")

    :   Initialization of *this* [[`EngineProcessor`]](#searx.search.processors.abstract.EngineProcessor "searx.search.processors.abstract.EngineProcessor").

        If processor's engine has an [`init`] method, it is called first. Engine's [`init`] method is executed in a thread, meaning that the *registration* (the [`callback`]) may occur later and is not already established by the return from this registration method.

        Registration only takes place if the [`init`] method is not available or is successfully run through.

    [[get_params]][(]*[[search_query]][[:]][ ][[[SearchQuery]](searx.search.html#searx.search.models.SearchQuery "searx.search.models.SearchQuery")]*, *[[engine_category]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[RequestParams]](#searx.search.processors.abstract.RequestParams "searx.search.processors.abstract.RequestParams")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/search/processors/abstract.html#EngineProcessor.get_params)[¶](#searx.search.processors.abstract.EngineProcessor.get_params "Link to this definition")

    :   Returns a dictionary with the [[request parameters]](../dev/engines/engine_overview.html#engine-request-arguments) ([[`RequestParams`]](#searx.search.processors.abstract.RequestParams "searx.search.processors.abstract.RequestParams")), if the search condition is not supported by the engine, [`None`] is returned:

        -   

            *time range* filter in search conditions, but the engine does not have

            :   a corresponding filter

        -   page number \> 1 when engine does not support paging

        -   page number \> [`max_page`]

[]

## [Offline processor](#id2)[¶](#module-searx.search.processors.offline "Link to this heading")

Processors for engine-type: [`offline`]

*[[class]][ ]*[[searx.search.processors.offline.]][[OfflineProcessor]][(]*[[engine]][[:]][ ][[[Engine]](../dev/engines/enginelib.html#searx.enginelib.Engine "searx.enginelib.Engine")[ ][[\|]][ ][[types.ModuleType]](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/search/processors/offline.html#OfflineProcessor)[¶](#searx.search.processors.offline.OfflineProcessor "Link to this definition")

:   Processor class used by [`offline`] engines.

[]

## [Online processor](#id3)[¶](#module-searx.search.processors.online "Link to this heading")

Processor used for [`online`] engines.

*[[class]][ ]*[[searx.search.processors.online.]][[OnlineProcessor]][(]*[[engine]][[:]][ ][[[Engine]](../dev/engines/enginelib.html#searx.enginelib.Engine "searx.enginelib.Engine")[ ][[\|]][ ][[types.ModuleType]](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/search/processors/online.html#OnlineProcessor)[¶](#searx.search.processors.online.OnlineProcessor "Link to this definition")

:   Processor class for [`online`] engines.

    [[init_engine]][(][)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/search/processors/online.html#OnlineProcessor.init_engine)[¶](#searx.search.processors.online.OnlineProcessor.init_engine "Link to this definition")

    :   This method is called in a thread, and before the base method is called, the network must be set up for the [`online`] engines.

    [[get_params]][(]*[[search_query]][[:]][ ][[[SearchQuery]](searx.search.html#searx.search.models.SearchQuery "searx.search.models.SearchQuery")]*, *[[engine_category]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[OnlineParams]](#searx.search.processors.online.OnlineParams "searx.search.processors.online.OnlineParams")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/search/processors/online.html#OnlineProcessor.get_params)[¶](#searx.search.processors.online.OnlineProcessor.get_params "Link to this definition")

    :   Returns a dictionary with the [[request params]](../dev/engines/engine_overview.html#engine-request-online) ([[`OnlineParams`]](#searx.search.processors.online.OnlineParams "searx.search.processors.online.OnlineParams")), if the search condition is not supported by the engine, [`None`] is returned.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online.]][[OnlineParams]][[[\[source\]]]](../_modules/searx/search/processors/online.html#OnlineParams)[¶](#searx.search.processors.online.OnlineParams "Link to this definition")

:   Request parameters of a [`online`] engine.

[]

## [Online currency processor](#id4)[¶](#module-searx.search.processors.online_currency "Link to this heading")

Processor used for [`online_currency`] engines.

[[searx.search.processors.online_currency.]][[search_syntax]]*[ ][[=]][ ][re.compile(\'.\*?(\\\\d+(?:\\\\.\\\\d+)?)] [(\[\^.0-9\]+)] [(?:in\|to)] [(\[\^.0-9\]+)\',] [re.IGNORECASE)]*[¶](#searx.search.processors.online_currency.search_syntax "Link to this definition")

:   Search syntax used for from/to currency (e.g. [`10`]` `[`usd`]` `[`to`]` `[`eur`])

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_currency.]][[CurrenciesParams]][[[\[source\]]]](../_modules/searx/search/processors/online_currency.html#CurrenciesParams)[¶](#searx.search.processors.online_currency.CurrenciesParams "Link to this definition")

:   Currencies request parameters.

    [[amount]]*[[:]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*[¶](#searx.search.processors.online_currency.CurrenciesParams.amount "Link to this definition")

    :   Currency amount to be converted

    [[to_iso4217]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.online_currency.CurrenciesParams.to_iso4217 "Link to this definition")

    :   [ISO_4217](https://en.wikipedia.org/wiki/ISO_4217) alpha code of the currency used as the basis for conversion.

    [[from_iso4217]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.online_currency.CurrenciesParams.from_iso4217 "Link to this definition")

    :   [ISO_4217](https://en.wikipedia.org/wiki/ISO_4217) alpha code of the currency to be converted.

    [[from_name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.online_currency.CurrenciesParams.from_name "Link to this definition")

    :   Name of the currency used as the basis for conversion.

    [[to_name]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.online_currency.CurrenciesParams.to_name "Link to this definition")

    :   Name of the currency of the currency to be converted.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_currency.]][[OnlineCurrenciesParams]][[[\[source\]]]](../_modules/searx/search/processors/online_currency.html#OnlineCurrenciesParams)[¶](#searx.search.processors.online_currency.OnlineCurrenciesParams "Link to this definition")

:   Request parameters of a [`online_currency`] engine.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_currency.]][[OnlineCurrencyProcessor]][(]*[[engine]][[:]][ ][[[Engine]](../dev/engines/enginelib.html#searx.enginelib.Engine "searx.enginelib.Engine")[ ][[\|]][ ][[types.ModuleType]](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/search/processors/online_currency.html#OnlineCurrencyProcessor)[¶](#searx.search.processors.online_currency.OnlineCurrencyProcessor "Link to this definition")

:   Processor class used by [`online_currency`] engines.

    [[get_params]][(]*[[search_query]][[:]][ ][[[SearchQuery]](searx.search.html#searx.search.models.SearchQuery "searx.search.models.SearchQuery")]*, *[[engine_category]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[OnlineCurrenciesParams]](#searx.search.processors.online_currency.OnlineCurrenciesParams "searx.search.processors.online_currency.OnlineCurrenciesParams")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/search/processors/online_currency.html#OnlineCurrencyProcessor.get_params)[¶](#searx.search.processors.online_currency.OnlineCurrencyProcessor.get_params "Link to this definition")

    :   Returns a dictionary with the [[request params]](../dev/engines/engine_overview.html#engine-request-online-currency) ([[`OnlineCurrenciesParams`]](#searx.search.processors.online_currency.OnlineCurrenciesParams "searx.search.processors.online_currency.OnlineCurrenciesParams")). [`None`] is returned if the search query does not match [[`search_syntax`]](#searx.search.processors.online_currency.search_syntax "searx.search.processors.online_currency.search_syntax").

[]

## [Online dictionary processor](#id5)[¶](#module-searx.search.processors.online_dictionary "Link to this heading")

Processor used for [`online_dictionary`] engines.

[[searx.search.processors.online_dictionary.]][[search_syntax]]*[ ][[=]][ ][re.compile(\'.\*?(\[a-z\]+)-(\[a-z\]+)] [(.+)\$\',] [re.IGNORECASE)]*[¶](#searx.search.processors.online_dictionary.search_syntax "Link to this definition")

:   Search syntax used for from/to language (e.g. [`en-de`])

```
<!-- -->
```

[[searx.search.processors.online_dictionary.]][[FromToType]][¶](#searx.search.processors.online_dictionary.FromToType "Link to this definition")

:   Type of a language descriptions in the context of a [`online_dictionary`].

    alias of [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")\[[[`bool`]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"), [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\]

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_dictionary.]][[DictParams]][[[\[source\]]]](../_modules/searx/search/processors/online_dictionary.html#DictParams)[¶](#searx.search.processors.online_dictionary.DictParams "Link to this definition")

:   Dictionary request parameters.

    [[from_lang]]*[[:]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.search.processors.online_dictionary.DictParams.from_lang "Link to this definition")

    :   Language from which is to be translated.

    [[to_lang]]*[[:]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.search.processors.online_dictionary.DictParams.to_lang "Link to this definition")

    :   Language to translate into.

    [[query]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.search.processors.online_dictionary.DictParams.query "Link to this definition")

    :   Search term, cleaned of search syntax (*from-to* has been removed).

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_dictionary.]][[OnlineDictParams]][[[\[source\]]]](../_modules/searx/search/processors/online_dictionary.html#OnlineDictParams)[¶](#searx.search.processors.online_dictionary.OnlineDictParams "Link to this definition")

:   Request parameters of a [`online_dictionary`] engine.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_dictionary.]][[OnlineDictionaryProcessor]][(]*[[engine]][[:]][ ][[[Engine]](../dev/engines/enginelib.html#searx.enginelib.Engine "searx.enginelib.Engine")[ ][[\|]][ ][[types.ModuleType]](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/search/processors/online_dictionary.html#OnlineDictionaryProcessor)[¶](#searx.search.processors.online_dictionary.OnlineDictionaryProcessor "Link to this definition")

:   Processor class for [`online_dictionary`] engines.

    [[get_params]][(]*[[search_query]][[:]][ ][[[SearchQuery]](searx.search.html#searx.search.models.SearchQuery "searx.search.models.SearchQuery")]*, *[[engine_category]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[OnlineDictParams]](#searx.search.processors.online_dictionary.OnlineDictParams "searx.search.processors.online_dictionary.OnlineDictParams")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/search/processors/online_dictionary.html#OnlineDictionaryProcessor.get_params)[¶](#searx.search.processors.online_dictionary.OnlineDictionaryProcessor.get_params "Link to this definition")

    :   Returns a dictionary with the [[request params]](../dev/engines/engine_overview.html#engine-request-online-dictionary) ([[`OnlineDictParams`]](#searx.search.processors.online_dictionary.OnlineDictParams "searx.search.processors.online_dictionary.OnlineDictParams")). [`None`] is returned if the search query does not match [[`search_syntax`]](#searx.search.processors.online_dictionary.search_syntax "searx.search.processors.online_dictionary.search_syntax").

[]

## [Online URL search processor](#id6)[¶](#module-searx.search.processors.online_url_search "Link to this heading")

Processor used for [`online_url_search`] engines.

[[searx.search.processors.online_url_search.]][[search_syntax]]*[ ][[=]][ ][ [re.compile(\'data:image/\[\^;] [\]\*;base64,\[\^] [\]\*\'),] [\'ftp\':] [re.compile(\'ftps?:\\\\/\\\\/\[\^] [\]\*\'),] [\'http\':] [re.compile(\'https?:\\\\/\\\\/\[\^] [\]\*\')}]*[¶](#searx.search.processors.online_url_search.search_syntax "Link to this definition")

:   Search syntax used for a URL search.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_url_search.]][[UrlParams]][[[\[source\]]]](../_modules/searx/search/processors/online_url_search.html#UrlParams)[¶](#searx.search.processors.online_url_search.UrlParams "Link to this definition")

:   URL request parameters.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_url_search.]][[OnlineUrlSearchParams]][[[\[source\]]]](../_modules/searx/search/processors/online_url_search.html#OnlineUrlSearchParams)[¶](#searx.search.processors.online_url_search.OnlineUrlSearchParams "Link to this definition")

:   Request parameters of a [`online_url_search`] engine.

```
<!-- -->
```

*[[class]][ ]*[[searx.search.processors.online_url_search.]][[OnlineUrlSearchProcessor]][(]*[[engine]][[:]][ ][[[Engine]](../dev/engines/enginelib.html#searx.enginelib.Engine "searx.enginelib.Engine")[ ][[\|]][ ][[types.ModuleType]](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/search/processors/online_url_search.html#OnlineUrlSearchProcessor)[¶](#searx.search.processors.online_url_search.OnlineUrlSearchProcessor "Link to this definition")

:   Processor class used by [`online_url_search`] engines.

    [[get_params]][(]*[[search_query]][[:]][ ][[[SearchQuery]](searx.search.html#searx.search.models.SearchQuery "searx.search.models.SearchQuery")]*, *[[engine_category]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[OnlineUrlSearchParams]](#searx.search.processors.online_url_search.OnlineUrlSearchParams "searx.search.processors.online_url_search.OnlineUrlSearchParams")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/search/processors/online_url_search.html#OnlineUrlSearchProcessor.get_params)[¶](#searx.search.processors.online_url_search.OnlineUrlSearchProcessor.get_params "Link to this definition")

    :   Returns a dictionary with the [[request params]](../dev/engines/engine_overview.html#engine-request-online-currency) ([[`OnlineUrlSearchParams`]](#searx.search.processors.online_url_search.OnlineUrlSearchParams "searx.search.processors.online_url_search.OnlineUrlSearchParams")). [`None`] is returned if the search query does not match [[`search_syntax`]](#searx.search.processors.online_url_search.search_syntax "searx.search.processors.online_url_search.search_syntax").