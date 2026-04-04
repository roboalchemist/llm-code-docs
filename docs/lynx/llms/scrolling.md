# Source: https://lynxjs.org/guide/ui/scrolling.md

# Managing Scrolling

Overflow behavior occurs when the content of an element (its own content and child elements) exceeds the size of the element itself. During the process of building a page, it is inevitable to encounter situations of overflow. You can use the [`overflow`](/api/css/properties/overflow.md) property to crop the overflowing content, or use a \[scrollable element]\(#scrollable element to make the overflowing content scrollable, and control the scrolling direction of the content through the `scroll-orientation` property.

<table rules="none" align="center" width="100%" style={{ tableLayout: 'fixed' }}>
  <thead align="center">
    <th colSpan={2}>
      <span style={{ fontWeight: 'bold' }}>
        non-scrollable element
      </span>
    </th>

    <th colSpan={2}>
      <span style={{ fontWeight: 'bold' }}>
        scrollable element
      </span>
    </th>
  </thead>

  <tr>
    <td style={{ padding: '15px 0 15px 15px' }}>
      <center>
        <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/style-guide-overflow-visible.png" style={{ width: '70%', aspectRatio: '1/1' }} />
      </center>
    </td>

    <td style={{ padding: '15px 15px 15px 0' }}>
      <center>
        <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/style-guide-overflow-hidden.png" style={{ width: '70%', aspectRatio: '1/1' }} />
      </center>
    </td>

    <td style={{ padding: '15px 0 15px 15px' }}>
      <center>
        <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/guide-scroll-orientation-vertical.gif" style={{ width: '70%', aspectRatio: '1/1' }} />
      </center>
    </td>

    <td style={{ padding: '15px 15px 15px 0' }}>
      <center>
        <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/guide-scroll-orientation-horizontal.gif" style={{ width: '70%', aspectRatio: '1/1' }} />
      </center>
    </td>
  </tr>

  <tr>
    <td style={{ padding: '15px 0 15px 15px' }}>
      <center>
        <span>
          Content overflow has occurred.
        </span>
      </center>
    </td>

    <td style={{ padding: '15px 15px 15px 0' }}>
      <center>
        <span>
          crop the overflowing content through 

          <code>overflow: hidden</code>
        </span>
      </center>
    </td>

    <td style={{ padding: '15px 0 15px 15px' }}>
      <center>
        <span>
          <code>scroll-orientation: vertical</code>

           scrollable element 
        </span>
      </center>
    </td>

    <td style={{ padding: '15px 15px 15px 0' }}>
      <center>
        <span>
          <code>scroll-orientation: horizontal</code>

           scrollable element
        </span>
      </center>
    </td>
  </tr>
</table>

<Details title={<span>Doesn't support<code>overflow:scroll</code>for scrolling effect !</span>}>
  In `Lynx`, the `view` component doesn't support the scrolling effect achieved by `overflow: scroll` as in the Web. Only scrolling containers like `<scroll-view>` and `<list>` have the scrolling effect.
</Details>

## scrollable element

For some basic `<view>` element, the scrolling effect is not supported. Please use dedicated scroll container components [`<scroll-view>`](/api/elements/built-in/scroll-view.md) or [`<list>`](/api/elements/built-in/list.md).

### use `<scroll-view>` for basic scrolling

`<scroll-view>` is a basic scrolling component in `Lynx`. It allows users to scroll content vertically or horizontally within a fixed viewport area. Take the following figure as an example. When the height of the internal child nodes exceeds that of the parent `<scroll-view>` container, you only need to set the layout direction `scroll-orientation` to `vertical` to achieve the vertical scrolling effect.

**This is an example below:  scroll-view**

**Entry:** `src/event`
**Bundle:** `dist/vertical.lynx.bundle` | Web: `dist/vertical.web.bundle`

```tsx {9}
import { root } from "@lynx-js/react";
import { VerticalScrollItem } from "../component/scrollItem.jsx";

const VerticalScrollContainer = () => {
  return (
    <view style={{ width: "100%", height: "100%" }}>
      <text className="title">ScrollView Example</text>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "100%", paddingLeft: "10px", marginLeft: "5px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => <VerticalScrollItem index={index} />)}
      </scroll-view>
    </view>
  );
};

root.render(<VerticalScrollContainer />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### use `<list>` to manage large amount of data

`<scroll-view>` is used to display a small amount of data in a simple and intuitive way. On the other hand, `<list>` is suitable for scenarios where a large amount of data needs to be presented, or in scenarios with infinite scrolling for loading more content. It can adopt an on-demand loading way, rendering only the content in the visible area.

**This is an example below:  list**

**Bundle:** `dist/base.lynx.bundle` | Web: `dist/base.web.bundle`

```tsx {12-14}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root } from "@lynx-js/react";
import { ItemView } from "./baseView.jsx";

const ListContainer = () => {
  return (
    <list
      scroll-orientation="vertical"
      list-type="single"
      span-count={1}
      style={{
        width: "100%",
        height: "100vh",
        listMainAxisGap: "5px",
        padding: "10px",
      }}
    >
      {Array.from({ length: 50 }).map((item, index) => {
        return (
          <list-item
            item-key={`list-item-${index}`}
            key={`list-item-${index}`}
          >
            <ItemView index={index} />
          </list-item>
        );
      })}
    </list>
  );
};

root.render(<ListContainer />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### use `<list>` to handle complex layout

`<scroll-view>` only has the ability of linear layout, presenting elements in an orderly manner through linear arrangement. However, when facing complex interfaces, `<list>` offers a wide range of layout options. You can choose different layouts such as [flow](/api/elements/built-in/list.md#flow) and [waterfall](/api/elements/built-in/list.md#waterfall) to flexibly customize business requirements.

**This is an example below:  list**

**Entry:** `src/waterfall`
**Bundle:** `dist/waterfall.lynx.bundle` | Web: `dist/waterfall.web.bundle`

```tsx {14-16}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root } from "@lynx-js/react";

import "./index.scss";
import { ItemView } from "./baseView.jsx";

const ListContainer = () => {
  return (
    <list
      className="list-container"
      list-type="waterfall"
      span-count={2}
      scroll-orientation="vertical"
    >
      {Array.from({ length: 40 }).map((item, index) => {
        return (
          <list-item
            item-key={`list-item-${index}`}
            key={`list-item-${index}`}
          >
            <ItemView index={index} />
          </list-item>
        );
      })}
    </list>
  );
};

root.render(<ListContainer />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Additional Features

- sticky capability：`<scroll-view>`[sticky](/api/elements/built-in/scroll-view.md#sticky-capability)；`<list>`[sticky](/api/elements/built-in/list.md#implementing-sticky-nodes)

- `<list>` [paginated scrolling](/api/elements/built-in/list.md#implementing-paginated-scrolling)

- `<list>` [load more](/api/elements/built-in/list.md#implementing-load-more)
