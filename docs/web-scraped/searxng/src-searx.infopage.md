# Source: https://docs.searxng.org/src/searx.infopage.html

[][]

# Online [`/info`][¶](#module-searx.infopage "Link to this heading")

Render SearXNG instance documentation.

Usage in a Flask app route:

    from searx import infopage
    from searx.extended_types import sxng_request

    _INFO_PAGES = infopage.InfoPageSet(infopage.MistletoePage)

    @app.route('/info/<pagename>', methods=['GET'])
    def info(pagename):

        locale = sxng_request.preferences.get_value('locale')
        page = _INFO_PAGES.get_page(pagename, locale)

*[[class]][ ]*[[searx.infopage.]][[InfoPage]][(]*[[fname]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)][[[\[source\]]]](../_modules/searx/infopage.html#InfoPage)[¶](#searx.infopage.InfoPage "Link to this definition")

:   A page of the [[`online`]` `[`documentation`]](#searx.infopage.InfoPageSet "searx.infopage.InfoPageSet").

    *[[property]][ ]*[[raw_content]][[[\[source\]]]](../_modules/searx/infopage.html#InfoPage.raw_content)[¶](#searx.infopage.InfoPage.raw_content "Link to this definition")

    :   Raw content of the page (without any jinja rendering)

    *[[property]][ ]*[[content]][[[\[source\]]]](../_modules/searx/infopage.html#InfoPage.content)[¶](#searx.infopage.InfoPage.content "Link to this definition")

    :   Content of the page (rendered in a Jinja context)

    *[[property]][ ]*[[title]][[[\[source\]]]](../_modules/searx/infopage.html#InfoPage.title)[¶](#searx.infopage.InfoPage.title "Link to this definition")

    :   Title of the content (without any markup)

    *[[property]][ ]*[[html]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[[[\[source\]]]](../_modules/searx/infopage.html#InfoPage.html)[¶](#searx.infopage.InfoPage.html "Link to this definition")

    :   Render Markdown ([CommonMark](https://commonmark.org/)) to HTML by using [markdown-it-py](https://github.com/executablebooks/markdown-it-py).

    [[get_ctx]][(][)] [[→] [[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][[[\[source\]]]](../_modules/searx/infopage.html#InfoPage.get_ctx)[¶](#searx.infopage.InfoPage.get_ctx "Link to this definition")

    :   Jinja context to render [[`InfoPage.content`]](#searx.infopage.InfoPage.content "searx.infopage.InfoPage.content")

```
<!-- -->
```

*[[class]][ ]*[[searx.infopage.]][[InfoPageSet]][(]*[[page_class]][[:]][ ][[[type]](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[\[]][[InfoPage]](#searx.infopage.InfoPage "searx.infopage.InfoPage")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[info_folder]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/searx/infopage.html#InfoPageSet)[¶](#searx.infopage.InfoPageSet "Link to this definition")

:   Cached rendering of the online documentation a SearXNG instance has.

    Parameters[:]

    :   -   **page_class** ([[`InfoPage`]](#searx.infopage.InfoPage "searx.infopage.InfoPage")) -- render online documentation by [[`InfoPage`]](#searx.infopage.InfoPage "searx.infopage.InfoPage") parser.

        -   **info_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- information directory

    [[folder]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.infopage.InfoPageSet.folder "Link to this definition")

    :   location of the Markdown files

    [[locale_default]]*[[:]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[¶](#searx.infopage.InfoPageSet.locale_default "Link to this definition")

    :   default language

    [[locales]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.infopage.InfoPageSet.locales "Link to this definition")

    :   list of supported languages (aka locales)

    [[toc]]*[[:]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]*[¶](#searx.infopage.InfoPageSet.toc "Link to this definition")

    :   list of articles in the online documentation

    [[get_page]][(]*[[pagename]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[locale]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/searx/infopage.html#InfoPageSet.get_page)[¶](#searx.infopage.InfoPageSet.get_page "Link to this definition")

    :   Return [`pagename`] instance of [[`InfoPage`]](#searx.infopage.InfoPage "searx.infopage.InfoPage")

        Parameters[:]

        :   -   **pagename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- name of the page, a value from [[`InfoPageSet.toc`]](#searx.infopage.InfoPageSet.toc "searx.infopage.InfoPageSet.toc")

            -   **locale** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- language of the page, e.g. [`en`], [`zh_Hans_CN`] (default: [`InfoPageSet.i18n_origin`])

    [[iter_pages]][(]*[[locale]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[fallback_to_default]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][[[\[source\]]]](../_modules/searx/infopage.html#InfoPageSet.iter_pages)[¶](#searx.infopage.InfoPageSet.iter_pages "Link to this definition")

    :   Iterate over all pages of the TOC