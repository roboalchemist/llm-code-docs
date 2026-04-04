# Source: https://lynxjs.org/guide/ui/layout/relative-layout.md

# Relative Layout <NoWeb />

If you want a layout that allows easily control the relative position between the parent and children or between the sibling elements without using complex hierarchical structure, **relative layout** (inspired by [relative Layout](https://developer.android.com/develop/ui/views/layout/relative) in Android) is the best choice. While using [grid](/guide/ui/layout/grid-layout.md), [flexible box](/guide/ui/layout/flexible-box-layout.md), and [linear](/guide/ui/layout/linear-layout.md) layouts, it's challenging to achieve a design that includes numerous relative positions using only a few styles.

Relative layout is a layout that displays children in relative positions, where each view's position can be specified relative to sibling elements (for example, to the left or below another view) or relative to the parent's area (e.g., align at bottom, left or center). For the supported properties, please refer to the [Reference section](#reference).

## How to Build a Relative Layout?

In the scenario described below, where the "user name" and "description" have a positional relationship, and the "user name" also aligns with the "avatar" on the right. What's more, the "follow", "close", "user" also have corresponding relationships with each other. The dashed lines and arrows in the image below are to indicate their positional relationship.

<center>
  <img width="70%" src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/relative_demo_1.png" />
</center>

**Let's implement the above diagram using the relative layout in following steps:**

### Step 1: Apply `display: relative`

You can apply [`display: relative`](/api/css/properties/display.md) to the parent element where you want the relative layout.

```css
display: relative;
```

### Step 2: Set ID for Children

Assign a unique [`relative-id`](/api/css/properties/relative-id.md) (integer, not `0`) for each child in the relative layout. This step is to better identify each element.

```css
// avatar
relative-id: 1;
// user_name
relative-id: 2;
// user_description
relative-id: 3;
// user_lv
relative-id: 4;
// close
relative-id: 5;
// follow
relative-id: 6;
```

### Step 3: Set Edge Alignment Properties

Use these edge alignment properties to specify alignment of the element with its **parent or sibling**'s edge. For instance, [`relative-align-top`](/api/css/properties/relative-align-top.md) ensures the element aligns with the top edge of the designated parent or sibling id.

Physical Properties

- [`relative-align-top`](/api/css/properties/relative-align-top.md)、[`relative-align-right`](/api/css/properties/relative-align-right.md)、[`relative-align-bottom`](/api/css/properties/relative-align-bottom.md)、[`relative-align-left`](/api/css/properties/relative-align-left.md)

Logical Properties

- [`relative-align-inline-start`](/api/css/properties/relative-align-inline-start.md)、[`relative-align-inline-end`](/api/css/properties/relative-align-inline-end.md)

### Step 4: Set Relative Position Properties

Define relative positioning of the current element to its **sibling** elements using these properties. As an example, [`relative-left-of`](/api/css/properties/relative-left-of.md) arranges the current element to the left of the designated sibling, closely aligning right edge with the sibling's left edge.

Physical Properties

- [`relative-left-of`](/api/css/properties/relative-left-of.md)、[`relative-right-of`](/api/css/properties/relative-right-of.md)、[`relative-top-of`](/api/css/properties/relative-top-of.md)、[`relative-bottom-of`](/api/css/properties/relative-bottom-of.md)

Logical Properties

- [`relative-inline-start-of`](/api/css/properties/relative-inline-start-of.md)、[`relative-inline-end-of`](/api/css/properties/relative-inline-end-of.md)

### Step 5: Set Center Property

Use [`relative-center`](/api/css/properties/relative-center.md) declare how the current children element is centered in the container. By setting `vertical` to achieve vertical centering, setting `horizontal` to achieve horizontal centering, or setting `both` to simultaneously achieve both vertical and horizontal centering.

### Example

<center>
  <img width="100%" src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/layout/lynx_layout_relative_demo.png" />
</center>

In this example, the container's width is fixed, while its height adjusts to its content. To incorporate gaps between elements, use `margin`.

**This is an example below:  layout**

**Entry:** `src/relative_layout`
**Bundle:** `dist/relative.lynx.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const RelativeExample = () => {
  return (
    <view className="container">
      <view className="close"></view>
      <view className="user_name"></view>
      <view className="user_description"></view>
      <view className="avatar"></view>
      <view className="user_lv"></view>
      <view className="follow"></view>
    </view>
  );
};

root.render(<RelativeExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



- **Best Practices**

  Reasonable use of the relative layout can offer developers a convenient and efficient layout experience. Therefore, it is strongly recommended that developers follow the following points when developing.

  1. Parent container positioning can be used freely without affecting performance.
  2. When using the positioning between sibling elements, it is recommended to enable the [`relative-layout-once`](/api/css/properties/relative-layout-once.md) (default enabled) style, and the sibling element will only rely on upwards.
  3. Avoid circular dependencies where 'a' depends on 'b' for its horizontal width, and 'b' depends on 'a' for its vertical width, as this can severely impact performance.
  4. Please do not have unresolved circular dependencies, which cannot get the correct layout result.
  5. Try to use logical attributes, inline-start and inline-end, to facilitate page internationalization support.

## Reference

- **Relative Id**

  - [`relative-id`](/api/css/properties/relative-id.md)

- **Edge Alignment Properties**

  **Physical Properties**

  - [`relative-align-top`](/api/css/properties/relative-align-top.md)
  - [`relative-align-right`](/api/css/properties/relative-align-right.md)
  - [`relative-align-bottom`](/api/css/properties/relative-align-bottom.md)
  - [`relative-align-left`](/api/css/properties/relative-align-left.md)

  **Logical Properties**

  - [`relative-align-inline-start`](/api/css/properties/relative-align-inline-start.md)
  - [`relative-align-inline-end`](/api/css/properties/relative-align-inline-end.md)

- **Relative Position Properties**

  **Physical Properties**

  - [`relative-left-of`](/api/css/properties/relative-left-of.md)
  - [`relative-right-of`](/api/css/properties/relative-right-of.md)
  - [`relative-top-of`](/api/css/properties/relative-top-of.md)
  - [`relative-bottom-of`](/api/css/properties/relative-bottom-of.md)

  **Logical Properties**

  - [`relative-inline-start-of`](/api/css/properties/relative-inline-start-of.md)
  - [`relative-inline-end-of`](/api/css/properties/relative-inline-end-of.md)

- **Center Property**

  - [`relative-center`](/api/css/properties/relative-center.md)

- **Layout Optimization Property**

  - [`relative-layout-once`](/api/css/properties/relative-layout-once.md)
