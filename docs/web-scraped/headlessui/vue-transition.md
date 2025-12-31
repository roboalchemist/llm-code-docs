# Source: https://headlessui.com/v1/vue/transition

# Transition

The Transition component takes Vue&#x27;s built-in transition element one step
further by letting you coordinate nested child transitions from a single root
component.

PreviewCode

CopyCopied!

## [](#installation)Installation

To get started, install Headless UI via npm.

Please note that **this library only supports Vue 3**.

`npm install @headlessui/vue`

## [](#about-this-component)About this component
Vue has a built-in `<transition>` component that works great with Tailwind&#x27;s class-based styling approach, as well as alongside other Headless UI components. In fact, most of the demos and code snippets you&#x27;ll find for the other Vue components on this site rely on this built-in transition exclusively.

But there&#x27;s one exception: nested child transitions. This technique is needed when you want to coordinate different animations for different child elements – for example, fading in a Dialog&#x27;s backdrop, while at the same time sliding in the contents of the Dialog from one side of the screen.

The only way to achieve this effect using the built-in `<transition>` element is to manually synchronize each of the child transitions, and even then the approach can be buggy and error-prone.

That&#x27;s why we&#x27;ve included a `<TransitionRoot />` component in Headless UI. Its API is similar to Vue&#x27;s own element, but it also provides a means for coordinating multiple transitions via the included `<TransitionChild />` component, as described below.

For all components except `Dialog`, you may use Vue&#x27;s built-in `<transition>` element whenever you&#x27;re applying a single transition. For animating a `Dialog`, or coordinating multiple transitions on any other component, use the `TransitionRoot` component from Headless UI instead.

## [](#basic-example)Basic example

The `TransitionRoot` accepts a `show` prop that controls whether the children should be shown or hidden, and a set of lifecycle props (like `enter-from`, and `leave-to`) that let you add CSS classes at specific phases of a transition.

`<template>
  <button @click="isShowing = !isShowing">Toggle</button>
  <TransitionRoot
    :show="isShowing"
    enter="transition-opacity duration-75"
    enter-from="opacity-0"
    enter-to="opacity-100"
    leave="transition-opacity duration-150"
    leave-from="opacity-100"
    leave-to="opacity-0"
  >
    I will fade in and out
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot } from '@headlessui/vue'

  const isShowing = ref(true)
</script>`

## [](#showing-and-hiding-content)Showing and hiding content
Wrap the content that should be conditionally rendered in a `<TransitionRoot>` component, and use the `show` prop to control whether the content should be visible or hidden.

`<template>
  <button @click="isShowing = !isShowing">Toggle</button>

  <TransitionRoot :show="isShowing">
    I will appear and disappear.
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot } from '@headlessui/vue'

  const isShowing = ref(true)
</script>
`

## [](#rendering-as-a-different-element)Rendering as a different element
By default, the transition components will render a `div` element.

Use the `as` prop to render a component as a different element or as your own custom component. Any other HTML attributes (like `class`) can be added directly to the `TransitionRoot` the same way they would be to regular elements.

`<template>
  <button @click="isShowing = !isShowing">Toggle</button>

  <TransitionRoot :show="isShowing" as="a" href="/my-url" class="font-bold">
    I will appear and disappear.
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot } from '@headlessui/vue'

  const isShowing = ref(true)
</script>
`

## [](#animating-transitions)Animating transitions
By default, a `TransitionRoot` will enter and leave instantly, which is probably not what you&#x27;re looking for if you&#x27;re using this component.

To animate your enter/leave transitions, add classes that provide the styling for each phase of the transitions using these props:

- **enter**: Applied the entire time an element is entering. Usually you define your duration and what properties you want to transition here, for example `transition-opacity duration-75`.

- **enter-from**: The starting point to enter from, for example `opacity-0` if something should fade in.

- **enter-to**: The ending point to enter to, for example `opacity-100` after fading in.

- **leave**: Applied the entire time an element is leaving. Usually you define your duration and what properties you want to transition here, for example `transition-opacity duration-75`.

- **leave-from**: The starting point to leave from, for example `opacity-100` if something should fade out.

- **leave-to**: The ending point to leave to, for example `opacity-0` after fading out.

Here&#x27;s an example:

`<template>
  <button @click="isShowing = !isShowing">Toggle</button>
  <TransitionRoot
    :show="isShowing"

    enter="transition-opacity duration-75"

    enter-from="opacity-0"

    enter-to="opacity-100"

    leave="transition-opacity duration-150"

    leave-from="opacity-100"

    leave-to="opacity-0"
  >
    I will appear and disappear.
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot } from '@headlessui/vue'

  const isShowing = ref(true)
</script>
`

