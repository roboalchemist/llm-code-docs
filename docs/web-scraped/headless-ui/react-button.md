# Source: https://headlessui.com/react/button

Title: Headless UI

URL Source: https://headlessui.com/react/button

Markdown Content:
A light wrapper around the native button element that provides more opinionated states for things like hover and focus.

[](https://headlessui.com/react/button#installation)
----------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/button#basic-example)
-----------------------------------------------------

Buttons are built using the `Button` component:

```
import { Button } from '@headlessui/react'

function Example() {
  return (
    <Button className="rounded bg-sky-600 px-4 py-2 text-sm text-white data-active:bg-sky-700 data-hover:bg-sky-500">
      Save changes
    </Button>
  )
}
```

You can pass any props to a `Button` that you'd normally pass to the native `button` element.

[](https://headlessui.com/react/button#styling)
-----------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not an input is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/button#using-data-attributes)

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, the `Button` component exposes a `data-hover` attribute, which tells you if the button is currently being hovered by the mouse, and a `data-active` attribute, which tells you if the button is currently being pressed.

```
<!-- Rendered `Button` -->
<button type="button" data-hover data-active></button>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Button } from '@headlessui/react'

function Example() {
  return (
    <Button className="rounded bg-sky-600 px-4 py-2 text-sm text-white data-hover:bg-sky-500 data-hover:data-active:bg-sky-700">      Save changes
    </Button>
  )
}
```

See the [component API](https://headlessui.com/react/button#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/button#using-render-props)

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, the `Button` component exposes a `hover` state, which tells you if the button is currently being hovered by the mouse, and an `active` state, which tells you if the button is currently being pressed.

```
import { Button } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Button as={Fragment}>
      {({ hover, active }) => (        <button
          className={clsx(
            'rounded px-4 py-2 text-sm text-white',
            !hover && !active && 'bg-sky-600',            hover && !active && 'bg-sky-500',            active && 'bg-sky-700'          )}
        >
          Save changes
        </button>
      )}    </Button>
  )
}
```

See the [component API](https://headlessui.com/react/button#component-api) for a list of all the available render props.

[](https://headlessui.com/react/button#examples)
------------------------------------------------

### [](https://headlessui.com/react/button#disabling-a-button)

Add the `disabled` prop to a `Button` to disable it:

```
import { Button } from '@headlessui/react'

function Example() {
  return (
    <Button
      disabled      className="rounded bg-sky-600 px-4 py-2 text-sm text-white data-active:bg-sky-700 data-disabled:bg-gray-500 data-hover:bg-sky-500"
    >
      Save changes
    </Button>
  )
}
```

[](https://headlessui.com/react/button#component-api)
-----------------------------------------------------

### [](https://headlessui.com/react/button#button)

A thin wrapper around the native `button` element.
