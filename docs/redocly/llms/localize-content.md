# Source: https://redocly.com/docs/realm/content/localization/localize-content.md

# Add translated content

After preparing the structure of your project for localization, add the translated content files to your locale folders.

## Before you begin

Make sure you have the following:

- the structure of your project prepared for localization
- translated content files


## Add translated content files

To add a translated Markdown file or API description file to your project, place the files in their respective locale folders inside the `@l10n` folder.

The relative path from the locale folder to the translated file must be the same as the relative path from the root of the project to the file in the default language.
For example, if you originally had a file with path `./index.md`, the file translated to Spanish must be located in `./@l10n/es-ES/index.md`, as in the following example:


```treeview Example file structure for localized content
    your-awesome-project/
    âââ @l10n/
    â   âââ es-ES/
    â   â   âââ images/
    â   â   âââ index.md
    â   â   âââ openapi.yaml   
    â   âââ es-419/
    â   â   âââ images/
    â   â   âââ index.md
    â   â   âââ openapi.yaml
    â   âââ fr/
    â   â   âââ images/
    â   â   âââ index.md
    â   â   âââ openapi.yaml
    â   âââ ja/
    â   â   âââ images/
    â   â   âââ index.md
    â   â   âââ openapi.yaml
    â   âââ zh-Hans/
    â   â   âââ images/
    â   â   âââ index.md
    â   â   âââ openapi.yaml
    â   âââ zh-Hant/
    â       âââ images/
    â       âââ openapi.yaml
    â       âââ index.md
    âââ images/
    âââ index.md
    âââ openapi.yaml
    âââ redocly.yaml
```

## Localize partial content

You can localize content you include in partials, or reusable content files pulled into multiple files using a [`partial` Markdoc tag](https://redocly.com/docs/learn-markdoc/tags/partial).

To localize content in partials:

1. Add a folder with the same name as your partials folder to each of your locale folders.
2. Place the translated content in each of the partials folders.



```treeview Example folder structure for localizing partials
    your-awesome-project/
    âââ _partials/
    âââ @l10n/
    â   âââ es-ES/
    â   â   âââ _partials/
    â   â   âââ images/
    â   â   âââ index.md
    â   â   âââ openapi.yaml
    â  ... 
    âââ images/
    âââ index.md
    âââ openapi.yaml
    âââ redocly.yaml
```

## Resources

- **[Localization configuration](/docs/realm/config/l10n)** - Configure language support, default locales, and localization behavior for your multi-language project
- **[Localize UI labels](/docs/realm/content/localization/localize-labels)** - Translate interface labels and UI text using translation keys for consistent multi-language user experience