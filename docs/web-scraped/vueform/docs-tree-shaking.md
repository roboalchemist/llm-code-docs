# Source: https://vueform.com/docs/tree-shaking

Title: Tree shaking | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/tree-shaking

Markdown Content:
Reduce the bundle size by removing unused parts of Vueform.

How to Tree Shake [​](https://vueform.com/docs/tree-shaking#how-to-tree-shake)
------------------------------------------------------------------------------

Tree-shaking requires importing component logic, templates and validation rules separately in `vueform.config.js` and our main `.js` file.

This is how our `vueform.config.js` looks by deafult (if we are using `vueform` theme):

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import vueform from '@vueform/vueform/dist/vueform'

export default defineConfig({
  theme: vueform,
  // ...
})
```

This is how our main `.js` file (eg. `main.js`) looks like by deafult:

js

```
// eg. main.js

import Vueform from '@vueform/vueform'
import vueformConfig from './vueform.config'

const app = createApp(App)
app.use(Vueform, vueformConfig)
app.mount('#app')
```

### Install Dependencies [​](https://vueform.com/docs/tree-shaking#install-dependencies)

First, we have to install a couple of Vueform's dependencies, that will be required to build from source:

npm yarn pnpm bun

bash

`npm install autosize flatpickr locutus lodash sortablejs`

bash

`yarn add autosize flatpickr locutus lodash sortablejs`

bash

`pnpm add autosize flatpickr locutus lodash sortablejs`

bash

`bun install autosize flatpickr locutus lodash sortablejs`

### Add Vite Plugin [​](https://vueform.com/docs/tree-shaking#add-vite-plugin)

If you are using Vite or Vite based framework (like Nuxt), add Vueform's vite plugin:

#### Vite [​](https://vueform.com/docs/tree-shaking#vite)

js

```
// vite.config.js

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueform from '@vueform/vueform/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueform(),
  ],
})
```

#### Nuxt [​](https://vueform.com/docs/tree-shaking#nuxt)

js

```
// nuxt.config.ts

import { defineNuxtConfig } from 'nuxt'
import vueform from '@vueform/vueform/vite'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  vite: {
    plugins: [
      vueform()
    ]
  }
})
```

### Component Logic [​](https://vueform.com/docs/tree-shaking#component-logic)

First let's import names component logic from `@vueform/vueform/src/core.js` and extend our config with it, using `components` prop:

js

```
// main.js

import Vueform, {
  // Essential form components
  FormErrors,
  FormMessages,

  // Essential element components
  ElementLayout,
  ElementLayoutInline,
  ElementLoader,
  ElementLabelFloating,
  ElementLabel,
  ElementInfo,
  ElementDescription,
  ElementError,
  ElementMessage,
  ElementText,
  ElementAddon,
  ElementAddonOptions,

  // Optional form components
  FormLanguages,
  FormLanguage,
  FormTabs,
  FormTab,
  FormSteps,
  FormStepsControls,
  FormStepsControl,
  FormStep,

  // Elements
  ButtonElement,
  CaptchaElement,
  CheckboxElement,
  CheckboxgroupElement,
  DateElement,
  DatesElement,
  FileElement,
  GroupElement,
  HiddenElement,
  ListElement,
  LocationElement,
  MultifileElement,
  MultiselectElement,
  ObjectElement,
  PhoneElement,
  RadioElement,
  RadiogroupElement,
  SelectElement,
  SignatureElement,
  SliderElement,
  StaticElement,
  TagsElement,
  TextareaElement,
  TextElement,
  ToggleElement,
  EditorElement,
  TTextareaElement,
  TTextElement,
  TEditorElement,

  // Element partials & wrappers
  DragAndDrop,
  CheckboxgroupCheckbox,
  RadiogroupRadio,
  FilePreview,
  DatepickerWrapper,
  EditorWrapper,
} from '@vueform/vueform/src/core.js'

import vueformConfig from './vueform.config'

