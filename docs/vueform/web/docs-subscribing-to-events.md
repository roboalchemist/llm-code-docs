# Source: https://vueform.com/docs/subscribing-to-events

Title: Subscribing to Events | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/subscribing-to-events

Markdown Content:
Learn how to subscribe to Vueform events on form or element level.

Subscribing to Events [​](https://vueform.com/docs/subscribing-to-events#subscribing-to-events-1)
-------------------------------------------------------------------------------------------------

We can subscribe to events and [Vue Lifecycle Hooks](https://v3.vuejs.org/api/options-lifecycle-hooks.html) of components:

Inline Schema SFC

vue

```
<template>
  <Vueform @change="..." @mounted="...">
    <template #empty>
      <FormSteps @next="..." @mounted="..." ...>
        <FormStep @complete="..." @mounted="..." ... />
      </FormSteps>

      <FormTabs @select="..." @mounted="..." ...>
        <FormTab @active="..." @mounted="..." ... />
      </FormTabs>

      <TextElement @change="..." @mounted="..." />
    </template>
  </Vueform>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" ref="form$" />
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form = ref({
  onChange() { ... },
  onMounted() { ... },
  steps: {
    first: {
      onComplete() { ... },
      onMounted() { ... },
    },
    // ...
  },
  tabs: {
    first: {
      onActive() { ... },
      onMounted() { ... },
    },
    // ...
  },
  schema: {
    element: {
      onChange() { ... },
      onMounted() { ... }
    }
  }
})

onMounted() {
  // Subscribing to form events & hooks
  form$.value.on('change', ...)
  form$.value.on('mounted', ...)

  // Subscribing to FormSteps events & hooks
  form$.value.steps$.on('change', ...)
  form$.value.steps$.on('mounted', ...)

  // Subscribing to FormTabs events & hooks
  form$.value.tabs$.on('change', ...)
  form$.value.tabs$.on('mounted', ...)

  // Subscribing to element events & hooks
  form$.value.el$('element').on('change', ...)
  form$.value.el$('element').on('mounted', ...)
}
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    form: {
      onChange() { ... },
      onMounted() { ... },
      steps: {
        first: {
          onComplete() { ... },
          onMounted() { ... },
        },
        // ...
      },
      tabs: {
        first: {
          onActive() { ... },
          onMounted() { ... },
        },
        // ...
      },
      schema: {
        element: {
          onChange() { ... },
          onMounted() { ... }
        }
      }
    }
  }),
  mounted() {
    // Subscribing to form events & hooks
    this.$refs.form$.on('change', ...)
    this.$refs.form$.on('mounted', ...)

    // Subscribing to FormSteps events & hooks
    this.$refs.form$.steps$.on('change', ...)
    this.$refs.form$.steps$.on('mounted', ...)

    // Subscribing to FormTabs events & hooks
    this.$refs.form$.tabs$.on('change', ...)
    this.$refs.form$.tabs$.on('mounted', ...)

    // Subscribing to element events & hooks
    this.$refs.form$.el$('element').on('change', ...)
    this.$refs.form$.el$('element').on('mounted', ...)
  }
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref, onMounted } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      onChange() { ... },
      onMounted() { ... },
      steps: {
        first: {
          onComplete() { ... },
          onMounted() { ... },
        },
        // ...
      },
      tabs: {
        first: {
          onActive() { ... },
          onMounted() { ... },
        },
        // ...
      },
      schema: {
        element: {
          onChange() { ... },
          onMounted() { ... }
        }
      }
    })

    onMounted(() => {
      // Subscribing to form events & hooks
      form.on('change', ...)
      form.on('mounted', ...)

      // Subscribing to FormSteps events & hooks
      form.steps$.value.on('change', ...)
      form.steps$.value.on('mounted', ...)

      // Subscribing to FormTabs events & hooks
      form.tabs$.value.on('change', ...)
      form.tabs$.value.on('mounted', ...)

      // Subscribing to element events & hooks
      form.el$('element').on('change', ...)
      form.el$('element').on('mounted', ...)
    })

    return {
      ...component,
      vueform,
    }
  },
}
</script>

<!-- Options API -->
<script>
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      onChange() { ... },
      onMounted() { ... },
      steps: {
        first: {
          onComplete() { ... },
          onMounted() { ... },
        },
        // ...
      },
      tabs: {
        first: {
          onActive() { ... },
          onMounted() { ... },
        },
        // ...
      },
      schema: {
        element: {
          onChange() { ... },
          onMounted() { ... }
        }
      }
    }
  }),
  mounted() {
    // Subscribing to form events & hooks
    this.on('change', ...)
    this.on('mounted', ...)

    // Subscribing to FormSteps events & hooks
    this.steps$.on('change', ...)
    this.steps$.on('mounted', ...)

    // Subscribing to FormTabs events & hooks
    this.tabs$.on('change', ...)
    this.tabs$.on('mounted', ...)

    // Subscribing to element events & hooks
    this.el$('element').on('change', ...)
    this.el$('element').on('mounted', ...)
  }
}
</script>
```

The available events are listed at the component's Components reference's "**Events**" section.

The available hooks from [Vue.js 3 Lifecycle Hooks](https://v3.vuejs.org/api/options-lifecycle-hooks.html) are:

*   `beforeCreate`
*   `created`
*   `beforeMount`
*   `mounted`
*   `beforeUpdate`
*   `updated`
*   `beforeUnmount` (equals to `beforeDestroy` in Vue.js 2)
*   `unmounted` (equals to `destroyed` in Vue.js 2)

We can also subscribe to events after components are mounted:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <template #empty>
      <FormSteps ...>
        <FormStep ... />
      </FormSteps>

      <FormTabs ...>
        <FormTab ... />
      </FormTabs>

      <TextElement ... />
    </template>
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  // Subscribing to Vueform events
  form$.value.on('change', ...)

  // Subscribing to FormSteps events
  form$.value.steps$.on('next', ...)

  // Subscribing to FormStep events
  form$.value.steps$.steps$.step_name.on('complete', ...)

  // Subscribing to FormTabs events
  form$.value.tabs$.on('select', ...)

  // Subscribing to FormTab events
  form$.value.tabs$.tabs$.tab_name.on('active', ...)

  // Subscribing to TextElement (or any other) events
  form$.value.el$('element_path').on('change', ...)
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <template #empty>
      <FormSteps ...>
        <FormStep ... />
      </FormSteps>

      <FormTabs ...>
        <FormTab ... />
      </FormTabs>

      <TextElement ... />
    </template>
  </Vueform>
</template>

<script>
export default {
  mounted() {
    // Subscribing to Vueform events
    this.$refs.form$.on('change', ...)

    // Subscribing to FormSteps events
    this.$refs.form$.steps$.on('next', ...)

    // Subscribing to FormStep events
    this.$refs.form$.steps$.steps$.step_name.on('complete', ...)

    // Subscribing to FormTabs events
    this.$refs.form$.tabs$.on('select', ...)

    // Subscribing to FormTab events
    this.$refs.form$.tabs$.tabs$.tab_name.on('active', ...)

    // Subscribing to TextElement (or any other) events
    this.$refs.form$.el$('element_path').on('change', ...)
  }
}
</script>
```

Unsubscribing From Events [​](https://vueform.com/docs/subscribing-to-events#unsubscribing-from-events)
-------------------------------------------------------------------------------------------------------

We can use the `off(event)` method to unsubscribe from all events of the component.

For example:

Composition API Options API

js

`form$.value.off('change')`

js

`this.$refs.form$.off('change')`

This will unsubscribe all listeners from `Vueform` component's `change` event.

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
