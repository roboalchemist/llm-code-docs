# Source: https://motion.dev/changelog

Title: Motion Changelog

URL Source: https://motion.dev/changelog

Published Time: Fri, 13 Mar 2026 09:29:30 GMT

Markdown Content:
### Fixed

*   Reduced filesize of `styleEffect`.

*   Fix rounding from `popLayout`.

*   `opacity` animations in React Strict Mode in development.

*   Ensure `useSpring` is not affected by monitor framerate.

*   Updating animations sequence segment types to exclude lifecycle handlers.

*   Fix layout animations with parents offset by a `%`-based translation.

*   Fix `autoplay: false` with WAAPI animations.

*   Fix layout jump in React Strict Mode in development.

*   Detect divide-by-zero in CSS `calc()` values before making animatable templates.

### Added

*   Allow `dragSnapToOrigin` to accept `"x"` or `"y"` for per-axis snapping.

*   Added axis-locked layout animations with `layout="x"` and `layout="y"`.

*   Added `skipInitialAnimation` to `useSpring`.

### Fixed

*   Fixed `height` and `width: auto` animations with `box-sizing: border-box`.

*   Reset component values when exit animation finishes.

*   Ensure `anticipate` easing returns `1` at `p === 1`.

*   Fix `@emotion/is-prop-valid` resolve error in Storybook.

*   Remove `data-pop-layout-id` from exiting elements when animation interrupted.

*   Ensure we skip WAAPI for non-animatable keyframes.

*   Ensure we skip WAAPI for SVG transforms.

*   Ensure `MotionValue` props are not passed to SVG.

*   `AnimatePresence`: Prevent `mode="wait"` elements from getting stuck when switched rapidly.

### Added

*   Skills: `/motion` skill. Includes design guidelines, performance tips, and API gotchas. Can reference the Motion Studio MCP for docs search.

*   Skills: `/css-spring` skill. Generates CSS spring easing functions via the Motion Studio MCP.

*   Skills: `/see-transition` skill. Visualise easing curves and springs via the Motion Studio MCP.

*   Skills: Added new `motion-ai-kit` installer with interactive skill picker.

### Added

*   Skills: Installer now supports VS Code.

### Updated

*   MCP: Now loads codex with documentation if purchased AI Kit.

### Fixed

*   Fixing combination of string keyframes, spring and `delay`.

*   Gracefully handle negative scroll values.

*   Fix one-frame visual gap when rapidly switching WAAPI animations.

*   `animation.time = 0` on a finished animation sets the playhead in a paused state.

### Fixed

*   Ensure final WAAPI styles are always committed synchronously to prevent flash of incorrect styles in Firefox.

*   Prevent Next.js from caching `typeof window` checks.

*   Improve projection node cleanup.

*   Variant propagation fixed for asynchronously-mounted children.

### Added

*   `ViewTimeline` support for `scroll` and `useScroll`.

### Fixed

*   Handle `%` translate values in layout animations.

### Fixed

*   Ensure `onComplete` fires at the end of an animation sequence.

Motion+

Level up your animations with Motion+
-------------------------------------

Unlock the full vault of 290+ Motion examples, premium APIs, private Discord and GitHub, and powerful VS Code animation editing tools.

One-time payment, lifetime updates.

![Image 1](https://framerusercontent.com/images/dvcUQX74Mh8wmjKmhIoM2Yli4.png?width=2000&height=2000)

### Fixed

*   Ensure `velocity` is never transferred to a time-derived spring.

### Fixed

*   Layout animations: Reset motion value velocity when starting a new layout animation.

### Fixed

*   `useScroll`: Ensure animations aren't hardware accelerated when `target` is set.

*   Improve animatable `"none"` generation for mask values.

### Added

*   `useCarousel` and `useTicker`: Provides `offset` motion value, which contains the unwrapped offset of a `Carousel` or `Ticker`.

### Fixed

*   `Ticker`: Improve accessibility attributes.

*   `Cursor`: Fix when using with browser-native drag gestures.

*   Updating `ref` type inference for `Typewriter`, `Ticker` and `ScrambleText`.

### Added

*   `Carousel`: New `wheelSwipeThreshold` prop configures the distance of wheel scroll before triggering a swipe.

### Added

*   `AnimateNumber`: `trend` prop to control digit spin direction.

    *   `trend={1}`: Digits always spin upward, wrapping 9 → 0.

    *   `trend={-1}`: Digits always spin downward, wrapping 0 → 9.

    *   `trend={(oldValue, newValue) => number}`: Function for custom logic.

    *   Default (no `trend`): Auto-detects direction based on value change.

### Changed

*   `AnimateNumber`: Now uses manual FLIP measurements instead of layout animations.

### Fixed

*   `splitText`: Ensure split text elements retain vertical positioning.

*   `Carousel`: Fix focus from breaking item reprojection.

### Added

*   Extension: Added support for spring editing.

*   Extension: Visual refresh.

*   Skills: Added Motion Performance Audit skill.

### Added

*   `AnimateView`: View animations for React.

### Fixed

*   `useScroll`: Hardware accelerated animations.

### Fixed

*   Improve detection of detached elements with vanilla layout animations.

### Fixed

*   `AnimatePresence`: Ensure exiting nodes are correctly removed when rapidly switching children.

### Added

*   `transition.inherit`: When `true`, inherit transition values from less-specific transitions.

### Fixed

*   `<motion />`: Ensure animation state is reset after being re-suspended.

*   Prevent stale values when mixing `transitionEnd` and `transition.type: false`.

*   Drag: Fix "sticky" throw velocity on initial interaciton.

*   Drag: Ensure catching a thrown element kills its velocity.

### Fixed

*   `onHoverStart` and `onHoverEnd` first argument now correctly typed as `PointerEvent`.

*   `whileHover`: No longer persists after drag end.

*   `AnimatePresence`: Allow changing `mode` prop.

### Added

*   `<motion />`: New `propagate.tap` prop prevents tap gestures from propagating to parents.

### Added

*   Drag constraints updated even when draggable or constraints resize outside of React renders.

### Added

*   `animate`: Support for bi-directional callbacks within animation sequences.

### Fixed

*   Ensure `onPan` never fires before `onPanStart`.

### Fixed

*   Allow drag to be initiated by child `a` and `button` elements.
