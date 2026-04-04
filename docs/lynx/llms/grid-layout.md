# Source: https://lynxjs.org/guide/ui/layout/grid-layout.md

# Grid Layout

If you want a responsive layout where multiple elements are staggered both vertically and horizontally, the **grid layout** is your best choice. This layout is based on a two-dimensional grid, and it is the most powerful CSS layout on the Web.

:::info
For further details, please refer to MDN's [css grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout).
In Lynx, the grid layout largely follows with web standards. Currently, Lynx does not support [`[line-names]`](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Grid_layout_using_named_grid_lines) and [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-area). Please refer to the [Reference](#reference) section for supported properties.
:::

**Here is a brief guide on using the grid layout.**

## How to Build a Grid Layout?

Before you build a grid layout, it's important first to understand the basic concepts.

### Basic Concepts

- **Grid Containers and Grid Items**

  The parent element using grid layout is called a "grid container." The children within the container that are layouted using grid layout are called "grid items".

- **Grid Lines**

  The lines that divide the grid layout are called "grid lines." Typically, x rows have x+1 horizontal grid lines, y columns have y+1 vertical grid lines, as shown in the image below with 6 horizontal and 4 vertical grid lines.

- **Grid Rows and Grid Columns**

  The spaces between two grid lines are called grid tracks. The horizontal tracks in the container are called "grid rows," and vertical tracks are called "grid columns."

- **Grid Cells**

  The intersection of rows and columns forms a grid cell.

- **Grid Areas**

  The area occupied by one or more grid cells by a grid item is called a grid area.

- **Inline Axis and Block Axis**

  As Lynx does not support [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode), the inline axis is horizontal, and the block axis is vertical.

<center>
  <img width="100%" src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/layout/grid_define.png" />
</center>

### Step 1: Apply `display: grid`

To implement the grid layout, set `display: grid` on the parent element.

```css
display: grid;
```

### Step 2: Specify the Size of Rows and Columns

Once the container has the grid layout specified, define the rows and columns. The [`grid-template-columns`] property specifies each column's width, while the [`grid-template-rows`] property defines each row's height.

If `grid-template-columns` or `grid-template-rows` are not explicitly used to define dimensions, the grid layout uses [`grid-auto-columns`] and [`grid-auto-rows`] for determining column widths and row heights.

**This is an example below:  layout**

**Entry:** `src/grid_size`
**Bundle:** `dist/grid_size.lynx.bundle` | Web: `dist/grid_size.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const GridSize = () => {
  return (
    <scroll-view>
      <text className="title">grid-template-columns: 1fr 100px;</text>
      <text className="title">grid-template-rows: repeat(3, 1fr);</text>
      <view className="container">
        <view className="item">
          <text className="text">ONE</text>
        </view>
        <view className="item">
          <text className="text">TWO</text>
        </view>
        <view className="item">
          <text className="text">THREE</text>
        </view>
        <view className="item">
          <text className="text">FOUR</text>
        </view>
        <view className="item">
          <text className="text">FIVE</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<GridSize />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Step 3: Specify Grid Gaps

Grid gap is the spacing between grid tracks. It can be indicated by [`column-gap`] for columns, [`row-gap`] for rows, or [`gap`] for both columns and rows.

**This is an example below:  layout**

**Entry:** `src/grid_gap`
**Bundle:** `dist/grid_gap.lynx.bundle` | Web: `dist/grid_gap.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const GridGap = () => {
  return (
    <scroll-view>
      <text className="title">gap: 20px;</text>
      <view className="container" style={{ gap: "20px" }}>
        <view className="item">
          <text className="text">ONE</text>
        </view>
        <view className="item">
          <text className="text">TWO</text>
        </view>
        <view className="item">
          <text className="text">THREE</text>
        </view>
        <view className="item">
          <text className="text">FOUR</text>
        </view>
        <view className="item">
          <text className="text">FIVE</text>
        </view>
      </view>

      <text className="title">column-gap: 20px;</text>
      <view className="container" style={{ columnGap: "20px" }}>
        <view className="item">
          <text className="text">ONE</text>
        </view>
        <view className="item">
          <text className="text">TWO</text>
        </view>
        <view className="item">
          <text className="text">THREE</text>
        </view>
        <view className="item">
          <text className="text">FOUR</text>
        </view>
        <view className="item">
          <text className="text">FIVE</text>
        </view>
      </view>

      <text className="title">row-gap: 20px;</text>
      <view className="container" style={{ rowGap: "20px" }}>
        <view className="item">
          <text className="text">ONE</text>
        </view>
        <view className="item">
          <text className="text">TWO</text>
        </view>
        <view className="item">
          <text className="text">THREE</text>
        </view>
        <view className="item">
          <text className="text">FOUR</text>
        </view>
        <view className="item">
          <text className="text">FIVE</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<GridGap />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Step 4: Align Grid Tracks to Inline and Block Axes

Align the grid tracks with the inline (horizontal axis) and block (vertical axis) using [`justify-content`] and [`align-content`].

**This is an example below:  layout**

**Entry:** `src/grid_axis_alignment`
**Bundle:** `dist/grid_axis_alignment.lynx.bundle` | Web: `dist/grid_axis_alignment.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const GridAxisAlignment = () => {
  return (
    <scroll-view>
      <text className="title">justify-content: center;</text>
      <text className="title">align-content: start;</text>
      <view className="container" style={{ justifyContent: "center", alignContent: "start" }}>
        <view className="item">
          <text className="text">ONE</text>
        </view>
        <view className="item">
          <text className="text">TWO</text>
        </view>
        <view className="item">
          <text className="text">THREE</text>
        </view>
        <view className="item">
          <text className="text">FOUR</text>
        </view>
        <view className="item">
          <text className="text">FIVE</text>
        </view>
      </view>

      <text className="title">justify-content: end;</text>
      <text className="title">align-content: center;</text>
      <view className="container" style={{ justifyContent: "end", alignContent: "center" }}>
        <view className="item">
          <text className="text">ONE</text>
        </view>
        <view className="item">
          <text className="text">TWO</text>
        </view>
        <view className="item">
          <text className="text">THREE</text>
        </view>
        <view className="item">
          <text className="text">FOUR</text>
        </view>
        <view className="item">
          <text className="text">FIVE</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<GridAxisAlignment />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Step 5: Specify the Grid Lines for Grid Items

The positions of grid items can be specified. Use [`grid-column-start`] and [`grid-column-end`] to set the columns a grid area spans, and [`grid-row-start`] and [`grid-row-end`] to define rows.

**This is an example below:  layout**

**Entry:** `src/grid_placement`
**Bundle:** `dist/grid_placement.lynx.bundle` | Web: `dist/grid_placement.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const GridAxisAlignment = () => {
  return (
    <scroll-view>
      <view className="container" style={{ justifyContent: "center", alignContent: "start" }}>
        <view className="item" style={{ gridColumnStart: "span 2" }}>
          <text className="text">grid-column-start: span 2</text>
        </view>
        <view className="item" style={{ gridColumnStart: "2", gridRowStart: "2" }}>
          <text className="text">grid-column-start: 2;</text>
          <text className="text">grid-row-start: 2</text>
        </view>
        <view className="item" style={{ gridRowEnd: "-2", gridColumnStart: "span 2" }}>
          <text className="text">grid-column-start: span 2;</text>
          <text className="text">grid-row-end: -2</text>
        </view>
        <view className="item" style={{ gridColumnEnd: "-2", gridRowEnd: "-1" }}>
          <text className="text">grid-column-end: -2;</text>
          <text className="text">grid-row-end: -1</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<GridAxisAlignment />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Step 6: Align Grid Items to the Grid Area

Having established the grid items' respective grid areas in previous steps, you can now use [`align-items`] and [`align-self`] to vertically align grid items to the grid area, and [`justify-items`] and [`justify-self`] to horizontally align them as well. It's notable that `align-self` and `justify-self` settings on grid items will override those set by `align-items` and `justify-items` on the container.

**This is an example below:  layout**

**Entry:** `src/grid_area_alignment`
**Bundle:** `dist/grid_area_alignment.lynx.bundle` | Web: `dist/grid_area_alignment.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const GridAxisAlignment = () => {
  return (
    <scroll-view>
      <text className="title">align-items: center;</text>
      <text className="title">justify-items: center;</text>
      <view className="container" style={{ alignItems: "center", justifyItems: "center" }}>
        <view className="item" style={{ gridColumnStart: "1", alignSelf: "end" }}>
          <text className="text">align-self: end;</text>
        </view>
        <view className="item_stretch">
          <text className="text">align-self: stretch;</text>
          <text className="text">justify-self: stretch;</text>
        </view>
        <view
          className="item"
          style={{ gridRowStart: "2", gridColumnStart: "1", justifySelf: "end", alignSelf: "start" }}
        >
          <text className="text">justify-self: end;</text>
          <text className="text">align-self: start;</text>
        </view>
        <view className="item_stretch">
          <text className="text">align-self: stretch;</text>
          <text className="text">justify-self: stretch;</text>
        </view>
        <view className="item" style={{ gridRowStart: "3", gridColumnStart: "1", justifySelf: "start" }}>
          <text className="text">justify-self: start;</text>
        </view>
        <view className="item_stretch">
          <text className="text">align-self: stretch;</text>
          <text className="text">justify-self: stretch;</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<GridAxisAlignment />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Reference

Currently, Lynx supports the following common grid layout properties:

- **CSS Properties**

  - [`grid-template-columns`](/api/css/properties/grid-template-columns.md)
  - [`grid-template-rows`](/api/css/properties/grid-template-rows.md)
  - [`grid-auto-columns`](/api/css/properties/grid-auto-columns.md)
  - [`grid-auto-rows`](/api/css/properties/grid-auto-rows.md)
  - [`grid-auto-flow`](/api/css/properties/grid-auto-flow.md)
  - [`grid-row-start`](/api/css/properties/grid-row-start.md)
  - [`grid-row-end`](/api/css/properties/grid-row-end.md)
  - [`grid-column-start`](/api/css/properties/grid-column-start.md)
  - [`grid-column-end`](/api/css/properties/grid-column-end.md)

- **Alignment Properties**

  - [`align-content`](/api/css/properties/align-content.md)
  - [`align-items`](/api/css/properties/align-items.md)
  - [`align-self`](/api/css/properties/align-self.md)
  - [`justify-content`](/api/css/properties/justify-content.md)
  - [`justify-items`](/api/css/properties/justify-items.md)
  - [`justify-self`](/api/css/properties/justify-self.md)
  - [`row-gap`](/api/css/properties/row-gap.md)
  - [`column-gap`](/api/css/properties/column-gap.md)
  - [`gap`](/api/css/properties/gap.md)

For more information on usage, please refer to MDN's [css grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout).

[`grid-template-columns`]: /api/css/properties/grid-template-columns.md

[`grid-template-rows`]: /api/css/properties/grid-template-rows.md

[`grid-auto-columns`]: /api/css/properties/grid-auto-columns.md

[`gap`]: /api/css/properties/gap.md

[`column-gap`]: /api/css/properties/column-gap.md

[`row-gap`]: /api/css/properties/row-gap.md

[`grid-auto-rows`]: /api/css/properties/grid-auto-rows.md

[`grid-column-start`]: /api/css/properties/grid-column-start.md

[`grid-column-end`]: /api/css/properties/grid-column-end.md

[`grid-row-start`]: /api/css/properties/grid-row-start.md

[`grid-row-end`]: /api/css/properties/grid-row-end.md

[`justify-content`]: /api/css/properties/justify-content.md

[`align-content`]: /api/css/properties/align-content.md

[`align-items`]: /api/css/properties/align-items.md

[`align-self`]: /api/css/properties/align-self.md

[`justify-items`]: /api/css/properties/justify-items.md

[`justify-self`]: /api/css/properties/justify-self.md
