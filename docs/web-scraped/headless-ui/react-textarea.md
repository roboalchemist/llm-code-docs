# Source: https://headlessui.com/react/textarea

Title: Headless UI

URL Source: https://headlessui.com/react/textarea

Markdown Content:
A light wrapper around the native textarea element that handles tedious accessibility concerns and provides more opinionated states for things like hover and focus.

[](https://headlessui.com/react/textarea#installation)
------------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/textarea#basic-example)
-------------------------------------------------------

Textareas are built using the `Textarea` component:

```
import { Textarea } from '@headlessui/react'

function Example() {
  return <Textarea name="description"></Textarea>
}
```

You can pass any props to a `Textarea` that you'd normally pass to the native `textarea` element.

[](https://headlessui.com/react/textarea#styling)
-------------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not a textarea is focused, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/textarea#using-data-attributes)

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

### [](https://headlessui.com/react/textarea#using-render-props)

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

[](https://headlessui.com/react/textarea#examples)
--------------------------------------------------

### [](https://headlessui.com/react/textarea#adding-a-label)

Wrap a `Label` and `Textarea` with the `Field` component to automatically associate them using a generated ID:

```
import { Field, Label, Textarea } from '@headlessui/react'

function Example() {
  return (
    <Field>      <Label>Description</Label>      <Textarea name="description"></Textarea>
    </Field>  )
}
```

### [](https://headlessui.com/react/textarea#adding-a-description)

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

### [](https://headlessui.com/react/textarea#disabling-a-textarea)

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

[](https://headlessui.com/react/textarea#component-api)
-------------------------------------------------------

### [](https://headlessui.com/react/textarea#textarea)

A thin wrapper around the native `textarea` element.

Groups a `Label`, `Description`, and form control together.

The `Label` component labels a form control.

The `Description` component describes a form control.
