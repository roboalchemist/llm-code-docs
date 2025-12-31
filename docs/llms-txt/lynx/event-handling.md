# Source: https://lynxjs.org/guide/interaction/event-handling.md

# Event Handling

Lynx provides an event mechanism similar to the Web, allowing developers to design and implement custom interaction logic based on events.

However, unlike the Web system, Lynx's event response mechanism supports dual-threaded processing. This means that event handling functions can be executed in the main thread or background thread as needed, thereby optimizing performance and response speed.

## What is an event

An event is a signal that triggers an action in the system. When an event is triggered, developers can implement the corresponding logic by listening to the event and executing the corresponding code. For example, developers can listen to click events and modify the background color of a node when a user clicks on the page.

**Example 1:**

**This is an example below:  event**

**Entry:** `src/event_bubble`
**Bundle:** `dist/event_bubble.lynx.bundle` | Web: `dist/event_bubble.web.bundle`

```tsx {7-12,23}
import { root, useState } from "@lynx-js/react";
import type { TouchEvent } from "@lynx-js/types";

export default function App() {
  const [bgColor, setBgColor] = useState<string>("white");

  function handleTap(e: TouchEvent) {
    const rndCol = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${
      Math.floor(Math.random() * 256)
    })`;
    setBgColor(rndCol);
  }

  return (
    <view
      style={{
        width: "100%",
        height: "100%",
        backgroundColor: bgColor,
        justifyContent: "center",
        alignItems: "center",
      }}
      bindtap={handleTap}
    >
      <view
        style={{
          width: "100px",
          height: "50px",
          borderRadius: "5px",
          backgroundColor: "gray",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <text style={{ color: "red" }}>click me</text>
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Listen for user clicks

When a user clicks on a page, the system triggers a `tap` event.

<img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/event/event_handling.png" width="100%" height="40%" />

As shown in the figure, developers can choose to handle the event in the main thread or the background thread.

- When timely event response is not required, you can choose to handle the event in the background thread, and the event processing of the background thread will not block the main thread.

- When timely event response is required, you can choose to handle the event in the main thread, which can avoid event delays caused by cross-threading, but it should be noted that excessive event processing may cause the main thread to be busy.

Specifically, if developers want to listen to the click event of a certain node, they can set the event handler property of type `bind` on the node:

```tsx
<view bindtap={handleTap} />
```

If the event handling function runs on the main thread, you need to add an additional `main-thread:` prefix before the event handler property, for example:

```tsx
<view main-thread:bindtap={handleTapInMTS} />
```

<Details title="How to intercept or specifically listen to an event?">
  In Lynx
  , the event handler property can also implement event interception and cross-component event listening. For details, please refer to [Event Propagation](/guide/interaction/event-handling/event-propagation.md).
</Details>

## Handling user clicks

When an event is triggered on a node, the event handling function set by the event handler property will be called. This function will receive an event object as a parameter, which contains detailed information about the event.

<Details title="What are the event objects?">
  All event objects inherit from [Event](/api/lynx-api/event/event.md). Developers
  can write event processing logic based on event objects in event processing
  functions.
</Details>

When the event processing function is a [main thread script](/react/main-thread-script.md), you need to add a [`'main thread'`](/api/react/Document.directives.md#main-thread) directive to the first line of the function body to indicate that the function runs on the main thread.

### Main thread event processing

In Lynx, the event objects of the main thread and the background thread are different. The event object of the background thread is a pure `json` object, while the event object of the main thread is an operable `Event Object`.

<Details title="How to operate nodes based on event objects?">
  Lynx provides a variety of ways to operate nodes, please refer to
  [Manipulating
  elements](/guide/interaction/event-handling/manipulating-element.react.md) for
  details.
</Details>

For example, for **Example 1**, when the developer chooses to handle events in the main thread, he can directly get [`e.currentTarget`](/api/lynx-api/event/event.md#currenttarget) in the [main thread script](/react/main-thread-script.md) and call [`setStyleProperty`](/api/lynx-api/main-thread/main-thread-element.md#elementsetstyleproperty) to modify the background color of the node.

**Example 2**

**This is an example below:  event**

**Entry:** `src/event_node_eom`
**Bundle:** `dist/event_node_eom.lynx.bundle` | Web: `dist/event_node_eom.web.bundle`

```tsx {4-11,16}
import { root } from "@lynx-js/react";
import type { MainThread } from "@lynx-js/types";

export default function App() {
  function handleTapInMTS(e: MainThread.TouchEvent) {
    "main thread";
    const rndCol = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${
      Math.floor(Math.random() * 256)
    })`;
    e.currentTarget.setStyleProperty("background-color", rndCol);
  }

  return (
    <view
      style={{ width: "100%", height: "100%", justifyContent: "center", alignItems: "center" }}
      main-thread:bindtap={handleTapInMTS}
    >
      <view
        style={{
          width: "100px",
          height: "50px",
          borderRadius: "5px",
          backgroundColor: "gray",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <text style={{ color: "red" }}>click me</text>
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Background thread event processing

For the event processing function of the background thread, developers cannot directly operate the node through [`e.currentTarget`](/api/lynx-api/event/event.md#currenttarget), but can obtain the node reference through [`SelectorQuery`](/api/lynx-api/selector-query.md) and then call [`setNativeProps`](/api/lynx-api/nodes-ref/nodes-ref-set-native-props.md) Modify the background color of the node.

**Example 3:**

**This is an example below:  event**

**Entry:** `src/event_node_sq`
**Bundle:** `dist/event_node_sq.lynx.bundle` | Web: `dist/event_node_sq.web.bundle`

```tsx {5-16,21}
import { root } from "@lynx-js/react";
import type { NodesRef, SelectorQuery, TouchEvent } from "@lynx-js/types";

export default function App() {
  function handleTap(e: TouchEvent) {
    const rndCol = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${
      Math.floor(Math.random() * 256)
    })`;
    (lynx
      .createSelectorQuery() as { selectUniqueID(uid: number): NodesRef } & SelectorQuery)
      .selectUniqueID(e.currentTarget.uid)
      .setNativeProps({
        "background-color": rndCol,
      })
      .exec();
  }

  return (
    <view
      style={{ width: "100%", height: "100%", justifyContent: "center", alignItems: "center" }}
      bindtap={handleTap}
    >
      <view
        style={{
          width: "100px",
          height: "50px",
          borderRadius: "5px",
          backgroundColor: "gray",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <text style={{ color: "red" }}>click me</text>
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Summary

So far, you have learned how to listen to user clicks and perform corresponding operations based on the event object.

For developers, Lynx events provide a Web-like API, but with a unique dual-threaded event response mechanism, allowing developers to choose to perform event processing in the main thread or background thread as needed, thereby optimizing performance and response speed.
