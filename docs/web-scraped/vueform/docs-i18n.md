# Source: https://vueform.com/docs/i18n

Title: I18n (internationalization) | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/i18n

Markdown Content:
Learn how to internationalize everything including the contents of your forms.

Using Locales [​](https://vueform.com/docs/i18n#using-locales)
--------------------------------------------------------------

Vueform comes with a built-in translation engine that handles different locales.

We can import locales from `@vueform/vueform/locales` directory, which we can add in [`vueform.config.js`](https://vueform.com/docs/configuration#locales):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import en from '@vueform/vueform/locales/en'

export default defineConfig({
  locale: 'en',
  locales: { en },
  // ...
})
```

We also need to set the locale that should be used by default with [`locale`](https://vueform.com/docs/configuration#locale) option.

### Customizing Locale [​](https://vueform.com/docs/i18n#customizing-locale)

To add or replace tags in a local, simply override its value in the locale object. For example here's how we can replace the label of list's **add button**:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import en from '@vueform/vueform/locales/en'

en.vueform.elements.list.add = 'Add item'

export default defineConfig({
  locales: { en },
  // ...
})
```

If we'd like replace a whole locale file we can copy `./node_modules/@vueform/vueform/locales/en/index.mjs` to our project folder, eg. `./vueform/locales/en.js`.

We can use the custom version after by including that one instead of the official:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import en from './vueform/locales/en'

export default defineConfig({
  locales: { en },
  locale: 'en',
  // ...
})
```

### Switching Locale [​](https://vueform.com/docs/i18n#switching-locale)

To switch a locale we can pass a `locale` option to Vueform upon installation:

js

```
import Vue from 'vue'
import Vueform from '@vueform/vueform'
import vueformConfig from './../vueform.config'

Vue.use(Vueform, {
  ...vueformConfig,
  locale: 'de'
})
```

To use a locale you need to include it first in [`vueform.config.js`](https://vueform.com/docs/configuration#locales)'s `locales` object:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import en from '@vueform/vueform/locales/en'
import de from '@vueform/vueform/locales/de'
import nl from '@vueform/vueform/locales/nl'

export default defineConfig({
  locale: 'en',
  locales: {
    en,
    de,
    nl,
  },
  // ...
})
```

#### Switching Locale Using Options API [​](https://vueform.com/docs/i18n#switching-locale-using-options-api)

We can switch locale anywhere in our application using the global `this.$vueform.i18n.locale` object in Options API:

js

```
mounted() {
  this.$vueform.i18n.locale = 'de'
}
```

#### Switching Locale Using Composition API [​](https://vueform.com/docs/i18n#switching-locale-using-composition-api)

From version `1.3.1` we can `inject` the global `$vueform` object in any `setup()` method and override the locale there using Composition API:

js

```
setup() {
  const $vueform = inject('$vueform')

  $vueform.value.i18n.locale = 'de'
}
```

#### Switching Locale Before Version 1.3.1 [​](https://vueform.com/docs/i18n#switching-locale-before-version-1-3-1)

Before `@vueform/vueform@1.3.1` you needed to add the locale as `key` to each Vueform component upon switching locale, eg: `<Vueform :key="locale">`.

### Adding Locale [​](https://vueform.com/docs/i18n#adding-locale)

To create a new locale copy `./node_modules/@vueform/vueform/locales/zh_TW/index.mjs` to your project folder, eg. `./vueform/locales/zh_HK.js`.

After the translation tags have been translated we can add it in `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import en from '@vueform/vueform/locales/en'
import zh_HK from './vueform/locales/zh_HK'

export default defineConfig({
  locale: 'en',
  locales: {
    en,
    zh_HK
  },
  // ...
})
```

Available Locales [​](https://vueform.com/docs/i18n#available-locales)
----------------------------------------------------------------------

Vueform is currently available in the following languages:

*   `bg` - Bulgarian 🇧🇬
*   `cs` - Czech 🇨🇿
*   `zh_CN` - Chinese (Simplified) 🇨🇳
*   `zh_TW` - Chinese (Traditional) 🇹🇼
*   `da` - Danish 🇩🇰
*   `nl` - Dutch 🇳🇱
*   `en` - English 🇺🇸
*   `fr` - French 🇫🇷
*   `fr_CA` - French (Canada) 🇨🇦
*   `de` - German 🇩🇪
*   `el` - Greek 🇬🇷
*   `hu` - Hungaian 🇭🇺
*   `id` - Indonesian 🇮🇩
*   `it` - Italian 🇮🇹
*   `ja` - Japanese 🇯🇵
*   `ko` - Korean 🇰🇷
*   `pt` - Portuguese 🇵🇹
*   `pt_BR` - Portuguese (Brazil) 🇧🇷
*   `ro` - Romanian 🇷🇴
*   `ru` - Russian 🇷🇺
*   `sk` - Slovak 🇸🇰
*   `es` - Spanish 🇪🇸
*   `sv` - Swedish 🇸🇪
*   `tr` - Turkish 🇹🇷
*   `uk` - Ukrainian 🇺🇦

Translating Element Properties [​](https://vueform.com/docs/i18n#translating-element-properties)
------------------------------------------------------------------------------------------------

Certain element options can be provided in multiple locales and the one that matches the current locale will be used.

Let's take `label` as an example:

js

```
const schema = ref({
  birthday: {
    type: 'date',
    label: {
      en: 'Birthday',
      de: 'Geburtstag',
    },
  }
})
```

As we can see the `label` is provided as an `object` with `en` and `de` keys. This means that if Vueform's locale is **English** then **Birthday** will be used, and if it's **German** then **Geburtstag** will be used.

Options that can be localized are indicated in their component reference by "**Localizable: `true`**" like [`label`](https://vueform.com/reference/date-element#option-label) for `DateElement`.

Translating Dates [​](https://vueform.com/docs/i18n#translating-dates)
----------------------------------------------------------------------

When we use [`DateElement`](https://vueform.com/reference/date-element) or [`DatesElement`](https://vueform.com/reference/dates-element) we rely upon the locale to determine date format.

In the locale file look for `vueform.dateFormats` object which contains different variations of date formatting tags depending on what parts of a date our element displays.

Here's the default configuration from `@vueform/vueform/locales/en/index.mjs`:

js

```
// @vueform/vueform/locales/en/index.mjs

export default {
  vueform: {
    // ...
    dateFormats: {
      // date: true, time: true, seconds: true, hour24: true
      datetimeSeconds24: 'YYYY-MM-DD HH:mm:ss', 

      // date: true, time: true, seconds: true, hour24: false
      datetimeSeconds12: 'YYYY-MM-DD hh:mm:ss a',

      // date: true, time: true, seconds: false, hour24: true
      datetime24: 'YYYY-MM-DD HH:mm',

      // date: true, time: true, seconds: false, hour24: false
      datetime12: 'YYYY-MM-DD hh:mm a',

      // date: false, time: true, seconds: true, hour24: true
      timeSeconds24: 'HH:mm:ss',

      // date: false, time: true, seconds: true, hour24: false
      timeSeconds12: 'hh:mm:ss a',

      // date: false, time: true, seconds: false, hour24: true
      time24: 'HH:mm',

      // date: false, time: true, seconds: false, hour24: false
      time12: 'hh:mm a',

      // date: true, time: false
      date: 'YYYY-MM-DD',
    },
    // ...
  },
  // ...
}
```

### Date Formatting Tokens [​](https://vueform.com/docs/i18n#date-formatting-tokens)

Here are the list of formatting tags available, based on [moment.js](https://momentjs.com/):

| Input | Example | Description |
| --- | --- | --- |
| Year |  |  |
| `YYYY` | `2014` | 4 or 2 digit year. Note: Only 4 digit can be parsed on strict mode |
| `YY` | `14` | 2 digit year |
| `Y` | `-25` | Year with any number of digits and sign |
| `Q` | `1..4` | Quarter of year. Sets month to first month in quarter. |
| Month |  |  |
| `M MM` | `1..12` | Month number |
| `MMM MMMM` | `Jan..December` | Month name in locale set by moment.locale() |
| Week |  |  |
| `gggg` | `2014` | Locale 4 digit week year |
| `gg` | `14` | Locale 2 digit week year |
| `w ww` | `1..53` | Locale week of year |
| `e` | `0..6` | Locale day of week |
| `ddd dddd` | `Mon...Sunday` | Day name in locale set by moment.locale() |
| `GGGG` | `2014` | ISO 4 digit week year |
| `GG` | `14` | ISO 2 digit week year |
| `W WW` | `1..53` | ISO week of year |
| `E` | `1..7` | ISO day of week |
| Day |  |  |
| `D DD` | `1..31` | Day of month |
| `Do` | `1st..31st` | Day of month with ordinal |
| `DDD DDDD` | `1..365` | Day of year |
| Time |  |  |
| `H HH` | `0..23` | Hours (24 hour time) |
| `h hh` | `1..12` | Hours (12 hour time used with a A.) |
| `k kk` | `1..24` | Hours (24 hour time from 1 to 24) |
| `a A` | `am pm` | Post or ante meridiem (Note the one character a p are also considered valid) |
| `m mm` | `0..59` | Minutes |
| `s ss` | `0..59` | Seconds |
| `S SS SSS ... SSSSSSSSS` | `0..999999999` | Fractional seconds |
| Timestamp |  |  |
| `X` | `1410715640.579` | Unix timestamp |
| `x` | `1410715640579` | Unix ms timestamp |

Translating Elements [​](https://vueform.com/docs/i18n#translating-elements)
----------------------------------------------------------------------------

Elements that start with `T` or `t-` (eg. [`TTextElement`](https://vueform.com/reference/t-text-element) or [`t-textarea-element`](https://vueform.com/reference/t-textarea-element)) are translatable elements that can have multiple values in different languages.

For example:

vue

```
<template>
  <Vueform multilingual>
    <TTextElement name="title" placeholder="Title" />
    <TEditorElement name="description" placeholder="Description" />
  </Vueform>
</template>
```

By enabling `multilingual`, the [`FormLanguages`](https://vueform.com/reference/form-languages) component will appear above the form, which allows us to choose the language of the translatable elements within the form.

### Adding Languages [​](https://vueform.com/docs/i18n#adding-languages)

By default the `languages` and the initially selected `langage` are based on values defined in [`vueform.config.js](https://vueform.com/docs/configuration#languages):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  languages: { // available languages
    en: 'English',
    zh: 'Chinese',
  },
  language: 'en' // initially selected language
})
```

We can customize languages and initial language on form level using [`languages`](https://vueform.com/docs/configuration#languages) and [`language`](https://vueform.com/docs/configuration#language) option:

template

```
<template>
  <Vueform multilingual language="zh" :languages="{
    en: 'English',
    zh: 'Chinese',
    nl: 'Dutch',
  }">
    <TTextElement name="title" placeholder="Title" />
    <TEditorElement name="description" placeholder="Description" />
  </Vueform>
</template>
```

Vueform has the following translatable elements:

*   [`TTextElement`](https://vueform.com/reference/t-text-element)
*   [`TTextareaElement`](https://vueform.com/reference/t-textarea-element)
*   [`TEditorElement`](https://vueform.com/reference/t-editor-element)

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
