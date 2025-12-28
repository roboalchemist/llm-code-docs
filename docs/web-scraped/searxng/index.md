# Source: https://docs.searxng.org/index.html

# Welcome to SearXNG[¶](#welcome-to-searxng "Link to this heading")

> <div>
>
> *Search without being tracked.*
>
> </div>

SearXNG is a free internet metasearch engine which aggregates results from up to 247 [[search services]](user/configured_engines.html#configured-engines). Users are neither tracked nor profiled. Additionally, SearXNG can be used over Tor for online anonymity.

Get started with SearXNG by using one of the instances listed at [searx.space](https://searx.space). If you don't trust anyone, you can set up your own, see [[Installation]](admin/installation.html#installation).

features

-   [[self hosted]](admin/installation.html#installation)

-   [[no user tracking / no profiling]](own-instance.html#searxng-protect-privacy)

-   script & cookies are optional

-   secure, encrypted connections

-   [[247 search engines]](user/configured_engines.html#configured-engines)

-   [58 translations](https://translate.codeberg.org/projects/searxng/searxng/)

-   about 70 [well maintained](https://uptime.searxng.org/) instances on [searx.space](https://searx.space)

-   [[easy integration of search engines]](dev/engines/demo/demo_online.html#demo-online-engine)

-   professional development: [CI](https://github.com/searxng/searxng/actions), [quality assurance](https://dev.searxng.org/) & [automated tested UI](https://dev.searxng.org/screenshots.html)

be a part

SearXNG is driven by an open community, come join us! Don't hesitate, no need to be an *expert*, everyone can contribute:

-   [help to improve translations](https://translate.codeberg.org/projects/searxng/searxng/)

-   [discuss with the community](https://matrix.to/#/#searxng:matrix.org)

-   report bugs & suggestions

-   ...

the origin

SearXNG development has been started in the middle of 2021 as a fork of the searx project.

-   [User information](user/index.html)
    -   [Search syntax](user/search-syntax.html)
    -   [Configured Engines](user/configured_engines.html)
    -   [About SearXNG](user/about.html)
-   [Why use a private instance?](own-instance.html)
    -   [How does SearXNG protect privacy?](own-instance.html#how-does-searxng-protect-privacy)
    -   [Conclusion](own-instance.html#conclusion)
-   [Administrator documentation](admin/index.html)
    -   [Settings](admin/settings/index.html)
    -   [Installation](admin/installation.html)
    -   [Installation container](admin/installation-docker.html)
    -   [Installation Script](admin/installation-scripts.html)
    -   [Step by step installation](admin/installation-searxng.html)
    -   [Granian](admin/installation-granian.html)
    -   [uWSGI](admin/installation-uwsgi.html)
    -   [NGINX](admin/installation-nginx.html)
    -   [Apache](admin/installation-apache.html)
    -   [SearXNG maintenance](admin/update-searxng.html)
    -   [Answer CAPTCHA from server's IP](admin/answer-captcha.html)
    -   [Favicons](admin/searx.favicons.html)
    -   [Limiter](admin/searx.limiter.html)
    -   [Administration API](admin/api.html)
    -   [Architecture](admin/architecture.html)
    -   [List of plugins](admin/plugins.html)
    -   [Buildhosts](admin/buildhosts.html)
-   [Developer documentation](dev/index.html)
    -   [Development Quickstart](dev/quickstart.html)
    -   [Git Commits & Change Management](dev/commits.html)
    -   [How to contribute](dev/contribution_guide.html)
    -   [Extended Types](dev/extended_types.html)
    -   [Engine Implementations](dev/engines/index.html)
    -   [Result Types](dev/result_types/index.html)
    -   [Simple Theme Templates](dev/templates.html)
    -   [Search API](dev/search_api.html)
    -   [Plugins](dev/plugins/index.html)
    -   [Answerers](dev/answerers/index.html)
    -   [Translation](dev/translation.html)
    -   [Makefile & [`./manage`]](dev/makefile.html)
    -   [reST primer](dev/reST.html)
    -   [Tooling box [`searxng_extra`]](dev/searxng_extra/index.html)
-   [DevOps tooling box](utils/index.html)
    -   [[`utils/searxng.sh`]](utils/searxng.sh.html)
    -   [Common command environments](utils/index.html#common-command-environments)
-   [Source-Code](src/index.html)
    -   [Custom message extractor (i18n)](src/searx.babel_extract.html)
    -   [Bot Detection](src/searx.botdetection.html)
    -   [Caches](src/searx.cache.html)
    -   [SearXNG Exceptions](src/searx.exceptions.html)
    -   [Favicons (source)](src/searx.favicons.html)
    -   [Online [`/info`]](src/searx.infopage.html)
    -   [Locales](src/searx.locales.html)
    -   [Search](src/searx.search.html)
    -   [Search processors](src/searx.search.processors.html)
    -   [Settings Loader](src/searx.settings.html)
    -   [SQLite DB](src/searx.sqlitedb.html)
    -   [Utility functions for the engines](src/searx.utils.html)
    -   [Valkey DB](src/searx.valkeydb.html)
    -   [Valkey Library](src/searx.valkeylib.html)
    -   [Weather](src/searx.weather.html)

## Acknowledgements[¶](#acknowledgements "Link to this heading")

The following organizations have provided SearXNG access to their paid plans at no cost:

  ---------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  [![Docker](_images/docker.svg)](https://docker.com)                     [![Tuta](_images/tuta.svg)](https://tuta.com)

  [![BrowserStack](_images/browserstack.svg)](https://browserstack.com)   
  ---------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------