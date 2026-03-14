# Source: https://vueform.com/docs/creating-elements

Title: Creating Elements | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/creating-elements

Markdown Content:
Learn how to create a new element with custom features or integrate a third party component.

Generic Element [​](https://vueform.com/docs/creating-elements#generic-element)
-------------------------------------------------------------------------------

We can use the following boilerplate to create a new Vueform element:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <!-- ADD YOUR ELEMENT TEMPLATE HERE -->
    </template>

    <!-- Default element slots -->
    <template v-for="(component, slot) in elementSlots" #[slot]><slot :name="slot" :el$="el$"><component :is="component" :el$="el$"/></slot></template>
  </ElementLayout>
</template>

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      // ...
    }
  })
</script>
```

This will create a [GenericElement](https://vueform.com/reference/generic-element) which has all the generic features such as value or validation out-of-the-box that can be used and extended further.

Name [​](https://vueform.com/docs/creating-elements#name)
---------------------------------------------------------

The name defines the `type` or the _first part_ of the component name when used inline.

> **IMPORTANT:** the element name must end with `Element`.

Let's define our new element's name:

js

```
export default defineElement({
  name: 'MyAwesomeElement',
})
```

Later it can by used like this:

js

```
schema: {
  my_element: {
    type: 'my-awesome'
  }
}
```

or like this:

vue

```
<!-- App.vue -->

<template> 
  <Vueform>
    <MyAwesomeElement name="my_element" />
  </Vueform>
</template>
```

Registering Elements [​](https://vueform.com/docs/creating-elements#registering-elements)
-----------------------------------------------------------------------------------------

New elements can be registered in `vueform.config.js`:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'
import CustomElement from './CustomElement.vue'

export default defineConfig({
  elements: [
    CustomElement,
  ],
  // ...
})
```

Template [​](https://vueform.com/docs/creating-elements#template)
-----------------------------------------------------------------

In the `<template>` part we use the [`ElementLayout`](https://vueform.com/reference/element-layout) component as a wrapper for our element and we define the actual element template in `#element` slot:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <input /> <!-- this will render a basic, unstyled input field -->
    </template>
    <!-- ... -->
  </ElementLayout>
</template>
```

In the following sections we will learn how we can extend our element with actual features.

Props [​](https://vueform.com/docs/creating-elements#props)
-----------------------------------------------------------

### Generic Props [​](https://vueform.com/docs/creating-elements#generic-props)

The first argument of `setup()` is `props`, that we can use to access our element's custom props and the props provided by GenericElement:

Show all

vue

```
<!-- CustomElement.vue -->

<script>
  import { toRefs } from 'vue'
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, context) {
      const { type } = toRefs(props)

      console.log(type.value) // 'custom' - the element type

      console.log(Object.keys(props))

      /* Output: [
        "addClass",
        "addClasses",
        "after",
        "before",
        "between",
        "columns",
        "conditions",
        "default",
        "description",
        "disabled",
        "fieldName",
        "formatData",
        "formatLoad",
        "id",
        "info",
        "infoPosition",
        "inline",
        "label",
        "layout",
        "messages",
        "name",
        "onBeforeCreate",
        "onBeforeMount",
        "onBeforeUnmount",
        "onBeforeUpdate",
        "onChange",
        "onCreated",
        "onMounted",
        "onUnmounted",
        "onUpdated",
        "overrideClass",
        "overrideClasses",
        "presets",
        "removeClass",
        "removeClasses",
        "replaceClass",
        "replaceClasses",
        "rules",
        "size",
        "slots",
        "submit",
        "templates",
        "type",
        "view",
        "views"
      ] */
    }
  })
</script>
```

> Always make sure to transform `props` with `toRefs()` before using them, to keep their reactivity.

All of these props can be used in our element's template:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      {{ id }} {{ disabled }} {{ ... }}
    </template>
  </ElementLayout>
</template>
```

The generic props (or configuration options) are described in GenericElement's [Components / Options](https://vueform.com/reference/generic-element#options).

### Custom Props [​](https://vueform.com/docs/creating-elements#custom-props)

We can add custom props to our element:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    props: {
      customProp: {
        type: String,
        required: false,
        default: 'custom',
      }
    },
    // ...
  })
