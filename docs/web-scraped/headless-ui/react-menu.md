# Source: https://headlessui.com/react/menu

Title: Headless UI

URL Source: https://headlessui.com/react/menu

Markdown Content:
Menus offer an easy way to build custom, accessible dropdown components with robust support for keyboard navigation.

[](https://headlessui.com/react/menu#installation)
--------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/menu#basic-example)
---------------------------------------------------

Menus are built using the `Menu`, `MenuButton`, `MenuItems`, and `MenuItem` components:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom">
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

The `MenuButton` will automatically open and close the `MenuItems` when clicked, and when the menu is opened the list of items receives focus and is navigable via the keyboard.

[](https://headlessui.com/react/menu#styling)
---------------------------------------------

Headless UI keeps track of a lot of state about each component, like which menu item is currently focused via the keyboard, whether a popover is open or closed, or which listbox option is currently selected.

But because the components are headless and completely unstyled out of the box, you can't see this information in your UI until you provide the styles you want for each state yourself.

### [](https://headlessui.com/react/menu#using-data-attributes)

The easiest way to style the different states of a Headless UI component is using the `data-*` attributes that each component exposes.

For example, the `MenuButton` component exposes a `data-active` attribute, which tells you if the menu is currently open, and the `MenuItem` component exposes a `data-focus` attribute, which tells you if the menu item is currently focused via the mouse or keyboard.

```
<!-- Rendered `MenuButton`, `MenuItems`, and `MenuItem` -->
<button data-active>Options</button>
<div data-open>
  <a href="/settings">Settings</a>
  <a href="/support" data-focus>Support</a>
  <a href="/license">License</a>
</div>
```

Use the [CSS attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) to conditionally apply styles based on the presence of these data attributes. If you're using Tailwind CSS, the [data attribute modifier](https://tailwindcss.com/docs/hover-focus-and-other-states#data-attributes) makes this easy:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

const links = [
  { href: '/settings', label: 'Settings' },
  { href: '/support', label: 'Support' },
  { href: '/license', label: 'License' },
]

function Example() {
  return (
    <Menu>
      <MenuButton className="data-active:bg-blue-200">My account</MenuButton>      <MenuItems anchor="bottom">
        {links.map((link) => (
          <MenuItem key={link.href} className="block data-focus:bg-blue-100">            <a href={link.href}>{link.label}</a>
          </MenuItem>
        ))}
      </MenuItems>
    </Menu>
  )
}
```

See the [component API](https://headlessui.com/react/menu#component-api) for a list of all the available data attributes.

### [](https://headlessui.com/react/menu#using-render-props)

Each component also exposes information about its current state via [render props](https://reactjs.org/docs/render-props.html) that you can use to conditionally apply different styles or render different content.

For example, the `MenuButton` component exposes an `active` state, which tells you if the menu is currently open, and the `MenuItem` component exposes a `focus` state, which tells you if the menu item is currently focused via the mouse or keyboard.

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'
import clsx from 'clsx'
import { Fragment } from 'react'

const links = [
  { href: '/settings', label: 'Settings' },
  { href: '/support', label: 'Support' },
  { href: '/license', label: 'License' },
]

function Example() {
  return (
    <Menu>
      <MenuButton as={Fragment}>        {({ active }) => <button className={clsx(active && 'bg-blue-200')}>My account</button>}      </MenuButton>      <MenuItems anchor="bottom">
        {links.map((link) => (
          <MenuItem key={link.href} as={Fragment}>            {({ focus }) => (              <a className={clsx('block', focus && 'bg-blue-100')} href={link.href}>                {link.label}              </a>            )}          </MenuItem>        ))}
      </MenuItems>
    </Menu>
  )
}
```

See the [component API](https://headlessui.com/react/menu#component-api) for a list of all the available render props.

[](https://headlessui.com/react/menu#examples)
----------------------------------------------

### [](https://headlessui.com/react/menu#using-with-buttons)

In addition to links, you can also use buttons in a `MenuItem`. This is useful when you want to trigger an action like opening a dialog or submitting a form.

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  function showSettingsDialog() {
    alert('Open settings dialog!')
  }

  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom">
        <MenuItem>          <button onClick={showSettingsDialog} className="block w-full text-left data-focus:bg-blue-100">            Settings          </button>        </MenuItem>        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
        <form action="/logout" method="post">          <MenuItem>            <button type="submit" className="block w-full text-left data-focus:bg-blue-100">              Sign out            </button>          </MenuItem>        </form>      </MenuItems>
    </Menu>
  )
}
```

### [](https://headlessui.com/react/menu#disabling-an-item)

Use the `disabled` prop to disable a `MenuItem` and prevent it from being selected:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom">
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
        <MenuItem disabled>          <a className="block data-disabled:opacity-50" href="/invite-a-friend">            Invite a friend (coming soon!)          </a>        </MenuItem>      </MenuItems>
    </Menu>
  )
}
```

### [](https://headlessui.com/react/menu#separating-items)

Use the `MenuSeparator` component to add a visual separation between items in a menu.

```
import { Menu, MenuButton, MenuItem, MenuItems, MenuSeparator } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom">
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuSeparator className="my-1 h-px bg-black" />        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

### [](https://headlessui.com/react/menu#grouping-items)

Use the `MenuSection`, `MenuHeading`, and `MenuSeparator` components to group items into sections with labels:

```
import { Menu, MenuButton, MenuHeading, MenuItem, MenuItems, MenuSection, MenuSeparator } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom">
        <MenuSection>          <MenuHeading className="text-sm opacity-50">Settings</MenuHeading>          <MenuItem>
            <a className="block data-focus:bg-blue-100" href="/profile">
              My profile
            </a>
          </MenuItem>
          <MenuItem>
            <a className="block data-focus:bg-blue-100" href="/notifications">
              Notifications
            </a>
          </MenuItem>
        </MenuSection>        <MenuSeparator className="my-1 h-px bg-black" />        <MenuSection>          <MenuHeading className="text-sm opacity-50">Support</MenuHeading>          <MenuItem>
            <a className="block data-focus:bg-blue-100" href="/support">
              Documentation
            </a>
          </MenuItem>
          <MenuItem>
            <a className="block data-focus:bg-blue-100" href="/license">
              License
            </a>
          </MenuItem>
        </MenuSection>      </MenuItems>
    </Menu>
  )
}
```

### [](https://headlessui.com/react/menu#setting-the-dropdown-width)

The `MenuItems` dropdown has no width set by default, but you can add one using CSS:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom" className="w-52">        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

If you'd like the dropdown width to match the `MenuButton` width, use the `--button-width` CSS variable that's exposed on the `MenuItems` element:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom" className="w-(--button-width)">        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

### [](https://headlessui.com/react/menu#positioning-the-dropdown)

Add the `anchor` prop to the `MenuItems` to automatically position the dropdown relative to the `MenuButton`:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom start">        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

Use the values `top`, `right`, `bottom`, or `left` to center the dropdown along the appropriate edge, or combine it with `start` or `end` to align the dropdown to a specific corner, such as `top start` or `bottom end`.

To control the gap between the button and the dropdown, use the `--anchor-gap` CSS variable:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom start" className="[--anchor-gap:4px] sm:[--anchor-gap:8px]">        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

Additionally, you can use `--anchor-offset` to control the distance that the dropdown should be nudged from its original position, and `--anchor-padding` to control the minimum space that should exist between the dropdown and the viewport.

The `anchor` prop also supports an object API that allows you to control the `gap`, `offset`, and `padding` values using JavaScript:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor={{ to: 'bottom start', gap: '4px' }}>        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

See the [MenuItems API](https://headlessui.com/react/menu#menu-items) for more information about these options.

### [](https://headlessui.com/react/menu#adding-transitions)

To animate the opening and closing of the dropdown, add the `transition` prop to the `MenuItems` component and then use CSS to style the different stages of the transition:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'

function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems
        anchor="bottom"
        transition        className="origin-top transition duration-200 ease-out data-closed:scale-95 data-closed:opacity-0"      >
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

Internally, the `transition` prop is implemented in the exact same way as the `Transition` component. See the [Transition documentation](https://headlessui.com/react/transition) to learn more.

### [](https://headlessui.com/react/menu#animating-with-framer-motion)

Headless UI also composes well with other animation libraries in the React ecosystem like [Framer Motion](https://www.framer.com/motion/) and [React Spring](https://www.react-spring.io/). You just need to expose some state to those libraries.

For example, to animate the menu with Framer Motion, add the `static` prop to the `MenuItems` component and then conditionally render it based on the `open` render prop:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'
import { AnimatePresence, motion } from 'framer-motion'

function Example() {
  return (
    <Menu>
      {({ open }) => (        <>
          <MenuButton>My account</MenuButton>
          <AnimatePresence>
            {open && (              <MenuItems
                static                as={motion.div}
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
                anchor="bottom"
                className="origin-top"
              >
                <MenuItem>
                  <a className="block data-focus:bg-blue-100" href="/settings">
                    Settings
                  </a>
                </MenuItem>
                <MenuItem>
                  <a className="block data-focus:bg-blue-100" href="/support">
                    Support
                  </a>
                </MenuItem>
                <MenuItem>
                  <a className="block data-focus:bg-blue-100" href="/license">
                    License
                  </a>
                </MenuItem>
              </MenuItems>
            )}          </AnimatePresence>
        </>
      )}    </Menu>
  )
}
```

