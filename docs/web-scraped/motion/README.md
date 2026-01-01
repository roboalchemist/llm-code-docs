# Source: https://motion.dev

# Motion - Animation Library for React, JavaScript, and Vue

Motion (formerly known as Framer Motion) is a free and open-source animation library that enables developers to create smooth, production-grade animations. It supports React, JavaScript, and Vue with a simple yet powerful declarative API.

## Key Features

- **GPU-Accelerated Animations**: Hybrid engine combining JavaScript with native browser APIs for 120fps, GPU-accelerated animations
- **React Components**: The `motion` component wraps HTML and SVG elements with animation capabilities
- **Gesture Support**: Built-in support for hover, tap, pan, drag, focus, and in-view gestures
- **Layout Animations**: Animate element size and position changes with FLIP animations and shared element transitions
- **Scroll Animations**: Create scroll-linked animations with ease
- **Motion Values**: Track animated values without triggering React re-renders for optimal performance
- **Variants**: Orchestrate complex animation sequences with named animation targets
- **TypeScript Support**: Fully typed with TypeScript for better developer experience
- **Spring Physics**: Natural, kinetic animations with configurable spring parameters

## Installation

### Package Manager

Motion can be installed via npm, Yarn, or pnpm:

```bash
npm install motion
```

### Yarn

```bash
yarn add motion
```

### pnpm

```bash
pnpm add motion
```

### CDN via jsDelivr

```html
<script src="https://cdn.jsdelivr.net/npm/motion"></script>
```

### Requirements

Motion requires React 18.2 or higher for React support.

## Getting Started

### React Installation

```jsx
import { motion } from "motion/react"
```

### React Server Components (Next.js)

```jsx
import * as motion from "motion/react-client"
```

### JavaScript Installation

```javascript
import { animate, scroll } from "motion"
```

### Your First Animation

The `motion` component is the core API. It's a DOM element supercharged with animation capabilities:

```jsx
import { motion } from "motion/react"

export default function App() {
  return (
    <motion.ul
      animate={{ rotate: 360 }}
      transition={{ duration: 2 }}
    />
  )
}
```

When values in the `animate` prop change, the component will animate smoothly.

## Core Concepts

### Motion Component

There's a `motion` component for every HTML and SVG element:

```jsx
<motion.div />
<motion.a href="#" />
<motion.circle cx={0} />
<motion.button />
```

Key characteristics:
- Performs 120fps animations without triggering React re-renders
- Can use motion values with `style` prop to further avoid re-renders
- Fully compatible with React Server Components (RSC)
- Works exactly like normal HTML/SVG components

### Animation Props

Motion components accept special animation props:

```jsx
<motion.div
  // Animate when this value changes
  animate={{ scale: 2 }}

  // Fade in when element enters viewport
  whileInView={{ opacity: 1 }}

  // Animate layout changes
  layout

  // Configure animation timing
  transition={{ duration: 0.5 }}
/>
```

### Transitions

A transition defines the type of animation used when animating between values:

- **Tween**: Linear interpolation with customizable easing
- **Spring**: Physics-based animation with natural motion
- **Inertia**: Decelerating animation, useful for gestures

```jsx
<motion.div
  animate={{ x: 100 }}
  transition={{
    type: "spring",
    stiffness: 100,
    damping: 10
  }}
/>
```

### Motion Values

Motion values track the state and velocity of animated values without triggering React re-renders:

```jsx
import { useMotionValue } from "motion/react"

const x = useMotionValue(0)

useEffect(() => {
  // Won't trigger a re-render!
  const timeout = setTimeout(() => x.set(100), 1000)
  return () => clearTimeout(timeout)
}, [])

return <motion.div style={{ x }} />
```

## Animation Capabilities

### Basic Animation

```jsx
<motion.div animate={{ rotate: 360, opacity: 0 }} />
```

### Hover Animation

```jsx
<motion.button
  whileHover={{
    scale: 1.2,
    transition: { duration: 1 },
  }}
  whileTap={{ scale: 0.9 }}
>
  Hover me
</motion.button>
```

### Tap/Press Animation

```jsx
<motion.div
  whileTap={{
    scale: 0.95,
  }}
/>
```

### Drag Animation

```jsx
<motion.div
  drag
  whileDrag={{ scale: 1.1 }}
/>
```

### Drag with Constraints

```jsx
<motion.div
  drag
  dragConstraints={{
    left: -100,
    right: 100,
    top: -100,
    bottom: 100
  }}
/>
```

### Drag Controls

```jsx
import { useDragControls } from "motion/react"

const controls = useDragControls()

return (
  <motion.div
    drag
    dragControls={controls}
  />
)
```

### Focus Animation

```jsx
<motion.input
  whileFocus={{
    scale: 1.1,
    boxShadow: "0 0 10px rgba(0,0,0,0.2)"
  }}
/>
```

