# Source: https://headlessui.com/v1/vue/tabs

# Tabs

Easily create accessible, fully customizable tab interfaces, with robust focus
management and keyboard navigation support.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm:

`npm install @headlessui/vue`

## [](#basic-example)Basic example
Tabs are built using the `TabGroup`, `TabList`, `Tab`, `TabPanels`, and `TabPanel` components. By default the first tab is selected, and clicking on any tab or selecting it with the keyboard will activate the corresponding panel.

`<template>
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
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>`

## [](#styling-different-states)Styling different states
Headless UI keeps track of a lot of state about each component, like which tab option is currently checked, whether a popover is open or closed, or which item in a menu is currently active via the keyboard.

But because the components are headless and completely unstyled out of the box, you can&#x27;t *see* this information in your UI until you provide the styles you want for each state yourself.

### [](#using-slots)Using slots

Each component exposes information about its current state via [slot props](https://vuejs.org/api/built-in-directives.html#v-slot) that you can use to conditionally apply different styles or render different content.

For example, the `Tab` component exposes a `selected` state, which tells you if the tab is currently selected.

`<template>
  <TabGroup>
    <TabList>
      <!-- Use the `selected` state to conditionally style the selected tab. -->

      <Tab as="template" v-slot="{ selected }">
        <button

          :class="{ 'bg-blue-500 text-white': selected, 'bg-white text-black': !selected }"
        >
          Tab 1
        </button>
      </Tab>
      <!-- ... -->
    </TabList>
    <TabPanels>
      <TabPanel>Content 1</TabPanel>
      <!-- ... -->
    </TabPanels>
  </TabGroup>
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>
`

For the complete slot props API for each component, see the [component API documentation](#component-api).

### [](#using-data-attributes)Using data attributes

Each component also exposes information about its current state via a `data-headlessui-state` attribute that you can use to conditionally apply different styles.

When any of the states in the [slot props API](#component-api) are `true`, they will be listed in this attribute as space-separated strings so you can target them with a [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) in the form `[attr~=value]`.

For example, here&#x27;s what the `TabGroup` component with some child `Tab` components renders when the second tab is `selected`:

`<!-- Rendered `TabGroup` -->
<div>
  <button data-headlessui-state="">Tab 1</button>
  <button data-headlessui-state="selected">Tab 2</button>
  <button data-headlessui-state="">Tab 3</button>
</div>
<div>
  <div data-headlessui-state="">Content 1</div>
  <div data-headlessui-state="selected">Content 2</div>
  <div data-headlessui-state="">Content 3</div>
</div>`

If you are using [Tailwind CSS](https://tailwindcss.com/), you can use the [@headlessui/tailwindcss](https://github.com/tailwindlabs/headlessui/tree/main/packages/%40headlessui-tailwindcss) plugin to target this attribute with modifiers like `ui-open:*`:

`<template>
  <TabGroup>
    <TabList>
      <Tab

        class="ui-selected:bg-blue-500 ui-selected:text-white ui-not-selected:bg-white ui-not-selected:text-black"
      >
        Tab 1
      </Tab>
      <!-- ... -->
    </TabList>
    <TabPanels>
      <TabPanel>Content 1</TabPanel>
      <!-- ... -->
    </TabPanels>
  </TabGroup>
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>
`

## [](#disabling-a-tab)Disabling a tab
To disable a tab, use the `disabled` prop on the `Tab` component. Disabled tabs cannot be selected with the mouse, and are also skipped when navigating the tab list using the keyboard.

`<template>
  <TabGroup>
    <TabList>
      <Tab>Tab 1</Tab>

      <Tab disabled>Tab 2</Tab>
      <Tab>Tab 3</Tab>
    </TabList>
    <TabPanels>
      <TabPanel>Content 1</TabPanel>
      <TabPanel>Content 2</TabPanel>
      <TabPanel>Content 3</TabPanel>
    </TabPanels>
  </TabGroup>
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>
`

## [](#manually-activating-tabs)Manually activating tabs
By default, tabs are automatically selected as the user navigates through them using the arrow keys.

If you&#x27;d rather not change the current tab until the user presses `Enter` or `Space`, use the `manual` prop on the `TabGroup` component. This can be helpful if selecting a tab performs an expensive operation and you don&#x27;t want to run it unnecessarily.

`<template>

  <TabGroup manual>
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
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>
`

The `manual` prop has no impact on mouse interactions — tabs will still be selected as soon as they are clicked.

## [](#vertical-tabs)Vertical tabs

If you&#x27;ve styled your `TabList` to appear vertically, use the `vertical` prop to enable navigating with the up and down arrow keys instead of left and right, and to update the `aria-orientation` attribute for assistive technologies.

`<template>

  <TabGroup vertical>
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
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>
`

## [](#specifying-the-default-tab)Specifying the default tab
To change which tab is selected by default, use the `:defaultIndex="number"` prop on the `TabGroup` component.

`<template>

  <TabGroup :defaultIndex="1">
    <TabList>
      <Tab>Tab 1</Tab>

      <!-- Selects this tab by default -->

      <Tab>Tab 2</Tab>

      <Tab>Tab 3</Tab>
    </TabList>
    <TabPanels>
      <TabPanel>Content 1</TabPanel>

      <!-- Displays this tab by default -->

      <TabPanel>Content 2</TabPanel>

      <TabPanel>Content 3</TabPanel>
    </TabPanels>
  </TabGroup>
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
</script>
`

If you happen to provide an index that is out of bounds, then the last non-disabled tab will be selected on initial render. (For example, `<TabGroup :defaultIndex="5"` in the example above would render the third panel as selected.)

## [](#listening-for-changes)Listening for changes

To run a function whenever the selected tab changes, use the `@change` event on the `TabGroup` component.

`<template>

  <TabGroup @change="changeTab">
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
</template>

<script setup>
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'

  function changeTab(index) {

    console.log('Changed active tab to:', index)

  }
</script>
`

## [](#controlling-the-active-tab)Controlling the active tab
The tabs component can also be used as a controlled component. To do this, provide the `selectedIndex` and manage the state yourself.

`<template>

  <TabGroup :selectedIndex="selectedTab" @change="changeTab">
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
</template>

<script setup>
  import { ref } from 'vue'
  import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'

  const selectedTab = ref(0)

  function changeTab(index) {

    selectedTab.value = index

  }
</script>
`

## [](#accessibility-notes)Accessibility notes

### [](#mouse-interaction)Mouse interaction
Clicking a `Tab` will select that tab and display the corresponding `TabPanel`.

### [](#keyboard-interaction)Keyboard interaction

All interactions apply when a `Tab` component is focused.

CommandDescription
ArrowLeft and ArrowRight

Selects the previous/next non-disabled tab.

ArrowUp and ArrowDownwhen `vertical` is set

Selects the previous/next non-disabled tab.

Home or PageUp

Selects the first non-disabled tab.

End or PageDown

Selects the last non-disabled tab.

Enter or Space when `manual` is set

Activates the selected tab.

### [](#other)Other

All relevant ARIA attributes are automatically managed.

For a full reference on all accessibility features implemented in `Tabs`, see [the ARIA spec on Tabs](https://www.w3.org/TR/wai-aria-practices-1.2/#tabpanel).

## [](#component-api)Component API

### [](#tab-group)TabGroup

The main TabGroup component.

PropDefaultDescription`as``template`
`String | Component`

The element or component the `TabGroup` should render as.

`defaultIndex``0`
`Number`

The default selected index

`selectedIndex`—
`number`

The selected index if you want to use the Tabs component as a controlled
component.

`vertical``false`
`Boolean`

When true, the orientation of the `TabList` will be `vertical`, otherwise
it will be `horizontal`.

`manual``false`
`Boolean`

When true, the user can only display a panel via the keyboard by first
navigating to it using the arrow keys, and then by pressing `Enter` or
`Space`. By default, panels are automatically displayed when navigated to
via the arrow keys. Note that this prop has no affect on mouse behavior.

Slot PropDescription`selectedIndex`
`Number`

The currently selected index.

EventDescription`change`

A function called whenever the active tab changes.

### [](#tab-list)TabList

PropDefaultDescription`as``div`
`String | Component`

The element or component the `TabList` should render as.

Slot PropDescription`selectedIndex`
`Number`

The currently selected index.

### [](#tab)Tab

PropDefaultDescription`as``button`
`String | Component`

The element or component the `Tab` should render as.

`disabled``false`
`Boolean`

Whether or not the `Tab` is currently disabled.

Slot PropDescription`selected`
`Boolean`

Whether or not the `Tab` is currently selected.

### [](#tab-panels)TabPanels

PropDefaultDescription`as``div`
`String | Component`

The element or component the `TabPanels` should render as.

Slot PropDescription`selectedIndex`
`Number`

The currently selected index.

### [](#tab-panel)TabPanel

PropDefaultDescription`as``div`
`String | Component`

The element or component the `TabPanel` should render as.

`static``false`
`Boolean`

Whether the element should ignore the selected index.

_Note: `static` and `unmount` can not be used at the same time.

`unmount``true`
`Boolean`

Whether the element should be unmounted or hidden based on the selected
index.

_Note: `static` and `unmount` can not be used at the same time.

Slot PropDescription`selected`
`Boolean`

Whether or not the `TabPanel` is currently selected.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)