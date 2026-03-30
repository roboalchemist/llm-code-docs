# Source: https://redocly.com/docs/realm/content/localization/localize-labels.md

# Localize UI labels using translation keys

Redocly projects include user interface (UI) elements with text labels.
These labels can either be the default generated labels or configured labels added by users when defining elements such as the sidebars or the footer.

To localize UI labels, first you need to add keys to the user-defined UI elements, then copy them to a `translations.yaml` file and add the translations to each key.
A `translations.yaml` file contains translation keys and localized labels for a specific language.
These key-value pairs are used to translate different types of content, including the following:

- **User-defined UI elements:** Define and translate project labels by updating the `sidebars.yaml` or `redocly.yaml` files with the translation keys and including a `translations.yaml` file in each locale folder with the language specific key-value pairs.
- **Base UI component labels:** Translate base UI component labels by including a `translations.yaml` file in each locale folder with the language specific key-value pairs.
- **Content on React pages:** Define and translate content on React pages by creating the translation keys on the React page and including a `translations.yaml` file in each locale folder with the language specific key-value pairs.


Base UI component labels include predefined keys; however, you must create keys for all other types of content.

## Before you begin

Make sure you have the following:

- a project with an `@l10n` folder containing your translated content organized into locales.
See [l10n configuration](/docs/realm/config/l10n) for setup information and [Add translated content](/docs/realm/content/localization/localize-content) for content localization.


## Localize base UI components

