# Source: https://lynxjs.org/guide/interaction/event-handling/manipulating-element.react.md

# Direct Manipulation of Elements

In daily development, modern front-end frameworks handle most element tree and node property updates for us. However, there are times when you need to manipulate elements directly, such as controlling media players, manipulating view behavior, getting element information, or directly modifying styles.

These functionalities are typically implemented by components on the client side, and you need to access them through element references.

## Manipulating Elements in Background Thread

### Example: Auto-scrolling

Let's try a simple requirement - auto-scrolling the page. We need to call the [`autoScroll`] method of the `<scroll-view />` element:

**This is an example below:  element-manipulation**

**Entry:** `src/ref-background`
**Bundle:** `dist/ref-background.lynx.bundle`

```tsx {7,10-18,28}
import { useRef } from "@lynx-js/react";
import type { NodesRef } from "@lynx-js/types";

import { ScrollItem } from "../component/scrollItem.jsx";

export const App = () => {
  const scrollRef = useRef<NodesRef>(null);

  const handleTap = () => {
    scrollRef.current
      ?.invoke({
        method: "autoScroll",
        params: {
          rate: 120,
          start: true,
        },
      })
      .exec();
  };

  return (
    <view
      style={{
        width: "100%",
        height: "100%",
        padding: "10px",
        display: "linear",
        marginTop: "20px",
      }}
    >
      <view bindtap={handleTap}>
        <text
          style={{
            fontSize: "20px",
            height: "40px",
            paddingLeft: "10px",
            marginTop: "10px",
          }}
        >
          Tap me to enable auto-scroll
        </text>
      </view>
      <scroll-view
        ref={scrollRef}
        scroll-orientation="vertical"
        style={{ width: "100%", height: "100%", paddingLeft: "5px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => (
          <ScrollItem width="calc(100% - 10px)" height="100px" index={index} />
        ))}
      </scroll-view>
    </view>
  );
};

```



This example demonstrates two steps for manipulating elements: creating a reference using `useRef` and binding it to the target element using `ref={scrollRef}`, then calling the element method using `invoke()` in the event handler.

### Obtaining a Reference to an Element Using `ref`

If you're familiar with React, you'll find that using `ref` is very similar:

```tsx
const nodeRef = useRef<NodesRef>(null);
// ...
<text ref={nodeRef} />;
```

