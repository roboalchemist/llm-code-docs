# Source: https://headlessui.com/react/fieldset

Title: Headless UI

URL Source: https://headlessui.com/react/fieldset

Markdown Content:
Group a set of form controls together with these fully accessible but much easier-to-style versions of the native fieldset and legend elements.

[](https://headlessui.com/react/fieldset#installation)
------------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/fieldset#basic-example)
-------------------------------------------------------

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

Since the native HTML `<legend>` element is difficult to style, the `Legend` component is rendered as a `<div>`. The `<Fieldset>` component uses the native `<fieldset>` component.

[](https://headlessui.com/react/fieldset#styling)
-------------------------------------------------

Headless UI keeps track of a lot of state about each component, like whether or not a fieldset is disabled, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/fieldset#using-data-attributes)

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, both the `Fieldset` and `Legend` components expose a `data-disabled` attribute, which tells you if the fieldset is currently disabled.

```
<!-- Rendered `Fieldset` and `Legend` -->
<fieldset aria-labelledby="..." disabled data-disabled>
  <div id="..." data-disabled>Shipping details</div>
  <!-- ... -->
</fieldset>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Fieldset, Legend } from '@headlessui/react'

function Example() {
  return (
    <Fieldset disabled className="space-y-8 data-disabled:opacity-50">      <Legend className="text-lg font-bold">Shipping details</Legend>
      {/* ... */}
    </Fieldset>
  )
}
```

See the [component API](https://headlessui.com/react/fieldset#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/fieldset#using-render-props)

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, both the `Fieldset` and `Legend` components expose a `disabled` state, which tells you if the fieldset is currently disabled.

```
import { Fieldset, Legend } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <Fieldset disabled as={Fragment}>
      {({ disabled }) => (        <div className={clsx('space-y-8', disabled && 'opacity-50')}>          <Legend className="text-lg font-bold">Shipping details</Legend>
          {/* ... */}
        </div>
      )}    </Fieldset>
  )
}
```

See the [component API](https://headlessui.com/react/fieldset#component-api) for a list of all the available render props.

[](https://headlessui.com/react/fieldset#examples)
--------------------------------------------------

### [](https://headlessui.com/react/fieldset#disabling-a-fieldset)

Add the `disabled` prop to a `Fieldset` component to disable the entire fieldset:

```
import { Fieldset, Legend } from '@headlessui/react'

function Example() {
  return (
    <Fieldset disabled>      <Legend>Shipping details</Legend>
      {/* ... */}
    </Fieldset>
  )
}
```

[](https://headlessui.com/react/fieldset#component-api)
-------------------------------------------------------

### [](https://headlessui.com/react/fieldset#fieldset)

Group a set of form controls together with a title.

### [](https://headlessui.com/react/fieldset#legend)

The title for a `Fieldset`.