## Gesture Animation

Motion extends React's event listeners with powerful UI gestures:

- **Hover**: `whileHover` - Animate while hovering
- **Tap**: `whileTap` - Animate while tapping/clicking
- **Pan**: `onPan`, `onPanStart`, `onPanEnd` - Track pan movement
- **Drag**: `drag`, `whileDrag` - Drag with constraints
- **Focus**: `whileFocus` - Animate on focus
- **InView**: `whileInView` - Animate when element enters viewport

## Layout Animations

Motion makes it simple to animate an element's size and position:

```jsx
<motion.div
  layout
  onClick={() => setIsExpanded(!isExpanded)}
>
  {isExpanded ? <ExpandedContent /> : null}
</motion.div>
```

### Shared Layout Animation (Magic Motion)

Create seamless transitions between separate elements:

```jsx
<motion.div layoutId="expandableBox">
  {isExpanded ? <FullBox /> : <CompactBox />}
</motion.div>
```

### Layout Groups

Group layout animations together:

```jsx
import { LayoutGroup } from "motion/react"

<LayoutGroup>
  <motion.div layout onClick={...} />
  <motion.div layout onClick={...} />
</LayoutGroup>
```

## Scroll Animations

### Scroll-Linked Animations

Use `whileInView` to animate elements as they enter the viewport:

```jsx
<motion.div
  whileInView={{ opacity: 1, y: 0 }}
  initial={{ opacity: 0, y: 100 }}
/>
```

### useScroll Hook

Create scroll-linked animations with pixel-perfect control:

```jsx
import { useScroll, useTransform, motion } from "motion/react"

const { scrollY } = useScroll()
const opacity = useTransform(scrollY, [0, 100], [1, 0])

return <motion.div style={{ opacity }} />
```

## SVG Animations

Animate SVG properties including paths, transforms, and more:

```jsx
<motion.svg viewBox="0 0 100 100">
  <motion.circle
    cx={50}
    cy={50}
    r={40}
    animate={{
      r: [40, 50, 40],
    }}
    transition={{ repeat: Infinity }}
  />
</motion.svg>
```

### Path Drawing

Animate SVG paths with `pathLength`:

```jsx
<motion.path
  d="M10,10 L90,90"
  strokeDasharray="0 1"
  animate={{
    strokeDasharray: "1 0",
  }}
/>
```

### Path Morphing

Morph between different SVG paths:

```jsx
<motion.path
  d={isOpen ? pathOpen : pathClosed}
  animate={{
    d: isOpen ? pathOpen : pathClosed
  }}
/>
```

## Variants

Variants are named animation targets that can be reused and orchestrated:

```jsx
const variants = {
  hidden: { opacity: 0, y: -20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { staggerChildren: 0.1 }
  },
  exit: { opacity: 0, y: 20 }
}

const itemVariants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 }
}

<motion.ul
  initial="hidden"
  animate="visible"
  variants={variants}
>
  {items.map(item => (
    <motion.li
      key={item.id}
      variants={itemVariants}
    >
      {item.name}
    </motion.li>
  ))}
</motion.ul>
```

## Components

### AnimatePresence

Animate components as they mount and unmount:

```jsx
import { AnimatePresence } from "motion/react"

<AnimatePresence>
  {isVisible && (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    />
  )}
</AnimatePresence>
```

### MotionConfig

Set animation configuration for a component tree:

```jsx
import { MotionConfig } from "motion/react"

<MotionConfig transition={{ duration: 0.2 }}>
  <motion.div animate={{ x: 100 }} />
</MotionConfig>
```

### LazyMotion

Reduce bundle size by lazy-loading Motion features:

```jsx
import { LazyMotion, domAnimation, motion } from "motion/react"

<LazyMotion features={domAnimation}>
  <motion.div animate={{ x: 100 }} />
</LazyMotion>
```

### Reorder

Reorder list items with drag:

```jsx
import { Reorder } from "motion/react"

const [items, setItems] = useState([...])

<Reorder.Group axis="y" values={items} onReorder={setItems}>
  {items.map(item => (
    <Reorder.Item key={item.id} value={item}>
      {item.name}
    </Reorder.Item>
  ))}
</Reorder.Group>
```

## Hooks

### useMotionValue

Track animated values without triggering re-renders:

```jsx
import { useMotionValue } from "motion/react"

const x = useMotionValue(0)
const y = useMotionValue(0)
```

### useMotionTemplate

Combine motion values into CSS values:

```jsx
import { useMotionTemplate, useMotionValue } from "motion/react"

const x = useMotionValue(0)
const background = useMotionTemplate`rgb(${x}, 0, 0)`
```

### useTransform

Transform motion values into new values:

```jsx
import { useScroll, useTransform } from "motion/react"

const { scrollY } = useScroll()
const opacity = useTransform(scrollY, [0, 100], [1, 0])
```

