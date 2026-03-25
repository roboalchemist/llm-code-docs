# Source: https://headlessui.com/react/transition

Title: Headless UI

URL Source: https://headlessui.com/react/transition

Markdown Content:
Control the transition styles of conditionally rendered elements, including nested child transitions, using CSS classes.

[](https://headlessui.com/react/transition#installation)
--------------------------------------------------------

To get started, install Headless UI via npm:

`npm install @headlessui/react`
[](https://headlessui.com/react/transition#basic-example)
---------------------------------------------------------

To transition a conditionally rendered element, wrap it in the `Transition` component and use the `show` prop to indicate whether it is open or closed.

Then, use native CSS transition styles to apply an animation, specifying the element's closed styles by targeting the `data-closed` attribute that the `Transition` component exposes.

```
import { Transition } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [open, setOpen] = useState(false)

  return (
    <>
      <button onClick={() => setOpen((open) => !open)}>Toggle</button>
      <Transition show={open}>
        <div className="transition duration-300 ease-in data-closed:opacity-0">I will fade in and out</div>
      </Transition>
    </>
  )
}
```

Styles defined with the `data-closed` attribute will be used as the starting point when transitioning in as well as the ending point when transitioning out.

For more complex transitions, you can also use the `data-enter`, `data-leave`, and `data-transition` attributes to apply styles at the different stages of the transition.

[](https://headlessui.com/react/transition#examples)
----------------------------------------------------

### [](https://headlessui.com/react/transition#different-enter-leave-transitions)

Use the `data-enter` and `data-leave` attributes to apply different transition styles when entering and leaving:

```
import { Transition } from '@headlessui/react'
import clsx from 'clsx'
import { useState } from 'react'

function Example() {
  const [open, setOpen] = useState(false)

  return (
    <div className="relative">
      <button onClick={() => setOpen((open) => !open)}>Toggle</button>
      <Transition show={open}>
        <div
          className={clsx([
            // Base styles
            'absolute w-48 border transition ease-in-out',
            // Shared closed styles
            'data-closed:opacity-0',
            // Entering styles
            'data-enter:duration-100 data-enter:data-closed:-translate-x-full',
            // Leaving styles
            'data-leave:duration-300 data-leave:data-closed:translate-x-full',
          ])}
        >
          I will enter from the left and leave to the right
        </div>
      </Transition>
    </div>
  )
}
```

This example combines the `data-enter` and `data-closed` attributes to specify the starting point of the enter transition, and combines the `data-leave` and `data-closed` attributes to specify the ending point of the leave transition.

It also uses the `data-enter` and `data-leave` attributes to specify different enter and leave durations.

### [](https://headlessui.com/react/transition#coordinating-multiple-transitions)

Sometimes you need to transition multiple elements with different animations but all based on the same state. For example, say the user clicks a button to open a sidebar that slides over the screen, and you also need to fade-in a backdrop at the same time.

You can do this by wrapping the related elements with a parent `Transition` component, and wrapping each child that needs its own transition styles with a `TransitionChild` component, which will automatically communicate with the parent `Transition` and inherit the parent's `open` state.

```
import { Transition, TransitionChild } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [open, setOpen] = useState(false)

  return (
    <>
      <button onClick={() => setOpen(true)}>Open</button>
      {/* The `show` prop controls all nested `TransitionChild` components. */}
      <Transition show={open}>        {/* Backdrop */}
        <TransitionChild>          <div
            className="fixed inset-0 bg-black/30 transition duration-300 data-closed:opacity-0"
            onClick={() => setOpen(false)}
          />
        </TransitionChild>
        {/* Slide-in sidebar */}
        <TransitionChild>          <div className="fixed inset-y-0 left-0 w-64 bg-white transition duration-300 data-closed:-translate-x-full">
            {/* ... */}
          </div>        </TransitionChild>      </Transition>
    </>
  )
}
```

The `TransitionChild` component has the exact same API as the `Transition` component, but with no `show` prop, since the `show` value is controlled by the parent.

Parent `Transition` components will always automatically wait for all children to finish transitioning before unmounting, so you don't need to manage any of that timing yourself.

### [](https://headlessui.com/react/transition#transitioning-on-initial-mount)

If you want an element to transition the very first time it's rendered, set the `appear` prop to `true`.

This is useful if you want something to transition in on initial page load, or when its parent is conditionally rendered.

```
import { Transition } from '@headlessui/react'
import { useState } from 'react'

function Example() {
  const [open, setOpen] = useState(true)

  return (
    <>
      <button onClick={() => setOpen((open) => !open)}>Toggle</button>
      <Transition show={open} appear={true}>        <div className="transition duration-300 ease-in data-closed:opacity-0">I will fade in on initial render</div>
      </Transition>
    </>
  )
}
```

[](https://headlessui.com/react/transition#component-api)
---------------------------------------------------------

### [](https://headlessui.com/react/transition#transition)
