# Source: https://vueform.com/docs/configuration

Title: Configuration | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/configuration

Markdown Content:
Learn how to configure Vueform.

Project Configuration [​](https://vueform.com/docs/configuration#project-configuration)
---------------------------------------------------------------------------------------

To create a configuration file follow the steps in our [Installation Guide](https://vueform.com/docs/installation#installation).

After that, we can `vueform.config.js` to set global configuration options:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import vueform from '@vueform/vueform/themes/vueform'
import en from '@vueform/vueform/locales/en'

export default defineConfig({
  theme: vueform,
  locales: { en },
  locale: 'en',
})
```

The configuration should at least contain a [`theme`](https://vueform.com/docs/configuration#theme), [`locales`](https://vueform.com/docs/configuration#locales) and [`locale`](https://vueform.com/docs/configuration#locale) options.

Configuration Options [​](https://vueform.com/docs/configuration#configuration-options)
---------------------------------------------------------------------------------------

Here is the list of available configuration options.

### env [​](https://vueform.com/docs/configuration#env)

*   Type: `string`
*   Default: `development`

The environment variable. Possible values: `production|development`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  env: 'production',
  // ...
})
```

### expressions [​](https://vueform.com/docs/configuration#expressions)

*   Type: `object`
*   Default: `{}`

Custom functions and consts for [expressions](https://vueform.com/docs/expressions#adding-custom-functions-and-constants).

js

```
import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  expression: {
    functions: {
      CUSTOM_FUNC(arg1, arg2, ...) {
        return 'return value'
      },
      DYNAMIC_FUNC: (form$) => (path) => {
        return form$.el$(path)?.label // returns the label of an element by path
      },
    },
    consts: {
      CUSTOM_CONST: 'const value',
    }
  }
},
```

### expressionDebug [​](https://vueform.com/docs/configuration#expressiondebug)

*   Type: `boolean`
*   Default: `false`

Whether expressions should display warning and errors.

js

```
import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  expressionDebug: true
},
```

### plugins [​](https://vueform.com/docs/configuration#plugins)

*   Type: `array`
*   Default: `[]`

Registers plugins.

js

```
// vueform.config.js

import { defineConfig, plugin } from '@vueform/vueform'

export default defineConfig({
  plugins: [
    plugin({
      apply: /^.*Element/,
      setup(props, context, component) {
        // ...
      }
    })
  ]
  // ...
})
```

Learn more about plugins [here](https://vueform.com/docs/plugins).

### elements [​](https://vueform.com/docs/configuration#elements)

*   Type: `array`
*   Default: `[]`

Registers custom elmenets.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import RatingElement from './path/to/RatingElement.vue'

export default defineConfig({
  elements: [
    RatingElement,
  ]
  // ...
})
```

Learn more about creating elements [here](https://vueform.com/docs/creating-elements).

### components [​](https://vueform.com/docs/configuration#components)

*   Type: `object`
*   Default: `{}`

Components to register when tree-shaking.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

import {
  EditorWrapper,
  EditorElement,
} from '@vueform/vueform/core'

export default defineConfig({
  components: [
    EditorWrapper,
    EditorElement,
  ]
  // ...
})
```

Learn more about tree-shaking [here](https://vueform.com/docs/tree-shaking).

### theme [​](https://vueform.com/docs/configuration#theme)

*   Type: `object`
*   Default: `{}`
*   Required: `true`

A theme contains templates, classes and styles for all Vueform components. Currently available themes are `vueform` and `tailwind`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import vueform from '@vueform/vueform/themes/vueform'

export default defineConfig({
  theme: vueform,
  // ...
})
```

Learn more about available themes [here](https://vueform.com/themes/tailwind).

### templates [​](https://vueform.com/docs/configuration#templates)

*   Type: `object`
*   Default: `{}`

Globally replaces component templates provided by the [`theme`](https://vueform.com/docs/configuration#theme).

For example here's how we can replace the template of [`ElementDescription`](https://vueform.com/docs/element-description) component:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import CustomElementDescription from '/path/to/custom/CustomElementDescription.vue'

export default defineConfig({
  templates: {
    ElementDescription,
  }
  // ...
})
```

Learn more about overriding templates [here](https://vueform.com/docs/styles-and-layout#templates).

### views [​](https://vueform.com/docs/configuration#views)

*   Type: `object`
*   Default: `{}`

The default views for each component.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  views: {
    CheckboxgroupCheckbox: 'tabs'
  },
  // ...
})
```

Learn more about views [here](https://vueform.com/docs/styles-and-layout#views).

### size [​](https://vueform.com/docs/configuration#size)

*   Type: `string`
*   Default: `md`

The default size of components.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  size: 'lg',
  // ...
})
```

Learn more about size [here](https://vueform.com/docs/styles-and-layout#size).

### classHelpers [​](https://vueform.com/docs/configuration#classhelpers)

*   Type: `boolean`
*   Default: `false`

Enables class helpers unless `env` is `production`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  classHelpers: true,
  // ...
})
```

Learn more about class helpers [here](https://vueform.com/docs/styles-and-layout#class-helpers).

### addClasses [​](https://vueform.com/docs/configuration#addclasses)

*   Type: `object`
*   Default: `{}`

Globally add classes to components provided by theme [`theme`](https://vueform.com/docs/configuration#theme).

For example here's how we can add a class to the `container` class of [`ElementDescription`](https://vueform.com/docs/element-description):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  addClasses: {
    ElementDescription: {
      container: 'added-class',
    },
  },
  // ...
})
```

Learn more about adding classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### removeClasses [​](https://vueform.com/docs/configuration#removeclasses)

*   Type: `object`
*   Default: `{}`

Globally removes classes from components provided by theme [`theme`](https://vueform.com/docs/configuration#theme).

For example here's how we can remove a class from the `container` class of [`ElementDescription`](https://vueform.com/docs/element-description):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  removeClasses: {
    ElementDescription: {
      container: 'text-gray-500',
    },
  },
  // ...
})
```

Learn more about removing classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### replaceClasses [​](https://vueform.com/docs/configuration#replaceclasses)

*   Type: `object`
*   Default: `{}`

Globally replaces component classes provided by theme [`theme`](https://vueform.com/docs/configuration#theme).

For example here's how we can replace a class from the `container` class of [`ElementDescription`](https://vueform.com/docs/element-description):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  replaceClasses: {
    ElementDescription: {
      container: {
        'text-gray-500': 'text-green-500'
      },
    },
  },
  // ...
})
```

Learn more about replacing classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### overrideClasses [​](https://vueform.com/docs/configuration#overrideclasses)

*   Type: `object`
*   Default: `{}`

Globally overrides component classes provided by theme [`theme`](https://vueform.com/docs/configuration#theme).

For example here's how we can override the `container` class of [`ElementDescription`](https://vueform.com/docs/element-description):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  overrideClasses: {
    ElementDescription: {
      container: 'text-green-500',
    },
  },
  // ...
})
```

Learn more about overriding classes [here](https://vueform.com/docs/styles-and-layout#modify-multiple-components).

### presets [​](https://vueform.com/docs/configuration#presets)

*   Type: `object`
*   Default: `{}`

Preset definitions.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  presets: {
    presetName: {
      addClasses: {
        // ...
      },
      templates: {
        // ...
      },
      // ...
    }
  }
  // ...
})
```