In this example, the transitioning element will take 75ms to enter (that&#x27;s the `duration-75` class), and will transition the opacity property during that time (that&#x27;s `transition-opacity`).

It will start completely transparent before entering (that&#x27;s `opacity-0` in the `enter-from` phase), and fade in to completely opaque (`opacity-100`) when finished (that&#x27;s the `enterTo` phase).

When the element is being removed (the `leave` phase), it will transition the opacity property, and spend 150ms doing it (`transition-opacity duration-150`).

It will start as completely opaque (the `opacity-100` in the `leave-from` phase), and finish as completely transparent (the `opacity-0` in the `leave-to` phase).

All of these props are optional, and will default to just an empty string.

## [](#co-ordinating-multiple-transitions)Co-ordinating multiple transitions

Sometimes you need to transition multiple elements with different animations but all based on the same state. For example, say the user clicks a button to open a sidebar that slides over the screen, and you also need to fade-in a background overlay at the same time.

You can do this by wrapping the related elements with a parent `TransitionRoot` component, and wrapping each child that needs its own transition styles with a `TransitionChild` component, which will automatically communicate with the parent `TransitionRoot` and inherit the parent&#x27;s `show` state.

`<template>
  <!-- The `show` prop controls all nested `TransitionChild` components. -->
  <TransitionRoot :show="isShowing">
    <!-- Background overlay -->
    <TransitionChild
      enter="transition-opacity ease-linear duration-300"
      enter-from="opacity-0"
      enter-to="opacity-100"
      leave="transition-opacity ease-linear duration-300"
      leave-from="opacity-100"
      leave-to="opacity-0"
    >
      <!-- ... -->
    </TransitionChild>

    <!-- Sliding sidebar -->
    <TransitionChild
      enter="transition ease-in-out duration-300 transform"
      enter-from="-translate-x-full"
      enter-to="translate-x-0"
      leave="transition ease-in-out duration-300 transform"
      leave-from="translate-x-0"
      leave-to="-translate-x-full"
    >
      <!-- ... -->
    </TransitionChild>
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot, TransitionChild } from '@headlessui/vue'

  const isShowing = ref(true)
</script>`

The `TransitionChild` component has the exact same API as the `TransitionRoot` component, but with no `show` prop, since the `show` value is controlled by the parent.

Parent `TransitionRoot` components will always automatically wait for all children to finish transitioning before unmounting, so you don&#x27;t need to manage any of that timing yourself.

## [](#transitioning-on-initial-mount)Transitioning on initial mount

If you want an element to transition the very first time it&#x27;s rendered, set the `appear` prop to `true`.

This is useful if you want something to transition in on initial page load, or when its parent is conditionally rendered.

`<template>
  <TransitionRoot

    appear
    :show="isShowing"
    enter="transition-opacity duration-75"
    enter-from="opacity-0"
    enter-to="opacity-100"
    leave="transition-opacity duration-150"
    leave-from="opacity-100"
    leave-to="opacity-0"
  >
    <!-- Your content goes here -->
  </TransitionRoot>
</template>

<script setup>
  import { ref } from 'vue'
  import { TransitionRoot } from '@headlessui/vue'

  const isShowing = ref(true)
</script>
`

## [](#component-api)Component API

### [](#transition-root)TransitionRoot

PropDefaultDescription`show`—
`Boolean`

Whether the children should be shown or hidden.

`as``div`
`String | Component`

The element or component to render in place of the Transition itself.

`appear``false`
`Boolean`

Whether the transition should run on initial mount.

`unmount``true`
`Boolean`

Whether the element should be unmounted or hidden based on the show state.

`enter`—
`String`

Classes to add to the transitioning element during the entire enter phase.

`enter-from`—
`String`

Classes to add to the transitioning element before the enter phase starts.

`enter-to`—
`String`

Classes to add to the transitioning element immediately after the enter
phase starts.

`entered`—
`String`

Classes to add to the transitioning element once the transition is done.
These classes will persist after that, until it&#x27;s time to leave.

`leave`—
`String`

Classes to add to the transitioning element during the entire leave phase.

`leave-from`—
`String`

Classes to add to the transitioning element before the leave phase starts.

`leave-to`—
`String`

Classes to add to the transitioning element immediately after the leave
phase starts.

EventDescription`before-enter`

Emitted before the enter transition starts.

`after-enter`

Emitted after the enter transition finishes.

`before-leave`

Emitted before the leave transition starts.

`after-leave`

Emitted after the leave transition finishes.

### [](#transition-child)TransitionChild

PropDefaultDescription`as``div`
`String | Component`

The element or component to render in place of the Transition itself.

`appear``false`
`Boolean`

Whether the transition should run on initial mount.

`unmount``true`
`Boolean`

Whether the element should be unmounted or hidden based on the show state.

`enter`—
`String`

Classes to add to the transitioning element during the entire enter phase.

`enter-from`—
`String`

Classes to add to the transitioning element before the enter phase starts.

`enter-to`—
`String`

Classes to add to the transitioning element immediately after the enter
phase starts.

`entered`—
`String`

Classes to add to the transitioning element once the transition is done.
These classes will persist after that, until it&#x27;s time to leave.

`leave`—
`String`

Classes to add to the transitioning element during the entire leave phase.

`leave-from`—
`String`

Classes to add to the transitioning element before the leave phase starts.

`leave-to`—
`String`

Classes to add to the transitioning element immediately after the leave
phase starts.

EventDescription`before-enter`

Emitted before the enter transition starts.

`after-enter`

Emitted after the enter transition finishes.

`before-leave`

Emitted before the leave transition starts.

`after-leave`

Emitted after the leave transition finishes.

## [](#styled-examples)Styled examples

If you&#x27;re interested in predesigned component examples using Headless UI and Tailwind CSS, check out **Tailwind UI** — a collection of beautifully designed and expertly crafted components built by us.

It&#x27;s a great way to support our work on open-source projects like this and makes it possible for us to improve them and keep them well-maintained.

[
Explore more predesigned examples→
](https://tailwindui.com/)