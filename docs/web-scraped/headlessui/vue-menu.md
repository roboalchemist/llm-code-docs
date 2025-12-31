# Source: https://headlessui.com/v1/vue/menu

# Menu (Dropdown)

Menus offer an easy way to build custom, accessible dropdown components with
robust support for keyboard navigation.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Menu Buttons are built using the `Menu`, `MenuButton`, `MenuItems`, and `MenuItem` components.

The `MenuButton` will automatically open/close the `MenuItems` when clicked, and when the menu is open, the list of items receives focus and is automatically navigable via the keyboard.

`<template>
  <Menu>
    <MenuButton>More</MenuButton>
    <MenuItems>
      <MenuItem v-slot="{ active }">
        <a :class='{ "bg-blue-500": active }' href="/account-settings">
          Account settings
        </a>
      </MenuItem>
      <MenuItem v-slot="{ active }">
        <a :class='{ "bg-blue-500": active }' href="/account-settings">
          Documentation
        </a>
      </MenuItem>
      <MenuItem disabled>
        <span class="opacity-75">Invite a friend (coming soon!)</span>
      </MenuItem>
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
</script>`

## [](#styling-different-states)Styling different states
Headless UI keeps track of a lot of state about each component, like which listbox option is currently selected, whether a popover is open or closed, or which item in a menu is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `MenuItem` component exposes an `active` state, which tells you if the item is currently focused via the mouse or keyboard.

`<template>
  <Menu>
    <MenuButton>Options</MenuButton>
    <MenuItems>
      <!-- Use the `active` state to conditionally style the active item. -->
      <MenuItem
        v-for="link in links"
        :key="link.href"
        as="template"

        v-slot="{ active }"
      >
        <a
          :href="link.href"

          :class="{ 'bg-blue-500 text-white': active, 'bg-white text-black': !active }"
        >
          {{ link.label }}
        </a>
      </MenuItem>
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'

  const links = [
    { href: '/account-settings', label: 'Account settings' },
    { href: '/support', label: 'Support' },
    { href: '/license', label: 'License' },
    { href: '/sign-out', label: 'Sign out' },
  ]
</script>
`

For a complete list of all the available slot props, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot prop API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `MenuItems` component with some child `MenuItem` components renders when the menu is open and the second item is `active`:

`<!-- Rendered `MenuItems` -->
<ul data-headlessui-state="open">
  <li data-headlessui-state="">Account settings</li>
  <li data-headlessui-state="active">Support</li>
  <li data-headlessui-state="">License</li>
</ul>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-open:*` and `ui-active:*`:

`<template>
  <Menu>
    <MenuButton>Options</MenuButton>
    <MenuItems>
      <!-- Use the `active` state to conditionally style the active item. -->
      <MenuItem
        v-for="link in links"
        :key="link.href"
        :href="link.href"
        as="a"

        class="ui-active:bg-blue-500 ui-active:text-white ui-not-active:bg-white ui-not-active:text-black"
      >
        {{ link.label }}
      </MenuItem>
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'

  const links = [
    { href: '/account-settings', label: 'Account settings' },
    { href: '/support', label: 'Support' },
    { href: '/license', label: 'License' },
    { href: '/sign-out', label: 'Sign out' },
  ]
</script>
`

## [](#showing-hiding-the-menu)Showing/hiding the menu
By default, your `MenuItems` instance will be shown/hidden automatically based on the internal `open` state tracked within the `Menu` component itself.

`<template>
  <Menu>
    <MenuButton>More</MenuButton>

    <!--
      By default, the `MenuItems` will automatically show/hide
      when the `MenuButton` is pressed.
    -->
    <MenuItems>
      <MenuItem><!-- ... --></MenuItem>
      <!-- ... -->
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
</script>`

If you&#x27;d rather handle this yourself (perhaps because you need to add an extra wrapper element for one reason or another), you can add a `static` prop to the `MenuItems` instance to tell it to always render, and inspect the `open` slot prop provided by the `Menu` to control which element is shown/hidden yourself.