</script>

<template>
  <ElementLayout>
    <template #element>
      {{ customProp }}
    </template>
    <!-- ... -->
  </ElementLayout>
</template>
```

Properties and Methods [​](https://vueform.com/docs/creating-elements#properties-and-methods)
---------------------------------------------------------------------------------------------

### Generic Properties and Methods [​](https://vueform.com/docs/creating-elements#generic-properties-and-methods)

The second argument of `setup()` is `context`, which contains an `element` property, that we can use to access the GenericElement's [Properties](https://vueform.com/reference/generic-element#properties) and [Methods](https://vueform.com/reference/generic-element#methods).

Here's an example of how we can use our element's [`update()`](https://vueform.com/reference/generic-element#method-update) method:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      const { update } = element

      // This will update the element's value,
      // using the GenericElement's `update` method:
      update('value')
    }
  })
</script>
```

> **The `element` variable in `context` gives access to the GenericElement's API.**

All the properties and methods provided by the GenericElement can be used in our element's template:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <input
        :value="value"
        v-bind="aria"
        @input="handleInput"
      />
    </template>
  </ElementLayout>
</template>
```

#### All Generic Properties and Methods [​](https://vueform.com/docs/creating-elements#all-generic-properties-and-methods)

Here's the full list of properties and methods that are available in a GenericElement (`element` is now deconstructed from `context`):

Show all

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      console.log(Object.keys(element))

      /* Output: [
        "activate",
        "active",
        "addConditions",
        "additionalConditions",
        "aria",
        "available",
        "busy",
        "classes",
        "classesInstance",
        "clean",
        "clear",
        "clearMessages",
        "cols",
        "columnsClasses",
        "columnsClassesService",
        "conditionList",
        "container",
        "data",
        "dataPath",
        "deactivate",
        "debouncing",
        "defaultValue",
        "descriptionId",
        "dirt",
        "dirty",
        "disable",
        "el$",
        "elementLayout",
        "elementSlots",
        "empty",
        "enable",
        "error",
        "errorId",
        "errors",
        "events",
        "fieldId",
        "fieldSlots",
        "fire",
        "flat",
        "focus",
        "focused",
        "form$",
        "genericName",
        "handleInput",
        "hasLabel",
        "hidden",
        "hide",
        "infoId",
        "initMessageBag",
        "initValidation",
        "initWatcher",
        "initialValue",
        "input",
        "internalValue",
        "invalid",
        "isActive",
        "isArrayType",
        "isDanger",
        "isDisabled",
        "isFileType",
        "isImageType",
        "isStatic",
        "isSuccess",
        "Label",
        "labelId",
        "listeners",
        "load",
        "localDisabled",
        "messageBag",
        "model",
        "mounted",
        "nullValue",
        "off",
        "on",
        "parent",
        "path",
        "pending",
        "prepare",
        "reinitValidation",
        "removeConditions",
        "requestData",
        "reset",
        "resetValidators",
        "show",
        "Size",
        "state",
        "template",
        "Templates",
        "theme",
        "update",
        "updateColumns",
        "updateConditions",
        "validate",
        "validated",
        "validationRules",
        "Validators",
        "value",
        "View",
        "Views",
        "visible"
      ] */
    }
  })
</script>
```

You can find most of the properties and methods in the GenericElement's reference under [Properties](https://vueform.com/reference/generic-element#properties) and [Methods](https://vueform.com/reference/generic-element#methods).

For the others, which aren't publicly documented, you can check directly the GenericElement's source: [https://github.com/vueform/vueform/blob/main/src/components/elements/GenericElement.js](https://github.com/vueform/vueform/blob/main/src/components/elements/GenericElement.js).

### Generic Overrides [​](https://vueform.com/docs/creating-elements#generic-overrides)

We can override the default properties and methods of the GenericElement by exporting the same key.

Say we have a third party component that we want to use as the input for our element. It emits the value in a different format than what [handleInput](https://github.com/vueform/vueform/blob/main/src/composables/elements/useHandleInput.js#L16) can manage.

For the sake of the example and to keep things consistent let's replace the `handleInput` with a custom handler instead of creating a completely different one:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      const { model } = element

      const handleInput = (value) => {
        model.value = value
      }

      return {
        handleInput,
      }
    },
  })
