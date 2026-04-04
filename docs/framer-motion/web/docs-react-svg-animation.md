# Source: https://motion.dev/docs/react-svg-animation

Title: SVG Animation in React — Paths, Morph & Line Drawing | Motion

URL Source: https://motion.dev/docs/react-svg-animation

Published Time: Fri, 13 Mar 2026 09:28:50 GMT

Markdown Content:
Motion makes React SVG animation straightforward. In this guide, we'll learn how to make line drawing animations, path morphing animations, animate `viewBox` and more.

[Overview](https://motion.dev/docs/react-svg-animation#overview)
----------------------------------------------------------------

SVG animations are performed via the `motion`[component](https://motion.dev/docs/react-motion-component). There's a `motion` component for every SVG element (e.g. `<motion.svg>`, `<motion.path>`, `<motion.circle>`, and even filters like `<motion.feTurbulence>` and `<motion.feDisplacementMap>`).

<motion.svg>

<motion.circle/>

</motion.svg>

A `motion` component can animate `style`, as normal:

<motion.circle

style={{fill:"#00f"}}

animate={{fill:"#f00"}}

/>

But it can also animate attributes:

<motion.circle

cx={0}

animate={{cx:50}}

/>

### [Animate `viewBox`](https://motion.dev/docs/react-svg-animation#animate-viewbox)

The `motion.svg` component can additionally animate `viewBox`. This is especially useful for easy panning animations:

<motion.svg

viewBox="0 0 200 200"

animate={{viewBox:"100 0 200 200"}}// 100px to the right

/>

Or zoom in/out animations:

<motion.svg
  viewBox="0 0 200 200"
  animate={{ viewBox: "-100 -100 300 300" }} // Zoom out
/>

### [Transforms](https://motion.dev/docs/react-svg-animation#transforms)

SVG transforms work differently to CSS transforms. When we define a CSS transform, the default origin is **relative to the element itself.** So for instance, this `div` will rotate around its center point, as you'd intuitively expect:

<motion.div style={{ rotate: 90 }} />

With SVGs, the transform point is relative to the top/left corner of the `viewBox`, which is less intuitive. Motion changes this behaviour so SVGs work the same as normal elements. Therefore, this:

<motion.rect style={{ rotate: 90 }} />

Will also rotate the `rect` element around its center point.

The default behaviour can be restored by explicitly setting an element's `transformBox` style:

<motion.rect style={{ rotate: 90, transformBox: "view-box" }} />

### [`x`/`y`/`scale` attributes](https://motion.dev/docs/react-svg-animation#x-y-scale-attributes)

`motion` components provide shorthands for `x`, `y`, and `scale` transforms:

<motion.div animate={{ x: 100 }} />

With SVG components, these will still render via the `style` tag. This is usually fine, but some SVG components accept `x`, `y`, and `scale` attributes also. You can target these via animation props using `attrX`, `attrY` and `attrScale` respectively:

<motion.rect attrX={0} animate={{ attrX: 100 }} />

### [Passing `MotionValue`](https://motion.dev/docs/react-svg-animation#passing-motionvalue)

[Motion values](https://motion.dev/docs/react-motion-value) should be passed via `style`, when animating regular styles, or via the component's attribute where appropriate:

const cx = useMotionValue(100)
const opacity = useMotionValue(1)

return <motion.rect cx={cx} style={{ opacity }} />

[Line drawing](https://motion.dev/docs/react-svg-animation#line-drawing)
------------------------------------------------------------------------

Motion simplifies the creation of “hand-drawn” line animations using three special values. Each is set as a `0`-`1` progress value, where `1` is the total length of the line:

*   `pathLength`: total drawn length

*   `pathSpacing`: length between segments

*   `pathOffset`: where the segment starts

These values work on `path`, `circle`, `ellipse`, `line`, `polygon`, `polyline`, `rect`.

<motion.path
  d={d}
  initial={{ pathLength: 0 }}
  animate={{ pathLength: 1 }}
/>

[Path morphing](https://motion.dev/docs/react-svg-animation#path-morphing)
--------------------------------------------------------------------------

It's possible to also animate the shape of a `path` via its `d` attribute.

<motion.path
  d="M 0,0 l 0,10 l 10,10"
  animate={{ d: "M 0,0 l 10,0 l 10,10" }}
/>

This works natively in Motion **as long as the two paths are similar**. You can see in the example above that each path has the same number and type of path instructions.

For interpolating between very different paths, you can incorporate a third-party path mixer like [Flubber](https://www.npmjs.com/package/flubber):

[Drag gesture](https://motion.dev/docs/react-svg-animation#drag-gesture)
------------------------------------------------------------------------

SVG elements can be made draggable in the same way as their HTML counterparts, using the `drag` prop.

<motion.circle drag />

However, it's possible that an SVG is rendered with a `viewBox` that is different from its rendered size.

For example, this SVG has a `viewBox` of `100px` width and height, vs a rendered size of `200px`:

<svg viewBox="0 0 100 100" style={{ width: 200, height: 200 }} />

This will conflict with the drag gesture. To fix, we can use the `MotionConfig``transformPagePoint` prop to rescale pointer movements:

import { motion, MotionConfig, transformViewBoxPoint } from "motion/react"

function Component() {
  const ref = useRef(null)

  return (
    <MotionConfig transformPagePoint={transformViewBoxPoint(ref)}>
      <svg ref={ref} viewBox="0 0 100 100" style={{ width: 200, height: 200 }}>
        <motion.circle drag />
      </svg>
    </MotionConfig>
  )
}
