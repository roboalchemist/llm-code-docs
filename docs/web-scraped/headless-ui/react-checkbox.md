# Source: https://headlessui.com/react/checkbox

Title: Headless UI

URL Source: https://headlessui.com/react/checkbox

Published Time: Tue, 10 Mar 2026 03:56:28 GMT

Markdown Content:
Checkbox - Headless UI
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

Checkbox
========

Checkboxes provide the same functionality as native HTML checkboxes, without any of the styling, giving you a clean slate to design them however you'd like.

Preview Code

[](https://headlessui.com/react/checkbox#installation)Installation
------------------------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/checkbox#basic-example)Basic example
--------------------------------------------------------------------

Checkboxes are built using the `Checkbox` component. You can toggle your checkbox by clicking directly on the component, or by pressing the spacebar while it's focused.

Toggling the checkbox calls the `onChange` function with the new `checked` value.

```
import { Checkbox } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Checkbox
      checked={enabled}
      onChange={setEnabled}
      className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
    >
      {/* Checkmark icon */}
      <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
        <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </Checkbox>
  )
}
```

[](https://headlessui.com/react/checkbox#styling)Styling
--------------------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not a checkbox is checked, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/checkbox#using-data-attributes)Using data attributes

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, the `Checkbox` component exposes a `data-checked` attribute, which tells you if the checkbox is currently checked, and a `data-disabled` attribute, which tells you if the checkbox is currently disabled.

```
<!-- Rendered `Checkbox` -->
<span role="checkbox" data-checked data-disabled>
  <!-- ... -->
</span>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Checkbox } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Checkbox
      checked={enabled}
      onChange={setEnabled}
      className="group block size-4 rounded border bg-white data-checked:bg-blue-500 data-disabled:cursor-not-allowed data-disabled:opacity-50 data-checked:data-disabled:bg-gray-500"    >
      <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">        <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </Checkbox>
  )
}
```

See the [component API](https://headlessui.com/react/checkbox#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/checkbox#using-render-props)Using render props

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, the `Checkbox` component exposes a `checked` state, which tells you if the checkbox is currently checked, and a `disabled` state, which tells you if the checkbox is currently disabled.

```
import { Checkbox } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment, useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Checkbox checked={enabled} onChange={setEnabled} as={Fragment}>
      {({ checked, disabled }) => (        <span
          className={clsx(
            'block size-4 rounded border',
            !checked && 'bg-white',            checked && !disabled && 'bg-blue-500',            checked && disabled && 'bg-gray-500',            disabled && 'cursor-not-allowed opacity-50'          )}
        >
          <svg className={clsx('stroke-white', checked ? 'opacity-100' : 'opacity-0')} viewBox="0 0 14 14" fill="none">            <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </span>
      )}    </Checkbox>
  )
}
```

See the [component API](https://headlessui.com/react/checkbox#component-api) for a list of all the available render props.

[](https://headlessui.com/react/checkbox#examples)Examples
----------------------------------------------------------

### [](https://headlessui.com/react/checkbox#adding-a-label)Adding a label

Wrap a `Label` and `Checkbox` with the `Field` component to automatically associate them using a generated ID:

```
import { useState } from 'react'
import { Checkbox, Field, Label } from '@headlessui/react'
function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Field className="flex items-center gap-2">      <Checkbox
        checked={enabled}
        onChange={setEnabled}
        className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
      >
        <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
          <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </Checkbox>
      <Label>Enable beta features</Label>    </Field>  )
}
```

By default, clicking the `Label` will toggle the `Checkbox`, just like labels do for native HTML checkboxes. If you'd like to make the `Label` non-clickable, you can add a `passive` prop to the `Label` component:

`<Label passive>Enable beta features</Label>`
### [](https://headlessui.com/react/checkbox#adding-a-description)Adding a description

Use the `Description` component within a `Field` to automatically associate it with a `Checkbox` using the `aria-describedby` attribute:

```
import { Checkbox, Description, Field, Label } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Field>      <Label>Enable beta features</Label>
      <Description>This will give you early access to new features we're developing.</Description>      <Checkbox
        checked={enabled}
        onChange={setEnabled}
        className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
      >
        <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
          <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </Checkbox>
    </Field>  )
}
```

### [](https://headlessui.com/react/checkbox#disabling-a-checkbox)Disabling a checkbox

Add the `disabled` prop to the `Field` component to disable a `Checkbox` and its associated `Label` and `Description`:

```
import { Checkbox, Description, Field, Label } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Field disabled>      <Label className="data-disabled:opacity-50">Enable beta features</Label>
      <Description className="data-disabled:opacity-50">
        This will give you early access to new features we're developing.
      </Description>
      <Checkbox
        checked={enabled}
        onChange={setEnabled}
        className="group block size-4 rounded border bg-white data-checked:bg-blue-500 data-disabled:cursor-not-allowed data-disabled:opacity-50 data-checked:data-disabled:bg-gray-500"
      >
        <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
          <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </Checkbox>
    </Field>
  )
}
```

You can also disable a checkbox outside of a `Field` by adding the disabled prop directly to the `Checkbox` itself.

### [](https://headlessui.com/react/checkbox#using-with-html-forms)Using with HTML forms

If you add the `name` prop to your `Checkbox`, a hidden `input` element will be rendered and kept in sync with the checkbox state.

```
import { Checkbox } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <form action="/accounts" method="post">
      <Checkbox
        checked={enabled}
        onChange={setEnabled}
        name="terms-of-service"        className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
      >
        <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
          <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </Checkbox>
      <button>Submit</button>
    </form>
  )
}
```

This lets you use a checkbox inside a native HTML `<form>` and make traditional form submissions as if your checkbox was a native HTML form control.

By default, the value will be `on` when the checkbox is checked, and not present when the checkbox is unchecked.

```
<!-- Rendered hidden input -->
<input type="hidden" name="terms-of-service" value="on" />
```

You can customize the value if needed by using the `value` prop:

```
import { Checkbox } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <form action="/accounts" method="post">
      <Checkbox
        checked={enabled}
        onChange={setEnabled}
        name="terms-of-service"
        value="accept"        className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
      >
        <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
          <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </Checkbox>
      <button>Submit</button>
    </form>
  )
}
```

The hidden input will then use your custom value when the checkbox is checked:

```
<!-- Rendered hidden input -->
<input type="hidden" name="terms-of-service" value="accept" />
```

Basic values like strings will be rendered as a single hidden input containing that value, but complex values like objects will be encoded into multiple inputs using a square bracket notation for the names.

### [](https://headlessui.com/react/checkbox#using-as-uncontrolled)Using as uncontrolled

If you omit the `checked` prop, Headless UI will track its state internally for you, allowing you to use it as an [uncontrolled component](https://reactjs.org/docs/uncontrolled-components.html).

When uncontrolled, you can check the `Checkbox` by default using the `defaultChecked` prop.

```
import { Checkbox } from '@headlessui/react'

function Example() {
  return (
    <form action="/accounts" method="post">
      <Checkbox
        defaultChecked={true}        name="terms-of-service"
        className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
      >
        <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
          <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </Checkbox>
      <button>Submit</button>
    </form>
  )
}
```

This can simplify your code when using the checkbox [with HTML forms](https://headlessui.com/react/checkbox#using-with-html-forms) or with form APIs that collect their state using [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instead of tracking it using React state.

Any `onChange` prop you provide will still be called when the component's value changes in case you need to run any side effects, but you won't need to use it to track the component's state yourself.

### [](https://headlessui.com/react/checkbox#adding-transitions)Adding transitions

Because checkboxes are typically always rendered to the DOM (rather than being mounted/unmounted like other components), simple CSS transitions are often enough to animate your checkbox:

```
import { Checkbox } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Checkbox
      checked={enabled}
      onChange={setEnabled}
      className="group block size-4 rounded border bg-white transition data-checked:bg-blue-500"    >
      <svg className="stroke-white opacity-0 transition group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
        <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />      </svg>
    </Checkbox>
  )
}
```

Because they're renderless, Headless UI components also compose well with other animation libraries in the React ecosystem like [Framer Motion](https://www.framer.com/motion/) and [React Spring](https://www.react-spring.io/).

### [](https://headlessui.com/react/checkbox#rendering-as-different-element)Rendering as different element

The `Checkbox` component renders a `span` by default. Use the `as` prop to render the component as a different element or as your own custom component.

```
import { Checkbox } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [enabled, setEnabled] = useState(false)

  return (
    <Checkbox
      as="div"      checked={enabled}
      onChange={setEnabled}
      className="group block size-4 rounded border bg-white data-checked:bg-blue-500"
    >
      <svg className="stroke-white opacity-0 group-data-checked:opacity-100" viewBox="0 0 14 14" fill="none">
        <path d="M3 8L6 11L11 3.5" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </Checkbox>
  )
}
```

[](https://headlessui.com/react/checkbox#keyboard-interaction)Keyboard interaction
----------------------------------------------------------------------------------

Command Description
Space when a `Checkbox` is focused Toggles the Checkbox
Enter when a `Checkbox` is focused Submit the parent form if it exists

[](https://headlessui.com/react/checkbox#component-api)Component API
--------------------------------------------------------------------

### [](https://headlessui.com/react/checkbox#checkbox)Checkbox

Prop Default Description
`as``span``String | Component`

The element or component the checkbox should render as.
`checked`—`Boolean`

Whether or not the checkbox is checked.
`defaultChecked`—`T`

The default checked value when using as an uncontrolled component.
`onChange`—`(value: Boolean) => void`

The function to call when the checkbox is toggled.
`indeterminate`—`Boolean`

Whether or not the checkbox is indeterminate.
`disabled``false``Boolean`

Whether or not the checkbox is disabled.
`autoFocus``false``Boolean`

Whether or not the checkbox should receive focus when first rendered.
`name`—`String`

The name used when using the checkbox inside a form.
`form`—`String`

The id of the form that the checkbox belongs to.

If `name` is provided but `form` is not, the checkbox will add its state to the nearest ancestor `form` element.
`value`—`String`

The value used when using this component inside a form, if it is checked.

Data Attribute Render Prop Description
`data-checked``checked``Boolean`

Whether or not the checkbox is checked.
`data-indeterminate``indeterminate``Boolean`

Whether or not the checkbox is indeterminate.
`data-disabled``disabled``Boolean`

Whether or not the checkbox is disabled.
`data-focus``focus``Boolean`

Whether or not the checkbox is focused.
`data-hover``hover``Boolean`

Whether or not the checkbox is hovered.
`data-active``active``Boolean`

Whether or not the checkbox is in an active or pressed state.
`data-autofocus``autofocus``Boolean`

Whether or not the `autoFocus` prop was set to `true`.
`data-changing``changing``Boolean`

Whether or not the checked state is currently changing.

When the `checked` state changes, `changing` will be `true` for two animation frames, allowing you to fine-tune transitions.

### [](https://headlessui.com/react/checkbox#field)Field

Groups a `Label`, `Description`, and form control together.

Prop Default Description
`as``div``String | Component`

The element or component the field should render as.
`disabled``false``Boolean`

Whether or not the field is disabled.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the field is disabled.

### [](https://headlessui.com/react/checkbox#label)Label

The `Label` component labels a form control.

Prop Default Description
`as``label``String | Component`

The element or component the label should render as.
`passive``false``Boolean`

When true, clicking the label won't focus the associated form control.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the parent `Field` is disabled.

### [](https://headlessui.com/react/checkbox#description)Description

The `Description` component describes a form control.

Prop Default Description
`as``p``String | Component`

The element or component the description should render as.

Data Attribute Render Prop Description
`data-disabled``disabled``Boolean`

Whether or not the parent `Field` is disabled.

[](https://headlessui.com/react/checkbox#styled-examples)Styled examples
------------------------------------------------------------------------

If you're interested in predesigned [Tailwind CSS checkbox component examples](https://tailwindui.com/components/application-ui/forms/checkboxes), check out **Tailwind Plus** — a collection of beautifully designed and expertly crafted components built by us.

It's a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[Explore more predesigned examples →](https://tailwindcss.com/plus)

[![Image 1: Various components from Tailwind UI](https://headlessui.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftailwind-plus.434a3ca6.png&w=3840&q=75)](https://tailwindcss.com/plus)

On this page

*   [Installation](https://headlessui.com/react/checkbox#installation) 
*   [Basic example](https://headlessui.com/react/checkbox#basic-example) 
*   [Styling](https://headlessui.com/react/checkbox#styling)

    *   [Using data attributes](https://headlessui.com/react/checkbox#using-data-attributes) 
    *   [Using render props](https://headlessui.com/react/checkbox#using-render-props) 

*   [Examples](https://headlessui.com/react/checkbox#examples)

    *   [Adding a label](https://headlessui.com/react/checkbox#adding-a-label) 
    *   [Adding a description](https://headlessui.com/react/checkbox#adding-a-description) 
    *   [Disabling a checkbox](https://headlessui.com/react/checkbox#disabling-a-checkbox) 
    *   [Using with HTML forms](https://headlessui.com/react/checkbox#using-with-html-forms) 
    *   [Using as uncontrolled](https://headlessui.com/react/checkbox#using-as-uncontrolled) 
    *   [Adding transitions](https://headlessui.com/react/checkbox#adding-transitions) 
    *   [Rendering as different element](https://headlessui.com/react/checkbox#rendering-as-different-element) 

*   [Keyboard interaction](https://headlessui.com/react/checkbox#keyboard-interaction) 
*   [Component API](https://headlessui.com/react/checkbox#component-api)

    *   [Checkbox](https://headlessui.com/react/checkbox#checkbox) 
    *   [Field](https://headlessui.com/react/checkbox#field) 
    *   [Label](https://headlessui.com/react/checkbox#label) 
    *   [Description](https://headlessui.com/react/checkbox#description) 

*   [Styled examples](https://headlessui.com/react/checkbox#styled-examples) 

© 2025 Tailwind Labs Inc. All rights reserved.