</script>

<template>
  <ElementLayout>
    <template #element>
      <ThirdPartyComponent
        @input="handleInput"
      />
    </template>
    <!-- ... -->
  </ElementLayout>
</template>
```

Now when `ThirdPartyComponent` emits the `input` event, our element's value will change.

##### The steps we took: [​](https://vueform.com/docs/creating-elements#the-steps-we-took)

*   first noticed that there is a `handleInput` method [provided by our element](https://vueform.com/docs/creating-elements#all-generic-properties-and-methods)
*   we looked for a composable in the [GenericElement's source](https://github.com/vueform/vueform/blob/main/src/components/elements/GenericElement.js#L19) that might contain this method (the `useHandleInput` composable seemed like a good direction to investigate further)
*   we looked at [`useHandleInput` composable's source](https://github.com/vueform/vueform/blob/main/src/composables/elements/useHandleInput.js#L16) and found where `handleInput` method is defined there
*   we saw that the default `handleInput` is using `e.target.value` to update the element value (via [`model`](https://github.com/vueform/vueform/blob/main/src/composables/elements/useValue.js#L86)) which will not be suitable for out use-case
*   we created an override for `handleInput` in the example above and we implemented our custom value update mechanism that is compatible with our third party library.

You can follow these steps anytime you need to change the original behavior of the custom element. An important take-away is that in most cases you need to check out the actual source code to see what you have to change.

### Custom Properties and Methods [​](https://vueform.com/docs/creating-elements#custom-properties-and-methods)

We can use element's `setup()` to add different props, methods, watchers, etc. to the element using Composition API:

vue

```
<!-- CustomElement.vue -->

<script>
  import { ref, computed } from 'vue'
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, context) {
      const customRef = ref('custom-ref-value')
      const customComputed = computed(() => 'custom-computed-value')
      // methods, hooks, watchers, etc...

      return {
        customRef,
        customComputed,
        // ...
      }
    }
  })
</script>

<template>
  <ElementLayout>
    <template #element>
      {{ customRef }}
      {{ customComputed }}
    </template>
    <!-- ... -->
  </ElementLayout>
</template>
```

Input [​](https://vueform.com/docs/creating-elements#input)
-----------------------------------------------------------

One of the most likely thing we will want to do is to add some kind of an input for our element.

This can be a native HTML input like `<input>` or a third party component like `<ckeditor>`.

Regardless which one is it, it's useful to add a reference for it, so that we can later reach it via the element:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <input ref="input" ... />
    </template>
  </ElementLayout>
</template>
```

or:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <ckeditor ref="input" ... />
    </template>
  </ElementLayout>
</template>
```

Later we can reach the input field or component directly once the component is mounted:

vue

```
<!-- App.vue -->

<template>
  <Vueform ref="form$">
    <CustomElement name="custom" />
  </Vueform>
</template>

<script setup>
import { ref } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.el$('custom').input // returns the `<input>` element or the `<ckeditor>` component
})
</script>
```

> The `input` is the standard property used to reach an element's actual input field.

Value [​](https://vueform.com/docs/creating-elements#value)
-----------------------------------------------------------

By default an element's value is included in form [`data`](https://vueform.com/reference/vueform#property-data):

vue

```
<!-- App.vue -->

<template>
  <Vueform ref="form$">
    <CustomElement name="custom" />
  </Vueform>
</template>

<script setup>
import { ref } from 'vue'

const form$ = ref(null)

onMounted(() => {
  console.log(form$.value.data) // Form data: { custom: null }
  console.log(form$.value.el$('custom').value) // Element value: null
})
</script>
```

The element's value is `null` by default.

### update() [​](https://vueform.com/docs/creating-elements#update)

Let's go ahead, and set a value for our custom element using [`update()`](https://vueform.com/reference/generic-element#method-update) upon element creation:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      const { update } = element

      update('foo')
    }
  })
</script>
```

Now our output should be `'foo'`:

js

```
onMounted(() => {
  console.log(form$.value.data) // { custom: 'foo' }
  console.log(form$.value.el$('custom').value) // 'foo'
})
```

