# Source: https://headlessui.com/v1/vue/listbox

# Listbox (Select)

Listboxes are a great foundation for building custom, accessible select menus
for your app, complete with robust support for keyboard navigation.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Listboxes are built using the `Listbox`, `ListboxButton`, `ListboxOptions`, `ListboxOption` and `ListboxLabel` components.

The `ListboxButton` will automatically open/close the `ListboxOptions` when clicked, and when the menu is open, the list of items receives focus and is automatically navigable via the keyboard.

`<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
    <ListboxOptions>
      <ListboxOption
        v-for="person in people"
        :key="person.id"
        :value="person"
        :disabled="person.unavailable"
      >
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds', unavailable: false },
    { id: 2, name: 'Kenton Towne', unavailable: false },
    { id: 3, name: 'Therese Wunsch', unavailable: false },
    { id: 4, name: 'Benedict Kessler', unavailable: true },
    { id: 5, name: 'Katelyn Rohan', unavailable: false },
  ]
  const selectedPerson = ref(people[0])
</script>`

## [](#styling-different-states)Styling different states
Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a listbox is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `ListboxOption` component exposes an `active` state, which tells you if the item is currently focused via the mouse or keyboard.

`<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
    <ListboxOptions>
      <!-- Use the `active` state to conditionally style the active option. -->
      <!-- Use the `selected` state to conditionally style the selected option. -->
      <ListboxOption
        v-for="person in people"
        :key="person.id"
        :value="person"
        as="template"

        v-slot="{ active, selected }"
      >
        <li
          :class="{

            'bg-blue-500 text-white': active,

            'bg-white text-black': !active,
          }"
        >

          <CheckIcon v-show="selected" />
          {{ person.name }}
        </li>
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'
  import { CheckIcon } from '@heroicons/vue/20/solid'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

For a complete list of all the available slot props, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot prop API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `ListboxOptions` component with some child `ListboxOption` components renders when the listbox is open and the second item is `active`:

`<!-- Rendered `ListboxOptions` -->
<ul data-headlessui-state="open">
  <li data-headlessui-state="">Wade Cooper</li>
  <li data-headlessui-state="active selected">Arlene Mccoy</li>
  <li data-headlessui-state="">Devon Webb</li>
</ul>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-open:*` and `ui-active:*`:

`<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
    <ListboxOptions>
      <ListboxOption
        v-for="person in people"
        :key="person.id"
        :value="person"

        class="ui-active:bg-blue-500 ui-active:text-white ui-not-active:bg-white ui-not-active:text-black"
      >

        <CheckIcon class="hidden ui-selected:block" />
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'
  import { CheckIcon } from '@heroicons/vue/20/solid'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

## [](#binding-objects-as-values)Binding objects as values
Unlike native HTML form controls which only allow you to provide strings as values, Headless UI supports binding complex objects as well.

`<template>

  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
    <ListboxOptions>
      <ListboxOption
        v-for="person in people"
        :key="person.id"

        :value="person"
        :disabled="person.unavailable"
      >
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [

    { id: 1, name: 'Durward Reynolds', unavailable: false },

    { id: 2, name: 'Kenton Towne', unavailable: false },

    { id: 3, name: 'Therese Wunsch', unavailable: false },

    { id: 4, name: 'Benedict Kessler', unavailable: true },

    { id: 5, name: 'Katelyn Rohan', unavailable: false },

  ]
  const selectedPerson = ref(people[1])
</script>
`

When binding objects as values, it&#x27;s important to make sure that you use the *same instance* of the object as both the `value` of the `Listbox` as well as the corresponding `ListboxOption`, otherwise they will fail to be equal and cause the listbox to behave incorrectly.

To make it easier to work with different instances of the same object, you can use the `by` prop to compare the objects by a particular field instead of comparing object identity:

`<template>
  <Listbox
    :modelValue="modelValue"
    @update:modelValue="value => emit('update:modelValue', value)"

    by="id"
  >
    <ListboxButton>{{ modelValue.name }}</ListboxButton>
    <ListboxOptions>
      <ListboxOption
        v-for="department in departments"
        :key="department.id"
        :value="department"
      >
        {{ department.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const props = defineProps({ modelValue: Object })
  const emit = defineEmits(['update:modelValue'])

  const departments = [
    { id: 1, name: 'Marketing', contact: 'Durward Reynolds' },
    { id: 2, name: 'HR', contact: 'Kenton Towne' },
    { id: 3, name: 'Sales', contact: 'Therese Wunsch' },
    { id: 4, name: 'Finance', contact: 'Benedict Kessler' },
    { id: 5, name: 'Customer service', contact: 'Katelyn Rohan' },
  ]
</script>
`

