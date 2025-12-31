# Source: https://headlessui.com/v1/vue/switch

# Switch (Toggle)

Switches are a pleasant interface for toggling a value between two states, and
offer the same semantics and keyboard navigation as native checkbox elements.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Switches are built using the `Switch` component, which takes in a ref via the `v-model` prop. You can toggle your Switch by clicking directly on the component, or by pressing the spacebar while its focused.

Toggling the switch updates your ref to its negated value.

`<template>
  <Switch
    v-model="enabled"
    :class="enabled ? 'bg-blue-600' : 'bg-gray-200'"
    class="relative inline-flex h-6 w-11 items-center rounded-full"
  >
    <span class="sr-only">Enable notifications</span>
    <span
      :class="enabled ? 'translate-x-6' : 'translate-x-1'"
      class="inline-block h-4 w-4 transform rounded-full bg-white transition"
    />
  </Switch>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch } from '@headlessui/vue'

  const enabled = ref(false)
</script>`

## [](#styling-different-states)Styling different states
Headless UI keeps track of a lot of state about each component, like which switch option is currently selected, whether a popover is open or closed, or which item in a menu is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `Switch` component exposes an `checked` state, which tells you if the switch is currently checked or not.

`<template>

  <!-- Use the `checked` state to conditionally style the button. -->
  <Switch v-model="enabled" as="template" v-slot="{ checked }">
    <button
      class="relative inline-flex h-6 w-11 items-center rounded-full"

      :class="checked ? 'bg-blue-600' : 'bg-gray-200'"
    >
      <span class="sr-only">Enable notifications</span>
      <span

        :class="checked ? 'translate-x-6' : 'translate-x-1'"
        class="inline-block h-4 w-4 transform rounded-full bg-white transition"
      />
    </button>
  </Switch>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch } from '@headlessui/vue'

  const enabled = ref(false)
</script>
`

For a complete list of all the available slot props, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot prop API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `Switch` component renders when the switch is checked:

`<!-- Rendered `Switch` -->
<button data-headlessui-state="checked"></button>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-checked:*`:

`<template>
  <Switch
    v-model="enabled"

    class="relative inline-flex h-6 w-11 items-center rounded-full ui-checked:bg-blue-600 ui-not-checked:bg-gray-200"
  >
    <span class="sr-only">Enable notifications</span>
    <span

      class="inline-block h-4 w-4 transform rounded-full bg-white transition ui-checked:translate-x-6 ui-not-checked:translate-x-1"
    />
  </Switch>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch } from '@headlessui/vue'

  const enabled = ref(false)
</script>
`

## [](#using-a-custom-label)Using a custom label
By default, a Switch renders a `button` as well as whatever children you pass into it. This can make it harder to implement certain UIs, since the children will be nested within the button.

In these situations, you can use the `SwitchLabel` component for more flexibility.

This example demonstrates how to use the `SwitchGroup`, `Switch` and `SwitchLabel` components to render a label as a sibling to the button. Note that `SwitchLabel` works alongside a `Switch` component, and they both must be rendered within a parent `SwitchGroup` component.

`<template>

  <SwitchGroup>
    <div class="flex items-center">

      <SwitchLabel class="mr-4">Enable notifications</SwitchLabel>
      <Switch
        v-model="enabled"
        :class='enabled ? "bg-blue-600" : "bg-gray-200"'
        class="relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
      >
        <span
          :class='enabled ? "translate-x-6" : "translate-x-1"'
          class="inline-block h-4 w-4 transform rounded-full bg-white transition-transform"
        />
      </Switch>
    </div>

  </SwitchGroup>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch, SwitchGroup, SwitchLabel } from '@headlessui/vue'

  const enabled = ref(false)
</script>
`

By default, clicking a `SwitchLabel` will toggle the Switch, just like labels in native HTML checkboxes do. If you&#x27;d like to make the label non-clickable (which you might if it doesn&#x27;t make sense for your design), you can add a `passive` prop to the `SwitchLabel` component:

`<template>
  <SwitchGroup>

    <SwitchLabel passive>Enable notifications</SwitchLabel>
    <Switch v-model="enabled">
      <!-- ... -->
    </Switch>
  </SwitchGroup>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch, SwitchGroup, SwitchLabel } from '@headlessui/vue'

  const enabled = ref(false)
</script>
`

## [](#using-with-html-forms)Using with HTML forms
If you add the `name` prop to your switch, a hidden `input` element will be rendered and kept in sync with the switch state.

