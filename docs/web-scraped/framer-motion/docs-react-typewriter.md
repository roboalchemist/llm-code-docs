# Source: https://motion.dev/docs/react-typewriter

Title: Typewriter: Realistic typing animations in React | Motion

URL Source: https://motion.dev/docs/react-typewriter

Published Time: Fri, 13 Mar 2026 09:31:07 GMT

Markdown Content:
Typewriter: Realistic typing animations in React | Motion
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

Typewriter
==========

This feature is available with [Motion+](https://motion.dev/plus)

Checking Motion+ status…

Typewriter

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

`Typewriter` is a 1.3kb React component for creating realistic typewriter animations. It emulates natural human typing behaviour, handles dynamic content (with intelligent backspacing), and provides full playback control for scroll-triggered effects. All while ensuring screen reader accessibility.

<Typewriter>Hello world!</Typewriter>

`Typewriter` is exclusive to [Motion+](https://motion.dev/plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

[Features](https://motion.dev/docs/react-typewriter#features)
-------------------------------------------------------------

*   **Natural animation:**Typing speeds and variance emulate real-world behaviour.

*   **Playback control:** Easily play and pause animations, perfect for scroll-triggered animations.

*   **Accessible:** Correct ARIA labels for screen reader compatibility.

*   **Reactive:** Will animate with backspace and typing to the latest provided value.

*   **Customisable:**Control everything from typing speed and variance to cursor style and blink speed.

[Install](https://motion.dev/docs/react-typewriter#install)
-----------------------------------------------------------

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev/). You need to be a [Motion+ member](https://motion.dev/plus) to generate a private token.

npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.8.0&token=YOUR_AUTH_TOKEN"

[Usage](https://motion.dev/docs/react-typewriter#usage)
-------------------------------------------------------

Import from `"motion-plus/react"`.

import{Typewriter}from"motion-plus/react"

By passing a string as the `Typewriter` child, it will animate that text in character by character.

<Typewriter>Hello world!</Typewriter>

### [Dynamic content](https://motion.dev/docs/react-typewriter#dynamic-content)

When the `children` prop changes, `Typewriter` will intelligently animate from the old text to the new text. By default, it backspaces character by character to the point of difference and then types out the new content.

By default, each character will be backspaced individually. Using the `backspace` prop we can also backspace each word/special character:

<Typewriter backspace="word">{text}</Typewriter>

Or remove all the mismatching content immediately:

<Typewriter backspace="all">{text}</Typewriter>

### [Adjust speed](https://motion.dev/docs/react-typewriter#adjust-speed)

The animation will emulate "normal" real-world typing speeds, based on real research. It's also possible to set speed as `"fast"`, `"slow"`, or a custom interval (in milliseconds).

<Typewriter speed="slow">Hello world!</Typewriter>

By default, the typing speed will vary naturally per character, based on the type of content being "typed".

For example, typing will slow down while typing long words, while at the start/end of a word, when using punctuation, or when using uncommon character combinations.

This can be configured with the `variance` prop. This is a `0`-`1` factor applied to `speed`, to create a range of speeds that we can randomly select between.

So for instance if we want no variance then we can set this to `0`.

<Typewriter variance={0}>Hello world!</Typewriter>

Or to have some variance it could be set to `0.5`:

<Typewriter variance={0.5}>Hello world!</Typewriter>

### [](https://motion.dev/docs/react-typewriter#)

Related topics
--------------

*   [### Motion component Animate elements with a declarative API. Supports variants, gestures, and layout animations.](https://motion.dev/docs/react-motion-component)  

*   [### Typewriter examples See all examples & tutorials, with full copy & paste source code.](https://motion.dev/examples?platform=react&search=Typewriter)

Previous

[Ticker](https://motion.dev/docs/react-ticker)

Next

[Motion values overview](https://motion.dev/docs/react-motion-value)

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
