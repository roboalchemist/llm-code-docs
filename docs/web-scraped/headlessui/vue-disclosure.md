# Source: https://headlessui.com/v1/vue/disclosure

# Disclosure

A simple, accessible foundation for building custom UIs that show and hide
content, like togglable accordion panels.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Disclosures are built using the `Disclosure`, `DisclosureButton` and `DisclosurePanel` components.

The button will automatically open/close the panel when clicked, and all components will receive the appropriate aria-* related attributes like `aria-expanded` and `aria-controls`.

`<template>
  <Disclosure>
    <DisclosureButton class="py-2">
      Is team pricing available?
    </DisclosureButton>
    <DisclosurePanel class="text-gray-500">
      Yes! You can purchase a license that you can share with your entire team.
    </DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
</script>`

## [](#styling-different-states)Styling different states
Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a disclosure is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `Disclosure` component exposes an `open` state, which tells you if the disclosure is currently open.

`<template>

  <Disclosure v-slot="{ open }">
    <!-- Use the `open` state to conditionally change the direction of an icon. -->
    <DisclosureButton class="py-2">
      <span>Do you offer technical support?</span>

      <ChevronRightIcon :class="open && 'rotate-90 transform'" />
    </DisclosureButton>
    <DisclosurePanel>No</DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
  import { ChevronRightIcon } from '@heroicons/vue/20/solid'
</script>
`

For a complete list of all the available slot props, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot prop API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `Disclosure` component renders when the disclosure is open:

`<!-- Rendered `Disclosure` -->
<div data-headlessui-state="open">
  <button data-headlessui-state="open">Do you offer technical support?</button>
  <div data-headlessui-state="open">No</div>
</div>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-open:*`:

`<template>
  <Disclosure>
    <DisclosureButton class="py-2">
      <span>Do you offer technical support?</span>

      <ChevronRightIcon class="ui-open:rotate-90 ui-open:transform" />
    </DisclosureButton>
    <DisclosurePanel>No</DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
  import { ChevronRightIcon } from '@heroicons/vue/20/solid'
</script>
`

## [](#showing-hiding-the-panel)Showing/hiding the panel
By default, your `DisclosurePanel` will be shown/hidden automatically based on the internal open state tracked within the `Disclosure` component itself.

`<template>
  <Disclosure>
    <DisclosureButton>Is team pricing available?</DisclosureButton>

    <!--
      By default, the `DisclosurePanel` will automatically show/hide
      when the `DisclosureButton` is pressed.
    -->
    <DisclosurePanel>
      Yes! You can purchase a license that you can share with your entire team.
    </DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
</script>`

If you&#x27;d rather handle this yourself (perhaps because you need to add an extra wrapper element for one reason or another), you can pass a `static` prop to the `DisclosurePanel` to tell it to always render, and then use the `open` slot prop to control when the panel is shown/hidden yourself.

`<template>

  <Disclosure v-slot="{ open }">
    <DisclosureButton>Is team pricing available?</DisclosureButton>

    <div v-show="open">
      <!--
        Using the `static` prop, the `DisclosurePanel` is always
        rendered and the `open` state is ignored.
      -->

      <DisclosurePanel static>
        Yes! You can purchase a license that you can share with your entire
        team.
      </DisclosurePanel>
    </div>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
</script>
`

## [](#closing-disclosures-manually)Closing disclosures manually
To close a disclosure manually when clicking a child of its panel, render that child as a `DisclosureButton`. You can use the `:as` prop to customize which element is being rendered.

`<template>
  <Disclosure>
    <DisclosureButton>Open mobile menu</DisclosureButton>
    <DisclosurePanel>

      <DisclosureButton :as="MyLink" href="/home">Home</DisclosureButton>
      <!-- ... -->
    </DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
  import MyLink from './MyLink'
</script>
`

This is especially useful when using disclosures for things like mobile menus that contain links where you want the disclosure to close when navigating to the next page.

Alternatively, `Disclosure` and `DisclosurePanel` expose a `close()` slot prop which you can use to imperatively close the panel, say after running an async action:

`<template>
  <Disclosure>
    <DisclosureButton>Terms</DisclosureButton>

    <DisclosurePanel v-slot="{ close }">

      <button @click="accept(close)">Read and accept</button>

    </DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'

  async function accept(close) {

    await fetch('/accept-terms', { method: 'POST' })

    close()

  }
</script>
`