Learn more about presets [here](https://vueform.com/docs/styles-and-layout#presets).

### usePresets [​](https://vueform.com/docs/configuration#usepresets)

*   Type: `array`
*   Default: `[]`

The list of presets to apply globally.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  usePresets: ['preset1', 'preset2'],
  // ...
})
```

Learn more about presets [here](https://vueform.com/docs/styles-and-layout#presets).

### columns [​](https://vueform.com/docs/configuration#columns)

*   Type: `object`
*   Default: `{ container: 12, label: 12, wrapper: 12 }`

Sets the default column sizes globally.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  columns: {
    container: 12,
    label: 3,
    wrapper: 12,
  }
  // ...
})
```

Learn more about columns [here](https://vueform.com/docs/styles-and-layout#columns).

### forceLabels [​](https://vueform.com/docs/configuration#forcelabels)

*   Type: `boolean`
*   Default: `false`

Sets globally whether empty labels should be displayed for elements.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  forceLabels: true,
  // ...
})
```

### floatPlaceholders [​](https://vueform.com/docs/configuration#floatplaceholders)

*   Type: `boolean`
*   Default: `true`

Sets globally whether floating labels should be automatically created from placeholders (unless they are explicitly defined).

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  floatPlaceholders: false,
  // ...
})
```

### displayErrors [​](https://vueform.com/docs/configuration#displayerrors)

