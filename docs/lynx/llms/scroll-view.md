# Source: https://lynxjs.org/api/elements/built-in/scroll-view.md

# `<scroll-view>`

<APISummary />

Basic scrolling component supporting both horizontal and vertical scrolling. When its content area is larger than its visible area, it allows users to scroll to reveal more content.

## Usage

### Horizontal and Vertical Scrolling

`<scroll-view>` supports both horizontal and vertical scrolling, implemented through the `scroll-orientation` properties.
`<scroll-view>` always uses the [linear](/guide/ui/layout/linear-layout.md) layout, and the layout direction is determined by the `scroll-orientation` attributes.

**This is an example below:  scroll-view**

**Entry:** `src/base`
**Bundle:** `dist/base.lynx.bundle` | Web: `dist/base.web.bundle`

```tsx {15,24}
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { VerticalScrollItem } from "../component/scrollItem.jsx";
import { HorizontalScrollItem } from "../component/scrollItem.jsx";

export const App = () => {
  return (
    <view style={{ width: "100%", height: "100%", padding: 10, display: "linear", marginTop: 20 }}>
      <text style={{ fontSize: "20px", fontWeight: "bold", height: "40px", paddingLeft: "10px", marginTop: "10px" }}>
        Horizontal ScrollView Example
      </text>
      <scroll-view
        scroll-orientation="horizontal"
        style={{ width: "calc(100% - 10px)", height: "100px", paddingLeft: "5px", borderRadius: "10px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => <HorizontalScrollItem index={index} />)}
      </scroll-view>
      <text style={{ fontSize: "20px", fontWeight: "bold", height: "40px", paddingLeft: "10px", marginTop: "10px" }}>
        Vertical ScrollView Example
      </text>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "100%", paddingLeft: "5px", marginLeft: "5px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => <VerticalScrollItem index={index} />)}
      </scroll-view>
    </view>
  );
};

```



### Scroll Events

