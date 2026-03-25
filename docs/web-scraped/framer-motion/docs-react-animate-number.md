# Source: https://motion.dev/docs/react-animate-number

Title: AnimateNumber — React ticker & countdown animation | Motion

URL Source: https://motion.dev/docs/react-animate-number

Published Time: Fri, 13 Mar 2026 09:31:25 GMT

Markdown Content:
AnimateNumber — React ticker & countdown animation | Motion
===============

[](https://motion.dev/)

[Docs](https://motion.dev/docs)

[Examples](https://motion.dev/examples)

[Tutorials](https://motion.dev/tutorials)

[AI Kit](https://motion.dev/docs/ai-kit)

![Image 1: icon entry point for Site Search](https://framerusercontent.com/images/LcSrauRN6S5dbcfiUyHSBISkE.svg?width=20&height=20)

[Motion+](https://motion.dev/plus)

[JS --](https://motion.dev/docs/quick-start)[React -----](https://motion.dev/docs/react)[Vue](https://motion.dev/docs/vue)[Studio](https://motion.dev/docs/studio)

[### Get started](https://motion.dev/docs/react)[### Examples](https://motion.dev/examples?platform=react)[### Courses](https://motion.dev/docs/react-courses)

### Animation

*   [Overview](https://motion.dev/docs/react-animation) 
*   [Layout](https://motion.dev/docs/react-layout-animations) 
*   [Scroll](https://motion.dev/docs/react-scroll-animations) 
*   [SVG](https://motion.dev/docs/react-svg-animation) 
*   [Transitions](https://motion.dev/docs/react-transitions) 

### Gestures

*   [Overview](https://motion.dev/docs/react-gestures) 
*   [Hover](https://motion.dev/docs/react-hover-animation) 
*   [Drag](https://motion.dev/docs/react-drag) 

### Components

*   [Motion component](https://motion.dev/docs/react-motion-component) 
*   [AnimateActivity](https://motion.dev/docs/react-animate-activity) 
*   [AnimatePresence](https://motion.dev/docs/react-animate-presence) 
*   [AnimateView](https://motion.dev/docs/react-animate-view) 
*   [LayoutGroup](https://motion.dev/docs/react-layout-group) 
*   [LazyMotion](https://motion.dev/docs/react-lazy-motion) 
*   [MotionConfig](https://motion.dev/docs/react-motion-config) 
*   [Reorder](https://motion.dev/docs/react-reorder) 

### Premium APIs

*   [AnimateNumber](https://motion.dev/docs/react-animate-number) 
*   [Carousel](https://motion.dev/docs/react-carousel) 
*   [Cursor](https://motion.dev/docs/cursor) 
*   [ScrambleText](https://motion.dev/docs/react-scramble-text) 
*   [Ticker](https://motion.dev/docs/react-ticker) 
*   [Typewriter](https://motion.dev/docs/react-typewriter) 

### Motion values

*   [Overview](https://motion.dev/docs/react-motion-value) 
*   [useMotionTemplate](https://motion.dev/docs/react-use-motion-template) 
*   [useMotionValueEvent](https://motion.dev/docs/react-use-motion-value-event) 
*   [useScroll](https://motion.dev/docs/react-use-scroll) 
*   [useSpring](https://motion.dev/docs/react-use-spring) 
*   [useTime](https://motion.dev/docs/react-use-time) 
*   [useTransform](https://motion.dev/docs/react-use-transform) 
*   [useVelocity](https://motion.dev/docs/react-use-velocity) 

### Hooks

*   [useAnimate](https://motion.dev/docs/react-use-animate) 
*   [useAnimationFrame](https://motion.dev/docs/react-use-animation-frame) 
*   [useDragControls](https://motion.dev/docs/react-use-drag-controls) 
*   [useInView](https://motion.dev/docs/react-use-in-view) 
*   [usePageInView](https://motion.dev/docs/react-use-page-in-view) 
*   [useReducedMotion](https://motion.dev/docs/react-use-reduced-motion) 

### Integrations

*   [Framer](https://motion.dev/docs/framer) 
*   [Figma](https://motion.dev/docs/figma) 
*   [Tailwind CSS](https://motion.dev/docs/react-tailwind) 
*   [Base UI](https://motion.dev/docs/base-ui) 
*   [Radix](https://motion.dev/docs/radix) 

### Guides

*   [Installation](https://motion.dev/docs/react-installation) 
*   [Upgrade guide](https://motion.dev/docs/react-upgrade-guide) 
*   [Accessibility](https://motion.dev/docs/react-accessibility) 
*   [Reduce bundle size](https://motion.dev/docs/react-reduce-bundle-size) 

[React](https://motion.dev/docs/react)

[Motion+ Exclusive](https://motion.dev/plus)

Copy page

AnimateNumber
=============

This feature is available with [Motion+](https://motion.dev/plus)

Checking Motion+ status…

AnimateNumber

is exclusive to Motion+

290+ examples & 40+ tutorials

Premium APIs

Motion Studio editing tools

`alpha`

Discord community

Early access

Lifetime updates

[Get Motion+ for instant access](https://motion.dev/plus)

One-time payment, lifetime updates

Already joined?

[Login](https://plus.motion.dev/login?redirect=)

`AnimateNumber` is a lightweight (2.5kb) React component for creating beautiful number animations with Motion. It's perfect for counters, dynamic pricing, countdowns, and more.

<AnimateNumber>{count}</AnimateNumber>

Built on top of Motion's powerful layout animations, `AnimateNumber` allows you to leverage all of Motion's existing transition settings, like `spring` and `tween`, to create fluid and engaging effects.

`AnimateNumber` is exclusive to [Motion+](https://motion.dev/plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

[Features](https://motion.dev/docs/react-animate-number#features)
-----------------------------------------------------------------

*   **Built on Motion:**Leverages Motion's robust animation engine, allowing you to use familiar `transition` props like `spring`, `duration`, and `ease`.

*   **Lightweight:** Adds only 2.5kb on top of Motion.

*   **Advanced formatting:** Uses the built-in `Intl.NumberFormat` for powerful, locale-aware number formatting (e.g., currency, compact notation).

*   **Customisable:**Provides distinct CSS classes for each part of the number (prefix, integer, fraction, suffix) for full styling control.

[Install](https://motion.dev/docs/react-animate-number#install)
---------------------------------------------------------------

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev/). You need to be a [Motion+ member](https://motion.dev/plus) to generate a private token.

npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.10.0&token=YOUR_AUTH_TOKEN"

[Usage](https://motion.dev/docs/react-animate-number#usage)
-----------------------------------------------------------

`AnimateNumber` accepts a single child, a number.

<AnimateNumber>300</AnimateNumber>

When this number changes, it'll animate to its latest value.

import { AnimateNumber } from "motion-plus/react"

function Counter() {
  const [count, setCount] = useState(0)

  return (
    <>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <AnimateNumber>{count}</AnimateNumber>
    </>
  )
}

### [Customise animation](https://motion.dev/docs/react-animate-number#customise-animation)

The `transition` prop accepts Motion for React's [transition options](https://motion.dev/docs/react-transitions).

<AnimateNumber transition={{ type: "spring" }}>

`transition` accepts value-specific transition settings, so it's possible to set specific transitions for `layout`, `y` and `opacity`:

<AnimateNumber transition={{
  layout: { duration: 0.3 },
  opacity: { ease: "linear" },
  y: { type: "spring", visualDuration: 0.4, bounce: 0.2 }
}}>

Related topics
--------------

*   [### Layout animation Smoothly animate layout changes and create shared element animations.](https://motion.dev/docs/react-layout-animations)  

*   [### AnimateNumber examples See all examples & tutorials, with full copy & paste source code.](https://motion.dev/examples?platform=react&search=AnimateNumber)

Previous

[Reorder](https://motion.dev/docs/react-reorder)

Next

[Carousel](https://motion.dev/docs/react-carousel)

Motion+

Level up your animations with Motion+
-------------------------------------

Unlock the full vault of 330+ Motion examples, 100+ tutorials, premium APIs, private Discord and GitHub, and powerful Motion Studio animation editing tools for your IDE.

[Get Motion+](https://motion.dev/plus)

One-time payment, lifetime updates.

![Image 2](https://framerusercontent.com/images/dvcUQX74Mh8wmjKmhIoM2Yli4.png?width=2000&height=2000)

[![Image 3](https://framerusercontent.com/images/a6LWvnzoehr1qy4ywp7QSBDq5iQ.jpg?width=290&height=223) AI-ready animations Make your LLM an animation expert with 330+ pre-built examples available via MCP.](https://motion.dev/plus)

Motion is supported by the best in the industry.

[](https://framer.link/6ogjBZd)

[](https://cursor.com/)

[](https://linear.app/)

[animations.dev](https://animations.dev/)

[](https://figma.com/)

[](https://clerk.com/?utm_campaign=motion)

[](https://www.sanity.io/)

[](https://www.greptile.com/?utm_source=motion&utm_medium=sponsorship)

##### Stay in the loop

Subscribe for the latest news & updates.

Subscribe

![Image 4](https://framerusercontent.com/images/asanCTGT7yglcSpcyzjAmzwnJw.png?scale-down-to=1000&width=2000&height=767)

Site
----

*   [Blog](https://motion.dev/)
*   [Docs](https://motion.dev/docs)
*   [Examples](https://motion.dev/examples)
*   [Magazine](https://motion.dev/magazine)
*   [Motion+](https://motion.dev/plus)
*   [Studio](https://motion.dev/studio)
*   [Support](https://motion.dev/support)
*   [Tutorials](https://motion.dev/tutorials)

###### Most Popular

*   [React animation](https://motion.dev/docs/react-animation)
*   [Layout animation](https://motion.dev/docs/react-layout-animations)
*   [SVG animation](https://motion.dev/docs/react-svg-animation)
*   [Motion component](https://motion.dev/docs/react-motion-component)
*   [GSAP vs Motion](https://motion.dev/docs/gsap-vs-motion)

Premium APIs
------------

*   [Carousel](https://motion.dev/docs/react-carousel)
*   [Custom Cursor](https://motion.dev/docs/cursor)
*   [Number animations](https://motion.dev/docs/react-animate-number)
*   [Ticker](https://motion.dev/docs/react-ticker)
*   [Typewriter](https://motion.dev/docs/react-typewriter)

###### Docs

*   [JavaScript](https://motion.dev/docs/quick-start)
*   [React](https://motion.dev/docs/react)
*   [Vue](https://motion.dev/docs/vue)
*   [Studio](https://motion.dev/docs/studio)

Social
------

*   [Discord](https://motion.dev/plus)
*   [GitHub](https://github.com/motiondivision/motion)
*   [X/Twitter](https://x.com/motiondotdev)
*   [YouTube](https://www.youtube.com/@motiondotdev)

Latest version:

[12.35.2](https://motion.dev/changelog)

Motion+

[Login](https://plus.motion.dev/login)

[Register](https://plus.motion.dev/register)

[Upgrade](https://motion.dev/plus)
