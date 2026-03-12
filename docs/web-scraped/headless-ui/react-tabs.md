# Source: https://headlessui.com/react/tabs

Title: Headless UI

URL Source: https://headlessui.com/react/tabs

Markdown Content:
Easily create accessible, fully customizable tab interfaces, with robust focus management and keyboard navigation support.

[](https://headlessui.com/react/tabs#installation)
--------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/tabs#basic-example)
---------------------------------------------------

Tabs are built using the `TabGroup`, `TabList`, `Tab`, `TabPanels`, and `TabPanel` components. By default the first tab is selected, and clicking on any tab or selecting it with the keyboard will activate the corresponding panel.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup>
      <TabList>
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

[](https://headlessui.com/react/tabs#styling)
---------------------------------------------

Headless UI keeps track of a lot of state about each component, like which tab is currently selected, whether a popover is open or closed, or which item in a menu is currently focused via the keyboard.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/tabs#using-data-attributes)

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, the `Tab` component exposes a `data-selected` attribute, which tells you if the tab is currently selected, and a `data-hover` attribute, which tells you if the tab is currently being hovered by the mouse.

```
<!-- Rendered `TabGroup` -->
<div>
  <div>
    <button>Tab 1</button>
    <button data-selected>Tab 2</button>
    <button data-hover>Tab 3</button>
  </div>
  <div>
    <div>Content 1</div>
    <div data-selected>Content 2</div>
    <div>Content 3</div>
  </div>
</div>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup>
      <TabList>
        <Tab className="data-hover:underline data-selected:bg-blue-500 data-selected:text-white">Tab 1</Tab>        <Tab className="data-hover:underline data-selected:bg-blue-500 data-selected:text-white">Tab 2</Tab>        <Tab className="data-hover:underline data-selected:bg-blue-500 data-selected:text-white">Tab 3</Tab>      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

See the [component API](https://headlessui.com/react/tabs#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/tabs#using-render-props)

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, the `Tab` component exposes a `selected` state, which tells you if the tab is currently selected, and a `hover` state, which tells you if the tab is currently being hovered by the mouse.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

function Example() {
  return (
    <TabGroup>
      <TabList>
        <Tab as={Fragment}>
          {({ hover, selected }) => (            <button className={clsx(hover && 'underline', selected && 'bg-blue-500 text-white')}>Tab 1</button>          )}        </Tab>
        <Tab as={Fragment}>
          {({ hover, selected }) => (            <button className={clsx(hover && 'underline', selected && 'bg-blue-500 text-white')}>Tab 2</button>          )}        </Tab>
        <Tab as={Fragment}>
          {({ hover, selected }) => (            <button className={clsx(hover && 'underline', selected && 'bg-blue-500 text-white')}>Tab 3</button>          )}        </Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

See the [component API](https://headlessui.com/react/tabs#component-api) for a list of all the available render props.

[](https://headlessui.com/react/tabs#examples)
----------------------------------------------

### [](https://headlessui.com/react/tabs#disabling-a-tab)

Use the `disabled` prop to disable a `Tab` and prevent it from being selected:

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup>
      <TabList>
        <Tab>Tab 1</Tab>
        <Tab disabled className="disabled:opacity-50">          Tab 2
        </Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

### [](https://headlessui.com/react/tabs#displaying-tabs-vertically)

If you've styled your `TabList` to appear vertically, use the `vertical` prop to enable navigating with the up and down arrow keys instead of left and right, and to update the `aria-orientation` attribute for assistive technologies.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup vertical>      <TabList className="flex flex-col">
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

### [](https://headlessui.com/react/tabs#manually-activating-tabs)

By default, tabs are automatically selected as the user navigates through them using the arrow keys.

If you'd rather not change the current tab until the user presses `Enter` or `Space`, use the `manual` prop on the `TabGroup` component. This can be helpful if selecting a tab performs an expensive operation and you don't want to run it unnecessarily.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup manual>      <TabList>
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

The `manual` prop has no impact on mouse interactions — tabs will still be selected as soon as they are clicked.

### [](https://headlessui.com/react/tabs#specifying-the-default-tab)

To change which tab is selected by default, use the `defaultIndex={number}` prop on the `TabGroup` component.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup defaultIndex={1}>      <TabList>
        <Tab>Tab 1</Tab>

        {/* Selects this tab by default */}        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>

        {/* Displays this panel by default */}        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

If you happen to provide an index that is out of bounds, then the last non-disabled tab will be selected on initial render. (For example, `<TabGroup defaultIndex={5}>` in the example above would render the third panel as selected.)

### [](https://headlessui.com/react/tabs#listening-for-changes)

To run a function whenever the selected tab changes, use the `onChange` prop on the `TabGroup` component.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'

function Example() {
  return (
    <TabGroup
      onChange={(index) => {        console.log('Changed selected tab to:', index)      }}    >
      <TabList>
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

### [](https://headlessui.com/react/tabs#controlling-the-selected-tab)

By default, the tabs component manages the selected tab internally. However, you can control the selected tab yourself using the `selectedIndex` prop and `onChange` callback:

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [selectedIndex, setSelectedIndex] = useState(0)
  return (
    <TabGroup selectedIndex={selectedIndex} onChange={setSelectedIndex}>      <TabList>
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

### [](https://headlessui.com/react/tabs#rendering-as-different-elements)

By default, the `TabGroup` and its subcomponents each render a default element that is sensible for that component.

For example, `TabGroup` renders a `div`, `TabList` renders a `div`, and `Tab` renders a `button`.

Use the `as` prop to render the component as a different element or as your own custom component, making sure your custom components [forward refs](https://react.dev/reference/react/forwardRef) so that Headless UI can wire things up correctly.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'
import { forwardRef } from 'react'

let MyCustomButton = forwardRef(function (props, ref) {  return <button className="..." ref={ref} {...props} />})
function Example() {
  return (
    <TabGroup>
      <TabList as="aside">        <Tab as={MyCustomButton}>Tab 1</Tab>
        <Tab as={MyCustomButton}>Tab 2</Tab>
        <Tab as={MyCustomButton}>Tab 3</Tab>
      </TabList>
      <TabPanels as="section">        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

To tell an element to render its children directly with no wrapper element, use a `Fragment`.

```
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/react'
import { Fragment } from 'react'

function Example() {
  return (
    <TabGroup as={Fragment}>      <TabList>
        <Tab>Tab 1</Tab>
        <Tab>Tab 2</Tab>
        <Tab>Tab 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Content 1</TabPanel>
        <TabPanel>Content 2</TabPanel>
        <TabPanel>Content 3</TabPanel>
      </TabPanels>
    </TabGroup>
  )
}
```

[](https://headlessui.com/react/tabs#keyboard-interaction)
----------------------------------------------------------

All interactions apply when a `Tab` component is focused.

[](https://headlessui.com/react/tabs#component-api)
---------------------------------------------------

### [](https://headlessui.com/react/tabs#tab-group)

The main TabGroup component.