By default, the `Menu` will close when clicking a `MenuItem`. However, some third-party `Link` components use `event.preventDefault()` which prevents the menu from closing.

In these situations you can imperatively close the menu using the `close` render prop that's available on both the `Menu` and `MenuItem` components:

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'
import { MyCustomLink } from './MyCustomLink'

function Example() {
  return (
    <Menu>
      <MenuButton>Terms</MenuButton>
      <MenuItems anchor="bottom">
        <MenuItem>
          {({ close }) => (            <MyCustomLink href="/" onClick={close}>              Read and accept
            </MyCustomLink>
          )}        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

### [](https://headlessui.com/react/menu#rendering-as-different-elements)

By default, the `Menu` and its subcomponents each render a default element that is sensible for that component.

For example, `MenuButton` renders a `button` by default, and `MenuItems` renders a `div`. By contrast, `Menu` and `MenuItem`_do not render an element_, and instead render their children directly by default.

Use the `as` prop to render the component as a different element or as your own custom component, making sure your custom components [forward refs](https://react.dev/reference/react/forwardRef) so that Headless UI can wire things up correctly.

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'
import { forwardRef } from 'react'

let MyCustomButton = forwardRef(function (props, ref) {  return <button className="..." ref={ref} {...props} />})
function Example() {
  return (
    <Menu>
      <MenuButton as={MyCustomButton}>My account</MenuButton>      <MenuItems anchor="bottom" as="section">        <MenuItem as="a" className="block data-focus:bg-blue-100" href="/settings">          Settings
        </MenuItem>
        <MenuItem as="a" className="block data-focus:bg-blue-100" href="/support">          Support
        </MenuItem>
        <MenuItem as="a" className="block data-focus:bg-blue-100" href="/license">          License
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

To tell an element to render its children directly with no wrapper element, use `as={Fragment}`.

```
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react'
import { Fragment } from 'react'

function Example() {
  return (
    <Menu>
      <MenuButton as={Fragment}>        <button>My account</button>      </MenuButton>      <MenuItems anchor="bottom">
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/settings">
            Settings
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/support">
            Support
          </a>
        </MenuItem>
        <MenuItem>
          <a className="block data-focus:bg-blue-100" href="/license">
            License
          </a>
        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

This is important if you are using an interactive element like an `<a>` tag inside the `MenuItem`. If the `MenuItem` had an `as="div"`, then the props provided by Headless UI would be forwarded to the `div` instead of the `a`, which means that you can't go to the URL provided by the `<a>` tag anymore via your keyboard.

### [](https://headlessui.com/react/menu#integrating-with-next-js)

Prior to Next.js v13, the `Link` component did not forward unknown props to the underlying `a` element, preventing the menu from closing on click when used inside a `MenuItem`.

If you're using Next.js v12 or older, you can work around this issue by creating your own component that wraps `Link` and forwards unknown props to the child `a` element:

```
import { forwardRef } from 'react'
import Link from 'next/link'
import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/react'

const MyLink = forwardRef((props, ref) => {  let { href, children, ...rest } = props  return (    <Link href={href}>      <a ref={ref} {...rest}>        {children}      </a>    </Link>  )})
function Example() {
  return (
    <Menu>
      <MenuButton>My account</MenuButton>
      <MenuItems anchor="bottom">
        <MenuItem>
          <MyLink href="/settings">Settings</MyLink>        </MenuItem>
      </MenuItems>
    </Menu>
  )
}
```

This will ensure that all of the event listeners Headless UI needs to add to the `a` element are properly applied.

This behavior was changed in Next.js v13 making this workaround no longer necessary.

[](https://headlessui.com/react/menu#keyboard-interaction)
----------------------------------------------------------

Divides a list of `MenuItem` components into sections with proper accessibility semantics.

Adds an accessible label to a `MenuSection`.

Separates two `MenuSection` components, with proper accessibility semantics.
