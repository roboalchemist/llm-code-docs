# Source: https://headlessui.com/v1/vue/radio-group

# Radio Group

Radio Groups give you the same functionality as native HTML radio inputs,
without any of the styling. They&#x27;re perfect for building out custom UIs for
selectors.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Radio Groups are built using the `RadioGroup`, `RadioGroupLabel`, and `RadioGroupOption` components.

Clicking an option will select it, and when the Radio Group is focused, the arrow keys will change the selected option.

`<template>
  <RadioGroup v-model="plan">
    <RadioGroupLabel>Plan</RadioGroupLabel>
    <RadioGroupOption v-slot="{ checked }" value="startup">
      <span :class="checked ? 'bg-blue-200' : ''">Startup</span>
    </RadioGroupOption>
    <RadioGroupOption v-slot="{ checked }" value="business">
      <span :class="checked ? 'bg-blue-200' : ''">Business</span>
    </RadioGroupOption>
    <RadioGroupOption v-slot="{ checked }" value="enterprise">
      <span :class="checked ? 'bg-blue-200' : ''">Enterprise</span>
    </RadioGroupOption>
  </RadioGroup>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'

  const plan = ref('startup')
</script>`

## [](#styling-different-states)Styling different states
Headless UI keeps track of a lot of state about each component, like which radiogroup option is currently selected, whether a popover is open or closed, or which item in a radiogroup is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `RadioGroupOption` component exposes an `active` state, which tells you if the item is currently focused via the mouse or keyboard.

`<template>
  <RadioGroup v-model="plan">
    <RadioGroupLabel>Plan</RadioGroupLabel>
    <!-- Use the `active` state to conditionally style the active option. -->
    <!-- Use the `checked` state to conditionally style the checked option. -->
    <RadioGroupOption
      v-for="plan in plans"
      :key="plan"
      :value="plan"
      as="template"

      v-slot="{ active, checked }"
    >
      <li
        :class="{

          'bg-blue-500 text-white': active,

          'bg-white text-black': !active,
        }"
      >

        <CheckIcon v-show="checked" />
        {{ plan }}
      </li>
    </RadioGroupOption>
  </RadioGroup>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'
  import { CheckIcon } from '@heroicons/vue/20/solid'

  const plans = ['Startup', 'Business', 'Enterprise']
  const plan = ref(plans[0])
</script>
`

For a complete list of all the available slot props, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot prop API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `RadioGroup` component with some child `RadioGroupOption` components renders when the radiogroup is open and the second item is `active`:

`<!-- Rendered `RadioGroup` -->
<ul data-headlessui-state="open">
  <li data-headlessui-state="">Wade Cooper</li>
  <li data-headlessui-state="active selected">Arlene Mccoy</li>
  <li data-headlessui-state="">Devon Webb</li>
</ul>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-open:*` and `ui-active:*`:

`<template>
  <RadioGroup v-model="plan">
    <RadioGroupLabel>Plan</RadioGroupLabel>
    <RadioGroupOption
      v-for="plan in plans"
      :key="plan"
      :value="plan"
      as="template"
    >
      <li

        class="ui-active:bg-blue-500 ui-active:text-white ui-not-active:bg-white ui-not-active:text-black"
      >

        <CheckIcon class="hidden ui-checked:block" />
        {{ plan }}
      </li>
    </RadioGroupOption>
  </RadioGroup>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'
  import { CheckIcon } from '@heroicons/vue/20/solid'

  const plans = ['Startup', 'Business', 'Enterprise']
  const plan = ref(plans[0])
</script>
`

## [](#binding-objects-as-values)Binding objects as values
Unlike native HTML form controls which only allow you to provide strings as values, Headless UI supports binding complex objects as well.

`<template>

  <RadioGroup v-model="plan">
    <RadioGroupLabel>Plan</RadioGroupLabel>

    <RadioGroupOption v-for="plan in plans" :key="plan.id" :value="plan">
      {{ plan.name }}
    </RadioGroupOption>
  </RadioGroup>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'

  const plans = [

    { id: 1, name: 'Startup' },

    { id: 2, name: 'Business' },

    { id: 3, name: 'Enterprise' },

  ]
  const plan = ref(plans[1])
</script>
`

