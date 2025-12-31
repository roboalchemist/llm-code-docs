# Source: https://headlessui.com/react/fieldset

React
[Vue](/v1/vue)

# Fieldset

Group a set of form controls together with these fully accessible but much easier-to-style versions of the native
fieldset and legend elements.

PreviewCode

## [](#installation)Installation

To get started, install Headless UI via npm:

```
npm install @headlessui/react
```

## [](#basic-example)Basic example

Use the `Fieldset` and `Legend` components to group a set of form controls together with a title:

```
import { Field, Fieldset, Input, Label, Legend, Select, Textarea } from '@headlessui/react'

function Example() {
  return (
    <Fieldset className="space-y-8">
      <Legend className="text-lg font-bold">Shipping details</Legend>
      <Field>
        <Label className="block">Street address</Label>
        <Input className="mt-1 block" name="address" />
      </Field>
      <Field>
        <Label className="block">Country</Label>
        <Select className="mt-1 block" name="country">
          <option>Canada</option>
          <option>Mexico</option>
          <option>United States</option>
        </Select>
      </Field>
      <Field>
        <Label className="block">Delivery notes</Label>
        <Textarea className="mt-1 block" name="notes" />
      </Field>
    </Fieldset>
  )
}
```

Since the native HTML `<legend>` element is difficult to style, the `Legend` component is rendered as a `<div>`. The
`<Fieldset>` component uses the native `<fieldset>` component.

## [](#styling)Styling

Headless UI keeps track of a lot of state about each component, like whether or not a fieldset is disabled, whether a
popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t see this information in your
UI until you provide the styles you want for each state yourself.

### [](#using-data-attributes)Using data attributes

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each
component exposes.

For example, both the `Fieldset` and `Legend` components expose a `data-disabled` attribute, which tells you if the
fieldset is currently disabled.

```
<!-- Rendered `Fieldset` and `Legend` -->
<fieldset aria-labelledby="..." disabled data-disabled>
  <div id="..." data-disabled>Shipping details</div>
  <!-- ... -->
</fieldset>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally
apply styles based on the presence of these data attributes. If you&#x27;re using Tailwind CSS, the
[data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Fieldset, Legend } from '@headlessui/react'

function Example() {
  return (

    <Fieldset disabled className="space-y-8 data-disabled:opacity-50">
      <Legend className="text-lg font-bold">Shipping details</Legend>
      {/* ... */}
    </Fieldset>
  )
}

```

See the [component API](#component-api) for a list of all the available data attributes.

### [](#using-render-props)Using render props

Each component also exposes information about its current state via
[render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or
render different content.

For example, both the `Fieldset` and `Legend` components expose a `disabled` state, which tells you if the fieldset is
currently disabled.

```
import { Fieldset, Legend } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Fieldset disabled as={Fragment}>

      {({ disabled }) => (

        <div className={clsx('space-y-8', disabled && 'opacity-50')}>
          <Legend className="text-lg font-bold">Shipping details</Legend>
          {/* ... */}
        </div>

      )}
    </Fieldset>
  )
}

```

See the [component API](#component-api) for a list of all the available render props.

## [](#examples)Examples

### [](#disabling-a-fieldset)Disabling a fieldset

Add the `disabled` prop to a `Fieldset` component to disable the entire fieldset:

```
import { Fieldset, Legend } from '@headlessui/react'

function Example() {
  return (

    <Fieldset disabled>
      <Legend>Shipping details</Legend>
      {/* ... */}
    </Fieldset>
  )
}

```

## [](#component-api)Component API

### [](#fieldset)Fieldset

Group a set of form controls together with a title.

PropDefaultDescription`as``fieldset`
`String | Component`

The element or component the fieldset should render as.

`disabled``false`
`Boolean`

Use this to disable all form controls in the fieldset.

Data AttributeRender PropDescription`data-disabled``disabled`
`Boolean`

Whether or not the fieldset is disabled.

### [](#legend)Legend

The title for a `Fieldset`.

PropDefaultDescription`as``div`
`String | Component`

The element or component the legend should render as.

Data AttributeRender PropDescription`data-disabled``disabled`
`Boolean`

Whether or not the legend is disabled.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned [Tailwind CSS form layout examples](https://tailwindui.com/components/application-ui/forms/form-layouts), check out **Tailwind Plus** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[Explore more predesigned examples →](https://tailwindcss.com/plus)
[](https://tailwindcss.com/plus)