# Source: https://vueform.com/docs/breaking-forms-into-steps

Title: Breaking Forms into Steps | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/breaking-forms-into-steps

Published Time: Wed, 21 Jan 2026 09:54:47 GMT

Markdown Content:
Learn how to break you forms into steps to enchance user experience.

Using Form Steps [​](https://vueform.com/docs/breaking-forms-into-steps#using-form-steps)
-----------------------------------------------------------------------------------------

We can use `FormSteps` and `FormStep` components to break forms into steps:

Inline Schema SFC

vue

```
<template>
  <Vueform>
    <template #empty>
      <FormSteps>
        <FormStep name="first" label="First" :elements="['first_input']" />
        <FormStep name="second" label="Second" :elements="['second_input']" />
        <FormStep name="third" label="Third" :elements="['third_input']" />
      </FormSteps>

      <FormElements>
        <TextElement name="first_input" placeholder="First input" />
        <TextElement name="second_input" placeholder="Second input" />
        <TextElement name="third_input" placeholder="Third input" />
      </FormElements>

      <FormStepsControls />
    </template>
  </Vueform>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref } from 'vue'

const form = ref({
  steps: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
    second: {
      label: 'Second',
      elements: ['second_input']
    },
    third: {
      label: 'Third',
      elements: ['third_input']
    },
  },
  schema: {
    first_input: { type: 'text', placeholder: 'First input' },
    second_input: { type: 'text', placeholder: 'Second input' },
    third_input: { type: 'text', placeholder: 'Third input' },
  }
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    form: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input']
        },
        second: {
          label: 'Second',
          elements: ['second_input']
        },
        third: {
          label: 'Third',
          elements: ['third_input']
        },
      },
      schema: {
        first_input: { type: 'text', placeholder: 'First input' },
        second_input: { type: 'text', placeholder: 'Second input' },
        third_input: { type: 'text', placeholder: 'Third input' },
      }
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      steps: {
        first: {
          label: 'First',
          elements: ['first_input']
        },
        second: {
          label: 'Second',
          elements: ['second_input']
        },
        third: {
          label: 'Third',
          elements: ['third_input']
        },
      },
      schema: {
        first_input: { type: 'text', placeholder: 'First input' },
        second_input: { type: 'text', placeholder: 'Second input' },
        third_input: { type: 'text', placeholder: 'Third input' },
      }
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input']
        },
        second: {
          label: 'Second',
          elements: ['second_input']
        },
        third: {
          label: 'Third',
          elements: ['third_input']
        },
      },
      schema: {
        first_input: { type: 'text', placeholder: 'First input' },
        second_input: { type: 'text', placeholder: 'Second input' },
        third_input: { type: 'text', placeholder: 'Third input' },
      }
    }
  })
}
</script>
```

When using them inline we have to put all the content of the form into [`#empty`](https://vueform.com/reference/vueform#slot-empty) slot, becase the default Vueform slots is only intended for rendering elements.

Form elements have to be put into `FormElements` component which serves as a wrapper.

We also need to add `FormStepsControls` to the template, which renders the form controls (Previous, Next, Finish).

We can use these three parts anywhere in out template, which gives us the freedom to create any kind of layout we want.

### Step Options [​](https://vueform.com/docs/breaking-forms-into-steps#step-options)

Each `FormStep` component must have at least 2 props:

*   `name` - the internal name of the step we can later use to reach its API
*   `elements` - an array of element **names** (as string) that the step should include.

And also `label`, which is the label visible to the user if it is not defined inline between `<FormStep></FormStep>`.

### Customizing Step Label [​](https://vueform.com/docs/breaking-forms-into-steps#customizing-step-label)

Step labels can be passed via default slot or as a string and can contain HTML:

Inline Schema SFC

template

```
<template>
  <FormStep name="first" ...>
    <b>I.</b> First
  </FormStep>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref, h, resolveComponent } from 'vue'

const form = ref({
  steps: {
    first: {
      label: '<b>I.</b> First',
      elements: ['first_input'],
    },
    // ...
  },
  // ...
})
</script>

<!-- Options API -->
<script>
import { h, resolveComponent } from 'vue'

export default {
  data: () => ({
    forms: {
      steps: {
        first: {
          label: '<b>I.</b> First',
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      steps: {
        first: {
          label: '<b>I.</b> First',
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: '<b>I.</b> First',
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

... or they can be Vue components:

Inline Schema SFC

template

```
<template>
  <FormStep name="first" ...>
    <AppIcon :icon="['fas', 'id-card']"> First
  </FormStep>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref, h, resolveComponent } from 'vue'

const form = ref({
  steps: {
    first: {
      label: {
        props: ['form$'],
        render: () => h('span', [
          h(resolveComponent('AppIcon'), {
            icon: ['far', 'id-card']
          }),
          'First',
        ])
      },
      elements: ['first_input'],
    },
    // ...
  },
  // ...
})
</script>

<!-- Options API -->
<script>
import { h, resolveComponent } from 'vue'

export default {
  data: () => ({
    forms: {
      steps: {
        first: {
          label: {
            props: ['form$'],
            render: () => h('span', [
              h(resolveComponent('AppIcon'), {
                icon: ['far', 'id-card']
              }),
              'First',
            ])
          },
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      steps: {
        first: {
          label: {
            props: ['form$'],
            render: () => h('span', [
              h(resolveComponent('AppIcon'), {
                icon: ['far', 'id-card']
              }),
              'First',
            ])
          },
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: {
            props: ['form$'],
            render: () => h('span', [
              h(resolveComponent('AppIcon'), {
                icon: ['far', 'id-card']
              }),
              'First',
            ])
          },
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

### Customizing Steps Controls [​](https://vueform.com/docs/breaking-forms-into-steps#customizing-steps-controls)

We can hide buttons for a step using `buttons` option. For example:

Inline Schema SFC

template

```
<template>
  <FormStep name="first" :buttons="{
    previous: false
  }" ... />
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref } from 'vue'

const form = ref({
  steps: {
    first: {
      label: 'First',
      elements: ['first_input'],
      buttons: {
        previous: false,
      }
    },
    // ...
  },
  // ...
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    forms: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          buttons: {
            previous: false,
          }
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          buttons: {
            previous: false,
          }
        },
        // ...
      },
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          buttons: {
            previous: false,
          }
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

This will hide the previous button on the first step. We can also hide `next` and `finish` buttons.

We can also change the labels of buttons for a step using `labels` options. For example:

Inline Schema SFC

template

```
<template>
  <FormStep name="first" :labels="{
    previous: '< Previous',
    next: 'Next >'
  }" ... />
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref } from 'vue'

const form = ref({
  steps: {
    first: {
      label: 'First',
      elements: ['first_input'],
      labels: {
        previous: '< Previous',
        next: 'Next >'
      }
    },
    // ...
  },
  // ...
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    forms: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          labels: {
            previous: '< Previous',
            next: 'Next >'
          }
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          labels: {
            previous: '< Previous',
            next: 'Next >'
          }
        },
        // ...
      },
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          labels: {
            previous: '< Previous',
            next: 'Next >'
          }
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

Button labels can contain HTML or they can be Vue components:

Inline Schema SFC

template

```
<template>
  <FormStepsControls :labels="false">
    <template #previous><icon name='arrow-left' /> Previous</template>
    <template #next>Next <icon name='arrow-right' /></template>
    <template #finish><icon name='tick' /> Finish</template>
  </FormStepsControls>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref, h, resolveComponent } from 'vue'

const form = ref({
  steps: {
    first: {
      label: 'First',
      elements: ['first_input'],
      labels: {
        previous: {
          props: ['step$'],
          render: () => h('span', [
            h(resolveComponent('AppIcon'), {
              icon: ['far', 'arrow-left']
            }),
            h('Previous'),
          ])
        },
        // ...
      }
    },
    // ...
  },
  // ...
})
</script>

<!-- Options API -->
<script>
import { h, resolveComponent } from 'vue'

export default {
  data: () => ({
    forms: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          labels: {
            previous: {
              props: ['step$'],
              render: () => h('span', [
                h(resolveComponent('AppIcon'), {
                  icon: ['far', 'arrow-left']
                }),
                h('Previous'),
              ])
            },
            // ...
          }
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          labels: {
            previous: {
              props: ['step$'],
              render: () => h('span', [
                h(resolveComponent('AppIcon'), {
                  icon: ['far', 'arrow-left']
                }),
                h('Previous'),
              ])
            },
            // ...
          }
        },
        // ...
      },
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
          labels: {
            previous: {
              props: ['step$'],
              render: () => h('span', [
                h(resolveComponent('AppIcon'), {
                  icon: ['far', 'arrow-left']
                }),
                h('Previous'),
              ])
            },
            // ...
          }
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

When using slots for custom controls template [`FormStepsControls`](https://vueform.com/reference/form-steps-controls) component must receive [`:labels="false"`](https://vueform.com/reference/form-steps-controls#option-labels) option and it will ignore the [`:labels`](https://vueform.com/reference/form-step#option-labels) object of [`FormStep`](https://vueform.com/reference/form-step).

Steps API [​](https://vueform.com/docs/breaking-forms-into-steps#steps-api)
---------------------------------------------------------------------------

Once we have steps we can reach their API and use their methods and properties.

This is how we can reach [`FormSteps`](https://vueform.com/reference/form-steps) and [`FormStep`](https://vueform.com/reference/form-step) components:

Inline Schema SFC

vue

```
<template>
  <Vueform ref="form$">
    <template #empty>
      <FormSteps>
        <FormStep name="first" ... />
      </FormSteps>
    </template>
  </Vueform>
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.steps$ // returns FormSteps component instance
  form$.value.steps$.steps$.first // returns FormStep component instance named `first`
})
</script>

<!-- Options API -->
<script>
export default {
  mounted() {
    this.$refs.form$.steps$ // returns FormSteps component instance
    this.$refs.form$.steps$.steps$.first // returns FormStep component instance named `first`
  }
}
</script>
```

vue

```
<template>
  <Vueform v-bind="form" ref="form$" />
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const form = ref({
  steps: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
  },
  // ...
})

onMounted(() => {
  form$.value.steps$ // returns FormSteps component instance
  form$.value.steps$.steps$.first // returns FormStep component instance named `first`
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    steps: {
      first: {
        label: 'First',
        elements: ['first_input']
      },
    },
    // ...
  }),
  mounted() {
    this.$refs.form$.steps$ // returns FormSteps component instance
    this.$refs.form$.steps$.steps$.first // returns FormStep component instance named `first`
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
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    })

    onMounted(() => {
      form.steps$.value // returns FormSteps component instance
      form.steps$.value.steps$.first // returns FormStep component instance named `first`
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    }
  }),
  mounted() {
    this.steps$ // returns FormSteps component instance
    this.steps$.steps$.first // returns FormStep component instance named `first`
  }
}
</script>
```

Alternatively we can use Vueform's [`@mounted`](https://vueform.com/reference/vueform#event-mounted) event to access `steps$`:

Inline Schema SFC

template

```
<template>
  <Vueform @mounted="(form$) => {
    form$.steps$ // returns FormSteps component instance
    form$.steps$.steps$.first // returns FormStep component instance named `first`
  }">
    <template #empty>
      <FormSteps>
        <FormStep name="first" ... />
      </FormSteps>
    </template>
  </Vueform>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const form = ref({
  steps: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
  },
  onMounted(form$) {
    form$.steps$ // returns FormSteps component instance
    form$.steps$.steps$.first // returns FormStep component instance named `first`
  }
  // ...
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    steps: {
      first: {
        label: 'First',
        elements: ['first_input']
      },
    },
    onMounted(form$) {
      form$.steps$ // returns FormSteps component instance
      form$.steps$.steps$.first // returns FormStep component instance named `first`
    }
    // ...
  }),
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
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      onMounted(form$) {
        form$.steps$ // returns FormSteps component instance
        form$.steps$.steps$.first // returns FormStep component instance named `first`
      }
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      onMounted(form$) {
        form$.steps$ // returns FormSteps component instance
        form$.steps$.steps$.first // returns FormStep component instance named `first`
      },
      // ...
    }
  }),
}
</script>
```

Later we can use check out [`FormSteps`](https://vueform.com/reference/form-steps) and [`FormStep`](https://vueform.com/reference/form-step) component reference to see what method and properties can be used.

### Subscribing To Step Events [​](https://vueform.com/docs/breaking-forms-into-steps#subscribing-to-step-events)

We can subscribe to [`FormSteps`](https://vueform.com/reference/form-steps) events like [`@next`](https://vueform.com/reference/form-steps#event-next) or [`@previous`](https://vueform.com/reference/form-steps#event-previous) and [`FormStep`](https://vueform.com/reference/form-step) event like [`@activate`](https://vueform.com/reference/form-step#event-activate) or [`@complete`](https://vueform.com/reference/form-step#event-complete) via Vueform's `steps$` property:

Inline Schema SFC

vue

```
<template>
  <Vueform ref="form$">
    <template #empty>
      <FormSteps>
        <FormStep name="first" ... />
      </FormSteps>
    </template>
  </Vueform>
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  // Subscribe to FormSteps' @next event
  form$.value.steps$.on('next', (step$) => {
    // ...
  })
  
  // Subscribe to `first` FormStep's @activate event
  form$.value.steps$.steps$.first.on('activate', (step$) => {
    // ...
  })
})
</script>