When binding objects as values, it&#x27;s important to make sure that you use the *same instance* of the object as both the `value` of the `RadioGroup` as well as the corresponding `RadioGroupOption`, otherwise they will fail to be equal and cause the radiogroup to behave incorrectly.

To make it easier to work with different instances of the same object, you can use the `by` prop to compare the objects by a particular field instead of comparing object identity:

`<template>
  <RadioGroup
    :modelValue="modelValue"
    @update:modelValue="value => emit('update:modelValue', value)"

    by="id"
  >
    <RadioGroupLabel>Assignee</RadioGroupLabel>
    <RadioGroupOption v-for="plan in plans" :key="plan.id" :value="plan">
      {{ plan.name }}
    </RadioGroupOption>
  </RadioGroup>
</template>

<script setup>
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'

  const props = defineProps({ modelValue: Object })
  const emit = defineEmits(['update:modelValue'])

  const plans = [
    { id: 1, name: 'Startup' },
    { id: 2, name: 'Business' },
    { id: 3, name: 'Enterprise' },
  ]
</script>
`

You can also pass your own comparison function to the `by` prop if you&#x27;d like complete control over how objects are compared:

`<template>
  <RadioGroup
    :modelValue="modelValue"
    @update:modelValue="value => emit('update:modelValue', value)"

    :by="comparePlans"
  >
    <RadioGroupLabel>Assignee</RadioGroupLabel>
    <RadioGroupOption v-for="plan in plans" :key="plan.id" :value="plan">
      {{ plan.name }}
    </RadioGroupOption>
  </RadioGroup>
</template>

<script setup>
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'

  const props = defineProps({ modelValue: Object })
  const emit = defineEmits(['update:modelValue'])

  function comparePlans(a, b) {

    return a.name.toLowerCase() === b.name.toLowerCase()

  }

  const plans = [
    { id: 1, name: 'Startup' },
    { id: 2, name: 'Business' },
    { id: 3, name: 'Enterprise' },
  ]
</script>
`

## [](#using-with-html-forms)Using with HTML forms
If you add the `name` prop to your listbox, hidden `input` elements will be rendered and kept in sync with your selected value.

`<template>
  <form action="/billing" method="post">

    <RadioGroup v-model="plan" name="plan">
      <RadioGroupLabel>Plan</RadioGroupLabel>
      <RadioGroupOption v-for="plan in plans" :key="plan" :value="plan">
        {{ plan }}
      </RadioGroupOption>
    </RadioGroup>
    <button>Submit</button>
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'

  const plans = ['startup', 'business', 'enterprise']
  const plan = ref(plans[0])
</script>
`

This lets you use a radio group inside a native HTML `<form>` and make traditional form submissions as if your radio group was a native HTML form control.

Basic values like strings will be rendered as a single hidden input containing that value, but complex values like objects will be encoded into multiple inputs using a square bracket notation for the names.

`<input type="hidden" name="plan" value="startup" />`