### value [​](https://vueform.com/docs/creating-elements#value-1)

Alternatively we can update the [`value`](https://vueform.com/reference/generic-element#property-value) property directly, which will have the same result:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      const { value } = element

      value.value = 'foo'
    }
  })
</script>
```

Result:

js

```
onMounted(() => {
  console.log(form$.value.data)// { custom: 'foo' }
  console.log(form$.value.el$('custom').value) // 'foo'
})
```

We can use the `value` property to retrieve the element's value anytime.

### v-model [​](https://vueform.com/docs/creating-elements#v-model)

Now we are only a step away of implementing **two-way data binding** for our custom element.

Let's add an `<input>` and `v-model` to our element:

vue

```
<!-- App.vue -->

<template>
  <ElementLayout>
    <template #element>
      <input
        v-model="value"
      />
    </template>
  </ElementLayout>
</template>
```

Now every time our element's input field's value changes, it will be reflected in the element's value and vice-verse.

We might also deconstruct the `v-model` to `value` and `@input` for custom or third party components:

vue

```
<!-- App.vue -->

<template>
  <ElementLayout>
    <template #element>
      <ThirdPartyComponent
        :value="value"
        @input="handleInput"
      />
    </template>
  </ElementLayout>
</template>
```

The `handleInput` method is included in the [`useHandleInput`](https://github.com/vueform/vueform/blob/main/src/composables/elements/useHandleInput.js) composable, which is used by the GenericElement and sets the element's value using `target.value`.

You are free to implement your own `handleInput` or similar method, that works with non-native HTML elements as well.

### nullValue [​](https://vueform.com/docs/creating-elements#nullvalue)

The element's value is `null` by default. This might not be ideal if we create an element that has eg. an `array` data type.

We can define what the `null` state should look like for an element with `nullValue`, which should be exported directly from the component:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    nullValue: [], // `null` state will be an empty array instead of `null`
    // ...
  })
</script>
```

Validation [​](https://vueform.com/docs/creating-elements#validation)
---------------------------------------------------------------------

Vueform's validation engine can validate any elements' value, including our custom element's value without any further configuration:

vue

```
<!-- App.vue -->

<template>
  <Vueform ref="form$">
    <CustomElement
      name="custom"
      rules="required|min:5|max:255|..."
    />
  </Vueform>
</template>
```

Events [​](https://vueform.com/docs/creating-elements#events)
-------------------------------------------------------------

We can define events for our element using providing them in the `emits` array:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    emits: ['custom-event'],
    // ...
  })
</script>
```

Later, we can use the `fire()` method to fire the event from the element:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    emits: ['custom-event'],
    setup(props, { element }) {
      const { fire } = element

      fire('custom-event', 'foo', 'bar')
    }
  })
</script>
```

We are using `fire()` instead of the native `context.emit()` because this way, we can listen to events when our element is defined in the schema as well:

vue

```
<!-- App.vue -->

<template>
  <!-- Subscribing to the event inline -->
  <Vueform>
    <CustomElement
      name="custom"
      @custom-event="handleCustomEvent"
    />
  </Vueform>

  <!-- Subscribing to the event using schema -->
  <Vueform :schema="schema" />
</template>

<script setup>
import { ref } from 'vue'

const schema = ref({
  custom: {
    type: 'custom',
    onCustomEvent: (foo, bar) => { ... }
  }
})
</script>
```

Classes [​](https://vueform.com/docs/creating-elements#classes)
---------------------------------------------------------------

Vueform has a built-in mechanism for handling classes. Each Vueform component has a `defaultClasses` and `classes` property.

The `defaultClasses` is an object where we can define the classes to be used within the component.

The `classes` property is used by the component's template to access the 'final' classes, which might include some on-the-flight changes.

In every Vueform element we can use class modifiers like `addClasses` or `replaceClasses` that will change how the final class list should look like for the element.

Let's add some classes for our element:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <div :class="classes.inputWrapper">
        <input :class="classes.input" />
      </div>
    </template>
    <!-- ... -->
  </ElementLayout>
</template>

<script>
  import { ref } from 'vue'
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      const defaultClasses = ref({
        container: '', // added to the element's outermost DOM in ElementLayout
        inputWrapper: 'w-full',
        input: 'border',
        input_sm: 'text-sm',
        input_md: 'text-base',
        input_lg: 'text-lg',
        $input: (classes, { Size }) => ([
          classes.input,
          classes[`input_${Size}`],
        ])
      })

      return {
        defaultClasses,
      }
    }
  })
