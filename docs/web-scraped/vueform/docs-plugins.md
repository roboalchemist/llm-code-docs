# Source: https://vueform.com/docs/plugins

Title: Plugins | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/plugins

Markdown Content:
Learn how to extend Vueform with plugins.

Examples [​](https://vueform.com/docs/plugins#examples)
-------------------------------------------------------

Check out our official plugins for inspiration:

*   [https://github.com/vueform/plugin-mask](https://github.com/vueform/plugin-mask)
*   [https://github.com/vueform/vueform-plugin-toggle-confirm](https://github.com/vueform/vueform-plugin-toggle-confirm)
*   [https://github.com/vueform/vueform-plugin-toggle-tooltip](https://github.com/vueform/vueform-plugin-toggle-tooltip)

Registering Plugins [​](https://vueform.com/docs/plugins#registering-plugins)
-----------------------------------------------------------------------------

Plugins can be applied in `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import vueformPlugin from '@vueform/vueform-plugin'

export default defineConfig({
  plugins: [
    vueformPlugin,
  ],
  // ...
})
```

Plugin Options [​](https://vueform.com/docs/plugins#plugin-options)
-------------------------------------------------------------------

A plugin must be a `function` that returns an `object` with the plugin options.

js

```
export default function myPlugin() {
  return {
    // ... plugin options
  }
}
```

### apply [​](https://vueform.com/docs/plugins#apply)

*   Type: `string|regex|array`
*   Default: `undefined`

Which components in Vueform this plugin's [`setup`](https://vueform.com/docs/plugins#setup) option should be applied to.

js

```
export default function myPlugin() {
  return {
    apply: /^[a-zA-Z]+Element$/,
    setup(props, context, component) { /* ... */ },
  }
}
```

It can be an exact component name as a `string`:

js

`apply: 'TextElement',`

Multiple component names as an `array`:

js

`apply: ['TextElement', 'TextareaElement'],`

A `regex`, eg. which applies to each element:

js

`apply: /^[a-zA-Z]+Element$/,`

Or an array of `regex`:

js

`apply: [/^[a-zA-Z]+Element/, /^Element[a-zA-Z]+$/],`

If left empty and the plugin contains a [`setup`](https://vueform.com/docs/plugins#setup) option it will be applied to each component. Component names can be found at [Components](https://vueform.com/reference/text-element) page.

### setup [​](https://vueform.com/docs/plugins#setup)

*   Type: `function`
*   Arguments: 
    *   `{object} props` - the Composition API's `props` object
    *   `{object} context` - the Composition API's `context` object
    *   `{object} component` - the component's exported properties and methods

*   Returns: `object` - component properties and methods

Extends the component's properties and methods.

js

```
import { ref } from 'vue'

export default function myPlugin() {
  return {
    apply: 'TextElement',
    setup(props, context, component) {
      const myRef = ref('Hello World')

      // Hides all text element by default
      component.hidden.value = true

      return {
        ...component,
        myRef,
      }
    },
  }
}
```

The `component` argument is an object containing all the component's properties and methods. Properties are either [`ref`](https://vuejs.org/api/reactivity-core.html#ref) or [`computed`](https://vuejs.org/api/reactivity-core.html#computed) objects so `.value` is required to access / modify their values.

Component properties and methods can be found at [Components](https://vueform.com/reference/text-element) page.

### props [​](https://vueform.com/docs/plugins#props)

*   Type: `object`
*   Default: `{}`

Extends the component's prop list.

js

```
export default function myPlugin() {
  return {
    apply: 'TextElement',
    props: {
      format: {
        type: String,
        required: false,
      }
    }
  }
}
```

### config [​](https://vueform.com/docs/plugins#config)

*   Type: `function`
*   Arguments: 
    *   `{object} config` - the default Vueform config object

*   Returns: `void`

Modifies the default [configuration](https://vueform.com/docs/configuration). Executed before project level config is applied.

js

```
import myPreset from 'my-preset'

export default function myPlugin() {
  return {
    config(config) {
      // Adds a new config value
      config.foo = 'bar'

      // Applies `myPreset` by default to all Vueform instances
      config.presets.myPreset = myPreset
      config.usePresets.push('myPreset')
    }
  }
}
```

### install [​](https://vueform.com/docs/plugins#install)

*   Type: `function`
*   Arguments: 
    *   `{object} app` - the Vue.js app instance
    *   `{object} $vueform` - the global $vueform object

*   Returns: `void`

Executed after configuration object is resolved, before registering components and setting global `$vueform` object. Only use this, if you know what you are doing.

js

```
export default function myPlugin() {
  return {
    install(app, $vueform) {
      // Adding new variable to global $vueform object
      $vueform.foo = 'bar'
    }
  }
}
```

*   [`vueform-plugin-checkbox-select-all`](https://github.com/dev-mohieb/vueform-plugin-checkbox-select-all) by [dev-mohieb](https://github.com/dev-mohieb)

[Input Mask](https://vueform.com/docs/input-mask)[Creating Elements](https://vueform.com/docs/creating-elements)

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)

Drag and Drop

Form Builder

Try it for free. No registration needed.

![Image 1: Vueform | Vue Form Builder and Generator](https://vueform.com/images/small-builder.webp)![Image 2: Vueform | Vue Form Builder and Generator](https://vueform.com/images/concentric-circles.svg)