const app = createApp(App)
app.use(Vueform, {
  ...vueformConfig,
  components: {
    // [INSERT COMPONENTS HERE]
  }
})
app.mount('#app')
```

The `Vueform` and `FormElements` components are automatically included in our bundle, so we don't need to import them separately.

### Templates [​](https://vueform.com/docs/tree-shaking#templates)

The next step is to import the component templates from our theme to match the components we imported in our main `.js` file.

Here, we need to import `Vueform` and `FormElements` as well.

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform/src/core.js'

import {
  // Mandatory form components
  Vueform,
  FormElements,
  
  // Essential form components (optional)
  FormErrors,
  FormMessages,

  // Essential element components (optional)
  ElementLayout,
  ElementLayoutInline,
  ElementLoader,
  ElementLabelFloating,
  ElementLabel,
  ElementInfo,
  ElementDescription,
  ElementError,
  ElementMessage,
  ElementText,
  ElementAddon,
  ElementAddonOptions,

  // Optional form components (optional)
  FormLanguages,
  FormLanguage,
  FormTabs,
  FormTab,
  FormSteps,
  FormStepsControls,
  FormStepsControl,
  FormStep,

  // Elements (optional)
  ButtonElement,
  CaptchaElement,
  CheckboxElement,
  CheckboxgroupElement,
  DateElement,
  DatesElement,
  FileElement,
  GroupElement,
  HiddenElement,
  ListElement,
  LocationElement,
  MultifileElement,
  MultiselectElement,
  ObjectElement,
  PhoneElement,
  RadioElement,
  RadiogroupElement,
  SelectElement,
  SignatureElement,
  SliderElement,
  StaticElement,
  TagsElement,
  TextareaElement,
  TextElement,
  ToggleElement,
  EditorElement,
  TTextareaElement,
  TTextElement,
  TEditorElement,

  // Element partials & wrappers (optional)
  DragAndDrop,
  CheckboxgroupCheckbox,
  RadiogroupRadio,
  FilePreview,
  DatepickerWrapper,
  EditorWrapper,

  // Alternative views (optional)
  CheckboxgroupElement_tabs,
  CheckboxgroupElement_blocks,
  CheckboxgroupCheckbox_tabs,
  CheckboxgroupCheckbox_blocks,
  FilePreview_image,
  FilePreview_gallery,
  RadiogroupRadio_tabs,
  RadiogroupRadio_blocks,
  RadiogroupElement_tabs,
  RadiogroupElement_blocks,
  
  // Mandatory imports
  classes,
  columns,
} from '@vueform/vueform/themes/vueform'

// create our own theme
const vueform = {
  templates: {
    // [INSERT COMPONENTS HERE]
  },

  // Include these
  classes,
  columns,
}

export default defineConfig({
  theme: vueform,
  // ...
})
```

### Validation rules [​](https://vueform.com/docs/tree-shaking#validation-rules)

Next we will add required validation rules manually to `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

import {
  accepted,
  active_url,
  after,
  after_or_equal,
  alpha,
  alpha_dash,
  alpha_num,
  array,
  before,
  before_or_equal,
  between,
  boolean,
  captcha,
  completed,
  confirmed,
  date,
  date_equals,
  date_format,
  different,
  digits,
  digits_between,
  dimensions,
  distinct,
  email,
  exists,
  file,
  filled,
  gt,
  gte,
  image,
  in_,
  in_array,
  integer,
  ip,
  ipv4,
  ipv6,
  json,
  lt,
  lte,
  max,
  mimes,
  mimetypes,
  min,
  not_in,
  not_regex,
  nullable,
  numeric,
  regex,
  required,
  same,
  size,
  string,
  timezone,
  unique,
  url,
  uuid,
} from '@vueform/vueform/src/core.js'

export default defineConfig({
  rules: {
    // [INSERT RULES HERE]
  },
  // ...
})
```

**IMPORTANT:** the `in` rule is imported as `in_`, so it must be passed to `rules` as:

