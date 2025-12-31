# Source: https://lynxjs.org/guide/ui/layout/flexible-box-layout.md

# Flexible Box Layout

If you need to make the size of child elements adapt to the space of the parent element (such as expanding child elements to fill the unused space or shrinking child elements to avoid overflow), you can set the [`display: flex`](/api/css/properties/display.md) property to the parent element and use the **flexible box layout**.

::: info
For more information, please refer to the [CSS Flexible Box Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout) on MDN. Lynx supports common flexible box layout properties and in most cases aligns with Web standards. For the supported properties, please refer to the [Reference section](#reference).
:::

**The following examples show typical features of the flexible box layout.**

## Typical Features

### Filling the Parent Element with `flex-grow`

The [`flex-grow`] property helps you allocate the remaining space of the parent element to the size of the sub-elements based on the weight declared by `flex-grow`.

**This is an example below:  layout**

**Entry:** `src/flex_grow`
**Bundle:** `dist/flex_grow.lynx.bundle` | Web: `dist/flex_grow.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const FlexGrowExample = () => {
  return (
    <scroll-view>
      <text className="title">
        flex-direction: column
      </text>
      <view className="container">
        <view className="item1">
          <text className="text">flex-grow: 1</text>
        </view>
        <view className="item2">
          <text className="text">flex-grow: 2</text>
        </view>
        <view className="item3">
          <text className="text">100px</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<FlexGrowExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Shrinking Child Elements with `flex-shrink`

When the child elements are about to overflow the parent element, the child elements can shrinked according to the weight declared by [flex-shrink](/api/css/properties/flex-shrink.md) to fit the size of the parent element.

**This is an example below:  layout**

**Entry:** `src/flex_shrink`
**Bundle:** `dist/flex_shrink.lynx.bundle` | Web: `dist/flex_shrink.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const FlexShrinkExample = () => {
  return (
    <scroll-view>
      <text className="title">
        flex-direction: column
      </text>
      <view className="container">
        <view className="item1">
          <text className="text">flex-shrink: 0</text>
          <text className="text">height 300px</text>
        </view>
        <view className="item2">
          <text className="text">flex-shrink: 1</text>
          <text className="text">height shrinks from 300px to fit container</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<FlexShrinkExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



<Details title={<span>Lynx differs from Web in the minimum value for shrinking sub-elements.</span>}>
  Lynx currently does not support [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/min-content), and therefore treats it temporarily as `0px`. This means that while the Web can ensure sub-elements do not shrink below their minimum content width when fitting the parent element size, Lynx cannot guarantee this at present.

  <Columns titles={['Code', 'Inconsistent behavior between Web and Lynx']}>
    ```html
    <div
      style="width:100px;
                height:70px;
                display:flex;
                background-color:rgb(0, 235, 235);"
    >
      <div
        style="display:flex;
                  height:50px;
                  background-color:rgb(255, 53, 26);"
      >
        <div
          style="width:150px;
                    height:50px;"
        ></div>
      </div>
    </div>
    ```

    <center>
      <img width="70%" src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/layout/layout_min_content.png" />
    </center>
  </Columns>
</Details>

### Wrapping with `flex-wrap`

The [`flex-wrap`] property allows content that doesn't fit on a single line to be displayed on subsequent lines. This attribute specifies whether flex elements are shown in a single or multiple lines. When allowed to wrap, this attribute can control the stacking direction of the lines.

**This is an example below:  layout**

**Entry:** `src/flex_wrap`
**Bundle:** `dist/flex_wrap.lynx.bundle` | Web: `dist/flex_wrap.web.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const FlexWrapExample = () => {
  return (
    <scroll-view>
      <text className="title">
        flex-direction: row;
      </text>
      <text className="title">
        flex-wrap: wrap;
      </text>
      <view className="container" style={{ flexWrap: "wrap" }}>
        <view className="item">
          <text className="text">Item 1</text>
        </view>
        <view className="item" style={{ backgroundColor: "rgb(0,235,235)" }}>
          <text className="text">Item 2</text>
        </view>
        <view className="item">
          <text className="text">Item 3</text>
        </view>
      </view>

      <text className="title">
        flex-direction: row;
      </text>
      <text className="title">
        flex-wrap: nowrap;
      </text>
      <view className="container" style={{ flexWrap: "nowrap" }}>
        <view className="item">
          <text className="text">Item 1</text>
        </view>
        <view className="item" style={{ backgroundColor: "rgb(0,235,235)" }}>
          <text className="text">Item 2</text>
        </view>
        <view className="item">
          <text className="text">Item 3</text>
        </view>
      </view>
    </scroll-view>
  );
};

root.render(<FlexWrapExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Reference

Currently, Lynx supports the following common flexible box layout properties:

- **CSS Properties**

  - [`flex`](/api/css/properties/flex.md)
  - [`flex-basis`](/api/css/properties/flex-basis.md)
  - [`flex-direction`](/api/css/properties/flex-direction.md)
  - [`flex-flow`](/api/css/properties/flex-flow.md)
  - [`flex-grow`](/api/css/properties/flex-grow.md)
  - [`flex-shrink`](/api/css/properties/flex-shrink.md)
  - [`flex-wrap`](/api/css/properties/flex-wrap.md)
  - [`order`](/api/css/properties/order.md)

- **Alignment Properties**

  - [`align-content`](/api/css/properties/align-content.md)
  - [`align-items`](/api/css/properties/align-items.md)
  - [`align-self`](/api/css/properties/align-self.md)
  - [`justify-content`](/api/css/properties/justify-content.md)
  - [`row-gap`](/api/css/properties/row-gap.md)
  - [`column-gap`](/api/css/properties/column-gap.md)
  - [`gap`](/api/css/properties/gap.md)

For more usage details, please refer to the [CSS Flexible Box Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout) on MDN.

[`flex-grow`]: /api/css/properties/flex-grow.md

[`flex-shrink`]: /api/css/properties/flex-shrink.md

[`flex-wrap`]: /api/css/properties/flex-wrap.md
