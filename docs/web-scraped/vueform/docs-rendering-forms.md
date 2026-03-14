# Source: https://vueform.com/docs/rendering-forms

Title: Rendering forms | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/rendering-forms

Markdown Content:
Learn how to render forms using Vueform in three different ways.

Forms can be rendered in several ways:

*   inline, using `<template>` syntax
*   using an SFC with a `vueform` configuration object
*   mixing the two of them.

This chapter is about going through these different options, their basic use cases, pros and cons.

Using Inline Elements [​](https://vueform.com/docs/rendering-forms#using-inline-elements)
-----------------------------------------------------------------------------------------

Once Vueform is installed we can use `<Vueform>` component anywhere in out project:

template

```
<template>
  <div id="app">
    <Vueform></Vueform>
  </div>
</template>
```

When we render a `Vueform` component we create a wrapper for of its elements.

To render elements, we can simply include their components in `Vueform` component:

template

```
<template>
  <div id="app">
    <Vueform>
      <TextElement name="name" ... />
      <TextElement name="email" ... />
    </Vueform>
  </div>
</template>
```

Elements always have a `name` while other options can be passed over as a props:

vue

`<TextElement name="name" label="Name" placeholder="Your name" ... />`

> You can see the list elements and their options available in Vueform in our [Components](https://vueform.com/reference/text-element) reference that you are encouraged to check after finishing this guide.

**Pros**

The benefits of this approach are:

*   intuitiveness
*   form layout can be customized.

**Cons**

The drawbacks of this approach are:

*   redundant writing
*   harder to dynamize.

Using `schema` Object [​](https://vueform.com/docs/rendering-forms#using-schema-object)
---------------------------------------------------------------------------------------

The second approach is defining elements in an object called `schema` instead of writing them inline:

Composition API Options API

vue

```
<template>
  <div id="app">
    <Vueform :schema="schema"></Vueform>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const schema = ref({
  name: { type: 'text', label: 'Name' },
  email: { type: 'text', label: 'Email' }
})
</script>
```

vue

```
<template>
  <div id="app">
    <Vueform :schema="schema"></Vueform>
  </div>
</template>

<script>
export default {
  data: () => ({
    schema: {
      name: { type: 'text', label: 'Name' },
      email: { type: 'text', label: 'Email' }
    }
  })
}
</script>
```

In this case all the elements of the form are defined as a single object and rendered sequentially. The keys in `schema` are the names of the elements, while the values are their options.

This approach enables us to store complete form schemas (or even complete form configurations) in **database** and load them dynamically:

Composition API Options API

vue

```
<script setup>
import { ref, onMounted } from 'vue'

const schema = ref({})

onMounted(async () => {
  schema.value = (await axios.get('/forms/login')).data
})
</script>
```

vue

```
<script>
export default {
  data: () => ({
    schema: {}
  }),
  async mounted() {
    this.schema = (await axios.get('/forms/login')).data
  }
}
</script>
```

**Pros**

The benefits of this approach are:

*   form elements and configration are easier to dynamize
*   less writing

**Cons**

The drawbacks of this approach are:

*   form layout cannot be customized
*   less intuitive

Using Single File Component [​](https://vueform.com/docs/rendering-forms#using-single-file-component)
-----------------------------------------------------------------------------------------------------

The third approach is to create a component and make it _"act"_ like Vueform:

Composition API Options API

vue

```
<!-- ./components/forms/LoginForm.vue -->

<script>
import { ref, onMounted } from 'vue'
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup(props, context) {
    const form = ...useVueform(props, context)

    const vueform = ref({
      schema: {
        email: { type: 'text', label: 'Email' },
        password: { type: 'text', inputType: 'password', label: 'Password' },
      }
    })

    // TIP:
    onMounted(() => {
      // Vueform props and methods can be used here, eg:
      const formData = form.data.value
      form.el$(/*...*/)
      form.update(/*...*/)
    })

    return {
      ...form,
      vueform,
    }
  },
}
</script>
```

vue

```
<!-- ./components/forms/LoginForm.vue -->

<script>
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      schema: {
        email: { type: 'text', label: 'Email' },
        password: { type: 'text', inputType: 'password', label: 'Password' },
      }
    }
  }),
  // TIP:
  mounted() {
    // Vueform props and methods are available via `this`:
    const formData = this.data
    this.el$(/*...*/)
    this.update(/*...*/)
  }
}
</script>
```

As we can see we are using `Vueform` and `useVueform` to make our component behave as Vueform.

The `Vueform` mixin is responsible for adding Vueform's `props` to the component, so it can still accept configuration options from the outside.

The `useVueform` composable brings a set of properties and methods defined with Composition API that gives the core functionality of Vueform.

The third thing we can inspect, is that `schema` is defined in the `vueform` object. The `vueform` object is where we configure [default options](https://vueform.com/reference/vueform#options) for the form. Later these options can even be **extended** via component props.

What does it mean? Let's see an example.

This is how we would use `LoginForm.vue` in an application:

template

```
<template>
  <div id="app">
    <LoginForm />
  </div>
</template>
```

This will render the `email` and `password` elements as we defined previously in our component.

Now what if we'd like to add some other elements to the form? For example adding a "Login" button with different colors or different label in different places of the application, but using the same login form.

That's something we can do as Vueform **combines** its default configuration and the props provided to it:

template

```
<template>
  <div id="app">
    <LoginForm :schema="{
      button: { type: 'button', buttonLabel: 'Login', submits: true }
    }" />
  </div>
</template>
```

**When using Vueform as an SFC, it combines its internal configuration (`vueform`) with the options it receives as props.**

The following options are being merged when they both exist in `data().vueform` object and as a prop:

*   [`schema`](https://vueform.com/reference/vueform#option-schema)
*   [`tabs`](https://vueform.com/reference/vueform#option-tabs)
*   [`steps`](https://vueform.com/reference/vueform#option-steps)

Everything else is **overwritten** by the **props** provided to the component.

### Customizing Form Layout [​](https://vueform.com/docs/rendering-forms#customizing-form-layout)

Using Vueform as an SFC not only gives us the opportunity to create base configurations, but we can create base **form layouts** as well.

Let's stick to our previous example, but instead of defining elements in `schema` let's use a custom `<template>` with inline elements:

vue

```
<!-- ./components/forms/LoginForm.vue -->

<template>
  <form>
    <div class="w-full flex">
      <div class="w-1/2"><TextElement name="email" label="Email" /></div>
      <div class="w-1/2"><TextElement name="password" label="Password" /></div>
    </div>
  </form>
</template>

<script>
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
}
</script>
```

This will render the `email` and `password` fields next to each other (using Tailwind CSS utility classes). As you've probably noticed we are not using `vueform` object. This is because element options are already defined inline so we don't need `schema` (as in our first example).

Our `LoginForm` is still just a regular component that has some properties and methods provided by `Vueform` mixin and `useVueform` setup function.

So if we want we can provide custom props and use them in our template:

vue

```
<!-- ./components/forms/LoginForm.vue -->

<template>
  <form>
    <div class="w-full flex">
      <div :class="`w-${width}`"><TextElement name="email" label="Email" /></div>
      <div :class="`w-${width}`"><TextElement name="password" label="Password" /></div>
    </div>
  </form>
</template>

<script>
import { Vueform, useVueform } from '@vueform/vueform'

export default {
  mixins: [Vueform],
  setup: useVueform,
  props: {
    width: {
      required: false,
      type: String,
      default: '1/2'
    }
  }
}
</script>
```

And then we can override default element width when using the `LoginForm` component with `width` prop:

vue

```
<template>
  <div id="app">
    <LoginForm width="full" />
  </div>
</template>
```

> **Note:** element widths can be customized with `columns` option much easier as you'll learn later.

**Pros**

The benefits of using Single File Components are:

*   easier to reusability
*   leverage compositions
*   form layout still can be customized
*   form configuration can be dynamized

**Cons**

The drawbacks of using Single File Components are:

*   requires a separate file
*   harder to read/write

Which Approach to Choose? [​](https://vueform.com/docs/rendering-forms#which-approach-to-choose)
------------------------------------------------------------------------------------------------

It depends on your use case.

The **basic recommended** approach is using [template syntax](https://vueform.com/docs/rendering-forms#using-inline-elements) by default as that's the cleanest, most intuitive way that other developers will also understand the easiest.

If you need **dynamic** forms, because you are adding/removing elements, changing configuration on runtime or loading them from database you should use [schema object](https://vueform.com/docs/rendering-forms#using-schema-object) or [Single File Components](https://vueform.com/docs/rendering-forms#using-single-file-component).

If you explicitly want to **reuse** or oursource more complex forms into separate files you should go with [Single File Components](https://vueform.com/docs/rendering-forms#using-single-file-component).

Web Components [​](https://vueform.com/docs/rendering-forms#web-components)
---------------------------------------------------------------------------

Please check out the following example to learn how to render forms using [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components):

[https://stackblitz.com/edit/github-lkevth?file=src%2Fmain.js,index.html,src%2Fcomponents%2FMyForm.vue](https://stackblitz.com/edit/github-lkevth?file=src%2Fmain.js,index.html,src%2Fcomponents%2FMyForm.vue)

Using in Nuxt [​](https://vueform.com/docs/rendering-forms#using-in-nuxt)
-------------------------------------------------------------------------

Vueform currently does not support SSR, so when used in Nuxt it needs to be wrapped in `client-only`:

template

```
<template>
  <ClientOnly>
    <Vueform></Vueform>
  </ClientOnly>
</template>
```

Further Reading [​](https://vueform.com/docs/rendering-forms#further-reading)
-----------------------------------------------------------------------------

Vueform can not only display elements, but also other components like [`FormSteps`](https://vueform.com/reference/form-steps) or [`FormTabs`](https://vueform.com/reference/form-tabs). Besides it offers various configuration options that you can be learned by checking out [`Vueform`](https://vueform.com/reference/vueform#options) API.

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
