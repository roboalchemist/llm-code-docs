# Source: https://vueform.com/docs/input-mask

Title: Input Mask | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/input-mask

Markdown Content:
Learn how to add masks to input fields.

Plugin Installation [​](https://vueform.com/docs/input-mask#plugin-installation)
--------------------------------------------------------------------------------

Input mask can be added to Vueform's `TextElement` field by installing [`@vueform/plugin-mask`](https://github.com/vueform/plugin-mask) plugin.

First, let's install the plugin:

npm yarn pnpm bun

bash

`npm install @vueform/plugin-mask`

bash

`yarn add @vueform/plugin-mask`

bash

`pnpm install @vueform/plugin-mask`

bash

`bun install @vueform/plugin-mask`

After that, we need to add the plugin to `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import PluginMask from '@vueform/plugin-mask'

export default defineConfig({
  plugins: [
    PluginMask,
  ]
})
```

We can test if the plugin has been succefully installed by adding `mask` prop to a `TextElement`:

vue

`<TextElement mask="+1 (000)-000-0000" />`

Usage [​](https://vueform.com/docs/input-mask#usage)
----------------------------------------------------

Masks can only be used with `inputType: 'text'` which is the default type of `TextElement`.

DO:

vue

```
<TextElement mask="..." ... />
<TextElement input-type="text" mask="..." ... />
```

DON'T:

vue

```
<TextElement input-type="number" mask="..." ... />
<TextElement input-type="week" mask="..." ... />
<TextElement input-type="date" mask="..." ... />
<!-- ... -->
```

Placeholder [​](https://vueform.com/docs/input-mask#placeholder)
----------------------------------------------------------------

Mask placeholders are **invisible** by default. We can make them visible by setting `placeholder: true`:

vue

```
<TextElement mask="+1 (000)-000-0000" /> <!-- placeholder: false -->
<TextElement :mask="{ mask: '+1 (000)-000-0000', placeholder: true }" />
```

> Mask placeholders are different from the element's [`placeholder`](https://vueform.com/reference/text-element#option-placeholder) option. Mask placeholders represent the mask format and are always visible when the user types, while element placeholder describe what kind of information the user should type and disappear when the input has value.

##### Placeholder Character [​](https://vueform.com/docs/input-mask#placeholder-character)

We can change the placeholder character by replacing `placeholderChar`:

vue

`<TextElement :mask="{ mask: '+1 (000)-000-0000', placeholderChar: '#', placeholder: true }" />`

Unmasked Value [​](https://vueform.com/docs/input-mask#unmasked-value)
----------------------------------------------------------------------

By default the element value will be pick up the mask format, including any extra characters it may have. We can disable this and **only have the input entered by the user** as the element's value by setting `unmasked` prop:

vue

```
<TextElement mask="+1 (000)-000-0000" /> <!-- unmask: false -->
<TextElement mask="+1 (000)-000-0000" unmask />
```

> When using `unmask` the element value may be provided as **masked** or **unmasked** value when loading/updating data, either like `6502530000` or `+1 (650)-253-0000` and it will be automatically **converted to the unmasked** value.

Overwrite Mode [​](https://vueform.com/docs/input-mask#overwrite-mode)
----------------------------------------------------------------------

By default the entered value is shifted when the user is typing. This means that if they already have a string of `abcd` and the click between `b` and `c` and add an `x` it will become `abxcd`.

If overwrite mode is enabled with `overwrite: true`, the same action would result in `abxd`.

vue

```
<TextElement mask="aaaaa" /> <!-- overwrite: false -->
<TextElement :mask="{ mask: 'aaaaa', overwrite: true }" />
```

Secure Entry [​](https://vueform.com/docs/input-mask#secure-entry)
------------------------------------------------------------------

We might replace the entered characters to hide input value upon typing (much like `password` input type does):

vue

`<TextElement :mask="{ mask: '000000', displayChar: '#' }" ... />`

Number [​](https://vueform.com/docs/input-mask#number)
------------------------------------------------------

Number mask can be used to restrict input to integer or decimal numbers.

vue

```
<TextElement :mask="{
  mask: 'number',

  /**
   * Optional params (with defaults)
  */
  thousandsSeparator: '',     // any single char
  scale: 2,                   // digits after fractional delimiter, 0 for integers
  padFractionalZeros: false,  // pads zeros at end to the length of scale
  normalizeZeros: true,       // removes zeros at ends (eg. 1,10 -> 1,1)
  radix: ',',                 // fractional delimiter
  mapToRadix: ['.'],          // symbols to process as radix
  min: -10000,                // minimum allowed value
  max: 10000,                 // maximum allowed value
  autofix: true,              // replace with min/max value if outside of range
}" ... />
```

Range [​](https://vueform.com/docs/input-mask#range)
----------------------------------------------------

Range mask can be used to restrict input to a number range.

vue

```
<TextElement :mask="{
  mask: 'range',
  from: 1,        // minimum allowed value
  to: 90,         // maximum allowed value
  
  /**
   * Optional params
  */
  maxLength: 3,   // smaller values will pad zeros at start
  autofix: true,  // replace with min/max value if outside of range
}" ... />
```

Enum [​](https://vueform.com/docs/input-mask#enum)
--------------------------------------------------

Enum mask can be used to restrict input within characters enum with **autocomplete**.

vue

```
<TextElement :mask="{
  mask: 'enum',
  enum: [              
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ],
  
  /**
   * Optional params (with defaults)
  */
  caseInsensitive: true, // use case insensitive match
}" ... />
```

Pattern [​](https://vueform.com/docs/input-mask#pattern)
--------------------------------------------------------

Pattern masks are useful when the mask needs to match a certain **pattern** and is more or less **fixed in size**.

Here's an example of a **US SSN** (Social Security Number) input:

vue

`<TextElement name="ssn" mask="000-00-0000" placeholder="000-00-0000" />`

#### Allow Incomplete [​](https://vueform.com/docs/input-mask#allow-incomplete)

By default the element's value will be only fulfilled if the input value matches the **full string**. This can be disabled with `allowIncomplete` option:

vue

`<TextElement name="ssn" :mask="{ mask: '000-00-0000', placeholder: true }" allow-incomplete ... />`

### Tokens [​](https://vueform.com/docs/input-mask#tokens)

The pattern mask can use the following tokens:

*   `0` - any digit
*   `a` - any letter
*   `*` - any char

The following pattern should match **any 4 characters** followed by **4 letters** and **4 digits**:

Custom Tokens can be created as we will learn [later on](https://vueform.com/docs/input-mask#custom-tokens).

### Modifiers [​](https://vueform.com/docs/input-mask#modifiers)

Modifiers can add special behavior to mask patterns:

*   `[]` - make input optional
*   `{}` - include fixed part in unmasked value
*   ``` - _(backtick)_ prevent symbols shift back

#### [] - conditional [​](https://vueform.com/docs/input-mask#conditional)

Makes a part of the pattern optional.

vue

`<TextElement mask="[aa]0000" ... />`

#### {} - include in unmasked value [​](https://vueform.com/docs/input-mask#include-in-unmasked-value)

Makes a part of the pattern included in [umasked value](https://vueform.com/docs/input-mask#unmasked-value).

vue

```
<TextElement mask="+1 (000)-000-0000" unmask ... />
<TextElement mask="{+1} (000)-000-0000" unmask ... />
```

> When not using `unmask` all characters of the mask are included in the value.

#### ` - prevent shift back [​](https://vueform.com/docs/input-mask#prevent-shift-back)

Anything entered **after** this character will not be shifted back when the user removes a character before it.

vue

```
<TextElement mask="000-000" ... /> <!-- allow shift back -->
<TextElement mask="000-`000" ... /> <!-- prevent shift back -->
```

### Fixed Characters [​](https://vueform.com/docs/input-mask#fixed-characters)

Any character that is not defined as a token will be **fixed** in the pattern:

vue

```
<TextElement mask="DE89 0000 0000 0000 00" ... />
         <!-- Fixed^^^^ ^^^^^^^^^^^^^^^^^Pattern -->
```

### Escape Tokens [​](https://vueform.com/docs/input-mask#escape-tokens)

Tokens can be escaped by double backslash `\\`:

vue

```
<TextElement mask="GE29 NB\\0\\0 0000 0000 0000 00" ... />
         <!-- Fixed^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^Pattern -->
```

### Eager Mode [​](https://vueform.com/docs/input-mask#eager-mode)

When a mask contains fixed characters after the start of the string we can decide whether they should be displayed **after the last character** or **before the next character** is typed in.

If `false` (default) the fixed character will only be displayed before the next character is typed. If `true` the fixed characters will be displayed after the previous character is typed.

vue

```
<TextElement mask="GE00 NB\0\0 0000 0000 0000 00" ... /> <!-- eager: false -->
<TextElement :mask="{ mask: 'GE00 NB\\0\\0 0000 0000 0000 00', eager: true }" ... />
```

### Custom Tokens [​](https://vueform.com/docs/input-mask#custom-tokens)

We can create custom tokens by using `definitions` object:

vue

```
<TextElement :mask="{
  mask: '#hhhhhh',
  definitions: {
    'h': /[0-9a-fA-F]/ // Regex or another token
  }
}" ... />
```

The **key** of the definition should be a single character and the **value** can be another **token** or a **regex** that the token will be tested against.

#### Register Custom Tokens Globally [​](https://vueform.com/docs/input-mask#register-custom-tokens-globally)

Custom tokens can be registered globally by passing them to the mask plugin:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import PluginMask from '@vueform/plugin-mask'

export default defineConfig({
  plugins: [
    PluginMask({
      definitions: {
        'h': /[0-9a-fA-F]/
      },
    }),
  ],
})
```

After we registered a token globally we can use it as a regular token in our patterns:

vue

`<TextElement mask="#hhhhhh" ... />`

### Custom Blocks [​](https://vueform.com/docs/input-mask#custom-blocks)

Custom blocks are different from [Custom Tokens](https://vueform.com/docs/input-mask#custom-tokens) as they can represent more complex masks, not just single characters. Think about them as nested masks, where different parts of the original mask can have different "submasks".

vue

```
<TextElement :mask="{
  mask: 'Ple\\ase fill ye\\ar 19YY, month MM',
  placeholder: true,  // make placeholder always visible
  blocks: {
    YY: {
      mask: '00',
    },
    MM: {
      mask: 'enum',
      enum: [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
      ],
    }
  }
}" ... />
```

#### Register Custom Blocks Globally [​](https://vueform.com/docs/input-mask#register-custom-blocks-globally)

Custom blocks can be registered globally by passing them to the mask plugin:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import PluginMask from '@vueform/plugin-mask'

export default defineConfig({
  plugins: [
    PluginMask({
      blocks: {
        MM: {
          mask: 'enum',
          enum: [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December',
          ],
        }
      },
    }),
  ],
})
```

### Repeat Pattern [​](https://vueform.com/docs/input-mask#repeat-pattern)

Repeating certain patterns can be achieved using `blocks`:

vue

```
<TextElement :mask="{
  mask: 'VFr',
  blocks: {
    r: {
      repeat: Infinity, // number of times to repeat: Infinity | number | [min, max]
      mask: '-000',
    }
  },
}" ... />
```

The value will only be considered **complete** if only full repeatabled patterns matched.

When using `repeat: [2,4]` the value will be considered complete if the pattern is repeated between **2** and **4** times:

vue

```
<TextElement :mask="{
  mask: 'VFr',
  blocks: {
    r: {
      repeat: [2,4], // number of times to repeast: Infinity | number | [min, max]
      mask: '-000',
    }
  },
}" ... />
```

Regex [​](https://vueform.com/docs/input-mask#regex)
----------------------------------------------------

Regular expressions can be used as mask. When the user types it will be matched against the regex, which means that it needs to accept intermediary states as well.

This is a **correct** regex, as it allows entering one or more numbers, so it intermediary values are accepted:

vue

`<TextElement :mask="/^[a-fA-F0-9]{0,6}$/" ... />`

However this would be an **incorrect** regex, as only the final value is define by the regex and **not** intermediary ones:

vue

```
<!-- Don't do this -->
<TextElement :mask="/^123$/" ... />
```

This regex only accepts `123` as an input but not `1` or `12` so the user won't be able to enter data.

To accept any growing sequence from 0 to 9 we can use a `Function` mask combined with regex:

vue

```
<TextElement :mask="() => ({ mask: value => /^\d*$/.test(value) &&
    value.split('').every((ch, i) => {
      const prevCh = value[i-1];
      return !prevCh || prevCh < ch;
    })
  })" ... />
```

> Always think about intermediary values when using regex mask. In complex cases it might be better to use [Pattern](https://vueform.com/docs/input-mask#pattern) masks.

Date [​](https://vueform.com/docs/input-mask#date)
--------------------------------------------------

Date mask can be used to input dates that are validated against existing dates (eg. don't allow `2023-02-29`).

vue

```
<TextElement :mask="{
  mask: 'date',

  /**
   * Optional params (with defaults)
  */

  // the date pattern
  pattern: 'd.`m.`Y',    

  // blocks for the pattern   
  blocks: {                 
    d: {
      mask: 'range',
      from: 1,
      to: 31,
      maxLength: 2,
    },
    m: {
      mask: 'range',
      from: 1,
      to: 12,
      maxLength: 2,
    },
    Y: {
      mask: 'range',
      from: 1900,
      to: 9999,
    }
  },

  // define Date -> string convertion (required if custom pattern is defined)
  format: (Date) => {         
    let day = Date.getDate()
    let month = Date.getMonth() + 1
    let year = Date.getFullYear()

    return [
      day < 10 ? '0' + day : day,
      month < 10 ? '0' + month : month,
      year,
    ].join('.')
  },

  // define string -> Date convertion (required if custom pattern is defined)
  parse: (str) => {           
    const yearMonthDay = str.split('.')
    return new Date(yearMonthDay[2], yearMonthDay[1] - 1, yearMonthDay[0])
  },

  // min date that can be entered
  min: new Date(1900, 0, 1),  

  // max date that can be entered
  max: new Date(9999, 0, 1),  
}" ... />
```

The date will be validated before the last character is entered. If it would be an invalid date it won't allow the value.

It can be used with date libraries eg. [`moment.js`](https://momentjs.com/) which takes care of formatting:

vue

```
<script setup>
import { ref } from 'vue'

const momentFormat = ref('YYYY/MM/DD HH:mm')
</script>

<TextElement :mask="{
  mask: 'date',
  pattern: momentFormat,
  blocks: {
    YYYY: {
      mask: 'range',
      from: 1900,
      to: 9999
    },
    MM: {
      mask: 'range',
      from: 1,
      to: 12
    },
    DD: {
      mask: 'range',
      from: 1,
      to: 31
    },
    HH: {
      mask: 'range',
      from: 0,
      to: 23
    },
    mm: {
      mask: 'range',
      from: 0,
      to: 59
    }
  },
  format: (date) => moment(date).format(momentFormat),
  parse: (str) => moment(str, momentFormat),
  placeholder: true,
}" ... />
```

> [Blocks can be registered globally](https://vueform.com/docs/input-mask#register-custom-blocks-globally).

Dynamic Masks [​](https://vueform.com/docs/input-mask#dynamic-masks)
--------------------------------------------------------------------

Dynamic mask automatically selects appropriate mask from provided array of masks. Mask with the largest number of fitting characters is selected considering provided masks order.

vue

```
<TextElement :mask="{
  mask: [
    {
      mask: 'rgb(RGB,RGB,RGB)',
      eager: true,
      blocks: {
        RGB: {
          mask: 'range',
          from: 0,
          to: 255
        }
      }
    },
    {
      mask: /^#[0-9a-f]{0,6}$/i
    }
  ]
}" ... />
```

It is also possible to select mask based on how they start:

vue

```
<TextElement :mask="{
  mask: [
    {
      mask: '+0 (000)-000-00-00',
      startsWith: '1',
      placeholder: true,
      country: 'US'
    },
    {
      mask: '+00 00 000 0000',
      startsWith: '36',
      placeholder: true,
      country: 'HU'
    },
    {
      mask: '+00 0000 000000',
      startsWith: '49',
      placeholder: true,
      country: 'DE'
    },
    {
      mask: '+0000000[0000000]',
      startsWith: '',
      country: ''
    }
  ],
}" ... />
```

### Mask Based on Another Element [​](https://vueform.com/docs/input-mask#mask-based-on-another-element)

By specifying `element` in the mask object we can pass a [path](https://vueform.com/reference/text-element#property-path) of an other element which will decide which mask to choose. The masks then have to have a `when` property that basically says "choose this mask when `element`'s value equals this".

Here's an example how we can select phone number formats dynamically based on country:

vue

```
<SelectElement
  name="country"
  placeholder="Select country..."
  default="US"
  :items="{
    US: 'United States',
    HU: 'Hungary',
    DE: 'Germany',
    other: 'Other'
  }"
></SelectElement>
<TextElement name="phone_number" :mask="{
  mask: [
    {
      mask: '+1 (000)-000-00-00',
      placeholder: true,
      when: 'US'
    },
    {
      mask: '+36 00 000 0000',
      placeholder: true,
      when: 'HU'
    },
    {
      mask: '+49 0000 000000',
      placeholder: true,
      when: 'DE'
    },
    {
      mask: '+0000000[0000000]',
      when: ''
    }
  ],
  element: 'country',
}" />
```

There always needs to be a mask with `when: ''` which will be the default mask when a match isn't found.

_(A full list of international phone mask formats can be found [here](https://github.com/vueform/international-phone-masks/blob/main/masks.json).)_

### Customize Mask Selector [​](https://vueform.com/docs/input-mask#customize-mask-selector)

The mask selector can be customized with `dispatch`. Here's the default dispatcher that matched the mask based on `startsWith`:

js

```
{
  mask: [
    // ...
  ],
  dispatch: (appended, dynamicMasked, el$, form$) => {
    const number = (dynamicMasked.value + appended).replace(/\D/g,'')

    return dynamicMasked.compiledMasks.find(m => number.indexOf(m.startsWith) === 0)
  }
}
```

Treeshaking [​](https://vueform.com/docs/input-mask#treeshaking)
----------------------------------------------------------------

The default mask plugin includes several masking features which adds about `15kBs` to the final bundle's gzipped size.

If we don't need all the features we can only include the ones we use:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import IMask from 'imask/holder'
import PluginMask from '@vueform/plugin-mask/plugin'

// remove the ones not needed
import 'imask/masked/date'
import 'imask/masked/number'
import 'imask/masked/dynamic'
import 'imask/masked/enum'
import 'imask/masked/number'
import 'imask/masked/pattern'
import 'imask/masked/range'
import 'imask/masked/regexp'
import 'imask/masked/repeat'
import 'imask/masked/function'

export default defineConfig({
  plugins: [
    PluginMask(
      { /* options */ },
      IMask
    )
  ]
})
```

Advanced [​](https://vueform.com/docs/input-mask#advanced)
----------------------------------------------------------

Vueform's mask plugin is based on [`imaskjs`](https://github.com/uNmAnNeR/imaskjs), a **fantastic** and **well-maintained** library for vanilla javascript input mask by [Alexey Kryazhev](https://github.com/uNmAnNeR).

If more advanced input masks are required, please head to their [official website](https://imask.js.org/) for more info. In general, all the options we pass to our input as `mask` will be passed down to `IMask` as the second argument, so even if a property is not described here, can be used.

The IMask object can be accessed by passing the `mask` as a function with `IMask` param that should return an object with the mask options:

vue

```
<TextElement :mask="(IMask) => ({
  mask: 'enum',
  // ...
})">
```

If the `TextElement` has a `mask` prop, it exposes `Mask` object which is the `IMask` instance:

vue

```
<TextElement mask="..." @change="(newValue, oldValue, el$) => {
  console.log(el$.Mask)
}" >
```

It also exposes the following methods:

*   `destroyMask` - destroys the `IMask` instance
*   `initMask` - inits the `IMask` instance
*   `syncMask` - syncs the `IMask` value with the element `value` and `model`
*   `refreshMask` - reinits the `IMask` instance

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