</script>
```

The `container` class is added to the `ElementLayout`'s outermost DOM - we leave it blank for now.

We added the `inputWrapper` class, which returns `w-full` by default.

We defined `input`, `input_sm`, `input_md`, `input_lg` and the `$input()` function which all seems to be connected.

What we want to achieve for `input` class is that it has `border` class in any cases, `text-sm` when the element's [Size](https://vueform.com/reference/generic-element#property-Size) is `sm`, `text-base` if `md` and `text-lg` if `lg`.

To avoid having complex class logic in our template, we can define the `$input()` function, so Vueform knows when `classes.input` is used, it should use the calculated value of `$input()` if it exists instead of the static `input`.

This can be used for any class, the only requirement is that the function name equals to the class we want to replace and it's prefixed with `$`. The function's first argument is the `classes` object, which equals to `defaultClasses` and anything can be retrieved from it. The second argument is the [`el$`](https://vueform.com/reference/generic-element#property-el_) element instance itself, so all of our element's options, properties and methods are available.

This method can be used to contain complex logic in single class names and keep our templates clean.

Slots [​](https://vueform.com/docs/creating-elements#slots)
-----------------------------------------------------------

### Generic Slots [​](https://vueform.com/docs/creating-elements#generic-slots)

In the second part of our [Boilerplate](https://vueform.com/docs/creating-elements#generic-element) template we pass over all the generic slots for the `ElementLayout`:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <!-- ... -->
    <template v-for="(component, slot) in elementSlots" #[slot]><slot :name="slot" :el$="el$"><component :is="component" :el$="el$"/></slot></template>
  </ElementLayout>
</template>
```

This enables us to use inline slots for generic slots like _label_, _description_, etc:

vue

```
<!-- App.vue -->

<template>
  <Vueform>
    <CustomElement name="custom">
      <template #label>Foo</template>
      <template #description>Bar</template>
    </CustomElement>
  </Vueform>
</template>
```

The following generic slots are available for a new element:

*   `label`
*   `info`
*   `description`
*   `before`
*   `between`
*   `after`

### Custom Slots [​](https://vueform.com/docs/creating-elements#custom-slots)

To add a custom slot, we can define a `<slot>` within our template:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <slot name="custom" :my-param="myParam" />
      <!-- REST OF THE ELEMENT TEMPLATE -->
    </template>
    <template v-for="(component, slot) in elementSlots" #[slot]><slot :name="slot" :el$="el$"><component :is="component" :el$="el$"/></slot></template>
  </ElementLayout>
</template>
```

After this we will be able to use our `#custom` slot:

vue

```
<!-- App.vue -->

<template>
  <Vueform>
    <CustomElement name="custom">
      <template #custom="{ myParam }">
        Custom text with {{ myParam }}
      </template>
    </CustomElement>
  </Vueform>
</template>
```