However, note that in Lynx, the type of node reference is [`NodesRef`], which is different from React. If you want to learn more about using references, you can refer to [Manipulating the Element with Refs](https://react.dev/learn/manipulating-the-dom-with-refs).

### Manipulating an Element via Its Reference

After obtaining a node reference, let's see how to use it. [`NodesRef`] provides a series of useful APIs.

For example, you can use [`NodesRef.invoke()`](/api/lynx-api/nodes-ref/nodes-ref-invoke.md) to call the element's methods. Each component provides specific methods that are implemented on the client side and exposed for front-end use.

When calling a method, you can pass required parameters through `params`, handle successful results using the `success` callback, and handle potential errors using the `fail` callback. Remember to call [`exec()`](/api/lynx-api/selector-query/selector-query-exec.md) at the end to submit the operation for actual execution:

```tsx
ref
  .invoke({
    method: 'boundingClientRect',
    params: {
      relativeTo: 'screen',
    },
    success: (res) => {
      // Handle successful result
      const { left, top, width, height } = res;
    },
    fail: (err) => {
      // Handle potential errors
      console.error('Failed to get element position:', err);
    },
  })
  .exec();
```

## Manipulating Elements in Main Thread

If you want better performance and more intuitive code, you can consider manipulating elements in the main thread. It offers lower operation latency with faster UI response and more natural API calls.

Let's see how to implement the same functionality in the main thread:

**This is an example below:  element-manipulation**

**Entry:** `src/ref-main-thread`
**Bundle:** `dist/ref-main-thread.lynx.bundle`

```tsx {7,10-14,19,25}
import { useMainThreadRef } from "@lynx-js/react";
import { MainThread } from "@lynx-js/types";

import { ScrollItem } from "../component/scrollItem.jsx";

export const App = () => {
  const scrollRef = useMainThreadRef<MainThread.Element>(null);

  const handleTap = () => {
    "main thread";
    scrollRef.current?.invoke("autoScroll", {
      rate: 120,
      start: true,
    });
  };

  return (
    <view
      style={{
        width: "100%",
        height: "100%",
        padding: "10px",
        display: "linear",
        marginTop: "20px",
      }}
    >
      <view main-thread:bindtap={handleTap}>
        <text
          style={{
            fontSize: "20px",
            height: "40px",
            paddingLeft: "10px",
            marginTop: "10px",
          }}
        >
          Tap me to enable auto-scroll
        </text>
      </view>
      <scroll-view
        main-thread:ref={scrollRef}
        scroll-orientation="vertical"
        style={{ width: "100%", height: "100%", paddingLeft: "5px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => (
          <ScrollItem width="calc(100% - 10px)" height="100px" index={index} />
        ))}
      </scroll-view>
    </view>
  );
};

```



The main changes here are: node operations need to be written in [main thread functions](/api/react/Document.directives.md#main-thread); using [`useMainThreadRef`] and `main-thread:ref` to get the main thread node reference; the node reference type becomes [`MainThread.Element`], which provides various methods for manipulating nodes; and we used [`MainThread.Element.invoke()`] to call the node's [`autoScroll`] method.

## Obtaining Element References via Selectors

In certain scenarios, such as when you need to batch operate on elements or dynamically find elements, using selectors can be particularly useful.

### Background Thread

In the background thread, we can use the [`SelectorQuery`] API to find elements. Let's look at an example:

**This is an example below:  element-manipulation**

**Entry:** `src/selector-query-background`
**Bundle:** `dist/selector-query-background.lynx.bundle`

```tsx {5-6}
import { ScrollItem } from "../component/scrollItem.jsx";

export const App = () => {
  const handleTap = () => {
    lynx
      .createSelectorQuery()
      .select("scroll-view")
      .invoke({
        method: "autoScroll",
        params: {
          rate: 120,
          start: true,
        },
      })
      .exec();
  };

  return (
    <view
      style={{
        width: "100%",
        height: "100%",
        padding: "10px",
        display: "linear",
        marginTop: "20px",
      }}
    >
      <view bindtap={handleTap}>
        <text
          style={{
            fontSize: "20px",
            height: "40px",
            paddingLeft: "10px",
            marginTop: "10px",
          }}
        >
          Tap me to enable auto-scroll
        </text>
      </view>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "100%", paddingLeft: "5px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => (
          <ScrollItem width="calc(100% - 10px)" height="100px" index={index} />
        ))}
      </scroll-view>
    </view>
  );
};

```



Using selectors is simple: first create a query object using [`lynx.createSelectorQuery()`], then use methods like [`select()`] to find elements. To learn about all supported selectors, you can check our [API documentation](/api/lynx-api/selector-query.md).

### Main Thread

When manipulating elements in the main thread, things become even simpler. You can use the browser-like [`lynx.querySelector()`] API:

**This is an example below:  element-manipulation**

**Entry:** `src/selector-query-main-thread`
**Bundle:** `dist/selector-query-main-thread.lynx.bundle`

```tsx {6-9}
import { ScrollItem } from "../component/scrollItem.jsx";

export const App = () => {
  const handleTap = () => {
    "main thread";
    lynx.querySelector("scroll-view")?.invoke("autoScroll", {
      rate: 120,
      start: true,
    });
  };

  return (
    <view
      style={{
        width: "100%",
        height: "100%",
        padding: "10px",
        display: "linear",
        marginTop: "20px",
      }}
    >
      <view main-thread:bindtap={handleTap}>
        <text
          style={{
            fontSize: "20px",
            height: "40px",
            paddingLeft: "10px",
            marginTop: "10px",
          }}
        >
          Tap me to enable auto-scroll
        </text>
      </view>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "100%", paddingLeft: "5px" }}
      >
        {Array.from({ length: 20 }).map((item, index) => (
          <ScrollItem width="calc(100% - 10px)" height="100px" index={index} />
        ))}
      </scroll-view>
    </view>
  );
};

```



## Obtaining a Reference to the Event Target Element

When handling events, we often need to manipulate the element that triggered the event.

### Main Thread

In the main thread, you can get the element reference directly from the event object. Similar to browsers, we provide [`target`] and [`currentTarget`] properties:

**This is an example below:  element-manipulation**

**Entry:** `src/event-main-thread`
**Bundle:** `dist/event-main-thread.lynx.bundle`

```tsx {6-9}
import type { MainThread } from "@lynx-js/types";

export const App = () => {
  function handleTap(e: MainThread.TouchEvent) {
    "main thread";
    e.currentTarget.setStyleProperty(
      "color",
      "linear-gradient(to right, rgb(255,53,26), rgb(0,235,235))",
    );
  }

  return (
    <view>
      <text
        style={{
          fontSize: "20px",
          height: "40px",
          paddingLeft: "10px",
          marginTop: "10px",
        }}
        main-thread:bindtap={handleTap}
      >
        Tap me to change my color!
      </text>
    </view>
  );
};

```



Here we used [`MainThread.Element.setStyleProperty()`] to modify styles.

## Using `getElementById` API

[`getElementById`] is currently our main API for handling animations and CSS variables. Although this is a traditional interface, it's still the best choice when you need to execute JavaScript animations or dynamically modify CSS variable values.

To learn more about usage, you can check [Animation API documentation](/api/lynx-api/lynx/lynx-animate-api.md) and [CSS Variables Operation Guide](/api/css/properties/css-variable.md). We are developing more modern APIs to replace [`getElementById`], stay tuned.

[`autoScroll`]: /api/elements/built-in/scroll-view.md#autoscroll

[`currentTarget`]: /api/lynx-api/event/event.md#currentTarget

[`getElementById`]: /api/lynx-api/lynx/lynx-get-element-by-id.md

[`lynx.createSelectorQuery()`]: /api/lynx-api/lynx/lynx-create-selector-query.md

[`lynx.querySelector()`]: /api/lynx-api/main-thread/lynx-query-selector.md

[`MainThread.Element`]: /api/lynx-api/main-thread/main-thread-element.md

[`MainThread.Element.invoke()`]: /api/lynx-api/main-thread/main-thread-element.md#elementinvoke

[`MainThread.Element.setStyleProperty()`]: /api/lynx-api/main-thread/main-thread-element.md#elementsetstyleproperty

[`NodesRef`]: /api/lynx-api/nodes-ref.md

[`select()`]: /api/lynx-api/selector-query/selector-query-select.md

[`SelectorQuery`]: /api/lynx-api/selector-query.md

[`target`]: /api/lynx-api/event/event.md#target

[`useMainThreadRef`]: /api/react/Function.useMainThreadRef.md