## [](#using-as-an-uncontrolled-component)Using as an uncontrolled component
If you provide a `defaultValue` prop to the `RadioGroup` instead of a `value`, Headless UI will track its state internally for you, allowing you to use it as an [uncontrolled component](https://reactjs.org/docs/uncontrolled-components.html).

`<template>
  <form action="/billing" method="post">

    <RadioGroup name="plan" :defaultValue="plans[0]">
      <RadioGroupLabel>Plan</RadioGroupLabel>
      <RadioGroupOption v-for="plan in plans" :key="plan" :value="plan">
        {{ plan }}
      </RadioGroupOption>
    </RadioGroup>
    <button>Submit</button>
  </form>
</template>

<script setup>
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'

  const plans = ['startup', 'business', 'enterprise']
</script>
`

This can simplify your code when using the combobox [with HTML forms](#using-with-html-forms) or with form APIs that collect their state using [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instead of tracking it using React state.

Any `@update:modelValue` prop you provide will still be called when the component&#x27;s value changes in case you need to run any side effects, but you won&#x27;t need to use it to track the component&#x27;s state yourself.

## [](#using-the-label-and-description-components)Using the Label and Description components

You can use the `RadioGroupLabel` and `RadioGroupDescription` components to mark up each option&#x27;s contents. Doing so will automatically link each component to its ancestor `RadioGroupOption` component via the `aria-labelledby` and `aria-describedby` attributes and autogenerated `id`s, improving the semantics and accessibility of your custom selector.

By default, `RatioGroupLabel` renders a `label` element and `RadioGroupDescription` renders a `<div>`. These can also be customized using the `as` prop, as described in the API docs below.

Note also that `Label`s and `Description`s can be nested. Each one will refer to its nearest ancestor component, whether than ancestor is a `RadioGroupOption` or the root `RadioGroup` itself.

`<template>
  <RadioGroup v-model="plan">
    <!-- This label is for the root `RadioGroup` -->

    <RadioGroupLabel class="sr-only">Plan</RadioGroupLabel>
    <div class="rounded-md bg-white">
      <RadioGroupOption value="startup" as="template" v-slot="{ checked }">
        <div
          :class='checked ? "bg-indigo-50 border-indigo-200" : "border-gray-200"'
          class="relative flex border p-4"
        >
          <div class="flex flex-col">
            <!-- This label is for the `RadioGroupOption` -->

            <RadioGroupLabel as="template">

              <span

                :class='checked ? "text-indigo-900" : "text-gray-900"'

                class="block text-sm font-medium"

                >Startup</span

              >

            </RadioGroupLabel>

            <!-- This description is for the `RadioGroupOption` -->

            <RadioGroupDescription as="template">

              <span

                :class='checked ? "text-indigo-700" : "text-gray-500"'

                class="block text-sm"

                >Up to 5 active job postings</span

              >

            </RadioGroupDescription>
          </div>
        </div>
      </RadioGroupOption>
    </div>
  </RadioGroup>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
    RadioGroupDescription,
  } from '@headlessui/vue'

  const plan = ref('startup')
</script>
`

## [](#accessibility-notes)Accessibility notes

### [](#mouse-interaction)Mouse interaction
Clicking a `RadioGroupOption` will select it.

### [](#keyboard-interaction)Keyboard interaction

All interactions apply when a `RadioGroup` component is focused.

CommandDescription
ArrowDown or ArrowUp or ArrowLeft or ArrowRight 

Cycles through a RadioGroup&#x27;s options

Space when no option is selected yet

Selects the first option

Enter when in a form

Submits the form

### [](#other)Other

All relevant ARIA attributes are automatically managed.

## [](#component-api)Component API

### [](#radio-group)RadioGroup

The main Radio Group component.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `RadioGroup` should render as.

`v-model`—
`T`

The selected value.

`defaultValue`—
`T`

The default value when using as an uncontrolled component.

`by`—
`keyof T | ((a: T, z: T) => boolean)`

Use this to compare objects by a particular field, or pass your own
comparison function for complete control over how objects are compared.

`disabled``false`
`boolean`

Whether or not the `RadioGroup` and all of its `RadioGroupOption`&#x27;s&#x27; are
disabled.

### [](#radio-group-option)RadioGroupOption

The wrapper component for each selectable option.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `RadioGroupOption` should render as.

`value`—
`T | undefined`

The value of the current `RadioGroupOption`. The type should match the
type of the `value` in the `RadioGroup` component.

`disabled``false`
`boolean`

Whether or not the `RadioGroupOption` is disabled.

`name`—
`String`

The name used when using this component inside a form.

Slot PropDescription`active`
`Boolean`

Whether or not the option is active (using the mouse or keyboard).

`checked`
`Boolean`

Whether or not the current option is the checked value.

`disabled`
`boolean`

Whether or not the current option is disabled.

### [](#radio-group-label)RadioGroupLabel

Renders an element whose `id` attribute is automatically generated, and is then linked to its nearest ancestor `RadioGroup` or `RadioGroupOption` component via the `aria-labelledby` attribute.

PropDefaultDescription`as``label`
`String | Component`

The element or component the `RadioGroupLabel` should render as.

### [](#radio-group-description)RadioGroupDescription

Renders an element whose `id` attribute is automatically generated, and is then linked to its nearest ancestor `RadioGroup` or `RadioGroupOption` component via the `aria-describedby` attribute.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `RadioGroupDescription` should render as.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)