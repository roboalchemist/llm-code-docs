# Source: https://motion.dev/docs/react

Title: Get started

URL Source: https://motion.dev/docs/react

Published Time: Fri, 13 Mar 2026 09:28:50 GMT

Markdown Content:
**Motion for React** (previously Framer Motion) is a React animation library for building smooth, production-grade UI animations. You can start with simple prop-based animations before growing to layout, gesture and scroll animations.

Motion's hybrid engine runs animations natively in the browser using the Web Animations API and ScrollTimeline for 120fps performance. When you need capabilities those APIs can't provide (like spring physics, interruptible keyframes, or gesture tracking) it seamlessly falls back to JavaScript.

Motion is trusted by companies like [Framer](https://framer.com/) and [Figma](https://figma.com/) to power animations for their millions of users, and has over 30 million downloads per month on [npm](https://www.npmjs.com/package/framer-motion).

In this guide, we'll learn **why** and **when** you should use Motion, how to **install** it, and give you an overview of its main features.

[Why Motion for React?](https://motion.dev/docs/react#why-motion-for-react)
---------------------------------------------------------------------------

React gives you the power to build dynamic user interfaces, but orchestrating complex, performant animations can be a challenge. Motion is a production-ready React animation library designed to solve this problem, making it simple to create everything from beautiful micro-interactions to complex, gesture-driven animations.

import{motion}from"motion/react"

function Component(){

return<motion.button animate={{opacity:1}}/>

}

### [Key advantages](https://motion.dev/docs/react#key-advantages)

Here’s when it’s the right choice for your project.

*   **Built for React.** While other animation libraries like [GSAP](https://motion.dev/docs/gsap-vs-motion) are messy to integrate with React, Motion's declarative API is a natural fit. Animations can be linked directly to state and props.

*   **Hardware-acceleration.** Motion leverages the same high-performance browser animations as CSS, ensuring your UIs stay smooth and snappy. 120fps animations with a much simpler and more expressive API.

*   **Animate anything.** CSS has hard limits. Values you can't animate, keyframes you can't interrupt, staggers that must be hardcoded. Motion provides a single, consistent API that scales from simple to complex.

*   **App-like gestures.** Standard CSS `:hover` events are unreliable on touch devices. Motion provides robust, cross-device gesture recognisers for tap, drag, and hover that feel native and intuitive on any device.

*   **Production ready.** Built on TypeScript, surrounded by an extensive test suite, and fully tree-shakable so you only include what you import.

### [When is CSS a better choice?](https://motion.dev/docs/react#when-is-css-a-better-choice)

For simple, self-contained effects (like a color change on hover) a standard CSS transition is a lightweight solution. The strength of Motion is that it can do these simple kinds of animations but also scale to anything you can imagine. All with the same easy to write and maintain API.

[Install](https://motion.dev/docs/react#install)
------------------------------------------------

Motion is available via [npm](https://www.npmjs.com/package/motion):

npm install motion

Features can now be imported via `"motion/react"`:

import { motion } from "motion/react"

Prefer to install via CDN, or looking for framework-specific instructions? Check out our [full installation guide](https://motion.dev/docs/react-installation).

[Create your first animation](https://motion.dev/docs/react#create-your-first-animation)
----------------------------------------------------------------------------------------

The `<motion />` component is the foundation of Motion for React. Prefix any HTML or SVG tag with `motion.` to unlock animation props like `animate`, `whileHover`, and `exit`:

<motion.ul animate={{ rotate: 360 }} />

When values in `animate` change, Motion automatically transitions between them.

Physical properties like `x` and `scale` use spring physics by default; visual properties like `opacity` use tween easing. Override the animation type, duration, easing, or delay via [the](https://motion.dev/docs/react-transitions)`transition`[prop](https://motion.dev/docs/react-transitions):

<motion.div
  animate={{
    scale: 2,
    transition: { duration: 2 }
  }}
/>

[Learn more about React animation](https://motion.dev/docs/react-animation)

If you're the kind of developer who learns better by doing, check out our library of [Basics examples](https://motion.dev/examples#basics). Each comes complete with a live demo and copy/paste source code.

[Enter animation](https://motion.dev/docs/react#enter-animation)
----------------------------------------------------------------

When a component enters the page, it will automatically animate to the values defined in the `animate` prop.

You can provide values to animate from via the `initial` prop (otherwise these will be read from the DOM).

<motion.button initial={{ scale: 0 }} animate={{ scale: 1 }} />

Or disable this initial animation entirely by setting `initial` to `false`.

<motion.button initial={false} animate={{ scale: 1 }} />

[Hover & tap animation](https://motion.dev/docs/react#hover-tap-animation)
--------------------------------------------------------------------------

`<motion />` extends React's event system with powerful [gesture animations](https://motion.dev/docs/react-gestures). It currently supports hover, tap, focus, and drag.

<motion.button
  whileHover={{ scale: 1.1 }}
  whileTap={{ scale: 0.95 }}
  onHoverStart={() => console.log('hover started!')}
/>

Motion's gestures are designed to feel better than using CSS or JavaScript events alone.

[Scroll animation](https://motion.dev/docs/react#scroll-animation)
------------------------------------------------------------------

Motion supports both types of [scroll animations](https://motion.dev/docs/react-scroll-animations): **Scroll-triggered**and **scroll-linked**.

To trigger an animation on scroll, the `whileInView` prop defines a state to animate to/from when an element enters/leaves the viewport:

<motion.div
  initial={{ backgroundColor: "rgb(0, 255, 0)", opacity: 0 }}
  whileInView={{ backgroundColor: "rgb(255, 0, 0)", opacity: 1 }}
/>

Whereas to link a value directly to scroll position, it's possible to use `MotionValue`s via `useScroll`.

const { scrollYProgress } = useScroll()

return <motion.div style={{ scaleX: scrollYProgress }} />

[Layout animation](https://motion.dev/docs/react#layout-animation)
------------------------------------------------------------------

Motion's [layout animation](https://motion.dev/docs/react-layout-animations) engine detects layout changes (size, position, reorder) and smoothly animates between states using transforms. Unlike basic "FLIP" implementations, it does so while correcting for scale-distortion.

It's as easy as applying the `layout` prop.

<motion.div layout />

Or to animate between completely different elements, a `layoutId`:

<motion.div layoutId="underline" />

[Exit animations](https://motion.dev/docs/react#exit-animations)
----------------------------------------------------------------

By wrapping `motion` components with `<AnimatePresence>` we gain access to [exit animations](https://motion.dev/docs/react-animate-presence). This allows us to animate elements as they're removed from the DOM.

<AnimatePresence>
  {show ? <motion.div key="box" exit={{ opacity: 0 }} /> : null}
</AnimatePresence>

[SVG animations](https://motion.dev/docs/react#svg-animations)
--------------------------------------------------------------

Motion has full support for [SVG animations](https://motion.dev/docs/react-svg-animation), including support for animating `viewBox` and special values for simple path drawing effects.

<motion.circle animate={{ pathLength: 1 }} />

[Development tools](https://motion.dev/docs/react#development-tools)
--------------------------------------------------------------------

Want an AI that knows every Motion API and can generate animations on demand? Or visual animation editing, directly in your code editor? [Motion Studio](https://motion.dev/studio) provides all that and more. Enhance your workflow tools with an [AI-searchable examples database](https://motion.dev/docs/studio-ai-context), a [CSS and Motion transition editor](https://motion.dev/docs/studio-visual-controls), [performance audit skill](https://motion.dev/docs/animation-performance-audit), and more.

### Install Motion Studio

One-click install for Cursor:

#### Stay in the loop

Sign up for the Motion newsletter.

[Learn next](https://motion.dev/docs/react#learn-next)
------------------------------------------------------

That covers the core building blocks. Here's where to go next based on what you want to build and your learning style.

The [React animation](https://motion.dev/docs/react-animation) guide will teach you more about the different types of animations you can build with this React animation library.

Or, you can learn by doing, diving straight into our collection of [examples](https://motion.dev/examples?platform=react#basics). Each comes complete with full source code that you can copy-paste into your project.
