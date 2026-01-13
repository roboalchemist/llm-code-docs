# CSS Animation Libraries Quick Reference (2026)

Fast lookup guide for CSS animation libraries, motion frameworks, and animation tools.

## By Category

### Pure CSS (No JavaScript)
| Library | Size | Setup | Use Case |
|---------|------|-------|----------|
| **Animate.css** | 7KB | CDN/npm | 50+ pre-made effects, easy class-based animations |
| **Animista** | 0KB | Web tool | Custom CSS generator, copy-paste implementation |
| **Magic Animations** | Small | CDN | Lightweight vanilla CSS effects |
| **Native CSS Scroll-Driven** | 0KB | Native | Browser-native scroll animations (Chrome 115+, Safari 26+) |

### Lightweight JavaScript (<15KB)
| Library | Size | Framework | Use Case |
|---------|------|-----------|----------|
| **Motion One** | 4KB | Any | Spring physics, WAAPI-based, modern apps |
| **Popmotion** | 5KB | Any | Physics-based, gestures, functional API |
| **AOS** | 7KB | Any | Scroll-triggered fade/flip/slide effects |
| **Anime.js** | 14KB | Any | Simple syntax, elegant UI animations |
| **LDRS** | Small | React | Loading spinners and loaders |

### React-Focused Animation
| Library | Size | Key Feature | Best For |
|---------|------|-------------|----------|
| **Framer Motion** | 40KB | Gestures, variants, fluid | React apps, gesture-driven UI |
| **Chakra UI** | Variable | Framer Motion-powered | Component library with animations |
| **Motion One** | 4KB | WAAPI-based, lightweight | Modern React, performance-critical |

### Professional/Enterprise
| Library | Size | Use Case | Best For |
|---------|------|----------|----------|
| **GSAP (core)** | 30KB | Timeline-based, easing | Complex animations, industry standard |
| **GSAP + ScrollTrigger** | 60KB | Scroll-linked, pinning | Scroll storytelling, parallax effects |
| **GSAP + Observer** | Premium | Gesture-aware | Drag, swipe, real-time interactions |
| **GSAP + Draggable** | Premium | Interactive drag mechanics | Draggable UI elements |

### 3D & Graphics
| Library | Size | Type | Use Case |
|---------|------|------|----------|
| **Three.js** | 200KB | WebGL | 3D graphics, interactive visualizations |
| **react-three-fiber** | Included | React + Three.js | React 3D projects, declarative approach |
| **SVG Morphing (GSAP)** | Premium | SVG animations | Logo morphing, diagram animations |

### Tailwind CSS Integration
| Tool | Size | Use Case |
|------|------|----------|
| **TAOS** | 600B | Scroll-triggered with Tailwind |
| **Tailwind @keyframes** | Built-in | Custom keyframes, animations utility |

---

## By Use Case

### Simple, Quick Animations
1. **Animate.css** - Just add classes
2. **Animista** - Generate and copy CSS
3. **Magic Animations** - Lightweight vanilla CSS

**Installation:**
```bash
npm install animate.css
# or use CDN: https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css
```

### React Component Interactions
1. **Framer Motion** - Full-featured, gestures
2. **Motion One** - Lightweight alternative
3. **Chakra UI** - Pre-animated components

**Installation:**
```bash
npm install framer-motion
# or
npm install motion
```

### Scroll-Triggered Effects
1. **GSAP ScrollTrigger** - Most powerful
2. **AOS** - Simple, lightweight
3. **Native CSS Scroll-Driven** - Modern browsers only
4. **TAOS** - Tailwind CSS integration

**Installation:**
```bash
# GSAP
npm install gsap gsap/ScrollTrigger

# AOS
npm install aos

# TAOS
npm install taos
```

### Complex Timelines & Sequences
1. **GSAP** - Industry standard
2. **Anime.js** - Lighter alternative
3. **Popmotion** - Functional approach

