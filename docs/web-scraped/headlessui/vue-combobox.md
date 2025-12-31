# Source: https://headlessui.com/v1/vue/combobox

# Combobox (Autocomplete)

Comboboxes are the foundation of accessible autocompletes and command palettes
for your app, complete with robust support for keyboard navigation.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Comboboxes are built using the `Combobox`, `ComboboxInput`, `ComboboxButton`,
`ComboboxOptions`, `ComboboxOption` and `ComboboxLabel` components.

The `ComboboxInput` will automatically open/close the `ComboboxOptions` when
searching.

You are completely in charge of how you filter the results, whether it be with
a fuzzy search library client-side or by making server-side requests to an API.
In this example we will keep the logic simple for demo purposes.

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput @change="query = $event.target.value" />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person"
        :value="person"
      >
        {{ person }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    'Durward Reynolds',
    'Kenton Towne',
    'Therese Wunsch',
    'Benedict Kessler',
    'Katelyn Rohan',
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>`

In the previous example we used a list of `string` values as data, but you can
also use objects with additional information. The only caveat is that you have
to provide a `displayValue` to the input. This is important so that a string
based version of your object can be rendered in the `ComboboxInput`.

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"

      :displayValue="(person) => person.name"
    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
        :disabled="person.unavailable"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds', unavailable: false },
    { id: 2, name: 'Kenton Towne', unavailable: false },
    { id: 3, name: 'Therese Wunsch', unavailable: false },
    { id: 4, name: 'Benedict Kessler', unavailable: true },
    { id: 5, name: 'Katelyn Rohan', unavailable: false },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#styling-different-states)Styling different states
Headless UI keeps track of a lot of state about each component, like which combobox option is currently selected, whether a popover is open or closed, or which item in a combobox is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `ComboboxOption` component exposes an `active` state, which tells you if the item is currently focused via the mouse or keyboard.

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />
    <ComboboxOptions>
      <!-- Use the `active` state to conditionally style the active option. -->
      <!-- Use the `selected` state to conditionally style the selected option. -->
      <ComboboxOption
        v-for="person in filteredPeople"
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
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
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
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

For a complete list of all the available slot props, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot prop API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `ComboboxOptions` component with some child `ComboboxOption` components renders when the combobox is open and the second item is `active`:

`<!-- Rendered `ComboboxOptions` -->
<ul data-headlessui-state="open">
  <li data-headlessui-state="">Wade Cooper</li>
  <li data-headlessui-state="active selected">Arlene Mccoy</li>
  <li data-headlessui-state="">Devon Webb</li>
</ul>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-open:*` and `ui-active:*`:

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"

        class="ui-active:bg-blue-500 ui-active:text-white ui-not-active:bg-white ui-not-active:text-black"
      >

        <CheckIcon class="hidden ui-selected:block" />
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
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
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#binding-objects-as-values)Binding objects as values
Unlike native HTML form controls which only allow you to provide strings as values, Headless UI supports binding complex objects as well.

`<template>

  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"

        :value="person"
        :disabled="person.unavailable"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [

    { id: 1, name: 'Durward Reynolds', unavailable: false },

    { id: 2, name: 'Kenton Towne', unavailable: false },

    { id: 3, name: 'Therese Wunsch', unavailable: false },

    { id: 4, name: 'Benedict Kessler', unavailable: true },

    { id: 5, name: 'Katelyn Rohan', unavailable: false },

  ]
  const selectedPerson = ref(people[1])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

When binding objects as values, it&#x27;s important to make sure that you use the *same instance* of the object as both the `value` of the `Combobox` as well as the corresponding `ComboboxOption`, otherwise they will fail to be equal and cause the combobox to behave incorrectly.

To make it easier to work with different instances of the same object, you can use the `by` prop to compare the objects by a particular field instead of comparing object identity:

`<template>
  <Combobox
    :modelValue="modelValue"
    @update:modelValue="value => emit('update:modelValue', value)"

    by="id"
  >
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(department) => department.name"
    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="department in filteredDepartments"
        :key="department.id"
        :value="department"
      >
        {{ department.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
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
  const query = ref('')

  const filteredDepartments = computed(() =>
    query.value === ''
      ? departments
      : departments.filter((department) => {
          return department.name
            .toLowerCase()
            .includes(query.value.toLowerCase())
        })
  )
</script>
`

You can also pass your own comparison function to the `by` prop if you&#x27;d like complete control over how objects are compared:

`<template>
  <Combobox
    :modelValue="modelValue"
    @update:modelValue="value => emit('update:modelValue', value)"

    :by="compareDepartments"
  >
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(department) => department.name"
    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="department in departments"
        :key="department.id"
        :value="department"
      >
        {{ department.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
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
  const query = ref('')

  const filteredDepartments = computed(() =>
    query.value === ''
      ? departments
      : departments.filter((department) => {
          return department.name
            .toLowerCase()
            .includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#selecting-multiple-values)Selecting multiple values
The Combobox component allows you to select multiple values. You can enable this by providing an
array of values instead of a single value.

`<template>

  <Combobox v-model="selectedPeople" multiple>
    <ul v-if="selectedPeople.length > 0">
      <li v-for="person in selectedPeople" :key="person.id">
        {{ person.name }}
      </li>
    </ul>
    <ComboboxInput />
    <ComboboxOptions>
      <ComboboxOption v-for="person in people" :key="person.id" :value="person">
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
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

This will keep the combobox open when you are selecting options, and choosing an option will toggle it in place.

Your `v-model` binding will be updated with an array containing all selected options any time an option is added or removed.

## [](#using-a-custom-label)Using a custom label

By default the `Combobox` will use the input contents as the label for
screenreaders. If you&#x27;d like more control over what is announced to assistive
technologies, use the `ComboboxLabel` component.

`<template>
  <Combobox v-model="selectedPerson">

    <ComboboxLabel>Assignee:</ComboboxLabel>
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxLabel,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#using-with-html-forms)Using with HTML forms
If you add the `name` prop to your combobox, hidden `input` elements will be rendered and kept in sync with your selected value.

`<template>
  <form action="/projects/1/assignee" method="post">

    <Combobox v-model="selectedPerson" name="assignee">
      <ComboboxInput
        @change="query = $event.target.value"
        :displayValue="(person) => person.name"
      />
      <ComboboxOptions>
        <ComboboxOption
          v-for="person in filteredPeople"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ComboboxOption>
      </ComboboxOptions>
    </Combobox>
    <button>Submit</button>
  </form>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

This lets you use a combobox inside a native HTML `<form>` and make traditional form submissions as if your combobox was a native HTML form control.

Basic values like strings will be rendered as a single hidden input containing that value, but complex values like objects will be encoded into multiple inputs using a square bracket notation for the names:

`<input type="hidden" name="assignee[id]" value="1" />
<input type="hidden" name="assignee[name]" value="Durward Reynolds" />`

## [](#using-as-an-uncontrolled-component)Using as an uncontrolled component
If you provide a `defaultValue` prop to the `Combobox` instead of a `value`, Headless UI will track its state internally for you, allowing you to use it as an [uncontrolled component](https://reactjs.org/docs/uncontrolled-components.html).

`<template>
  <form action="/projects/1/assignee" method="post">

    <Combobox name="assignee" :defaultValue="people[0]">
      <ComboboxInput
        @change="query = $event.target.value"
        :displayValue="(person) => person.name"
      />
      <ComboboxOptions>
        <ComboboxOption
          v-for="person in filteredPeople"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ComboboxOption>
      </ComboboxOptions>
    </Combobox>
    <button>Submit</button>
  </form>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

This can simplify your code when using the combobox [with HTML forms](#using-with-html-forms) or with form APIs that collect their state using [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instead of tracking it using React state.

Any `@update:modelValue` prop you provide will still be called when the component&#x27;s value changes in case you need to run any side effects, but you won&#x27;t need to use it to track the component&#x27;s state yourself.

## [](#allowing-custom-values)Allowing custom values

You can allow users to enter their own value that doesn&#x27;t exist in the list by including a dynamic `ComboboxOption` based on the `query` value.

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />
    <ComboboxOptions>

      <ComboboxOption v-if="queryPerson" :value="queryPerson">

        Create "{{ query }}"

      </ComboboxOption>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const queryPerson = computed(() => {

    return query.value === '' ? null : { id: null, name: query.value }

  })

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#rendering-the-active-option-on-the-side)Rendering the active option on the side
Depending on what you&#x27;re building it can sometimes make sense to render
additional information about the active option outside of the
`<ComboboxOptions>`. For example, a preview of the active option within the
context of a command palette. In these situations you can read the
`activeOption` slot prop argument to access this information.

`<template>

  <Combobox v-model="selectedPerson" v-slot="{ activeOption }">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>

    <div v-if="activeOption">

      The current active user is: {{ activeOption.name }}

    </div>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

The `activeOption` will be the `value` of the current active `ComboboxOption`.

## [](#showing-hiding-the-combobox)Showing/hiding the combobox

By default, your `ComboboxOptions` instance will be shown/hidden automatically
based on the internal `open` state tracked within the `Combobox` component
itself.

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />

    <!--
      By default, the `ComboboxOptions` will automatically show/hide when
      typing in the `ComboboxInput`, or when pressing the `ComboboxButton`.
    -->
    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>`

If you&#x27;d rather handle this yourself (perhaps because you need to add an extra wrapper element for one reason or another), you can add a `static` prop to the `ComboboxOptions` instance to tell it to always render, and inspect the `open` slot prop provided by the `Combobox` to control which element is shown/hidden yourself.

`<template>

  <Combobox v-model="selectedPerson" v-slot="{ open }">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />

    <div v-show="open">
      <!--
        Using the `static` prop, the `ComboboxOptions` are always
        rendered and the `open` state is ignored.
      -->

      <ComboboxOptions static>
        <ComboboxOption
          v-for="person in filteredPeople"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ComboboxOption>
      </ComboboxOptions>
    </div>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#disabling-an-option)Disabling an option
Use the `disabled` prop to disable a `ComboboxOption`. This will make it unselectable via mouse and keyboard, and it will be skipped when pressing the up/down arrows.

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />

    <ComboboxOptions>
      <!-- Disabled options will be skipped by keyboard navigation. -->
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"

        :disabled="person.unavailable"
      >
        <span :class='{ "opacity-75": person.unavailable }'>
          {{ person.name }}
        </span>
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds', unavailable: true },
    { id: 2, name: 'Kenton Towne', unavailable: false },
    { id: 3, name: 'Therese Wunsch', unavailable: false },
    { id: 4, name: 'Benedict Kessler', unavailable: true },
    { id: 5, name: 'Katelyn Rohan', unavailable: false },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#allowing-empty-values)Allowing empty values
By default, once you&#x27;ve selected a value in a combobox there is no way to clear the combobox back to an empty value — when you clear the input and tab away, the value returns to the previously selected value.

If you want to support empty values in your combobox, use the `nullable` prop.

`<template>

  <Combobox v-model="selectedPerson" nullable>
    <ComboboxInput
      @change="query = $event.target.value"

      :displayValue="(person) => person?.name"
    />

    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds', unavailable: true },
    { id: 2, name: 'Kenton Towne', unavailable: false },
    { id: 3, name: 'Therese Wunsch', unavailable: false },
    { id: 4, name: 'Benedict Kessler', unavailable: true },
    { id: 5, name: 'Katelyn Rohan', unavailable: false },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

When the `nullable` prop is used, clearing the input and navigating away from the element will update your `v-model` binding and invoke your `displayValue` callback with `null`.

This prop doesn&#x27;t do anything when allowing [multiple values](#selecting-multiple-values) because options are
toggled on and off, resulting in an empty array (rather than null) if nothing is selected.

## [](#transitions)Transitions

To animate the opening/closing of your combobox, you can use Vue&#x27;s built-in `<transition>` component. All you need to do is wrap your `ComboboxOptions` instance in a `<transition>`, and the transition will be applied automatically.

`<template>
  <Combobox v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />

    <!-- Use Vue's built-in `transition` component to add transitions. -->

    <transition

      enter-active-class="transition duration-100 ease-out"

      enter-from-class="transform scale-95 opacity-0"

      enter-to-class="transform scale-100 opacity-100"

      leave-active-class="transition duration-75 ease-out"

      leave-from-class="transform scale-100 opacity-100"

      leave-to-class="transform scale-95 opacity-0"

    >
      <ComboboxOptions>
        <ComboboxOption
          v-for="person in filteredPeople"
          :key="person.id"
          :value="person"
        >
          {{ person.name }}
        </ComboboxOption>
      </ComboboxOptions>

    </transition>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

If you&#x27;d like to coordinate multiple transitions for different children of your Combobox, check out the [Transition component included in Headless UI](/v1/vue/transition).

## [](#rendering-as-different-elements)Rendering as different elements

By default, the `Combobox` and its subcomponents each render a default element that is sensible for that component.

For example, `ComboboxLabel` renders a `label` by default, `ComboboxInput`
renders an `input`, `ComboboxButton` renders a `button`, `ComboboxOptions`
renders a `ul`, and `ComboboxOption` renders a `li`. By contrast, `Combobox`
*does not render an element*, and instead renders its children directly.

This is easy to change using the `as` prop, which exists on every component.

`<template>
  <!-- Render a `div` instead of nothing -->

  <Combobox as="div" v-model="selectedPerson">
    <ComboboxInput
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    />

    <!-- Render a `div` instead of a `ul` -->

    <ComboboxOptions as="div">
      <!-- Render a `span` instead of a `li` -->
      <ComboboxOption

        as="span"
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

To tell an element to render its children directly with no wrapper element, use `as="template"`.

`<template>
  <Combobox v-model="selectedPerson">
    <!-- Render children directly instead of an `input` -->
    <ComboboxInput

      as="template"
      @change="query = $event.target.value"
      :displayValue="(person) => person.name"
    >
      <input />
    </ComboboxInput>

    <ComboboxOptions>
      <ComboboxOption
        v-for="person in filteredPeople"
        :key="person.id"
        :value="person"
      >
        {{ person.name }}
      </ComboboxOption>
    </ComboboxOptions>
  </Combobox>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxOptions,
    ComboboxOption,
  } from '@headlessui/vue'

  const people = [
    { id: 1, name: 'Durward Reynolds' },
    { id: 2, name: 'Kenton Towne' },
    { id: 3, name: 'Therese Wunsch' },
    { id: 4, name: 'Benedict Kessler' },
    { id: 5, name: 'Katelyn Rohan' },
  ]
  const selectedPerson = ref(people[0])
  const query = ref('')

  const filteredPeople = computed(() =>
    query.value === ''
      ? people
      : people.filter((person) => {
          return person.name.toLowerCase().includes(query.value.toLowerCase())
        })
  )
</script>
`

## [](#accessibility-notes)Accessibility notes

### [](#focus-management)Focus management
When a Combobox is toggled open, the `ComboboxInput` stays focused.

The `ComboboxButton` is ignored for the default tab flow, this means that pressing `Tab` in the `ComboboxInput` will skip passed the `ComboboxButton`.

### [](#mouse-interaction)Mouse interaction

Clicking a `ComboboxButton` toggles the options list open and closed. Clicking anywhere outside of the options list will close the combobox.

### [](#keyboard-interaction)Keyboard interaction

CommandDescription
ArrowDown,  or ArrowUp when `ComboboxInput` is focused

Opens combobox and focuses the selected item

Enter, Space, ArrowDown,  or ArrowUp when `ComboboxButton` is focused

Opens combobox, focuses the input and selects the selected item

Esc when combobox is open

Closes combobox and restores the selected item in the input field

ArrowDown or ArrowUp when combobox is open

Focuses previous/next non-disabled item

Home or PageUp when combobox is open

Focuses first non-disabled item

End or PageDown when combobox is open

Focuses last non-disabled item

Enter when combobox is open

Selects the current item

Enter when combobox is closed and in a form

Submits the form

Tab when combobox is open

Selects the current active item and closes the combobox

A–Z or a–z when combobox is open

Calls the `onChange` which allows you to filter the list

### [](#other)Other

All relevant ARIA attributes are automatically managed.

## [](#component-api)Component API

### [](#combobox)Combobox

The main Combobox component.

PropDefaultDescription`as``template`
`String | Component`

The element or component the `Combobox` should render as.

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

Use this to disable the entire combobox component & related children.

`name`—
`String`

The name used when using this component inside a form.

`nullable`—
`Boolean`

Whether you can clear the combobox or not.

`multiple``false`
`Boolean`

Whether multiple options can be selected or not.

Slot PropDescription`value`
`T`

The selected value.

`open`
`Boolean`

Whether or not the combobox is open.

`disabled`
`Boolean`

Whether or not the combobox is disabled.

`activeIndex`
`Number | null`

The index of the active option or null if none is active.

`activeOption`
`T | null`

The active option or null if none is active.

### [](#combobox-input)ComboboxInput

The Combobox&#x27;s input.

PropDefaultDescription`as``input`
`String | Component`

The element or component the `ComboboxInput` should render as.

`displayValue`—
`(item: T) => string`

The string representation of your `value`.

Render PropDescription`open`
`Boolean`

Whether or not the Combobox is open.

`disabled`
`Boolean`

Whether or not the Combobox is disabled.

### [](#combobox-button)ComboboxButton

The Combobox&#x27;s button.

PropDefaultDescription`as``button`
`String | Component`

The element or component the `ComboboxButton` should render as.

Slot PropDescription`value`
`T`

The selected value.

`open`
`Boolean`

Whether or not the Combobox is open.

`disabled`
`Boolean`

Whether or not the Combobox is disabled.

### [](#combobox-label)ComboboxLabel

A label that can be used for more control over the text your Combobox will announce to screenreaders. Its `id` attribute will be automatically generated and linked to the root `Combobox` component via the `aria-labelledby` attribute.

PropDefaultDescription`as``label`
`String | Component`

The element or component the `ComboboxLabel` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the Combobox is open.

`disabled`
`Boolean`

Whether or not the Combobox is disabled.

### [](#combobox-options)ComboboxOptions

The component that directly wraps the list of options in your custom Combobox.

PropDefaultDescription`as``ul`
`String | Component`

The element or component the `ComboboxOptions` should render as.

`static``false`
`Boolean`

Whether the element should ignore the internally managed open/closed
state.

`unmount``true`
`Boolean`

Whether the element should be unmounted or hidden based on the open/closed
state.

`hold``false`
`boolean`

Whether or not the active option should stay active even when the mouse
leaves the active option.

Slot PropDescription`open`
`Boolean`

Whether or not the Combobox is open.

### [](#combobox-option)ComboboxOption

Used to wrap each item within your Combobox.

PropDefaultDescription`value`—
`T`

The option value.

`as``li`
`String | Component`

The element or component the `ComboboxOption` should render as.

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