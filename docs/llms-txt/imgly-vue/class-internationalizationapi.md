# Class: InternationalizationAPI

Manages localization and internationalization settings for the Creative Editor SDK.

The InternationalisationAPI provides methods to get and set the current locale, as well as add custom translations for the editor interface.

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`InternationalizationAPI`

## Localization[#](#localization)

Methods for managing locale settings and custom translations within the editor.

### getLocale()[#](#getlocale)

  

Gets the currently active locale.

#### Returns[#](#returns)

`string`

The currently set locale as a string, or the fallback locale if none is set.

#### Signature[#](#signature)

```
getLocale(): string
```

* * *

### listLocales()[#](#listlocales)

  

Returns all available locales that have been loaded.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `matcher?`: `string`; } | Optional configuration object with the following properties: - `matcher`: Optional pattern to match against. Use `*` for wildcard matching. |
| `options.matcher?` | `string` | \- |

#### Returns[#](#returns-1)

`string`\[\]

An array of locale strings that have translations available.

#### Example[#](#example)

```
const allLocales = cesdk.i18n.listLocales();console.log('Available locales:', allLocales);// Output: ['en', 'de', 'fr', ...]
// Find all English variants using wildcardconst englishLocales = cesdk.i18n.listLocales({ matcher: 'en*' });console.log('English locales:', englishLocales);// Output: ['en', 'en-US', 'en-GB', ...]
```

#### Signature[#](#signature-1)

```
listLocales(options?: object): string[]
```

* * *

### setLocale()[#](#setlocale)

  

Sets the active locale for the editor interface.

This will **not check** whether translations for the given locale are available.

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `locale` | `string` | The locale string to set as active (e.g., ‘en’, ‘de’, ‘fr’). |

#### Returns[#](#returns-2)

`void`

* * *

### setTranslations()[#](#settranslations)

  

Adds custom translations for the editor interface.

This method allows you to provide custom translations that will be used by the editor interface. Translations are organized by locale and can override or extend the default editor translations.

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `definition` | `Partial`<`Record`<`string`, `Partial`<[`Translations`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/translations/)\>>> | An object mapping locale strings to translation objects. |

#### Returns[#](#returns-3)

`void`

#### Example[#](#example-1)

```
setTranslations({ en: {   presets: {     scene: ...   } }})
```

#### Signature[#](#signature-2)

```
setTranslations(definition: Partial<Record<string, Partial<Translations>>>): void
```

* * *

### getTranslations()[#](#gettranslations)

  

Retrieves the translations for the specified locales.

This method returns the translations for the given locales, or all available translations if no specific locales are provided.

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `locales?` | `string`\[\] | An optional array of locale strings to retrieve translations for. |

#### Returns[#](#returns-4)

`Partial`<`Record`<`string`, `Partial`<[`Translations`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/translations/)\>>>

An object mapping locale strings to their respective translations.

#### Signature[#](#signature-3)

```
getTranslations(locales?: string[]): Partial<Record<string, Partial<Translations>>>
```

* * *

### translate()[#](#translate)

  

Translates a key or array of keys to the current locale.

This method retrieves the translation for the given key(s) in the currently active locale. When an array of keys is provided, the first key that has a translation will be used. If no translation is found for any of the provided keys, the last key in the array (or the single key if a string is provided) will be returned as the fallback value.

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | `string`\[\] |

#### Returns[#](#returns-5)

`string`

The translated string for the key in the current locale, or the key itself if no translation is found.

#### Example[#](#example-2)

```
// Single keyconst translation = cesdk.i18n.translate('common.save');// Returns: "Save" (if translation exists) or "common.save" (if not found)
// Array of keys (fallback)const translation = cesdk.i18n.translate(['specific.save', 'common.save']);// Tries 'specific.save' first, then 'common.save'// Returns the first found translation or "common.save" if neither exists
```

#### Signature[#](#signature-4)

```
translate(key: string | string[]): string
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/classes/featureapi)