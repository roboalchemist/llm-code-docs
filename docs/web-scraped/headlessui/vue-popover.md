# Source: https://headlessui.com/v1/vue/popover

# Popover

Popovers are perfect for floating panels with arbitrary content like
navigation menus, mobile menus and flyout menus.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Popovers are built using the `Popover`, `PopoverButton`, and `PopoverPanel` components.

Clicking the `PopoverButton` will automatically open/close the `PopoverPanel`. When the panel is open, clicking anywhere outside of its contents, pressing the Escape key, or tabbing away from it will close the Popover.

`<template>
  <Popover class="relative">
    <PopoverButton>Solutions</PopoverButton>

    <PopoverPanel class="absolute z-10">
      <div class="grid grid-cols-2">
        <a href="/analytics">Analytics</a>
        <a href="/engagement">Engagement</a>
        <a href="/security">Security</a>
        <a href="/integrations">Integrations</a>
      </div>

      <img src="/solutions.jpg" alt="" />
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
</script>`

These components are completely unstyled, so how you style your `Popover` is up to you. In our example we&#x27;re using absolute positioning on the `PopoverPanel` to position it near the `PopoverButton` and not disturb the normal document flow.

## [](#styling-different-states)Styling different states

Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a popover is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `Popover` component exposes an `open` state, which tells you if the popover is currently open.

`<template>

  <Popover v-slot="{ open }">
    <!-- Use the `open` state to conditionally change the direction of the chevron icon. -->
    <PopoverButton>
      Solutions

      <ChevronDownIcon :class="{ 'rotate-180 transform': open }" />
    </PopoverButton>

    <PopoverPanel>
      <a href="/insights">Insights</a>
      <a href="/automations">Automations</a>
      <a href="/reports">Reports</a>
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
  import { ChevronDownIcon } from '@heroicons/vue/20/solid'
</script>
`

For a complete list of all the available slot props, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot prop API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `Popover` component renders when the popover is open:

`<!-- Rendered `Popover` -->
<div data-headlessui-state="open">
  <button data-headlessui-state="open">Solutions</button>
  <div data-headlessui-state="open">
    <a href="/insights">Insights</a>
    <a href="/automations">Automations</a>
    <a href="/reports">Reports</a>
  </div>
</div>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-open:*`:

`<template>
  <Popover>
    <PopoverButton>
      Solutions

      <ChevronDownIcon class="ui-open:rotate-180 ui-open:transform" />
    </PopoverButton>

    <PopoverPanel>
      <a href="/insights">Insights</a>
      <a href="/automations">Automations</a>
      <a href="/reports">Reports</a>
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
  import { ChevronDownIcon } from '@heroicons/vue/20/solid'
</script>
`

## [](#showing-hiding-the-popover)Showing/hiding the popover
By default, your `PopoverPanel` will be shown/hidden automatically based on the internal open state tracked within the `Popover` component itself.

`<template>
  <Popover>
    <PopoverButton>Solutions</PopoverButton>
    <!--
      By default, the `PopoverPanel` will automatically show/hide
      when the `PopoverButton` is pressed.
    -->
    <PopoverPanel>
      <!-- ... -->
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
</script>`

If you&#x27;d rather handle this yourself (perhaps because you need to add an extra wrapper element for one reason or another), you can pass a `static` prop to the `PopoverPanel` to tell it to always render, and then use the `open` slot prop to control when the panel is shown/hidden yourself.

`<template>

  <Popover v-slot="{ open }">
    <PopoverButton>Solutions</PopoverButton>

    <div v-if="open">

      <!--
        Using the `static` prop, the `PopoverPanel` is always

        rendered and the `open` state is ignored.
      -->
      <PopoverPanel static>
        <!-- ... -->
      </PopoverPanel>
    </div>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
</script>
`

## [](#closing-popovers-manually)Closing popovers manually
Since popovers can contain interactive content like form controls, we can&#x27;t automatically close them when you click something inside of them like we can with `Menu` components.

To close a popover manually when clicking a child of its panel, render that child as a `PopoverButton`. You can use the `:as` prop to customize which element is being rendered.