`<template>

  <Menu v-slot="{ open }">
    <MenuButton>More</MenuButton>

    <div v-show="open">
      <!--
        Using the `static` prop, the `MenuItems` are always
        rendered and the `open` state is ignored.
      -->

      <MenuItems static>
        <MenuItem><!-- ... --></MenuItem>
        <!-- ... -->
      </MenuItems>
    </div>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
</script>
`

## [](#closing-menus-manually)Closing menus manually
The menu will already close by default, however it can happen that 3rd party `Link` components use `event.preventDefault()`, which prevents the default behaviour and therefore won&#x27;t close the menu.

The `Menu` and `MenuItem` expose a `close()` slot prop which you can use to imperatively close the menu:

`<template>
  <Menu>
    <MenuButton>Terms</MenuButton>

    <MenuItems>

      <MenuItem v-slot="{ close }">

        <MyCustomLink href="/" @click="close">Read and accept</MyCustomLink>
      </MenuItem>
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
  import { MyCustomLink } from './MyCustomLink'
</script>
`

## [](#disabling-an-item)Disabling an item
Use the `disabled` prop to disable a `MenuItem`. This will make it unselectable via keyboard navigation, and it will be skipped when pressing the up/down arrows.

`<template>
  <Menu>
    <MenuButton>More</MenuButton>

    <MenuItems>
      <!-- ... -->

      <!-- This item will be skipped by keyboard navigation. -->

      <MenuItem disabled>
        <span class="opacity-75">Invite a friend (coming soon!)</span>
      </MenuItem>
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
</script>
`

## [](#transitions)Transitions
To animate the opening/closing of the menu panel, you can use Vue&#x27;s built-in `<transition>` component. All you need to do is wrap your `MenuItems` instance in a `<transition>`, and the transition will be applied automatically.

`<template>
  <Menu>
    <MenuButton>More</MenuButton>

    <!-- Use Vue's built-in `transition` element to add transitions. -->

    <transition

      enter-active-class="transition duration-100 ease-out"

      enter-from-class="transform scale-95 opacity-0"

      enter-to-class="transform scale-100 opacity-100"

      leave-active-class="transition duration-75 ease-out"

      leave-from-class="transform scale-100 opacity-100"

      leave-to-class="transform scale-95 opacity-0"

    >
      <MenuItems>
        <MenuItem><!-- ... --></MenuItem>

        <!-- ... -->
      </MenuItems>
    </transition>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
</script>
`

If you&#x27;d like to coordinate multiple transitions for different children of your Menu, check out the [Transition component included in Headless UI](/v1/vue/transition).

## [](#rendering-additional-content)Rendering additional content

The accessibility semantics of `role="menu"` are fairly strict and any children of a `Menu` that are not `MenuItem` components will be automatically hidden from assistive technology to make sure the menu works the way screen reader users expect.

For this reason, rendering any children other than `MenuItem` components is discouraged as that content will be inaccessible to people using assistive technology.

If you want to build a dropdown with more flexible content, consider using [Popover](/v1/vue/popover) instead.

## [](#rendering-as-different-elements)Rendering as different elements

By default, the `Menu` and its subcomponents each render a default element that is sensible for that component.

For example, `MenuButton` renders a `button` by default, and `MenuItems`
renders a `div`. By contrast, `Menu` and `MenuItem` *do not render an element*,
and instead render their children directly by default.

This is easy to change using the `as` prop, which exists on every component.

`<template>
  <!-- Render a `div` instead of no wrapper element -->

  <Menu as="div">
    <MenuButton>More</MenuButton>

    <!-- Render a `section` instead of a `div` -->

    <MenuItems as="section">
      <MenuItem v-slot="{ active }">
        <a :class='{ "bg-blue-500": active }' href="/account-settings">
          Account settings
        </a>
      </MenuItem>

      <!-- ... -->
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
</script>
`

To tell an element to render its children directly with no wrapper element, use `as="template"`.

`<template>
  <Menu>
    <!-- Render no wrapper, instead pass in a `button` manually. -->

    <MenuButton as="template">
      <button>More</button>
    </MenuButton>
    <MenuItems>
      <MenuItem v-slot="{ active }">
        <a :class='{ "bg-blue-500": active }' href="/account-settings">
          Account settings
        </a>
      </MenuItem>
      <!-- ... -->
    </MenuItems>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
</script>
`

