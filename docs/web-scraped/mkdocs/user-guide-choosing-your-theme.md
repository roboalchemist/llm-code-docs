# Source: https://www.mkdocs.org/user-guide/choosing-your-theme/

[MkDocs](../..)

[]

-   [Home](../..)
-   [Getting Started](../../getting-started/)
-   [User Guide ](#)
    -   [User Guide](../)
    -   [Installation](../installation/)
    -   [Writing Your Docs](../writing-your-docs/)
    -   [Choosing Your Theme](./)
    -   [Customizing Your Theme](../customizing-your-theme/)
    -   [Localizing Your Theme](../localizing-your-theme/)
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
-   [ Previous](../writing-your-docs/)
-   [Next ](../customizing-your-theme/)
-   [ Edit on GitHub](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/choosing-your-theme.md)

[]

-   [Choosing your Theme](#choosing-your-theme)
    -   [mkdocs](#mkdocs)
    -   [readthedocs](#readthedocs)
    -   [Third Party Themes](#third-party-themes)

# Choosing your Theme[](#choosing-your-theme "Permanent link")

Selecting and configuring a theme.

------------------------------------------------------------------------

MkDocs includes two built-in themes ([mkdocs](#mkdocs) and [readthedocs](#readthedocs)), as documented below. However, many [third party themes](#third-party-themes) are available to choose from as well.

To choose a theme, set the [theme](../configuration/#theme) configuration option in your `mkdocs.yml` config file.

``` highlight
theme:
  name: readthedocs
```

## mkdocs[](#mkdocs "Permanent link")

The default theme, which was built as a custom [Bootstrap](https://getbootstrap.com/) theme, supports almost every feature of MkDocs.

![MkDocs theme in light mode](../../img/mkdocs_theme_light_mode.png)

![MkDocs theme in dark mode](../../img/mkdocs_theme_dark_mode.png)

In addition to the default [theme configuration options](../configuration/#theme), the `mkdocs` theme supports the following options:

-   **`color_mode`**: Set the default color mode for the theme to one of `light`, `dark`, or `auto`. The `auto` mode will switch to `light` or `dark` based on the system configuration of the user\'s device. Default: `light`.

-   **`user_color_mode_toggle`**: Enable a toggle menu in the navigation bar which allows users to select their preferred `color_mode` (light, dark, auto) from within the browser and save their preference for future page loads. The default selection of the toggle menu on first page load is the value set to `color_mode`. Default: `false`.

    ![color mode toggle menu](../../img/color_mode_toggle_menu.png)

-   **`nav_style`**: Adjust the visual style of the top navigation bar. Set to one of `primary`, `dark` or `light`. Default: `primary`. This option is independent of the `color_mode` option and must be defined separately.

-   **`highlightjs`**: Enables highlighting of source code in code blocks using the [highlight.js](https://highlightjs.org/) JavaScript library. Default: `True`.

-   **`hljs_style`**: The highlight.js library provides many different [styles](https://highlightjs.org/static/demo/) (color variations) for highlighting source code in code blocks. Set this to the name of the desired style when in `light` mode. Default: `github`.

-   **`hljs_style_dark`**: Set this to the name of the desired highlight.js style when in `dark` mode. Default: `github_dark`.

-   **`hljs_languages`**: By default, highlight.js only supports 23 common languages. List additional languages here to include support for them.

    ``` highlight
    theme:
      name: mkdocs
      highlightjs: true
      hljs_languages:
        - yaml
        - rust
    ```

-   **`analytics`**: Defines configuration options for an analytics service. Currently, only Google Analytics v4 is supported via the `gtag` option.

    -   **`gtag`**: To enable Google Analytics, set to a Google Analytics v4 tracking ID, which uses the `G-` format. See Google\'s documentation to [Set up Analytics for a website and/or app (GA4)](https://support.google.com/analytics/answer/9304153?hl=en&ref_topic=9303319) or to [Upgrade to a Google Analytics 4 property](https://support.google.com/analytics/answer/9744165?hl=en&ref_topic=9303319).

        ``` highlight
        theme:
          name: mkdocs
          analytics:
            gtag: G-ABC123
        ```

        When set to the default (`null`) Google Analytics is disabled for the site.

-   **`shortcuts`**: Defines keyboard shortcut keys.

    ``` highlight
    theme:
      name: mkdocs
      shortcuts:
        help: 191    # ?
        next: 78     # n
        previous: 80 # p
        search: 83   # s
    ```

    All values must be numeric key codes. It is best to use keys that are available on all keyboards. You may use <https://keycode.info/> to determine the key code for a given key.

    -   **`help`**: Display a help modal that lists the keyboard shortcuts. Default: `191` (?)

    -   **`next`**: Navigate to the \"next\" page. Default: `78` (n)

    -   **`previous`**: Navigate to the \"previous\" page. Default: `80` (p)

    -   **`search`**: Display the search modal. Default: `83` (s)

-   **`navigation_depth`**: The maximum depth of the navigation tree in the sidebar. Default: `2`.

-   **`locale`**: The locale (language/location) used to build the theme. If your locale is not yet supported, it will fall back to the default.

    The following locales are supported by this theme:

    -   `en`: English (default)
    -   `de`: German
    -   `es`: Spanish
    -   `fa`: Persian
    -   `fr`: French
    -   `id`: Indonesian
    -   `it`: Italian
    -   `ja`: Japanese
    -   `nb`: Norwegian Bokmål
    -   `nl`: Dutch
    -   `nn`: Norwegian Nynorsk
    -   `pl`: Polish
    -   `pt_BR`: Portuguese (Brazil)
    -   `ru`: Russian
    -   `tr`: Turkish
    -   `uk`: Ukrainian
    -   `zh_CN`: Chinese (Simplified, China)
    -   `zh_TW`: Chinese (Traditional, Taiwan)

    See the guide on [localizing your theme](../localizing-your-theme/) for more information.

## readthedocs[](#readthedocs "Permanent link")

A clone of the default theme used by the [Read the Docs](https://readthedocs.org/) service, which offers the same restricted feature set as its parent theme. Like its parent theme, only two levels of navigation are supported.

![ReadTheDocs](../../img/readthedocs.png)

In addition to the default [theme configuration options](../configuration/#theme), the `readthedocs` theme supports the following options:

-   **`highlightjs`**: Enables highlighting of source code in code blocks using the [highlight.js](https://highlightjs.org/) JavaScript library. Default: `True`.

-   **`hljs_languages`**: By default, highlight.js only supports 23 common languages. List additional languages here to include support for them.

    ``` highlight
    theme:
      name: readthedocs
      highlightjs: true
      hljs_languages:
        - yaml
        - rust
    ```

-   **`analytics`**: Defines configuration options for an analytics service.

    -   **`gtag`**: To enable Google Analytics, set to a Google Analytics v4 tracking ID, which uses the `G-` format. See Google\'s documentation to [Set up Analytics for a website and/or app (GA4)](https://support.google.com/analytics/answer/9304153?hl=en&ref_topic=9303319) or to [Upgrade to a Google Analytics 4 property](https://support.google.com/analytics/answer/9744165?hl=en&ref_topic=9303319).

        ``` highlight
        theme:
          name: readthedocs
          analytics:
            gtag: G-ABC123
        ```

        When set to the default (`null`) Google Analytics is disabled for the

    -   **`anonymize_ip`**: To enable anonymous IP address for Google Analytics, set this to `True`. Default: `False`.

-   **`include_homepage_in_sidebar`**: Lists the homepage in the sidebar menu. As MkDocs requires that the homepage be listed in the `nav` configuration option, this setting allows the homepage to be included or excluded from the sidebar. Note that the site name/logo always links to the homepage. Default: `True`.

-   **`prev_next_buttons_location`**: One of `bottom`, `top`, `both` , or `none`. Displays the "Next" and "Previous" buttons accordingly. Default: `bottom`.

-   **`navigation_depth`**: The maximum depth of the navigation tree in the sidebar. Default: `4`.

-   **`collapse_navigation`**: Only include the page section headers in the sidebar for the current page. Default: `True`.

-   **`titles_only`**: Only include page titles in the sidebar, excluding all section headers for all pages. Default: `False`.

-   **`sticky_navigation`**: If True, causes the sidebar to scroll with the main page content as you scroll the page. Default: `True`.

-   **`locale`**: The locale (language/location) used to build the theme. If your locale is not yet supported, it will fall back to the default.

    The following locales are supported by this theme:

    -   `en`: English (default)
    -   `de`: German
    -   `es`: Spanish
    -   `fa`: Persian
    -   `fr`: French
    -   `id`: Indonesian
    -   `it`: Italian
    -   `ja`: Japanese
    -   `nl`: Dutch
    -   `pl`: Polish
    -   `pt_BR`: Portuguese (Brazil)
    -   `ru`: Russian
    -   `tr`: Turkish
    -   `uk`: Ukrainian
    -   `zh_CN`: Chinese (Simplified, China)
    -   `zh_TW`: Chinese (Traditional, Taiwan)

    See the guide on [localizing your theme](../localizing-your-theme/) for more information.

-   **`logo`**: To set a logo on your project instead of the plain text `site_name`, set this variable to be the location of your image. Default: `null`.

## Third Party Themes[](#third-party-themes "Permanent link")

A list of third party themes can be found at the [community wiki](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) page and [the ranked catalog](https://github.com/mkdocs/catalog#-theming). If you have created your own, please add them there.

Warning

Installing an MkDocs theme means installing a Python package and executing any code that the author has put in there. So, exercise the usual caution; there\'s no attempt at sandboxing.

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