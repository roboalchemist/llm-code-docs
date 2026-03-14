# Source: https://loguru.readthedocs.io/en/stable/api.html

Title: API Reference — loguru documentation

URL Source: https://loguru.readthedocs.io/en/stable/api.html

Markdown Content:
API Reference — loguru documentation
===============

[loguru](https://loguru.readthedocs.io/en/stable/index.html)

*   [Overview](https://loguru.readthedocs.io/en/stable/overview.html)
*   [API Reference](https://loguru.readthedocs.io/en/stable/api.html#)
    *   [`loguru.logger`](https://loguru.readthedocs.io/en/stable/api/logger.html)
    *   [Type Hints](https://loguru.readthedocs.io/en/stable/api/type_hints.html)

*   [Help & Guides](https://loguru.readthedocs.io/en/stable/resources.html)
*   [Project Information](https://loguru.readthedocs.io/en/stable/project.html)

[![Image 1: Sponsored: Augment](https://media.ethicalads.io/media/images/2026/01/cropped_2Hd7jQi.png)](https://server.ethicalads.io/proxy/click/10134/019cdf47-cb28-7bd3-acd0-93e3e4b4a8a5/)

[**Still Using Cursor?**Fix bugs faster with Augment's full-codebase context.**Install Now**](https://server.ethicalads.io/proxy/click/10134/019cdf47-cb28-7bd3-acd0-93e3e4b4a8a5/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=rtd-sidebar-buy-ads)

![Image 2](https://server.ethicalads.io/proxy/view/10134/019cdf47-cb28-7bd3-acd0-93e3e4b4a8a5/)

[loguru](https://loguru.readthedocs.io/en/stable/index.html)

*   [](https://loguru.readthedocs.io/en/stable/index.html)
*   API Reference

* * *

API Reference[](https://loguru.readthedocs.io/en/stable/api.html#module-loguru "Link to this heading")
=======================================================================================================

The Loguru library provides a pre-instanced logger to facilitate dealing with logging in Python.

Just `from loguru import logger`.

*   [`Logger`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger "loguru._logger.Logger")

> *   [`add()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.add "loguru._logger.Logger.add")
> 
> 
> > *   [The sink parameter](https://loguru.readthedocs.io/en/stable/api/logger.html#sink)
> > 
> >         *   [The logged message](https://loguru.readthedocs.io/en/stable/api/logger.html#message)
> > 
> >         *   [The severity levels](https://loguru.readthedocs.io/en/stable/api/logger.html#levels)
> > 
> >         *   [The record dict](https://loguru.readthedocs.io/en/stable/api/logger.html#record)
> > 
> >         *   [The time formatting](https://loguru.readthedocs.io/en/stable/api/logger.html#time)
> > 
> >         *   [The file sinks](https://loguru.readthedocs.io/en/stable/api/logger.html#file)
> > 
> >         *   [The color markups](https://loguru.readthedocs.io/en/stable/api/logger.html#color)
> > 
> >         *   [The environment variables](https://loguru.readthedocs.io/en/stable/api/logger.html#env)
> 
>     *   [`remove()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.remove "loguru._logger.Logger.remove")
> 
>     *   [`complete()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.complete "loguru._logger.Logger.complete")
> 
>     *   [`catch()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.catch "loguru._logger.Logger.catch")
> 
>     *   [`opt()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.opt "loguru._logger.Logger.opt")
> 
>     *   [`bind()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.bind "loguru._logger.Logger.bind")
> 
>     *   [`contextualize()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.contextualize "loguru._logger.Logger.contextualize")
> 
>     *   [`patch()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.patch "loguru._logger.Logger.patch")
> 
>     *   [`level()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.level "loguru._logger.Logger.level")
> 
>     *   [`disable()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.disable "loguru._logger.Logger.disable")
> 
>     *   [`enable()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.enable "loguru._logger.Logger.enable")
> 
>     *   [`configure()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.configure "loguru._logger.Logger.configure")
> 
>     *   [`parse()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.parse "loguru._logger.Logger.parse")
> 
>     *   [`trace()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.trace "loguru._logger.Logger.trace")
> 
>     *   [`debug()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.debug "loguru._logger.Logger.debug")
> 
>     *   [`info()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.info "loguru._logger.Logger.info")
> 
>     *   [`success()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.success "loguru._logger.Logger.success")
> 
>     *   [`warning()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.warning "loguru._logger.Logger.warning")
> 
>     *   [`error()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.error "loguru._logger.Logger.error")
> 
>     *   [`critical()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.critical "loguru._logger.Logger.critical")
> 
>     *   [`log()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.log "loguru._logger.Logger.log")
> 
>     *   [`exception()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.exception "loguru._logger.Logger.exception")

*   [Type Hints](https://loguru.readthedocs.io/en/stable/api/type_hints.html#type-hints)

[Previous](https://loguru.readthedocs.io/en/stable/overview.html "Overview")[Next](https://loguru.readthedocs.io/en/stable/api/logger.html "loguru.logger")

* * *

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
