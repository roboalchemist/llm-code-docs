# Source: https://lynxjs.org/guide/interaction/visibility-detection/exposure-ability.md

# Exposure Ability

The exposure capability provides a capability to observe changes in the visibility of a target node. When a target node changes from invisible to visible, an exposure event is triggered. Otherwise, an anti-exposure event is triggered.

Developers can monitor the exposure/anti-exposure events of nodes by setting relevant properties for the target nodes to be observed, thereby achieving requirements such as point reporting and `UI` lazy loading.

The exposure capability observes changes in node visibility through timed exposure detection tasks. The visibility of a node depends on the following factors:

- Visibility of the target node: The target node itself has width and height and is opaque, and the parent node has no clipping with zero width or height.
- Viewport intersection of the target node: The target node intersects with the parent scroll container, `Lynxview`, and the viewport of the screen.

<img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/exposure-ability.png" width="40%" height="40%" />

## Monitor exposure of the entire page

When developers need to monitor exposure/anti-exposure events of nodes in the entire page, they can subscribe to the exposure event [`exposure`](/api/lynx-api/event/global-event.md#exposure) and anti-exposure event [`disexposure`](/api/lynx-api/event/global-event.md#disexposure) of the node with the [`exposure-id`](/api/elements/built-in/view.md#exposure-id) attribute set through [`GlobalEventEmitter`](/guide/interaction/event-handling/event-propagation.md#globaleventemitter).

In the following example, the developer uses [`GlobalEventEmitter`](/guide/interaction/event-handling/event-propagation.md#globaleventemitter) to monitor whether the node in `ComponentA` is exposed, and outputs the exposed node [`exposure-id`](/api/elements/built-in/view.md#exposure-id) when it is exposed.

**Example 1:**

**This is an example below:  event**

**Entry:** `src/visibility_expose_global`
**Bundle:** `dist/visibility_expose_global.lynx.bundle` | Web: `dist/visibility_expose_global.web.bundle`

```tsx {8-12,14-21,56}
import { root, useState } from "@lynx-js/react";
import { useLynxGlobalEventListener } from "@lynx-js/react";

export function ComponentA() {
  const [eventLog, setEventLog] = useState<string>("");

  useLynxGlobalEventListener("exposure", (e) => {
    (e as { "exposure-id": string }[]).forEach((item) => {
      setEventLog((log) => log + (log === "" ? "" : ", ") + item["exposure-id"]);
    });
  });

  useLynxGlobalEventListener("disexposure", (e) => {
    let log = eventLog.split(", ");
    (e as { "exposure-id": string }[]).forEach((item) => {
      log = log.filter(id => id !== item["exposure-id"]);
    });
    log.sort();
    setEventLog(log.join(", "));
  });

  return (
    <view style={{ width: "100%", height: "100%", justifyContent: "center", alignItems: "center" }}>
      <text>Exposed nodes:</text>
      <text style={{ color: "red" }}>{eventLog}</text>
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
      <scroll-view scroll-orientation="vertical" style={{ width: "100%", height: "100%", borderWidth: "2px" }}>
        {[0, 1, 2, 3, 4, 5, 6].map((item) => {
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
              exposure-id={`scroll-item-${item + 1}`}
            >
              <text>scroll-item-{item + 1}</text>
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



The format of the exposure/anti-exposure event is an array, which contains the target node information of each triggering exposure/anti-exposure event.

```json
[
  {
    "exposure-id": string,        // exposure-id set on the target node
    "exposure-scene": string,     // exposure-scene set on the target node
    "sign": string,               // uid of the target node
    "dataset": object,            // "data-" field set on the target node
    //......
  },
  //......
]
```

## Monitor the exposure of a certain node

When the developer only needs to listen to the exposure/anti-exposure events of a certain node, you can set the \[event handler]\(../event-handling/event-listening.mdx#Event handler properties) to listen to the node's [`uiappear`](/api/elements/built-in/view.md#binduiappear) and [`uidisappear`](/api/elements/built-in/view.md#binduidisappear) events.

In the following example, the developer sets the \[event handler]\(../event-handling/event-listening.mdx#Event handler properties) to listen to whether the node is exposed, and outputs the exposed node [`id`](/api/elements/built-in/view.md#id) when it is exposed.

**Example 2:**

**This is an example below:  event**

**Entry:** `src/visibility_expose_custom`
**Bundle:** `dist/visibility_expose_custom.lynx.bundle` | Web: `dist/visibility_expose_custom.web.bundle`

```tsx {7-9,11-16,57-59}
import { root, useState } from "@lynx-js/react";
import type { Target, UIAppearanceDetailEvent } from "@lynx-js/types";

export default function App() {
  const [eventLog, setEventLog] = useState<string>("");

  function handleUIAppear(e: UIAppearanceDetailEvent<Target>) {
    setEventLog((log) => log + (log === "" ? "" : ", ") + e.detail.dataset.item);
  }

  function handleUIDisappear(e: UIAppearanceDetailEvent<Target>) {
    let log = eventLog.split(", ");
    log = log.filter(item => item !== e.detail.dataset.item);
    log.sort();
    setEventLog(log.join(", "));
  }

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
        }}
      >
        <text>Exposed node:</text>
        <text style={{ color: "red" }}>{eventLog}</text>
      </view>
      <scroll-view
        scroll-orientation="vertical"
        style={{
          width: "100%",
          height: "calc(100% - 165px)",
          backgroundColor: "yellow",
          marginTop: "15px",
          paddingTop: "40px",
        }}
        id="container"
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
                alignItems: "center",
              }}
              data-item={`scroll-item-${item + 1}`}
              binduiappear={handleUIAppear}
              binduidisappear={handleUIDisappear}
            >
              <text>scroll-item-{item + 1}</text>
            </view>
          );
        })}
        <view style={{ position: "absolute" }}>
          <text style={{ color: "blue" }}>scroll container</text>
        </view>
      </scroll-view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



