# Source: https://lingui.dev/guides/pseudolocalization.md

# Pseudolocalization

Pseudo-localization is a method used to check the software's readiness to be localized. This method shows how the product's UI will look after translation. Use this feature to reduce potential rework by checking whether any source strings should be altered before the translation process begins.

It also makes it easy to identify hard-coded strings and improperly concatenated strings so that they can be localized properly.

> Example: Ţĥĩś ţēxţ ĩś ƥśēũďōĺōćàĺĩźēď

## Configuration[​](#configuration "Direct link to Configuration")

To configure pseudolocalization, add the [`pseudoLocale`](/ref/conf.md#pseudolocale) property to your Lingui configuration file:

lingui.config.{ts,js}

```
import { defineConfig } from "@lingui/cli";

export default defineConfig({
  locales: ["en", "pseudo-LOCALE"],
  pseudoLocale: "pseudo-LOCALE",
  fallbackLocales: {
    "pseudo-LOCALE": "en",
  },
});
```

The `pseudoLocale` option must be set to any string that matches a value in the [`locales`](/ref/conf.md#locales) configuration. If this is not set correctly, no folder or pseudolocalization will be created.

If the `fallbackLocales` is configured, the pseudolocalization will be generated from the translated fallback locale instead.

## Generate Pseudolocalization[​](#generate-pseudolocalization "Direct link to Generate Pseudolocalization")

After running the [`extract`](/ref/cli.md#extract) command, verify that the folder for the pseudolocale has been created.

Pseudolocalization is automatically generated during the [`compile`](/ref/cli.md#compile) process, using the messages.

## Switch Browser Into Specified Pseudolocale[​](#switch-browser-into-specified-pseudolocale "Direct link to Switch Browser Into Specified Pseudolocale")

You can switch your browser to a pseudolocale either by adjusting the browser settings or by using extensions. Extensions provide flexibility by allowing you to use any locale, while browser settings are usually limited to valid language tags (BCP 47).

In such cases, the pseudolocale must be a standard locale that isn't already used in your application. For example, you could use `zu-ZA` (Zulu - South Africa).

Chrome:

* With extension (valid locale) - [Locale Switcher](https://chrome.google.com/webstore/detail/locale-switcher/kngfjpghaokedippaapkfihdlmmlafcc).
* Without extension (valid locale) - <chrome://settings/?search=languages>.

Firefox:

* With extension (any string) - [Quick Accept-Language Switcher](https://addons.mozilla.org/en-GB/firefox/addon/quick-accept-language-switc/?src=search).
* Without extension (valid locale) - [about](about:preferences#general)
  <!-- -->
  [:preferences](about:preferences#general)
  <!-- -->
  [#general](about:preferences#general) > *Language*.