**Installation:**
```bash
npm install gsap
# or
npm install animejs
# or
npm install popmotion
```

### 3D Graphics & Visualization
1. **Three.js** - Standalone or with React
2. **react-three-fiber** - React declarative approach

**Installation:**
```bash
npm install three
npm install three @react-three/fiber
```

### Gesture-Driven Interactions
1. **Framer Motion** - Hover, tap, drag, pan
2. **GSAP Observer** - Scroll, drag, swipe detection
3. **Popmotion** - Physics-based gestures

### Loading States & Spinners
1. **Whirl** - Pure CSS spinners
2. **LDRS** - CSS loaders with React support
3. **Tailwind CSS** - Built-in spin/pulse animations

### Text Animations
1. **Moving Letters** - Text-specific effects
2. **Anime.js** - Text morphing and effects
3. **GSAP TextPlugin** - Advanced text animation

---

## Bundle Size Comparison

```
Motion One:          4KB    🟢 Minimal
Popmotion:           5KB    🟢 Minimal
AOS:                 7KB    🟢 Minimal
Animate.css:         7KB    🟢 Minimal
Anime.js:           14KB    🟢 Small
GSAP (core):        30KB    🟡 Medium
Framer Motion:      40KB    🟡 Medium
Three.js:          200KB    🔴 Large
```

---

## Browser Support Matrix

| Feature | Chrome | Safari | Firefox | Edge | IE 11 |
|---------|--------|--------|---------|------|-------|
| CSS Animations | ✓ | ✓ | ✓ | ✓ | ✓ |
| Scroll-Driven CSS | 115+ | 26+ | TBD | 115+ | ✗ |
| Web Animations API | ✓ | ✓ | ✓ | ✓ | ✗ |
| SVG Animations | ✓ | ✓ | ✓ | ✓ | Partial |
| WebGL (Three.js) | ✓ | ✓ | ✓ | ✓ | ✗ |
| Intersection Observer | ✓ | 12+ | 55+ | ✓ | ✗ |

---

## Selection Flowchart

```
Do you need animations?
│
├─ Pure CSS only?
│  └─ Yes → Animate.css or Animista
│  └─ No → Continue
│
├─ Building with React?
│  └─ Yes, need gestures?
│     ├─ Yes → Framer Motion
│     └─ No, lightweight? → Motion One
│  └─ No → Continue
│
├─ Need scroll-triggered?
│  └─ Yes
│     ├─ With Tailwind? → TAOS
│     ├─ Need pinning/scrubbing? → GSAP ScrollTrigger
│     └─ Simple fade/slide? → AOS
│  └─ No → Continue
│
├─ Need 3D graphics?
│  └─ Yes → Three.js or react-three-fiber
│  └─ No → Continue
│
├─ Complex timelines?
│  └─ Yes → GSAP
│  └─ No → Anime.js or Popmotion
```

---

## Quick Installation Guide

### Most Common Setup: React + Animations
```bash
# Option 1: Framer Motion (full-featured)
npm install framer-motion

# Option 2: Lightweight combo
npm install motion taos tailwindcss

# Option 3: GSAP power user
npm install gsap gsap/ScrollTrigger
```

### Simple CSS Animations
```html
<!-- Animate.css via CDN -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>

<!-- Or npm -->
npm install animate.css
```

### GSAP Full Stack
```bash
npm install gsap
# Add plugins as needed
npm install gsap/ScrollTrigger
npm install gsap/Draggable
npm install gsap/MotionPathPlugin  # Premium
npm install gsap/TextPlugin         # Premium
```

### 3D Web Experience
```bash
npm install three @react-three/fiber @react-three/drei
```

---

## Performance Tips

### GPU-Accelerated Properties
Only animate these for best performance:
- `transform` (translate, rotate, scale)
- `opacity`
- `filter`

**Example:**
```javascript
// Good ✓
gsap.to(".element", { x: 100, opacity: 0.5, duration: 1 });

// Avoid ✗
gsap.to(".element", { width: 200, height: 200, duration: 1 });
```