*   Type: `boolean`
*   Default: `true`

Sets globally whether error messages from [`messageBag`](https://vueform.com/docs/vueform#property-message-bag) should be displayed above the form in [`FormErrors`](https://vueform.com/docs/form-errors) component.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  displayErrors: false,
  // ...
})
```

### displayMessages [​](https://vueform.com/docs/configuration#displaymessages)

*   Type: `boolean`
*   Default: `true`

Sets globally whether form messages from [`messageBag`](https://vueform.com/docs/vueform#property-message-bag) should be displayed above the form in [`FormMessages`](https://vueform.com/docs/form-messages) component.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  displayMessages: false,
  // ...
})
```

### languages [​](https://vueform.com/docs/configuration#languages)

*   Type: `object`
*   Default: `{ en: 'English' }`

Sets the availble languages when using [`multilingual: true`](https://vueform.com/docs/vueform#option-multilingual). You can learn more about it at [Translating Elements](https://vueform.com/docs/i18n#translating-elements).

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  languages: {
    en: 'English',
    zh: 'Chinese',
    nl: 'Dutch',
  },
  // ...
})
```

### language [​](https://vueform.com/docs/configuration#language)

*   Type: `string`
*   Default: `en`

Sets the default language when using [`multilingual: true`](https://vueform.com/docs/vueform#option-multilingual).

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  language: 'zh',
  // ...
})
```

### locales [​](https://vueform.com/docs/configuration#locales)

*   Type: `object`
*   Default: `{ }`
*   Required: `true`

Sets the list of available locales. You can learn more about it at [`Using Locales`](https://vueform.com/docs/i18n#using-locales).

The available locales are:

*   `en`

js

```
// vueform.config.js

import { defaultConfig } from '@vueform/vueform'
import { en } from '@vueform/vueform/locales/en'

export default defineConfig({
  locales: {
    en,
  },
  // ...
})
```

### locale [​](https://vueform.com/docs/configuration#locale)

*   Type: `string`
*   Default: `null`
*   Required: `true`

Sets the current locale.

js

```
// vueform.config.js

import { defaultConfig } from '@vueform/vueform'
import { en } from '@vueform/vueform/locales/en'

export default defineConfig({
  locales: {
    en,
  },
  locale: 'en',
  // ...
})
```

### fallbackLocale [​](https://vueform.com/docs/configuration#fallbacklocale)

*   Type: `string`
*   Default: `en`

Sets the fallback locale, which is used when a translation tag is not available in the current [`locale`](https://vueform.com/docs/configuration#locale).

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  fallbackLocale: 'zh',
  // ...
})
```

### orderFrom [​](https://vueform.com/docs/configuration#orderfrom)

*   Type: `number`
*   Default: `1`

Sets globally whether [list order](https://vueform.com/docs/list-element#option-store-order) should start from `0` or `1`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  orderFrom: 0,
  // ...
})
```

### rules [​](https://vueform.com/docs/configuration#rules)

*   Type: `object`
*   Default: `{}`

Registers custom validation rules.

js

```
// vueform.config.js
import uppercase from '/path/to/custom/rules/Uppercase.js'

export default defineConfig({
  rules: {
    uppercase,
  }
  // ...
})
```

Learn more about validation rules [here](https://vueform.com/docs/validating-elements#custom-validation-rules).

### validateOn [​](https://vueform.com/docs/configuration#validateon)

*   Type: `string`
*   Default: `change|step`

Sets globally when the form should trigger validation. Values must be concatenated with |. Possible values: change and step.

If change is present, an element will be validated when its value is changed.

If step is present, all the elements within a step will be validated when the user tries to navigate to the next step using the Next form step control.

The form always validates unvalidated elements before submitting data to the server.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  validateOn: 'step',
  // ...
})
```

### scrollToInvalid [​](https://vueform.com/docs/configuration#scrolltoinvalid)

*   Type: `boolean`
*   Default: `true`

Whether to scroll to the first invalid element when the form gets submitted.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  scrollToInvalid: false,
  // ...
})
```

