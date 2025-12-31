# Source: https://lynxjs.org/guide/interaction/event-handling/event-propagation.md

# Event Propagation

When an event is triggered, it will propagate along the event response chain. If the corresponding type of event handler property is set on the node, the node can listen to the corresponding event or even intercept it during the event propagation process.

In addition, Lynx also provides cross-component event monitoring, event aspect interface, and `GlobalEventEmitter` to implement special event propagation.

## Event handler property

By setting the event handler properties, developers can decide at which stage (or across components) of event propagation to listen or intercept the event, and specify the processing function to be called when the event is triggered. The names of these event handler properties are usually composed of the bound event type and event name.

| Event Type      | Description                                                                         |
| --------------- | ----------------------------------------------------------------------------------- |
| `bind`          | Listen to events in the bubbling stage, and do not intercept event bubbling.        |
| `catch`         | Listen to events in the bubbling stage and intercept event bubbling.                |
| `capture-bind`  | Listen to events in the capture phase, do not intercept event capture and bubbling. |
| `capture-catch` | Listen to events in the capture phase, intercept event capture and bubbling.        |
| `global-bind`   | Listen to events across components.                                                 |

In particular, when the event handler is a [main thread script](/react/main-thread-script.md), you need to add the `main-thread:` prefix before the event handler property name to ensure that the handler is executed in the main thread.

## Event response chain

The event response chain refers to a linked list of nodes that can respond to events. Generally speaking, the event response chain consists of the path from the root node of the page to the node where the action is actually triggered. However, for non-[touch events](/api/lynx-api/event/touch-event.md), the event response chain only contains the node where the action is actually triggered.

**Example 1:**

**This is an example below:  event**

**Entry:** `src/event_chain`
**Bundle:** `dist/event_chain.lynx.bundle` | Web: `dist/event_chain.web.bundle`

```tsx {50,65,78,95,108}
import { root, useState } from "@lynx-js/react";
import type { TouchEvent } from "@lynx-js/types";

export default function App() {
  const [tap, setTap] = useState<boolean>(false);
  const [tap1, setTap1] = useState<boolean>(false);
  const [tap11, setTap11] = useState<boolean>(false);
  const [tap2, setTap2] = useState<boolean>(false);
  const [tap22, setTap22] = useState<boolean>(false);

  function handleTap(e: TouchEvent) {
    if (e.currentTarget.id === "tap") {
      setTap(!tap);
    }
    if (e.currentTarget.id === "tap1") {
      setTap1(!tap1);
    }
    if (e.currentTarget.id === "tap11") {
      setTap11(!tap11);
    }
    if (e.currentTarget.id === "tap2") {
      setTap2(!tap2);
    }
    if (e.currentTarget.id === "tap22") {
      setTap22(!tap22);
    }
  }

  function handletouchstart(e: TouchEvent) {
    setTap(false);
    setTap1(false);
    setTap11(false);
    setTap2(false);
    setTap22(false);
  }

  return (
    <view
      id="tap"
      style={{
        width: "calc(100% - 40px)",
        height: "90%",
        margin: "20px",
        borderRadius: "10px",
        boxShadow: "0 0 5px 5px #ccc",
        backgroundColor: tap ? "rgb(255, 179, 0)" : "white",
        justifyContent: "center",
        alignItems: "center",
      }}
      bindtap={handleTap}
      capture-bindtouchstart={handletouchstart}
    >
      <view
        id="tap1"
        style={{
          width: "70%",
          height: "40%",
          marginBottom: "25px",
          borderRadius: "10px",
          boxShadow: "0 0 5px 5px #ccc",
          backgroundColor: tap1 ? "rgb(255, 179, 0)" : "white",
          justifyContent: "center",
          alignItems: "center",
        }}
        bindtap={handleTap}
      >
        <view
          id="tap11"
          style={{
            width: "60%",
            height: "45%",
            borderRadius: "10px",
            boxShadow: "0 0 5px 5px #ccc",
            backgroundColor: tap11 ? "rgb(255, 179, 0)" : "white",
            justifyContent: "center",
            alignItems: "center",
          }}
          bindtap={handleTap}
        >
          <text user-interaction-enabled={false} style={{ color: "green" }}>click me 1</text>
        </view>
      </view>
      <view
        id="tap2"
        style={{
          width: "70%",
          height: "40%",
          marginTop: "25px",
          borderRadius: "10px",
          boxShadow: "0 0 5px 5px #ccc",
          backgroundColor: tap2 ? "rgb(255, 179, 0)" : "white",
          justifyContent: "center",
          alignItems: "center",
        }}
        bindtap={handleTap}
      >
        <view
          id="tap22"
          style={{
            width: "60%",
            height: "45%",
            borderRadius: "10px",
            boxShadow: "0 0 5px 5px #ccc",
            backgroundColor: tap22 ? "rgb(255, 179, 0)" : "white",
            justifyContent: "center",
            alignItems: "center",
          }}
          bindtap={handleTap}
        >
          <text user-interaction-enabled={false} style={{ color: "red" }}>click me 2</text>
        </view>
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



In the above example, when the user clicks on the page, the background color of the node on the event response chain will be set to orange.

## Event capture

The event will go through two stages in the event response chain: event capture and event bubbling. In the event capture stage, the event will start from the root node of the page and propagate down along the event response chain until the node where the action is actually triggered. In the event capture stage, nodes with the event handler property of the `capture-bind` type set can listen to the corresponding event.

**Example 2:**

**This is an example below:  event**

**Entry:** `src/event_capture`
**Bundle:** `dist/event_capture.lynx.bundle` | Web: `dist/event_capture.web.bundle`

```tsx {7-9,14}
import { root, useState } from "@lynx-js/react";
import type { TouchEvent } from "@lynx-js/types";

