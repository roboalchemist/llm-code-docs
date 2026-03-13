# Source: https://headlessui.com/react/select

Title: Headless UI

URL Source: https://headlessui.com/react/select

Published Time: Thu, 05 Mar 2026 11:24:56 GMT

Markdown Content:
Select - Headless UI
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

Select
======

A light wrapper around the native select element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

Preview Code

[](https://headlessui.com/react/select#installation)Installation
----------------------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/select#basic-example)Basic example
------------------------------------------------------------------

Select controls are built using the `Select` component:

```
import { Select } from '@headlessui/react'

function Example() {
  return (
    <Select name="status" aria-label="Project status">
      <option value="active">Active</option>
      <option value="paused">Paused</option>
      <option value="delayed">Delayed</option>
      <option value="canceled">Canceled</option>
    </Select>
  )
}
```

You can pass any props to a `Select` that you'd normally pass to the native `select` element.

[](https://headlessui.com/react/select#styling)Styling
------------------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not a select is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/select#using-data-attributes)Using data attributes

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, the `Select` component exposes a `data-focus` attribute, which tells you if the select is currently focused via keyboard, and a `data-hover` attribute, which tells you if the select is currently being hovered by the mouse.

```
<!-- Rendered `Select` -->
<select name="status" data-focus data-hover>
  <option value="active">Active</option>
  <option value="paused">Paused</option>
  <option value="delayed">Delayed</option>
  <option value="canceled">Canceled</option>
</select>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Select } from '@headlessui/react'

function Example() {
  return (
    <Select name="status" className="border data-focus:bg-blue-100 data-hover:shadow" aria-label="Project status">      <option value="active">Active</option>
      <option value="paused">Paused</option>
      <option value="delayed">Delayed</option>
      <option value="canceled">Canceled</option>
    </Select>
  )
}
```

See the [component API](https://headlessui.com/react/select#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/select#using-render-props)Using render props

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, the `Select` component exposes a `focus` state, which tells you if the select is currently focused via the keyboard, and a `hover` state, which tells you if the select is currently being hovered by the mouse.

```
import { Select } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Select name="status" as={Fragment}>
      {({ focus, hover }) => (        <select className={clsx('border', focus && 'bg-blue-100', hover && 'shadow')} aria-label="Project status">          <option value="active">Active</option>
          <option value="paused">Paused</option>
          <option value="delayed">Delayed</option>
          <option value="canceled">Canceled</option>
        </select>
      )}    </Select>
  )
}
```

See the [component API](https://headlessui.com/react/select#component-api) for a list of all the available render props.

[](https://headlessui.com/react/select#examples)Examples
--------------------------------------------------------

### [](https://headlessui.com/react/select#adding-a-label)Adding a label

Wrap a `Label` and `Select` with the `Field` component to automatically associate them using a generated ID:

```
import { Field, Label, Select } from '@headlessui/react'

function Example() {
  return (
    <Field>      <Label>Project status</Label>      <Select name="status">
        <option value="active">Active</option>
        <option value="paused">Paused</option>
        <option value="delayed">Delayed</option>
        <option value="canceled">Canceled</option>
      </Select>
    </Field>  )
}
```

### [](https://headlessui.com/react/select#adding-a-description)Adding a description

Use the `Description` component within a `Field` to automatically associate it with a `Select` using the `aria-describedby` attribute:

```
import { Description, Field, Label, Select } from '@headlessui/react'

function Example() {
  return (
    <Field>      <Label>Project status</Label>
      <Description>This will be visible to clients on the project.</Description>      <Select name="status">
        <option value="active">Active</option>
        <option value="paused">Paused</option>
        <option value="delayed">Delayed</option>
        <option value="canceled">Canceled</option>
      </Select>
    </Field>  )
}
```

### [](https://headlessui.com/react/select#disabling-a-select)Disabling a select

Add the `disabled` prop to the `Field` component to disable a `Select` and its associated `Label` and `Description`:

```
import { Description, Field, Label, Select } from '@headlessui/react'

function Example() {
  return (
    <Field disabled>      <Label className="data-disabled:opacity-50">Project status</Label>      <Description className="data-disabled:opacity-50">This will be visible to clients on the project.</Description>      <Select name="status" className="data-disabled:bg-gray-100">        <option value="active">Active</option>
        <option value="paused">Paused</option>
        <option value="delayed">Delayed</option>
        <option value="canceled">Canceled</option>
      </Select>
    </Field>
  )
}
```

You can also disable a select outside of a `Field` by adding the disabled prop directly to the `Select` itself.

[](https://headlessui.com/react/select#component-api)Component API
------------------------------------------------------------------

### [](https://headlessui.com/react/select#select)Select

A thin wrapper around the native `select` element.

Prop Default Description
`as``select``String | Component`

The element or component the select should render as.
`invalid``false``Boolean`

Whether or not the select is invalid.
`disabled``false``Boolean`

Whether or not the select is disabled.
`autoFocus``false``Boolean`

Whether or not the select should receive focus when first rendered.

Data Attribute Render Prop Description
`data-invalid``invalid``Boolean`

Whether or not the select is invalid.
`data-disabled``disabled``Boolean`

Whether or not the select is disabled.
`data-focus``focus``Boolean`

Whether or not the select is focused.
`data-hover``hover``Boolean`

Whether or not the select is hovered.
`data-active``active``Boolean`

Whether or not the select is in an active or pressed state.
`data-autofocus``autofocus``Boolean`

Whether or not the `autoFocus` prop was set to `true`.

### [](https://headlessui.com/react/select#field)Field

Groups a `Label`, `Description`, and form control together.

Prop Default Description
`as``div``String | Component`

The element or component the field should render as.
`disabled``false``Boolean`

Whether or not the field is disabled.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the field is disabled.

### [](https://headlessui.com/react/select#label)Label

The `Label` component labels a form control.

Prop Default Description
`as``label``String | Component`

The element or component the label should render as.
`passive``false``Boolean`

When true, clicking the label won't focus the associated form control.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the parent `Field` is disabled.

### [](https://headlessui.com/react/select#description)Description

The `Description` component describes a form control.

Prop Default Description
`as``p``String | Component`

The element or component the description should render as.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the parent `Field` is disabled.

[](https://headlessui.com/react/select#styled-examples)Styled examples
----------------------------------------------------------------------

If you're interested in predesigned [Tailwind CSS select menu examples](https://tailwindui.com/components/application-ui/forms/select-menus), check out **Tailwind Plus** — a collection of beautifully designed and expertly crafted components built by us.

It's a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[Explore more predesigned examples →](https://tailwindcss.com/plus)

[![Image 1: Various components from Tailwind UI](https://headlessui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftailwind-plus.434a3ca6.png&w=3840&q=75)](https://tailwindcss.com/plus)

On this page

*   [Installation](https://headlessui.com/react/select#installation) 
*   [Basic example](https://headlessui.com/react/select#basic-example) 
*   [Styling](https://headlessui.com/react/select#styling)

    *   [Using data attributes](https://headlessui.com/react/select#using-data-attributes) 
    *   [Using render props](https://headlessui.com/react/select#using-render-props) 

*   [Examples](https://headlessui.com/react/select#examples)

    *   [Adding a label](https://headlessui.com/react/select#adding-a-label) 
    *   [Adding a description](https://headlessui.com/react/select#adding-a-description) 
    *   [Disabling a select](https://headlessui.com/react/select#disabling-a-select) 

*   [Component API](https://headlessui.com/react/select#component-api)

    *   [Select](https://headlessui.com/react/select#select) 
    *   [Field](https://headlessui.com/react/select#field) 
    *   [Label](https://headlessui.com/react/select#label) 
    *   [Description](https://headlessui.com/react/select#description) 

*   [Styled examples](https://headlessui.com/react/select#styled-examples) 

© 2025 Tailwind Labs Inc. All rights reserved.
