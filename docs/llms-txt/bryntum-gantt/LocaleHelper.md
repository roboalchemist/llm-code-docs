# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/localization/LocaleHelper.md

# [LocaleHelper](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper)

Thin class which provides locale management methods. Class doesn't import other API classes and can be used separately for publishing locales before importing product classes.

Locale should be published with [publishLocale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleHelper#function-publishLocale-static) method before it is available for localizing of Bryntum API classes and widgets.

Example:

```
LocaleHelper.publishLocale({
    localeName : 'En',
    localeDesc : 'English (US)',
    localeCode : 'en-US',
    ... (localization key:value pairs)
});
```

or for asynchronous loading from remote path on applying locale

```
LocaleHelper.publishLocale({
    localeName : 'En',
    localeDesc : 'English (US)',
    localeCode : 'en-US',
    localePath : 'https://my-server/localization/en.js'
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[locales](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#property-locales-static)
Get/set currently published locales. Returns an object with locales.

Example:

```
const englishLocale = LocaleHelper.locales.En;
```

`englishLocale` contains [Locale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleHelper#typedef-Locale) object.

[localeName](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#property-localeName-static)
Get/set current locale name. Defaults to "En"

[locale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#property-locale-static)
Get current locale config specified by [localeName](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleHelper#property-localeName-static). If no current locale specified, returns default `En` locale or first published locale or empty locale object if no published locales found.

## Functions

Functions are methods available for calling on the class

[mergeLocales](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#function-mergeLocales-static)
Merges all properties of provided locale objects into new locale object. Locales are merged in order they provided and locales which go later replace same properties of previous locales.

[trimLocale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#function-trimLocale-static)
Removes all properties from `locale` that are present in the provided `toTrim`.

[normalizeLocale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#function-normalizeLocale-static)
Normalizes locale object to [Locale](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleHelper#typedef-Locale) type.

Supported configs:

```
LocaleHelper.normalizeLocale({
    localeName : 'En',
    localeDesc : 'English (US)',
    localeCode : 'en-US',
    ... (localization key:value pairs)
});
```

and for backward compatibility

```
LocaleHelper.normalizeLocale('En', {
    name : 'En',
    desc : 'English (US)',
    code : 'en-US',
    locale : {
        ... (localization key:value pairs)
    }
});
```

[publishLocale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#function-publishLocale-static)
Publishes a locale to make it available for applying. Published locales are available in [locales](https://bryntum.com/docs/gantt/api/#Core/localization/LocaleHelper#property-locales-static).

Recommended usage:

```
LocaleHelper.publishLocale({
    localeName : 'En',
    localeDesc : 'English (US)',
    localeCode : 'en-US',
    ... (localization key:value pairs)
});
```

for backward compatibility (prior to `5.3.0` version):

```
LocaleHelper.publishLocale('En', {
    name : 'En',
    desc : 'English (US)',
    code : 'en-US',
    locale : {
        ... (localization key:value pairs)
    }
});
```

Publishing a locale will automatically merge it's localization keys with existing locale matching by locale name, replacing existing one with new. To replace existing locale entirely pass `true` to optional `config` parameter.

Example:

```
LocaleHelper.publishLocale({
    localeName : 'En',
    localeDesc : 'English (US)',
    localeCode : 'en-US',
    ... (localization key:value pairs)
}, true);
```

## Typedefs

Typedefs are type definitions for the class

[LocaleKeys](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#typedef-LocaleKeys)
Object which contains `key: value` localization pairs. Key value may have `String`, `Function`, `LocaleKeys` or `Object` type.

Example:

```
{
    title   : 'Title',
    count   : number => `Count is ${number}`,
    MyClass : {
       foo : 'bar'
    }
}
```

[Locale](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#typedef-Locale)
Locale configuration object which contains locale properties alongside with localization pairs.

Example:

```
 {
    localeName : 'En',
    localeDesc : 'English (US)',
    localeCode : 'en-US',
    ... (localization key:value pairs)
}
```

[Locales](https://bryntum.com/docs/gantt/api/Core/localization/LocaleHelper#typedef-Locales)
Object which contains locales. Each object key represents published locale by its `localeName`.

Example:

```
// This returns English locale.
const englishLocale = LocaleHelper.locales.En;
```
