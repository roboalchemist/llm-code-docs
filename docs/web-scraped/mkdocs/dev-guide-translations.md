# Source: https://www.mkdocs.org/dev-guide/translations/

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
    -   [Developer Guide](../)
    -   [Themes](../themes/)
    -   [Translations](./)
    -   [Plugins](../plugins/)
    -   [API Reference](../api/)
-   [About ](#)
    -   [Release Notes](../../about/release-notes/)
    -   [Contributing](../../about/contributing/)
    -   [License](../../about/license/)

```
<!-- -->
```
-   [ Search](#)
-   [ Previous](../themes/)
-   [Next ](../plugins/)
-   [ Edit on GitHub](https://github.com/mkdocs/mkdocs/blob/master/docs/dev-guide/translations.md)

[]

-   [Translations](#translations)
    -   [Localization tooling prerequisites](#localization-tooling-prerequisites)
    -   [Adding language translations to themes](#adding-language-translations-to-themes)
    -   [Updating a theme translation](#updating-a-theme-translation)
    -   [Updating theme documentation](#updating-theme-documentation)
    -   [Contributing translations](#contributing-translations)

# Translations[](#translations "Permanent link")

Theme localization guide.

------------------------------------------------------------------------

The [built-in themes](../../user-guide/choosing-your-theme/) that are included with MkDocs provide support for translations. This is a guide for translators, which documents the process for contributing new translations and/or updating existing translations. For guidance on modifying the existing themes, see the [Contributing Guide](../../about/contributing/#submitting-changes-to-the-builtin-themes). To enable a specific translation see the documentation about the specific theme you are using in the [User Guide](../../user-guide/choosing-your-theme/). For translations of third-party themes, please see the documentation for those themes. For a third-party theme to make use of MkDocs\' translation tools and methods, that theme must be properly [configured](../themes/#supporting-theme-localizationtranslation) to make use of those tools.

Note

Translations only apply to text contained within a theme\'s template, such as \"next\" and \"previous\" links. The Markdown content of a page is not translated. If you wish to create multilingual documentation, you need to combine theme localization with a third-party internationalization/localization plugin.

## Localization tooling prerequisites[](#localization-tooling-prerequisites "Permanent link")

Theme localization makes use of the [babel](https://babel.pocoo.org/en/latest/cmdline.html) project for generation and compilation of localization files. You will need to be working from the git working tree on your local machine to make use of the translation commands.

See the [Contributing Guide](../../about/contributing/) for direction on how to [Install for Development](../../about/contributing/#installing-for-development) and [Submit a Pull Request](../../about/contributing/#submitting-pull-requests). The instructions in this document assume that you are working from a properly configured development environment.

Make sure translation requirements are installed in your environment:

``` highlight
pip install 'mkdocs[i18n]'
```

## Adding language translations to themes[](#adding-language-translations-to-themes "Permanent link")

If your favorite language locale is not yet supported on one (or both) of the built-in themes (`mkdocs` and `readthedocs`), you can easily contribute a translation by following the steps below.

Here is a quick summary of what you\'ll need to do:

1.  [Fork and clone the MkDocs repository](#fork-and-clone-the-mkdocs-repository) and then [install MkDocs for development](../../about/contributing/#installing-for-development) for adding and testing translations.
2.  [Initialize new localization catalogs](#initializing-the-localization-catalogs) for your language (if a translation for your locale already exists, follow the instructions for [updating theme localization files](#updating-the-translation-catalogs) instead).
3.  [Add a translation](#translating-the-mkdocs-themes) for every text placeholder in the localized catalogs.
4.  [Locally serve and test](#testing-theme-translations) the translated themes for your language.
5.  [Update the documentation](#updating-theme-documentation) about supported translations for each translated theme.
6.  [Contribute your translation](#contributing-translations) through a Pull Request.

Note

Translation locales are usually identified using the [ISO-639-1](https://en.wikipedia.org/wiki/ISO_639-1) (2-letter) language codes. While territory/region/county codes are also supported, location specific translations should only be added after the general language translation has been completed and the regional dialect requires use of a term which differs from the general language translation.

### Fork and clone the MkDocs repository[](#fork-and-clone-the-mkdocs-repository "Permanent link")

In the following steps you\'ll work with a fork of the MkDocs repository. Follow the instructions for [forking and cloning the MkDocs repository](../../about/contributing/#installing-for-development).

To test the translations you also need to [install MkDocs for development](../../about/contributing/#installing-for-development) from your fork.

### Initializing the localization catalogs[](#initializing-the-localization-catalogs "Permanent link")

The templates for each theme contain text placeholders that have been extracted into a Portable Object Template (`messages.pot`) file, which is present in each theme\'s folder.

Initializing a catalog consists of running a command which will create a directory structure for your desired language and prepare a Portable Object (`messages.po`) file derived from the `pot` file of the theme.

Use the `init_catalog` command on each theme\'s directory and provide the appropriate language code (`-l <language>`).

The language code is almost always just two lowercase letters, such as `sv`, but in some cases it needs to be further disambiguated.

See:

-   [Already translated languages for built-in themes](../../user-guide/choosing-your-theme/#mkdocs-locale)
-   [ISO 639 Language List](https://www.localeplanet.com/icu/iso639.html)
-   [Language subtag registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry)

In particular, the way to know that the `pt` language should be disambiguated as `pt_PT` and `pt_BR` is that the *Language subtag registry* page contains `pt-` if you search for it. Whereas `sv` should remain just `sv`, because that page does *not* contain `sv-`.

So, if we pick `es` (Spanish) as our example language code, to add a translation for it to both built-in themes, run these commands:

``` highlight
pybabel init --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l es
pybabel init --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l es
```

The above command will create a file structure as follows:

``` highlight
mkdocs/themes/mkdocs/locales
├── es
│   └── LC_MESSAGES
│       └── messages.po
```

You can now move on to the next step and [add a translation](#translating-the-mkdocs-themes) for every text placeholder in the localized catalog.

## Updating a theme translation[](#updating-a-theme-translation "Permanent link")

If a theme\'s `messages.pot` template file has been [updated](../../about/contributing/#submitting-changes-to-the-builtin-themes) since the `messages.po` was last updated for your locale, follow the steps below to update the theme\'s `messages.po` file:

1.  [Update the theme\'s translation catalog](#updating-the-translation-catalogs) to refresh the translatable text placeholders of each theme.
2.  [Translate](#translating-the-mkdocs-themes) the newly added translatable text placeholders on every `messages.po` catalog file language you can.
3.  [Locally serve and test](#testing-theme-translations) the translated themes for your language.
4.  [Contribute your translation](#contributing-translations) through a Pull Request.

### Updating the translation catalogs[](#updating-the-translation-catalogs "Permanent link")

This step should be completed after a theme template have been [updated](../../about/contributing/#submitting-changes-to-the-builtin-themes) for each language that you are comfortable contributing a translation for.

To update the `fr` translation catalog of both built-in themes, use the following commands:

``` highlight
pybabel update --ignore-obsolete --input-file mkdocs/themes/mkdocs/messages.pot --output-dir mkdocs/themes/mkdocs/locales -l fr
pybabel update --ignore-obsolete --input-file mkdocs/themes/readthedocs/messages.pot --output-dir mkdocs/themes/readthedocs/locales -l fr
```

You can now move on to the next step and [add a translation](#translating-the-mkdocs-themes) for every updated text placeholder in the localized catalog.

### Translating the MkDocs themes[](#translating-the-mkdocs-themes "Permanent link")

Now that your localized `messages.po` files are ready, all you need to do is add a translation in each `msgstr` item for each `msgid` item in the file.

``` highlight
msgid "Next"
msgstr "Siguiente"
```

Warning

Do not modify the `msgid` as it is common to all translations. Just add its translation in the `msgstr` item.

Once you have finished translating all of the terms listed in the `po` file, you\'ll want to [test your localized theme](#testing-theme-translations).

### Testing theme translations[](#testing-theme-translations "Permanent link")

To test a theme with translations, you need to first compile the `messages.po` files of your theme into `messages.mo` files. The following commands will compile the `es` translation for both built-in themes:

``` highlight
pybabel compile --statistics --directory mkdocs/themes/mkdocs/locales -l es
pybabel compile --statistics --directory mkdocs/themes/readthedocs/locales -l es
```

The above command results in the following file structure:

``` highlight
mkdocs/themes/mkdocs/locales
├── es
│   └── LC_MESSAGES
│       ├── messages.mo
│       └── messages.po
```

Note that the compiled `messages.mo` file was generated based on the `messages.po` file that you just edited.

Then modify the `mkdocs.yml` file at the root of the project to test the new and/or updated locale:

``` highlight
theme:
  name: mkdocs
  locale: es
```

Finally, run `mkdocs serve` to check out your new localized version of the theme.

Note

The build and release process takes care of compiling and distributing all locales to end users so you only have to worry about contributing the actual text translation `messages.po` files (the rest is ignored by git).

After you have finished testing your work, be sure to undo the change to the `locale` setting in the `mkdocs.yml` file before submitting your changes.

## Updating theme documentation[](#updating-theme-documentation "Permanent link")

The page [Choosing your theme](../../user-guide/choosing-your-theme/) updates by itself with all available locale options.

## Contributing translations[](#contributing-translations "Permanent link")

It is now time for you to [contribute](../../about/contributing/) your nice work to the project. Thank you!

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