You can also pass your own comparison function to the `by` prop if you&#x27;d like complete control over how objects are compared:

`<template>
  <Listbox
    :modelValue="modelValue"
    @update:modelValue="value => emit('update:modelValue', value)"

    :by="compareDepartments"
  >
    <ListboxButton>{{ modelValue.name }}</ListboxButton>
    <ListboxOptions>
      <ListboxOption
        v-for="department in departments"
        :key="department.id"
        :value="department"
      >
        {{ department.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const props = defineProps({ modelValue: Object })
  const emit = defineEmits(['update:modelValue'])

  function compareDepartments(a, b) {

    return a.name.toLowerCase() === b.name.toLowerCase()

  }

  const departments = [
    { id: 1, name: 'Marketing', contact: 'Durward Reynolds' },
    { id: 2, name: 'HR', contact: 'Kenton Towne' },
    { id: 3, name: 'Sales', contact: 'Therese Wunsch' },
    { id: 4, name: 'Finance', contact: 'Benedict Kessler' },
    { id: 5, name: 'Customer service', contact: 'Katelyn Rohan' },
  ]
</script>
`

## [](#selecting-multiple-values)Selecting multiple values
To allow selecting multiple values in your listbox, use the `multiple` prop and pass an array to `v-model` instead of a single option.

`<template>

  <Listbox v-model="selectedPeople" multiple>
    <ListboxButton>
      {{ selectedPeople.map((person) => person.name).join(', ') }}
    </ListboxButton>
    <ListboxOptions>
      <ListboxOption v-for="person in people" :key="person.id" :value="person">
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]

  const selectedPeople = ref([people[0], people[1]])
</script>
`

This will keep the listbox open when you are selecting options, and choosing an option will toggle it in place.

Your `v-model` binding will be updated with an array containing all selected options any time an option is added or removed.

## [](#using-a-custom-label)Using a custom label

By default the `Listbox` will use the button contents as the label for screenreaders. If you&#x27;d like more control over what is announced to assistive technologies, use the `ListboxLabel` component.

`<template>
  <Listbox v-model="selectedPerson">

    <ListboxLabel>Assignee:</ListboxLabel>
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
    <ListboxOptions>
      <ListboxOption v-for="person in people" :key="person.id" :value="person">
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxLabel,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

## [](#using-with-html-forms)Using with HTML forms
If you add the `name` prop to your listbox, hidden `input` elements will be rendered and kept in sync with your selected value.

`<template>
  <form action="/projects/1/assignee" method="post">

    <Listbox v-model="selectedPerson" name="assignee">
      <ListboxButton>{{ selectedPerson.name }}</ListboxButton>
      <ListboxOptions>
        <ListboxOption
          v-for="person in people"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ListboxOption>
      </ListboxOptions>
    </Listbox>
    <button>Submit</button>
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

This lets you use a listbox inside a native HTML `<form>` and make traditional form submissions as if your listbox was a native HTML form control.

Basic values like strings will be rendered as a single hidden input containing that value, but complex values like objects will be encoded into multiple inputs using a square bracket notation for the names:

`<input type="hidden" name="assignee[id]" value="1" />
<input type="hidden" name="assignee[name]" value="Durward Reynolds" />`

