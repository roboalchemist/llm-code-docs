# Source: https://motion.dev/docs/react-ticker

Title: Ticker — Infinite scroll marquee animation | Motion

URL Source: https://motion.dev/docs/react-ticker

Published Time: Fri, 13 Mar 2026 09:33:20 GMT

Markdown Content:
Ticker — Infinite scroll marquee animation | Motion
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

Ticker
======

This feature is available with [Motion+](https://motion.dev/plus)

Checking Motion+ status…

Ticker

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

The `Ticker` component for React creates performant, flexible, and fully accessible ticker and marquee animations. It's perfect for showcasing logos, photos, testimonials, news headlines, and more.

`Ticker`'s simple API makes these infinitely-scrolling animations easy to build.

<Ticker items={items}/>

It intelligently clones only the minimum number of items needed to create a seamless loop, ensuring optimal performance. Because it's powered by Motion, you can take full manual control with a [motion value](https://motion.dev/docs/react-motion-value) to create scroll-driven or draggable effects.

`Ticker` is exclusive to [Motion+](https://motion.dev/plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

[Features](https://motion.dev/docs/react-ticker#features)
---------------------------------------------------------

`Ticker` is a production-ready component built with performance and accessibility at its core.

*   **Lightweight:**Just `+2.1kb` on top of Motion for React.

*   **Accessible:** Automatic support for "reduced motion" and intelligent keyboard focus-trapping means your site is inclusive for all users.

*   **Flexible:**Animate horizontally or vertically. Control the animation with velocity, scroll position, or drag gestures.

*   **Performant:**Creates the absolute minimum number of cloned elements required to fill the viewport. [Read more about Motion+ Ticker's unique renderer.](https://motion.dev/magazine/building-the-ultimate-ticker) More efficient and maintainable than hand-rolled CSS tickers.

*   **Full-width overflow:** Easily create tickers that are contained within your layout but visually extend to the edges of the viewport.

*   **RTL-compatible:**Automatically adapts to RTL layouts.

[Install](https://motion.dev/docs/react-ticker#install)
-------------------------------------------------------

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev/). You need to be a [Motion+ member](https://motion.dev/plus) to generate a private token.

npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.0.2&token=YOUR_AUTH_TOKEN"

[Usage](https://motion.dev/docs/react-ticker#usage)
---------------------------------------------------

`Ticker` accepts on mandatory prop, `items`. This is a list of valid React nodes (which can be components, strings or numbers):

const items = [
  <span>One</span>,
  <span>Two</span>,
  <span>Three</span>
]

return <Ticker items={items} />

### [Direction](https://motion.dev/docs/react-ticker#direction)

By default, tickers will scroll horizontally, but via the `axis` prop we can lay out and animate items on the `"y"` axis too.

<Ticker items={items} axis="y" />

### [Adjust speed](https://motion.dev/docs/react-ticker#adjust-speed)

Setting the `velocity` prop (in pixels per second) will change the speed and direction of the ticker animation.

<Ticker items={items} velocity={100} />

Flipping this to a negative value will reverse the direction of the ticker.

<Ticker items={items} velocity={-100} />

Whereas setting it to `0` will stop all motion.

<Ticker items={items} velocity={0} />

Related topics
--------------

*   [### React animation Create React animation with Motion components. Learn variants, gestures, and keyframes.](https://motion.dev/docs/react-animation)  
*   [### Motion component Animate elements with a declarative API. Supports variants, gestures, and layout animations.](https://motion.dev/docs/react-motion-component)  
*   [### Motion values overview Composable animatable values that can updated styles without re-renders.](https://motion.dev/docs/react-motion-value)  

*   [### Ticker examples See all examples & tutorials, with full copy & paste source code.](https://motion.dev/examples?platform=react&search=Ticker)

Previous

[ScrambleText](https://motion.dev/docs/react-scramble-text)

Next

[Typewriter](https://motion.dev/docs/react-typewriter)

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