`<template>
  <form action="/notification-settings" method="post">

    <Switch v-model="enabled" name="notifications">
      <!-- ... -->
    </Switch>
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch } from '@headlessui/vue'

  const enabled = ref(true)
</script>
`

This lets you use a switch inside a native HTML `<form>` and make traditional form submissions as if your switch was a native HTML form control.

By default, the value will be `&#x27;on&#x27;` when the switch is checked, and not present when the switch is unchecked.

`<input type="hidden" name="notifications" value="on" />`

You can customize the value if needed by using the `value` prop:

`<template>
  <form action="/accounts" method="post">

    <Switch v-model="enabled" name="terms" value="accept">
      <!-- ... -->
    </Switch>
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch } from '@headlessui/vue'

  const enabled = ref(true)
</script>
`

The hidden input will then use your custom value when the switch is checked:

`<input type="hidden" name="terms" value="accept" />`

## [](#using-as-an-uncontrolled-component)Using as an uncontrolled component
If you provide a `defaultChecked` prop to the `Switch` instead of a `checked` prop, Headless UI will track its state internally for you, allowing you to use it as an [uncontrolled component](https://reactjs.org/docs/uncontrolled-components.html).

You can access the current state via the `checked` slot prop on the `Switch` component.

`<template>
  <form action="/accounts" method="post">
    <Switch
      name="terms-of-service"

      :defaultChecked="true"
      as="template"
      v-slot="{ checked }"
    >
      <button
        :class="checked ? 'bg-blue-600' : 'bg-gray-200'"
        class="relative inline-flex h-6 w-11 items-center rounded-full"
      >
        <span class="sr-only">Enable notifications</span>
        <span
          :class="checked ? 'translate-x-6' : 'translate-x-1'"
          class="inline-block h-4 w-4 transform rounded-full bg-white transition"
        />
      </button>
    </Switch>
    <button>Submit</button>
  </form>
</template>

<script setup>
  import { Switch } from '@headlessui/vue'
</script>
`

This can simplify your code when using the listbox [with HTML forms](#using-with-html-forms) or with form APIs that collect their state using [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instead of tracking it using React state.

Any `@update:modelValue` prop you provide will still be called when the component&#x27;s value changes in case you need to run any side effects, but you won&#x27;t need to use it to track the component&#x27;s state yourself.

## [](#transitions)Transitions

Because Switches are typically always rendered to the DOM (rather than being mounted/unmounted like other components), simple CSS transitions are often enough to animate your Switch:

`<template>
  <Switch v-model="enabled">
    <!-- Transition the switch's knob on state change -->
    <span

      :class="enabled ? 'translate-x-9' : 'translate-x-0'"
      class="transform transition duration-200 ease-in-out"
    />
    <!-- ... -->
  </Switch>
</template>

<script setup>
  import { ref } from 'vue'
  import { Switch } from '@headlessui/vue'

  const enabled = ref(false)
</script>
`

## [](#accessibility-notes)Accessibility notes

### [](#labels)Labels
By default, the children of a `Switch` will be used as the label for screen readers. If you&#x27;re using `SwitchLabel`, the content of your `Switch` component will be ignored by assistive technologies.

### [](#mouse-interaction)Mouse interaction

Clicking a `Switch` or a `SwitchLabel` toggles the Switch on and off.

### [](#keyboard-interaction)Keyboard interaction

CommandDescription
Space when a `Switch` is focused

Toggles the Switch

Enter when in a form

Submits the form

### [](#other)Other

All relevant ARIA attributes are automatically managed.

## [](#component-api)Component API

### [](#switch)Switch

The main Switch component.

PropDefaultDescription`as``button`
`String | Component`

The element or component the `Switch` should render as.

`v-model`—
`Boolean`

Whether or not the switch is checked.

`defaultChecked`—
`T`

The default checked value when using as an uncontrolled component.

`name`—
`String`

The name used when using this component inside a form.

`value`—
`String`

The value used when using this component inside a form, if it is checked.

Slot PropDescription`checked`
`Boolean`

Whether or not the switch is checked.

### [](#switch-label)SwitchLabel

PropDefaultDescription`as``label`
`String | Component`

The element or component the `SwitchLabel` should render as.

`passive``false`
`Boolean`

When true, clicking the label won&#x27;t toggle the `Switch`.

### [](#switch-description)SwitchDescription

PropDefaultDescription`as``p`
`String | Component`

The element or component the `Switch.Description` should render as.

### [](#switch-group)SwitchGroup

PropDefaultDescription`as``template`
`String | Component`

The element or component the `SwitchGroup` should render as.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)