`<template>
  <Popover>
    <PopoverButton>Solutions</PopoverButton>

    <PopoverPanel>

      <PopoverButton :as="MyLink" href="/insights">Insights</PopoverButton>
      <!-- ... -->
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
  import MyLink from './MyLink'
</script>
`

Alternatively, `Popover` and `PopoverPanel` expose a `close()` slot prop which you can use to imperatively close the panel, say after running an async action:

`<template>
  <Popover>
    <PopoverButton>Solutions</PopoverButton>

    <PopoverPanel v-slot="{ close }">

      <button @click="accept(close)">Read and accept</button>

    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'

  async function accept(close) {

    await fetch('/accept-terms', { method: 'POST' })

    close()

  }
</script>
`

By default the `PopoverButton` receives focus after calling `close()`, but you can change this by passing a ref into `close(ref)`.

## [](#adding-an-overlay)Adding an overlay

If you&#x27;d like to style a backdrop over your application UI whenever you open a Popover, use the `PopoverOverlay` component:

`<template>
  <Popover v-slot="{ open }">
    <PopoverButton>Solutions</PopoverButton>

    <PopoverOverlay class="fixed inset-0 bg-black opacity-30" />

    <PopoverPanel>
      <!-- ... -->
    </PopoverPanel>
  </Popover>
</template>

<script setup>
  import {
    Popover,
    PopoverOverlay,
    PopoverButton,
    PopoverPanel,
  } from '@headlessui/vue'
</script>
`

In this example, we put the `PopoverOverlay` before the `Panel` in the DOM so
that it doesn&#x27;t cover up the panel&#x27;s contents.

But like all the other components, `PopoverOverlay` is completely headless, so
how you style it is up to you.

## [](#transitions)Transitions

To animate the opening/closing of your Popover&#x27;s panel, you can use Vue&#x27;s built-in `<transition>` element. All you need to do is wrap your `PopoverPanel` in a `<transition>`, and the transition will be applied automatically.

`<template>
  <Popover>
    <PopoverButton>Solutions</PopoverButton>

    <!-- Use the built-in `transition` component to add transitions. -->

    <transition

      enter-active-class="transition duration-200 ease-out"

      enter-from-class="translate-y-1 opacity-0"

      enter-to-class="translate-y-0 opacity-100"

      leave-active-class="transition duration-150 ease-in"

      leave-from-class="translate-y-0 opacity-100"

      leave-to-class="translate-y-1 opacity-0"

    >
      <PopoverPanel>
        <!-- ... -->
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
</script>
`

If you&#x27;d like to coordinate multiple transitions for different children of your Popover, check out the [Transition component included in Headless UI](/v1/vue/transition).

## [](#grouping-related-popovers)Grouping related popovers

When rendering several related Popovers, for example in a site&#x27;s header navigation, use the `PopoverGroup` component. This ensures panels stay open while users are tabbing between Popovers within a group, but closes any open panel once the user tabs outside of the group:

`<template>

  <PopoverGroup>
    <Popover>
      <PopoverButton>Product</PopoverButton>
      <PopoverPanel>
        <!-- ... -->
      </PopoverPanel>
    </Popover>

    <Popover>
      <PopoverButton>Solutions</PopoverButton>
      <PopoverPanel>
        <!-- ... -->
      </PopoverPanel>
    </Popover>

  </PopoverGroup>
</template>

<script setup>
  import {
    PopoverGroup,
    Popover,
    PopoverButton,
    PopoverPanel,
  } from '@headlessui/vue'
</script>
`

## [](#rendering-as-different-elements)Rendering as different elements
`Popover` and its subcomponents each render a default element that is sensible for that component: the `Popover`, `Overlay`, `Panel` and `Group` components all render a `<div>`, and the `Button` component renders a `<button>`.

This is easy to change using the `as` prop, which exists on every component.

`<template>
  <!-- Render a `nav` instead of a `div` -->

  <Popover as="nav">
    <PopoverButton>Solutions</PopoverButton>

    <!-- Render a `form` instead of a `div` -->

    <PopoverPanel as="form"><!-- ... --></PopoverPanel>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
</script>
`