The event parameter `e.detail` contains the node information.

```json
{
  "type": string                    // event name
  "detail":
    {
      "exposure-id": string,        // exposure-id set on the target node
      "exposure-scene": string,     // exposure-scene set on the target node
      "unique-id": string,          // uid of the target node
      "dataset": object,            // "data-" field set on the target node
      //......
    },
  //......
}
```

## Control exposure detection

Lynx also provides some properties and methods to control the execution of exposure detection tasks.

For example, developers can use the following methods to control whether the exposure detection task is started, stopped, and the execution frequency.

- [`lynx.stopExposure [BTS]`](/api/lynx-api/lynx/lynx-stop-exposure.md) or [`lynx.stopExposure [MTS]`](/api/lynx-api/main-thread/lynx-stop-exposure.md): Called in the main thread or background thread to stop exposure detection, that is, no longer detect the visibility of the target node, and no exposure/anti-exposure events will be triggered later.
- [`lynx.resumeExposure [BTS]`](/api/lynx-api/lynx/lynx-resume-exposure.md) or [`lynx.resumeExposure [MTS]`](/api/lynx-api/main-thread/lynx-resume-exposure.md): Called in the main thread or background thread to start exposure detection, that is, restart the visibility detection of the target node, and then trigger the exposure/anti-exposure events normally.
- [`lynx.setObserverFrameRate`](/api/lynx-api/lynx/lynx-set-observer-frame-rate.md): used to set the frequency of exposure detection.

In addition, developers can also control the exposure detection logic of the node by setting exposure-related properties on the node, such as [`exposure-screen-margin-*`](/api/elements/built-in/view.md#exposure-screen-margin-), [`exposure-ui-margin-*`](/api/elements/built-in/view.md#exposure-ui-margin-), [`exposure-area`](/api/elements/built-in/view.md#exposure-area), etc.
