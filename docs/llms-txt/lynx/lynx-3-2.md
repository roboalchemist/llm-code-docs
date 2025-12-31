# Source: https://lynxjs.org/blog/lynx-3-2.md

_May 14th, 2025_

# What’s new in Lynx 3.2

<BlogAvatar list={['shiwentao', 'lynx']} />

![lynx-in-3-2](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/blog/news-in-3.2/lynx-3-2.png)

Today, I'm pleased to share that Lynx 3.2, the first version of Lynx since we [open-sourced](/blog/lynx-unlock-native-for-more.md) it in March 2025, is now stable!

Lynx 3.2 delivers updates across its framework, engine, and tools, including the [ReactLynx testing tools](#reactlynx-testing-library), [`llms.txt` support](#websitellmstxt-support), [new Grid Layout features](#css-grid-layoutminmaxmax-contentfit-content), improvements to [`<list>`](#improvements-tolist) and [`<text>`](#text-can-be-customized-to-select-across-multiple-elements), and more, to bring you more familiar development experience and more capabilities. With over [296 commits](https://github.com/lynx-family/lynx/releases/) from 61 contributors (including some first-time contributors). Let’s explore what’s new!

## ReactLynx Testing Library

[Testing Library](https://testing-library.com/) is a popular way in the JavaScript community to test UI components, and we've adapted it for Lynx. We now introduce a new package [`@lynx-js/react/testing-library/`](/api/reactlynx-testing-library/index.md) to provide testing abstractions such as [`render`](/api/reactlynx-testing-library/Function.render.md). It can also be used with the official [`@testing-library/jest-dom`](https://github.com/testing-library/jest-dom) to assert the presence and behavior of elements using matchers such as [`toBeInTheDocument`](https://github.com/testing-library/jest-dom?tab=readme-ov-file#tobeinthedocument).

```js
import '@testing-library/jest-dom';
import { expect, it } from 'vitest';
import { render } from '@lynx-js/react/testing-library';

it('renders', () => {
  const Wrapper = ({ children }) => (
    <view data-testid="wrapper">{children}</view>
  );
  const Comp = () => (
    <view data-testid="inner" style="background-color: yellow;" />
  );
  const { container, getByTestId } = render(<Comp />, { wrapper: Wrapper });

  expect(getByTestId('wrapper')).toBeInTheDocument();
  expect(container.firstChild).toMatchInlineSnapshot(`
    <view data-testid="wrapper">
      <view data-testid="inner" style="background-color: yellow;"/>
    </view>
  `);
});
```

[Learn more about how to use ReactLynx Testing Library here.](/react/reactlynx-testing-library.md)

## Website: `llms.txt` Support

By upgrading to [Rspress v2](https://v2.rspress.dev/) and taking advantage of the new [LLM plugin](https://x.com/rspack_dev/status/1917844832149725695), the Lynx website is now fully equipped with [https://lynxjs.org/llms.txt](https://lynxjs.org/llms.txt) and [https://lynxjs.org/llms-full.txt](https://lynxjs.org/llms-full.txt) to help with AI understanding and improve your experience vibe-coding with Lynx. For every page you can get the original markdown by replacing the .html extension with .md.

[Learn more about what is `llms.txt`](https://llmstxt.org/).

## CSS Grid Layout: `minmax()`
, `max-content`
, `fit-content`
 <Badge>Web-friendly</Badge>

Lynx 3.2 adds three CSS functions `minmax()`, `max-content`, and `fit-content`, to help you better controll grid sizes in the [CSS Grid Layout](/guide/ui/layout/grid-layout.md). You can use them in `grid-template-columns`, `grid-template-rows`, `grid-auto-columns`, and `grid-auto-rows`.

Let's take a look at an example of building a three-column grid with `grid-template-columns: 20% max-content minmax(50px, max-content)`:

- First column: Takes up 20% of the container width
- Second column: Sizes itself to fit its content using `max-content`
- Third column: Uses `minmax(50px, max-content)` to have a minimum width of 50px but can grow to fit content

**This is an example below:  css**

**Entry:** `src/grid_layout`
**Bundle:** `dist/grid_layout.lynx.bundle` | Web: `dist/grid_layout.web.bundle`

```tsx {24}
import { root } from "@lynx-js/react";
import { useCallback, useEffect, useState } from "@lynx-js/react";
import arrow from "./assets/arrow.png";
import lynxLogo from "./assets/lynx-logo.png";
import reactLynxLogo from "./assets/react-logo.png";

import "./index.scss";
const GridComponent = () => {
  const [alterLogo, setAlterLogo] = useState(false);

  useEffect(() => {
    console.info("Hello, ReactLynx");
  }, []);

  const onTap = useCallback(() => {
    "background-only";
    setAlterLogo(!alterLogo);
  }, [alterLogo]);

  return (
    <page>
      <view className="Background" />
      <view className="Container">
        <view className="GridContainer" style={{ gridTemplateColumns: "20% max-content minmax(50px, max-content)" }}>
          <view className="Logo" bindtap={onTap}>
            {alterLogo
              ? <image src={reactLynxLogo} className="Logo--react" />
              : <image src={lynxLogo} className="Logo--lynx" />}
          </view>
          <text className="Title" style={{ alignSelf: "center" }}>No Wrap</text>
          <text className="Subtitle">min-width:50px, will fit the container</text>
        </view>
        <view className="Content">
          <image src={arrow} className="Arrow" />
          <text className="Description">Tap the logo and have fun!</text>
          <text className="Hint">
            Edit<text style={{ fontStyle: "italic" }}>{" src/index.tsx "}</text>
            to see updates!
          </text>
        </view>
      </view>
    </page>
  );
};
root.render(<GridComponent />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Improvements to `<list>`

### Scroll Snapping with `item-snap`

The [**scroll snapping**](/api/elements/built-in/list.md#item-snap) feature has graduated to a stable feature in Lynx 3.2. It provides smooth and easy to use pagination across all platforms, enabling developers to create feeds or carousels with precise scrolling interactions.

**This is an example below:  list**

**Entry:** `src/horizontal-snap`
```tsx {26}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root } from "@lynx-js/react";
import { HorizontalView } from "./horizontalView.jsx";
import { VerticalView } from "./verticalView.jsx";

const ListContainer = () => {
  return (
    <view
      style={{
        width: "100%",
        height: "100vh",
        display: "linear",
      }}
    >
      <list
        scroll-orientation="horizontal"
        list-type="single"
        span-count={1}
        style={{
          width: "100%",
          height: "20vh",
        }}
        item-snap={{ factor: 0, offset: -20 }}
      >
        {Array.from({ length: 50 }).map((item, index) => {
          return (
            <list-item
              item-key={`list-item-${index}`}
              key={`list-item-${index}`}
            >
              <HorizontalView index={index} />
            </list-item>
          );
        })}
      </list>
      <list
        scroll-orientation="vertical"
        list-type="single"
        span-count={1}
        style={{
          width: "100%",
          height: "80vh",
        }}
        item-snap={{ factor: 0, offset: 0 }}
      >
        {Array.from({ length: 50 }).map((item, index) => {
          return (
            <list-item
              item-key={`list-item-${index}`}
              key={`list-item-${index}`}
            >
              <VerticalView index={index} />
            </list-item>
          );
        })}
      </list>
    </view>
  );
};

root.render(<ListContainer />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



[Learn more about implementing Pagination with `item-snap`.](/api/elements/built-in/list.md#pagination-withitem-snap)

### `z-index`
 Support in `<list-item>`
 <Badge>Web-friendly</Badge>

Lynx 3.2 supports [**z-index**](/zh/api/css/properties/z-index.md) on `<list-item>`, allowing for more flexible adjustment of the view hierarchy of list items.

**This is an example below:  list**

**Entry:** `src/zIndex`
**Bundle:** `dist/zIndex.lynx.bundle` | Web: `dist/zIndex.web.bundle`

```tsx {23}
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
      preload-buffer-count={1} // add buffer
      style={{
        width: "100%",
        height: "100vh",
        listMainAxisGap: "5px",
        padding: "10px",
        zIndex: "0",
      }}
    >
      <list-item item-key={`list-item-over-flow`} key={`list-item-list-item-over-flow`} style={{ zIndex: "1" }}>
        <view style={{ width: "100%", height: "20px", backgroundColor: "red" }}>
          <text
            style={{
              fontSize: "16px",
              paddingLeft: "6px",
              paddingTop: "6px",
              height: "40px",
              overflow: "visible",
              background: "blue",
            }}
          >
            {`overflowView:z-index:1`}
          </text>
        </view>
      </list-item>

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



## `<text>`
 Can Be Customized to Select Across Multiple Elements <Badge>Web-friendly</Badge>

In long article scenarios, with the newly added [`custom-text-selection`](/api/elements/built-in/text.md#custom-text-selection) attribute, you can now [implement customized logic](/api/elements/built-in/text.md#crosstext-selection-and-copying) to select and copy text across text elements, making the text selection experience more similar to the Web.

**This is an example below:  text**

**Entry:** `src/cross_text_selection`
**Bundle:** `dist/cross_text_selection.lynx.bundle` | Web: `dist/cross_text_selection.web.bundle`

```tsx {31}
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root, useEffect } from "@lynx-js/react";
import type { CommonEvent, SelectorQuery, TouchEvent } from "@lynx-js/types";

import "./index.scss";

/**
 * Metadata for each <text> node: position, dimensions, and selection bounds.
 */
interface TextNodeInfo {
  id: string; // Unique identifier for the DOM node
  left: number; // X-coordinate of node's left edge
  top: number; // Y-coordinate of node's top edge
  width: number; // Width of the node's bounding box
  height: number; // Height of the node's bounding box
  startX: number; // Selected region's start X
  startY: number; // Selected region's start Y
  endX: number; // Selected region's end X
  endY: number; // Selected region's end Y
}

// Global storage for node info and selection handlers
let textsInfo: TextNodeInfo[] = [];
let handlers: Array<{ x: number; y: number; radius: number; startX: number; startY: number }> = [];
let startPosition = { x: 0, y: 0 }; // Initial touch point for selection
let isSelecting = false; // Flag: currently dragging a selection handle

const CrossTextSelection = () => {
  // useEffect hook to run code when the component mounts and unmounts
  useEffect(() => {
    console.log("component did mount");
    getTextNodeRect();
    return () => {
      console.log("component will unmount");
    };
  }, []);

  // Handle long press event to start text selection
  const handleLongPress = (e: CommonEvent) => {
    isSelecting = true;
    startPosition.x = e.detail.x;
    startPosition.y = e.detail.y;
    setSelection(e.detail.x, e.detail.y, e.detail.x, e.detail.y);
  };

  // Handle touch start event to check if the touch is on a handler
  const handleTouchStart = (e: TouchEvent) => {
    if (handlers.length === 0) {
      return;
    }
    const { x, y } = e.detail;
    for (const [index, handler] of handlers.entries()) {
      if (Math.pow(handler.x - x, 2) + Math.pow(handler.y - y, 2) < Math.pow(handler.radius, 2)) {
        isSelecting = true;
        const another = handlers[(index + 1) % 2];
        startPosition = { x: another.startX, y: another.startY };
        break;
      }
    }
  };

  // Handle touch move event to update the selection area
  const handleTouchMove = (e: TouchEvent) => {
    if (isSelecting) {
      setSelection(startPosition.x, startPosition.y, e.detail.x, e.detail.y);
    }
  };

  // Handle touch end event to finalize the selection
  const handleTouchEnd = (e: TouchEvent) => {
    if (isSelecting) {
      setSelection(startPosition.x, startPosition.y, e.detail.x, e.detail.y);
    }
    isSelecting = false;
  };

  // Handle tap event to clear the selection
  const handleTap = () => {
    if (handlers.length === 0) {
      return;
    }
    setSelection(-1, -1, -1, -1);
  };

  // Asynchronous function to get the bounding rectangles of text nodes
  async function getTextNodeRect() {
    let resArray = await new Promise<SelectorQuery[]>((resolve) => {
      lynx.createSelectorQuery()
        .selectAll("#container text")
        .fields(
          {
            // @ts-expect-error TODO(types): support `query` in `@lynx-js/types`
            query: true,
            id: true,
          },
          resolve,
        )
        .exec();
    });

    Promise.all(
      resArray.map((element) => {
        return new Promise<{
          top: number;
          left: number;
          width: number;
          height: number;
          id: string;
        }>((resolve) => {
          // @ts-expect-error TODO(types): support `query` in `@lynx-js/types`
          element.query
            .selectRoot()
            .invoke({
              method: "boundingClientRect",
              success: (res: {
                top: number;
                left: number;
                width: number;
                height: number;
                id: string;
              }) => {
                resolve(res);
              },
            })
            .exec();
        });
      }),
    ).then((values) => {
      textsInfo = [...values].map(({ top, left, width, height, id }) => ({
        id: String(id),
        left: Number(left),
        top: Number(top),
        width: Number(width),
        height: Number(height),
        startX: -1,
        startY: 0,
        endX: width,
        endY: height,
      }));
    });
  }

  // Function to execute text selection on a specific node
  function execSelection(
    node: TextNodeInfo,
    startX: number,
    startY: number,
    endX: number,
    endY: number,
    showStartHandle = true,
    showEndHandle = true,
  ) {
    lynx
      .createSelectorQuery()
      .select(`#${node.id}`)
      .invoke({
        method: "setTextSelection",
        params: {
          startX,
          startY,
          endX,
          endY,
          showStartHandle,
          showEndHandle,
        },
        success(res) {
          if (!res) {
            return;
          }
          const boxes = res.boxes || [];
          const hs = res.handles || [];
          if (Array.isArray(boxes) && boxes.length > 0) {
            node.startX = boxes[0].left;
            node.startY = boxes[0].top + boxes[0].height / 2;
            node.endX = boxes[boxes.length - 1].left + boxes[boxes.length - 1].width;
            node.endY = boxes[boxes.length - 1].top + boxes[boxes.length - 1].height / 2;
          } else {
            node.startX =
              node.startY =
              node.endX =
              node.endY =
                -1;
          }
          showStartHandle && (handlers[0] = { ...hs[0], startX: node.startX, startY: node.startY });
          showEndHandle && (handlers[1] = { ...hs[1], startX: node.endX, startY: node.endY });
        },
      })
      .exec();
    if (startX === -1) {
      node.startX = -1;
      handlers = [];
    }
  }

  // Function to set the text selection based on the start and end coordinates
  function setSelection(x1: number, y1: number, x2: number, y2: number) {
    const [[startX, startY], [endX, endY]] = [
      [x1, y1],
      [x2, y2],
    ].sort((a, b) => {
      if (a[1] === b[1]) {
        return a[0] - b[0];
      }
      return a[1] - b[1];
    });
    const clear: TextNodeInfo[] = [];
    const update: TextNodeInfo[] = [];
    for (const node of textsInfo) {
      if (
        (startY < node.top && node.top + node.height < endY)
        || (node.left <= startX && startX <= node.left + node.width && node.top <= startY
          && startY <= node.top + node.height)
        || (node.left <= endX && endX <= node.left + node.width && node.top <= endY && endY <= node.top + node.height)
      ) {
        update.push(node);
      } else if (node.startX !== -1) {
        clear.push(node);
      }
    }
    if (clear.length > 0 || update.length > 0) {
      for (const node of clear) {
        execSelection(node, -1, -1, -1, -1, false, false);
      }
      const start = update[0];
      const end = update[update.length - 1];
      if (update.length === 1) {
        execSelection(
          start,
          Math.max(0, startX - start.left),
          Math.max(0, startY - start.top),
          Math.min(start.width, endX - start.left),
          Math.min(start.height, endY - start.top),
          true,
          true,
        );
      } else if (update.length > 1) {
        execSelection(
          start,
          Math.max(0, startX - start.left),
          Math.max(0, startY - start.top),
          start.width,
          start.height,
          true,
          false,
        );
        for (let i = 1; i < update.length - 1; i++) {
          execSelection(update[i], 0, 0, update[i].width, update[i].height, false, false);
        }
        execSelection(
          end,
          0,
          0,
          Math.min(end.width, endX - end.left),
          Math.min(end.height, endY - end.top),
          false,
          true,
        );
      }
      return true;
    }
    return false;
  }

  return (
    <page>
      <view className="Background" />
      <view className="App">
        <view
          id="container"
          style={{ width: "90vw" }}
          className="Container"
          bindlongpress={handleLongPress}
          bindtouchstart={handleTouchStart}
          bindtouchmove={handleTouchMove}
          bindtouchend={handleTouchEnd}
          bindtap={handleTap}
        >
          <text id="0" text-selection={true} custom-text-selection={true} flatten={false} className="Title">
            This is title
          </text>
          <view className="SplitLine" />
          <text id="1" className="NormalText" text-selection={true} custom-text-selection={true} flatten={false}>
            1.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
            dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat justo id, feugiat leo.
            Cras eu elementum dui.
          </text>
          <view className="SplitLine" />
          <text id="2" className="NormalText" text-selection={true} custom-text-selection={true} flatten={false}>
            2.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
            dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat justo id, feugiat leo.
            Cras eu elementum dui.
          </text>
          <view className="SplitLine" />
          <text id="3" className="NormalText" text-selection={true} custom-text-selection={true} flatten={false}>
            3.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
            dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat justo id, feugiat leo.
            Cras eu elementum dui.
          </text>
        </view>
      </view>
    </page>
  );
};

export default CrossTextSelection;

root.render(<CrossTextSelection />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Microtasks <Badge>Web-friendly</Badge>

Before Lynx 3.2, Lynx did not support micro-task. The behavior of the following code is inconsistent with that in web browsers. In Lynx 3.2, `Promise` based on microtasks is implemented, and a new API [`lynx.queueMicrotask`](/api/lynx-api/lynx/lynx-queue-microtask.md) is delivered.

```js
setTimeout(() => {
  console.log('this is a timeout, will exec after');
}, 0);

Promise.resolve().then((value) => {
  console.log('this is a Promise, will exec before');
});
```

| Results in Lynx before 3.2                                                                                               | Results in Chrome                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| ![](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/blog/news-in-3.2/lynx-test-result.png) | ![](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/blog/news-in-3.2/chrome-test-result.png) |

## More `console`
 APIs <Badge>Web-friendly</Badge>

Lynx 3.2 further implements most of the [W3C-compliant](https://developer.mozilla.org/en-US/docs/Web/API/console) `console` APIs to provide a more comprehensive debugging experience. See the [API Reference](/api/lynx-api/global/console/assert.md) for more details.

<center>
  <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/blog/news-in-3.2/lynx-console.gif" width="400" height="400" align="center" />
</center>

## Rspeedy: Rslib and Rspack 1.3

Rspeedy [v0.9.0](https://github.com/lynx-family/lynx-stack/discussions/482) is now available, featuring significant improvements in size and performance. In v0.9.0, Rspeedy bundles with [Rslib](https://lib.rsbuild.dev/), reducing installation size by 50%. The upgrade to [Rspack](https://rspack.dev/) [1.3](https://rspack.dev/blog/announcing-1-3) delivers enhanced code splitting, optimized bundle size, and improved memory efficiency. Additional enhancements include new CLI flags and configurations. For more details, refer to the complete full CHANGELOG [`@lynx-js/rspeedy v0.9.0`](https://github.com/lynx-family/lynx-stack/blob/main/packages/rspeedy/core/CHANGELOG.md#090).

To upgrade, run the following command in your Rspeedy project:

```js
npx upgrade-rspeedy@latest
```

## DevTool: Screen Mirroring with Resolution Control

DevTool's screen mirroring feature, located in the left panel, now includes resolution switching capabilities. Users can toggle between High Definition (HD) and Standard Definition (SD) modes. The SD mode is particularly useful for reducing bandwidth consumption during unstable device connections, ensuring smoother screen mirroring performance.

Download the latest DevTool Desktop Application from the [DevTool Release](https://github.com/lynx-family/lynx-devtool/releases/tag/v0.0.2) page to get started.

<center>
  <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/blog/news-in-3.2/devtoolsopt.gif" width="800" height="800" />
</center>

## Upgrade to Lynx 3.2

### Android

Please refer to the [integrate-with-existing-apps](/guide/start/integrate-with-existing-apps.md#platform=ios) and update your Lynx and LynxService dependencies.

In your project's `build.gradle` or `build.gradle.kts` file, update the Lynx version as follows:

<Tabs groupId="update-lynx-3-2-with-existing-app">
  <Tab label="build.gradle">
    ```groovy title=build.gradle {3-6}
    dependencies {
        // lynx dependencies
        implementation "org.lynxsdk.lynx:lynx:3.2.0"
        implementation "org.lynxsdk.lynx:lynx-jssdk:3.2.0"
        implementation "org.lynxsdk.lynx:lynx-trace:3.2.0"
        implementation "org.lynxsdk.lynx:primjs:2.12.0"
    }
    ```
  </Tab>

  <Tab label="build.gradle.kts">
    ```groovy title=build.gradle.kts {3-6}
    dependencies {
        // lynx dependencies
        implementation("org.lynxsdk.lynx:lynx:3.2.0")
        implementation("org.lynxsdk.lynx:lynx-jssdk:3.2.0")
        implementation("org.lynxsdk.lynx:lynx-trace:3.2.0")
        implementation("org.lynxsdk.lynx:primjs:2.12.0")
    }
    ```
  </Tab>
</Tabs>

In your project's `build.gradle` or `build.gradle.kts` file, update the LynxService version:

<Tabs groupId="update-lynx-3-2-with-existing-app">
  <Tab label="build.gradle">
    <CodeFold height={360} toggle>
      ```groovy title=build.gradle {8-24}
      dependencies {
          // lynx dependencies
          implementation "org.lynxsdk.lynx:lynx:3.2.0"
          implementation "org.lynxsdk.lynx:lynx-jssdk:3.2.0"
          implementation "org.lynxsdk.lynx:lynx-trace:3.2.0"
          implementation "org.lynxsdk.lynx:primjs:2.12.0"

          // integrating image-service
          implementation "org.lynxsdk.lynx:lynx-service-image:3.2.0"

          // image-service dependencies, if not added, images cannot be loaded; if the host APP needs to use other image libraries, you can customize the image-service and remove this dependency
          implementation "com.facebook.fresco:fresco:2.3.0"
          implementation "com.facebook.fresco:animated-gif:2.3.0"
          implementation "com.facebook.fresco:animated-webp:2.3.0"
          implementation "com.facebook.fresco:webpsupport:2.3.0"
          implementation "com.facebook.fresco:animated-base:2.3.0"

          // integrating log-service
          implementation "org.lynxsdk.lynx:lynx-service-log:3.2.0"

          // integrating http-service
          implementation "org.lynxsdk.lynx:lynx-service-http:3.2.0"

          implementation "com.squareup.okhttp3:okhttp:4.9.0"

      }
      ```
    </CodeFold>
  </Tab>

  <Tab label="build.gradle.kts">
    <CodeFold height={360} toggle>
      ```groovy title=build.gradle.kts {8-24}
      dependencies {
          // lynx dependencies
          implementation("org.lynxsdk.lynx:lynx:3.2.0")
          implementation("org.lynxsdk.lynx:lynx-jssdk:3.2.0")
          implementation("org.lynxsdk.lynx:lynx-trace:3.2.0")
          implementation("org.lynxsdk.lynx:primjs:2.12.0")

          // integrating image-service
          implementation("org.lynxsdk.lynx:lynx-service-image:3.2.0-")

          // image-service dependencies, if not added, images cannot be loaded; if the host APP needs to use other image libraries, you can customize the image-service and remove this dependency
          implementation("com.facebook.fresco:fresco:2.3.0")
          implementation("com.facebook.fresco:animated-gif:2.3.0")
          implementation("com.facebook.fresco:animated-webp:2.3.0")
          implementation("com.facebook.fresco:webpsupport:2.3.0")
          implementation("com.facebook.fresco:animated-base:2.3.0")

          // integrating log-service
          implementation("org.lynxsdk.lynx:lynx-service-log:3.2.0")

          // integrating http-service
          implementation("org.lynxsdk.lynx:lynx-service-http:3.2.0")

          implementation("com.squareup.okhttp3:okhttp:4.9.0")
      }
      ```
    </CodeFold>
  </Tab>
</Tabs>

### iOS

In your project's `Podfile` file, update the Lynx version as follows:

<CodeFold height={360} toggle>
  ```ruby title="Podfile" {1,6-8,10}
  source 'https://cdn.cocoapods.org/'

  platform :ios, '10.0'

  target 'YourTarget' do
  pod 'Lynx', '3.2.0', :subspecs => [
  'Framework',
  ]

  pod 'PrimJS', '2.12.0', :subspecs => ['quickjs', 'napi']
  end
  ```
</CodeFold>

In your project's `Podfile` file, update the LynxService version as follows:

<CodeFold height={360} toggle>
  ```ruby title="Podfile" {8-13,15-17}
  source 'https://cdn.cocoapods.org/'
  platform :ios, '10.0'
  target 'YourTarget' do
    pod 'Lynx', '3.2.0', :subspecs => [
      'Framework',
    ]
    pod 'PrimJS', '2.12.0', :subspecs => ['quickjs', 'napi']
    # integrate image-service, log-service, and http-service
    pod 'LynxService', '3.2.0', :subspecs => [
        'Image',
        'Log',
        'Http',
    ]

    # ImageService
    pod 'SDWebImage','5.15.5'
    pod 'SDWebImageWebPCoder', '0.11.0'

  end
  ```
</CodeFold>

## Final Words

Thanks to Lynx community for making this release possible! As a newly open-source project, we're thrilled about our future and we can’t wait to see the use of Lynx in your apps.

In the future, we will gradually introduce more feature support as our [roadmap](/blog/lynx-open-source-roadmap-2025.md). We'll add new components like `<Input>` and adapt to more platforms such as HarmonyOS and PC.

Please check the [release notes and changelog](https://github.com/lynx-family/lynx/releases/tag/3.2.0), and let’s embark on a new adventure!

***

_Thanks to [Xuan Huang](https://x.com/huxpro), [Ray Zhang](https://x.com/zoolsher), and [Shouqun Liu](https://x.com/liushouqun) for their contributions in creating this blog post._