Components [​](https://vueform.com/docs/creating-elements#components)
---------------------------------------------------------------------

We can pass components to our custom element:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'
  import MyComponent from './MyComponent'

  export default defineElement({
    name: 'CustomElement',
    components: {
      MyComponent,
    },
    // ...
  })
</script>

<template>
  <ElementLayout>
    <template #element>
      <MyComponent />
      <!-- REST OF THE ELEMENT TEMPLATE -->
    </template>
    <!-- ... -->
  </ElementLayout>
</template>
```

Mixins [​](https://vueform.com/docs/creating-elements#mixins)
-------------------------------------------------------------

We can pass mixins to our custom element:

vue

```
<!-- CustomElement.vue -->

<script>
  import { defineElement } from '@vueform/vueform'
  import MyMixin from './MyMixin'

  export default defineElement({
    name: 'CustomElement',
    mixins: [MyMixin],
    // ...
  })
</script>
```

> Using mixins is [**no longer recommended**](https://vuejs.org/api/options-composition.html#mixins). Mixins were the primary mechanism for creating reusable chunks of component logic. While mixins continue to be supported in Vue 3, Composable functions using Composition API is now the preferred approach for code reuse between components.

Copy Element [​](https://vueform.com/docs/creating-elements#copy-element)
-------------------------------------------------------------------------

We can copy any existing Vueform element, apply changes to it and use it as a new element type.

In this example we will copy the `EditorElement`.

### Script [​](https://vueform.com/docs/creating-elements#script)

First we have to add `EditorElement` to our custom element, then override `name` and `setup()`:

vue

```
<!-- CustomElement.vue -->

<script>
  import { EditorElement } from '@vueform/vueform'

  export default {
    ...EditorElement, // adding props, mixins, emits
    name: 'CustomElement',
    setup(props, context) {
      const element = EditorElement.setup(props, context)

      return {
        ...element
      }
    }
  })ó
</script>
```

As we are overriding `EditorElement`'s `setup()` we need to manually run it, which will give us the `element` variable, that will contain the properties and methods of the `EditorElement`.

When copying elements we need to return the `element` from our custom element so the copied element's properties and methods are all exported.

### Template [​](https://vueform.com/docs/creating-elements#template-1)

The next step is to add the `EditorElement`'s template. There are two ways to do this.

##### Copy template for changes [​](https://vueform.com/docs/creating-elements#copy-template-for-changes)

If we **want to change** the original element's template, we can look up its template in the [source](https://github.com/vueform/vueform/blob/main/themes/blank/templates/elements/EditorElement.vue) and copy it:

vue

```
<!-- CustomElement.vue -->

<template>
  <component :is="elementLayout" ref="container">
    <template #element>
      <EditorWrapper
        :value="model"
        :placeholder="Placeholder"
        :id="fieldId"
        :accept="accept"
        :accept-mimes="acceptMimes"
        :endpoint="editorEndpoint"
        :method="editorMethod"
        :disabled="isDisabled"
        :hide-tools="hideTools"
        :class="classes.input"
        :attrs="aria"
        @input="handleInput"
        @alert="handleAlert"
        @error="handleError"
        @blur="handleBlur"
        ref="input"
     />
    </template>

    <!-- Default element slots -->
    <template v-for="(component, slot) in elementSlots" #[slot]><slot :name="slot" :el$="el$"><component :is="component" :el$="el$"/></slot></template>
  </component>
</template>

<script>
  import { EditorElement } from '@vueform/vueform'

  export default {
    ...EditorElement, // adding props, mixins, emits
    name: 'CustomElement',
    setup(props, context) {
      const element = EditorElement.setup(props, context)

      return {
        ...element
      }
    }
  }
</script>
```

##### Copy template without changing it [​](https://vueform.com/docs/creating-elements#copy-template-without-changing-it)

If we **do not want to change** the original element's template, we can just add the `EditorElement`'s template to our custom element (which will in fact add `render` and `staticRenderFns`):

vue

```
<!-- CustomElement.vue -->

<script>
  import { EditorElement } from '@vueform/vueform'
  import { EditorElement as EditorElementTemplate } from '@vueform/vueform/dist/[theme_name]'

  export default {
    ...EditorElement, // adding props, mixins, emits
    ...EditorElementTemplate,
    name: 'CustomElement',
    setup(props, context) {
      const element = EditorElement.setup(props, context)

      return {
        ...element
      }
    }
  }
</script>
```

Make sure to no `<template>` or `<style>` block is defined for the element in this case and to replace the `[theme_name]` with the theme you use.

### Style [​](https://vueform.com/docs/creating-elements#style)

The last step is to copy the classes of the `EditorElement` to our `defaultClasses`.

##### Named class based themes [​](https://vueform.com/docs/creating-elements#named-class-based-themes)

If we are using `vueform`, `material` or `bootstrap` theme, we can copy the default classes directly from the component's template:

vue

```
<!-- CustomElement.vue -->