### useVelocity

Track the velocity of a motion value:

```jsx
import { useMotionValue, useVelocity } from "motion/react"

const x = useMotionValue(0)
const xVelocity = useVelocity(x)
```

### useScroll

Get scroll progress and velocity:

```jsx
import { useScroll } from "motion/react"

const { scrollY, scrollYProgress } = useScroll()
```

### useSpring

Create spring-based motion values:

```jsx
import { useSpring } from "motion/react"

const springValue = useSpring(0, {
  stiffness: 100,
  damping: 10
})
```

### useAnimate

Manually trigger animations:

```jsx
import { useAnimate } from "motion/react"

const [scope, animate] = useAnimate()

await animate(scope.current, { opacity: 0 })
```

### useAnimationFrame

Run a callback on every animation frame:

```jsx
import { useAnimationFrame } from "motion/react"

useAnimationFrame((time) => {
  ref.current.style.transform = `rotateY(${time}deg)`
})
```

### useInView

Detect when an element enters the viewport:

```jsx
import { useInView } from "motion/react"

const ref = useRef(null)
const isInView = useInView(ref)
```

### useReducedMotion

Respect prefers-reduced-motion:

```jsx
import { useReducedMotion } from "motion/react"

const shouldReduceMotion = useReducedMotion()
```

## Premium APIs (Motion+)

Motion+ is a premium subscription offering additional features:

- **AnimateNumber**: Beautiful number ticker and countdown animations
- **Carousel**: Advanced carousel with multiple pagination styles
- **Cursor**: Create custom cursor and follow-along effects
- **Ticker**: Create animated ticker/news feed components
- **Typewriter**: Typewriter text animation effects
- **300+ Examples**: Copy-paste ready code examples
- **Motion Studio**: VS Code animation editor integration
- **Private Discord & GitHub**: Community and support access

## Performance Optimization

### Performance Characteristics

- `motion` components animate without triggering React re-renders
- Using motion values instead of React state avoids re-renders
- GPU-accelerated transforms and opacity for optimal performance
- Supports 120fps animations with hybrid JavaScript/native engine

### Lazy Motion

Reduce bundle size by lazy-loading Motion features:

```jsx
import { LazyMotion, domAnimation } from "motion/react"

<LazyMotion features={domAnimation}>
  {/* Motion components here */}
</LazyMotion>
```

## Accessibility

### Respect Prefers-Reduced-Motion

```jsx
import { useReducedMotion } from "motion/react"

const shouldReduceMotion = useReducedMotion()

<motion.div
  animate={{ x: shouldReduceMotion ? 0 : 100 }}
/>
```

## Framework Integration

Motion provides integration guides for:

- **Framer**: Visual design-to-code export
- **Figma**: Figma plugin for animation creation
- **Next.js**: Works out of the box with server components
- **Vite**: Zero-configuration support
- **Tailwind CSS**: Full compatibility
- **Base UI**: Component library integration
- **Radix UI**: Accessible component library integration

## Examples

### Fade In

```jsx
<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: 0.5 }}
/>
```

### Slide In

```jsx
<motion.div
  initial={{ x: -100 }}
  animate={{ x: 0 }}
  transition={{ type: "spring", stiffness: 100 }}
/>
```

### Bounce

```jsx
<motion.div
  animate={{ y: [0, -10, 0] }}
  transition={{ repeat: Infinity, duration: 1 }}
/>
```

### Scale on Hover

```jsx
<motion.button
  whileHover={{ scale: 1.1 }}
  whileTap={{ scale: 0.95 }}
/>
```

### Staggered List

```jsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
}

const item = {
  hidden: { opacity: 0, y: 10 },
  show: { opacity: 1, y: 0 }
}

<motion.ul
  variants={container}
  initial="hidden"
  animate="show"
>
  {items.map(i => (
    <motion.li key={i.id} variants={item} />
  ))}
</motion.ul>
```

### Parallax Scroll

```jsx
const { scrollY } = useScroll()
const yRange = useTransform(scrollY, [0, 500], [0, -100])

<motion.div style={{ y: yRange }} />
```

## Resources

- **Official Website**: https://motion.dev
- **Documentation**: https://motion.dev/docs
- **GitHub Repository**: https://github.com/motiondivision/motion
- **Examples**: https://motion.dev/docs/examples
- **Tutorials**: https://motion.dev/docs/tutorials
- **Motion Studio**: https://motion.dev/docs/studio

## Version

Latest version: 12.23.26+

## License

Motion is free and open source. Check the GitHub repository for license details.

## Support

- **Community Examples**: https://animations.dev
- **Official Tutorials**: https://motion.dev/docs/tutorials
- **GitHub Issues**: https://github.com/motiondivision/motion/issues
- **Motion+**: Premium features and community support
