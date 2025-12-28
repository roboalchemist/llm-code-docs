# Source: https://docs.searxng.org/dev/engines/index.html

[]

# Engine Implementations[¶](#engine-implementations "Link to this heading")

-   [ResultList and engines](#resultlist-and-engines)

-   [Engine Types](#engine-types)

    -   [Online Engines](#online-engines)

    -   [Offline Engines](#offline-engines)

    -   [Online URL Search](#online-url-search)

    -   [Online Currency](#online-currency)

    -   [Online Dictionary](#online-dictionary)

[Framework Components]

-   [Engine Library](enginelib.html)
    -   [[`EngineCache`]](enginelib.html#searx.enginelib.EngineCache)
    -   [[`Engine`]](enginelib.html#searx.enginelib.Engine)
    -   [[`ENGINES_CACHE`]](enginelib.html#searx.enginelib.ENGINES_CACHE)
    -   [Engine traits](enginelib.html#module-searx.enginelib.traits)
-   [SearXNG's engines loader](engines.html)
    -   [[`engines`]](engines.html#searx.engines.engines)
    -   [[`engine_shortcuts`]](engines.html#searx.engines.engine_shortcuts)
    -   [[`load_engine()`]](engines.html#searx.engines.load_engine)
    -   [[`is_missing_required_attributes()`]](engines.html#searx.engines.is_missing_required_attributes)
    -   [[`using_tor_proxy()`]](engines.html#searx.engines.using_tor_proxy)
    -   [[`load_engines()`]](engines.html#searx.engines.load_engines)
-   [Engine Overview](engine_overview.html)
    -   [General Engine Configuration](engine_overview.html#general-engine-configuration)
    -   [Making a Request](engine_overview.html#making-a-request)
    -   [Making a Response](engine_overview.html#making-a-response)

## [ResultList and engines](#id7)[¶](#resultlist-and-engines "Link to this heading")

*[[class]][ ]*[[searx.result_types.]][[ResultList]][[[\[source\]]]](../../_modules/searx/result_types.html#ResultList)[¶](#searx.result_types.ResultList "Link to this definition")

:   Base class of all result lists (abstract).

```
<!-- -->
```

*[[class]][ ]*[[searx.result_types.]][[EngineResults]][[[\[source\]]]](../../_modules/searx/result_types.html#EngineResults)[¶](#searx.result_types.EngineResults "Link to this definition")

:   Result list that should be used by engine developers. For convenience, engine developers don't need to import types / see [`ResultList.types`].

    ::: 
    ::: highlight
        from searx.result_types import EngineResults
        ...
        def response(resp) -> EngineResults:
            res = EngineResults()
            ...
            res.add( res.types.Answer(answer="lorem ipsum ..", url="https://example.org") )
            ...
            return res
    :::
    :::

## [Engine Types](#id8)[¶](#engine-types "Link to this heading")

The [[`engine_type`]](enginelib.html#searx.enginelib.Engine.engine_type "searx.enginelib.Engine.engine_type") of an engine determines which [[search processor]](../../src/searx.search.processors.html#searx-search-processors) is used by the engine.

In this section a list of the engines that are documented is given, a complete list of the engines can be found in the source under: [git://searx/engines](https://github.com/searxng/searxng/blob/master/searx/engines).

[]

### [Online Engines](#id9)[¶](#online-engines "Link to this heading")

info

-   [[`processors.online`]](../../src/searx.search.processors.html#module-searx.search.processors.online "searx.search.processors.online")

-   [Demo Online Engine](demo/demo_online.html)
-   [XPath Engine](xpath.html)
-   [MediaWiki Engine](mediawiki.html)
-   [JSON Engine](json_engine.html)

-   [Adobe Stock](online/adobe_stock.html)
-   [Alpine Linux Packages](online/alpinelinux.html)
-   [Anna's Archive](online/annas_archive.html)
-   [Arch Linux](online/archlinux.html)
-   [arXiv](online/arxiv.html)
-   [Astrophysics Data System (ADS)](online/astrophysics_data_system.html)
-   [Azure Resources](online/azure.html)
-   [Bing Engines](online/bing.html)
-   [Bpb](online/bpb.html)
-   [Brave Engines](online/brave.html)
-   [BT4G](online/bt4g.html)
-   [ChinaSo](online/chinaso.html)
-   [CORE](online/core.html)
-   [Crossref](online/crossref.html)
-   [Dailymotion](online/dailymotion.html)
-   [Discourse Forums](online/discourse.html)
-   [DuckDuckGo Engines](online/duckduckgo.html)
-   [Geizhals](online/geizhals.html)
-   [Gitea](online/gitea.html)
-   [Github Code](online/github_code.html)
-   [GitLab](online/gitlab.html)
-   [Google Engines](online/google.html)
-   [Hugging Face](online/huggingface.html)
-   [Lemmy](online/lemmy.html)
-   [Library of Congress](online/loc.html)
-   [Marginalia Search](online/marginalia.html)
-   [Mastodon](online/mastodon.html)
-   [Moviepilot](online/moviepilot.html)
-   [Matrix Rooms Search (MRS)](online/mrs.html)
-   [Mwmbl Engine](online/mwmbl.html)
-   [Odysee](online/odysee.html)
-   [OpenAlex](online/openalex.html)
-   [Open Library](online/openlibrary.html)
-   [Peertube Engines](online/peertube.html)
-   [Piped](online/piped.html)
-   [Presearch Engine](online/presearch.html)
-   [PubMed](online/pubmed.html)
-   [Qwant](online/qwant.html)
-   [RadioBrowser](online/radio_browser.html)
-   [Recoll Engine](online/recoll.html)
-   [Repology](online/repology.html)
-   [Reuters](online/reuters.html)
-   [Seekr Engines](online/seekr.html)
-   [Semantic Scholar](online/semantic_scholar.html)
-   [Soundcloud](online/soundcloud.html)
-   [Sourcehut](online/sourcehut.html)
-   [Springer Nature](online/springer.html)
-   [Startpage Engines](online/startpage.html)
-   [Tagesschau API](online/tagesschau.html)
-   [Torznab WebAPI](online/torznab.html)
-   [Tube Archivist](online/tubearchivist.html)
-   [Void Linux binary packages](online/void.html)
-   [Wallhaven](online/wallhaven.html)
-   [Wikimedia](online/wikipedia.html)
-   [Yacy](online/yacy.html)
-   [Yahoo Engine](online/yahoo.html)
-   [Z-Library](online/zlibrary.html)

[]

### [Offline Engines](#id10)[¶](#offline-engines "Link to this heading")

info

-   [[`processors.offline`]](../../src/searx.search.processors.html#module-searx.search.processors.offline "searx.search.processors.offline")

-   [Offline Concept](offline_concept.html)
-   [Demo Offline Engine](demo/demo_offline.html)
-   [Command Line Engines](offline/command-line-engines.html)
-   [NoSQL databases](offline/nosql-engines.html)
-   [Local Search APIs](offline/search-indexer-engines.html)
-   [SQL Engines](offline/sql-engines.html)

[]

### [Online URL Search](#id11)[¶](#online-url-search "Link to this heading")

info

-   [[`processors.online_url_search`]](../../src/searx.search.processors.html#module-searx.search.processors.online_url_search "searx.search.processors.online_url_search")

-   [Tineye](online_url_search/tineye.html)

[]

### [Online Currency](#id12)[¶](#online-currency "Link to this heading")

info

-   [[`processors.online_currency`]](../../src/searx.search.processors.html#module-searx.search.processors.online_currency "searx.search.processors.online_currency")

*no engine of this type is documented yet / coming soon*

[]

### [Online Dictionary](#id13)[¶](#online-dictionary "Link to this heading")

info

-   [[`processors.online_dictionary`]](../../src/searx.search.processors.html#module-searx.search.processors.online_dictionary "searx.search.processors.online_dictionary")

*no engine of this type is documented yet / coming soon*