## [](#accessibility-notes)Accessibility notes

### [](#focus-management)Focus management
Pressing Tab on an open panel will focus the first focusable element within the panel&#x27;s contents. If a `PopoverGroup` is being used, Tab cycles from the end of an open panel&#x27;s content to the next Popover&#x27;s button.

### [](#mouse-interaction)Mouse interaction

Clicking a `PopoverButton` toggles a panel open and closed. Clicking anywhere outside of an open panel will close that panel.

### [](#keyboard-interaction)Keyboard interaction

CommandDescription
Enter or Spacewhen a `PopoverButton` is focused.

Toggle panel

Esc

Closes any open Popovers

Tab

Cycle through an open panel&#x27;s contents

Tabbing out of an open panel will close that panel, and tabbing from one
open panel to a sibling Popover&#x27;s button (within a PopoverGroup) closes
the first panel

Shift + Tab

Cycle backwards through the focus order

### [](#other)Other

Nested Popovers are supported, and all panels will close correctly whenever the root panel is closed.

All relevant ARIA attributes are automatically managed.

## [](#when-to-use-a-popover)When to use a Popover

Here&#x27;s how Popovers compare to other similar components:

- 

**`<Menu />`**. Popovers are more general-purpose than Menus. Menus only support very restricted content and have specific accessibility semantics. Arrow keys also navigate a Menu&#x27;s items. Menus are best for UI elements that resemble things like the menus you&#x27;d find in the title bar of most operating systems. If your floating panel has images or more markup than simple links, use a Popover.

- 

**`<Disclosure />`**. Disclosures are useful for things that typically reflow the document, like Accordions. Popovers also have extra behavior on top of Disclosures: they render overlays, and are closed when the user either clicks the overlay (by clicking outside of the Popover&#x27;s content) or presses the escape key. If your UI element needs this behavior, use a Popover instead of a Disclosure.

- 

**`<Dialog />`**. Dialogs are meant to grab the user&#x27;s full attention. They typically render a floating panel in the center of the screen, and use a backdrop to dim the rest of the application&#x27;s contents. They also capture focus and prevent tabbing away from the Dialog&#x27;s contents until the Dialog is dismissed. Popovers are more contextual, and are usually positioned near the element that triggered them.

## [](#component-api)Component API

### [](#popover)Popover

The main Popover component.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `Popover` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the popover is open.

`close`
`(ref?: ref | HTMLElement) => void`

Closes the popover and refocuses `PopoverButton`. Optionally pass in a
**ref** or **HTMLElement** to focus that element instead.

### [](#popover-overlay)PopoverOverlay

This can be used to create an overlay for your Popover component. Clicking on the overlay will close the Popover.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `PopoverOverlay` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the popover is open.

### [](#popover-button)PopoverButton

This is the trigger component to toggle a Popover. You can also use this
`PopoverButton` component inside a `PopoverPanel`, if you do so, then it will
behave as a `close` button. We will also make sure to provide the correct
`aria-*` attributes onto the button.

PropDefaultDescription`as``button`
`String | Component`

The element or component the `PopoverButton` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the popover is open.

### [](#popover-panel)PopoverPanel

This component contains the contents of your Popover.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `PopoverPanel` should render as.

`focus``false`
`Boolean`

This will force focus inside the `PopoverPanel` when the `Popover` is
open. It will also close the `Popover` if focus left this component.

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

Whether or not the popover is open.

`close`
`(ref?: ref | HTMLElement) => void`

Closes the popover and refocuses `PopoverButton`. Optionally pass in a
**ref** or **HTMLElement** to focus that element instead.

### [](#popover-group)PopoverGroup

Link related sibling popovers by wrapping them in a `PopoverGroup`. Tabbing out of one `PopoverPanel` will focus the next popover&#x27;s `PopoverButton`, and tabbing outside of the `PopoverGroup` completely will close all popovers inside the group.

PropDefaultDescription`as``div`
`String | Component`

The element or component the `PopoverGroup` should render as.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)