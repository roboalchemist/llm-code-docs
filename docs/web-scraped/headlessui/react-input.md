# Source: https://headlessui.com/react/input

React
[Vue](/v1/vue)

# Input

A light wrapper around the native input element that handles tedious accessibility concerns and provides more
opinionated states for things like hover and focus.

PreviewCode

## [](#installation)Installation

To get started, install Headless UI via npm:

```
npm install @headlessui/react
```

## [](#basic-example)Basic example

Inputs are built using the `Input` component:

```
import { Input } from '@headlessui/react'

function Example() {
  return <Input name="full_name" type="text" />
}
```

You can pass any props to an `Input` that you&#x27;d normally pass to the native `input` element.

## [](#styling)Styling

Headless UI keeps track of a lot of state about each component, like whether or not an input is focused, whether a
popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t see this information in your
UI until you provide the styles you want for each state yourself.

### [](#using-data-attributes)Using data attributes

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each
component exposes.

For example, the `Input` component exposes a `data-focus` attribute, which tells you if the input is currently focused
via the mouse or keyboard, and a `data-hover` attribute, which tells you if the input is currently being hovered by the
mouse.

```
<!-- Rendered `Input` -->
<input type="text" name="full_name" data-focus data-hover />
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally
apply styles based on the presence of these data attributes. If you&#x27;re using Tailwind CSS, the
[data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Input } from '@headlessui/react'

function Example() {

  return <Input type="text" name="full_name" className="border data-focus:bg-blue-100 data-hover:shadow" />
}

```

See the [component API](#component-api) for a list of all the available data attributes.

### [](#using-render-props)Using render props

Each component also exposes information about its current state via
[render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or
render different content.

For example, the `Input` component exposes a `focus` state, which tells you if the input is currently focused via the
mouse or keyboard, and a `hover` state, which tells you if the input is currently being hovered by the mouse.

```
import { Input } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Input type="text" name="full_name" as={Fragment}>

      {({ focus, hover }) => <input className={clsx('border', focus && 'bg-blue-100', hover && 'shadow')} />}
    </Input>
  )
}

```

See the [component API](#component-api) for a list of all the available render props.

## [](#examples)Examples

### [](#adding-a-label)Adding a label

Wrap a `Label` and `Input` with the `Field` component to automatically associate them using a generated ID:

```
import { Field, Input, Label } from '@headlessui/react'

function Example() {
  return (

    <Field>

      <Label>Name</Label>
      <Input name="full_name" />

    </Field>
  )
}

```

### [](#adding-a-description)Adding a description

Use the `Description` component within a `Field` to automatically associate it with an `Input` using the
`aria-describedby` attribute:

```
import { Description, Field, Input, Label } from '@headlessui/react'

function Example() {
  return (

    <Field>
      <Label>Name</Label>

      <Description>Use your real name so people will recognize you.</Description>
      <Input name="full_name" />

    </Field>
  )
}

```

### [](#disabling-an-input)Disabling an input

Add the `disabled` prop to the `Field` component to disable an `Input` and its associated `Label` and `Description`:

```
import { Description, Field, Input, Label } from '@headlessui/react'

function Example() {
  return (

    <Field disabled>
      <Label className="data-disabled:opacity-50">Name</Label>
      <Description className="data-disabled:opacity-50">Use your real name so people will recognize you.</Description>
      <Input name="full_name" className="data-disabled:bg-gray-100" />
    </Field>
  )
}

```

You can also disable an input outside of a `Field` by adding the disabled prop directly to the `Input` itself.

## [](#component-api)Component API

### [](#input)Input

A thin wrapper around the native `input` element.

PropDefaultDescription`as``input`
`String | Component`

The element or component the input should render as.

`invalid``false`
`Boolean`

Whether or not the input is invalid.

`disabled``false`
`Boolean`

Whether or not the input is disabled.

`autoFocus``false`
`Boolean`

Whether or not the input should receive focus when first rendered.

Data AttributeRender PropDescription`data-invalid``invalid`
`Boolean`

Whether or not the input is invalid.

`data-disabled``disabled`
`Boolean`

Whether or not the input is disabled.

`data-focus``focus`
`Boolean`

Whether or not the input is focused.

`data-hover``hover`
`Boolean`

Whether or not the input is hovered.

`data-autofocus``autofocus`
`Boolean`

Whether or not the `autoFocus` prop was set to `true`.

### [](#field)Field

Groups a `Label`, `Description`, and form control together.

PropDefaultDescription`as``div`
`String | Component`

The element or component the field should render as.

`disabled``false`
`Boolean`

Whether or not the field is disabled.

Data AttributeRender PropDescription`data-disabled``disabled`
`Boolean`

Whether or not the field is disabled.

### [](#label)Label

The `Label` component labels a form control.

PropDefaultDescription`as``label`
`String | Component`

The element or component the label should render as.

`passive``false`
`Boolean`

When true, clicking the label won&#x27;t focus the associated form control.

Data AttributeRender PropDescription`data-disabled``disabled`
`Boolean`

Whether or not the parent `Field` is disabled.

### [](#description)Description

The `Description` component describes a form control.

PropDefaultDescription`as``p`
`String | Component`

The element or component the description should render as.

Data AttributeRender PropDescription`data-disabled``disabled`
`Boolean`

Whether or not the parent `Field` is disabled.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned [Tailwind CSS form input group examples](https://tailwindui.com/components/application-ui/forms/input-groups), check out **Tailwind Plus** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[Explore more predesigned examples →](https://tailwindcss.com/plus)
[](https://tailwindcss.com/plus)