<!-- Options API -->
<script>
export default {
  mounted() {
    // Subscribe to FormSteps' @next event
    this.$refs.form$.steps$.on('next', (step$) => {
      // ...
    })

    // Subscribe to `first` FormStep's @activate event
    this.$refs.form$.steps$.steps$.first.on('activate', (step$) => {
      // ...
    })
  }
}
</script>
```

vue

```
<template>
  <Vueform v-bind="form" ref="form$" />
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const form = ref({
  steps: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
  },
  // ...
})

onMounted(() => {
  // Subscribe to FormSteps' @next event
  form$.value.steps$.on('next', (step$) => {
    // ...
  })

  // Subscribe to `first` FormStep's @activate event
  form$.value.steps$.steps$.first.on('activate', (step$) => {
    // ...
  })
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    steps: {
      first: {
        label: 'First',
        elements: ['first_input']
      },
    },
    // ...
  }),
  mounted() {
    // Subscribe to FormSteps' @next event
    this.$refs.form$.steps$.on('next', (step$) => {
      // ...
    })
    
    // Subscribe to `first` FormStep's @activate event
    this.$refs.form$.steps$.steps$.first.on('activate', (step$) => {
      // ...
    })
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
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    })

    onMounted(() => {
      // Subscribe to FormSteps' @next event
      form.steps$.value.on('next', (step$) => {
        // ...
      })

      // Subscribe to `first` FormStep's @activate event
      form.steps$.value.steps$.first.on('activate', (step$) => {
        // ...
      })
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      steps: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    }
  }),
  mounted() {
    // Subscribe to FormSteps' @next event
    this.steps$.on('next', (step$) => {
      // ...
    })

    // Subscribe to `first` FormStep's @activate event
    this.steps$.steps$.first.on('activate', (step$) => {
      // ...
    })

  }
}
</script>
```

[Related Recipe Complete form steps up until a point Complete forms steps up until a point eg. when loading a partially filled in form.](https://vueform.com/recipes/complete-form-steps-up-until-a-point)

Using Tabs [​](https://vueform.com/docs/breaking-forms-into-steps#using-tabs)
-----------------------------------------------------------------------------

Tabs are useful for users to submit data in a more user friendly way, but it's less convenient for changing existing data. If we'd like to load existing data which was initially submitted via steps, we can use [`FormTabs`](https://vueform.com/reference/form-tabs) and [`FormTab`](https://vueform.com/reference/form-tab) components to replace steps:

Inline Schema SFC

vue

```
<template>
  <Vueform>
    <template #empty>
      <FormTabs>
        <FormTab name="first" label="First" :elements="['first_input']" />
        <FormTab name="second" label="Second" :elements="['second_input']" />
        <FormTab name="third" label="Third" :elements="['third_input']" />
      </FormTabs>

      <FormElements>
        <TextElement name="first_input" placeholder="First input" />
        <TextElement name="second_input" placeholder="Second input" />
        <TextElement name="third_input" placeholder="Third input" />
      </FormElements>
    </template>
  </Vueform>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref } from 'vue'

