# Source: https://headlessui.com/react/input

Title: Headless UI

URL Source: https://headlessui.com/react/input

Markdown Content:
A light wrapper around the native input element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

[](https://headlessui.com/react/input#installation)
---------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/input#basic-example)
----------------------------------------------------

Inputs are built using the `Input` component:

```
import { Input } from '@headlessui/react'

function Example() {
  return <Input name="full_name" type="text" />
}
```

You can pass any props to an `Input` that you'd normally pass to the native `input` element.

[](https://headlessui.com/react/input#styling)
----------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not an input is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/input#using-data-attributes)

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, the `Input` component exposes a `data-focus` attribute, which tells you if the input is currently focused via the mouse or keyboard, and a `data-hover` attribute, which tells you if the input is currently being hovered by the mouse.

```
<!-- Rendered `Input` -->
<input type="text" name="full_name" data-focus data-hover />
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Input } from '@headlessui/react'

function Example() {
  return <Input type="text" name="full_name" className="border data-focus:bg-blue-100 data-hover:shadow" />}
```

See the [component API](https://headlessui.com/react/input#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/input#using-render-props)

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, the `Input` component exposes a `focus` state, which tells you if the input is currently focused via the mouse or keyboard, and a `hover` state, which tells you if the input is currently being hovered by the mouse.

```
import { Input } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Input type="text" name="full_name" as={Fragment}>
      {({ focus, hover }) => <input className={clsx('border', focus && 'bg-blue-100', hover && 'shadow')} />}    </Input>
  )
}
```

See the [component API](https://headlessui.com/react/input#component-api) for a list of all the available render props.

[](https://headlessui.com/react/input#examples)
-----------------------------------------------

### [](https://headlessui.com/react/input#adding-a-label)

Wrap a `Label` and `Input` with the `Field` component to automatically associate them using a generated ID:

```
import { Field, Input, Label } from '@headlessui/react'

function Example() {
  return (
    <Field>      <Label>Name</Label>      <Input name="full_name" />
    </Field>  )
}
```

### [](https://headlessui.com/react/input#adding-a-description)

Use the `Description` component within a `Field` to automatically associate it with an `Input` using the `aria-describedby` attribute:

```
import { Description, Field, Input, Label } from '@headlessui/react'

function Example() {
  return (
    <Field>      <Label>Name</Label>
      <Description>Use your real name so people will recognize you.</Description>      <Input name="full_name" />
    </Field>  )
}
```

### [](https://headlessui.com/react/input#disabling-an-input)

Add the `disabled` prop to the `Field` component to disable an `Input` and its associated `Label` and `Description`:

```
import { Description, Field, Input, Label } from '@headlessui/react'

function Example() {
  return (
    <Field disabled>      <Label className="data-disabled:opacity-50">Name</Label>
      <Description className="data-disabled:opacity-50">Use your real name so people will recognize you.</Description>
      <Input name="full_name" className="data-disabled:bg-gray-100" />
    </Field>
  )
}
```

You can also disable an input outside of a `Field` by adding the disabled prop directly to the `Input` itself.

[](https://headlessui.com/react/input#component-api)
----------------------------------------------------

### [](https://headlessui.com/react/input#input)

A thin wrapper around the native `input` element.

Groups a `Label`, `Description`, and form control together.

The `Label` component labels a form control.

The `Description` component describes a form control.
