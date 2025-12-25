# Source: https://docs.readthedocs.com/platform/latest/localization.html

# Localization and Internationalization[](#localization-and-internationalization "Link to this heading")

In this article, we explain high-level approaches to internationalizing and localizing your documentation.

By default, Read the Docs assumes that your documentation is or *might become* multilingual one day. The initial default language is English and therefore you often see the initial build of your documentation published at [`/en/latest/`], where the [`/en`] denotes that it's in English. By having the [`en`] URL component present from the beginning, you are ready for the eventuality that you would want a second language.

Read the Docs supports hosting your documentation in multiple languages. Read below for the various approaches that we support.

-   [Projects with one language](#projects-with-one-language)

-   [Projects with multiple translations](#projects-with-multiple-translations)

    -   [Translation workflows](#translation-workflows)

## [Projects with one language](#id1)[](#projects-with-one-language "Link to this heading")

If your documentation isn't in English (the default), you should indicate which language you have written it in.

It is easy to set the *Language* of your project. On the project *Admin* page (or *Import* page), simply select your desired *Language* from the dropdown. This will tell Read the Docs that your project is in the language. The language will be represented in the URL for your project.

For example, a project that is in Spanish will have a default URL of [`/es/latest/`] instead of [`/en/latest/`].