const form = ref({
  tabs: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
    second: {
      label: 'Second',
      elements: ['second_input']
    },
    third: {
      label: 'Third',
      elements: ['third_input']
    },
  },
  schema: {
    first_input: { type: 'text', placeholder: 'First input' },
    second_input: { type: 'text', placeholder: 'Second input' },
    third_input: { type: 'text', placeholder: 'Third input' },
  }
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    form: {
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input']
        },
        second: {
          label: 'Second',
          elements: ['second_input']
        },
        third: {
          label: 'Third',
          elements: ['third_input']
        },
      },
      schema: {
        first_input: { type: 'text', placeholder: 'First input' },
        second_input: { type: 'text', placeholder: 'Second input' },
        third_input: { type: 'text', placeholder: 'Third input' },
      }
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input']
        },
        second: {
          label: 'Second',
          elements: ['second_input']
        },
        third: {
          label: 'Third',
          elements: ['third_input']
        },
      },
      schema: {
        first_input: { type: 'text', placeholder: 'First input' },
        second_input: { type: 'text', placeholder: 'Second input' },
        third_input: { type: 'text', placeholder: 'Third input' },
      }
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input']
        },
        second: {
          label: 'Second',
          elements: ['second_input']
        },
        third: {
          label: 'Third',
          elements: ['third_input']
        },
      },
      schema: {
        first_input: { type: 'text', placeholder: 'First input' },
        second_input: { type: 'text', placeholder: 'Second input' },
        third_input: { type: 'text', placeholder: 'Third input' },
      }
    }
  })
}
</script>
```

*   First

*   Second

*   Third

### Tab Options [​](https://vueform.com/docs/breaking-forms-into-steps#tab-options)

Each `FormTab` component must have at least 2 props:

*   `name` - the internal name of the tab we can later use to reach its API
*   `elements` - an array of element **names** (as string) that the tab should include.

And also `label`, which is the label visible to the user if it is not defined inline between `<FormTab></FormTab>`.

### Customizing Tab Label [​](https://vueform.com/docs/breaking-forms-into-steps#customizing-tab-label)

Tab labels can be passed via default slot or as a string and can contain HTML:

Inline Schema SFC

template

```
<template>
  <FormTab name="first" ...>
    <b>I.</b> First
  </FormTab>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref, h, resolveComponent } from 'vue'