export default function App() {
  const [cnt, setCnt] = useState<number>(0);

  function handleTap(e: TouchEvent) {
    setCnt(cnt + 1);
  }

  return (
    <view
      style={{ width: "100%", height: "90%" }}
      capture-bindtap={handleTap}
    >
      <view
        style={{
          width: "calc(100% - 10px)",
          height: "150px",
          margin: "5px",
          borderWidth: "2px",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <text>
          Counts the number of clicks on a page: <text style={{ color: "red" }}>{cnt}</text>
        </text>
      </view>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "calc(100% - 150px)" }}
      >
        {[0, 1, 2, 3, 4, 5, 6].map((item) => {
          return (
            <view
              style={{
                width: "calc(100% - 10px)",
                height: "150px",
                margin: "5px",
                backgroundColor: `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${
                  Math.floor(Math.random() * 256)
                })`,
                borderRadius: "5px",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <text>item-{item + 1}</text>
            </view>
          );
        })}
      </scroll-view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



In the above example, since event propagation starts from the capture phase, and the capture phase starts from the root node, when the user clicks on the page, the root node can always listen to the `tap` event, thereby realizing the function of counting the number of page clicks.

## Event bubble

In the event bubbling phase, the event will propagate upward along the event response chain from the node where the action is actually triggered, until the root node of the page. In the event bubbling phase, nodes with the `bind` type event handler attribute set can listen to the corresponding event.

**Example 3**

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



In the above example, when the user clicks any node on the page, the event will bubble from the child node to the parent node by default. Therefore, the parent node can always listen to the `tap` event and change the background color of the node.

## Event interception

During the process of event propagation, the event can be intercepted midway to prevent the event from continuing to propagate. When the `catch` type event handler property is set on the node, the event will be intercepted when it propagates to the node and will no longer propagate.

**Example 4**

**This is an example below:  event**

**Entry:** `src/event_static_catch`
**Bundle:** `dist/event_static_catch.lynx.bundle` | Web: `dist/event_static_catch.web.bundle`

```tsx {7-12,23,34}
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
        catchtap={(e: TouchEvent) => {}}
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



In the above example, since the `click me` area sets the static interception `tap` event, the event will bubble to the parent node and the background color of the node will change only when the non-`click me` area is clicked.

## Prevent Event Propagation in Main Thread Script

When used with [Main Thread Script](/react/main-thread-script.md), event propagation can be prevented by calling the [`stopPropagation`](/api/lynx-api/event/event.md#stoppropagation) method of the event object.

**Example 5:**

**This is an example below:  event**

**Entry:** `src/event_stop_propagation`
**Bundle:** `dist/event_stop_propagation.lynx.bundle` | Web: `dist/event_stop_propagation.web.bundle`

```tsx {34}
import { root, runOnBackground, useState } from "@lynx-js/react";
import "./index.css";
import type { MainThread } from "@lynx-js/types";

export default function App() {
  const [active, setActive] = useState({ outer: false, middle: false, inner: false });

  // Utility to flash a box when it's clicked
  const flashBT = (key: "outer" | "middle" | "inner") => {
    setActive((prev) => ({ ...prev, [key]: true }));
    setTimeout(() => setActive((prev) => ({ ...prev, [key]: false })), 200);
  };

  // Utility to flash a box when it's clicked
  const flash = (
    key: "outer" | "middle" | "inner",
  ) => {
    "main thread";
    runOnBackground(flashBT)(key);
  };

  function handleOuterTap(e: MainThread.TouchEvent) {
    "main thread";
    flash("outer");
  }

  function handleMiddleTap(e: MainThread.TouchEvent) {
    "main thread";
    flash("middle");
  }

  function handleInnerTap(e: MainThread.TouchEvent) {
    "main thread";
    e.stopPropagation(); // ✋ stop event bubbling
    flash("inner");
  }

  return (
    <view
      main-thread:bindtap={handleOuterTap}
      className={`box outer ${active.outer ? "active" : ""}`}
    >
      <text>Outer {active.outer ? "(active)" : "(inactive)"}</text>
      <view
        main-thread:bindtap={handleMiddleTap}
        className={`box middle ${active.middle ? "active" : ""}`}
      >
        <text>Middle {active.middle ? "(active)" : "(inactive)"}</text>
        <view
          main-thread:bindtap={handleInnerTap}
          className={`box inner ${active.inner ? "active" : ""}`}
        >
          <text>Inner (click me, stops propagation) {active.inner ? "(active)" : "(inactive)"}</text>
        </view>
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



In the above example, click the inner will not trigger the `tap` event of the outer.

## Cross-component event listening <NoWeb />

Generally speaking, when a node is not on the event response chain, the event cannot be monitored. Lynx provides a way to monitor cross-component events, allowing developers to register event monitoring on any node and receive corresponding events.

For example, developers can set the event handler property of the `global-bind` type on a node to listen to the `tap` event. When any node is clicked, the node can listen to the `tap` event, thereby realizing the function of counting the number of page clicks.

**Example 5:**

**This is an example below:  event**

**Entry:** `src/event_global_bind`
**Bundle:** `dist/event_global_bind.lynx.bundle` | Web: `dist/event_global_bind.web.bundle`

```tsx {8-10,12-14,19-20,47-48}
import { root, useState } from "@lynx-js/react";
import type { TouchEvent } from "@lynx-js/types";

export function ComponentA() {
  const [scrollContainer, setScrollContainer] = useState<string>("");
  const [cnt, setCnt] = useState<number>(0);

  function handleScroll(e: TouchEvent) {
    setScrollContainer(e.target.id);
  }

  function handleTap(e: TouchEvent) {
    setCnt(cnt + 1);
  }

  return (
    <view
      style={{ width: "100%", height: "100%", justifyContent: "center", alignItems: "center" }}
      global-bindscroll={handleScroll}
      global-bindtap={handleTap}
    >
      <text>
        Counts the number of clicks on a page: <text style={{ color: "red" }}>{cnt}</text>
      </text>
      <text>
        Current scroll container: <text style={{ color: "green" }}>{scrollContainer}</text>
      </text>
    </view>
  );
}

export function ComponentB() {
  return (
    <view
      style={{
        width: "calc(100% - 10px)",
        height: "calc(100% - 45px)",
        marginTop: "40px",
        marginLeft: "5px",
        marginRight: "5px",
        marginBottom: "5px",
      }}
    >
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "50%", borderWidth: "2px" }}
        id="scroll-1"
        bindscroll={(e) => {}}
      >
        {[0, 1, 2, 3, 4, 5, 6].map((item) => {
          return (
            <view
              style={{
                width: "calc(100% - 10px)",
                height: "200px",
                margin: "5px",
                backgroundColor: "orange",
                borderRadius: "5px",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <text>scroll-1-item-{item + 1}</text>
            </view>
          );
        })}
      </scroll-view>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "calc(50% - 10px)", marginTop: "10px", borderWidth: "2px" }}
        id="scroll-2"
        bindscroll={(e) => {}}
      >
        {[0, 1, 2, 3, 4, 5, 6].map((item) => {
          return (
            <view
              style={{
                width: "calc(100% - 10px)",
                height: "200px",
                margin: "5px",
                backgroundColor: "purple",
                borderRadius: "5px",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <text>scroll-2-item-{item + 1}</text>
            </view>
          );
        })}
      </scroll-view>
    </view>
  );
}

export default function App() {
  return (
    <view style={{ width: "100%", height: "90%" }}>
      <view style={{ width: "100%", height: "150px", backgroundColor: "yellow" }}>
        <view style={{ position: "absolute" }}>
          <text style={{ color: "blue" }}>ComponentA</text>
        </view>
        <ComponentA />
      </view>
      <view style={{ width: "100%", height: "calc(100% - 165px)", marginTop: "15px", backgroundColor: "#ccc" }}>
        <view style={{ position: "absolute" }}>
          <text style={{ color: "blue" }}>ComponentB</text>
        </view>
        <ComponentB />
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



It should be noted that for non-[touch events](/api/lynx-api/event/touch-event.md), the event handler property of the non-cross-component event listening type needs to be set on the monitored node. In addition, developers can also set `global-target` on the node to specify that only events with a specific value of the node [`id`](/api/elements/built-in/view.md#id) are listened (type is `string`, multiple [`id`](/api/elements/built-in/view.md#id) can be specified, separated by commas).

## Event aspect interface

Sometimes, developers may need to uniformly listen to and handle events of a specific type somewhere, and do not rely on component registration event listeners. For example, count all triggered `tap` events on the page. At this time, developers can use the event aspect interface ([`beforePublishEvent`](/api/lynx-api/lynx/lynx-before-publish-event.md)) provided by Lynx to implement the corresponding function.

**Example 6:**

**This is an example below:  event**

**Entry:** `src/event_aop`
**Bundle:** `dist/event_aop.lynx.bundle` | Web: `dist/event_aop.web.bundle`

```tsx {7-12,65}
import { root, useMemo, useState } from "@lynx-js/react";
import type { TouchEvent } from "@lynx-js/types";

export default function App() {
  const [cnt, setCnt] = useState<number>(0);

  useMemo(() => {
    "background-only";
    lynx.beforePublishEvent.add("tap", () => {
      setCnt((cnt) => cnt + 1);
    });
  }, []);

  return (
    <view
      style={{ width: "100%", height: "90%" }}
    >
      <view
        style={{
          width: "calc(100% - 10px)",
          height: "150px",
          margin: "5px",
          borderWidth: "2px",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <text>
          Counts the number of clicks on a page: <text style={{ color: "red" }}>{cnt}</text>
        </text>
      </view>
      <scroll-view
        scroll-orientation="vertical"
        style={{ width: "100%", height: "calc(100% - 150px)" }}
      >
        {[0, 1].map((item) => {
          return (
            <view
              style={{
                width: "calc(100% - 10px)",
                height: "150px",
                margin: "5px",
                backgroundColor: "yellow",
                borderRadius: "5px",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <text>{"Don't listen tap event-" + (item + 1)}</text>
            </view>
          );
        })}
        {[0, 1, 2, 3].map((item) => {
          return (
            <view
              style={{
                width: "calc(100% - 10px)",
                height: "150px",
                margin: "5px",
                backgroundColor: "orange",
                borderRadius: "5px",
                justifyContent: "center",
                alignItems: "center",
              }}
              bindtap={(e: TouchEvent) => {}}
            >
              <text>{"Listen tap event-" + (item + 1)}</text>
            </view>
          );
        })}
      </scroll-view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



The event aspect interface is a type of aspect programming. By injecting the corresponding interface at the event trigger point, the event is forwarded to a certain place when a specific event is triggered. This interface is only implemented in the BTS context. Therefore, it can only be used in the background thread, and the corresponding event can only be listened to when the event processing function is triggered.

## `GlobalEventEmitter`

Sometimes, developers may need to pass events between different elements and components, or need to pass events between the client and the front end, and do not rely on the element to register event listeners. At this time, developers can use `GlobalEventEmitter` to achieve global scope transmission of events in a page.

Developers can obtain the `GlobalEventEmitter` object through [`lynx.getJSModule`](/api/lynx-api/lynx/lynx-get-js-module.md), which provides the following interfaces:

| Function name        | Function description                                                                        | Function parameter                |
| -------------------- | ------------------------------------------------------------------------------------------- | --------------------------------- |
| `addListener`        | Subscribe to events and register event listeners.                                           | `(eventName, listener, context?)` |
| `removeListener`     | Remove the specified listener for a specific event.                                         | `(eventName, listener)`           |
| `removeAllListeners` | Remove all listeners for a specific event.                                                  | `(eventName)`                     |
| `toggle`             | Broadcast an event with a specified event name, supporting multiple transparent parameters. | `(eventName, ...data)`            |
| `trigger`            | Broadcasts an event with a specified event name, supporting a transparent parameter.        | `(eventName, params)`             |

Note that `GlobalEventEmitter` is only supported in the BTS context, so it can only be used in background threads.

### Event broadcast

Developers can broadcast events through `GlobalEventEmitter` to send events to the front end.

In the following example, when the user clicks on the page, the developer broadcasts the event by calling the `toggle` method of `GlobalEventEmitter`, so that the click event is propagated from component `ComponentA` to `ComponentB`.

**Example 7:**

**This is an example below:  event**

**Entry:** `src/event_emitter_toggle`
**Bundle:** `dist/event_emitter_toggle.lynx.bundle` | Web: `dist/event_emitter_toggle.web.bundle`

```tsx {8-10,22-24,41}
import { root, useState } from "@lynx-js/react";
import { useLynxGlobalEventListener } from "@lynx-js/react";
import type { TouchEvent } from "@lynx-js/types";

export function ComponentA() {
  const [eventLog, setEventlog] = useState<string>("");

  useLynxGlobalEventListener("tapitem", (e) => {
    setEventlog((e as TouchEvent).target.dataset.item);
  });

  return (
    <view style={{ width: "100%", height: "100%", justifyContent: "center", alignItems: "center" }}>
      <text>
        Tap on item-<text style={{ color: "red" }}>{eventLog}</text>
      </text>
    </view>
  );
}

export function ComponentB() {
  function handleTap(e: TouchEvent) {
    lynx.getJSModule("GlobalEventEmitter").toggle("tapitem", e);
  }

  return (
    <scroll-view
      scroll-orientation="vertical"
      style={{ width: "100%", height: "calc(100% - 40px)", marginTop: "40px" }}
    >
      {[0, 1, 2, 3, 4, 5, 6].map((item) => {
        return (
          <view
            style={{
              width: "calc(100% - 10px)",
              height: "200px",
              margin: "5px",
              backgroundColor: "orange",
              borderRadius: "5px",
              justifyContent: "center",
              alignItems: "center",
            }}
            data-item={item + 1}
            bindtap={handleTap}
          >
            <text user-interaction-enabled={false}>item-{item + 1}</text>
          </view>
        );
      })}
    </scroll-view>
  );
}

export default function App() {
  return (
    <view style={{ width: "100%", height: "90%" }}>
      <view
        style={{ width: "100%", height: "150px", backgroundColor: "yellow" }}
      >
        <view style={{ position: "absolute" }}>
          <text style={{ color: "blue" }}>ComponentA</text>
        </view>
        <ComponentA />
      </view>
      <view
        style={{
          width: "100%",
          height: "calc(100% - 165px)",
          marginTop: "15px",
          backgroundColor: "#ccc",
        }}
      >
        <view style={{ position: "absolute" }}>
          <text style={{ color: "blue" }}>ComponentB</text>
        </view>
        <ComponentB />
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



For the client, the example is as follows:

<PlatformTabs queryKey="platform">
  <PlatformTabs.Tab platform="ios">
    ```objective-c
    // You can call the sendGlobalEvent function of LynxContext
    // The first parameter is the event name monitored by the front end, and the second parameter is the data received by the front end
    [LynxContext sendGlobalEvent:@"eventName" withParams:args];
    // Or call the sendGlobalEvent function of LynxView
    [LynxView sendGlobalEvent:@"eventName" withParams:args];
    ```
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="android">
    ```java
    // You can call the sendGlobalEvent function of LynxContext
    // The first parameter is the event name monitored by the front end, and the second parameter is the data received by the front end
    LynxContext.sendGlobalEvent("eventName", args);
    // Or call the sendGlobalEvent function of LynxView
    LynxView.sendGlobalEvent("eventName", args);
    ```
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="harmony">
    ```js
    // You can call the sendGlobalEvent function of LynxContext
    // The first parameter is the event name monitored by the front end, and the second parameter is the data received by the front end
    LynxContext.sendGlobalEvent('eventName', args);
    ```
  </PlatformTabs.Tab>
</PlatformTabs>

### Event subscribe

Developers can also subscribe to events through the `addListener` method of `GlobalEventEmitter` to receive events from the front end and client.

In the following example, users can receive the [`onWindowResize`](/api/lynx-api/event/global-event.md#onwindowresize) event sent by Lynx, which is triggered when the Lynx page size changes.

**Example 8:**

**This is an example below:  event**

**Entry:** `src/event_emitter_listen`
**Bundle:** `dist/event_emitter_listen.lynx.bundle` | Web: `dist/event_emitter_listen.web.bundle`

```tsx {7-9}
import { root, useState } from "@lynx-js/react";
import { useLynxGlobalEventListener } from "@lynx-js/react";

export default function App() {
  const [eventLog, setEventLog] = useState<string>("");
  useLynxGlobalEventListener("onWindowResize", (e) => {
    setEventLog("" + e);
  });

  return (
    <view
      style={{
        width: "100%",
        height: "100%",
        borderWidth: "1px",
        borderColor: "red",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <text>Listen onWindowResize Event:</text>
      <text>
        LynxView's width has changed to: <text style={{ color: "red" }}>{eventLog}</text>
      </text>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```


