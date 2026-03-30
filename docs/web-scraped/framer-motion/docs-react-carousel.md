# Source: https://motion.dev/docs/react-carousel

Title: Carousel, a performant, infinite scrolling carousel | Motion

URL Source: https://motion.dev/docs/react-carousel

Published Time: Fri, 13 Mar 2026 09:28:49 GMT

Markdown Content:
The Carousel component creates performant, accessible and fully-featured carousels in React. It's designed to be flexible and easy to use, supporting pointer, wheel and keyboard navigation out the box.

It allows you to go beyond the traditional limitations of CSS-only approaches, with support for infinitely-scrolling carousels and without limitations on styling.

### [Features](https://motion.dev/docs/react-carousel#features)

*   **Lightweight:** Just `+5.5kb` on top of [the](https://motion.dev/docs/react-motion-component)`motion`[component](https://motion.dev/docs/react-motion-component).

*   **Accessible:** Automatic ARIA labels, respects reduced motion, RTL layouts, and all major input methods.

*   **Performant:** Built on the same [unique rendering](https://motion.dev/magazine/building-the-ultimate-ticker) used by the [Ticker](https://motion.dev/docs/react-ticker) component that achieves infinite scrolling with while minimising or eliminating item cloning.

*   **Customisable:** Provides functions and state to easily create custom controls and pagination.

[Install](https://motion.dev/docs/react-carousel#install)
---------------------------------------------------------

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev/). You need to be a [Motion+ member](https://motion.dev/plus) to generate a private token.

[Usage](https://motion.dev/docs/react-carousel#usage)
-----------------------------------------------------

### [Import](https://motion.dev/docs/react-carousel#import)

Import the `Carousel` component from "motion-plus/react"`:

`Carousel` accepts a single mandatory prop, `items`. This is a list of valid React nodes (which can be components, strings or numbers):

### [Direction](https://motion.dev/docs/react-carousel#direction)

By default, carousels will scroll horizontally. Setting the `axis` prop to `y`, we can make them vertical.

### [Layout](https://motion.dev/docs/react-carousel#layout)

Items are laid out via flexbox. Passing `gap` and `align` will adjust the spacing and off-axis alignment of them items.

### [Overflow](https://motion.dev/docs/react-carousel#overflow)

By setting `overflow` to `true`, items will visually extend out from the container to the edges of the viewport.

This makes it straightforward to place a `Carousel` within a document flow but still extend the ticker effect across the full viewport.

### [Infinite scrolling](https://motion.dev/docs/react-carousel#infinite-scrolling)

By default, carousels will scroll infinitely. This can be disabled by setting `loop={false}`.

### [Layout](https://motion.dev/docs/react-carousel#layout-1)

By default, each item will be sized according to its contents. By setting `itemSize="fill"`, items will extend the match the width of the container.

### [Snapping](https://motion.dev/docs/react-carousel#snapping)

By default, drag and wheel controls will snap between pages. By setting `snap={false}`, snapping can be disabled and the carousel will freely scroll.

### [Custom controls](https://motion.dev/docs/react-carousel#custom-controls)

Custom controls can be passed to `Carousel` as children.

Any component rendered within `Carousel` can call `useCarousel` to access state and pagination functions. This hook provides:

*   `nextPage`/`prevPage`: Paginate next/previous.

*   `gotoPage`: Pass it a page index to animate to this page.

*   `isNextActive`/`isPrevActive`: If `loop={false}` then these will be false when we hit the limits of the carousel.

*   `currentPage`: Index of the current page

*   `totalPages`: Number of total pages.

### [Autoplay](https://motion.dev/docs/react-carousel#autoplay)

With `currentPage` and `nextPage` from `useCarousel`, we can also set up our own autoplay functionality.

By passing `currentPage` to the `useEffect`, the timer will restart whenever the page changes, whether that's from a swipe/drag, or from the autoplay timer itself.

By using `currentPage`, `totalPages` and `gotoPage` from `useCarousel`, a custom pagination indicator/navigator can be built.