const form = ref({
  tabs: {
    first: {
      label: '<b>I.</b> First',
      elements: ['first_input'],
    },
    // ...
  },
  // ...
})
</script>

<!-- Options API -->
<script>
import { h, resolveComponent } from 'vue'

export default {
  data: () => ({
    forms: {
      tabs: {
        first: {
          label: '<b>I.</b> First',
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      tabs: {
        first: {
          label: '<b>I.</b> First',
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      tabs: {
        first: {
          label: '<b>I.</b> First',
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

... or they can be Vue components:

Inline Schema SFC

template

```
<template>
  <FormTab name="first" ...>
    <AppIcon :icon="['fas', 'id-card']"> First
  </FormTab>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref, h, resolveComponent } from 'vue'

const form = ref({
  tabs: {
    first: {
      label: {
        props: ['form$'],
        render: () => h('span', [
          h(resolveComponent('AppIcon'), {
            icon: ['far', 'id-card']
          }),
          'First',
        ])
      },
      elements: ['first_input'],
    },
    // ...
  },
  // ...
})
</script>

<!-- Options API -->
<script>
import { h, resolveComponent } from 'vue'

export default {
  data: () => ({
    forms: {
      tabs: {
        first: {
          label: {
            props: ['form$'],
            render: () => h('span', [
              h(resolveComponent('AppIcon'), {
                icon: ['far', 'id-card']
              }),
              'First',
            ])
          },
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

vue

```
<!-- Composition API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: (props, context) => {
    const form = useVueform(props, context)

    const vueform = ref({
      tabs: {
        first: {
          label: {
            props: ['form$'],
            render: () => h('span', [
              h(resolveComponent('AppIcon'), {
                icon: ['far', 'id-card']
              }),
              'First',
            ])
          },
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref, h, resolveComponent } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      tabs: {
        first: {
          label: {
            props: ['form$'],
            render: () => h('span', [
              h(resolveComponent('AppIcon'), {
                icon: ['far', 'id-card']
              }),
              'First',
            ])
          },
          elements: ['first_input'],
        },
        // ...
      },
      // ...
    }
  })
}
</script>
```

Tabs API [​](https://vueform.com/docs/breaking-forms-into-steps#tabs-api)
-------------------------------------------------------------------------

We can also reach [`FormTabs`](https://vueform.com/reference/form-tabs) and [`FormTab`](https://vueform.com/reference/form-tab) components' API once they are mounted:

Inline Schema SFC

vue

```
<template>
  <Vueform ref="form$">
    <template #empty>
      <FormTabs>
        <FormTab name="first" ... />
      </FormTabs>
    </template>
  </Vueform>
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.tabs$ // returns FormTabs component instance
  form$.value.tabs$.tabs$.first // returns FormTab component instance named `first`
})
</script>

<!-- Options API -->
<script>
export default {
  mounted() {
    this.$refs.form$.tabs$ // returns FormTabs component instance
    this.$refs.form$.tabs$.tabs$.first // returns FormTab component instance named `first`
  }
}
</script>
```

vue

```
<template>
  <Vueform v-bind="form" ref="form$" />
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const form = ref({
  tabs: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
  },
  // ...
})

onMounted(() => {
  form$.value.tabs$ // returns FormTabs component instance
  form$.value.tabs$.tabs$.first // returns FormTab component instance named `first`
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    tabs: {
      first: {
        label: 'First',
        elements: ['first_input']
      },
    },
    // ...
  }),
  mounted() {
    this.$refs.form$.tabs$ // returns FormTabs component instance
    this.$refs.form$.tabs$.tabs$.first // returns FormTab component instance named `first`
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
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    })

    onMounted(() => {
      form.tabs$.value // returns FormTabs component instance
      form.tabs$.value.tabs$.first // returns FormTab component instance named `first`
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    }
  }),
  mounted() {
    this.tabs$ // returns FormTabs component instance
    this.tabs$.tabs$.first // returns FormTab component instance named `first`
  }
}
</script>
```

Alternatively we can use Vueform's [`@mounted`](https://vueform.com/reference/vueform#event-mounted) event to access `tabs$`:

Inline Schema SFC

template

```
<template>
  <Vueform @mounted="(form$) => {
    form$.tabs$ // returns FormTabs component instance
    form$.tabs$.tabs$.first // returns FormTab component instance named `first`
  }">
    <template #empty>
      <FormTabs>
        <FormTab name="first" ... />
      </FormTabs>
    </template>
  </Vueform>
</template>
```

vue

```
<template>
  <Vueform v-bind="form" />
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const form = ref({
  tabs: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
  },
  onMounted(form$) {
    form$.tabs$ // returns FormTabs component instance
    form$.tabs$.tabs$.first // returns FormTab component instance named `first`
  }
  // ...
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    tabs: {
      first: {
        label: 'First',
        elements: ['first_input']
      },
    },
    onMounted(form$) {
      form$.tabs$ // returns FormTabs component instance
      form$.tabs$.tabs$.first // returns FormTab component instance named `first`
    }
    // ...
  }),
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
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      onMounted(form$) {
        form$.tabs$ // returns FormTabs component instance
        form$.tabs$.tabs$.first // returns FormTab component instance named `first`
      }
      // ...
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      onMounted(form$) {
        form$.tabs$ // returns FormTabs component instance
        form$.tabs$.tabs$.first // returns FormTab component instance named `first`
      },
      // ...
    }
  }),
}
</script>
```

Later we can use check out [`FormTabs`](https://vueform.com/reference/form-tabs) and [`FormTab`](https://vueform.com/reference/form-tab) component reference to see what method and properties can be used.

### Subscribing To Tab Events [​](https://vueform.com/docs/breaking-forms-into-steps#subscribing-to-tab-events)

We can subscribe to [`FormTabs`](https://vueform.com/reference/form-tabs) events like [`@select`](https://vueform.com/reference/form-tabs#event-select) and [`FormTab`](https://vueform.com/reference/form-tab) event like [`@activate`](https://vueform.com/reference/form-tab#event-activate) or [`@inactivate`](https://vueform.com/reference/form-tab#event-inactivate) via Vueform's `tabs$` property:

Inline Schema SFC

vue

```
<template>
  <Vueform ref="form$">
    <template #empty>
      <FormTabs>
        <FormTab name="first" ... />
      </FormTabs>
    </template>
  </Vueform>
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  // Subscribe to FormTabs' @select event
  form$.value.tabs$.on('select', (currentTab$, previousTab$) => {
    // ...
  })
  
  // Subscribe to `first` FormTab's @activate event
  form$.value.tabs$.tabs$.first.on('activate', (tab$) => {
    // ...
  })
})
</script>