By default the `DisclosureButton` receives focus after calling `close()`, but you can change this by passing a ref into `close(ref)`.

## [](#transitions)Transitions

To animate the opening/closing of your Disclosure&#x27;s panel, you can use Vue&#x27;s built-in `<transition>` component. All you need to do is wrap your `DisclosurePanel`in a `<transition>`, and the transition will be applied automatically.

`<template>
  <Disclosure>
    <DisclosureButton>Is team pricing available?</DisclosureButton>

    <!-- Use the built-in `transition` component to add transitions. -->

    <transition

      enter-active-class="transition duration-100 ease-out"

      enter-from-class="transform scale-95 opacity-0"

      enter-to-class="transform scale-100 opacity-100"

      leave-active-class="transition duration-75 ease-out"

      leave-from-class="transform scale-100 opacity-100"

      leave-to-class="transform scale-95 opacity-0"

    >
      <DisclosurePanel>
        Yes! You can purchase a license that you can share with your entire
        team.
      </DisclosurePanel>
    </transition>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
</script>
`

If you&#x27;d like to coordinate multiple transitions for different children of your Disclosure, check out the [Transition component included in Headless UI](/v1/vue/transition).

## [](#rendering-as-different-elements)Rendering as different elements

`Disclosure` and its subcomponents each render a default element that is
sensible for that component: the `Button` renders a `<button>`, `Panel` renders
a `<div>`. By contrast, the root `Disclosure` component *does not render an
element*, and instead renders its children directly by default.

This is easy to change using the `as` prop, which exists on every component.

`<template>
  <!-- Render a `div` for the root `Disclosure` component -->

  <Disclosure as="div">
    <!-- Don't render any element (only children) for the `DisclosureButton` component -->

    <DisclosureButton as="template">
      <button>What languages do you support?</button>
    </DisclosureButton>

    <!-- Render a `ul` for the `DisclosurePanel` component -->

    <DisclosurePanel as="ul">
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </DisclosurePanel>
  </Disclosure>
</template>

<script setup>
  import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  } from '@headlessui/vue'
</script>
`

## [](#accessibility-notes)Accessibility notes

### [](#mouse-interaction)Mouse interaction
Clicking a `DisclosureButton` toggles the Disclosure&#x27;s panel open and closed.

### [](#keyboard-interaction)Keyboard interaction

CommandDescription
Enter or Space when a `DisclosureButton` is focused.

Toggles panel

### [](#other)Other

All relevant ARIA attributes are automatically managed.

## [](#component-api)Component API

### [](#disclosure)Disclosure

The main Disclosure component.

PropDefaultDescription`as``template`
`String | Component`

The element or component the `Disclosure` should render as.

`defaultOpen``false`
`Boolean`

Whether or not the `Disclosure` component should be open by default.

Slot PropDescription`open`
`Boolean`

Whether or not the disclosure is open.

`close`
`(ref?: ref | HTMLElement) => void`

Closes the disclosure and refocuses `DisclosureButton`. Optionally pass in
a **ref** or **HTMLElement** to focus that element instead.

### [](#disclosure-button)DisclosureButton

The trigger component that toggles a Disclosure.

PropDefaultDescription`as``button`
`String | Component`

The element or component the `DisclosureButton` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the disclosure is open.

### [](#disclosure-panel)DisclosurePanel

This component contains the contents of your Disclosure.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `DisclosurePanel` should render as.

`static``false`
`Boolean`

Whether the element should ignore the internally managed open/closed
state.

*Note: `static` and `unmount` can not be used at the same time. You will
get a TypeScript error if you try to do it.*

`unmount``true`
`Boolean`

Whether the element should be unmounted or hidden based on the
open/closed state.

*Note: `static` and `unmount` can not be used at the same time. You will
get a TypeScript error if you try to do it.*

Slot PropDescription`open`
`Boolean`

Whether or not the disclosure is open.

`close`
`(ref?: ref | HTMLElement) => void`

Closes the disclosure and refocuses `DisclosureButton`. Optionally pass in
a **ref** or **HTMLElement** to focus that element instead.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)