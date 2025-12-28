# Source: https://docs.searxng.org/src/searx.favicons.html

[]

# Favicons (source)[¶](#favicons-source "Link to this heading")

-   [Favicons Config](#module-searx.favicons.config)

-   [Favicons Proxy](#module-searx.favicons.proxy)

-   [Favicons Resolver](#module-searx.favicons.resolvers)

-   [Favicons Cache](#module-searx.favicons.cache)

Implementations for providing the favicons in SearXNG.

There is a command line for developer purposes and for deeper analysis. Here is an example in which the command line is called in the development environment:

    $ ./manage pyenv.cmd bash --norc --noprofile
    (py3) python -m searx.favicons --help

[[searx.favicons.]][[favicon_url]][(]*[[authority]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/favicons/proxy.html#favicon_url)[¶](#searx.favicons.favicon_url "Link to this definition")

:   Function to generate the image URL used for favicons in SearXNG's result lists. The [`authority`] argument (aka netloc / [][**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html)) is usually a (sub-) domain name. This function is used in the HTML (jinja) templates.

    ::: 
    ::: highlight
        <div class="favicon">
           <img src="}">
        </div>
    :::
    :::

    The returned URL is a route to [[`favicon_proxy`]](#searx.favicons.favicon_proxy "searx.favicons.favicon_proxy") REST API.

    If the favicon is already in the cache, the returned URL is a [data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs) (something like [`data:image/png;base64,...`]). By generating a data url from the [[`cache.FaviconCache`]](#searx.favicons.cache.FaviconCache "searx.favicons.cache.FaviconCache"), additional HTTP roundtripps via the [[`favicon_proxy`]](#searx.favicons.favicon_proxy "searx.favicons.favicon_proxy") are saved. However, it must also be borne in mind that data urls are not cached in the client (web browser).

```
<!-- -->
```

[[searx.favicons.]][[favicon_proxy]][(][)][[[\[source\]]]](../_modules/searx/favicons/proxy.html#favicon_proxy)[¶](#searx.favicons.favicon_proxy "Link to this definition")

:   REST API of SearXNG's favicon proxy service

    ::: 
    ::: highlight
        /favicon_proxy?authority=<...>&h=<...>
    :::
    :::

    [`authority`]:

    :   Domain name [][**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) / see [[`favicon_url`]](#searx.favicons.favicon_url "searx.favicons.favicon_url")

    [`h`]:

    :   HMAC [][**RFC 2104**](https://datatracker.ietf.org/doc/html/rfc2104.html), build up from the [[server.secret_key]](../admin/settings/settings_server.html#settings-server) setting.

[][]

## [Favicons Config](#id7)[¶](#module-searx.favicons.config "Link to this heading")

[[searx.favicons.config.]][[CONFIG_SCHEMA]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[=]][ ][1]*[¶](#searx.favicons.config.CONFIG_SCHEMA "Link to this definition")

:   Version of the configuration schema.

```
<!-- -->
```

[[searx.favicons.config.]][[TOML_CACHE_CFG]]*[[:]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[FaviconConfig]](#searx.favicons.config.FaviconConfig "searx.favicons.config.FaviconConfig")[[\]]][ ][[=]][ ][]*[¶](#searx.favicons.config.TOML_CACHE_CFG "Link to this definition")

:   Cache config objects by TOML's filename.

```
<!-- -->
```

*[[class]][ ]*[[searx.favicons.config.]][[FaviconConfig]][(]*[[cfg_schema:] [int]]*, *[[cache:] [\~searx.favicons.cache.FaviconCacheConfig] [=] [\<factory\>]]*, *[[proxy:] [\~searx.favicons.proxy.FaviconProxyConfig] [=] [\<factory\>]]*[)][[[\[source\]]]](../_modules/searx/favicons/config.html#FaviconConfig)[¶](#searx.favicons.config.FaviconConfig "Link to this definition")

:   The class aggregates configurations of the favicon tools

    [[cfg_schema]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.config.FaviconConfig.cfg_schema "Link to this definition")

    :   Config's schema version. The specification of the version of the schema is mandatory, currently only version [[`CONFIG_SCHEMA`]](#searx.favicons.config.CONFIG_SCHEMA "searx.favicons.config.CONFIG_SCHEMA") is supported. By specifying a version, it is possible to ensure downward compatibility in the event of future changes to the configuration schema

    [[cache]]*[[:]][ ][[FaviconCacheConfig]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig")*[¶](#searx.favicons.config.FaviconConfig.cache "Link to this definition")

    :   Setup of the [[`cache.FaviconCacheConfig`]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig").

    [[proxy]]*[[:]][ ][[FaviconProxyConfig]](#searx.favicons.proxy.FaviconProxyConfig "searx.favicons.proxy.FaviconProxyConfig")*[¶](#searx.favicons.config.FaviconConfig.proxy "Link to this definition")

    :   Setup of the [[`proxy.FaviconProxyConfig`]](#searx.favicons.proxy.FaviconProxyConfig "searx.favicons.proxy.FaviconProxyConfig").

    *[[classmethod]][ ]*[[from_toml_file]][(]*[[cfg_file]][[:]][ ][[[Path]](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")]*, *[[use_cache]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*[)] [[→] [[[FaviconConfig]](#searx.favicons.config.FaviconConfig "searx.favicons.config.FaviconConfig")]][[[\[source\]]]](../_modules/searx/favicons/config.html#FaviconConfig.from_toml_file)[¶](#searx.favicons.config.FaviconConfig.from_toml_file "Link to this definition")

    :   Create a config object from a TOML file, the [`use_cache`] argument specifies whether a cache should be used.

[][]

## [Favicons Proxy](#id8)[¶](#module-searx.favicons.proxy "Link to this heading")

Implementations for a favicon proxy

*[[class]][ ]*[[searx.favicons.proxy.]][[FaviconProxyConfig]][(]*[[max_age:] [int] [=] [604800]]*, *[[secret_key:] [str] [=] [\'\']]*, *[[resolver_timeout:] [int] [=] [3.0]]*, *[[resolver_map:] [dict\[str]]*, *[[str\]] [=] [\<factory\>]]*, *[[favicon_path:] [str] [=] [\'/home/runner/work/searxng/searxng/searx/static/themes//img/empty_favicon.svg\']]*, *[[favicon_mime_type:] [str] [=] [\'image/svg+xml\']]*[)][[[\[source\]]]](../_modules/searx/favicons/proxy.html#FaviconProxyConfig)[¶](#searx.favicons.proxy.FaviconProxyConfig "Link to this definition")

:   Configuration of the favicon proxy.

    [[max_age]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.proxy.FaviconProxyConfig.max_age "Link to this definition")

    :   HTTP header [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) [`max-age`]

    [[secret_key]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.favicons.proxy.FaviconProxyConfig.secret_key "Link to this definition")

    :   By default, the value from [[server.secret_key]](../admin/settings/settings_server.html#settings-server) setting is used.

    [[resolver_timeout]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.proxy.FaviconProxyConfig.resolver_timeout "Link to this definition")

    :   Timeout which the resolvers should not exceed, is usually passed to the outgoing request of the resolver. By default, the value from [[outgoing.request_timeout]](../admin/settings/settings_outgoing.html#settings-outgoing) setting is used.

    [[resolver_map]]*[[:]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.favicons.proxy.FaviconProxyConfig.resolver_map "Link to this definition")

    :   The resolver_map is a key / value dictionary where the key is the name of the resolver and the value is the fully qualifying name (fqn) of resolver's function (the callable). The resolvers from the python module [`searx.favicons.resolver`] are available by default.

    [[get_resolver]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/favicons/proxy.html#FaviconProxyConfig.get_resolver)[¶](#searx.favicons.proxy.FaviconProxyConfig.get_resolver "Link to this definition")

    :   Returns the callable object (function) of the resolver with the [`name`]. If no resolver is registered for the [`name`], [`None`] is returned.

    [[favicon]][(]*[[\*\*]][[replacements]]*[)][[[\[source\]]]](../_modules/searx/favicons/proxy.html#FaviconProxyConfig.favicon)[¶](#searx.favicons.proxy.FaviconProxyConfig.favicon "Link to this definition")

    :   Returns pathname and mimetype of the default favicon.

    [[favicon_data_url]][(]*[[\*\*]][[replacements]]*[)][[[\[source\]]]](../_modules/searx/favicons/proxy.html#FaviconProxyConfig.favicon_data_url)[¶](#searx.favicons.proxy.FaviconProxyConfig.favicon_data_url "Link to this definition")

    :   Returns data image URL of the default favicon.

```
<!-- -->
```

[[searx.favicons.proxy.]][[favicon_proxy]][(][)][[[\[source\]]]](../_modules/searx/favicons/proxy.html#favicon_proxy)[¶](#searx.favicons.proxy.favicon_proxy "Link to this definition")

:   REST API of SearXNG's favicon proxy service

    ::: 
    ::: highlight
        /favicon_proxy?authority=<...>&h=<...>
    :::
    :::

    [`authority`]:

    :   Domain name [][**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) / see [[`favicon_url`]](#searx.favicons.proxy.favicon_url "searx.favicons.proxy.favicon_url")

    [`h`]:

    :   HMAC [][**RFC 2104**](https://datatracker.ietf.org/doc/html/rfc2104.html), build up from the [[server.secret_key]](../admin/settings/settings_server.html#settings-server) setting.

```
<!-- -->
```

[[searx.favicons.proxy.]][[search_favicon]][(]*[[resolver]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[authority]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[,]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][[[\[source\]]]](../_modules/searx/favicons/proxy.html#search_favicon)[¶](#searx.favicons.proxy.search_favicon "Link to this definition")

:   Sends the request to the favicon resolver and returns a tuple for the favicon. The tuple consists of [`(data,`]` `[`mime)`], if the resolver has not determined a favicon, both values are [`None`].

    [`data`]:

    :   Binary data of the favicon.

    [`mime`]:

    :   Mime type of the favicon.

```
<!-- -->
```

[[searx.favicons.proxy.]][[favicon_url]][(]*[[authority]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/favicons/proxy.html#favicon_url)[¶](#searx.favicons.proxy.favicon_url "Link to this definition")

:   Function to generate the image URL used for favicons in SearXNG's result lists. The [`authority`] argument (aka netloc / [][**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html)) is usually a (sub-) domain name. This function is used in the HTML (jinja) templates.

    ::: 
    ::: highlight
        <div class="favicon">
           <img src="}">
        </div>
    :::
    :::

    The returned URL is a route to [[`favicon_proxy`]](#searx.favicons.proxy.favicon_proxy "searx.favicons.proxy.favicon_proxy") REST API.

    If the favicon is already in the cache, the returned URL is a [data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs) (something like [`data:image/png;base64,...`]). By generating a data url from the [[`cache.FaviconCache`]](#searx.favicons.cache.FaviconCache "searx.favicons.cache.FaviconCache"), additional HTTP roundtripps via the [[`favicon_proxy`]](#searx.favicons.proxy.favicon_proxy "searx.favicons.proxy.favicon_proxy") are saved. However, it must also be borne in mind that data urls are not cached in the client (web browser).

[][]

## [Favicons Resolver](#id9)[¶](#module-searx.favicons.resolvers "Link to this heading")

Implementations of the favicon *resolvers* that are available in the favicon proxy by default. A *resolver* is a function that obtains the favicon from an external source. The *resolver* function receives two arguments ([`domain,`]` `[`timeout`]) and returns a tuple [`(data,`]` `[`mime)`].

[[searx.favicons.resolvers.]][[allesedv]][(]*[[domain]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[timeout]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[,]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][[[\[source\]]]](../_modules/searx/favicons/resolvers.html#allesedv)[¶](#searx.favicons.resolvers.allesedv "Link to this definition")

:   Favicon Resolver from allesedv.com / [https://favicon.allesedv.com/](https://favicon.allesedv.com/)

```
<!-- -->
```

[[searx.favicons.resolvers.]][[duckduckgo]][(]*[[domain]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[timeout]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[,]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][[[\[source\]]]](../_modules/searx/favicons/resolvers.html#duckduckgo)[¶](#searx.favicons.resolvers.duckduckgo "Link to this definition")

:   Favicon Resolver from duckduckgo.com / [https://blog.jim-nielsen.com/2021/displaying-favicons-for-any-domain/](https://blog.jim-nielsen.com/2021/displaying-favicons-for-any-domain/)

```
<!-- -->
```

[[searx.favicons.resolvers.]][[google]][(]*[[domain]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[timeout]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[,]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][[[\[source\]]]](../_modules/searx/favicons/resolvers.html#google)[¶](#searx.favicons.resolvers.google "Link to this definition")

:   Favicon Resolver from google.com

```
<!-- -->
```

[[searx.favicons.resolvers.]][[yandex]][(]*[[domain]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[timeout]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[,]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][[[\[source\]]]](../_modules/searx/favicons/resolvers.html#yandex)[¶](#searx.favicons.resolvers.yandex "Link to this definition")

:   Favicon Resolver from yandex.com

[][]

## [Favicons Cache](#id10)[¶](#module-searx.favicons.cache "Link to this heading")

Implementations for caching favicons.

[[`FaviconCacheConfig`]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig"):

:   Configuration of the favicon cache

[[`FaviconCache`]](#searx.favicons.cache.FaviconCache "searx.favicons.cache.FaviconCache"):

:   Abstract base class for the implementation of a favicon cache.

[[`FaviconCacheSQLite`]](#searx.favicons.cache.FaviconCacheSQLite "searx.favicons.cache.FaviconCacheSQLite"):

:   Favicon cache that manages the favicon BLOBs in a SQLite DB.

[[`FaviconCacheNull`]](#searx.favicons.cache.FaviconCacheNull "searx.favicons.cache.FaviconCacheNull"):

:   Fallback solution if the configured cache cannot be used for system reasons.

------------------------------------------------------------------------

[[searx.favicons.cache.]][[state]][(][)][[[\[source\]]]](../_modules/searx/favicons/cache.html#state)[¶](#searx.favicons.cache.state "Link to this definition")

:   show state of the cache

```
<!-- -->
```

[[searx.favicons.cache.]][[maintenance]][(]*[[force]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[debug]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#maintenance)[¶](#searx.favicons.cache.maintenance "Link to this definition")

:   perform maintenance of the cache

```
<!-- -->
```

[[searx.favicons.cache.]][[init]][(]*[[cfg]][[:]][ ][[[FaviconCacheConfig]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig")]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#init)[¶](#searx.favicons.cache.init "Link to this definition")

:   Initialization of a global [`CACHE`]

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[searx.favicons.cache.]][[FaviconCacheConfig]][(]*[[db_type]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'sqlite\']][[,]][ ][[\'mem\']][[\]]]][ ][[=]][ ][[\'sqlite\']]*, *[[db_url]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'/tmp/faviconcache.db\']]*, *[[HOLD_TIME]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[2592000]]*, *[[LIMIT_TOTAL_BYTES]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[52428800]]*, *[[BLOB_MAX_BYTES]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[20480]]*, *[[MAINTENANCE_PERIOD]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[3600]]*, *[[MAINTENANCE_MODE]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'auto\']][[,]][ ][[\'off\']][[\]]]][ ][[=]][ ][[\'auto\']]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheConfig)[¶](#searx.favicons.cache.FaviconCacheConfig "Link to this definition")

:   Configuration of the favicon cache.

    [[db_type]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'sqlite\']][[,]][ ][[\'mem\']][[\]]]*[¶](#searx.favicons.cache.FaviconCacheConfig.db_type "Link to this definition")

    :   Type of the database:

        [`sqlite`]:

        :   [[`cache.FaviconCacheSQLite`]](#searx.favicons.cache.FaviconCacheSQLite "searx.favicons.cache.FaviconCacheSQLite")

        [`mem`]:

        :   [[`cache.FaviconCacheMEM`]](#searx.favicons.cache.FaviconCacheMEM "searx.favicons.cache.FaviconCacheMEM") (not recommended)

    [[db_url]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.favicons.cache.FaviconCacheConfig.db_url "Link to this definition")

    :   URL of the SQLite DB, the path to the database file.

    [[HOLD_TIME]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.cache.FaviconCacheConfig.HOLD_TIME "Link to this definition")

    :   Hold time (default in sec.), after which a BLOB is removed from the cache.

    [[LIMIT_TOTAL_BYTES]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.cache.FaviconCacheConfig.LIMIT_TOTAL_BYTES "Link to this definition")

    :   Maximum of bytes (default) stored in the cache of all blobs. Note: The limit is only reached at each maintenance interval after which the oldest BLOBs are deleted; the limit is exceeded during the maintenance period. If the maintenance period is *too long* or maintenance is switched off completely, the cache grows uncontrollably.

    [[BLOB_MAX_BYTES]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.cache.FaviconCacheConfig.BLOB_MAX_BYTES "Link to this definition")

    :   The maximum BLOB size in bytes that a favicon may have so that it can be saved in the cache. If the favicon is larger, it is not saved in the cache and must be requested by the client via the proxy.

    [[MAINTENANCE_PERIOD]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.cache.FaviconCacheConfig.MAINTENANCE_PERIOD "Link to this definition")

    :   Maintenance period in seconds / when [[`MAINTENANCE_MODE`]](#searx.favicons.cache.FaviconCacheConfig.MAINTENANCE_MODE "searx.favicons.cache.FaviconCacheConfig.MAINTENANCE_MODE") is set to [`auto`].

    [[MAINTENANCE_MODE]]*[[:]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'auto\']][[,]][ ][[\'off\']][[\]]]*[¶](#searx.favicons.cache.FaviconCacheConfig.MAINTENANCE_MODE "Link to this definition")

    :   Type of maintenance mode

        [`auto`]:

        :   Maintenance is carried out automatically as part of the maintenance intervals ([[`MAINTENANCE_PERIOD`]](#searx.favicons.cache.FaviconCacheConfig.MAINTENANCE_PERIOD "searx.favicons.cache.FaviconCacheConfig.MAINTENANCE_PERIOD")); no external process is required.

        [`off`]:

        :   Maintenance is switched off and must be carried out by an external process if required.

```
<!-- -->
```

*[[class]][ ]*[[searx.favicons.cache.]][[FaviconCacheStats]][(]*[favicons:] [int] [\|] [None] [=] [None,] [bytes:] [int] [\|] [None] [=] [None,] [domains:] [int] [\|] [None] [=] [None,] [resolvers:] [int] [\|] [None] [=] [None,] [field_descr:] [tuple\[tuple\[str,] [str,] [\~typing.Callable\[\[int,] [int\],] [str\]] [\|] [type\],] [\...\]] [=] [((\'favicons\',] [\'number] [of] [favicons] [in] [cache\',] [\<function] [humanize_number\>),] [(\'bytes\',] [\'total] [size] [(approx.] [bytes)] [of] [cache\',] [\<function] [humanize_bytes\>),] [(\'domains\',] [\'total] [number] [of] [domains] [in] [cache\',] [\<function] [humanize_number\>),] [(\'resolvers\',] [\'number] [of] [resolvers\',] [\<class] [\'str\'\>))]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheStats)[¶](#searx.favicons.cache.FaviconCacheStats "Link to this definition")

:   Dataclass which provides information on the status of the cache.

```
<!-- -->
```

*[[class]][ ]*[[searx.favicons.cache.]][[FaviconCache]][(]*[[cfg]][[:]][ ][[[FaviconCacheConfig]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig")]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCache)[¶](#searx.favicons.cache.FaviconCache "Link to this definition")

:   Abstract base class for the implementation of a favicon cache.

    *[[abstractmethod]][ ]*[[set]][(]*[[resolver]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[authority]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[mime]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[data]][[:]][ ][[[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCache.set)[¶](#searx.favicons.cache.FaviconCache.set "Link to this definition")

    :   Set data and mime-type in the cache. If data is None, the [`FALLBACK_ICON`] is registered. in the cache.

    *[[abstractmethod]][ ]*[[state]][(][)] [[→] [[[FaviconCacheStats]](#searx.favicons.cache.FaviconCacheStats "searx.favicons.cache.FaviconCacheStats")]][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCache.state)[¶](#searx.favicons.cache.FaviconCache.state "Link to this definition")

    :   Returns a [[`FaviconCacheStats`]](#searx.favicons.cache.FaviconCacheStats "searx.favicons.cache.FaviconCacheStats") (key/values) with information on the state of the cache.

    *[[abstractmethod]][ ]*[[maintenance]][(]*[[force]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCache.maintenance)[¶](#searx.favicons.cache.FaviconCache.maintenance "Link to this definition")

    :   Performs maintenance on the cache

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[searx.favicons.cache.]][[FaviconCacheNull]][(]*[[cfg]][[:]][ ][[[FaviconCacheConfig]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig")]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheNull)[¶](#searx.favicons.cache.FaviconCacheNull "Link to this definition")

:   A dummy favicon cache that caches nothing / a fallback solution. The NullCache is used when more efficient caches such as the [[`FaviconCacheSQLite`]](#searx.favicons.cache.FaviconCacheSQLite "searx.favicons.cache.FaviconCacheSQLite") cannot be used because, for example, the SQLite library is only available in an old version and does not meet the requirements.

    [[set]][(]*[[resolver]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[authority]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[mime]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[data]][[:]][ ][[[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheNull.set)[¶](#searx.favicons.cache.FaviconCacheNull.set "Link to this definition")

    :   Set data and mime-type in the cache. If data is None, the [`FALLBACK_ICON`] is registered. in the cache.

    [[state]][(][)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheNull.state)[¶](#searx.favicons.cache.FaviconCacheNull.state "Link to this definition")

    :   Returns a [[`FaviconCacheStats`]](#searx.favicons.cache.FaviconCacheStats "searx.favicons.cache.FaviconCacheStats") (key/values) with information on the state of the cache.

    [[maintenance]][(]*[[force]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheNull.maintenance)[¶](#searx.favicons.cache.FaviconCacheNull.maintenance "Link to this definition")

    :   Performs maintenance on the cache

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[searx.favicons.cache.]][[FaviconCacheSQLite]][(]*[[cfg]][[:]][ ][[[FaviconCacheConfig]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig")]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheSQLite)[¶](#searx.favicons.cache.FaviconCacheSQLite "Link to this definition")

:   Favicon cache that manages the favicon BLOBs in a SQLite DB. The DB model in the SQLite DB is implemented using the abstract class [`sqlitedb.SQLiteAppl`].

    For introspection of the DB, jump into developer environment and run command to show cache state:

    ::: 
    ::: highlight
        $ ./manage pyenv.cmd bash --norc --noprofile
        (py3) python -m searx.favicons cache state
    :::
    :::

    The following configurations are required / supported:

    -   [[`FaviconCacheConfig.db_url`]](#searx.favicons.cache.FaviconCacheConfig.db_url "searx.favicons.cache.FaviconCacheConfig.db_url")

    -   [[`FaviconCacheConfig.HOLD_TIME`]](#searx.favicons.cache.FaviconCacheConfig.HOLD_TIME "searx.favicons.cache.FaviconCacheConfig.HOLD_TIME")

    -   [[`FaviconCacheConfig.LIMIT_TOTAL_BYTES`]](#searx.favicons.cache.FaviconCacheConfig.LIMIT_TOTAL_BYTES "searx.favicons.cache.FaviconCacheConfig.LIMIT_TOTAL_BYTES")

    -   [[`FaviconCacheConfig.BLOB_MAX_BYTES`]](#searx.favicons.cache.FaviconCacheConfig.BLOB_MAX_BYTES "searx.favicons.cache.FaviconCacheConfig.BLOB_MAX_BYTES")

    -   [`MAINTENANCE_PERIOD`]

    -   [`MAINTENANCE_MODE`]

    [[DB_SCHEMA]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[=]][ ][1]*[¶](#searx.favicons.cache.FaviconCacheSQLite.DB_SCHEMA "Link to this definition")

    :   As soon as changes are made to the DB schema, the version number must be increased. Changes to the version number require the DB to be recreated (or migrated / if an migration path exists and is implemented).

    [[DDL_BLOBS]]*[ ][[=]][ ][\'CREATE] [TABLE] [IF] [NOT] [EXISTS] [blobs] [(\\n]  [sha256]     [TEXT,\\n]  [bytes_c]    [INTEGER,\\n]  [mime]       [TEXT] [NOT] [NULL,\\n]  [data]       [BLOB] [NOT] [NULL,\\n]  [PRIMARY] [KEY] [(sha256))\']*[¶](#searx.favicons.cache.FaviconCacheSQLite.DDL_BLOBS "Link to this definition")

    :   Table to store BLOB objects by their sha256 hash values.

    [[DDL_BLOB_MAP]]*[ ][[=]][ ][\"CREATE] [TABLE] [IF] [NOT] [EXISTS] [blob_map] [(\\n]    [m_time]     [INTEGER] [DEFAULT] [(strftime(\'%s\',] [\'now\')),]  [\--] [last] [modified] [(unix] [epoch)] [time] [in] [sec.\\n]    [sha256]     [TEXT,\\n]    [resolver]   [TEXT,\\n]    [authority]  [TEXT,\\n]    [PRIMARY] [KEY] [(resolver,] [authority))\"]*[¶](#searx.favicons.cache.FaviconCacheSQLite.DDL_BLOB_MAP "Link to this definition")

    :   Table to map from (resolver, authority) to sha256 hash values.

    [[SQL_DROP_LEFTOVER_BLOBS]]*[ ][[=]][ ][\'DELETE] [FROM] [blobs] [WHERE] [sha256] [IN] [(] [SELECT] [b.sha256]   [FROM] [blobs] [b]   [LEFT] [JOIN] [blob_map] [bm]     [ON] [b.sha256] [=] [bm.sha256]  [WHERE] [bm.sha256] [IS] [NULL)\']*[¶](#searx.favicons.cache.FaviconCacheSQLite.SQL_DROP_LEFTOVER_BLOBS "Link to this definition")

    :   Delete blobs.sha256 (BLOBs) no longer in blob_map.sha256.

    [[set]][(]*[[resolver]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[authority]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[mime]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[data]][[:]][ ][[[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheSQLite.set)[¶](#searx.favicons.cache.FaviconCacheSQLite.set "Link to this definition")

    :   Set data and mime-type in the cache. If data is None, the [`FALLBACK_ICON`] is registered. in the cache.

    *[[property]][ ]*[[next_maintenance_time]]*[[:]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[¶](#searx.favicons.cache.FaviconCacheSQLite.next_maintenance_time "Link to this definition")

    :   Returns (unix epoch) time of the next maintenance.

    [[maintenance]][(]*[[force]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheSQLite.maintenance)[¶](#searx.favicons.cache.FaviconCacheSQLite.maintenance "Link to this definition")

    :   Performs maintenance on the cache

    [[state]][(][)] [[→] [[[FaviconCacheStats]](#searx.favicons.cache.FaviconCacheStats "searx.favicons.cache.FaviconCacheStats")]][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheSQLite.state)[¶](#searx.favicons.cache.FaviconCacheSQLite.state "Link to this definition")

    :   Returns a [[`FaviconCacheStats`]](#searx.favicons.cache.FaviconCacheStats "searx.favicons.cache.FaviconCacheStats") (key/values) with information on the state of the cache.

```
<!-- -->
```

*[[final]][ ][[class]][ ]*[[searx.favicons.cache.]][[FaviconCacheMEM]][(]*[[cfg]][[:]][ ][[[FaviconCacheConfig]](#searx.favicons.cache.FaviconCacheConfig "searx.favicons.cache.FaviconCacheConfig")]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheMEM)[¶](#searx.favicons.cache.FaviconCacheMEM "Link to this definition")

:   Favicon cache in process' memory. Its just a POC that stores the favicons in the memory of the process.

    ::: 
    Attention

    Don't use it in production, it will blow up your memory!!
    :::

    [[set]][(]*[[resolver]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[authority]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[mime]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[data]][[:]][ ][[[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheMEM.set)[¶](#searx.favicons.cache.FaviconCacheMEM.set "Link to this definition")

    :   Set data and mime-type in the cache. If data is None, the [`FALLBACK_ICON`] is registered. in the cache.

    [[state]][(][)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheMEM.state)[¶](#searx.favicons.cache.FaviconCacheMEM.state "Link to this definition")

    :   Returns a [[`FaviconCacheStats`]](#searx.favicons.cache.FaviconCacheStats "searx.favicons.cache.FaviconCacheStats") (key/values) with information on the state of the cache.

    [[maintenance]][(]*[[force]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][[[\[source\]]]](../_modules/searx/favicons/cache.html#FaviconCacheMEM.maintenance)[¶](#searx.favicons.cache.FaviconCacheMEM.maintenance "Link to this definition")

    :   Performs maintenance on the cache