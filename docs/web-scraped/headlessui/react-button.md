# Source: https://headlessui.com/react/button

React
[Vue](/v1/vue)

# Button

A light wrapper around the native button element that provides more opinionated states for things like hover and
focus.

PreviewCode

## [](#installation)Installation

To get started, install Headless UI via npm:

```
npm install @headlessui/react
```

## [](#basic-example)Basic example

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

You can pass any props to a `Button` that you&#x27;d normally pass to the native `button` element.

## [](#styling)Styling

Headless UI keeps track of a lot of state about each component, like whether or not an input is focused, whether a
popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t see this information in your
UI until you provide the styles you want for each state yourself.

### [](#using-data-attributes)Using data attributes

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each
component exposes.

For example, the `Button` component exposes a `data-hover` attribute, which tells you if the button is currently being
hovered by the mouse, and a `data-active` attribute, which tells you if the button is currently being pressed.

```
<!-- Rendered `Button` -->
<button type="button" data-hover data-active></button>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally
apply styles based on the presence of these data attributes. If you&#x27;re using Tailwind CSS, the
[data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Button } from '@headlessui/react'

function Example() {
  return (

    <Button className="rounded bg-sky-600 px-4 py-2 text-sm text-white data-hover:bg-sky-500 data-hover:data-active:bg-sky-700">
      Save changes
    </Button>
  )
}

```

See the [component API](#component-api) for a list of all the available data attributes.

### [](#using-render-props)Using render props

Each component also exposes information about its current state via
[render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or
render different content.

For example, the `Button` component exposes a `hover` state, which tells you if the button is currently being hovered by
the mouse, and an `active` state, which tells you if the button is currently being pressed.

```
import { Button } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Button as={Fragment}>

      {({ hover, active }) => (
        <button
          className={clsx(
            'rounded px-4 py-2 text-sm text-white',

            !hover && !active && 'bg-sky-600',

            hover && !active && 'bg-sky-500',

            active && 'bg-sky-700'
          )}
        >
          Save changes
        </button>

      )}
    </Button>
  )
}

```

See the [component API](#component-api) for a list of all the available render props.

## [](#examples)Examples

### [](#disabling-a-button)Disabling a button

Add the `disabled` prop to a `Button` to disable it:

```
import { Button } from '@headlessui/react'

function Example() {
  return (
    <Button

      disabled
      className="rounded bg-sky-600 px-4 py-2 text-sm text-white data-active:bg-sky-700 data-disabled:bg-gray-500 data-hover:bg-sky-500"
    >
      Save changes
    </Button>
  )
}

```

## [](#component-api)Component API

### [](#button)Button

A thin wrapper around the native `button` element.

PropDefaultDescription`as``button`
`String | Component`

The element or component the button should render as.

`disabled``false`
`Boolean`

Whether or not the button is disabled.

`autoFocus``false`
`Boolean`

Whether or not the button should receive focus when first rendered.

`type``button`
`String`

The button type.

Data AttributeRender PropDescription`data-disabled``disabled`
`Boolean`

Whether or not the button is disabled.

`data-focus``focus`
`Boolean`

Whether or not the button is focused.

`data-hover``hover`
`Boolean`

Whether or not the button is hovered.

`data-active``active`
`Boolean`

Whether or not the button is in an active or pressed state.

`data-autofocus``autofocus`
`Boolean`

Whether or not the `autoFocus` prop was set to `true`.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned [Tailwind CSS button component examples](https://tailwindui.com/components/application-ui/elements/buttons), check out **Tailwind Plus** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[Explore more predesigned examples →](https://tailwindcss.com/plus)
[](https://tailwindcss.com/plus)