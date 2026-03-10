# Locales & translations

The Strapi [admin panel](/cms/admin-panel-customization) ships with English strings and supports adding other locales so your editorial team can work in their preferred language. Locales determine which languages appear in the interface, while translations provide the text displayed for each key in a locale.

This guide targets project maintainers customizing the admin experience from the application codebase. All examples modify the configuration exported from `/src/admin/app` file, which Strapi loads when the admin panel builds. You'll learn how to declare additional locales and how to extend Strapi or plugin translations when a locale is missing strings.

## Defining locales

To update the list of available locales in the admin panel, set the `config.locales` array in `src/admin/app` file:

</Tabs>

:::note Notes

- The `en` locale cannot be removed from the build as it is both the fallback (i.e. if a translation is not found in a locale, the `en` will be used) and the default locale (i.e. used when a user opens the administration panel for the first time).
- The full list of available locales is accessible on 

</Tabs>

A plugin's key/value pairs are declared independently in the plugin's files at `/admin/src/translations/[language-name].json`. These key/value pairs can similarly be extended in the `config.translations` key by prefixing the key with the plugin's name (i.e. `[plugin name].[key]: 'value'`) as in the following example:

</Tabs>

If you need to ship additional translation JSON files—for example to organize large overrides or to support a locale not bundled with Strapi—place them in the `/src/admin/extensions/translations` folder and ensure the locale code is listed in `config.locales`.

:::tip Rebuild the admin
Translation changes apply when the admin rebuilds. If updates don’t show, re-run your dev server or rebuild the admin to refresh bundled translations.
:::