This is important if you are using an interactive
element like an `<a>` tag inside the `MenuItem`. If
the `MenuItem` had an `as="div"`, then the props
provided by Headless UI would be forwarded to the `div`
instead of the `a`, which means that you can&#x27;t go to
the URL provided by the `<a>` tag anymore via your
keyboard.

## [](#accessibility-notes)Accessibility notes

### [](#focus-management)Focus management

Clicking the `MenuButton` toggles the menu and focuses the `MenuItems` component. Focus is trapped within the open menu until Escape is pressed or the user clicks outside the menu. Closing the menu returns focus to the `MenuButton`.

### [](#mouse-interaction)Mouse interaction

Clicking a `MenuButton` toggles the menu. Clicking anywhere outside of an open menu will close that menu.

### [](#keyboard-interaction)Keyboard interaction

CommandDescription
Enter or Space when `MenuButton` is focused

Opens menu and focuses first non-disabled item

ArrowDown or ArrowUp when `MenuButton` is focused

Opens menu and focuses first/last non-disabled item

Esc when menu is open

Closes any open Menus

ArrowDown or ArrowUp when menu is open

Focuses previous/next non-disabled item

Home or PageUp when menu is open

Focuses first non-disabled item

End or PageDown when menu is open

Focuses last non-disabled item

Enter or Space when menu is open

Activates/clicks the current menu item

A–Z or a–z when menu is open

Focuses first item that matches keyboard input

### [](#other)Other

All relevant ARIA attributes are automatically managed.

For a full reference on all accessibility features implemented in `Menu`, see [the ARIA spec on Menu Buttons](https://www.w3.org/TR/wai-aria-practices-1.2/#menubutton).

## [](#when-to-use-a-menu)When to use a Menu

Menus are best for UI elements that resemble things like the menus you&#x27;d find in the title bar of most operating systems. They have specific accessibility semantics, and their content should be restricted to a list of links or buttons. Focus is trapped in an open menu, so you cannot Tab through the content or away from the menu. Instead, the arrow keys navigate through a Menu&#x27;s items.

Here&#x27;s when you might use other similar components from Headless UI:

- 

**`<Popover />`**. Popovers are general-purpose floating menus. They appear near the button that triggers them, and you can put arbitrary markup in them like images or non-clickable content. The Tab key navigates the contents of a Popover like it would any other normal markup. They&#x27;re great for building header nav items with expandable content and flyout panels.

- 

**`<Disclosure />`**. Disclosures are useful for elements that expand to reveal additional information, like a toggleable FAQ section. They are typically rendered inline and reflow the document when they&#x27;re shown or hidden.

- 

**`<Dialog />`**. Dialogs are meant to grab the user&#x27;s full attention. They typically render a floating panel in the center of the screen, and use a backdrop to dim the rest of the application&#x27;s contents. They also capture focus and prevent tabbing away from the Dialog&#x27;s contents until the Dialog is dismissed.

## [](#component-api)Component API

### [](#menu)Menu

PropDefaultDescription`as``template`
`String | Component`

The element or component the `Menu` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the Menu is open.

`close`
`() => void`

Closes the menu and refocuses `MenuButton`.

### [](#menu-button)MenuButton

PropDefaultDescription`as``button`
`String | Component`

The element or component the `MenuButton` should render as.

Slot PropDescription`open`
`Boolean`

Whether or not the Menu is open.

### [](#menu-items)MenuItems

PropDefaultDescription`as``div`
`String | Component`

The element or component the `MenuItems` should render as.

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

Whether or not the Menu is open.

### [](#menu-item)MenuItem

PropDefaultDescription`as``template`
`String | Component`

The element or component the `MenuItem` should render as.

`disabled``false`
`Boolean`

Whether or not the item should be disabled for keyboard navigation and
ARIA purposes.

Slot PropDescription`active`
`Boolean`

Whether or not the item is the active/focused item in the list.

`disabled`
`Boolean`

Whether or not the item is the disabled for keyboard navigation and ARIA
purposes.

`close`
`() => void`

Closes the menu and refocuses `MenuButton`.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)