### Lazy Loading Animation Libraries
```javascript
// Load GSAP only when needed
const loadGSAP = async () => {
  const gsap = await import('gsap');
  gsap.to('.element', { duration: 1, x: 100 });
};
```

### CSS containment
```css
.animated-element {
  contain: layout style paint;
}
```

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
```

---

## Common Patterns

### Fade In on Scroll (React + Framer Motion)
```javascript
import { motion } from 'framer-motion';
import { useInView } from 'react-intersection-observer';

export default function FadeInOnScroll() {
  const { ref, inView } = useInView({ threshold: 0.1 });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0 }}
      animate={inView ? { opacity: 1 } : { opacity: 0 }}
      transition={{ duration: 0.6 }}
    >
      Content fades in when scrolled into view
    </motion.div>
  );
}
```

### Scroll Timeline (Pure CSS)
```css
@supports (animation-timeline: view()) {
  .element {
    animation: slideIn linear;
    animation-timeline: view();
    animation-range: entry 0%, cover 30%;
  }

  @keyframes slideIn {
    from { transform: translateX(-100%); }
    to { transform: translateX(0); }
  }
}
```

### GSAP Timeline
```javascript
const tl = gsap.timeline();
tl.to('.element1', { duration: 1, x: 100 })
  .to('.element2', { duration: 1, opacity: 0 }, 0) // 0 = start at same time
  .to('.element3', { duration: 1, rotation: 360 });
```

### Gesture Animation (Framer Motion)
```javascript
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  onClick={handleClick}
>
  Click me
</motion.button>
```

---

## Troubleshooting

### Animation Janky/Stuttering
- Check DevTools Performance tab for dropped frames
- Use `will-change` sparingly on animated elements
- Profile with Chrome DevTools
- Switch to GPU-accelerated properties (transform, opacity)

### Performance Issues with Scroll Animations
- Use GSAP ScrollTrigger (optimized)
- Avoid animating too many elements simultaneously
- Use `onEnter` callback instead of continuous timeline

### Animation Not Working
- Check browser console for errors
- Verify CSS selectors match elements
- Check z-index if animation invisible
- Confirm transform-origin is correct for rotations

### Bundle Size Too Large
- Use Motion One instead of Framer Motion (36KB savings)
- Use native CSS scroll-driven animations (Chrome 115+)
- Code-split GSAP plugins: load only what you use
- Consider pure CSS for simple animations

---

## Learning Path

### Beginner
1. Start with **Animate.css** - learn class-based animations
2. Learn **CSS @keyframes** - foundation knowledge
3. Try **Magic Animations** - lightweight vanilla CSS

### Intermediate
1. Learn **Framer Motion** basics (React)
2. Understand **WAAPI (Web Animations API)** concepts
3. Explore **scroll-triggered animations** with AOS

### Advanced
1. Master **GSAP** and timeline-based animations
2. Learn **Three.js** for 3D
3. Understand **physics-based animations** (springs, inertia)
4. Explore **gesture-driven interactions**

---

## 2026 Best Practices

1. **Choose the right tool** for your use case (don't use GSAP for simple hover effects)
2. **Prioritize bundle size** - modern apps favor lightweight solutions
3. **Use native CSS** when possible (scroll-driven animations)
4. **Respect user preferences** - honor `prefers-reduced-motion`
5. **Profile performance** - not all animations feel smooth, test!
6. **Component-first** - animations as part of component state (Framer Motion style)
7. **Combine tools** - Tailwind + Motion One + TAOS is better than one solution

---

## Related Resources

- **MDN Web Animations API:** https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
- **CSS Tricks - Animation:** https://css-tricks.com/tag/animation/
- **GSAP Docs:** https://gsap.com/docs
- **Framer Motion Docs:** https://www.framer.com/motion
- **Can I Use - Animations:** https://caniuse.com/?search=animation

---

*Last Updated: January 2026*