### showRequired [​](https://vueform.com/docs/configuration#showrequired)

*   Type: `array`
*   Default: `[]`

The list of element assets where an asterisk `*` should be shown if the element has `required` validation rule. The possible items are `label`, `placeholder` and `floating`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  showRequired: ['label', 'placeholder', 'floating'],
  // ...
})
```

### scrollOnNext [​](https://vueform.com/docs/configuration#scrollonnext)

*   Type: `boolean`
*   Default: `true`

Whether to scroll to the top of the form on hitting **Next** button when using [steps](https://vueform.com/docs/breaking-forms-into-steps#using-form-steps).

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  scrollOnNext: false,
  // ...
})
```

### endpoints [​](https://vueform.com/docs/configuration#endpoints)

*   Type: `object`
*   Default: `see below`

Sets default endpoints used by Vueform. Default:

js

```
// Default for `config.endpoints`:

{
  submit: {
    url: '/vueform/process',
    method: 'post',
  },
  uploadTempFile: {
    url: '/vueform/file/upload-temp',
    method: 'post',
  },
  removeTempFile: {
    url: '/vueform/file/remove-temp',
    method: 'post',
  },
  removeFile: {
    url: '/vueform/file/remove',
    method: 'post',
  },
  attachment: {
    url: '/vueform/editor/attachment',
    method: 'post',
  },
  activeUrl: {
    url: '/vueform/validators/active_url',
    method: 'post',
  },
  unique: {
    url: '/vueform/validators/unique',
    method: 'post',
  },
  exists: {
    url: '/vueform/validators/exists',
    method: 'post',
  },
}
```

For example here's how to replace the default form submit endpoint:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    submit: {
      url: '/form/submit',
      method: 'post',
    },
  }
  // ...
})
```

### sanitize [​](https://vueform.com/docs/configuration#sanitize)

*   Type: `boolean`
*   Default: `true`

When enabled, each property that can display HTML (eg. `label`, `description`, etc.) will be sanitized for improved security.

If you want to disable sanitization for some reason, you can set this to `false`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  sanitize: false, // this will disable sanitization
  // ...
})
```

### sanitizeOptions [​](https://vueform.com/docs/configuration#sanitizeoptions)

*   Type: `object`
*   Default: `{}`

The options for [`DOMPurify`](https://github.com/cure53/DOMPurify?tab=readme-ov-file#can-i-configure-dompurify), the underlying sanitization library.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  sanitizeOptions: {
    // This will enable iframes with the listed attributes
    ADD_TAGS: ['iframe'],
    ADD_ATTR: ['allow', 'allowfullscreen', 'frameborder', 'scrolling'],
  },
  // ...
})
```

### sanitizeInit [​](https://vueform.com/docs/configuration#sanitizeinit)

*   Type: `function`
*   Default: `DOMPurify => DOMPurify`

The function that gets executed before sanitization happens. This is where you can eg. subscribe to hooks of [`DOMPurify`](https://github.com/cure53/DOMPurify?tab=readme-ov-file#can-i-configure-dompurify).

Must return the `DOMPurify` instance.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  sanitizeInit: (DOMPurify) => {
    // This will only allow YouTube iframes
    DOMPurify.addHook('uponSanitizeElement', (node, data) => {
      if (data.tagName === 'iframe') {
        const src = node.getAttribute('src') || ''
        
        if (!src.startsWith('https://www.youtube.com/embed/')) {
            return node.parentNode?.removeChild(node)
        }
      }
    })

    return DOMPurify
  },
  // ...
})
```

### strictConditions [​](https://vueform.com/docs/configuration#strictconditions)

*   Type: `boolean`
*   Default: `false`