Redocly provides default translations for the most popular languages.
See [Supported default translations](/docs/realm/config/l10n#supported-default-translations) for a list of supported languages.

Each label from the components that come bundled with the project has a predefined translation key assigned to it.
See [l10n translation keys](/docs/realm/content/localization/translation-keys) for a list of predefined translation keys available.

To customize default translations or add new translations for the base UI components:

1. If you haven't already, add a `translations.yaml` file to each of your locale folders.
2. Copy and paste the [l10n translation keys](/docs/realm/content/localization/translation-keys) into each `translations.yaml` file in the locale folders.
3. Add the translated values for the translation keys.


For example, to translate the login button text to Spanish, use the following key value pair in your `translations.yaml` file in the `es-ES` subfolder:


```yaml translations.yaml
userMenu.login: acceso
```

## Localize user-defined UI elements

Some UI elements in your project support customizable configurations and can contain user-defined text, such as labels and titles.
To be able to localize the text components of these elements, you must first create translation keys in their configuration files.

The user-defined UI elements that use translation keys are:

- [navbar](/docs/realm/config/navbar)
- [breadcrumbs](/docs/realm/config/breadcrumbs)
- [search bar](/docs/realm/config/search)
- [footer](/docs/realm/config/footer)
- [catalog classic](/docs/realm/config/catalog-classic)
- [user menu](/docs/realm/config/user-menu)
- [sidebars](/docs/realm/config/sidebar)


### Add translation keys to user-defined UI elements

Translation keys for most user-defined UI elements are included in the `redocly.yaml` configuration files.
Sidebars are an exception and have their configuration in the `sidebars.yaml` files.

To add translation keys to user-defined elements, add translation key options to elements in your `redocly.yaml` or `sidebars.yaml` files.
For more information on the types of keys a UI element uses, see [Configure Redocly](/docs/realm/config) and navigate to the relevant reference documentation.

The following example shows a complete `redocly.yaml` file with translation keys configured for navbar and footer elements:


```yaml redocly.yaml
navbar:
  items:
    - label: Home
      page: /
    - group: Products
      groupTranslationKey: navbar.products.label
      items:
        - page: /redocly-museum/
          label: Redocly Museum API
footer:
  items:
    - groupTranslationKey: footer.legal.label
      items:
        - label: Terms of Use
          labelTranslationKey: footer.legal.termsOfUse
          href: '/terms-of-use/'
```

The following example is a sidebar with translation keys added to each `group`, `label`, and `separator`:


```yaml sidebars.yaml
    - group: Getting Started
      groupTranslationKey: sidebar.gettingStarted
      items:
        - separator: My separators
          separatorTranslationKey: sidebar.gettingStarted.separator
        - group: Introduction
          groupTranslationKey: sidebar.gettingStarted.introduction
          separatorLine: true
          items:
            - page: index.md
              label: First steps
              labelTranslationKey: sidebar.gettingStarted.first-steps
    - page: overview.md
      label: Installation
      labelTranslationKey: sidebar.installation
```

### Add translations for user-defined UI elements

To add translations for your configured translation keys:

1. Add a `translations.yaml` file to each of your locale folders (if you haven't already)
2. Find the options that end with `TranslationKey` in your project's `redocly.yaml` and `sidebars.yaml` files (such as `groupTranslationKey`, `labelTranslationKey`, `titleTranslationKey`, `descriptionTranslationKey`, `separatorTranslationKey`, and `missingCategoryNameTranslationKey`)
3. Add the translation key values with their translated text to each locale's `translations.yaml` file


The following example shows a complete `translations.yaml` file for Spanish translations:


```yaml @l10n/es-ES/translations.yaml
navbar.home: pÃ¡gina de inicio
navbar.products.label: productos
navbar.products.redocly-museum: Redocly Museo
footer.legal.label: Legal
footer.legal.termsOfUse: Condiciones de uso
sidebar.gettingStarted: Empezando
sidebar.gettingStarted.separator: Mis separadores
sidebar.gettingStarted.introduction: IntroducciÃ³n
sidebar.gettingStarted.first-steps: Primeros pasos
sidebar.installation: InstalaciÃ³n
```

## Localize React pages

You must create translations keys in the React file before you can assign it a language specific value in the `translations.yaml` file.

To translate content in React pages, use the `useTranslate` hook by extracting it from `useThemeHooks`.
This hook returns a `translate` function which accepts the following two arguments:

- a translation key
- a default value which is used when a translation is missing


The following is an example of a React page with a translated heading 1:


```typescript
import React from 'react';

import { useThemeHooks } from '@redocly/theme/core/hooks';

export default function () {
  const { useTranslate } = useThemeHooks();  
  const { translate } = useTranslate();
  return (
    <div>
      <h1>{translate('react-page.heading', 'This is default fallback text!')}</h1>
    </div>
  );
}
```

Note
The `react-page.heading` is an arbitrary name.
You can name your translation keys however you want.

The heading on the example React page includes the same text for all languages by default, "This is default fallback text!".
To translate it to different languages, add the key `react-page.heading` to the respective `translations.yaml` files, as in the following example for a Spanish translation:


```yaml translations.yaml
react-page.heading: Â¡Este es un texto traducido!
```

## Change the built-in UI labels

Redocly projects come with a set of built-in UI labels in US English.
You can configure a `translations.yaml` file to override these labels, accomplishing the following goals:

- Adjust the UI text to better suit your project (for example, change "Login" to "Sign in").
- Change the language used in the UI, without adding a language picker.


To change the built-in UI labels:

1. Add a `translations.yaml` file to the root of your project.
2. Copy and paste the [l10n translation keys](/docs/realm/content/localization/translation-keys) to the file.
3. Add your customized values for the translation keys.
4. Commit your changes.


The following is an example `translations.yaml` file that if included in the root of your project, changes the label of the login button to "Sign in":


```yaml
userMenu.login: Sign in
```

Alternatively, you can change the labels in the default UI components, by [ejecting the components you want to change](/docs/realm/customization/eject-components).

## Find translation keys using your browser

Your browser's developer tools can help you identify which translation keys to use.
These tools allow you to inspect HTML elements and see which translation keys are applied.

To find translation keys using browser developer tools:

1. Right-click the page element that you want to find the translation key for and click **Inspect element**.
The browser opens developer tools with the element highlighted in the **Elements** tab.
2. In the code of the highlighted element, locate the `data-translation-key` property.
The translation key is the value of the `data-translation-key` property.
In some cases you might need to drill down the code nested in the selected element.



Now you can add the key to the `translations.yaml` file and use it to localize or customize your project.

## Resources

- **[Localization configuration](/docs/realm/config/l10n)** - Configure language support, default locales, and localization behavior for your multi-language project
- **[Localize content files](/docs/realm/content/localization/localize-content)** - Translate your documentation content into multiple languages with proper file organization and structure