js

```
rules: {
  in: in_,
}
```

### Other replacements [​](https://vueform.com/docs/tree-shaking#other-replacements)

Check your project if you're importing `@vueform/vueform` anywhere else and change them to `@vueform/vueform/core` to avoid accidentally import the full bundle too.

Benchmark [​](https://vueform.com/docs/tree-shaking#benchmark)
--------------------------------------------------------------

Last tested on `2023-11-13` with version `1.5.7` in Vite `3.1.3`. Gzipped sizes.

| Bundle | JS | CSS |
| --- | --- | --- |
| Default components + all services | 91.88 kB | 8.75 kB |
| + native HTML elements | +12.42 kB | +0.02 kB |
| + default elements | +27.41 kB | +3.83 kB |
| + validation rules | +12.23 kB | +0 kB |
| + advanced components | +5.25 kB | +1.29 kB |
| + all other elements + views (full build) | +92.76 kB | +17.89 kB |

### Reference [​](https://vueform.com/docs/tree-shaking#reference)

##### Default components [​](https://vueform.com/docs/tree-shaking#default-components)

*   Vueform
*   FormElements
*   FormErrors
*   FormMessages
*   ElementLayout
*   ElementLayoutInline
*   ElementLoader
*   ElementLabelFloating
*   ElementLabel
*   ElementInfo
*   ElementDescription
*   ElementError
*   ElementMessage
*   ElementText
*   ElementAddon
*   ElementAddonOptions

##### Advanced components [​](https://vueform.com/docs/tree-shaking#advanced-components)

*   FormLanguages
*   FormLanguage
*   FormTabs
*   FormTab
*   FormSteps
*   FormStepsControls
*   FormStepsControl
*   FormStep

##### Native HTML elements [​](https://vueform.com/docs/tree-shaking#native-html-elements)

*   ButtonElement
*   CheckboxgroupElement
*   HiddenElement
*   RadiogroupElement
*   TextareaElement
*   TextElement

##### Default elements (including native HTML) [​](https://vueform.com/docs/tree-shaking#default-elements-including-native-html)

*   ButtonElement
*   CheckboxgroupElement
*   FileElement
*   HiddenElement
*   MultiselectElement
*   RadiogroupElement
*   SelectElement
*   TagsElement
*   TextareaElement
*   TextElement
*   CheckboxgroupCheckbox
*   RadiogroupRadio

##### All elements [​](https://vueform.com/docs/tree-shaking#all-elements)

*   ButtonElement
*   CaptchaElement
*   CheckboxElement
*   CheckboxgroupElement
*   DateElement
*   DatesElement
*   FileElement
*   GroupElement
*   HiddenElement
*   ListElement
*   LocationElement
*   MultifileElement
*   MultiselectElement
*   ObjectElement
*   PhoneElement
*   RadioElement
*   RadiogroupElement
*   SelectElement
*   SignatureElement
*   SliderElement
*   StaticElement
*   TagsElement
*   TextareaElement
*   TextElement
*   ToggleElement
*   EditorElement
*   TTextareaElement
*   TTextElement
*   TEditorElement

##### Validation rules [​](https://vueform.com/docs/tree-shaking#validation-rules-1)

*   accepted
*   active_url
*   after
*   after_or_equal
*   alpha
*   alpha_dash
*   alpha_num
*   array
*   before
*   before_or_equal
*   between
*   boolean
*   confirmed
*   date
*   date_equals
*   date_format
*   different
*   digits
*   digits_between
*   dimensions
*   distinct
*   email
*   exists
*   file
*   filled
*   gt
*   gte
*   image
*   in_
*   in_array
*   integer
*   ip
*   ipv4
*   ipv6
*   json
*   lt
*   lte
*   max
*   mimes
*   mimetypes
*   min
*   not_in
*   not_regex
*   nullable
*   numeric
*   regex
*   required
*   same
*   size
*   string
*   timezone
*   unique
*   url
*   uuid

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
