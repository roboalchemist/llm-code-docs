# Source: https://headlessui.com/react/select

Title: Headless UI

URL Source: https://headlessui.com/react/select

Markdown Content:
A light wrapper around the native select element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

[](https://headlessui.com/react/select#installation)
----------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/select#basic-example)
-----------------------------------------------------

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

[](https://headlessui.com/react/select#styling)
-----------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not a select is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/select#using-data-attributes)

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

### [](https://headlessui.com/react/select#using-render-props)

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

[](https://headlessui.com/react/select#examples)
------------------------------------------------

### [](https://headlessui.com/react/select#adding-a-label)

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

### [](https://headlessui.com/react/select#adding-a-description)

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

### [](https://headlessui.com/react/select#disabling-a-select)

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

[](https://headlessui.com/react/select#component-api)
-----------------------------------------------------

### [](https://headlessui.com/react/select#select)

A thin wrapper around the native `select` element.

Groups a `Label`, `Description`, and form control together.

The `Label` component labels a form control.

The `Description` component describes a form control.