## [](#using-as-an-uncontrolled-component)Using as an uncontrolled component
If you provide a `defaultValue` prop to the `Listbox` instead of a `value`, Headless UI will track its state internally for you, allowing you to use it as an [uncontrolled component](https://reactjs.org/docs/uncontrolled-components.html).

You can access the currently selected option via the `value` slot prop on the `Listbox` and `ListboxButton` components.

`<template>
  <form action="/projects/1/assignee" method="post">

    <Listbox name="assignee" :defaultValue="people[0]">

      <ListboxButton v-slot="{ value }">{{ value.name }}</ListboxButton>
      <ListboxOptions>
        <ListboxOption
          v-for="person in people"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ListboxOption>
      </ListboxOptions>
    </Listbox>
    <button>Submit</button>
  </form>
</template>

<script setup>
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
</script>
`

This can simplify your code when using the listbox [with HTML forms](#using-with-html-forms) or with form APIs that collect their state using [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instead of tracking it using React state.

Any `@update:modelValue` prop you provide will still be called when the component&#x27;s value changes in case you need to run any side effects, but you won&#x27;t need to use it to track the component&#x27;s state yourself.

## [](#showing-hiding-the-listbox)Showing/hiding the listbox

By default, your `ListboxOptions` instance will be shown/hidden automatically based on the internal `open` state tracked within the `Listbox` component itself.

`<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>

    <!--
      By default, the `ListboxOptions` will automatically show/hide
      when the `ListboxButton` is pressed.
    -->
    <ListboxOptions>
      <ListboxOption v-for="person in people" :key="person.id" :value="person">
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { name: 'Durward Reynolds' },
    { name: 'Kenton Towne' },
    { name: 'Therese Wunsch' },
    { name: 'Benedict Kessler' },
    { name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>`

If you&#x27;d rather handle this yourself (perhaps because you need to add an extra wrapper element for one reason or another), you can add a `static` prop to the `ListboxOptions` instance to tell it to always render, and inspect the `open` slot prop provided by the `Listbox` to control which element is shown/hidden yourself.

`<template>

  <Listbox v-model="selectedPerson" v-slot="{ open }">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>

    <div v-show="open">
      <!--
        Using the `static` prop, the `ListboxOptions` are always
        rendered and the `open` state is ignored.
      -->

      <ListboxOptions static>
        <ListboxOption
          v-for="person in people"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ListboxOption>
      </ListboxOptions>
    </div>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { name: 'Durward Reynolds' },
    { name: 'Kenton Towne' },
    { name: 'Therese Wunsch' },
    { name: 'Benedict Kessler' },
    { name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

## [](#disabling-an-option)Disabling an option
Use the `disabled` prop to disable a `ListboxOption`. This will make it unselectable via mouse and keyboard, and it will be skipped when pressing the up/down arrows.

`<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>

    <ListboxOptions>
      <!-- Disabled options will be skipped by keyboard navigation. -->
      <ListboxOption
        v-for="person in people"
        :key="person.name"
        :value="person"

        :disabled="person.unavailable"
      >
        <span :class='{ "opacity-75": person.unavailable }'>
          {{ person.name }}
        </span>
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { name: 'Durward Reynolds', unavailable: true },
    { name: 'Kenton Towne', unavailable: false },
    { name: 'Therese Wunsch', unavailable: false },
    { name: 'Benedict Kessler', unavailable: true },
    { name: 'Katelyn Rohan', unavailable: false },
  ]
  const selectedPerson = ref(people[0])
</script>
`

## [](#transitions)Transitions
To animate the opening/closing of your listbox, you can use Vue&#x27;s built-in `<transition>` component. All you need to do is wrap your `ListboxOptions` instance in a `<transition>`, and the transition will be applied automatically.

`<template>
  <Listbox v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>

    <!-- Use Vue's built-in `transition` component to add transitions. -->

    <transition

      enter-active-class="transition duration-100 ease-out"

      enter-from-class="transform scale-95 opacity-0"

      enter-to-class="transform scale-100 opacity-100"

      leave-active-class="transition duration-75 ease-out"

      leave-from-class="transform scale-100 opacity-100"

      leave-to-class="transform scale-95 opacity-0"

    >
      <ListboxOptions>
        <ListboxOption
          v-for="person in people"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ListboxOption>
      </ListboxOptions>
    </transition>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

If you&#x27;d like to coordinate multiple transitions for different children of your Listbox, check out the [Transition component included in Headless UI](/v1/vue/transition).

## [](#rendering-as-different-elements)Rendering as different elements

By default, the `Listbox` and its subcomponents each render a default element that is sensible for that component.

For example, `ListboxLabel` renders a `label` by default, `ListboxButton`
renders a `button`, `ListboxOptions` renders a `ul`, and `ListboxOption`
renders a `li`. By contrast, `Listbox` *does not render an element*, and
instead renders its children directly.

This is easy to change using the `as` prop, which exists on every component.

`<template>
  <!-- Render a `div` instead of nothing -->

  <Listbox as="div" v-model="selectedPerson">
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>

    <!-- Render a `div` instead of a `ul` -->

    <ListboxOptions as="div">
      <!-- Render a `span` instead of a `li` -->
      <ListboxOption

        as="span"
        v-for="person in people"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

To tell an element to render its children directly with no wrapper element, use `as="template"`.

`<template>
  <Listbox v-model="selectedPerson">
    <!-- Render children directly instead of a `ListboxButton` -->

    <ListboxButton as="template">
      <button>{{ selectedPerson.name }}</button>
    </ListboxButton>

    <ListboxOptions>
      <ListboxOption v-for="person in people" :key="person.id" :value="person">
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

## [](#horizontal-options)Horizontal options
If you&#x27;ve styled your `ListboxOptions` to appear horizontally, use the `horizontal` prop on the `Listbox` component to enable navigating the items with the left and right arrow keys instead of up and down, and to update the `aria-orientation` attribute for assistive technologies.

`<template>

  <Listbox v-model="selectedPerson" horizontal>
    <ListboxButton>{{ selectedPerson.name }}</ListboxButton>

    <ListboxOptions class="flex flex-row">
      <ListboxOption v-for="person in people" :key="person.id" :value="person">
        {{ person.name }}
      </ListboxOption>
    </ListboxOptions>
  </Listbox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
</script>
`

## [](#accessibility-notes)Accessibility notes

### [](#focus-management)Focus management
When a Listbox is toggled open, the `ListboxOptions` receives focus. Focus is trapped within the list of items until Escape is pressed or the user clicks outside the options. Closing the Listbox returns focus to the `ListboxButton`.

### [](#mouse-interaction)Mouse interaction

Clicking a `ListboxButton` toggles the options list open and closed. Clicking anywhere outside of the options list will close the listbox.

### [](#keyboard-interaction)Keyboard interaction

CommandDescription
Enter, Space, ArrowDown,  or ArrowUp when `ListboxButton` is focused

Opens listbox and focuses the selected item

Esc when listbox is open

Closes listbox

ArrowDown or ArrowUp when listbox is open

Focuses previous/next non-disabled item

ArrowLeft or ArrowRight when listbox is open and `horizontal` is set

Focuses previous/next non-disabled item

Home or PageUp when listbox is open

Focuses first non-disabled item

End or PageDown when listbox is open

Focuses last non-disabled item

Enter or Space when listbox is open

Selects the current item

A–Z or a–z when listbox is open

Focuses first item that matches keyboard input

### [](#other)Other

All relevant ARIA attributes are automatically managed.

## [](#component-api)Component API

### [](#listbox)Listbox

The main Listbox component.

PropDefaultDescription`as``template`
`String | Component`

The element or component the `Listbox` should render as.

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
`Boolean`

Use this to disable the entire Listbox component & related children.

`horizontal``false`
`Boolean`

When true, the orientation of the `ListboxOptions` will be `horizontal`,
otherwise it will be `vertical`.

`name`—
`String`

The name used when using this component inside a form.

`multiple``false`
`Boolean`

Whether multiple options can be selected or not.

Slot PropDescription`value`
`T`

The selected value.

`open`
`Boolean`

Whether or not the Listbox is open.

`disabled`
`Boolean`

Whether or not the Listbox is disabled.

### [](#listbox-button)ListboxButton

The Listbox&#x27;s button.

PropDefaultDescription`as``button`
`String | Component`

The element or component the `ListboxButton` should render as.

Slot PropDescription`value`
`T`

The selected value.

`open`
`Boolean`

Whether or not the Listbox is open.

`disabled`
`Boolean`

Whether or not the Listbox is disabled.

### [](#listbox-label)ListboxLabel

A label that can be used for more control over the text your Listbox will announce to screenreaders. Its `id` attribute will be automatically generated and linked to the root `Listbox` component via the `aria-labelledby` attribute.

PropDefaultDescription`as``label`
`String | Component`

The element or component the `ListboxLabel` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the Listbox is open.

`disabled`
`Boolean`

Whether or not the Listbox is disabled.

### [](#listbox-options)ListboxOptions

The component that directly wraps the list of options in your custom Listbox.

PropDefaultDescription`as``ul`
`String | Component`

The element or component the `ListboxOptions` should render as.

`static``false`
`Boolean`

Whether the element should ignore the internally managed open/closed
state.

`unmount``true`
`Boolean`

Whether the element should be unmounted or hidden based on the open/closed
state.

Slot PropDescription`open`
`Boolean`

Whether or not the Listbox is open.

### [](#listbox-option)ListboxOption

Used to wrap each item within your Listbox.

PropDefaultDescription`value`—
`T`

The option value.

`as``li`
`String | Component`

The element or component the `ListboxOption` should render as.

`disabled``false`
`Boolean`

Whether or not the option should be disabled for keyboard navigation and
ARIA purposes.

Slot PropDescription`active`
`Boolean`

Whether or not the option is the active/focused option.

`selected`
`Boolean`

Whether or not the option is the selected option.

`disabled`
`Boolean`

Whether or not the option is the disabled for keyboard navigation and ARIA
purposes.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)