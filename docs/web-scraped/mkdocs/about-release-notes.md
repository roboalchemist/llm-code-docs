# Source: https://www.mkdocs.org/about/release-notes/

[MkDocs](../..)

[]

-   [Home](../..)
-   [Getting Started](../../getting-started/)
-   [User Guide ](#)
    -   [User Guide](../../user-guide/)
    -   [Installation](../../user-guide/installation/)
    -   [Writing Your Docs](../../user-guide/writing-your-docs/)
    -   [Choosing Your Theme](../../user-guide/choosing-your-theme/)
    -   [Customizing Your Theme](../../user-guide/customizing-your-theme/)
    -   [Localizing Your Theme](../../user-guide/localizing-your-theme/)
    -   [Configuration](../../user-guide/configuration/)
    -   [Command Line Interface](../../user-guide/cli/)
    -   [Deploying Your Docs](../../user-guide/deploying-your-docs/)
-   [Developer Guide ](#)
    -   [Developer Guide](../../dev-guide/)
    -   [Themes](../../dev-guide/themes/)
    -   [Translations](../../dev-guide/translations/)
    -   [Plugins](../../dev-guide/plugins/)
    -   [API Reference](../../dev-guide/api/)
-   [About ](#)
    -   [Release Notes](./)
    -   [Contributing](../contributing/)
    -   [License](../license/)

```
<!-- -->
```
-   [ Search](#)
-   [ Previous](../../dev-guide/api/)
-   [Next ](../contributing/)
-   [ Edit on GitHub](https://github.com/mkdocs/mkdocs/blob/master/docs/about/release-notes.md)

[]

-   [Release Notes](#release-notes)
    -   [Upgrading](#upgrading)
    -   [Maintenance team](#maintenance-team)
    -   [Version 1.6.1 (2024-08-30)](#version-161-2024-08-30)
    -   [Version 1.6.0 (2024-04-20)](#version-160-2024-04-20)
    -   [Version 1.5.3 (2023-09-18)](#version-153-2023-09-18)
    -   [Version 1.5.2 (2023-08-02)](#version-152-2023-08-02)
    -   [Version 1.5.1 (2023-07-28)](#version-151-2023-07-28)
    -   [Version 1.5.0 (2023-07-26)](#version-150-2023-07-26)
    -   [Version 1.4.3 (2023-05-02)](#version-143-2023-05-02)
    -   [Version 1.4.2 (2022-11-01)](#version-142-2022-11-01)
    -   [Version 1.4.1 (2022-10-15)](#version-141-2022-10-15)
    -   [Version 1.4.0 (2022-09-27)](#version-140-2022-09-27)
    -   [Version 1.3.1 (2022-07-19)](#version-131-2022-07-19)
    -   [Version 1.3.0 (2022-03-26)](#version-130-2022-03-26)
    -   [Version 1.2.4 (2022-03-26)](#version-124-2022-03-26)
    -   [Version 1.2.3 (2021-10-12)](#version-123-2021-10-12)
    -   [Version 1.2.2 (2021-07-18)](#version-122-2021-07-18)
    -   [Version 1.2.1 (2021-06-09)](#version-121-2021-06-09)
    -   [Version 1.2 (2021-06-04)](#version-12-2021-06-04)
    -   [Version 1.1.2 (2020-05-14)](#version-112-2020-05-14)
    -   [Version 1.1.1 (2020-05-12)](#version-111-2020-05-12)
    -   [Version 1.1 (2020-02-22)](#version-11-2020-02-22)
    -   [Version 1.0.4 (2018-09-07)](#version-104-2018-09-07)
    -   [Version 1.0.3 (2018-08-29)](#version-103-2018-08-29)
    -   [Version 1.0.2 (2018-08-22)](#version-102-2018-08-22)
    -   [Version 1.0.1 (2018-08-13)](#version-101-2018-08-13)
    -   [Version 1.0 (2018-08-03)](#version-10-2018-08-03)
    -   [Version 0.17.5 (2018-07-06)](#version-0175-2018-07-06)
    -   [Version 0.17.4 (2018-06-08)](#version-0174-2018-06-08)
    -   [Version 0.17.3 (2018-03-07)](#version-0173-2018-03-07)
    -   [Version 0.17.2 (2017-11-15)](#version-0172-2017-11-15)
    -   [Version 0.17.1 (2017-10-30)](#version-0171-2017-10-30)
    -   [Version 0.17.0 (2017-10-19)](#version-0170-2017-10-19)
    -   [Version 0.16.3 (2017-04-04)](#version-0163-2017-04-04)
    -   [Version 0.16.2 (2017-03-13)](#version-0162-2017-03-13)
    -   [Version 0.16.1 (2016-12-22)](#version-0161-2016-12-22)
    -   [Version 0.16 (2016-11-04)](#version-016-2016-11-04)
    -   [Version 0.15.3 (2016-02-18)](#version-0153-2016-02-18)
    -   [Version 0.15.2 (2016-02-08)](#version-0152-2016-02-08)
    -   [Version 0.15.1 (2016-01-30)](#version-0151-2016-01-30)
    -   [Version 0.15.0 (2016-01-21)](#version-0150-2016-01-21)
    -   [Version 0.14.0 (2015-06-09)](#version-0140-2015-06-09)
    -   [Version 0.13.3 (2015-06-02)](#version-0133-2015-06-02)
    -   [Version 0.13.2 (2015-05-30)](#version-0132-2015-05-30)
    -   [Version 0.13.1 (2015-05-27)](#version-0131-2015-05-27)
    -   [Version 0.13.0 (2015-05-26)](#version-0130-2015-05-26)
    -   [Version 0.12.2 (2015-04-22)](#version-0122-2015-04-22)
    -   [Version 0.12.1 (2015-04-14)](#version-0121-2015-04-14)
    -   [Version 0.12.0 (2015-04-14)](#version-0120-2015-04-14)
    -   [Version 0.11.1 (2014-11-20)](#version-0111-2014-11-20)
    -   [Version 0.11.0 (2014-11-18)](#version-0110-2014-11-18)
    -   [Version 0.10.0 (2014-10-29)](#version-0100-2014-10-29)

# Release Notes[](#release-notes "Permanent link")

------------------------------------------------------------------------

## Upgrading[](#upgrading "Permanent link")

To upgrade MkDocs to the latest version, use pip:

``` highlight
pip install -U mkdocs
```

You can determine your currently installed version using `mkdocs --version`:

``` highlight
$ mkdocs --version
mkdocs, version 1.5.0 from /path/to/mkdocs (Python 3.10)
```

## Maintenance team[](#maintenance-team "Permanent link")

The current and past members of the MkDocs team.

-   [\@tomchristie](https://github.com/tomchristie/)
-   [\@d0ugal](https://github.com/d0ugal/)
-   [\@waylan](https://github.com/waylan/)
-   [\@oprypin](https://github.com/oprypin/)
-   [\@ultrabug](https://github.com/ultrabug/)

## Version 1.6.1 (2024-08-30)[](#version-161-2024-08-30 "Permanent link") 

### Fixed[](#fixed "Permanent link")

-   Fix build error when environment variable `SOURCE_DATE_EPOCH=0` is set. [#3795](https://github.com/mkdocs/mkdocs/issues/3795 "GitHub Issue mkdocs/mkdocs #3795")
-   Fix build error when `mkdocs_theme.yml` config is empty. [#3700](https://github.com/mkdocs/mkdocs/issues/3700 "GitHub Issue mkdocs/mkdocs #3700")
-   Support `python -W` and `PYTHONWARNINGS` instead of overriding the configuration. [#3809](https://github.com/mkdocs/mkdocs/issues/3809 "GitHub Issue mkdocs/mkdocs #3809")
-   Support running with Docker under strict mode, by removing `0.0.0.0` dev server warning. [#3784](https://github.com/mkdocs/mkdocs/issues/3784 "GitHub Issue mkdocs/mkdocs #3784")
-   Drop unnecessary `changefreq` from `sitemap.xml`. [#3629](https://github.com/mkdocs/mkdocs/issues/3629 "GitHub Issue mkdocs/mkdocs #3629")
-   Fix JavaScript console error when closing menu dropdown. [#3774](https://github.com/mkdocs/mkdocs/issues/3774 "GitHub Issue mkdocs/mkdocs #3774")
-   Fix JavaScript console error that occur on repeated clicks. [#3730](https://github.com/mkdocs/mkdocs/issues/3730 "GitHub Issue mkdocs/mkdocs #3730")
-   Fix JavaScript console error that can occur on dropdown selections. [#3694](https://github.com/mkdocs/mkdocs/issues/3694 "GitHub Issue mkdocs/mkdocs #3694")

### Added[](#added "Permanent link")

-   Added translations for Dutch. [#3804](https://github.com/mkdocs/mkdocs/issues/3804 "GitHub Issue mkdocs/mkdocs #3804")
-   Added and updated translations for Chinese (Simplified). [#3684](https://github.com/mkdocs/mkdocs/issues/3684 "GitHub Issue mkdocs/mkdocs #3684")

## Version 1.6.0 (2024-04-20)[](#version-160-2024-04-20 "Permanent link") 

### Local preview[](#local-preview "Permanent link")

-   `mkdocs serve` no longer locks up the browser when more than 5 tabs are open. This is achieved by closing the polling connection whenever a tab becomes inactive. Background tabs will no longer auto-reload either - that will instead happen as soon the tab is opened again. Context: [#3391](https://github.com/mkdocs/mkdocs/issues/3391 "GitHub Issue mkdocs/mkdocs #3391")

-   New flag `serve --open` to open the site in a browser.\
    After the first build is finished, this flag will cause the default OS Web browser to be opened at the home page of the local site.\
    Context: [#3500](https://github.com/mkdocs/mkdocs/issues/3500 "GitHub Issue mkdocs/mkdocs #3500")

#### Drafts[](#drafts "Permanent link")

Changed from version 1.5

**The `exclude_docs` config was split up into two separate concepts.**

The `exclude_docs` config no longer has any special behavior for `mkdocs serve` - it now always completely excludes the listed documents from the site.

If you wish to use the \"drafts\" functionality like the `exclude_docs` key used to do in MkDocs 1.5, please switch to the **new config key `draft_docs`**.

See [documentation](../../user-guide/configuration/#exclude_docs).

Other changes:

-   Reduce warning levels when a \"draft\" page has a link to a non-existent file. Context: [#3449](https://github.com/mkdocs/mkdocs/issues/3449 "GitHub Issue mkdocs/mkdocs #3449")

### Update to deduction of page titles[](#update-to-deduction-of-page-titles "Permanent link")

MkDocs 1.5 had a change in behavior in deducing the page titles from the first heading. Unfortunately this could cause unescaped HTML tags or entities to appear in edge cases.

Now tags are always fully sanitized from the title. Though it still remains the case that [`Page.title`](../../dev-guide/themes/#mkdocs.structure.pages.Page.title) is expected to contain HTML entities and is passed directly to the themes.

Images (notably, emojis in some extensions) get preserved in the title only through their `alt` attribute\'s value.

Context: [#3564](https://github.com/mkdocs/mkdocs/issues/3564 "GitHub Issue mkdocs/mkdocs #3564"), [#3578](https://github.com/mkdocs/mkdocs/issues/3578 "GitHub Issue mkdocs/mkdocs #3578")

### Themes[](#themes "Permanent link")

-   Built-in themes now also support Polish language ([#3613](https://github.com/mkdocs/mkdocs/issues/3613 "GitHub Issue mkdocs/mkdocs #3613"))

#### \"readthedocs\" theme[](#readthedocs-theme "Permanent link")

-   Fix: \"readthedocs\" theme can now correctly handle deeply nested nav configurations (over 2 levels deep), without confusedly expanding all sections and jumping around vertically. ([#3464](https://github.com/mkdocs/mkdocs/issues/3464 "GitHub Issue mkdocs/mkdocs #3464"))

-   Fix: \"readthedocs\" theme now shows a link to the repository (with a generic logo) even when isn\'t one of the 3 known hosters. ([#3435](https://github.com/mkdocs/mkdocs/issues/3435 "GitHub Issue mkdocs/mkdocs #3435"))

-   \"readthedocs\" theme now also has translation for the word \"theme\" in the footer that mistakenly always remained in English. ([#3613](https://github.com/mkdocs/mkdocs/issues/3613 "GitHub Issue mkdocs/mkdocs #3613"), [#3625](https://github.com/mkdocs/mkdocs/issues/3625 "GitHub Issue mkdocs/mkdocs #3625"))

#### \"mkdocs\" theme[](#mkdocs-theme "Permanent link")

The \"mkdocs\" theme got a big update to a newer version of Bootstrap, meaning a slight overhaul of styles. Colors (most notably of admonitions) have much better contrast.

The \"mkdocs\" theme now has support for dark mode - both automatic (based on the OS/browser setting) and with a manual toggle. Both of these options are **not** enabled by default and need to be configured explicitly.\
See `color_mode`, `user_color_mode_toggle` in [**documentation**](../../user-guide/choosing-your-theme/#mkdocs).

Possible breaking change

jQuery is no longer included into the \"mkdocs\" theme. If you were relying on it in your scripts, you will need to separately add it first (into mkdocs.yml) as an extra script:

``` highlight
extra_javascript:
  - https://code.jquery.com/jquery-3.7.1.min.js
```

Or even better if the script file is copied and included from your docs dir.

Context: [#3493](https://github.com/mkdocs/mkdocs/issues/3493 "GitHub Issue mkdocs/mkdocs #3493"), [#3649](https://github.com/mkdocs/mkdocs/issues/3649 "GitHub Issue mkdocs/mkdocs #3649")

### Configuration[](#configuration "Permanent link")

#### New \"`enabled`\" setting for all plugins[](#new-enabled-setting-for-all-plugins "Permanent link")

You may have seen some plugins take up the convention of having a setting `enabled: false` (or usually controlled through an environment variable) to make the plugin do nothing.

Now *every* plugin has this setting. Plugins can still *choose* to implement this config themselves and decide how it behaves (and unless they drop older versions of MkDocs, they still should for now), but now there\'s always a fallback for every plugin.

See [**documentation**](../../user-guide/configuration/#enabled-option). Context: [#3395](https://github.com/mkdocs/mkdocs/issues/3395 "GitHub Issue mkdocs/mkdocs #3395")

### Validation[](#validation "Permanent link")

#### Validation of hyperlinks between pages[](#validation-of-hyperlinks-between-pages "Permanent link")

##### Absolute links[](#absolute-links "Permanent link")

> Historically, within Markdown, MkDocs only recognized **relative** links that lead to another physical `*.md` document (or media file). This is a good convention to follow because then the source pages are also freely browsable without MkDocs, for example on GitHub. Whereas absolute links were left unmodified (making them often not work as expected or, more recently, warned against).

If you dislike having to always use relative links, now you can opt into absolute links and have them work correctly.

If you set the setting `validation.links.absolute_links` to the new value `relative_to_docs`, all Markdown links starting with `/` will be understood as being relative to the `docs_dir` root. The links will then be validated for correctness according to all the other rules that were already working for relative links in prior versions of MkDocs. For the HTML output, these links will still be turned relative so that the site still works reliably.

So, now any document (e.g. \"dir1/foo.md\") can link to the document \"dir2/bar.md\" as `[link](/dir2/bar.md)`, in addition to the previously only correct way `[link](../dir2/bar.md)`.

You have to enable the setting, though. The default is still to just skip any processing of such links.

See [**documentation**](../../user-guide/configuration/#validation-of-absolute-links). Context: [#3485](https://github.com/mkdocs/mkdocs/issues/3485 "GitHub Issue mkdocs/mkdocs #3485")

###### Absolute links within nav[](#absolute-links-within-nav "Permanent link")

Absolute links within the `nav:` config were also always skipped. It is now possible to also validate them in the same way with `validation.nav.absolute_links`. Though it makes a bit less sense because then the syntax is simply redundant with the syntax that comes without the leading slash.

##### Anchors[](#anchors "Permanent link")

There is a new config setting that is recommended to enable warnings for:

``` highlight
validation:
  anchors: warn
```

Example of a warning that this can produce:

``` highlight
WARNING -  Doc file 'foo/example.md' contains a link '../bar.md#some-heading', but the doc 'foo/bar.md' does not contain an anchor '#some-heading'.
```

Any of the below methods of declaring an anchor will be detected by MkDocs:

``` highlight
## Heading producing an anchor

## Another heading 

<a id="raw-anchor"></a>

[]()
```

Plugins and extensions that insert anchors, in order to be compatible with this, need to be developed as treeprocessors that insert `etree` elements as their mode of operation, rather than raw HTML which is undetectable for this purpose.

If you as a user are dealing with falsely reported missing anchors and there\'s no way to resolve this, you can choose to disable these messages by setting this option to `ignore` (and they are at INFO level by default anyway).

See [**documentation**](../../user-guide/configuration/#validation). Context: [#3463](https://github.com/mkdocs/mkdocs/issues/3463 "GitHub Issue mkdocs/mkdocs #3463")

Other changes:

-   When the `nav` config is not specified at all, the `not_in_nav` setting (originally added in 1.5.0) gains an additional behavior: documents covered by `not_in_nav` will not be part of the automatically deduced navigation. Context: [#3443](https://github.com/mkdocs/mkdocs/issues/3443 "GitHub Issue mkdocs/mkdocs #3443")

-   Fix: the `!relative` YAML tag for `markdown_extensions` (originally added in 1.5.0) - it was broken in many typical use cases.

    See [**documentation**](../../user-guide/configuration/#paths-relative-to-the-current-file-or-site). Context: [#3466](https://github.com/mkdocs/mkdocs/issues/3466 "GitHub Issue mkdocs/mkdocs #3466")

-   Config validation now exits on first error, to avoid showing bizarre secondary errors. Context: [#3437](https://github.com/mkdocs/mkdocs/issues/3437 "GitHub Issue mkdocs/mkdocs #3437")

-   MkDocs used to shorten error messages for unexpected errors such as \"file not found\", but that is no longer the case, the full error message and stack trace will be possible to see (unless the error has a proper handler, of course). Context: [#3445](https://github.com/mkdocs/mkdocs/issues/3445 "GitHub Issue mkdocs/mkdocs #3445")

### Upgrades for plugin developers[](#upgrades-for-plugin-developers "Permanent link")

#### Plugins can add multiple handlers for the same event type, at multiple priorities[](#plugins-can-add-multiple-handlers-for-the-same-event-type-at-multiple-priorities "Permanent link")

See [`mkdocs.plugins.CombinedEvent`](../../dev-guide/plugins/#mkdocs.plugins.CombinedEvent) in [**documentation**](../../dev-guide/plugins/#event-priorities). Context: [#3448](https://github.com/mkdocs/mkdocs/issues/3448 "GitHub Issue mkdocs/mkdocs #3448")

#### Enabling true generated files and expanding the [`File`](../../dev-guide/api/#mkdocs.structure.files.File) API[](#enabling-true-generated-files-and-expanding-the-file-api "Permanent link")

See [**documentation**](../../dev-guide/api/#mkdocs.structure.files.File).

-   There is a new pair of attributes [`File.content_string`](../../dev-guide/api/#mkdocs.structure.files.File.content_string)/[`content_bytes`](../../dev-guide/api/#mkdocs.structure.files.File.content_bytes) that becomes the official API for obtaining the content of a file and is used by MkDocs itself.

    This replaces the old approach where one had to manually read the file located at [`File.abs_src_path`](../../dev-guide/api/#mkdocs.structure.files.File.abs_src_path), although that is still the primary action that these new attributes do under the hood.

-   The content of a `File` can be backed by a string and no longer has to be a real existing file at `abs_src_path`.

    It is possible to **set** the attribute `File.content_string` or `File.content_bytes` and it will take precedence over `abs_src_path`.

    Further, `abs_src_path` is no longer guaranteed to be present and can be `None` instead. MkDocs itself still uses physical files in all cases, but eventually plugins will appear that don\'t populate this attribute.

-   There is a new constructor [`File.generated()`](../../dev-guide/api/#mkdocs.structure.files.File.generated) that should be used by plugins instead of the `File()` constructor. It is much more convenient because one doesn\'t need to manually look up the values such as `docs_dir` and `use_directory_urls`. Its signature is one of:

    ``` highlight
    f = File.generated(config: MkDocsConfig, src_uri: str, content: str | bytes)
    f = File.generated(config: MkDocsConfig, src_uri: str, abs_src_path: str)
    ```

    This way, it is now extremely easy to add a virtual file even from a hook:

    ``` highlight
    def on_files(files: Files, config: MkDocsConfig):
        files.append(File.generated(config, 'fake/path.md', content="Hello, world!"))
    ```

    For large content it is still best to use physical files, but one no longer needs to manipulate the path by providing a fake unused `docs_dir`.

-   There is a new attribute [`File.generated_by`](../../dev-guide/api/#mkdocs.structure.files.File.generated_by) that arose by convention - for generated files it should be set to the name of the plugin (the key in the `plugins:` collection) that produced this file. This attribute is populated automatically when using the `File.generated()` constructor.

-   It is possible to set the [`edit_uri`](../../dev-guide/api/#mkdocs.structure.files.File.edit_uri) attribute of a `File`, for example from a plugin or hook, to make it different from the default (equal to `src_uri`), and this will be reflected in the edit link of the document. This can be useful because some pages aren\'t backed by a real file and are instead created dynamically from some other source file or script. So a hook could set the `edit_uri` to that source file or script accordingly.

-   The `File` object now stores its original `src_dir`, `dest_dir`, `use_directory_urls` values as attributes.

-   Fields of `File` are computed on demand but cached. Only the three above attributes are primary ones, and partly also [`dest_uri`](../../dev-guide/api/#mkdocs.structure.files.File.dest_uri). This way, it is possible to, for example, overwrite `dest_uri` of a `File`, and `abs_dest_path` will be calculated based on it. However you need to clear the attribute first using `del f.abs_dest_path`, because the values are cached.

-   `File` instances are now hashable (can be used as keys of a `dict`). Two files can no longer be considered \"equal\" unless it\'s the exact same instance of `File`.

Other changes:

-   The internal storage of `File` objects inside a `Files` object has been reworked, so any plugins that choose to access `Files._files` will get a deprecation warning.

-   The order of `File` objects inside a `Files` collection is no longer significant when automatically inferring the `nav`. They get forcibly sorted according to the default alphabetic order.

Context: [#3451](https://github.com/mkdocs/mkdocs/issues/3451 "GitHub Issue mkdocs/mkdocs #3451"), [#3463](https://github.com/mkdocs/mkdocs/issues/3463 "GitHub Issue mkdocs/mkdocs #3463")

### Hooks and debugging[](#hooks-and-debugging "Permanent link")

-   Hook files can now import adjacent \*.py files using the `import` statement. Previously this was possible to achieve only through a `sys.path` workaround. See the new mention in [documentation](../../user-guide/configuration/#hooks). Context: [#3568](https://github.com/mkdocs/mkdocs/issues/3568 "GitHub Issue mkdocs/mkdocs #3568")

-   Verbose `-v` log shows the sequence of plugin events in more detail - shows each invoked plugin one by one, not only the event type. Context: [#3444](https://github.com/mkdocs/mkdocs/issues/3444 "GitHub Issue mkdocs/mkdocs #3444")

### Deprecations[](#deprecations "Permanent link")

-   Python 3.7 is no longer supported, Python 3.12 is officially supported. Context: [#3429](https://github.com/mkdocs/mkdocs/issues/3429 "GitHub Issue mkdocs/mkdocs #3429")

-   The theme config file `mkdocs_theme.yml` no longer executes YAML tags. Context: [#3465](https://github.com/mkdocs/mkdocs/issues/3465 "GitHub Issue mkdocs/mkdocs #3465")

-   The plugin event `on_page_read_source` is soft-deprecated because there is always a better alternative to it (see the new `File` API or just `on_page_markdown`, depending on the desired interaction).

    When multiple plugins/hooks apply this event handler, they trample over each other, so now there is a warning in that case.

    See [**documentation**](../../dev-guide/plugins/#on_page_read_source). Context: [#3503](https://github.com/mkdocs/mkdocs/issues/3503 "GitHub Issue mkdocs/mkdocs #3503")

#### API deprecations[](#api-deprecations "Permanent link")

-   It is no longer allowed to set `File.page` to a type other than `Page` or a subclass thereof. Context: [#3443](https://github.com/mkdocs/mkdocs/issues/3443 "GitHub Issue mkdocs/mkdocs #3443") - following the deprecation in version 1.5.3 and [#3381](https://github.com/mkdocs/mkdocs/issues/3381 "GitHub Issue mkdocs/mkdocs #3381").

-   `Theme._vars` is deprecated - use `theme['foo']` instead of `theme._vars['foo']`

-   `utils`: `modified_time()`, `get_html_path()`, `get_url_path()`, `is_html_file()`, `is_template_file()` are removed. `path_to_url()` is deprecated.

-   `LiveReloadServer.watch()` no longer accepts a custom callback.

Context: [#3429](https://github.com/mkdocs/mkdocs/issues/3429 "GitHub Issue mkdocs/mkdocs #3429")

### Misc[](#misc "Permanent link")

-   The `sitemap.xml.gz` file is slightly more reproducible and no longer changes on every build, but instead only once per day (upon a date change). Context: [#3460](https://github.com/mkdocs/mkdocs/issues/3460 "GitHub Issue mkdocs/mkdocs #3460")

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.5.3...1.6.0).

## Version 1.5.3 (2023-09-18)[](#version-153-2023-09-18 "Permanent link") 

-   Fix `mkdocs serve` sometimes locking up all browser tabs when navigating quickly ([#3390](https://github.com/mkdocs/mkdocs/issues/3390 "GitHub Issue mkdocs/mkdocs #3390"))

-   Add many new supported languages for \"search\" plugin - update lunr-languages to 1.12.0 ([#3334](https://github.com/mkdocs/mkdocs/issues/3334 "GitHub Issue mkdocs/mkdocs #3334"))

-   Bugfix (regression in 1.5.0): In \"readthedocs\" theme the styling of \"breadcrumb navigation\" was broken for nested pages ([#3383](https://github.com/mkdocs/mkdocs/issues/3383 "GitHub Issue mkdocs/mkdocs #3383"))

-   Built-in themes now also support Chinese (Traditional, Taiwan) language ([#3154](https://github.com/mkdocs/mkdocs/issues/3154 "GitHub Issue mkdocs/mkdocs #3154"))

-   Plugins can now set `File.page` to their own subclass of `Page`. There is also now a warning if `File.page` is set to anything other than a strict subclass of `Page`. ([#3367](https://github.com/mkdocs/mkdocs/issues/3367 "GitHub Issue mkdocs/mkdocs #3367"), [#3381](https://github.com/mkdocs/mkdocs/issues/3381 "GitHub Issue mkdocs/mkdocs #3381"))

    Note that just instantiating a `Page` [sets the file automatically](https://github.com/mkdocs/mkdocs/blob/f94ab3f62d0416d484d81a0c695c8ca86ab3b975/mkdocs/structure/pages.py#L34), so care needs to be taken not to create an unneeded `Page`.

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.5.2...1.5.3).

## Version 1.5.2 (2023-08-02)[](#version-152-2023-08-02 "Permanent link") 

-   Bugfix (regression in 1.5.0): Restore functionality of `--no-livereload`. ([#3320](https://github.com/mkdocs/mkdocs/issues/3320 "GitHub Issue mkdocs/mkdocs #3320"))

-   Bugfix (regression in 1.5.0): The new page title detection would sometimes be unable to drop anchorlinks - fix that. ([#3325](https://github.com/mkdocs/mkdocs/issues/3325 "GitHub Issue mkdocs/mkdocs #3325"))

-   Partly bring back pre-1.5 API: `extra_javascript` items will once again be mostly strings, and only sometimes `ExtraScriptValue` (when the extra `script` functionality is used).

    Plugins should be free to append strings to `config.extra_javascript`, but when reading the values, they must still make sure to read it as `str(value)` in case it is an `ExtraScriptValue` item. For querying the attributes such as `.type` you need to check `isinstance` first. Static type checking will guide you in that. ([#3324](https://github.com/mkdocs/mkdocs/issues/3324 "GitHub Issue mkdocs/mkdocs #3324"))

See [commit log](https://github.com/mkdocs/mkdocs/compare/1.5.1...1.5.2).

## Version 1.5.1 (2023-07-28)[](#version-151-2023-07-28 "Permanent link") 

-   Bugfix (regression in 1.5.0): Make it possible to treat `ExtraScriptValue` as a path. This lets some plugins still work despite the breaking change.

-   Bugfix (regression in 1.5.0): Prevent errors for special setups that have 3 conflicting files, such as `index.html`, `index.md` *and* `README.md` ([#3314](https://github.com/mkdocs/mkdocs/issues/3314 "GitHub Issue mkdocs/mkdocs #3314"))

See [commit log](https://github.com/mkdocs/mkdocs/compare/1.5.0...1.5.1).

## Version 1.5.0 (2023-07-26)[](#version-150-2023-07-26 "Permanent link") 

### New command `mkdocs get-deps`[](#new-command-mkdocs-get-deps "Permanent link")

This command guesses the Python dependencies that a MkDocs site requires in order to build. It simply prints the PyPI packages that need to be installed. In the terminal it can be combined directly with an installation command as follows:

``` highlight
pip install $(mkdocs get-deps)
```

The idea is that right after running this command, you can directly follow it up with `mkdocs build` and it will almost always \"just work\", without needing to think which dependencies to install.

The way it works is by scanning `mkdocs.yml` for `themes:`, `plugins:`, `markdown_extensions:` items and doing a reverse lookup based on a large list of known projects (catalog, see below).

Of course, you\'re welcome to use a \"virtualenv\" with such a command. Also note that for environments that require stability (for example CI) directly installing deps in this way is not a very reliable approach as it precludes dependency pinning.

The command allows overriding which config file is used (instead of `mkdocs.yml` in the current directory) as well as which catalog of projects is used (instead of downloading it from the default location). See [`mkdocs get-deps --help`](../../user-guide/cli/#mkdocs-get-deps).

Context: [#3205](https://github.com/mkdocs/mkdocs/issues/3205 "GitHub Issue mkdocs/mkdocs #3205")

### MkDocs has an official catalog of plugins[](#mkdocs-has-an-official-catalog-of-plugins "Permanent link")

Check out <https://github.com/mkdocs/catalog> and add all your general-purpose plugins, themes and extensions there, so that they can be looked up through `mkdocs get-deps`.

This was renamed from \"best-of-mkdocs\" and received significant updates. In addition to `pip` installation commands, the page now shows the config boilerplate needed to add a plugin.

### Expanded validation of links[](#expanded-validation-of-links "Permanent link")

#### Validated links in Markdown[](#validated-links-in-markdown "Permanent link")

> As you may know, within Markdown, MkDocs really only recognizes **relative** links that lead to another physical `*.md` document (or media file). This is a good convention to follow because then the source pages are also freely browsable without MkDocs, for example on GitHub. MkDocs knows that in the output it should turn those `*.md` links into `*.html` as appropriate, and it would also always tell you if such a link doesn\'t actually lead to an existing file.

However, the checks for links were really loose and had many concessions. For example, links that started with `/` (\"absolute\") and links that *ended* with `/` were left as is and no warning was shown, which allowed such very fragile links to sneak into site sources: links that happen to work right now but get no validation and links that confusingly need an extra level of `..` with `use_directory_urls` enabled.

Now, in addition to validating relative links, MkDocs will print `INFO` messages for unrecognized types of links (including absolute links). They look like this:

``` highlight
INFO - Doc file 'example.md' contains an absolute link '/foo/bar/', it was left as is. Did you mean 'foo/bar.md'?
```

If you don\'t want any changes, not even the `INFO` messages, and wish to revert to the silence from MkDocs 1.4, add the following configs to `mkdocs.yml` (**not** recommended):

``` highlight
validation:
  absolute_links: ignore
  unrecognized_links: ignore
```

If, on the opposite end, you want these to print `WARNING` messages and cause `mkdocs build --strict` to fail, you are recommended to configure these to `warn` instead.

See [**documentation**](../../user-guide/configuration/#validation) for actual recommended settings and more details. Context: [#3283](https://github.com/mkdocs/mkdocs/issues/3283 "GitHub Issue mkdocs/mkdocs #3283")

#### Validated links in the nav[](#validated-links-in-the-nav "Permanent link")

Links to documents in the [`nav` configuration](../../user-guide/configuration/#nav) now also have configurable validation, though with no changes to the defaults.

You are welcomed to turn on validation for files that were forgotten and excluded from the nav. Example:

``` highlight
validation:
  nav:
    omitted_files: warn
    absolute_links: warn
```

This can make the following message appear with the `WARNING` level (as opposed to `INFO` as the only option previously), thus being caught by `mkdocs --strict`:

``` highlight
INFO - The following pages exist in the docs directory, but are not included in the "nav" configuration: ...
```

See [**documentation**](../../user-guide/configuration/#validation). Context: [#3283](https://github.com/mkdocs/mkdocs/issues/3283 "GitHub Issue mkdocs/mkdocs #3283"), [#1755](https://github.com/mkdocs/mkdocs/issues/1755 "GitHub Issue mkdocs/mkdocs #1755")

#### Mark docs as intentionally \"not in nav\"[](#mark-docs-as-intentionally-not-in-nav "Permanent link")

There is a new config `not_in_nav`. With it, you can mark particular patterns of files as exempt from the above `omitted_files` warning type; no messages will be printed for them anymore. (As a corollary, setting this config to `*` is the same as ignoring `omitted_files` altogether.)

This is useful if you generally like these warnings about files that were forgotten from the nav, but still have some pages that you knowingly excluded from the nav and just want to build and copy them.

The `not_in_nav` config is a set of gitignore-like patterns. See the next section for an explanation of another such config.

See [**documentation**](../../user-guide/configuration/#not_in_nav). Context: [#3224](https://github.com/mkdocs/mkdocs/issues/3224 "GitHub Issue mkdocs/mkdocs #3224"), [#1888](https://github.com/mkdocs/mkdocs/issues/1888 "GitHub Issue mkdocs/mkdocs #1888")

### Excluded doc files[](#excluded-doc-files "Permanent link")

There is a new config `exclude_docs` that tells MkDocs to ignore certain files under `docs_dir` and *not* copy them to the built `site` as part of the build.

Historically MkDocs would always ignore file names starting with a dot, and that\'s all. Now this is all configurable: you can un-ignore these and/or ignore more patterns of files.

The `exclude_docs` config follows the [.gitignore pattern format](https://git-scm.com/docs/gitignore#_pattern_format) and is specified as a multiline YAML string. For example:

``` highlight
exclude_docs: |
  *.py               # Excludes e.g. docs/hooks/foo.py
  /requirements.txt  # Excludes docs/requirements.txt
```

Validation of links (described above) is also affected by `exclude_docs`. During `mkdocs serve` the messages explain the interaction, whereas during `mkdocs build` excluded files are as good as nonexistent.

As an additional related change, if you have a need to have both `README.md` and `index.md` files in a directory but publish only one of them, you can now use this feature to explicitly ignore one of them and avoid warnings.

See [**documentation**](../../user-guide/configuration/#exclude_docs). Context: [#3224](https://github.com/mkdocs/mkdocs/issues/3224 "GitHub Issue mkdocs/mkdocs #3224")

#### Drafts[](#drafts_1 "Permanent link") 

Dropped from version 1.6:

The `exclude_docs` config no longer applies the \"drafts\" functionality for `mkdocs serve`. This was renamed to [`draft_docs`](../../user-guide/configuration/#draft_docs).

The `exclude_docs` config has another behavior: all excluded Markdown pages will still be previewable in `mkdocs serve` only, just with a \"DRAFT\" marker on top. Then they will of course be excluded from `mkdocs build` or `gh-deploy`.

If you don\'t want `mkdocs serve` to have any special behaviors and instead want it to perform completely normal builds, use the new flag `mkdocs serve --clean`.

See [**documentation**](../../user-guide/configuration/#exclude_docs). Context: [#3224](https://github.com/mkdocs/mkdocs/issues/3224 "GitHub Issue mkdocs/mkdocs #3224")

### `mkdocs serve` no longer exits after build errors[](#mkdocs-serve-no-longer-exits-after-build-errors "Permanent link")

If there was an error (from the config or a plugin) during a site re-build, `mkdocs serve` used to exit after printing a stack trace. Now it will simply freeze the server until the author edits the files to fix the problem, and then will keep reloading.

But errors on the *first* build still cause `mkdocs serve` to exit, as before.

Context: [#3255](https://github.com/mkdocs/mkdocs/issues/3255 "GitHub Issue mkdocs/mkdocs #3255")

### Page titles will be deduced from any style of heading[](#page-titles-will-be-deduced-from-any-style-of-heading "Permanent link")

MkDocs always had the ability to infer the title of a page (if it\'s not specified in the `nav`) based on the first line of the document, if it had a `<h1>` heading that had to written starting with the exact character `#`. Now any style of Markdown heading is understood ([#1886](https://github.com/mkdocs/mkdocs/issues/1886 "GitHub Issue mkdocs/mkdocs #1886")). Due to the previous simplistic parsing, it was also impossible to use `attr_list` attributes in that first heading ([#3136](https://github.com/mkdocs/mkdocs/issues/3136 "GitHub Issue mkdocs/mkdocs #3136")). Now that is also fixed.

### Markdown extensions can use paths relative to the current document[](#markdown-extensions-can-use-paths-relative-to-the-current-document "Permanent link")

This is aimed at extensions such as `pymdownx.snippets` or `markdown_include.include`: you can now specify their include paths to be relative to the currently rendered Markdown document, or relative to the `docs_dir`. Any other extension can of course also make use of the new `!relative` YAML tag.

``` highlight
markdown_extensions:
  - pymdownx.snippets:
      base_path: !relative
```

See [**documentation**](../../user-guide/configuration/#paths-relative-to-the-current-file-or-site). Context: [#2154](https://github.com/mkdocs/mkdocs/issues/2154 "GitHub Issue mkdocs/mkdocs #2154"), [#3258](https://github.com/mkdocs/mkdocs/issues/3258 "GitHub Issue mkdocs/mkdocs #3258")

### `<script>` tags can specify `type="module"` and other attributes[](#script-tags-can-specify-typemodule-and-other-attributes "Permanent link")

In `extra_javascript`, if you use the `.mjs` file extension or explicitly specify a `type: module` key, the script will be added with the `type="module"` attribute. `defer: true` and `async: true` keys are also available.

See [updated **documentation** for `extra_javascript`](../../user-guide/configuration/#extra_javascript).

**At first this is only supported in built-in themes, other themes need to follow up, see below.**

Context: [#3237](https://github.com/mkdocs/mkdocs/issues/3237 "GitHub Issue mkdocs/mkdocs #3237")

### Changes for theme developers (action required!)[](#changes-for-theme-developers-action-required "Permanent link")

Using the construct `` is now fully obsolete because it cannot allow customizing the attributes of the `<script>` tag. It will keep working but blocks some of MkDocs\' features.

Instead, you now need to use `config.extra_javascript` (which was already the case for a while) and couple it with the new `script_tag` filter:

``` highlight
    
      }
    
```

See [**documentation**](../../dev-guide/themes/#picking-up-css-and-javascript-from-the-config).

### Upgrades for plugin developers[](#upgrades-for-plugin-developers_1 "Permanent link") 

-   Breaking change: `config.extra_javascript` is no longer a plain list of strings, but instead a list of `ExtraScriptValue` items. So you can no longer treat the list values as strings. If you want to keep compatibility with old versions, just always reference the items as `str(item)` instead. And you can still append plain strings to the list if you wish. See information about `<script>` tags above. Context: [#3237](https://github.com/mkdocs/mkdocs/issues/3237 "GitHub Issue mkdocs/mkdocs #3237")

-   `File` has a new attribute `inclusion`. Its value is calculated from both the `exclude_docs` and `not_in_nav` configs, and implements their behavior. Plugins can read this value or write to it. New `File` instances by default follow whatever the configs say, but plugins can choose to make this decision explicitly, per file.

-   When creating a `File`, one can now set a `dest_uri` directly, rather than having to update it (and other dependent attributes) after creation. [Context](https://github.com/mkdocs/mkdocs/commit/d5af6426c52421f1113f6dcc591de1e01bea48bd)

-   A new config option was added - `DictOfItems`. Similarly to `ListOfItems`, it validates a mapping of config options that all have the same type. Keys are arbitrary but always strings. Context: [#3242](https://github.com/mkdocs/mkdocs/issues/3242 "GitHub Issue mkdocs/mkdocs #3242")

-   A new function `get_plugin_logger` was added. In order to opt into a standardized way for plugins to log messages, please use the idiom:

    ``` highlight
    log = mkdocs.plugins.get_plugin_logger(__name__)
    ...
    log.info("Hello, world")
    ```

    Context: [#3245](https://github.com/mkdocs/mkdocs/issues/3245 "GitHub Issue mkdocs/mkdocs #3245")

-   `SubConfig` config option can be conveniently subclassed with a particular type of config specified. For example, `class ExtraScript(SubConfig[ExtraScriptValue]):`. To see how this is useful, search for this class in code. [Context](https://github.com/mkdocs/mkdocs/commit/73e503990e3e3504bfe1cb627d41a7e97970687e)

-   Bugfix: `SubConfig` had a bug where paths (from `FilesystemObject` options) were not made relative to the main config file as intended, because `config_file_path` was not properly inherited to it. This is now fixed. Context: [#3265](https://github.com/mkdocs/mkdocs/issues/3265 "GitHub Issue mkdocs/mkdocs #3265")

-   `Config` members now have a way to avoid clashing with Python\'s reserved words. This is achieved by stripping a trailing underscore from each member\'s name.

    Example of adding an `async` boolean option that can be set by the user as `async: true` and read programmatically as `config.async_`:

    ``` highlight
    class ExampleConfig(Config):
        async_ = Type(bool, default=False)
    ```

    Previously making a config key with a reserved name was impossible with new-style schemas. [Context](https://github.com/mkdocs/mkdocs/commit/1db8e884fa7135a49adf7740add5d875a16a18bc)

-   `Theme` has its attributes properly declared and gained new attributes `theme.locale`, `theme.custom_dir`.

-   Some type annotations were made more precise. For example:

    -   The `context` parameter has gained the type `TemplateContext` (`TypedDict`). [Context](https://github.com/mkdocs/mkdocs/commit/0f793b9984c7e6a1d53ce874e7d17b6d27ebf4b2)
    -   The classes `Page`, `Section`, `Link` now have a common base class `StructureItem`. [Context](https://github.com/mkdocs/mkdocs/commit/01be507e30b05db0a4c44ef05ba62b2098010653)
    -   Some methods stopped accepting `Config` and only accept `MkDocsConfig` as was originally intended. [Context](https://github.com/mkdocs/mkdocs/commit/c459cd24fc0320333f51525e9cf681d4a8370f50)
    -   `config.mdx_configs` got a proper type. Context: [#3229](https://github.com/mkdocs/mkdocs/issues/3229 "GitHub Issue mkdocs/mkdocs #3229")

### Theme updates[](#theme-updates "Permanent link")

-   Built-in themes mostly stopped relying on `<script defer>`. This may affect some usages of `extra_javascript`, mainly remove the need for custom handling of \"has the page fully loaded yet\". Context: [#3237](https://github.com/mkdocs/mkdocs/issues/3237 "GitHub Issue mkdocs/mkdocs #3237")

-   \"mkdocs\" theme now has a styling for `>` blockquotes, previously they were not distinguished at all. Context: [#3291](https://github.com/mkdocs/mkdocs/issues/3291 "GitHub Issue mkdocs/mkdocs #3291")

-   \"readthedocs\" theme was updated to v1.2.0 according to upstream, with improved styles for `<kbd>` and breadcrumb navigation. Context: [#3058](https://github.com/mkdocs/mkdocs/issues/3058 "GitHub Issue mkdocs/mkdocs #3058")

-   Both built-in themes had their version of highlight.js updated to 11.8.0, and jQuery updated to 3.6.0.

### Bug fixes[](#bug-fixes "Permanent link")

#### Relative paths in the nav can traverse above the root[](#relative-paths-in-the-nav-can-traverse-above-the-root "Permanent link")

Regression in 1.2 - relative paths in the nav could no longer traverse above the site\'s root and were truncated to the root. Although such traversal is discouraged and produces a warning, this was a documented behavior. The behavior is now restored.

Context: [#2752](https://github.com/mkdocs/mkdocs/issues/2752 "GitHub Issue mkdocs/mkdocs #2752"), [#3010](https://github.com/mkdocs/mkdocs/issues/3010 "GitHub Issue mkdocs/mkdocs #3010")

#### MkDocs can accept the config from stdin[](#mkdocs-can-accept-the-config-from-stdin "Permanent link")

This can be used for config overrides on the fly. See updated section at the bottom of [Configuration Inheritance](../../user-guide/configuration/#configuration-inheritance).

The command to use this is `mkdocs build -f -`. In previous versions doing this led to an error.

[Context](https://github.com/mkdocs/mkdocs/commit/d5bb15fa108da86a8e53fb7d84109d8f8d9d6453)

### New command line flags[](#new-command-line-flags "Permanent link")

-   `mkdocs --no-color build` disables color output and line wrapping. This option is also available through an environment variable `NO_COLOR=true`. Context: [#3282](https://github.com/mkdocs/mkdocs/issues/3282 "GitHub Issue mkdocs/mkdocs #3282")
-   `mkdocs build --no-strict` overrides the `strict` config to `false`. Context: [#3254](https://github.com/mkdocs/mkdocs/issues/3254 "GitHub Issue mkdocs/mkdocs #3254")
-   `mkdocs build -f -` (described directly above).
-   `mkdocs serve --clean` (described above).
-   `mkdocs serve --dirty` is the new name of `mkdocs serve --dirtyreload`.

### Deprecations[](#deprecations_1 "Permanent link") 

-   `extra_javascript` underwent a change that can break plugins in rare cases, and it requires attention from theme developers. See respective entries above.

-   Python-Markdown was unpinned from `<3.4`. That version is known to remove functionality. If you are affected by those removals, you can still choose to pin the version for yourself: `Markdown <3.4`. Context: [#3222](https://github.com/mkdocs/mkdocs/issues/3222 "GitHub Issue mkdocs/mkdocs #3222"), [#2892](https://github.com/mkdocs/mkdocs/issues/2892 "GitHub Issue mkdocs/mkdocs #2892")

-   `mkdocs.utils.warning_filter` now shows a warning about being deprecated. It does nothing since MkDocs 1.2. Consider `get_plugin_logger` or just logging under `mkdocs.plugins.*` instead. Context: [#3008](https://github.com/mkdocs/mkdocs/issues/3008 "GitHub Issue mkdocs/mkdocs #3008")

-   Accessing the `_vars` attribute of a `Theme` is deprecated - just access the keys directly.

-   Accessing the `user_configs` attribute of a `Config` is deprecated. Note: instead of `config.user_configs[*]['theme']['custom_dir']`, please use the new attribute `config.theme.custom_dir`.

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.4.3...1.5.0).

## Version 1.4.3 (2023-05-02)[](#version-143-2023-05-02 "Permanent link") 

-   Bugfix: for the `hooks` feature, modules no longer fail to load if using some advanced Python features like dataclasses ([#3193](https://github.com/mkdocs/mkdocs/issues/3193 "GitHub Issue mkdocs/mkdocs #3193"))

-   Bugfix: Don\'t create `None` sitemap entries if the page has no populated URL - affects sites that exclude some files from navigation ([`07a297b`](https://github.com/mkdocs/mkdocs/commit/07a297b3b4de4a1b49469b1497ee34039b9f38fa))

-   \"readthedocs\" theme:

    -   Accessibility: add aria labels to Home logo ([#3129](https://github.com/mkdocs/mkdocs/issues/3129 "GitHub Issue mkdocs/mkdocs #3129")) and search inputs ([#3046](https://github.com/mkdocs/mkdocs/issues/3046 "GitHub Issue mkdocs/mkdocs #3046"))
    -   \"readthedocs\" theme now supports `hljs_style:` config, same as \"mkdocs\" theme ([#3199](https://github.com/mkdocs/mkdocs/issues/3199 "GitHub Issue mkdocs/mkdocs #3199"))

-   Translations:

    -   Built-in themes now also support Indonesian language ([#3154](https://github.com/mkdocs/mkdocs/issues/3154 "GitHub Issue mkdocs/mkdocs #3154"))
    -   Fixed `zh_CN` translation ([#3125](https://github.com/mkdocs/mkdocs/issues/3125 "GitHub Issue mkdocs/mkdocs #3125"))
    -   `tr_TR` translation becomes just `tr` - usage should remain unaffected ([#3195](https://github.com/mkdocs/mkdocs/issues/3195 "GitHub Issue mkdocs/mkdocs #3195"))

See [commit log](https://github.com/mkdocs/mkdocs/compare/1.4.2...1.4.3).

## Version 1.4.2 (2022-11-01)[](#version-142-2022-11-01 "Permanent link") 

-   Officially support Python 3.11 ([#3020](https://github.com/mkdocs/mkdocs/issues/3020 "GitHub Issue mkdocs/mkdocs #3020"))

    ::: 
    Tip:

    Simply upgrading to Python 3.11 can cut off 10-15% of your site\'s build time.
    :::

-   Support multiple instances of the same plugin ([#3027](https://github.com/mkdocs/mkdocs/issues/3027 "GitHub Issue mkdocs/mkdocs #3027"))

    If a plugin is specified multiple times in the list under the `plugins:` config, that will create 2 (or more) instances of the plugin with their own config each.

    Previously this case was unforeseen and, as such, bugged.

    Now even though this works, by default a warning will appear from MkDocs anyway, unless the plugin adds a class variable `supports_multiple_instances = True`.

-   Bugfix (regression in 1.4.1): Don\'t error when a plugin puts a plain string into `warnings` ([#3016](https://github.com/mkdocs/mkdocs/issues/3016 "GitHub Issue mkdocs/mkdocs #3016"))

-   Bugfix: Relative links will always render with a trailing slash ([#3022](https://github.com/mkdocs/mkdocs/issues/3022 "GitHub Issue mkdocs/mkdocs #3022"))

    Previously under `use_directory_urls`, links *from* a sub-page *to* the main index page rendered as e.g. `<a href="../..">` even though in all other cases the links look like `<a href="../../">`. This caused unwanted behavior on some combinations of Web browsers and servers. Now this special-case bug was removed.

-   Built-in \"mkdocs\" theme now also supports Norwegian language ([#3024](https://github.com/mkdocs/mkdocs/issues/3024 "GitHub Issue mkdocs/mkdocs #3024"))

-   Plugin-related warnings look more readable ([#3016](https://github.com/mkdocs/mkdocs/issues/3016 "GitHub Issue mkdocs/mkdocs #3016"))

See [commit log](https://github.com/mkdocs/mkdocs/compare/1.4.1...1.4.2).

## Version 1.4.1 (2022-10-15)[](#version-141-2022-10-15 "Permanent link") 

-   Support theme-namespaced plugin loading ([#2998](https://github.com/mkdocs/mkdocs/issues/2998 "GitHub Issue mkdocs/mkdocs #2998"))

    Plugins\' entry points can be named as \'sometheme/someplugin\'. That will have the following outcome:

    -   If the current theme is \'sometheme\', the plugin \'sometheme/someplugin\' will always be preferred over \'someplugin\'.
    -   If the current theme *isn\'t* \'sometheme\', the only way to use this plugin is by specifying `plugins: [sometheme/someplugin]`.

    One can also specify `plugins: ['/someplugin']` instead of `plugins: ['someplugin']` to definitely avoid the theme-namespaced plugin.

-   Bugfix: `mkdocs serve` will work correctly with non-ASCII paths and redirects ([#3001](https://github.com/mkdocs/mkdocs/issues/3001 "GitHub Issue mkdocs/mkdocs #3001"))

-   Windows: \'colorama\' is now a dependency of MkDocs, to ensure colorful log output ([#2987](https://github.com/mkdocs/mkdocs/issues/2987 "GitHub Issue mkdocs/mkdocs #2987"))

-   Plugin-related config options have more reliable validation and error reporting ([#2997](https://github.com/mkdocs/mkdocs/issues/2997 "GitHub Issue mkdocs/mkdocs #2997"))

-   Translation sub-commands of `setup.py` were completely dropped. See documentation [\[1\]](../contributing/#submitting-changes-to-the-builtin-themes) [\[2\]](../../dev-guide/translations/#updating-the-translation-catalogs) for their new replacements ([#2990](https://github.com/mkdocs/mkdocs/issues/2990 "GitHub Issue mkdocs/mkdocs #2990"))

-   The [\'mkdocs\' package](https://pypi.org/project/mkdocs/#files) (wheel and source) is now produced by Hatch build system and pyproject.toml instead of setup.py ([#2988](https://github.com/mkdocs/mkdocs/issues/2988 "GitHub Issue mkdocs/mkdocs #2988"))

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.4.0...1.4.1).

## Version 1.4.0 (2022-09-27)[](#version-140-2022-09-27 "Permanent link") 

### Feature upgrades[](#feature-upgrades "Permanent link")

#### Hooks ([#2978](https://github.com/mkdocs/mkdocs/issues/2978 "GitHub Issue mkdocs/mkdocs #2978"))[](#hooks-2978 "Permanent link")

The new `hooks:` config allows you to add plugin-like event handlers from local Python files, without needing to set up and install an actual plugin.

See [**documentation**](../../user-guide/configuration/#hooks).

#### `edit_uri` flexibility ([#2927](https://github.com/mkdocs/mkdocs/issues/2927 "GitHub Issue mkdocs/mkdocs #2927"))[](#edit_uri-flexibility-2927 "Permanent link")

There is a new `edit_uri_template:` config.\
It works like `edit_uri` but more generally covers ways to construct an edit URL.\
See [**documentation**](../../user-guide/configuration/#edit_uri_template).

Additionally, the `edit_uri` functionality will now fully work even if `repo_url` is omitted ([#2928](https://github.com/mkdocs/mkdocs/issues/2928 "GitHub Issue mkdocs/mkdocs #2928"))

### Upgrades for plugin developers[](#upgrades-for-plugin-developers_2 "Permanent link") 

Note

This release has big changes to the implementation of plugins and their configs. But, the intention is to have zero breaking changes in all reasonably common use cases. Or at the very least if a code fix is required, there should always be a way to stay compatible with older MkDocs versions. Please report if this release breaks something.

#### Customize event order for plugin event handlers ([#2973](https://github.com/mkdocs/mkdocs/issues/2973 "GitHub Issue mkdocs/mkdocs #2973"))[](#customize-event-order-for-plugin-event-handlers-2973 "Permanent link")

Plugins can now choose to set a priority value for their event handlers. This can override the old behavior where for each event type, the handlers are called in the order that their plugins appear in the [`plugins` config](../../user-guide/configuration/#plugins).

If this is set, events with higher priority are called first. Events without a chosen priority get a default of 0. Events that have the same priority are ordered as they appear in the config.

Recommended priority values: `100` \"first\", `50` \"early\", `0` \"default\", `-50` \"late\", `-100` \"last\".\
As different plugins discover more precise relations to each other, the values should be further tweaked.

See [**documentation**](../../dev-guide/plugins/#event-priorities).

#### New events that persist across builds in `mkdocs serve` ([#2972](https://github.com/mkdocs/mkdocs/issues/2972 "GitHub Issue mkdocs/mkdocs #2972"))[](#new-events-that-persist-across-builds-in-mkdocs-serve-2972 "Permanent link")

The new events are `on_startup` and `on_shutdown`. They run at the very beginning and very end of an `mkdocs` invocation.\
`on_startup` also receives information on how `mkdocs` was invoked (e.g. `serve` `--dirtyreload`).

See [**documentation**](../../dev-guide/plugins/#events).

#### Replace `File.src_path` to not deal with backslashes ([#2930](https://github.com/mkdocs/mkdocs/issues/2930 "GitHub Issue mkdocs/mkdocs #2930"))[](#replace-filesrc_path-to-not-deal-with-backslashes-2930 "Permanent link") 

The property `src_path` uses backslashes on Windows, which doesn\'t make sense as it\'s a virtual path.\
To not make a breaking change, there\'s no change to how *this* property is used, but now you should:

-   Use **`File.src_uri`** instead of `File.src_path`
-   and **`File.dest_uri`** instead of `File.dest_path`.

These consistently use forward slashes, and are now the definitive source that MkDocs itself uses.

See [source code](https://github.com/mkdocs/mkdocs/blob/1.4.0/mkdocs/structure/files.py#L151).

As a related tip: you should also stop using `os.path.*` or `pathlib.Path()` to deal with these paths, and instead use `posixpath.*` or `pathlib.PurePosixPath()`

#### MkDocs is type-annotated, ready for use with [mypy](https://mypy.readthedocs.io/) ([#2941](https://github.com/mkdocs/mkdocs/issues/2941 "GitHub Issue mkdocs/mkdocs #2941"), [#2970](https://github.com/mkdocs/mkdocs/issues/2970 "GitHub Issue mkdocs/mkdocs #2970"))[](#mkdocs-is-type-annotated-ready-for-use-with-mypy-2941-2970 "Permanent link")

##### Type annotations for event handler methods ([#2931](https://github.com/mkdocs/mkdocs/issues/2931 "GitHub Issue mkdocs/mkdocs #2931"))[](#type-annotations-for-event-handler-methods-2931 "Permanent link")

MkDocs\' plugin event methods now have type annotations. You might have been adding annotations to events already, but now they will be validated to match the original.

See [source code](https://github.com/mkdocs/mkdocs/blob/1.4.0/mkdocs/plugins.py#L165) and [documentation](../../dev-guide/plugins/#events).

One big update is that now you should annotate method parameters more specifically as `config: defaults.MkDocsConfig` instead of `config: base.Config`. This not only makes it clear that it is the [main config of MkDocs itself](https://github.com/mkdocs/mkdocs/blob/1.4.0/mkdocs/config/defaults.py), but also provides type-safe access through attributes of the object (see next section).

See [source code](https://github.com/mkdocs/mkdocs/blob/1.4.0/mkdocs/config/defaults.py) and [documentation](../../dev-guide/plugins/#on_event_name).

#### Rework ConfigOption schemas as class-based ([#2962](https://github.com/mkdocs/mkdocs/issues/2962 "GitHub Issue mkdocs/mkdocs #2962"))[](#rework-configoption-schemas-as-class-based-2962 "Permanent link")

When developing a plugin, the settings that it accepts used to be specified in the `config_scheme` variable on the plugin class.\
This approach is now soft-deprecated, and instead you should specify the config in a sub-class of `base.Config`.

Old example:

``` highlight
from mkdocs import plugins
from mkdocs.config import base, config_options

class MyPlugin(plugins.BasePlugin):
    config_scheme = (
        ('foo', config_options.Type(int)),
        ('bar', config_options.Type(str, default='')),
    )

    def on_page_markdown(self, markdown: str, *, config: base.Config, **kwargs):
        if self.config['foo'] < 5:
            if config['site_url'].startswith('http:'):
                return markdown + self.config['baz']
```

This code snippet actually has many mistakes but it will pass all type checks and silently run and even succeed in some cases.

So, on to the new equivalent example, changed to new-style schema and attribute-based access:\
(Complaints from \"mypy\" added inline)

``` highlight
from mkdocs import plugins
from mkdocs.config import base, config_options as c

class MyPluginConfig(base.Config):
    foo = c.Optional(c.Type(int))
    bar = c.Type(str, default='')

class MyPlugin(plugins.BasePlugin[MyPluginConfig]):
    def on_page_markdown(self, markdown: str, *, config: defaults.MkDocsConfig, **kwargs):
        if self.config.foo < 5:  # Error, `foo` might be `None`, need to check first.
            if config.site_url.startswith('http:'):  # Error, MkDocs' `site_url` also might be `None`.
                return markdown + self.config.baz  # Error, no such attribute `baz`!
```

This lets you notice the errors from a static type checker before running the code and fix them as such:

``` highlight
class MyPlugin(plugins.BasePlugin[MyPluginConfig]):
    def on_page_markdown(self, markdown: str, *, config: defaults.MkDocsConfig, **kwargs):
        if self.config.foo is not None and self.config.foo < 5:  # OK, `int < int` is valid.
            if (config.site_url or '').startswith('http:'):  # OK, `str.startswith(str)` is valid.
                return markdown + self.config.bar  # OK, `str + str` is valid.
```

See [**documentation**](../../dev-guide/plugins/#config_scheme).

Also notice that we had to explicitly mark the config attribute `foo` as `Optional`.\
The new-style config has all attributes marked as required by default, and specifying `required=False` or `required=True` is not allowed!

##### New: `config_options.Optional` ([#2962](https://github.com/mkdocs/mkdocs/issues/2962 "GitHub Issue mkdocs/mkdocs #2962"))[](#new-config_optionsoptional-2962 "Permanent link") 

Wrapping something into `Optional` is conceptually similar to \"I want the default to be `None`\" \-- and you *have* to express it like that, because writing `default=None` doesn\'t actually work.

Breaking change: the method `BaseConfigOption.is_required()` was removed. Use `.required` instead. ([#2938](https://github.com/mkdocs/mkdocs/issues/2938 "GitHub Issue mkdocs/mkdocs #2938"))\
And even the `required` property should be mostly unused now.\
For class-based configs, there\'s a new definition for whether an option is \"required\":

-   It has no default, and
-   It is not wrapped into `config_options.Optional`.

##### New: `config_options.ListOfItems` ([#2938](https://github.com/mkdocs/mkdocs/issues/2938 "GitHub Issue mkdocs/mkdocs #2938"))[](#new-config_optionslistofitems-2938 "Permanent link") 

Defines a list of items that each must adhere to the same constraint. Kind of like a validated `Type(list)`

Examples how to express a list of integers (with `from mkdocs.config import config_options as c`):

  Description                 Code entry
  --------------------------- ------------------------------------------------
  Required to specify         `foo = c.ListOfItems(c.Type(int))`
  Optional, default is \[\]   `foo = c.ListOfItems(c.Type(int), default=[])`
  Optional, default is None   `foo = c.Optional(c.ListOfItems(c.Type(int)))`

See more [examples in **documentation**](../../dev-guide/plugins/#examples-of-config-definitions).

##### Updated: `config_options.SubConfig` ([#2807](https://github.com/mkdocs/mkdocs/issues/2807 "GitHub Issue mkdocs/mkdocs #2807"))[](#updated-config_optionssubconfig-2807 "Permanent link") 

`SubConfig` used to silently ignore all validation of its config options. Now you should pass `validate=True` to it or just use new class-based configs where this became the default.

So, it can be used to validate a nested sub-dict with all keys pre-defined and value types strictly validated.

See [examples in **documentation**](../../dev-guide/plugins/#examples-of-config-definitions).

#### Other changes to config options[](#other-changes-to-config-options "Permanent link")

`URL`\'s default is now `None` instead of `''`. This can still be checked for truthiness in the same way - `if config.some_url:` ([#2962](https://github.com/mkdocs/mkdocs/issues/2962 "GitHub Issue mkdocs/mkdocs #2962"))

`FilesystemObject` is no longer abstract and can be used directly, standing for \"file or directory\" with optional existence checking ([#2938](https://github.com/mkdocs/mkdocs/issues/2938 "GitHub Issue mkdocs/mkdocs #2938"))

Bug fixes:

-   Fix `SubConfig`, `ConfigItems`, `MarkdownExtensions` to not leak values across different instances ([#2916](https://github.com/mkdocs/mkdocs/issues/2916 "GitHub Issue mkdocs/mkdocs #2916"), [#2290](https://github.com/mkdocs/mkdocs/issues/2290 "GitHub Issue mkdocs/mkdocs #2290"))
-   `SubConfig` raises the correct kind of validation error without a stack trace ([#2938](https://github.com/mkdocs/mkdocs/issues/2938 "GitHub Issue mkdocs/mkdocs #2938"))
-   Fix dot-separated redirect in `config_options.Deprecated(moved_to)` ([#2963](https://github.com/mkdocs/mkdocs/issues/2963 "GitHub Issue mkdocs/mkdocs #2963"))

Tweaked logic for handling `ConfigOption.default` ([#2938](https://github.com/mkdocs/mkdocs/issues/2938 "GitHub Issue mkdocs/mkdocs #2938"))

Deprecated config option classes: `ConfigItems` ([#2983](https://github.com/mkdocs/mkdocs/issues/2983 "GitHub Issue mkdocs/mkdocs #2983")), `OptionallyRequired` ([#2962](https://github.com/mkdocs/mkdocs/issues/2962 "GitHub Issue mkdocs/mkdocs #2962")), `RepoURL` ([#2927](https://github.com/mkdocs/mkdocs/issues/2927 "GitHub Issue mkdocs/mkdocs #2927"))

### Theme updates[](#theme-updates_1 "Permanent link") 

-   Styles of admonitions in \"MkDocs\" theme ([#2981](https://github.com/mkdocs/mkdocs/issues/2981 "GitHub Issue mkdocs/mkdocs #2981")):

    -   Update colors to increase contrast
    -   Apply admonition styles also to `<details>` tag, to support Markdown extensions that provide it ([pymdownx.details](https://facelessuser.github.io/pymdown-extensions/extensions/details/), [callouts](https://oprypin.github.io/markdown-callouts/#collapsible-blocks))

-   Built-in themes now also support these languages:

    -   Russian ([#2976](https://github.com/mkdocs/mkdocs/issues/2976 "GitHub Issue mkdocs/mkdocs #2976"))
    -   Turkish (Turkey) ([#2946](https://github.com/mkdocs/mkdocs/issues/2946 "GitHub Issue mkdocs/mkdocs #2946"))
    -   Ukrainian ([#2980](https://github.com/mkdocs/mkdocs/issues/2980 "GitHub Issue mkdocs/mkdocs #2980"))

### Future compatibility[](#future-compatibility "Permanent link")

-   `extra_css:` and `extra_javascript:` warn if a backslash `\` is passed to them. ([#2930](https://github.com/mkdocs/mkdocs/issues/2930 "GitHub Issue mkdocs/mkdocs #2930"), [#2984](https://github.com/mkdocs/mkdocs/issues/2984 "GitHub Issue mkdocs/mkdocs #2984"))

-   Show `DeprecationWarning`s as INFO messages. ([#2907](https://github.com/mkdocs/mkdocs/issues/2907 "GitHub Issue mkdocs/mkdocs #2907"))

    If any plugin or extension that you use relies on deprecated functionality of other libraries, it is at risk of breaking in the near future. Plugin developers should address these in a timely manner.

-   Avoid a dependency on `importlib_metadata` starting from Python 3.10 ([#2959](https://github.com/mkdocs/mkdocs/issues/2959 "GitHub Issue mkdocs/mkdocs #2959"))

-   Drop support for Python 3.6 ([#2948](https://github.com/mkdocs/mkdocs/issues/2948 "GitHub Issue mkdocs/mkdocs #2948"))

#### Incompatible changes to public APIs[](#incompatible-changes-to-public-apis "Permanent link")

-   `mkdocs.utils`:
    -   `create_media_urls` and `normalize_url` warn if a backslash `\` is passed to them. ([#2930](https://github.com/mkdocs/mkdocs/issues/2930 "GitHub Issue mkdocs/mkdocs #2930"))
    -   `is_markdown_file` stops accepting case-insensitive variants such as `.MD`, which is how MkDocs build was already operating. ([#2912](https://github.com/mkdocs/mkdocs/issues/2912 "GitHub Issue mkdocs/mkdocs #2912"))
    -   Hard-deprecated: `modified_time`, `reduce_list`, `get_html_path`, `get_url_path`, `is_html_file`, `is_template_file`. ([#2912](https://github.com/mkdocs/mkdocs/issues/2912 "GitHub Issue mkdocs/mkdocs #2912"))

### Miscellaneous[](#miscellaneous "Permanent link")

-   If a plugin adds paths to `watch` in `LiveReloadServer`, it can now `unwatch` them. ([#2777](https://github.com/mkdocs/mkdocs/issues/2777 "GitHub Issue mkdocs/mkdocs #2777"))

-   Bugfix (regression in 1.2): Support listening on an IPv6 address in `mkdocs serve`. ([#2951](https://github.com/mkdocs/mkdocs/issues/2951 "GitHub Issue mkdocs/mkdocs #2951"))

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.3.1...1.4.0).

## Version 1.3.1 (2022-07-19)[](#version-131-2022-07-19 "Permanent link") 

-   Pin Python-Markdown version to \<3.4, thus excluding its latest release that breaks too many external extensions ([#2893](https://github.com/mkdocs/mkdocs/issues/2893 "GitHub Issue mkdocs/mkdocs #2893"))

-   When a Markdown extension fails to load, print its name and traceback ([#2894](https://github.com/mkdocs/mkdocs/issues/2894 "GitHub Issue mkdocs/mkdocs #2894"))

-   Bugfix for \"readthedocs\" theme (regression in 1.3.0): add missing space in breadcrumbs ([#2810](https://github.com/mkdocs/mkdocs/issues/2810 "GitHub Issue mkdocs/mkdocs #2810"))

-   Bugfix: don\'t complain when a file \"readme.md\" (lowercase) exists, it\'s not recognized otherwise ([#2852](https://github.com/mkdocs/mkdocs/issues/2852 "GitHub Issue mkdocs/mkdocs #2852"))

-   Built-in themes now also support these languages:

    -   Italian ([#2860](https://github.com/mkdocs/mkdocs/issues/2860 "GitHub Issue mkdocs/mkdocs #2860"))

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.3.0...1.3.1).

## Version 1.3.0 (2022-03-26)[](#version-130-2022-03-26 "Permanent link") 

### Feature upgrades[](#feature-upgrades_1 "Permanent link") 

-   ReadTheDocs theme updated from v0.4.1 to v1.0.0 according to upstream ([#2585](https://github.com/mkdocs/mkdocs/issues/2585 "GitHub Issue mkdocs/mkdocs #2585"))

    The most notable changes:

    -   New option `logo`: Rather than displaying the `site_name` in the title, one can specify a path to an image to display instead.
    -   New option `anonymize_ip` for Google Analytics.
    -   Dependencies were upgraded: jQuery upgraded to 3.6.0, Modernizr.js dropped, and others.

    See [documentation of config options for the theme](https://www.mkdocs.org/user-guide/choosing-your-theme/#readthedocs)

-   Built-in themes now also support these languages:

    -   German ([#2633](https://github.com/mkdocs/mkdocs/issues/2633 "GitHub Issue mkdocs/mkdocs #2633"))
    -   Persian (Farsi) ([#2787](https://github.com/mkdocs/mkdocs/issues/2787 "GitHub Issue mkdocs/mkdocs #2787"))

-   Support custom directories to watch when running `mkdocs serve` ([#2642](https://github.com/mkdocs/mkdocs/issues/2642 "GitHub Issue mkdocs/mkdocs #2642"))

    MkDocs by default watches the *docs* directory and the config file. Now there is a way to add more directories to watch for changes, either via the YAML `watch` key or the command line flag `--watch`.

    Normally MkDocs never reaches into any other directories (so this feature shouldn\'t be necessary), but some plugins and extensions may do so.

    See [documentation](https://www.mkdocs.org/user-guide/configuration/#watch).

-   New `--no-history` option for `gh_deploy` ([#2594](https://github.com/mkdocs/mkdocs/issues/2594 "GitHub Issue mkdocs/mkdocs #2594"))

    Allows to discard the history of commits when deploying, and instead replace it with one root commit

### Bug fixes[](#bug-fixes_1 "Permanent link") 

-   An XSS vulnerability when using the search function in built-in themes was fixed ([#2791](https://github.com/mkdocs/mkdocs/issues/2791 "GitHub Issue mkdocs/mkdocs #2791"))

-   Setting the `edit_uri` option no longer erroneously adds a trailing slash to `repo_url` ([#2733](https://github.com/mkdocs/mkdocs/issues/2733 "GitHub Issue mkdocs/mkdocs #2733"))

### Miscellaneous[](#miscellaneous_1 "Permanent link") 

-   Breaking change: the `pages` config option that was deprecated for a very long time now causes an error when used ([#2652](https://github.com/mkdocs/mkdocs/issues/2652 "GitHub Issue mkdocs/mkdocs #2652"))

    To fix the error, just change from `pages` to `nav`.

-   Performance optimization: during startup of MkDocs, code and dependencies of other commands will not be imported ([#2714](https://github.com/mkdocs/mkdocs/issues/2714 "GitHub Issue mkdocs/mkdocs #2714"))

    The most visible effect of this is that dependencies of `mkdocs serve` will not be imported when `mkdocs build` is used.

-   Recursively validate `nav` ([#2680](https://github.com/mkdocs/mkdocs/issues/2680 "GitHub Issue mkdocs/mkdocs #2680"))

    Validation of the nested `nav` structure has been reworked to report errors early and reliably. Some [edge cases](https://github.com/mkdocs/mkdocs/blob/b7272150bbc9bf8f66c878f6517742de3528972b/mkdocs/tests/config/config_options_tests.py#L783) have been declared invalid.

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.2.3...1.3.0).

## Version 1.2.4 (2022-03-26)[](#version-124-2022-03-26 "Permanent link") 

-   Compatibility with Jinja2 3.1.0 ([#2800](https://github.com/mkdocs/mkdocs/issues/2800 "GitHub Issue mkdocs/mkdocs #2800"))

    Due to a breaking change in Jinja2, MkDocs would crash with the message `AttributeError: module 'jinja2' has no attribute 'contextfilter'`

## Version 1.2.3 (2021-10-12)[](#version-123-2021-10-12 "Permanent link") 

-   Built-in themes now also support these languages:

    -   Simplified Chinese ([#2497](https://github.com/mkdocs/mkdocs/issues/2497 "GitHub Issue mkdocs/mkdocs #2497"))
    -   Japanese ([#2525](https://github.com/mkdocs/mkdocs/issues/2525 "GitHub Issue mkdocs/mkdocs #2525"))
    -   Brazilian Portuguese ([#2535](https://github.com/mkdocs/mkdocs/issues/2535 "GitHub Issue mkdocs/mkdocs #2535"))
    -   Spanish ([#2545](https://github.com/mkdocs/mkdocs/issues/2545 "GitHub Issue mkdocs/mkdocs #2545"), previously [#2396](https://github.com/mkdocs/mkdocs/issues/2396 "GitHub Issue mkdocs/mkdocs #2396"))

-   Third-party plugins will take precedence over built-in plugins with the same name ([#2591](https://github.com/mkdocs/mkdocs/issues/2591 "GitHub Issue mkdocs/mkdocs #2591"))

-   Bugfix: Fix ability to load translations for some languages: core support ([#2565](https://github.com/mkdocs/mkdocs/issues/2565 "GitHub Issue mkdocs/mkdocs #2565")) and search plugin support with fallbacks ([#2602](https://github.com/mkdocs/mkdocs/issues/2602 "GitHub Issue mkdocs/mkdocs #2602"))

-   Bugfix (regression in 1.2): Prevent directory traversal in the dev server ([#2604](https://github.com/mkdocs/mkdocs/issues/2604 "GitHub Issue mkdocs/mkdocs #2604"))

-   Bugfix (regression in 1.2): Prevent webserver warnings from being treated as a build failure in strict mode ([#2607](https://github.com/mkdocs/mkdocs/issues/2607 "GitHub Issue mkdocs/mkdocs #2607"))

-   Bugfix: Correctly print colorful messages in the terminal on Windows ([#2606](https://github.com/mkdocs/mkdocs/issues/2606 "GitHub Issue mkdocs/mkdocs #2606"))

-   Bugfix: Python version 3.10 was displayed incorrectly in `--version` ([#2618](https://github.com/mkdocs/mkdocs/issues/2618 "GitHub Issue mkdocs/mkdocs #2618"))

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.2.2...1.2.3).

## Version 1.2.2 (2021-07-18)[](#version-122-2021-07-18 "Permanent link") 

-   Bugfix (regression in 1.2): Fix serving files/paths with Unicode characters ([#2464](https://github.com/mkdocs/mkdocs/issues/2464 "GitHub Issue mkdocs/mkdocs #2464"))

-   Bugfix (regression in 1.2): Revert livereload file watching to use polling observer ([#2477](https://github.com/mkdocs/mkdocs/issues/2477 "GitHub Issue mkdocs/mkdocs #2477"))

    This had to be done to reasonably support usages that span virtual filesystems such as non-native Docker and network mounts.

    This goes back to the polling approach, very similar to that was always used prior, meaning most of the same downsides with latency and CPU usage.

-   Revert from 1.2: Remove the requirement of a `site_url` config and the restriction on `use_directory_urls` ([#2490](https://github.com/mkdocs/mkdocs/issues/2490 "GitHub Issue mkdocs/mkdocs #2490"))

-   Bugfix (regression in 1.2): Don\'t require trailing slash in the URL when serving a directory index in `mkdocs serve` server ([#2507](https://github.com/mkdocs/mkdocs/issues/2507 "GitHub Issue mkdocs/mkdocs #2507"))

    Instead of showing a 404 error, detect if it\'s a directory and redirect to a path with a trailing slash added, like before.

-   Bugfix: Fix `gh_deploy` with config-file in the current directory ([#2481](https://github.com/mkdocs/mkdocs/issues/2481 "GitHub Issue mkdocs/mkdocs #2481"))

-   Bugfix: Fix reversed breadcrumbs in \"readthedocs\" theme ([#2179](https://github.com/mkdocs/mkdocs/issues/2179 "GitHub Issue mkdocs/mkdocs #2179"))

-   Allow \"mkdocs.yaml\" as the file name when \'\--config\' is not passed ([#2478](https://github.com/mkdocs/mkdocs/issues/2478 "GitHub Issue mkdocs/mkdocs #2478"))

-   Stop treating \";\" as a special character in URLs: urlparse -\> urlsplit ([#2502](https://github.com/mkdocs/mkdocs/issues/2502 "GitHub Issue mkdocs/mkdocs #2502"))

-   Improve build performance for sites with many pages (partly already done in 1.2) ([#2407](https://github.com/mkdocs/mkdocs/issues/2407 "GitHub Issue mkdocs/mkdocs #2407"))

## Version 1.2.1 (2021-06-09)[](#version-121-2021-06-09 "Permanent link") 

-   Bugfix (regression in 1.2): Ensure \'gh-deploy\' always pushes.

## Version 1.2 (2021-06-04)[](#version-12-2021-06-04 "Permanent link") 

### Major Additions to Version 1.2[](#major-additions-to-version-12 "Permanent link") 

#### Support added for Theme Localization ([#2299](https://github.com/mkdocs/mkdocs/issues/2299 "GitHub Issue mkdocs/mkdocs #2299"))[](#support-added-for-theme-localization-2299 "Permanent link")

The `mkdocs` and `readthedocs` themes now support language localization using the `theme.locale` parameter, which defaults to `en` (English). The only other supported languages in this release are `fr` (French) and `es` (Spanish). For details on using the provided translations, see the [user guide](../../user-guide/localizing-your-theme/). Note that translation will not happen by default. Users must first install the necessary dependencies with the following command:

``` highlight
pip install 'mkdocs[i18n]'
```

Translation contributions are welcome and detailed in the [Translation Guide](../../dev-guide/translations/).

Developers of third party themes may want to review the relevant section of the [Theme Development Guide](../../dev-guide/themes/#supporting-theme-localizationtranslation).

Contributors who are updating the templates to the built-in themes should review the [Contributing Guide](../contributing/#submitting-changes-to-the-builtin-themes).

The `lang` setting of the `search` plugin now defaults to the language specified in `theme.locale`.

#### Support added for Environment Variables in the configuration file ([#1954](https://github.com/mkdocs/mkdocs/issues/1954 "GitHub Issue mkdocs/mkdocs #1954"))[](#support-added-for-environment-variables-in-the-configuration-file-1954 "Permanent link")

Environments variables may now be specified in the configuration file with the `!ENV` tag. The value of the variable will be parsed by the YAML parser and converted to the appropriate type.

``` highlight
somekey: !ENV VAR_NAME
otherkey: !ENV [VAR_NAME, FALLBACK_VAR, 'default value']
```

See [Environment Variables](../../user-guide/configuration/#environment-variables) in the Configuration documentation for details.

#### Support added for Configuration Inheritance ([#2218](https://github.com/mkdocs/mkdocs/issues/2218 "GitHub Issue mkdocs/mkdocs #2218"))[](#support-added-for-configuration-inheritance-2218 "Permanent link")

A configuration file may now inherit from a parent configuration file. In the primary file set the `INHERIT` key to the relative path of the parent file.

``` highlight
INHERIT: path/to/base.yml
```

The two files will then be deep merged. See [Configuration Inheritance](../../user-guide/configuration/#configuration-inheritance) for details.

#### Update `gh-deploy` command ([#2170](https://github.com/mkdocs/mkdocs/issues/2170 "GitHub Issue mkdocs/mkdocs #2170"))[](#update-gh-deploy-command-2170 "Permanent link")

The vendored (and modified) copy of ghp_import has been replaced with a dependency on the upstream library. As of version 1.0.0, [ghp-import](https://github.com/c-w/ghp-import/) includes a Python API which makes it possible to call directly.

MkDocs can now benefit from recent bug fixes and new features, including the following:

-   A `.nojekyll` file is automatically included when deploying to GitHub Pages.
-   The `--shell` flag is now available, which reportedly works better on Windows.
-   Git author and committer environment variables should be respected ([#1383](https://github.com/mkdocs/mkdocs/issues/1383 "GitHub Issue mkdocs/mkdocs #1383")).

#### Rework auto-reload and HTTP server for `mkdocs serve` ([#2385](https://github.com/mkdocs/mkdocs/issues/2385 "GitHub Issue mkdocs/mkdocs #2385"))[](#rework-auto-reload-and-http-server-for-mkdocs-serve-2385 "Permanent link")

`mkdocs serve` now uses a new underlying server + file watcher implementation, based on [http.server](https://docs.python.org/3/library/http.server.html) from standard library and [watchdog](https://pypi.org/project/watchdog/). It provides similar functionality to the previously used [livereload](https://pypi.org/project/livereload/) library (which is now dropped from dependencies, along with [tornado](https://pypi.org/project/tornado/)).

This makes reloads more responsive and consistent in terms of timing. Multiple rapid file changes no longer cause the site to repeatedly rebuild (issue [#2061](https://github.com/mkdocs/mkdocs/issues/2061 "GitHub Issue mkdocs/mkdocs #2061")).

Almost every aspect of the server is slightly different, but actual visible changes are minor. The logging outputs are only *similar* to the old ones. Degradations in behavior are not expected, and should be reported if found.

##### Offset the local site root according to the sub-path of the `site_url` ([#2424](https://github.com/mkdocs/mkdocs/issues/2424 "GitHub Issue mkdocs/mkdocs #2424"))[](#offset-the-local-site-root-according-to-the-sub-path-of-the-site_url-2424 "Permanent link")

When using `mkdocs serve` and having the `site_url` specified as e.g. `http://example.org/sub/path/`, now the root of the locally served site becomes `http://127.0.0.1:8000/sub/path/` and all document paths are offset accordingly.

#### A `build_error` event was added ([#2103](https://github.com/mkdocs/mkdocs/issues/2103 "GitHub Issue mkdocs/mkdocs #2103"))[](#a-build_error-event-was-added-2103 "Permanent link")

Plugin developers can now use the `on_build_error` hook to execute code when an exception is raised while building the site.

See [`on_build_error`](../../dev-guide/plugins/#on_build_error) in the Plugins documentation for details.

#### Three new exceptions: BuildError PluginError and Abort ([#2103](https://github.com/mkdocs/mkdocs/issues/2103 "GitHub Issue mkdocs/mkdocs #2103"))[](#three-new-exceptions-builderror-pluginerror-and-abort-2103 "Permanent link")

MkDocs now has tree new exceptions defined in `mkdocs.exceptions`: `BuildError`, `PluginError`, and `Abort`:

-   `PluginError` can be raised from a plugin to stop the build and log an error message *without traceback*.
-   `BuildError` should not be used by third-party plugins developers and is reserved for internal use only.
-   `Abort` is used internally to abort the build and display an error without a traceback.

See [`Handling errors`](../../dev-guide/plugins/#handling-errors) in the Plugins documentation for details.

#### Search Indexing Strategy configuration[](#search-indexing-strategy-configuration "Permanent link")

Users can now specify which strategy they wish to use when indexing their site for search. A user can select between the following options:

-   **full**: Adds page title, section headings, and full page text to the search index.
-   **sections**: Adds page titles and section headings only to the search index.
-   **titles**: Adds only the page titles to the search index.

See [`Search Indexing`](../../user-guide/configuration/#indexing) in the configuration documentation for details.

### Backward Incompatible Changes in 1.2[](#backward-incompatible-changes-in-12 "Permanent link") 

-   The [site_url](../../user-guide/configuration/#site_url) configuration option is now **required**. If it is not set, a warning will be issued. In a future release an error will be raised ([#2189](https://github.com/mkdocs/mkdocs/issues/2189 "GitHub Issue mkdocs/mkdocs #2189")).

    The [use_directory_urls](../../user-guide/configuration/#use_directory_urls) configuration option will be forced to `false` if [site_url](../../user-guide/configuration/#site_url) is set to an empty string. In that case, if `use_directory_urls` is not explicitly set to `false`, a warning will be issued ([#2189](https://github.com/mkdocs/mkdocs/issues/2189 "GitHub Issue mkdocs/mkdocs #2189")).

    ::: 
    Note

    This was reverted in release 1.2.2
    :::

-   The `google_analytics` configuration option is deprecated as Google appears to be phasing it out in favor of its new Google Analytics 4 property. See the documentation for your theme for alternatives which can be configured as part of your theme configuration. For example, the [mkdocs](../../user-guide/choosing-your-theme/#mkdocs) and [readthedocs](../../user-guide/choosing-your-theme/#readthedocs) themes have each added a new `theme.analytics.gtag` configuration option which uses the new Google Analytics 4 property. See Google\'s documentation on how to [Upgrade to a Google Analytics 4 property](https://support.google.com/analytics/answer/9744165?hl=en). Then set `theme.analytics.gtag` to the \"G-\" ID and delete the `google_analytics` configuration option which contains a \"UA-\" ID. So long as the old \"UA-\" ID and new \"G-\" ID are properly linked in your Google account, and you are using the \"G-\" ID, the data will be made available in both the old and new formats by Google Analytics. See [#2252](https://github.com/mkdocs/mkdocs/issues/2252 "GitHub Issue mkdocs/mkdocs #2252").

-   A theme\'s files are now excluded from the list of watched files by default when using the `--livereload` server. This new default behavior is what most users need and provides better performance when editing site content. Theme developers can enable the old behavior with the `--watch-theme` option. ([#2092](https://github.com/mkdocs/mkdocs/issues/2092 "GitHub Issue mkdocs/mkdocs #2092")).

-   The `mkdocs` theme now removes the sidebar when printing a page. This frees up horizontal space for better rendering of content like tables ([#2193](https://github.com/mkdocs/mkdocs/issues/2193 "GitHub Issue mkdocs/mkdocs #2193")).

-   The `mkdocs.config.DEFAULT_SCHEMA` global variable has been replaced with the function `mkdocs.config.defaults.get_schema()`, which ensures that each instance of the configuration is unique ([#2289](https://github.com/mkdocs/mkdocs/issues/2289 "GitHub Issue mkdocs/mkdocs #2289")).

-   The `mkdocs.utils.warning_filter` is deprecated and now does nothing. Plugins should remove any reference to is as it may be deleted in a future release. To ensure any warnings get counted, simply log them to the `mkdocs` log (i.e.: `mkdocs.plugins.pluginname`).

-   The `on_serve` event (which receives the `server` object and the `builder` function) is affected by the server rewrite. `server` is now a `mkdocs.livereload.LiveReloadServer` instead of `livereload.server.Server`. The typical action that plugins can do with these is to call `server.watch(some_dir, builder)`, which basically adds that directory to watched directories, causing the site to be rebuilt on file changes. That still works, but passing any other function to `watch` is deprecated and shows a warning. This 2nd parameter is already optional, and will accept only this exact `builder` function just for compatibility.

-   The `python` method of the `plugins.search.prebuild_index` configuration option is pending deprecation as of version 1.2. It is expected that in version 1.3 it will raise a warning if used and in version 1.4 it will raise an error. Users are encouraged to use an alternate method to generate a prebuilt index for search.

-   The `lunr` and `lunr[languages]` dependencies are no longer installed by default. The dependencies are only needed for the rare user who pre-builds the search index and uses the `python` option, which is now pending deprecation. If you use this feature, then you will need to manually install `lunr` and `lunr[languages]`. A warning is issued if the dependencies are needed but not installed.

### Other Changes and Additions to Version 1.2[](#other-changes-and-additions-to-version-12 "Permanent link") 

-   Bugfix: Properly process navigation child items in `_get_by_type` when filtering for sections ([#2203](https://github.com/mkdocs/mkdocs/issues/2203 "GitHub Issue mkdocs/mkdocs #2203")).
-   Official support for Python 3.9 has been added and support for Python 3.5 has been dropped.
-   Bugfix: Fixes an issue that would result in a partially cut-off navigation item in the ReadTheDocs theme ([#2297](https://github.com/mkdocs/mkdocs/issues/2297 "GitHub Issue mkdocs/mkdocs #2297")).
-   Structure Files object now has a `remove` method to help plugin developers manipulate the Files tree. The corresponding `src_paths` has become a property to accommodate this possible dynamic behavior. See [#2305](https://github.com/mkdocs/mkdocs/issues/2305 "GitHub Issue mkdocs/mkdocs #2305").
-   Updated highlight.js to 10.5.0. See [#2313](https://github.com/mkdocs/mkdocs/issues/2313 "GitHub Issue mkdocs/mkdocs #2313").
-   Bugfix: Search plugin now works with Japanese language. See [#2178](https://github.com/mkdocs/mkdocs/issues/2178 "GitHub Issue mkdocs/mkdocs #2178").
-   Documentation has been refactored ([#1629](https://github.com/mkdocs/mkdocs/issues/1629 "GitHub Issue mkdocs/mkdocs #1629")).
-   Restore styling of tables in the `readthedocs` theme ([#2028](https://github.com/mkdocs/mkdocs/issues/2028 "GitHub Issue mkdocs/mkdocs #2028")).
-   Ensure `site_url` ends with a slash ([#1785](https://github.com/mkdocs/mkdocs/issues/1785 "GitHub Issue mkdocs/mkdocs #1785")).
-   Correct documentation of `pages` template context variable ([#1736](https://github.com/mkdocs/mkdocs/issues/1736 "GitHub Issue mkdocs/mkdocs #1736")).
-   The `lunr` dependency has been updated to 0.5.9, and `lunr.js` to the corresponding 2.3.9 version ([#2306](https://github.com/mkdocs/mkdocs/issues/2306 "GitHub Issue mkdocs/mkdocs #2306")).
-   Color is now used in log messages to identify errors, warnings and debug messages.
-   Bugfix: Identify homepage when `use_directory_urls` is `False` ([#2362](https://github.com/mkdocs/mkdocs/issues/2362 "GitHub Issue mkdocs/mkdocs #2362")).

## Version 1.1.2 (2020-05-14)[](#version-112-2020-05-14 "Permanent link") 

-   Bugfix: Normalize IP addresses and change unsupported address error to a warning ([#2108](https://github.com/mkdocs/mkdocs/issues/2108 "GitHub Issue mkdocs/mkdocs #2108")).

## Version 1.1.1 (2020-05-12)[](#version-111-2020-05-12 "Permanent link") 

-   Bugfix: Allow compressed sitemap to be deterministic by supporting the `SOURCE_DATE_EPOCH` environment variable ([#2100](https://github.com/mkdocs/mkdocs/issues/2100 "GitHub Issue mkdocs/mkdocs #2100")).
-   Bugfix: Use `README.md` as `index.html` even if `use_directory_urls` is false ([#2081](https://github.com/mkdocs/mkdocs/issues/2081 "GitHub Issue mkdocs/mkdocs #2081")).
-   Bugfix: Ignore links which start with a backslash ([#1680](https://github.com/mkdocs/mkdocs/issues/1680 "GitHub Issue mkdocs/mkdocs #1680")).
-   Bugfix: Pass `builder` to the `on_serve` event so that it can be passed to `server.watch` by plugins ([#1952](https://github.com/mkdocs/mkdocs/issues/1952 "GitHub Issue mkdocs/mkdocs #1952")).
-   Bugfix: Use `lunr[languages]==0.5.8` to avoid `nltk` incompatibilities ([#2062](https://github.com/mkdocs/mkdocs/issues/2062 "GitHub Issue mkdocs/mkdocs #2062")).
-   Bugfix: Ensure wheel is Python 3 only ([#2021](https://github.com/mkdocs/mkdocs/issues/2021 "GitHub Issue mkdocs/mkdocs #2021")).
-   Bugfix: Clean up `dev_addr` validation and disallow `0.0.0.0` ([#2022](https://github.com/mkdocs/mkdocs/issues/2022 "GitHub Issue mkdocs/mkdocs #2022")).
-   Add support for `min_search_length` parameter for search plugin ([#2014](https://github.com/mkdocs/mkdocs/issues/2014 "GitHub Issue mkdocs/mkdocs #2014")).
-   Bugfix: `readthedocs` theme `code` colors ([#2027](https://github.com/mkdocs/mkdocs/issues/2027 "GitHub Issue mkdocs/mkdocs #2027")).

## Version 1.1 (2020-02-22)[](#version-11-2020-02-22 "Permanent link") 

### Major Additions to Version 1.1[](#major-additions-to-version-11 "Permanent link") 

#### Support for Lunr.py as `prebuild_index` engine[](#support-for-lunrpy-as-prebuild_index-engine "Permanent link") 

Mkdocs now supports pre-building indices using [Lunr.py](http://lunr.readthedocs.io/), a pure Python implementation of Lunr.js, allowing the user to avoid installing a NodeJS environment if so desired. For more information please read the [`prebuild_index` documentation](../../user-guide/configuration/#prebuild_index).

#### `readthedocs` theme updated with upstream ([#588](https://github.com/mkdocs/mkdocs/issues/588 "GitHub Issue mkdocs/mkdocs #588") and [#1374](https://github.com/mkdocs/mkdocs/issues/1374 "GitHub Issue mkdocs/mkdocs #1374"))[](#readthedocs-theme-updated-with-upstream-588-and-1374 "Permanent link")

The `readthedocs` theme now more closely matches the [upstream](https://github.com/rtfd/sphinx_rtd_theme/) Sphinx theme (version 0.4.1). A number of new theme configuration settings were added which mirror the upstream configuration options. See the [theme documentation](../../user-guide/choosing-your-theme/#readthedocs) for details.

#### Update `mkdocs` theme to Bootswatch 4.1.3 ([#1563](https://github.com/mkdocs/mkdocs/issues/1563 "GitHub Issue mkdocs/mkdocs #1563"))[](#update-mkdocs-theme-to-bootswatch-413-1563 "Permanent link") 

The `mkdocs` theme now supports all the features of [Bootswatch 4.1](https://getbootstrap.com/docs/4.1/getting-started/introduction/). Additionally, 2 filenames were changed in this update. If you are using a theme which inherits from the `mkdocs` theme, the theme developer may need to update these filenames as follows.

``` highlight
css/bootstrap-custom.min.css => css/bootstrap.min.css
js/bootstrap-3.0.3.min.js => js/bootstrap.min.js
```

#### Improved configuration support on the command line ([#1401](https://github.com/mkdocs/mkdocs/issues/1401 "GitHub Issue mkdocs/mkdocs #1401"))[](#improved-configuration-support-on-the-command-line-1401 "Permanent link")

The `build`, `serve`, and `gh-deploy` subcommands now support flags to control whether [directory URLs](../../user-guide/configuration/#use_directory_urls) should be created: `--use-directory-urls` / `--no-directory-urls`. In addition, the `gh-deploy` subcommand now supports all the configuration options that `build` and `serve` do, adding `--strict`, `--theme`, `--theme-dir`, and `--site-dir`.

#### Updated lunr-languages support ([#1729](https://github.com/mkdocs/mkdocs/issues/1729 "GitHub Issue mkdocs/mkdocs #1729"))[](#updated-lunr-languages-support-1729 "Permanent link")

The `lunr-languages` plugin has been updated to 1.4.0, adding support for Arabic (`ar`) and Vietnamese (`vi`) languages. In addition, the Dutch and Japanese language codes have been changed to their standard values: `nl` and `ja`, respectively. The old language codes (`du` and `jp`) remain as aliases but may be removed in a future version of MkDocs.

### Other Changes and Additions to Version 1.1[](#other-changes-and-additions-to-version-11 "Permanent link") 

-   Bugfix: Ensure nested dot files in themes are ignored and document behavior ([#1981](https://github.com/mkdocs/mkdocs/issues/1981 "GitHub Issue mkdocs/mkdocs #1981")).
-   Update minimum dependency to Markdown 3.2.1.
-   Updated minimum dependency to Jinja 2.10.1 to address security concerns ([#1780](https://github.com/mkdocs/mkdocs/issues/1780 "GitHub Issue mkdocs/mkdocs #1780")).
-   Update to lunr.js 2.3.8 ([#1989](https://github.com/mkdocs/mkdocs/issues/1989 "GitHub Issue mkdocs/mkdocs #1989")).
-   Add support for Python 3.8.
-   Drop support for Python 3.4.
-   Drop support for Python 2.7. MkDocs is PY3 only now ([#1926](https://github.com/mkdocs/mkdocs/issues/1926 "GitHub Issue mkdocs/mkdocs #1926")).
-   Bugfix: Select appropriate asyncio event loop on Windows for Python 3.8+ ([#1885](https://github.com/mkdocs/mkdocs/issues/1885 "GitHub Issue mkdocs/mkdocs #1885")).
-   Bugfix: Ensure nested index pages do not get identified as the homepage ([#1919](https://github.com/mkdocs/mkdocs/issues/1919 "GitHub Issue mkdocs/mkdocs #1919")).
-   Bugfix: Properly identify deployment version ([#1879](https://github.com/mkdocs/mkdocs/issues/1879 "GitHub Issue mkdocs/mkdocs #1879")).
-   Bugfix: Properly build `ValidationError` message for `custom_dir` ([#1849](https://github.com/mkdocs/mkdocs/issues/1849 "GitHub Issue mkdocs/mkdocs #1849")).
-   Bugfix: Exclude Markdown files and READMEs from theme ([#1766](https://github.com/mkdocs/mkdocs/issues/1766 "GitHub Issue mkdocs/mkdocs #1766")).
-   Bugfix: Account for encoded URLs ([#1670](https://github.com/mkdocs/mkdocs/issues/1670 "GitHub Issue mkdocs/mkdocs #1670")).
-   Bugfix: Ensure theme files do not override `docs_dir` files ([#1671](https://github.com/mkdocs/mkdocs/issues/1671 "GitHub Issue mkdocs/mkdocs #1671")).
-   Bugfix: Do not normalize URL fragments ([#1655](https://github.com/mkdocs/mkdocs/issues/1655 "GitHub Issue mkdocs/mkdocs #1655")).
-   Bugfix: Skip external URLs in sitemap.xml ([#1742](https://github.com/mkdocs/mkdocs/issues/1742 "GitHub Issue mkdocs/mkdocs #1742")).
-   Bugfix: Ensure theme files do not override docs_dir files on Windows ([#1876](https://github.com/mkdocs/mkdocs/issues/1876 "GitHub Issue mkdocs/mkdocs #1876"))
-   Add canonical tag to `readthedocs` theme ([#1669](https://github.com/mkdocs/mkdocs/issues/1669 "GitHub Issue mkdocs/mkdocs #1669")).
-   Improved error message for when `git` is not available.
-   Add support for `nav_style` theme option for the `mkdocs` theme ([#1930](https://github.com/mkdocs/mkdocs/issues/1930 "GitHub Issue mkdocs/mkdocs #1930")).
-   Bugfix: Long/nested dropdowns now behave more consistently for the `mkdocs` theme ([#1234](https://github.com/mkdocs/mkdocs/issues/1234 "GitHub Issue mkdocs/mkdocs #1234")).
-   Bugfix: Multi-row nav headers in the `mkdocs` theme no longer obscure the document content ([#716](https://github.com/mkdocs/mkdocs/issues/716 "GitHub Issue mkdocs/mkdocs #716")).
-   Add support for `navigation_depth` theme option for the `mkdocs` theme ([#1970](https://github.com/mkdocs/mkdocs/issues/1970 "GitHub Issue mkdocs/mkdocs #1970")).
-   `level` attribute in `page.toc` items is now 1-indexed to match the level in `<hN>` tags ([#1970](https://github.com/mkdocs/mkdocs/issues/1970 "GitHub Issue mkdocs/mkdocs #1970")).

## Version 1.0.4 (2018-09-07)[](#version-104-2018-09-07 "Permanent link") 

-   Bugfix: Ignore absolute links in Markdown ([#1621](https://github.com/mkdocs/mkdocs/issues/1621 "GitHub Issue mkdocs/mkdocs #1621")).

## Version 1.0.3 (2018-08-29)[](#version-103-2018-08-29 "Permanent link") 

-   Bugfix: Warn on relative paths in navigation ([#1604](https://github.com/mkdocs/mkdocs/issues/1604 "GitHub Issue mkdocs/mkdocs #1604")).
-   Bugfix: Handle empty `theme_config.yml` files correctly ([#1602](https://github.com/mkdocs/mkdocs/issues/1602 "GitHub Issue mkdocs/mkdocs #1602")).

## Version 1.0.2 (2018-08-22)[](#version-102-2018-08-22 "Permanent link") 

-   Bugfix: Provide absolute `base_url` to error templates ([#1598](https://github.com/mkdocs/mkdocs/issues/1598 "GitHub Issue mkdocs/mkdocs #1598")).

## Version 1.0.1 (2018-08-13)[](#version-101-2018-08-13 "Permanent link") 

-   Bugfix: Prevent page reload when \[Enter\] is pressed in search box ([#1589](https://github.com/mkdocs/mkdocs/issues/1589 "GitHub Issue mkdocs/mkdocs #1589")).
-   Bugfix: Avoid calling `search` until all assets are ready ([#1584](https://github.com/mkdocs/mkdocs/issues/1584 "GitHub Issue mkdocs/mkdocs #1584")).
-   Bugfix: Exclude `README.md` if `index.md` is present ([#1580](https://github.com/mkdocs/mkdocs/issues/1580 "GitHub Issue mkdocs/mkdocs #1580")).
-   Bugfix: Fix `readthedocs` theme navigation bug with homepage ([#1576](https://github.com/mkdocs/mkdocs/issues/1576 "GitHub Issue mkdocs/mkdocs #1576")).

## Version 1.0 (2018-08-03)[](#version-10-2018-08-03 "Permanent link") 

### Major Additions to Version 1.0[](#major-additions-to-version-10 "Permanent link") 

#### Internal Refactor of Pages, Files, and Navigation[](#internal-refactor-of-pages-files-and-navigation "Permanent link")

Internal handling of pages, files and navigation has been completely refactored. The changes included in the refactor are summarized below.

-   Support for hidden pages. All Markdown pages are now included in the build regardless of whether they are included in the navigation configuration ([#699](https://github.com/mkdocs/mkdocs/issues/699 "GitHub Issue mkdocs/mkdocs #699")).
-   The navigation can now include links to external sites ([#989](https://github.com/mkdocs/mkdocs/issues/989 "GitHub Issue mkdocs/mkdocs #989") [#1373](https://github.com/mkdocs/mkdocs/issues/1373 "GitHub Issue mkdocs/mkdocs #1373") & [#1406](https://github.com/mkdocs/mkdocs/issues/1406 "GitHub Issue mkdocs/mkdocs #1406")).
-   Page data (including titles) is properly determined for all pages before any page is rendered ([#1347](https://github.com/mkdocs/mkdocs/issues/1347 "GitHub Issue mkdocs/mkdocs #1347")).
-   Automatically populated navigation now sorts index pages to the top. In other words, The index page will be listed as the first child of a directory, while all other documents are sorted alphanumerically by file name after the index page ([#73](https://github.com/mkdocs/mkdocs/issues/73 "GitHub Issue mkdocs/mkdocs #73") & [#1042](https://github.com/mkdocs/mkdocs/issues/1042 "GitHub Issue mkdocs/mkdocs #1042")).
-   A `README.md` file is now treated as an index file within a directory and will be rendered to `index.html` ([#608](https://github.com/mkdocs/mkdocs/issues/608 "GitHub Issue mkdocs/mkdocs #608")).
-   The URLs for all files are computed once and stored in a files collection. This ensures all internal links are always computed correctly regardless of the configuration. This also allows all internal links to be validated, not just links to other Markdown pages. ([#842](https://github.com/mkdocs/mkdocs/issues/842 "GitHub Issue mkdocs/mkdocs #842") & [#872](https://github.com/mkdocs/mkdocs/issues/872 "GitHub Issue mkdocs/mkdocs #872")).
-   A new [url](../../dev-guide/themes/#url) template filter smartly ensures all URLs are relative to the current page ([#1526](https://github.com/mkdocs/mkdocs/issues/1526 "GitHub Issue mkdocs/mkdocs #1526")).
-   An [on_files](../../dev-guide/plugins/#on_files) plugin event has been added, which could be used to include files not in the `docs_dir`, exclude files, redefine page URLs (i.e. implement extensionless URLs), or to manipulate files in various other ways.

##### Backward Incompatible Changes[](#backward-incompatible-changes "Permanent link")

As part of the internal refactor, a number of backward incompatible changes have been introduced, which are summarized below.

###### URLs have changed when `use_directory_urls` is `False`[](#urls-have-changed-when-use_directory_urls-is-false "Permanent link")

Previously, all Markdown pages would be have their filenames altered to be index pages regardless of how the [use_directory_urls](../../user-guide/configuration/#use_directory_urls) setting was configured. However, the path munging is only needed when `use_directory_urls` is set to `True` (the default). The path mangling no longer happens when `use_directory_urls` is set to `False`, which will result in different URLs for all pages that were not already index files. As this behavior only effects a non-default configuration, and the most common user-case for setting the option to `False` is for local file system (`file://`) browsing, its not likely to effect most users. However, if you have `use_directory_urls` set to `False` for a MkDocs site hosted on a web server, most of your URLs will now be broken. As you can see below, the new URLs are much more sensible.

  Markdown file   Old URL                New URL
  --------------- ---------------------- ----------------
  `index.md`      `index.html`           `index.html`
  `foo.md`        `foo/index.html`       `foo.html`
  `foo/bar.md`    `foo/bar/index.html`   `foo/bar.html`

Note that there has been no change to URLs or file paths when `use_directory_urls` is set to `True` (the default), except that MkDocs more consistently includes an ending slash on all internally generated URLs.

###### The `pages` configuration setting has been renamed to `nav`[](#the-pages-configuration-setting-has-been-renamed-to-nav "Permanent link")

The `pages` configuration setting is deprecated and will issue a warning if set in the configuration file. The setting has been renamed `nav`. To update your configuration, simply rename the setting to `nav`. In other words, if your configuration looked like this:

``` highlight
pages:
  - Home: index.md
  - User Guide: user-guide.md
```

Simply edit the configuration as follows:

``` highlight
nav:
  - Home: index.md
  - User Guide: user-guide.md
```

In the current release, any configuration which includes a `pages` setting, but no `nav` setting, the `pages` configuration will be copied to `nav` and a warning will be issued. However, in a future release, that may no longer happen. If both `pages` and `nav` are defined, the `pages` setting will be ignored.

###### Template variables and `base_url`[](#template-variables-and-base_url "Permanent link")

In previous versions of MkDocs some URLs expected the [base_url](../../dev-guide/themes/#base_url) template variable to be prepended to the URL and others did not. That inconsistency has been removed in that no URLs are modified before being added to the template context.

For example, a theme template might have previously included a link to the `site_name` as:

``` highlight
<a href="}">}</a>
```

And MkDocs would magically return a URL for the homepage which was relative to the current page. That \"magic\" has been removed and the [url](../../dev-guide/themes/#url) template filter should be used:

``` highlight
<a href="}">}</a>
```

This change applies to any navigation items and pages, as well as the `page.next_page` and `page.previous_page` attributes. For the time being, the `extra_javascript` and `extra_css` variables continue to work as previously (without the `url` template filter), but they have been deprecated and the corresponding configuration values (`config.extra_javascript` and `config.extra_css` respectively) should be used with the filter instead.

``` highlight

    <link href="}" rel="stylesheet">

```

Note that navigation can now include links to external sites. Obviously, the `base_url` should not be prepended to these items. However, the `url` template filter is smart enough to recognize the URL is absolute and does not alter it. Therefore, all navigation items can be passed to the filter and only those that need to will be altered.

``` highlight

    <a href="}">}</a>

```

#### Path Based Settings are Relative to Configuration File ([#543](https://github.com/mkdocs/mkdocs/issues/543 "GitHub Issue mkdocs/mkdocs #543"))[](#path-based-settings-are-relative-to-configuration-file-543 "Permanent link")

Previously any relative paths in the various configuration options were resolved relative to the current working directory. They are now resolved relative to the configuration file. As the documentation has always encouraged running the various MkDocs commands from the directory that contains the configuration file (project root), this change will not affect most users. However, it will make it much easier to implement automated builds or otherwise run commands from a location other than the project root.

Simply use the `-f/--config-file` option and point it at the configuration file:

``` highlight
mkdocs build --config-file /path/to/my/config/file.yml
```

As previously, if no file is specified, MkDocs looks for a file named `mkdocs.yml` in the current working directory.

#### Added support for YAML Meta-Data ([#1542](https://github.com/mkdocs/mkdocs/issues/1542 "GitHub Issue mkdocs/mkdocs #1542"))[](#added-support-for-yaml-meta-data-1542 "Permanent link")

Previously, MkDocs only supported MultiMarkdown style meta-data, which does not recognize different data types and is rather limited. MkDocs now also supports YAML style meta-data in Markdown documents. MkDocs relies on the the presence or absence of the deliminators (`---` or `...`) to determine whether YAML style meta-data or MultiMarkdown style meta-data is being used.

Previously MkDocs would recognize MultiMarkdown style meta-data between the deliminators. Now, if the deliminators are detected, but the content between the deliminators is not valid YAML meta-data, MkDocs does not attempt to parse the content as MultiMarkdown style meta-data. Therefore, MultiMarkdown\'s style meta-data must not include the deliminators. See the [MultiMarkdown style meta-data documentation](../../user-guide/writing-your-docs/#multimarkdown-style-meta-data) for details.

Prior to version 0.17, MkDocs returned all meta-data values as a list of strings (even a single line would return a list of one string). In version 0.17, that behavior was changed to return each value as a single string (multiple lines were joined), which some users found limiting (see [#1471](https://github.com/mkdocs/mkdocs/issues/1471 "GitHub Issue mkdocs/mkdocs #1471")). That behavior continues for MultiMarkdown style meta-data in the current version. However, YAML style meta-data supports the full range of \"safe\" YAML data types. Therefore, it is recommended that any complex meta-data make use of the YAML style (see the [YAML style meta-data documentation](../../user-guide/writing-your-docs/#yaml-style-meta-data) for details). In fact, a future version of MkDocs may deprecate support for MultiMarkdown style meta-data.

#### Refactor Search Plugin[](#refactor-search-plugin "Permanent link")

The search plugin has been completely refactored to include support for the following features:

-   Use a web worker in the browser with a fallback ([#1396](https://github.com/mkdocs/mkdocs/issues/1396 "GitHub Issue mkdocs/mkdocs #1396")).
-   Optionally pre-build search index locally ([#859](https://github.com/mkdocs/mkdocs/issues/859 "GitHub Issue mkdocs/mkdocs #859") & [#1061](https://github.com/mkdocs/mkdocs/issues/1061 "GitHub Issue mkdocs/mkdocs #1061")).
-   Upgrade to lunr.js 2.x ([#1319](https://github.com/mkdocs/mkdocs/issues/1319 "GitHub Issue mkdocs/mkdocs #1319")).
-   Support search in languages other than English ([#826](https://github.com/mkdocs/mkdocs/issues/826 "GitHub Issue mkdocs/mkdocs #826")).
-   Allow the user to define the word separators ([#867](https://github.com/mkdocs/mkdocs/issues/867 "GitHub Issue mkdocs/mkdocs #867")).
-   Only run searches for queries of length \> 2 ([#1127](https://github.com/mkdocs/mkdocs/issues/1127 "GitHub Issue mkdocs/mkdocs #1127")).
-   Remove dependency on require.js ([#1218](https://github.com/mkdocs/mkdocs/issues/1218 "GitHub Issue mkdocs/mkdocs #1218")).
-   Compress the search index ([#1128](https://github.com/mkdocs/mkdocs/issues/1128 "GitHub Issue mkdocs/mkdocs #1128")).

Users can review the [configuration options](../../user-guide/configuration/#search) available and theme authors should review how [search and themes](../../dev-guide/themes/#search-and-themes) interact.

#### `theme_dir` Configuration Option fully Deprecated[](#theme_dir-configuration-option-fully-deprecated "Permanent link")

As of version 0.17, the [custom_dir](../../user-guide/configuration/#custom_dir) option replaced the deprecated `theme_dir` option. If users had set the `theme_dir` option, MkDocs version 0.17 copied the value to the `theme.custom_dir` option and a warning was issued. As of version 1.0, the value is no longer copied and an error is raised.

### Other Changes and Additions to Version 1.0[](#other-changes-and-additions-to-version-10 "Permanent link") 

-   Keyboard shortcuts changed to not conflict with commonly used accessibility shortcuts ([#1502](https://github.com/mkdocs/mkdocs/issues/1502 "GitHub Issue mkdocs/mkdocs #1502").)
-   User friendly YAML parse errors ([#1543](https://github.com/mkdocs/mkdocs/issues/1543 "GitHub Issue mkdocs/mkdocs #1543")).
-   Officially support Python 3.7.
-   A missing theme configuration file now raises an error.
-   Empty `extra_css` and `extra_javascript` settings no longer raise a warning.
-   Add highlight.js configuration settings to built-in themes ([#1284](https://github.com/mkdocs/mkdocs/issues/1284 "GitHub Issue mkdocs/mkdocs #1284")).
-   Close search modal when result is selected ([#1527](https://github.com/mkdocs/mkdocs/issues/1527 "GitHub Issue mkdocs/mkdocs #1527")).
-   Add a level attribute to AnchorLinks ([#1272](https://github.com/mkdocs/mkdocs/issues/1272 "GitHub Issue mkdocs/mkdocs #1272")).
-   Add MkDocs version check to gh-deploy script ([#640](https://github.com/mkdocs/mkdocs/issues/640 "GitHub Issue mkdocs/mkdocs #640")).
-   Improve Markdown extension error messages. ([#782](https://github.com/mkdocs/mkdocs/issues/782 "GitHub Issue mkdocs/mkdocs #782")).
-   Drop official support for Python 3.3 and set `tornado>=5.0` ([#1427](https://github.com/mkdocs/mkdocs/issues/1427 "GitHub Issue mkdocs/mkdocs #1427")).
-   Add support for GitLab edit links ([#1435](https://github.com/mkdocs/mkdocs/issues/1435 "GitHub Issue mkdocs/mkdocs #1435")).
-   Link to GitHub issues from release notes ([#644](https://github.com/mkdocs/mkdocs/issues/644 "GitHub Issue mkdocs/mkdocs #644")).
-   Expand  and  in gh-deploy commit message ([#1410](https://github.com/mkdocs/mkdocs/issues/1410 "GitHub Issue mkdocs/mkdocs #1410")).
-   Compress `sitemap.xml` ([#1130](https://github.com/mkdocs/mkdocs/issues/1130 "GitHub Issue mkdocs/mkdocs #1130")).
-   Defer loading JS scripts ([#1380](https://github.com/mkdocs/mkdocs/issues/1380 "GitHub Issue mkdocs/mkdocs #1380")).
-   Add a title attribute to the search input ([#1379](https://github.com/mkdocs/mkdocs/issues/1379 "GitHub Issue mkdocs/mkdocs #1379")).
-   Update RespondJS to latest version ([#1398](https://github.com/mkdocs/mkdocs/issues/1398 "GitHub Issue mkdocs/mkdocs #1398")).
-   Always load Google Analytics over HTTPS ([#1397](https://github.com/mkdocs/mkdocs/issues/1397 "GitHub Issue mkdocs/mkdocs #1397")).
-   Improve scrolling frame rate ([#1394](https://github.com/mkdocs/mkdocs/issues/1394 "GitHub Issue mkdocs/mkdocs #1394")).
-   Provide more version info. ([#1393](https://github.com/mkdocs/mkdocs/issues/1393 "GitHub Issue mkdocs/mkdocs #1393")).
-   Refactor `writing-your-docs.md` ([#1392](https://github.com/mkdocs/mkdocs/issues/1392 "GitHub Issue mkdocs/mkdocs #1392")).
-   Workaround Safari bug when zooming to \< 100% ([#1389](https://github.com/mkdocs/mkdocs/issues/1389 "GitHub Issue mkdocs/mkdocs #1389")).
-   Remove addition of `clicky` class to body and animations. ([#1387](https://github.com/mkdocs/mkdocs/issues/1387 "GitHub Issue mkdocs/mkdocs #1387")).
-   Prevent search plugin from re-injecting `extra_javascript` files ([#1388](https://github.com/mkdocs/mkdocs/issues/1388 "GitHub Issue mkdocs/mkdocs #1388")).
-   Refactor `copy_media_files` util function for more flexibility ([#1370](https://github.com/mkdocs/mkdocs/issues/1370 "GitHub Issue mkdocs/mkdocs #1370")).
-   Remove PyPI Deployment Docs ([#1360](https://github.com/mkdocs/mkdocs/issues/1360 "GitHub Issue mkdocs/mkdocs #1360")).
-   Update links to Python-Markdown library ([#1360](https://github.com/mkdocs/mkdocs/issues/1360 "GitHub Issue mkdocs/mkdocs #1360")).
-   Document how to generate manpages for MkDocs commands ([#686](https://github.com/mkdocs/mkdocs/issues/686 "GitHub Issue mkdocs/mkdocs #686")).

## Version 0.17.5 (2018-07-06)[](#version-0175-2018-07-06 "Permanent link") 

-   Bugfix: Fix Python 3.7 and PEP 479 incompatibility ([#1518](https://github.com/mkdocs/mkdocs/issues/1518 "GitHub Issue mkdocs/mkdocs #1518")).

## Version 0.17.4 (2018-06-08)[](#version-0174-2018-06-08 "Permanent link") 

-   Bugfix: Add multi-level nesting support to sitemap.xml ([#1482](https://github.com/mkdocs/mkdocs/issues/1482 "GitHub Issue mkdocs/mkdocs #1482")).

## Version 0.17.3 (2018-03-07)[](#version-0173-2018-03-07 "Permanent link") 

-   Bugfix: Set dependency `tornado>=4.1,<5.0` due to changes in 5.0 ([#1428](https://github.com/mkdocs/mkdocs/issues/1428 "GitHub Issue mkdocs/mkdocs #1428")).

## Version 0.17.2 (2017-11-15)[](#version-0172-2017-11-15 "Permanent link") 

-   Bugfix: Correct `extra_*` config setting regressions ([#1335](https://github.com/mkdocs/mkdocs/issues/1335 "GitHub Issue mkdocs/mkdocs #1335") & [#1336](https://github.com/mkdocs/mkdocs/issues/1336 "GitHub Issue mkdocs/mkdocs #1336")).

## Version 0.17.1 (2017-10-30)[](#version-0171-2017-10-30 "Permanent link") 

-   Bugfix: Support `repo_url` with missing ending slash. ([#1321](https://github.com/mkdocs/mkdocs/issues/1321 "GitHub Issue mkdocs/mkdocs #1321")).
-   Bugfix: Add length support to `mkdocs.toc.TableOfContext` ([#1325](https://github.com/mkdocs/mkdocs/issues/1325 "GitHub Issue mkdocs/mkdocs #1325")).
-   Bugfix: Add some theme specific settings to the search plugin for third party themes ([#1316](https://github.com/mkdocs/mkdocs/issues/1316 "GitHub Issue mkdocs/mkdocs #1316")).
-   Bugfix: Override `site_url` with `dev_addr` on local server ([#1317](https://github.com/mkdocs/mkdocs/issues/1317 "GitHub Issue mkdocs/mkdocs #1317")).

## Version 0.17.0 (2017-10-19)[](#version-0170-2017-10-19 "Permanent link") 

### Major Additions to Version 0.17.0[](#major-additions-to-version-0170 "Permanent link") 

#### Plugin API. ([#206](https://github.com/mkdocs/mkdocs/issues/206 "GitHub Issue mkdocs/mkdocs #206"))[](#plugin-api-206 "Permanent link") 

A new [Plugin API](../../dev-guide/plugins/) has been added to MkDocs which allows users to define their own custom behaviors. See the included documentation for a full explanation of the API.

The previously built-in search functionality has been removed and wrapped in a plugin (named \"search\") with no changes in behavior. When MkDocs builds, the search index is now written to `search/search_index.json` instead of `mkdocs/search_index.json`. If no plugins setting is defined in the config, then the `search` plugin will be included by default. See the [configuration](../../user-guide/configuration/#plugins) documentation for information on overriding the default.

#### Theme Customization. ([#1164](https://github.com/mkdocs/mkdocs/issues/1164 "GitHub Issue mkdocs/mkdocs #1164"))[](#theme-customization-1164 "Permanent link") 

Support had been added to provide theme specific customizations. Theme authors can define default options as documented in [Theme Configuration](../../dev-guide/themes/#theme-configuration). A theme can now inherit from another theme, define various static templates to be rendered, and define arbitrary default variables to control behavior in the templates. The theme configuration is defined in a configuration file named `mkdocs_theme.yml` which should be placed at the root of your template files. A warning will be raised if no configuration file is found and an error will be raised in a future release.

Users can override those defaults under the [theme](../../user-guide/configuration/#theme) configuration option of their `mkdocs.yml` configuration file, which now accepts nested options. One such nested option is the [custom_dir](../../user-guide/configuration/#custom_dir) option, which replaces the now deprecated `theme_dir` option. If users had previously set the `theme_dir` option, a warning will be issued, with an error expected in a future release.

If a configuration previously defined a `theme_dir` like this:

``` highlight
theme: mkdocs
theme_dir: custom
```

Then the configuration should be adjusted as follows:

``` highlight
theme:
  name: mkdocs
  custom_dir: custom
```

See the [theme](../../user-guide/configuration/#theme) configuration option documentation for details.

#### Previously deprecated Template variables removed. ([#1168](https://github.com/mkdocs/mkdocs/issues/1168 "GitHub Issue mkdocs/mkdocs #1168"))[](#previously-deprecated-template-variables-removed-1168 "Permanent link") 

##### Page Template[](#page-template "Permanent link")

The primary entry point for page templates has been changed from `base.html` to `main.html`. This allows `base.html` to continue to exist while allowing users to override `main.html` and extend `base.html`. For version 0.16, `base.html` continued to work if no `main.html` template existed, but it raised a deprecation warning. In version 1.0, a build will fail if no `main.html` template exists.

##### Context Variables[](#context-variables "Permanent link")

Page specific variable names in the template context have been refactored as defined in [Custom Themes](../../dev-guide/themes/#page). The old variable names issued a warning in version 0.16, but have been removed in version 1.0.

Any of the following old page variables should be updated to the new ones in user created and third-party templates:

  Old Variable Name   New Variable Name
  ------------------- --------------------------------------
  current_page        [page](../../dev-guide/themes/#page)
  page_title          page.title
  content             page.content
  toc                 page.toc
  meta                page.meta
  canonical_url       page.canonical_url
  previous_page       page.previous_page
  next_page           page.next_page

Additionally, a number of global variables have been altered and/or removed and user created and third-party templates should be updated as outlined below:

  Old Variable Name   New Variable Name or Expression
  ------------------- ----------------------------------------
  current_page        page
  include_nav         nav\|length\>1
  include_next_prev   (page.next_page or page.previous_page)
  site_name           config.site_name
  site_author         config.site_author
  page_description    config.site_description
  repo_url            config.repo_url
  repo_name           config.repo_name
  site_url            config.site_url
  copyright           config.copyright
  google_analytics    config.google_analytics
  homepage_url        nav.homepage.url
  favicon             }/img/favicon.ico

#### Auto-Populated extra_css and extra_javascript Fully Deprecated. ([#986](https://github.com/mkdocs/mkdocs/issues/986 "GitHub Issue mkdocs/mkdocs #986"))[](#auto-populated-extra_css-and-extra_javascript-fully-deprecated-986 "Permanent link") 

In previous versions of MkDocs, if the `extra_css` or `extra_javascript` config settings were empty, MkDocs would scan the `docs_dir` and auto-populate each setting with all of the CSS and JavaScript files found. On version 0.16 this behavior was deprecated and a warning was issued. In 0.17 any unlisted CSS and JavaScript files will not be included in the HTML templates, however, a warning will be issued. In other words, they will still be copied to the `site-dir`, but they will not have any effect on the theme if they are not explicitly listed.

All CSS and JavaScript files in the `docs_dir` should be explicitly listed in the `extra_css` or `extra_javascript` config settings going forward.

### Other Changes and Additions to Version 0.17.0[](#other-changes-and-additions-to-version-0170 "Permanent link") 

-   Add \"edit Link\" support to MkDocs theme ([#1129](https://github.com/mkdocs/mkdocs/issues/1129 "GitHub Issue mkdocs/mkdocs #1129"))
-   Open files with `utf-8-sig` to account for BOM ([#1186](https://github.com/mkdocs/mkdocs/issues/1186 "GitHub Issue mkdocs/mkdocs #1186"))
-   Symbolic links are now followed consistently ([#1134](https://github.com/mkdocs/mkdocs/issues/1134 "GitHub Issue mkdocs/mkdocs #1134"))
-   Support for keyboard navigation shortcuts added to included themes ([#1095](https://github.com/mkdocs/mkdocs/issues/1095 "GitHub Issue mkdocs/mkdocs #1095"))
-   Some refactoring and improvements to config_options ([#1296](https://github.com/mkdocs/mkdocs/issues/1296 "GitHub Issue mkdocs/mkdocs #1296"))
-   Officially added support for Python 3.6 ([#1296](https://github.com/mkdocs/mkdocs/issues/1296 "GitHub Issue mkdocs/mkdocs #1296"))
-   404 Error page added to readthedocs theme ([#1296](https://github.com/mkdocs/mkdocs/issues/1296 "GitHub Issue mkdocs/mkdocs #1296")))
-   Internal refactor of Markdown processing ([#713](https://github.com/mkdocs/mkdocs/issues/713 "GitHub Issue mkdocs/mkdocs #713"))
-   Removed special error message for mkdocs-bootstrap and mkdocs-bootswatch themes ([#1168](https://github.com/mkdocs/mkdocs/issues/1168 "GitHub Issue mkdocs/mkdocs #1168"))
-   The legacy pages config is no longer supported ([#1168](https://github.com/mkdocs/mkdocs/issues/1168 "GitHub Issue mkdocs/mkdocs #1168"))
-   The deprecated `json` command has been removed ([#481](https://github.com/mkdocs/mkdocs/issues/481 "GitHub Issue mkdocs/mkdocs #481"))
-   Support for Python 2.6 has been dropped ([#165](https://github.com/mkdocs/mkdocs/issues/165 "GitHub Issue mkdocs/mkdocs #165"))
-   File permissions are no longer copied during build ([#1292](https://github.com/mkdocs/mkdocs/issues/1292 "GitHub Issue mkdocs/mkdocs #1292"))
-   Support query and fragment strings in `edit_uri` ([#1224](https://github.com/mkdocs/mkdocs/issues/1224 "GitHub Issue mkdocs/mkdocs #1224") & [#1273](https://github.com/mkdocs/mkdocs/issues/1273 "GitHub Issue mkdocs/mkdocs #1273"))

## Version 0.16.3 (2017-04-04)[](#version-0163-2017-04-04 "Permanent link") 

-   Fix error raised by autoscrolling in the readthedocs theme ([#1177](https://github.com/mkdocs/mkdocs/issues/1177 "GitHub Issue mkdocs/mkdocs #1177"))
-   Fix a few documentation typos ([#1181](https://github.com/mkdocs/mkdocs/issues/1181 "GitHub Issue mkdocs/mkdocs #1181") & [#1185](https://github.com/mkdocs/mkdocs/issues/1185 "GitHub Issue mkdocs/mkdocs #1185"))
-   Fix a regression to livereload server introduced in 0.16.2 ([#1174](https://github.com/mkdocs/mkdocs/issues/1174 "GitHub Issue mkdocs/mkdocs #1174"))

## Version 0.16.2 (2017-03-13)[](#version-0162-2017-03-13 "Permanent link") 

-   System root (`/`) is not a valid path for site_dir or docs_dir ([#1161](https://github.com/mkdocs/mkdocs/issues/1161 "GitHub Issue mkdocs/mkdocs #1161"))
-   Refactor readthedocs theme navigation ([#1155](https://github.com/mkdocs/mkdocs/issues/1155 "GitHub Issue mkdocs/mkdocs #1155") & [#1156](https://github.com/mkdocs/mkdocs/issues/1156 "GitHub Issue mkdocs/mkdocs #1156"))
-   Add support to dev server to serve custom error pages ([#1040](https://github.com/mkdocs/mkdocs/issues/1040 "GitHub Issue mkdocs/mkdocs #1040"))
-   Ensure nav.homepage.url is not blank on error pages ([#1131](https://github.com/mkdocs/mkdocs/issues/1131 "GitHub Issue mkdocs/mkdocs #1131"))
-   Increase livereload dependency to 2.5.1 ([#1106](https://github.com/mkdocs/mkdocs/issues/1106 "GitHub Issue mkdocs/mkdocs #1106"))

## Version 0.16.1 (2016-12-22)[](#version-0161-2016-12-22 "Permanent link") 

-   Ensure scrollspy behavior does not affect nav bar ([#1094](https://github.com/mkdocs/mkdocs/issues/1094 "GitHub Issue mkdocs/mkdocs #1094"))
-   Only \"load\" a theme when it is explicitly requested by the user ([#1105](https://github.com/mkdocs/mkdocs/issues/1105 "GitHub Issue mkdocs/mkdocs #1105"))

## Version 0.16 (2016-11-04)[](#version-016-2016-11-04 "Permanent link") 

### Major Additions to Version 0.16.0[](#major-additions-to-version-0160 "Permanent link") 

#### Template variables refactored. ([#874](https://github.com/mkdocs/mkdocs/issues/874 "GitHub Issue mkdocs/mkdocs #874"))[](#template-variables-refactored-874 "Permanent link") 

##### Page Context[](#page-context "Permanent link")

Page specific variable names in the template context have been refactored as defined in [Custom Themes](../../dev-guide/themes/#page). The old variable names will issue a warning but continue to work for version 0.16, but may be removed in a future version.

Any of the following old page variables should be updated to the new ones in user created and third-party templates:

  Old Variable Name   New Variable Name
  ------------------- --------------------------------------
  current_page        [page](../../dev-guide/themes/#page)
  page_title          page.title
  content             page.content
  toc                 page.toc
  meta                page.meta
  canonical_url       page.canonical_url
  previous_page       page.previous_page
  next_page           page.next_page

##### Global Context[](#global-context "Permanent link")

Additionally, a number of global variables have been altered and/or deprecated and user created and third-party templates should be updated as outlined below:

Previously, the global variable `include_nav` was altered programmatically based on the number of pages in the nav. The variable will issue a warning but continue to work for version 0.16, but may be removed in a future version. Use `` instead.

Previously, the global variable `include_next_prev` was altered programmatically based on the number of pages in the nav. The variable will issue a warning but continue to work for version 0.16, but may be removed in a future version. Use `` instead.

Previously the global variable `page_description` was altered programmatically based on whether the current page was the homepage. Now it simply maps to `config['site_description']`. Use `` in the template to conditionally change the description.

The global variable `homepage_url` maps directly to `nav.homepage.url` and is being deprecated. The variable will issue a warning but continue to work for version 0.16, but may be removed in a future version. Use `nav.homepage.url` instead.

The global variable `favicon` maps to the configuration setting `site_favicon`. Both the template variable and the configuration setting are being deprecated and will issue a warning but continue to work for version 0.16, and may be removed in a future version. Use `}/img/favicon.ico` in your template instead. Users can simply save a copy of their custom favicon icon to `img/favicon.ico` in either their `docs_dir` or `theme_dir`.

A number of variables map directly to similarly named variables in the `config`. Those variables are being deprecated and will issue a warning but continue to work for version 0.16, but may be removed in a future version. Use `config.var_name` instead, where `var_name` is the name of one of the [configuration](../../user-guide/configuration/) variables.

Below is a summary of all of the changes made to the global context:

  Old Variable Name   New Variable Name or Expression
  ------------------- ----------------------------------------
  current_page        page
  include_nav         nav\|length\>1
  include_next_prev   (page.next_page or page.previous_page)
  site_name           config.site_name
  site_author         config.site_author
  page_description    config.site_description
  repo_url            config.repo_url
  repo_name           config.repo_name
  site_url            config.site_url
  copyright           config.copyright
  google_analytics    config.google_analytics
  homepage_url        nav.homepage.url
  favicon             }/img/favicon.ico

#### Increased Template Customization. ([#607](https://github.com/mkdocs/mkdocs/issues/607 "GitHub Issue mkdocs/mkdocs #607"))[](#increased-template-customization-607 "Permanent link") 

The built-in themes have been updated by having each of their many parts wrapped in template blocks which allow each individual block to be easily overridden using the `theme_dir` config setting. Without any new settings, you can use a different analytics service, replace the default search function, or alter the behavior of the navigation, among other things. See the relevant [documentation](../../user-guide/customizing-your-theme/#overriding-template-blocks) for more details.

To enable this feature, the primary entry point for page templates has been changed from `base.html` to `main.html`. This allows `base.html` to continue to exist while allowing users to override `main.html` and extend `base.html`. For version 0.16, `base.html` will continue to work if no `main.html` template exists, but it is deprecated and will raise a warning. In version 1.0, a build will fail if no `main.html` template exists. Any custom and third party templates should be updated accordingly.

The easiest way for a third party theme to be updated would be to simply add a `main.html` file which only contains the following line:

``` highlight

```

That way, the theme contains the `main.html` entry point, and also supports overriding blocks in the same manner as the built-in themes. Third party themes are encouraged to wrap the various pieces of their templates in blocks in order to support such customization.

#### Auto-Populated `extra_css` and `extra_javascript` Deprecated. ([#986](https://github.com/mkdocs/mkdocs/issues/986 "GitHub Issue mkdocs/mkdocs #986"))[](#auto-populated-extra_css-and-extra_javascript-deprecated-986 "Permanent link") 

In previous versions of MkDocs, if the `extra_css` or `extra_javascript` config settings were empty, MkDocs would scan the `docs_dir` and auto-populate each setting with all of the CSS and JavaScript files found. This behavior is deprecated and a warning will be issued. In the next release, the auto-populate feature will stop working and any unlisted CSS and JavaScript files will not be included in the HTML templates. In other words, they will still be copied to the `site-dir`, but they will not have any effect on the theme if they are not explicitly listed.

All CSS and JavaScript files in the `docs_dir` should be explicitly listed in the `extra_css` or `extra_javascript` config settings going forward.

#### Support for dirty builds. ([#990](https://github.com/mkdocs/mkdocs/issues/990 "GitHub Issue mkdocs/mkdocs #990"))[](#support-for-dirty-builds-990 "Permanent link") 

For large sites the build time required to create the pages can become problematic, thus a \"dirty\" build mode was created. This mode simply compares the modified time of the generated HTML and source markdown. If the markdown has changed since the HTML then the page is re-constructed. Otherwise, the page remains as is. This mode may be invoked in both the `mkdocs serve` and `mkdocs build` commands:

``` highlight
mkdocs serve --dirtyreload
```

``` highlight
mkdocs build --dirty
```

It is important to note that this method for building the pages is for development of content only, since the navigation and other links do not get updated on other pages.

#### Stricter Directory Validation[](#stricter-directory-validation "Permanent link")

Previously, a warning was issued if the `site_dir` was a child directory of the `docs_dir`. This now raises an error. Additionally, an error is now raised if the `docs_dir` is set to the directory which contains your config file rather than a child directory. You will need to rearrange you directory structure to better conform with the documented [layout](../../user-guide/writing-your-docs/#file-layout).

### Other Changes and Additions to Version 0.16.0[](#other-changes-and-additions-to-version-0160 "Permanent link") 

-   Bugfix: Support `gh-deploy` command on Windows with Python 3 ([#722](https://github.com/mkdocs/mkdocs/issues/722 "GitHub Issue mkdocs/mkdocs #722"))
-   Bugfix: Include .woff2 font files in Python package build ([#894](https://github.com/mkdocs/mkdocs/issues/894 "GitHub Issue mkdocs/mkdocs #894"))
-   Various updates and improvements to Documentation Home Page/Tutorial ([#870](https://github.com/mkdocs/mkdocs/issues/870 "GitHub Issue mkdocs/mkdocs #870"))
-   Bugfix: Support livereload for config file changes ([#735](https://github.com/mkdocs/mkdocs/issues/735 "GitHub Issue mkdocs/mkdocs #735"))
-   Bugfix: Non-media template files are no longer copied with media files ([#807](https://github.com/mkdocs/mkdocs/issues/807 "GitHub Issue mkdocs/mkdocs #807"))
-   Add a flag (-e/\--theme-dir) to specify theme directory with the commands `mkdocs build` and `mkdocs serve` ([#832](https://github.com/mkdocs/mkdocs/issues/832 "GitHub Issue mkdocs/mkdocs #832"))
-   Fixed issues with Unicode file names under Windows and Python 2. ([#833](https://github.com/mkdocs/mkdocs/issues/833 "GitHub Issue mkdocs/mkdocs #833"))
-   Improved the styling of in-line code in the MkDocs theme. ([#718](https://github.com/mkdocs/mkdocs/issues/718 "GitHub Issue mkdocs/mkdocs #718"))
-   Bugfix: convert variables to JSON when being passed to JavaScript ([#850](https://github.com/mkdocs/mkdocs/issues/850 "GitHub Issue mkdocs/mkdocs #850"))
-   Updated the ReadTheDocs theme to match the upstream font sizes and colors more closely. ([#857](https://github.com/mkdocs/mkdocs/issues/857 "GitHub Issue mkdocs/mkdocs #857"))
-   Fixes an issue with permalink markers showing when the mouse was far above them ([#843](https://github.com/mkdocs/mkdocs/issues/843 "GitHub Issue mkdocs/mkdocs #843"))
-   Bugfix: Handle periods in directory name when automatically creating the pages config. ([#728](https://github.com/mkdocs/mkdocs/issues/728 "GitHub Issue mkdocs/mkdocs #728"))
-   Update searching to Lunr 0.7, which comes with some performance enhancements for larger documents ([#859](https://github.com/mkdocs/mkdocs/issues/859 "GitHub Issue mkdocs/mkdocs #859"))
-   Bugfix: Support SOURCE_DATE_EPOCH environment variable for \"reproducible\" builds ([#938](https://github.com/mkdocs/mkdocs/issues/938 "GitHub Issue mkdocs/mkdocs #938"))
-   Follow links when copying media files ([#869](https://github.com/mkdocs/mkdocs/issues/869 "GitHub Issue mkdocs/mkdocs #869")).
-   Change \"Edit on\...\" links to point directly to the file in the source repository, rather than to the root of the repository ([#975](https://github.com/mkdocs/mkdocs/issues/975 "GitHub Issue mkdocs/mkdocs #975")), configurable via the new [`edit_uri`](../../user-guide/configuration/#edit_uri) setting.
-   Bugfix: Don\'t override config value for strict mode if not specified on CLI ([#738](https://github.com/mkdocs/mkdocs/issues/738 "GitHub Issue mkdocs/mkdocs #738")).
-   Add a `--force` flag to the `gh-deploy` command to force the push to the repository ([#973](https://github.com/mkdocs/mkdocs/issues/973 "GitHub Issue mkdocs/mkdocs #973")).
-   Improve alignment for current selected menu item in readthedocs theme ([#888](https://github.com/mkdocs/mkdocs/issues/888 "GitHub Issue mkdocs/mkdocs #888")).
-   `http://user.github.io/repo` =\> `https://user.github.io/repo/` ([#1029](https://github.com/mkdocs/mkdocs/issues/1029 "GitHub Issue mkdocs/mkdocs #1029")).
-   Improve installation instructions ([#1028](https://github.com/mkdocs/mkdocs/issues/1028 "GitHub Issue mkdocs/mkdocs #1028")).
-   Account for wide tables and consistently wrap inline code spans ([#834](https://github.com/mkdocs/mkdocs/issues/834 "GitHub Issue mkdocs/mkdocs #834")).
-   Bugfix: Use absolute URLs in nav & media links from error templates ([#77](https://github.com/mkdocs/mkdocs/issues/77 "GitHub Issue mkdocs/mkdocs #77")).

## Version 0.15.3 (2016-02-18)[](#version-0153-2016-02-18 "Permanent link") 

-   Improve the error message the given theme can\'t be found.
-   Fix an issue with relative symlinks ([#639](https://github.com/mkdocs/mkdocs/issues/639 "GitHub Issue mkdocs/mkdocs #639"))

## Version 0.15.2 (2016-02-08)[](#version-0152-2016-02-08 "Permanent link") 

-   Fix an incorrect warning that states external themes [will be removed from MkDocs](#add-support-for-installable-themes).

## Version 0.15.1 (2016-01-30)[](#version-0151-2016-01-30 "Permanent link") 

-   Lower the minimum supported Click version to 3.3 for package maintainers. ([#763](https://github.com/mkdocs/mkdocs/issues/763 "GitHub Issue mkdocs/mkdocs #763"))

## Version 0.15.0 (2016-01-21)[](#version-0150-2016-01-21 "Permanent link") 

### Major Additions to Version 0.15.0[](#major-additions-to-version-0150 "Permanent link") 

#### Add support for installable themes[](#add-support-for-installable-themes "Permanent link")

MkDocs now supports themes that are distributed via Python packages. With this addition, the Bootstrap and Bootswatch themes have been moved to external git repositories and python packages. See their individual documentation for more details about these specific themes.

-   [MkDocs Bootstrap](https://mkdocs.github.io/mkdocs-bootstrap/)
-   [MkDocs Bootswatch](https://mkdocs.github.io/mkdocs-bootswatch/)

They will be included with MkDocs by default until a future release. After that they will be installable with pip: `pip install mkdocs-bootstrap` and `pip install mkdocs-bootswatch`

See the documentation for [Customizing Your Theme](../../user-guide/customizing-your-theme/) for more information about using and customizing themes and [Custom themes](../../dev-guide/themes/) for creating and distributing new themes

### Other Changes and Additions to Version 0.15.0[](#other-changes-and-additions-to-version-0150 "Permanent link") 

-   Fix issues when using absolute links to Markdown files. ([#628](https://github.com/mkdocs/mkdocs/issues/628 "GitHub Issue mkdocs/mkdocs #628"))
-   Deprecate support of Python 2.6, pending removal in 1.0.0. ([#165](https://github.com/mkdocs/mkdocs/issues/165 "GitHub Issue mkdocs/mkdocs #165"))
-   Add official support for Python version 3.5.
-   Add support for [site_description](../../user-guide/configuration/#site_description) and [site_author](../../user-guide/configuration/#site_author) to the [ReadTheDocs](../../user-guide/choosing-your-theme/#readthedocs) theme. ([#631](https://github.com/mkdocs/mkdocs/issues/631 "GitHub Issue mkdocs/mkdocs #631"))
-   Update FontAwesome to 4.5.0. ([#789](https://github.com/mkdocs/mkdocs/issues/789 "GitHub Issue mkdocs/mkdocs #789"))
-   Increase IE support with X-UA-Compatible. ([#785](https://github.com/mkdocs/mkdocs/issues/785 "GitHub Issue mkdocs/mkdocs #785"))
-   Added support for Python\'s `-m` flag. ([#706](https://github.com/mkdocs/mkdocs/issues/706 "GitHub Issue mkdocs/mkdocs #706"))
-   Bugfix: Ensure consistent ordering of auto-populated pages. ([#638](https://github.com/mkdocs/mkdocs/issues/638 "GitHub Issue mkdocs/mkdocs #638"))
-   Bugfix: Scroll the tables of contents on the MkDocs theme if it is too long for the page. ([#204](https://github.com/mkdocs/mkdocs/issues/204 "GitHub Issue mkdocs/mkdocs #204"))
-   Bugfix: Add all ancestors to the page attribute `ancestors` rather than just the initial one. ([#693](https://github.com/mkdocs/mkdocs/issues/693 "GitHub Issue mkdocs/mkdocs #693"))
-   Bugfix: Include HTML in the build output again. ([#691](https://github.com/mkdocs/mkdocs/issues/691 "GitHub Issue mkdocs/mkdocs #691"))
-   Bugfix: Provide filename to Read the Docs. ([#721](https://github.com/mkdocs/mkdocs/issues/721 "GitHub Issue mkdocs/mkdocs #721") and RTD[#1480](https://github.com/mkdocs/mkdocs/issues/1480 "GitHub Issue mkdocs/mkdocs #1480"))
-   Bugfix: Silence Click\'s unicode_literals warning. ([#708](https://github.com/mkdocs/mkdocs/issues/708 "GitHub Issue mkdocs/mkdocs #708"))

## Version 0.14.0 (2015-06-09)[](#version-0140-2015-06-09 "Permanent link") 

-   Improve Unicode handling by ensuring that all config strings are loaded as Unicode. ([#592](https://github.com/mkdocs/mkdocs/issues/592 "GitHub Issue mkdocs/mkdocs #592"))
-   Remove dependency on the six library. ([#583](https://github.com/mkdocs/mkdocs/issues/583 "GitHub Issue mkdocs/mkdocs #583"))
-   Remove dependency on the ghp-import library. ([#547](https://github.com/mkdocs/mkdocs/issues/547 "GitHub Issue mkdocs/mkdocs #547"))
-   Add `--quiet` and `--verbose` options to all sub-commands. ([#579](https://github.com/mkdocs/mkdocs/issues/579 "GitHub Issue mkdocs/mkdocs #579"))
-   Add short options (`-a`) to most command line options. ([#579](https://github.com/mkdocs/mkdocs/issues/579 "GitHub Issue mkdocs/mkdocs #579"))
-   Add copyright footer for readthedocs theme. ([#568](https://github.com/mkdocs/mkdocs/issues/568 "GitHub Issue mkdocs/mkdocs #568"))
-   If the requested port in `mkdocs serve` is already in use, don\'t show the user a full stack trace. ([#596](https://github.com/mkdocs/mkdocs/issues/596 "GitHub Issue mkdocs/mkdocs #596"))
-   Bugfix: Fix a JavaScript encoding problem when searching with spaces. ([#586](https://github.com/mkdocs/mkdocs/issues/586 "GitHub Issue mkdocs/mkdocs #586"))
-   Bugfix: gh-deploy now works if the mkdocs.yml is not in the git repo root. ([#578](https://github.com/mkdocs/mkdocs/issues/578 "GitHub Issue mkdocs/mkdocs #578"))
-   Bugfix: Handle (pass-through instead of dropping) HTML entities while parsing TOC. ([#612](https://github.com/mkdocs/mkdocs/issues/612 "GitHub Issue mkdocs/mkdocs #612"))
-   Bugfix: Default extra_templates to an empty list, don\'t automatically discover them. ([#616](https://github.com/mkdocs/mkdocs/issues/616 "GitHub Issue mkdocs/mkdocs #616"))

## Version 0.13.3 (2015-06-02)[](#version-0133-2015-06-02 "Permanent link") 

-   Bugfix: Reduce validation error to a warning if the site_dir is within the docs_dir as this shouldn\'t cause any problems with building but will inconvenience users building multiple times. ([#580](https://github.com/mkdocs/mkdocs/issues/580 "GitHub Issue mkdocs/mkdocs #580"))

## Version 0.13.2 (2015-05-30)[](#version-0132-2015-05-30 "Permanent link") 

-   Bugfix: Ensure all errors and warnings are logged before exiting. ([#536](https://github.com/mkdocs/mkdocs/issues/536 "GitHub Issue mkdocs/mkdocs #536"))
-   Bugfix: Fix compatibility issues with ReadTheDocs. ([#554](https://github.com/mkdocs/mkdocs/issues/554 "GitHub Issue mkdocs/mkdocs #554"))

## Version 0.13.1 (2015-05-27)[](#version-0131-2015-05-27 "Permanent link") 

-   Bugfix: Fix a problem with minimal configurations which only contain a list of paths in the pages config. ([#562](https://github.com/mkdocs/mkdocs/issues/562 "GitHub Issue mkdocs/mkdocs #562"))

## Version 0.13.0 (2015-05-26)[](#version-0130-2015-05-26 "Permanent link") 

### Deprecations to Version 0.13.0[](#deprecations-to-version-0130 "Permanent link") 

#### Deprecate the JSON command[](#deprecate-the-json-command "Permanent link")

In this release the `mkdocs json` command has been marked as deprecated and when used a deprecation warning will be shown. It will be removed in a [future release](https://github.com/mkdocs/mkdocs/pull/481) of MkDocs, version 1.0 at the latest. The `mkdocs json` command provided a convenient way for users to output the documentation contents as JSON files but with the additions of search to MkDocs this functionality is duplicated.

A new index with all the contents from a MkDocs build is created in the [site_dir](../../user-guide/configuration/#site_dir), so with the default value for the `site_dir` It can be found in `site/mkdocs/search_index.json`.

This new file is created on every MkDocs build (with `mkdocs build`) and no configuration is needed to enable it.

#### Change the pages configuration[](#change-the-pages-configuration "Permanent link")

Provide a [new way](../../user-guide/writing-your-docs/#configure-pages-and-navigation) to define pages, and specifically nested pages, in the mkdocs.yml file and deprecate the existing approach, support will be removed with MkDocs 1.0.

#### Warn users about the removal of builtin themes[](#warn-users-about-the-removal-of-builtin-themes "Permanent link")

All themes other than mkdocs and readthedocs will be moved into external packages in a future release of MkDocs. This will enable them to be more easily supported and updates outside MkDocs releases.

### Major Additions to Version 0.13.0[](#major-additions-to-version-0130 "Permanent link") 

#### Search[](#search "Permanent link")

Support for search has now been added to MkDocs. This is based on the JavaScript library [lunr.js](https://lunrjs.com/). It has been added to both the `mkdocs` and `readthedocs` themes. See the custom theme documentation on [supporting search](../../dev-guide/themes/#search-and-themes) for adding it to your own themes.

#### New Command Line Interface[](#new-command-line-interface "Permanent link")

The command line interface for MkDocs has been re-written with the Python library [Click](https://click.palletsprojects.com/). This means that MkDocs now has an easier to use interface with better help output.

This change is partially backwards incompatible as while undocumented it was possible to pass any configuration option to the different commands. Now only a small subset of the configuration options can be passed to the commands. To see in full commands and available arguments use `mkdocs --help` and `mkdocs build --help` to have them displayed.

#### Support Extra HTML and XML files[](#support-extra-html-and-xml-files "Permanent link")

Like the [extra_javascript](../../user-guide/configuration/#extra_javascript) and [extra_css](../../user-guide/configuration/#extra_css) configuration options, a new option named [extra_templates](../../user-guide/configuration/#extra_templates) has been added. This will automatically be populated with any `.html` or `.xml` files in the project docs directory.

Users can place static HTML and XML files and they will be copied over, or they can also use Jinja2 syntax and take advantage of the [global variables](../../dev-guide/themes/#global-context).

By default MkDocs will use this approach to create a sitemap for the documentation.

### Other Changes and Additions to Version 0.13.0[](#other-changes-and-additions-to-version-0130 "Permanent link") 

-   Add support for [Markdown extension configuration options](../../user-guide/configuration/#markdown_extensions). ([#435](https://github.com/mkdocs/mkdocs/issues/435 "GitHub Issue mkdocs/mkdocs #435"))
-   MkDocs now ships Python [wheels](https://pythonwheels.com/). ([#486](https://github.com/mkdocs/mkdocs/issues/486 "GitHub Issue mkdocs/mkdocs #486"))
-   Only include the build date and MkDocs version on the homepage. ([#490](https://github.com/mkdocs/mkdocs/issues/490 "GitHub Issue mkdocs/mkdocs #490"))
-   Generate sitemaps for documentation builds. ([#436](https://github.com/mkdocs/mkdocs/issues/436 "GitHub Issue mkdocs/mkdocs #436"))
-   Add a clearer way to define nested pages in the configuration. ([#482](https://github.com/mkdocs/mkdocs/issues/482 "GitHub Issue mkdocs/mkdocs #482"))
-   Add an [extra config](../../user-guide/configuration/#extra) option for passing arbitrary variables to the template. ([#510](https://github.com/mkdocs/mkdocs/issues/510 "GitHub Issue mkdocs/mkdocs #510"))
-   Add `--no-livereload` to `mkdocs serve` for a simpler development server. ([#511](https://github.com/mkdocs/mkdocs/issues/511 "GitHub Issue mkdocs/mkdocs #511"))
-   Add copyright display support to all themes ([#549](https://github.com/mkdocs/mkdocs/issues/549 "GitHub Issue mkdocs/mkdocs #549"))
-   Add support for custom commit messages in a `mkdocs gh-deploy` ([#516](https://github.com/mkdocs/mkdocs/issues/516 "GitHub Issue mkdocs/mkdocs #516"))
-   Bugfix: Fix linking to media within the same directory as a markdown file called index.md ([#535](https://github.com/mkdocs/mkdocs/issues/535 "GitHub Issue mkdocs/mkdocs #535"))
-   Bugfix: Fix errors with Unicode filenames ([#542](https://github.com/mkdocs/mkdocs/issues/542 "GitHub Issue mkdocs/mkdocs #542")).

## Version 0.12.2 (2015-04-22)[](#version-0122-2015-04-22 "Permanent link") 

-   Bugfix: Fix a regression where there would be an error if some child titles were missing but others were provided in the pages config. ([#464](https://github.com/mkdocs/mkdocs/issues/464 "GitHub Issue mkdocs/mkdocs #464"))

## Version 0.12.1 (2015-04-14)[](#version-0121-2015-04-14 "Permanent link") 

-   Bugfix: Fixed a CSS bug in the table of contents on some browsers where the bottom item was not clickable.

## Version 0.12.0 (2015-04-14)[](#version-0120-2015-04-14 "Permanent link") 

-   Display the current MkDocs version in the CLI output. ([#258](https://github.com/mkdocs/mkdocs/issues/258 "GitHub Issue mkdocs/mkdocs #258"))
-   Check for CNAME file when using gh-deploy. ([#285](https://github.com/mkdocs/mkdocs/issues/285 "GitHub Issue mkdocs/mkdocs #285"))
-   Add the homepage back to the navigation on all themes. ([#271](https://github.com/mkdocs/mkdocs/issues/271 "GitHub Issue mkdocs/mkdocs #271"))
-   Add a strict more for local link checking. ([#279](https://github.com/mkdocs/mkdocs/issues/279 "GitHub Issue mkdocs/mkdocs #279"))
-   Add Google analytics support to all themes. ([#333](https://github.com/mkdocs/mkdocs/issues/333 "GitHub Issue mkdocs/mkdocs #333"))
-   Add build date and MkDocs version to the ReadTheDocs and MkDocs theme outputs. ([#382](https://github.com/mkdocs/mkdocs/issues/382 "GitHub Issue mkdocs/mkdocs #382"))
-   Standardize highlighting across all themes and add missing languages. ([#387](https://github.com/mkdocs/mkdocs/issues/387 "GitHub Issue mkdocs/mkdocs #387"))
-   Add a verbose flag. (-v) to show more details about what the build. ([#147](https://github.com/mkdocs/mkdocs/issues/147 "GitHub Issue mkdocs/mkdocs #147"))
-   Add the option to specify a remote branch when deploying to GitHub. This enables deploying to GitHub pages on personal and repo sites. ([#354](https://github.com/mkdocs/mkdocs/issues/354 "GitHub Issue mkdocs/mkdocs #354"))
-   Add favicon support to the ReadTheDocs theme HTML. ([#422](https://github.com/mkdocs/mkdocs/issues/422 "GitHub Issue mkdocs/mkdocs #422"))
-   Automatically refresh the browser when files are edited. ([#163](https://github.com/mkdocs/mkdocs/issues/163 "GitHub Issue mkdocs/mkdocs #163"))
-   Bugfix: Never re-write URLs in code blocks. ([#240](https://github.com/mkdocs/mkdocs/issues/240 "GitHub Issue mkdocs/mkdocs #240"))
-   Bugfix: Don\'t copy dotfiles when copying media from the `docs_dir`. ([#254](https://github.com/mkdocs/mkdocs/issues/254 "GitHub Issue mkdocs/mkdocs #254"))
-   Bugfix: Fix the rendering of tables in the ReadTheDocs theme. ([#106](https://github.com/mkdocs/mkdocs/issues/106 "GitHub Issue mkdocs/mkdocs #106"))
-   Bugfix: Add padding to the bottom of all bootstrap themes. ([#255](https://github.com/mkdocs/mkdocs/issues/255 "GitHub Issue mkdocs/mkdocs #255"))
-   Bugfix: Fix issues with nested Markdown pages and the automatic pages configuration. ([#276](https://github.com/mkdocs/mkdocs/issues/276 "GitHub Issue mkdocs/mkdocs #276"))
-   Bugfix: Fix a URL parsing error with GitHub enterprise. ([#284](https://github.com/mkdocs/mkdocs/issues/284 "GitHub Issue mkdocs/mkdocs #284"))
-   Bugfix: Don\'t error if the mkdocs.yml is completely empty. ([#288](https://github.com/mkdocs/mkdocs/issues/288 "GitHub Issue mkdocs/mkdocs #288"))
-   Bugfix: Fix a number of problems with relative URLs and Markdown files. ([#292](https://github.com/mkdocs/mkdocs/issues/292 "GitHub Issue mkdocs/mkdocs #292"))
-   Bugfix: Don\'t stop the build if a page can\'t be found, continue with other pages. ([#150](https://github.com/mkdocs/mkdocs/issues/150 "GitHub Issue mkdocs/mkdocs #150"))
-   Bugfix: Remove the site_name from the page title, this needs to be added manually. ([#299](https://github.com/mkdocs/mkdocs/issues/299 "GitHub Issue mkdocs/mkdocs #299"))
-   Bugfix: Fix an issue with table of contents cutting off Markdown. ([#294](https://github.com/mkdocs/mkdocs/issues/294 "GitHub Issue mkdocs/mkdocs #294"))
-   Bugfix: Fix hostname for BitBucket. ([#339](https://github.com/mkdocs/mkdocs/issues/339 "GitHub Issue mkdocs/mkdocs #339"))
-   Bugfix: Ensure all links end with a slash. ([#344](https://github.com/mkdocs/mkdocs/issues/344 "GitHub Issue mkdocs/mkdocs #344"))
-   Bugfix: Fix repo links in the readthedocs theme. ([#365](https://github.com/mkdocs/mkdocs/issues/365 "GitHub Issue mkdocs/mkdocs #365"))
-   Bugfix: Include jQuery locally to avoid problems using MkDocs offline. ([#143](https://github.com/mkdocs/mkdocs/issues/143 "GitHub Issue mkdocs/mkdocs #143"))
-   Bugfix: Don\'t allow the docs_dir to be in the site_dir or vice versa. ([#384](https://github.com/mkdocs/mkdocs/issues/384 "GitHub Issue mkdocs/mkdocs #384"))
-   Bugfix: Remove inline CSS in the ReadTheDocs theme. ([#393](https://github.com/mkdocs/mkdocs/issues/393 "GitHub Issue mkdocs/mkdocs #393"))
-   Bugfix: Fix problems with the child titles due to the order the pages config was processed. ([#395](https://github.com/mkdocs/mkdocs/issues/395 "GitHub Issue mkdocs/mkdocs #395"))
-   Bugfix: Don\'t error during live reload when the theme doesn\'t exist. ([#373](https://github.com/mkdocs/mkdocs/issues/373 "GitHub Issue mkdocs/mkdocs #373"))
-   Bugfix: Fix problems with the Meta extension when it may not exist. ([#398](https://github.com/mkdocs/mkdocs/issues/398 "GitHub Issue mkdocs/mkdocs #398"))
-   Bugfix: Wrap long inline code otherwise they will run off the screen. ([#313](https://github.com/mkdocs/mkdocs/issues/313 "GitHub Issue mkdocs/mkdocs #313"))
-   Bugfix: Remove HTML parsing regular expressions and parse with HTMLParser to fix problems with titles containing code. ([#367](https://github.com/mkdocs/mkdocs/issues/367 "GitHub Issue mkdocs/mkdocs #367"))
-   Bugfix: Fix an issue with the scroll to anchor causing the title to be hidden under the navigation. ([#7](https://github.com/mkdocs/mkdocs/issues/7 "GitHub Issue mkdocs/mkdocs #7"))
-   Bugfix: Add nicer CSS classes to the HTML tables in bootswatch themes. ([#295](https://github.com/mkdocs/mkdocs/issues/295 "GitHub Issue mkdocs/mkdocs #295"))
-   Bugfix: Fix an error when passing in a specific config file with `mkdocs serve`. ([#341](https://github.com/mkdocs/mkdocs/issues/341 "GitHub Issue mkdocs/mkdocs #341"))
-   Bugfix: Don\'t overwrite index.md files with the `mkdocs new` command. ([#412](https://github.com/mkdocs/mkdocs/issues/412 "GitHub Issue mkdocs/mkdocs #412"))
-   Bugfix: Remove bold and italic from code in the ReadTheDocs theme. ([#411](https://github.com/mkdocs/mkdocs/issues/411 "GitHub Issue mkdocs/mkdocs #411"))
-   Bugfix: Display images inline in the MkDocs theme. ([#415](https://github.com/mkdocs/mkdocs/issues/415 "GitHub Issue mkdocs/mkdocs #415"))
-   Bugfix: Fix problems with no-highlight in the ReadTheDocs theme. ([#319](https://github.com/mkdocs/mkdocs/issues/319 "GitHub Issue mkdocs/mkdocs #319"))
-   Bugfix: Don\'t delete hidden files when using `mkdocs build --clean`. ([#346](https://github.com/mkdocs/mkdocs/issues/346 "GitHub Issue mkdocs/mkdocs #346"))
-   Bugfix: Don\'t block newer versions of Python-markdown on Python \>= 2.7. ([#376](https://github.com/mkdocs/mkdocs/issues/376 "GitHub Issue mkdocs/mkdocs #376"))
-   Bugfix: Fix encoding issues when opening files across platforms. ([#428](https://github.com/mkdocs/mkdocs/issues/428 "GitHub Issue mkdocs/mkdocs #428"))

## Version 0.11.1 (2014-11-20)[](#version-0111-2014-11-20 "Permanent link") 

-   Bugfix: Fix a CSS wrapping issue with code highlighting in the ReadTheDocs theme. ([#233](https://github.com/mkdocs/mkdocs/issues/233 "GitHub Issue mkdocs/mkdocs #233"))

## Version 0.11.0 (2014-11-18)[](#version-0110-2014-11-18 "Permanent link") 

-   Render 404.html files if they exist for the current theme. ([#194](https://github.com/mkdocs/mkdocs/issues/194 "GitHub Issue mkdocs/mkdocs #194"))
-   Bugfix: Fix long nav bars, table rendering and code highlighting in MkDocs and ReadTheDocs themes. ([#225](https://github.com/mkdocs/mkdocs/issues/225 "GitHub Issue mkdocs/mkdocs #225"))
-   Bugfix: Fix an issue with the google_analytics code. ([#219](https://github.com/mkdocs/mkdocs/issues/219 "GitHub Issue mkdocs/mkdocs #219"))
-   Bugfix: Remove `__pycache__` from the package tar. ([#196](https://github.com/mkdocs/mkdocs/issues/196 "GitHub Issue mkdocs/mkdocs #196"))
-   Bugfix: Fix markdown links that go to an anchor on the current page. ([#197](https://github.com/mkdocs/mkdocs/issues/197 "GitHub Issue mkdocs/mkdocs #197"))
-   Bugfix: Don\'t add `prettyprint well` CSS classes to all HTML, only add it in the MkDocs theme. ([#183](https://github.com/mkdocs/mkdocs/issues/183 "GitHub Issue mkdocs/mkdocs #183"))
-   Bugfix: Display section titles in the ReadTheDocs theme. ([#175](https://github.com/mkdocs/mkdocs/issues/175 "GitHub Issue mkdocs/mkdocs #175"))
-   Bugfix: Use the polling observer in watchdog so rebuilding works on filesystems without inotify. ([#184](https://github.com/mkdocs/mkdocs/issues/184 "GitHub Issue mkdocs/mkdocs #184"))
-   Bugfix: Improve error output for common configuration related errors. ([#176](https://github.com/mkdocs/mkdocs/issues/176 "GitHub Issue mkdocs/mkdocs #176"))

## Version 0.10.0 (2014-10-29)[](#version-0100-2014-10-29 "Permanent link") 

-   Added support for Python 3.3 and 3.4. ([#103](https://github.com/mkdocs/mkdocs/issues/103 "GitHub Issue mkdocs/mkdocs #103"))
-   Configurable Python-Markdown extensions with the config setting `markdown_extensions`. ([#74](https://github.com/mkdocs/mkdocs/issues/74 "GitHub Issue mkdocs/mkdocs #74"))
-   Added `mkdocs json` command to output your rendered documentation as json files. ([#128](https://github.com/mkdocs/mkdocs/issues/128 "GitHub Issue mkdocs/mkdocs #128"))
-   Added `--clean` switch to `build`, `json` and `gh-deploy` commands to remove stale files from the output directory. ([#157](https://github.com/mkdocs/mkdocs/issues/157 "GitHub Issue mkdocs/mkdocs #157"))
-   Support multiple theme directories to allow replacement of individual templates rather than copying the full theme. ([#129](https://github.com/mkdocs/mkdocs/issues/129 "GitHub Issue mkdocs/mkdocs #129"))
-   Bugfix: Fix `<ul>` rendering in readthedocs theme. ([#171](https://github.com/mkdocs/mkdocs/issues/171 "GitHub Issue mkdocs/mkdocs #171"))
-   Bugfix: Improve the readthedocs theme on smaller displays. ([#168](https://github.com/mkdocs/mkdocs/issues/168 "GitHub Issue mkdocs/mkdocs #168"))
-   Bugfix: Relaxed required python package versions to avoid clashes. ([#104](https://github.com/mkdocs/mkdocs/issues/104 "GitHub Issue mkdocs/mkdocs #104"))
-   Bugfix: Fix issue rendering the table of contents with some configs. ([#146](https://github.com/mkdocs/mkdocs/issues/146 "GitHub Issue mkdocs/mkdocs #146"))
-   Bugfix: Fix path for embedded images in sub pages. ([#138](https://github.com/mkdocs/mkdocs/issues/138 "GitHub Issue mkdocs/mkdocs #138"))
-   Bugfix: Fix `use_directory_urls` config behavior. ([#63](https://github.com/mkdocs/mkdocs/issues/63 "GitHub Issue mkdocs/mkdocs #63"))
-   Bugfix: Support `extra_javascript` and `extra_css` in all themes. ([#90](https://github.com/mkdocs/mkdocs/issues/90 "GitHub Issue mkdocs/mkdocs #90"))
-   Bugfix: Fix path-handling under Windows. ([#121](https://github.com/mkdocs/mkdocs/issues/121 "GitHub Issue mkdocs/mkdocs #121"))
-   Bugfix: Fix the menu generation in the readthedocs theme. ([#110](https://github.com/mkdocs/mkdocs/issues/110 "GitHub Issue mkdocs/mkdocs #110"))
-   Bugfix: Fix the mkdocs command creation under Windows. ([#122](https://github.com/mkdocs/mkdocs/issues/122 "GitHub Issue mkdocs/mkdocs #122"))
-   Bugfix: Correctly handle external `extra_javascript` and `extra_css`. ([#92](https://github.com/mkdocs/mkdocs/issues/92 "GitHub Issue mkdocs/mkdocs #92"))
-   Bugfix: Fixed favicon support. ([#87](https://github.com/mkdocs/mkdocs/issues/87 "GitHub Issue mkdocs/mkdocs #87"))

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