Use event callbacks such as [`bindscroll`](#bindscroll), [`bindscrolltoupper`](#bindscrolltoupper), and [`bindscrolltolower`](#bindscrolltolower) to monitor changes in scroll progress.

**This is an example below:  scroll-view**

**Entry:** `src/event`
**Bundle:** `dist/base.lynx.bundle` | Web: `dist/base.web.bundle`

```tsx {16-24}
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.
import { root } from "@lynx-js/react";
import "./index.css";
import { VerticalScrollItem } from "../component/scrollItem.jsx";
const VerticalScrollContainer = () => {
  return (
    <view
      style={{ width: "100%", height: "100%" }}
    >
      <text className="title">ScrollView Example</text>
      <scroll-view
        scroll-orientation="vertical"
        style="width:100%; height: 100%; padding-left: 5px;margin-left:5px"
        bindscroll={(e) => {
          console.log(e.detail);
        }}
        bindscrolltoupper={(e) => {
          console.log(e.detail);
        }}
        bindscrolltolower={(e) => {
          console.log(e.detail);
        }}
      >
        {Array.from({ length: 20 }).map((item, index) => <VerticalScrollItem index={index} />)}
      </scroll-view>
    </view>
  );
};
export default VerticalScrollContainer;
root.render(<VerticalScrollContainer />);

```



### Sticky Capability

As a child node of `<scroll-view>`, you can set the `sticky` attribute making the child node remain at a certain distance from the top of the `<scroll-view>` and not continue scrolling with the content.

**This is an example below:  scroll-view**

**Entry:** `src/sticky`
**Bundle:** `dist/base.lynx.bundle` | Web: `dist/base.web.bundle`

```tsx
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.
import { root } from "@lynx-js/react";
import { VerticalScrollItem } from "../component/scrollItem.jsx";
import { StickyItem } from "./stickyItem.jsx";

const VerticalScrollContainer = () => {
  return (
    <view style={{ width: "100%", height: "100%" }}>
      <text className="title">ScrollView Example</text>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "100%", paddingLeft: "5px", marginTop: "5px", marginLeft: "5px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => {
          if (index == 2) {
            return <StickyItem index={index} height={100} sticky={true} />;
          }
          return <VerticalScrollItem index={index} />;
        })}
      </scroll-view>
    </view>
  );
};
export default VerticalScrollContainer;
root.render(<VerticalScrollContainer />);

```



:::tip
`sticky`
 can only be set for direct child nodes of `<scroll-view>`
. On <AndroidOnly />
, you need to add the `flatten={false}`
 attribute to `sticky`
 nodes.
The direct child nodes of `<scroll-view>` only support `linear` and `sticky`. If you need more complex layouts, such as child nodes adapting to expand, it is recommended to provide a single child view to the `<scroll-view>` and implement more robust CSS capabilities within that single child node.

```javascript
<scroll-view> scroll-y>
  <view> // do anything you want
  {...}
  </view>
</scroll-view>
```

:::


## Attributes

### `bounces`

{' '}

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: true
bounces?: boolean;
```

Enable bounce effect

### `enable-scroll`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: true
'enable-scroll'?: boolean;
```

Enable dragging

### `initial-scroll-offset`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.17
</VersionBadge>

```tsx
// @defaultValue: 0
'initial-scroll-offset'?: number;
```

Initial scroll position, only effective once, in PX

### `initial-scroll-to-index`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.17
</VersionBadge>

```tsx
// @defaultValue: 0
'initial-scroll-to-index'?: number;
```

Scroll to specified child node on first screen, only effective once. All direct child nodes must be flatten=false.

### `lower-threshold`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: 0
'lower-threshold'?: number;
```

Set upper threshold to bindscrolltoupper event.

### `scroll-bar-enable`

{' '}

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: true
'scroll-bar-enable'?: boolean;
```

Enable scrollbar

### `scroll-orientation`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  3.0
</VersionBadge>

```tsx
// @defaultValue: 'vertical'
'scroll-orientation'?: 'vertical' | 'horizontal';
```

Replacement of scroll-x and scroll-y

### `upper-threshold`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: 0
'upper-threshold'?: number;
```

Set upper threshold to bindscrolltoupper event.

## Events

Frontend can bind corresponding event callbacks to listen for runtime behaviors of the element, as shown below.

### `bindcontentsizechanged`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  1.6
</VersionBadge>

```tsx
bindcontentsizechanged = (e: ContentSizeChangedEvent) => {};
```

This event is triggered when the scrollview's content size changed.

### `bindscroll`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
bindscroll = (e: ScrollEvent) => {};
```

This event is triggered when the scrollview is scrolling.

### `bindscrollend`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.6
</VersionBadge>

```tsx
bindscrollend = (e: ScrollEndEvent) => {};
```

This event is triggered when the scrollview's scroll ended.

### `bindscrolltolower`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
bindscrolltolower = (e: ScrollToLowerEvent) => {};
```

This event is triggered when the lower/right edge of the scrolling area intersects with the visible area defined by the lowerThreshold.

### `bindscrolltoupper`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
bindscrolltoupper = (e: ScrollToUpperEvent) => {};
```

This event is triggered when the upper/left edge of the scrolling area intersects with the visible area defined by the upperThreshold.

## Methods

Frontend can invoke component methods via the [SelectorQuery](/api/lynx-api/nodes-ref/nodes-ref-invoke.md) API.

### `autoScroll`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

```ts

lynx.createSelectorQuery()
.select('#id')
.invoke({
method: 'autoScroll',
params: {
/**
_ The distance of each second's scrolling, which supports positive and negative values. The unit of distance can be "px", "rpx", "ppx", or null (for iOS, the value must be greater than 1/screen.scale px).
_ @Android
_ @iOS
_ @Harmony
_ @PC
_/
rate: number;
/**
_ Start/stop automatic scrolling.
_ @Android
_ @iOS
_ @Harmony
_ @PC
_/
start: boolean;
};
success: function (res) {},
fail: function (res) {},
})
.exec();

```

Automatic scrolling

### `getScrollInfo`

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

```ts

lynx.createSelectorQuery()
     .select('#id')
     .invoke({
      method: 'getScrollInfo',
      success: Callback<{
        /**
         * Total scrollable range along orientation, in PX
         * @Android
         * @iOS
         * @Harmony
         * @PC
         */
        scrollRange: number;
        /**
         * Content offset on X-axis, in PX
         * @Android
         * @iOS
         * @Harmony
         * @PC
         */
        scrollX: number;
        /**
         * Content offset on Y-axis, in PX
         * @Android
         * @iOS
         * @Harmony
         * @PC
         */
        scrollY: number;
      }>;
      fail: function (res) {},
    })
    .exec();

```

Get scroll info

### `scrollBy`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

```ts

lynx.createSelectorQuery()
.select('#id')
.invoke({
method: 'scrollBy',
params: {
/\*\*
_ Offset to scroll
_/
offset?: number;
};
success: function (res) {},
fail: function (res) {},
})
.exec();

```

Scroll by specified offset

### `scrollTo`

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

```ts

lynx.createSelectorQuery()
     .select('#id')
     .invoke({
      method: 'scrollTo',
      params: {
        /**
         * Target item index
         * @defaultValue 0
         */
        index?: number;
        /**
         * Offset relative to target node
         */
        offset?: number;
        /**
         * Enable scroll animation
         */
        smooth?: boolean;
      };
      success: function (res) {},
      fail: function (res) {},
    })
    .exec();

```

Scroll to specified position

## Performance Optimization Suggestions

`<scroll-view>` creates all of its child nodes at once, potentially causing severe first-screen load times. Use exposure events to drive it to create only visible child nodes.

`<scroll-view>` lacks any reuse mechanism. If content is too extensive, it may consume an exceptionally large amount of memory, possibly causing OOM and other stability problems.

For data exceeding three screens, use `<list>` to optimize performance, or simulate `<VisualizedList>` logic based on exposure events.

## Compatibility

**Compatibility Table**
**Query:** `elements.scroll-view`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 1.5 | - |
| iOS | 1.5 | - |
| HarmonyOS | 3.4 | - |
| Clay Android | 1.5 | - |
| Clay iOS | 1.5 | - |
| Clay Windows | 1.5 | - |
| Clay macOS | 1.5 | - |
| Web | ✅ Yes | - |

**Description:** scroll-view

