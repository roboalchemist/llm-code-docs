# Source: https://www.mkdocs.org/user-guide/localizing-your-theme/

[MkDocs](../..)

[]

-   [Home](../..)
-   [Getting Started](../../getting-started/)
-   [User Guide ](#)
    -   [User Guide](../)
    -   [Installation](../installation/)
    -   [Writing Your Docs](../writing-your-docs/)
    -   [Choosing Your Theme](../choosing-your-theme/)
    -   [Customizing Your Theme](../customizing-your-theme/)
    -   [Localizing Your Theme](./)
    -   [Configuration](../configuration/)
    -   [Command Line Interface](../cli/)
    -   [Deploying Your Docs](../deploying-your-docs/)
-   [Developer Guide ](#)
    -   [Developer Guide](../../dev-guide/)
    -   [Themes](../../dev-guide/themes/)
    -   [Translations](../../dev-guide/translations/)
    -   [Plugins](../../dev-guide/plugins/)
    -   [API Reference](../../dev-guide/api/)
-   [About ](#)
    -   [Release Notes](../../about/release-notes/)
    -   [Contributing](../../about/contributing/)
    -   [License](../../about/license/)

```
<!-- -->
```
-   [ Search](#)
-   [ Previous](../customizing-your-theme/)
-   [Next ](../configuration/)
-   [ Edit on GitHub](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/localizing-your-theme.md)

[]

-   [Localizing Your Theme](#localizing-your-theme)
    -   [Installation](#installation)
    -   [Supported locales](#supported-locales)
    -   [Usage](#usage)
    -   [Contributing theme translations](#contributing-theme-translations)

# Localizing Your Theme[](#localizing-your-theme "Permanent link")

Display your theme in your preferred language.

------------------------------------------------------------------------

Note

Theme localization only translates the text elements of the theme itself (such as \"next\" and \"previous\" links), not the actual content of your documentation. If you wish to create multilingual documentation, you need to combine theme localization as described here with a third-party internationalization/localization plugin.

## Installation[](#installation "Permanent link")

For theme localization to work, you must use a theme which supports it and enable `i18n` (internationalization) support by installing `mkdocs[i18n]`:

``` highlight
pip install 'mkdocs[i18n]'
```

## Supported locales[](#supported-locales "Permanent link")

In most cases a locale is designated by the [ISO-639-1](https://en.wikipedia.org/wiki/ISO_639-1) (2-letter) abbreviation for your language. However, a locale may also include a territory (or region or county) code as well. The language and territory must be separated by an underscore. For example, some possible locales for English might include `en`, `en_AU`, `en_GB`, and `en_US`.

For a list of locales supported by the theme you are using, see that theme\'s documentation.

-   [mkdocs](../choosing-your-theme/#mkdocs-locale)
-   [readthedocs](../choosing-your-theme/#readthedocs-locale)

Warning

If you configure a language locale which is not yet supported by the theme that you are using, MkDocs will fall back to the theme\'s default locale.

## Usage[](#usage "Permanent link")

To specify the locale that MkDocs should use, set the [locale](../configuration/#locale) parameter of the [theme](../configuration/#theme) configuration option to the appropriate code.

For example, to build the `mkdocs` theme in French you would use the following in your `mkdocs.yml` configuration file:

``` highlight
theme:
  name: mkdocs
  locale: fr
```

## Contributing theme translations[](#contributing-theme-translations "Permanent link")

If a theme has not yet been translated into your language, feel free to contribute a translation using the [Translation Guide](../../dev-guide/translations/).

------------------------------------------------------------------------

Copyright © 2014 [Tom Christie](https://twitter.com/starletdreaming), Maintained by the [MkDocs Team](/about/release-notes/#maintenance-team).

Documentation built with [MkDocs](https://www.mkdocs.org/).

#### Search 

[×][Close]

From here you can search these documents. Enter your search terms below.

#### Keyboard Shortcuts 

[×][Close]

  Keys        Action
  ----------- ----------------
  [?]   Open this help
  [n]   Next page
  [p]   Previous page
  [s]   Search