<script>
  import { ref } from 'vue'
  import { EditorElement } from '@vueform/vueform'
  import { EditorElement as EditorElementTemplate } from '@vueform/vueform/dist/[theme_name]'

  export default {
    ...EditorElement, // adding props, mixins, emits
    name: 'CustomElement',
    setup(props, context) {
      const element = EditorElement.setup(props, context)

      const defaultClasses = ref({
        ...EditorElementTemplate.data().defaultClasses,
      })

      return {
        defaultClasses,
        ...element,
      }
    }
  }
</script>
```

Make sure to replace the `[theme_name]` with the theme you use.

In this case styles will come from the globally imported theme's CSS file. The `defaultClasses` can be changed and `<style>` block may be used for our custom element to define custom styles.

##### Utility class based themes [​](https://vueform.com/docs/creating-elements#utility-class-based-themes)

If we are using `tailwind` or `tailwind_material` theme, we can copy the `EditorElement`'s classes directly from the theme's `classes` object:

vue

```
<!-- CustomElement.vue -->

<script>
  import { ref } from 'vue'
  import { EditorElement } from '@vueform/vueform'
  import { classes } from '@vueform/vueform/dist/[theme_name]'

  export default {
    ...EditorElement, // adding props, mixins, emits
    name: 'CustomElement',
    setup(props, context) {
      const element = EditorElement.setup(props, context)

      const defaultClasses = ref({
        ...classes.EditorElement,
      })

      return {
        defaultClasses,
        ...element,
      }
    }
  }
</script>
```

Make sure to replace the `[theme_name]` with the theme you use.

In this case styles will come from utility classes, which can be edited in the `defaultClasses` object.

Examples [​](https://vueform.com/docs/creating-elements#examples)
-----------------------------------------------------------------

### Simple Example [​](https://vueform.com/docs/creating-elements#simple-example)

Here's how we can create a very simple text input field that uses the element's `model` and dynamic classes:

vue

```
<!-- CustomElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <input
        v-model="model"
        :class="classes.input"
      />
    </template>

    <!-- Default element slots -->
    <template v-for="(component, slot) in elementSlots" #[slot]><slot :name="slot" :el$="el$"><component :is="component" :el$="el$"/></slot></template>
  </ElementLayout>
</template>

<script>
  import { ref } from 'vue'
  import { defineElement } from '@vueform/vueform'

  export default defineElement({
    name: 'CustomElement',
    setup(props, { element }) {
      const defaultClasses = ref({
        container: '', // added automatically to the element's outermost DOM in ElementLayout
        input: 'form-text-input',
        input_danger: 'has-errors',
        $input: (classes, { isDanger }) => ([
          classes.input,
          isDanger ? classes.input_danger : null,
        ])
      })

      return {
        defaultClasses,
      }
    }
  })
</script>

<style lang="scss">
  .form-text-input {
    border: 1px solid black;
    outline: none;
    width: 100%;

    &.has-errors {
      border: 1px solid red;
    }
  }
</style>
```

> If a class name has a counterpart prefixed with `$` function, it will be dynamic. The function's first argument is the class list and the second is the component properties.

Now if we use it we'll have a simple input field with a red border if it has any errors:

vue

```
<!-- App.vue -->

<template>
  <Vueform>
    <CustomElement name="custom" rules="email" />
  </Vueform>
</template>
```

### Advanced Example [​](https://vueform.com/docs/creating-elements#advanced-example)

If we'd like to create a more advanced element in terms of

vue

```
<!-- BirthdayElement.vue -->

<template>
  <ElementLayout>
    <template #element>
      <div :class="classes.wrapper">
        <select v-model="day" :class="classes.day">
          <option v-for="day, i in days" :value="day" :key="i">
            {{ day }}
          </option>
       </select>
        <select v-model="month" :class="classes.month">
          <option v-for="month, i in months" :value="month[0]" :key="i">
            {{ month[1] }}
          </option>
       </select>
        <select v-model="year" :class="classes.year">
          <option v-for="year, i in years" :value="year" :key="i">
            {{ year }}
          </option>
       </select>
      </div>
    </template>
    <template v-for="(component, slot) in elementSlots" #[slot]><slot :name="slot" :el$="el$"><component :is="component" :el$="el$"/></slot></template>
  </ElementLayout>
</template>