<!-- Options API -->
<script>
export default {
  mounted() {
    // Subscribe to FormTabs' @select event
    this.$refs.form$.tabs$.on('select', (currentTab$, previousTab$) => {
      // ...
    })

    // Subscribe to `first` FormTab's @activate event
    this.$refs.form$.tabs$.tabs$.first.on('activate', (tab$) => {
      // ...
    })
  }
}
</script>
```

vue

```
<template>
  <Vueform v-bind="form" ref="form$" />
</template>

<!-- Composition API -->
<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

const form = ref({
  tabs: {
    first: {
      label: 'First',
      elements: ['first_input']
    },
  },
  // ...
})

onMounted(() => {
  // Subscribe to FormTabs' @select event
  form$.value.tabs$.on('select', (currentTab$, previousTab$) => {
    // ...
  })

  // Subscribe to `first` FormTab's @activate event
  form$.value.tabs$.tabs$.first.on('activate', (tab$) => {
    // ...
  })
})
</script>

<!-- Options API -->
<script>
export default {
  data: () => ({
    tabs: {
      first: {
        label: 'First',
        elements: ['first_input']
      },
    },
    // ...
  }),
  mounted() {
    // Subscribe to FormTabs' @select event
    this.$refs.form$.tabs$.on('select', (currentTab$, previousTab$) => {
      // ...
    })
    
    // Subscribe to `first` FormTab's @activate event
    this.$refs.form$.tabs$.tabs$.first.on('activate', (tab$) => {
      // ...
    })
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
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    })

    onMounted(() => {
      // Subscribe to FormTabs' @select event
      form.tabs$.value.on('select', (currentTab$, previousTab$) => {
        // ...
      })

      // Subscribe to `first` FormTab's @activate event
      form.tabs$.value.tabs$.first.on('activate', (tab$) => {
        // ...
      })
    })

    return {
      ...form,
      vueform,
    }
  }
}
</script>

<!-- Options API -->
<script>
import { ref } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      tabs: {
        first: {
          label: 'First',
          elements: ['first_input'],
        },
      },
      // ...
    }
  }),
  mounted() {
    // Subscribe to FormTabs' @select event
    this.tabs$.on('select', (currentTab$, previousTab$) => {
      // ...
    })

    // Subscribe to `first` FormTab's @activate event
    this.tabs$.tabs$.first.on('activate', (tab$) => {
      // ...
    })

  }
}
</script>
```

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