When enabled, conditional logic will strictly evaluate field values, ensuring that `null`, undefined, or empty values do not satisfy numerical or logical conditions. When disabled, the app may apply type coercion, potentially treating null as `0` or an empty string, which could affect condition evaluations.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  strictConditions: true,
  // ...
})
```

### forceNumbers [​](https://vueform.com/docs/configuration#forcenumbers)

*   Type: `boolean`
*   Default: `false`

Whether text input values should be transformed to a `number` in form [`data`](https://vueform.com/reference/vueform#property-data) and [`requestData`](https://vueform.com/reference/vueform#property-request-data). If the input value contains any non-numeric character (except for `.` and `,`) it will be kept as `string`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  forceNumbers: true,
  // ...
})
```

It can be also set on [element level](https://vueform.com/reference/text-element#option-force-numbers) or [form level](https://vueform.com/reference/vueform#option-force-numbers).

### formData [​](https://vueform.com/docs/configuration#formdata)

*   Type: `function`
*   Default: `f$ => f$.requestData`

Sets the data object submitted by Vueform globally.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  formData(form$) {
    return form$.convertFormData(form$.requestData)
  },
  // ...
})
```

Learn more about form data [here](https://vueform.com/docs/vueform#option-form-data).

### beforeSend [​](https://vueform.com/docs/configuration#beforesend)

*   Type: `function`
*   Default: `null`

An async function to run each time before a form is submitted. It can stop the submit process by throwing an error. Receives [`form$`](https://vueform.com/docs/vueform#property-form) as its first param.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  async beforeSend(form$) {
    let active = (await form$.$vueform.services.axios.post('/user-still-active')).data

    if (!active) {
      throw new Error('User is not active anymore')
    }
  }
  // ...
})
```

### axios [​](https://vueform.com/docs/configuration#axios)

*   Type: `object|axios`
*   Default: `{}`

There are two ways to use this options.

It accepts an existing & configured `axios` instance:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import axios from 'axios'

axios.defaults.withCredentials = true
// ...

export default defineConfig({
  axios,
  // ...
})
```

Or if an `object` is provided it sets global [axios configuration](https://github.com/axios/axios#request-config). It has two custom options: `csrfRequest` and `onUnauthenticated`.

The `csrfRequest` option is an endpoint object that is used to submit an intermediate request to the server if an initial request returns `401` or `419`. The original request will be retried once after receiving a response from `csrfRequest` endpoint.

The `onUnauthenticated` option is a function that is called if the request still returns `401` or `419` after calling `csrfRequest` and repeating the original request.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  axios: {
    withCredentials: true,
    baseURL: '/api/',
    csrfRequest: {
      method: 'get',
      url: '/csrf-cookie',
    },
    onUnauthenticated() {
      location.href = '/sign-in'
    },
  },
  // ...
})
```

### locationProvider [​](https://vueform.com/docs/configuration#locationprovider)

*   Type: `string`
*   Default: `google`

Sets the default location provider for elements using location service, like [`LocationElement`](https://vueform.com/docs/location-element). Currently the only supported provider is `google`.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  locationProvider: 'google',
  // ...
})
```

Learn more about location providers [here](https://vueform.com/docs/location-element#option-provider).

### services [​](https://vueform.com/docs/configuration#services)

*   Type: `object`
*   Default: `see below`

Global configuration for services. Default:

js

```
// Default for `config.services`:

{
  services: {}
}
```

Example:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  services: {
    service_name: {
      service_option_1: '',
      service_option_2: '',
    }
  }
  // ...
})
```

### providers [​](https://vueform.com/docs/configuration#providers)

*   Type: `object`

Create and override providers.

Example:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import Recaptcha3Provider from './Recaptcha3Provider'

export default defineConfig({
  providers: {
    captcha: {
      recaptcha3: Recaptcha3Provider,
    },
  },
  // ...
})
```

### useProviders [​](https://vueform.com/docs/configuration#useproviders)

*   Type: `object`

Set the default providers.

Example:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  useProviders: {
    captcha: 'recaptcha3' // once `recaptcha3` is registered as a provider
  },
  // ...
})
```

### providerOptions [​](https://vueform.com/docs/configuration#provideroptions)

*   Type: `object`

Default options for registered providers.

Example:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  providerOptions: {
    recaptcha2: {
      sitekey: '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI',
    }
  },
  // ...
})
```

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