<script>
  import { defineElement } from '@vueform/vueform'
  import { ref, computed } from 'vue'

  export default defineElement({
    name: 'BirthdayElement',
    setup(props, { element }) {
      const months = ref([
        ['01', 'January'],
        ['02', 'February'],
        ['03', 'March'],
        ['04', 'April'],
        ['05', 'May'],
        ['06', 'June'],
        ['07', 'July'],
        ['08', 'August'],
        ['09', 'September'],
        ['10', 'October'],
        ['11', 'November'],
        ['12', 'December'],
      ])
      const days = ref([...Array(31).keys()].map(i=>i<9?'0'+(i+1):String(i+1)))
      const years = ref([...Array(100).keys()].map(i=>(new Date().getFullYear())-i))

      // Creating models for day, month, year from the element's model
      const datePart = (part) => {
        return {
          get: () => {
            return (element.model.value||'').split('-')[part]||null
          },
          set: (value) => {
            let date = (element.model.value||'').split('-')
            date[part] = value

            element.model.value = `${date[0]||'0000'}-${date[1]||'00'}-${date[2]||'00'}`
          }
        }
      }

      const day = computed(datePart(2))
      const month = computed(datePart(1))
      const year = computed(datePart(0))

      return {
        day,
        month,
        year,
        months,
        days,
        years,
      }
    },
    data() {
      return {
        defaultClasses: {
          container: '',
          wrapper: 'form-input-wrapper',
          input: 'form-text-input',
          day: 'day',
          month: 'month',
          year: 'year',
          $day: (classes) => ([
            classes.input,
            classes.day,
          ]),
          $month: (classes) => ([
            classes.input,
            classes.month,
          ]),
          $year: (classes) => ([
            classes.input,
            classes.year,
          ]),
        },
      }
    },
  })
</script>

<style lang="scss">
.form-input-wrapper {
  width: 100%;
  display: flex;
  column-gap: 0.5rem;
}

.form-text-input {
  border: 1px solid #000000;
  padding: 0.25rem 0.5rem;
  appearance: auto;

  &.day {
    width: calc(3 / 12 * 100%);
  }

  &.month {
    width: calc(5 / 12 * 100%);
  }

  &.year {
    width: calc(4 / 12 * 100%);
  }
}
</style>
```

We can use the created element as `BirthdayElement`:

vue

```
<!-- BirthdayElement.vue -->

<template>
  <Vueform>
    <BirthdayElement name="birthday" label="Birthday" rules="after:2022-02-01" />
  </Vueform>
</template>
```

Support [​](https://vueform.com/docs/creating-elements#support)
---------------------------------------------------------------

Creating elements after a certain point can become quite complex. When in doubt there are a couple of things you can do however.

### Check the Source [​](https://vueform.com/docs/creating-elements#check-the-source)

It's useful to examine how existing Vueform element are composed: [https://github.com/vueform/vueform/tree/main/src/components/elements](https://github.com/vueform/vueform/tree/main/src/components/elements)

It's also useful to check what functionalities composables add to certain elements: [https://github.com/vueform/vueform/tree/main/src/composables](https://github.com/vueform/vueform/tree/main/src/composables)

For element templates, this is the best place to look at: [https://github.com/vueform/vueform/tree/main/themes/blank/templates/elements](https://github.com/vueform/vueform/tree/main/themes/blank/templates/elements)

### Discuss on GitHub [​](https://vueform.com/docs/creating-elements#discuss-on-github)

Our GitHub Discussions are open to questions about the usage of Vueform including creating complex elements: [https://github.com/vueform/vueform/discussions/categories/questions](https://github.com/vueform/vueform/discussions/categories/questions)

### Discuss on Discord [​](https://vueform.com/docs/creating-elements#discuss-on-discord)

We're a welcoming community of developers and happy to help on our Discord server as well: [https://discord.gg/WhX2nG6GTQ](https://discord.gg/WhX2nG6GTQ)

### Pro Support [​](https://vueform.com/docs/creating-elements#pro-support)

If you're looking for our team's help either in the form of implementation or consulting, send a request here: [https://vueform.dev](https://vueform.dev/)

Or contact us at [info@vueform.com](mailto:info@vueform.com).

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
