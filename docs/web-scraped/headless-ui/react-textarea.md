# Source: https://headlessui.com/react/textarea

Title: Headless UI

URL Source: https://headlessui.com/react/textarea

Published Time: Tue, 10 Mar 2026 04:59:19 GMT

Markdown Content:
Textarea - Headless UI
===============

[](https://headlessui.com/)

v2.1

[](https://github.com/tailwindlabs/headlessui)

React

[Vue](https://headlessui.com/v1/vue)

Components
----------

[Dropdown Menu](https://headlessui.com/react/menu)[Disclosure](https://headlessui.com/react/disclosure)[Dialog](https://headlessui.com/react/dialog)[Popover](https://headlessui.com/react/popover)[Tabs](https://headlessui.com/react/tabs)[Transition](https://headlessui.com/react/transition)

### Forms

[Button](https://headlessui.com/react/button)[Checkbox](https://headlessui.com/react/checkbox)[Combobox](https://headlessui.com/react/combobox)[Fieldset](https://headlessui.com/react/fieldset)[Input](https://headlessui.com/react/input)[Listbox](https://headlessui.com/react/listbox)[Radio Group](https://headlessui.com/react/radio-group)[Select](https://headlessui.com/react/select)[Switch](https://headlessui.com/react/switch)[Textarea](https://headlessui.com/react/textarea)

Textarea
========

A light wrapper around the native textarea element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

Preview Code

[](https://headlessui.com/react/textarea#installation)Installation
------------------------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/textarea#basic-example)Basic example
--------------------------------------------------------------------

Textareas are built using the `Textarea` component:

```
import { Textarea } from '@headlessui/react'

function Example() {
  return <Textarea name="description"></Textarea>
}
```

You can pass any props to a `Textarea` that you'd normally pass to the native `textarea` element.

[](https://headlessui.com/react/textarea#styling)Styling
--------------------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not a textarea is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/textarea#using-data-attributes)Using data attributes

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, the `Textarea` component exposes a `data-focus` attribute, which tells you if the textarea is currently focused via the mouse or keyboard, and a `data-hover` attribute, which tells you if the textarea is currently being hovered by the mouse.

```
<!-- Rendered `Textarea` -->
<textarea name="description" data-focus data-hover></textarea>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Textarea } from '@headlessui/react'

function Example() {
  return <Textarea name="description" className="border data-focus:bg-blue-100 data-hover:shadow"></Textarea>}
```

See the [component API](https://headlessui.com/react/textarea#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/textarea#using-render-props)Using render props

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, the `Textarea` component exposes a `focus` state, which tells you if the textarea is currently focused via the mouse or keyboard, and a `hover` state, which tells you if the textarea is currently being hovered by the mouse.

```
import { Textarea } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Textarea name="description" as={Fragment}>
      {({ focus, hover }) => (        <textarea className={clsx('border', focus && 'bg-blue-100', hover && 'shadow')}></textarea>      )}    </Textarea>
  )
}
```

See the [component API](https://headlessui.com/react/textarea#component-api) for a list of all the available render props.

[](https://headlessui.com/react/textarea#examples)Examples
----------------------------------------------------------

### [](https://headlessui.com/react/textarea#adding-a-label)Adding a label

Wrap a `Label` and `Textarea` with the `Field` component to automatically associate them using a generated ID:

```
import { Field, Label, Textarea } from '@headlessui/react'

function Example() {
  return (
    <Field>      <Label>Description</Label>      <Textarea name="description"></Textarea>
    </Field>  )
}
```

### [](https://headlessui.com/react/textarea#adding-a-description)Adding a description

Use the `Description` component within a `Field` to automatically associate it with a `Textarea` using the `aria-describedby` attribute:

```
import { Description, Field, Label, Textarea } from '@headlessui/react'

function Example() {
  return (
    <Field>      <Label>Description</Label>
      <Description>Add any extra information about your event here.</Description>      <Textarea name="description"></Textarea>
    </Field>  )
}
```

### [](https://headlessui.com/react/textarea#disabling-a-textarea)Disabling a textarea

Add the `disabled` prop to the `Field` component to disable a `Textarea` and its associated `Label` and `Description`:

```
import { Description, Field, Label, Textarea } from '@headlessui/react'

function Example() {
  return (
    <Field disabled>      <Label className="data-disabled:opacity-50">Name</Label>
      <Description className="data-disabled:opacity-50">Add any extra information about your event here.</Description>
      <Textarea name="description" className="data-disabled:bg-gray-100"></Textarea>
    </Field>
  )
}
```

You can also disable a textarea outside of a `Field` by adding the disabled prop directly to the `Textarea` itself.

[](https://headlessui.com/react/textarea#component-api)Component API
--------------------------------------------------------------------

### [](https://headlessui.com/react/textarea#textarea)Textarea

A thin wrapper around the native `textarea` element.

Prop Default Description
`as``textarea``String | Component`

The element or component the textarea should render as.
`invalid``false``Boolean`

Whether or not the textarea is invalid.
`disabled``false``Boolean`

Whether or not the textarea is disabled.
`autoFocus``false``Boolean`

Whether or not the textarea should receive focus when first rendered.

Data Attribute Render Prop Description
`data-invalid``invalid``Boolean`

Whether or not the textarea is invalid.
`data-disabled``disabled``Boolean`

Whether or not the textarea is disabled.
`data-focus``focus``Boolean`

Whether or not the textarea is focused.
`data-hover``hover``Boolean`

Whether or not the textarea is hovered.
`data-autofocus``autofocus``Boolean`

Whether or not the `autoFocus` prop was set to `true`.

### [](https://headlessui.com/react/textarea#field)Field

Groups a `Label`, `Description`, and form control together.

Prop Default Description
`as``div``String | Component`

The element or component the field should render as.
`disabled``false``Boolean`

Whether or not the field is disabled.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the field is disabled.

### [](https://headlessui.com/react/textarea#label)Label

The `Label` component labels a form control.

Prop Default Description
`as``label``String | Component`

The element or component the label should render as.
`passive``false``Boolean`

When true, clicking the label won't focus the associated form control.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the parent `Field` is disabled.

### [](https://headlessui.com/react/textarea#description)Description

The `Description` component describes a form control.

Prop Default Description
`as``p``String | Component`

The element or component the description should render as.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the parent `Field` is disabled.

[](https://headlessui.com/react/textarea#styled-examples)Styled examples
------------------------------------------------------------------------

If you're interested in predesigned [Tailwind CSS textarea examples](https://tailwindui.com/components/application-ui/forms/textareas), check out **Tailwind Plus** — a collection of beautifully designed and expertly crafted components built by us.

It's a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[Explore more predesigned examples →](https://tailwindcss.com/plus)

[![Image 1: Various components from Tailwind UI](https://headlessui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftailwind-plus.434a3ca6.png&w=3840&q=75)](https://tailwindcss.com/plus)

On this page

*   [Installation](https://headlessui.com/react/textarea#installation) 
*   [Basic example](https://headlessui.com/react/textarea#basic-example) 
*   [Styling](https://headlessui.com/react/textarea#styling)

    *   [Using data attributes](https://headlessui.com/react/textarea#using-data-attributes) 
    *   [Using render props](https://headlessui.com/react/textarea#using-render-props) 

*   [Examples](https://headlessui.com/react/textarea#examples)

    *   [Adding a label](https://headlessui.com/react/textarea#adding-a-label) 
    *   [Adding a description](https://headlessui.com/react/textarea#adding-a-description) 
    *   [Disabling a textarea](https://headlessui.com/react/textarea#disabling-a-textarea) 

*   [Component API](https://headlessui.com/react/textarea#component-api)

    *   [Textarea](https://headlessui.com/react/textarea#textarea) 
    *   [Field](https://headlessui.com/react/textarea#field) 
    *   [Label](https://headlessui.com/react/textarea#label) 
    *   [Description](https://headlessui.com/react/textarea#description) 

*   [Styled examples](https://headlessui.com/react/textarea#styled-examples) 

© 2025 Tailwind Labs Inc. All rights reserved.
