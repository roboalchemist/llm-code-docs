# Source: https://lynxjs.org/guide/ui/layout/linear-layout.md

# Linear Layout

If you want to arrange children sequentially without dealing with the complexities of [flexible box](/guide/ui/layout/flexible-box-layout.md) and [grid](/guide/ui/layout/grid-layout.md) layouts (such as shrink and placement issues), consider using **linear layout**. This layout is inspired by [linear layout](https://developer.android.com/develop/ui/views/layout/linear) in Android.

The default layout direction of a linear layout is vertical. You can also use Web's alignment properties such as [`align-items`](/api/css/properties/align-items.md), [`align-self`](/api/css/properties/align-self.md), and [`justify-content`](/api/css/properties/justify-content.md) with this layout. For the supported properties, please refer to the [Reference section](#reference).

## How to Build a Linear Layout?

### Step 1: Apply `display: linear`

To implement a linear layout, modify the `display` property of the parent element to use a linear layout for its children.

```css
display: linear;
```

### Step 2: Set the Layout Direction

A linear layout arranges elements along the main and cross axes, similar to a [flexible box layout](/guide/ui/layout/flexible-box-layout.md). The **main axis** refers to the direction in which elements are aligned, whereas the **cross axis** is perpendicular to it.

You can adjust the layout direction by altering the [`linear-direction`](/api/css/properties/linear-direction.md) property of the parent container, akin to the [`flex-direction`](/api/css/properties/flex-direction.md) property in flexible box layouts. By default, `linear-direction` is set to `column`.

```css
linear-direction: column;
```

<center>
  <img width="50%" src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/linear_main_axis.png" />
</center>

### Step 3: Align Children Along the Main Axis

To control the position of child elements along the main axis, use the [`justify-content`](/api/css/properties/justify-content.md) property. In the demo below, the main axis is vertical.

**This is an example below:  layout**

**Entry:** `src/linear_justify_content`
**Bundle:** `dist/linear_justify_content.lynx.bundle` | Web: `dist/linear_justify_content.web.bundle`

```tsx {9,16,23}
import { root } from "@lynx-js/react";

import "./index.scss";

const LinearJustifyContentExample = () => {
  return (
    <scroll-view>
      <text className="title_style">justify-content: start</text>
      <view className="container" style={{ justifyContent: "start" }}>
        <view className="item1"></view>
        <view className="item2"></view>
        <view className="item3"></view>
      </view>

      <text className="title_style">justify-content: end</text>
      <view className="container" style={{ justifyContent: "end" }}>
        <view className="item1"></view>
        <view className="item2"></view>
        <view className="item3"></view>
      </view>

      <text className="title_style">justify-content: center</text>
      <view className="container" style={{ justifyContent: "center" }}>
        <view className="item1"></view>
        <view className="item2"></view>
        <view className="item3"></view>
      </view>

      <text className="title_style">justify-content: space-between</text>
      <view className="container" style={{ justifyContent: "space-between" }}>
        <view className="item1"></view>
        <view className="item2"></view>
        <view className="item3"></view>
      </view>
    </scroll-view>
  );
};

root.render(<LinearJustifyContentExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Step 4: Align Children Along the Cross Axis

To align items within a container along the cross axis, apply [`align-items`](/api/css/properties/align-items.md) to the container or [`align-self`](/api/css/properties/align-items.md) to children.

In the example below, the cross axis is vertical, with `align-items: center` used in the container to center children along this axis.

**This is an example below:  layout**

**Entry:** `src/linear_align_items`
**Bundle:** `dist/linear_align_items.lynx.bundle` | Web: `dist/linear_align_items.web.bundle`

```tsx {27}
import { root } from "@lynx-js/react";

const LinearAlignItemsExample = () => {
  return (
    <scroll-view>
      <text
        style={{
          fontSize: "45rpx",
          fontWeight: "bold",
          marginLeft: "auto",
          marginRight: "auto",
          textAlign: "center",
          color: "linear-gradient(to right, rgb(255,53,26), rgb(0,235,235))",
        }}
      >
        align-items: center
      </text>
      <view
        className="container"
        style={{
          display: "linear",
          linearOrientation: "horizontal",
          height: "300px",
          width: "90%",
          padding: "5px",
          margin: "10px",
          justifyContent: "center",
          marginLeft: "auto",
          marginRight: "auto",
          alignItems: "center",
          border: "1px solid #000",
          borderRadius: "6px",
        }}
      >
        <view
          style={{
            margin: "2px",
            height: "100px",
            width: "30%",
            backgroundColor: "rgb(255,53,26)",
            borderRadius: "6px",
          }}
        >
        </view>
        <view
          style={{
            margin: "2px",
            height: "100px",
            width: "30%",
            backgroundColor: "rgb(0,235,235)",
            borderRadius: "6px",
          }}
        >
        </view>
        <view
          style={{
            margin: "2px",
            height: "100px",
            width: "30%",
            backgroundColor: "rgb(255,53,26)",
            borderRadius: "6px",
          }}
        >
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<LinearAlignItemsExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



By adjusting the `align-self` property on a child, you can override `align-items` behavior, as shown with the first block below the parent element.

**This is an example below:  layout**

**Entry:** `src/linear_align_self`
**Bundle:** `dist/linear_align_self.lynx.bundle` | Web: `dist/linear_align_self.web.bundle`

```tsx {17,27}
import { root } from "@lynx-js/react";

const LinearAlignSelfExample = () => {
  return (
    <scroll-view>
      <view
        className="container"
        style={{
          display: "linear",
          linearOrientation: "horizontal",
          height: "300px",
          width: "90%",
          padding: "5px",
          margin: "10px",
          justifyContent: "center",
          marginLeft: "auto",
          marginRight: "auto",
          alignItems: "center",
          border: "1px solid #000",
          borderRadius: "6px",
        }}
      >
        <view
          style={{
            margin: "2px",
            height: "100px",
            width: "30%",
            alignSelf: "end",
            backgroundColor: "rgb(255,53,26)",
            borderRadius: "6px",
          }}
        >
        </view>
        <view
          style={{
            margin: "2px",
            height: "100px",
            width: "30%",
            backgroundColor: "rgb(0,235,235)",
            borderRadius: "6px",
          }}
        >
        </view>
        <view
          style={{
            margin: "2px",
            height: "100px",
            width: "30%",
            backgroundColor: "rgb(255,53,26)",
            borderRadius: "6px",
          }}
        >
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<LinearAlignSelfExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



::: info
Please note that when the cross-axis size of the parent element (such as the `width` when `linear-direction: column`) is set, and if the size of the child element in this direction is not specified (or `auto`), the children's size along the cross-axis will expand to fill the container.
:::

### Step 5: Specify Dynamic Sizes Along the Main Axis

Linear layout allows for the [`linear-weight`](/api/css/properties/linear-weight.md) attribute, enabling adaptive sizing along the main axis based on assigned weight ratios and available space.

Set the [`linear-weight`](/api/css/properties/linear-weight.md) for each child to define its size share along the main axis. The parent container adjusts every child's dimensions to fit proportions derived from their respective weight values relative to available space.

**This is an example below:  layout**

**Entry:** `src/linear_weight`
**Bundle:** `dist/linear_weight.lynx.bundle` | Web: `dist/linear_weight.web.bundle`

```tsx {33,42,51}
import { root } from "@lynx-js/react";

const LinearAlginItemsExample = () => {
  return (
    <scroll-view>
      <text
        style={{
          fontSize: "45rpx",
          fontWeight: "bold",
          marginLeft: "auto",
          marginRight: "auto",
          textAlign: "center",
          color: "linear-gradient(to right, rgb(255,53,26), rgb(0,235,235))",
        }}
      >
        linear-weight: 0.5 : 2 : 0.5
      </text>
      <view
        style={{
          display: "linear",
          linearOrientation: "vertical",
          height: "300px",
          width: "90%",
          padding: "5px",
          margin: "10px",
          marginLeft: "auto",
          marginRight: "auto",
          border: "1px solid #000",
          borderRadius: "6px",
        }}
      >
        <view
          style={{
            margin: "5px",
            linearWeight: 0.5,
            backgroundColor: "rgb(255,53,26)",
            borderRadius: "6px",
          }}
        >
        </view>
        <view
          style={{
            margin: "5px",
            linearWeight: 2,
            backgroundColor: "rgb(0,235,235)",
            borderRadius: "6px",
          }}
        >
        </view>
        <view
          style={{
            margin: "5px",
            linearWeight: 0.5,
            backgroundColor: "rgb(255,53,26)",
            borderRadius: "6px",
          }}
        >
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<LinearAlginItemsExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



In the above example, `linear-weight` specifies a scale value without unit representing the amount of space available for each child element along the main axis. The three child elements will have a 0.5 : 2 : 0.5 ratio of the main axis space.

## Reference

Currently, the linear layout supports the following layout properties:

- **Specific CSS Properties**

  - [`linear-direction`](/api/css/properties/linear-direction.md)
  - [`linear-weight`](/api/css/properties/linear-weight.md)

- **Alignment Properties**

  - [`justify-content`](/api/css/properties/justify-content.md)
  - [`align-items`](/api/css/properties/align-items.md)
  - [`align-self`](/api/css/properties/align-self.md)

- **Other Properties**

  Other properties such as [`order`](/api/css/properties/order.md), [`aspect-ratio`](/api/css/properties/aspect-ratio.md), etc., are not listed individually here; for specific property support, refer to the [API Reference](/api/css/properties.md).
