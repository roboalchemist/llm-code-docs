# Source: https://lynxjs.org/guide/interaction/visibility-detection.md

# Visibility detection

Lynx provides two capabilities for detecting node visibility. One is Lynx's unique exposure capability, which allows developers to easily monitor whether a node is exposed. The other is a Web-like intersection observer, which is a more atomic capability that allows developers to monitor the intersection positions of nodes.

## Detect whether a node is exposed

When developers are mainly concerned about whether multiple nodes are on the screen and not the intersection of nodes, and want to write code quickly, they can use [exposure ability](/guide/interaction/visibility-detection/exposure-ability.md).

[Exposure ability](/guide/interaction/visibility-detection/exposure-ability.md) is a declarative interface. Developers can specify the nodes that need to monitor exposure through the [`exposure-id`](/api/elements/built-in/view.md#exposure-id) attribute. When the node appears, the exposure event `exposure` is triggered, and when the node disappears, the anti-exposure event `disexposure` is triggered.

In the following example, the developer monitors whether the node is exposed/anti-exposed and displays the node [`exposure-id`](/api/elements/built-in/view.md#exposure-id) visible on the screen in real time.

**Example 2:**

**This is an example below:  event**

**Entry:** `src/visibility_expose`
**Bundle:** `dist/visibility_expose.lynx.bundle` | Web: `dist/visibility_expose.web.bundle`

```tsx {8-12,14-21,62}
import { root, useState } from "@lynx-js/react";
import { useLynxGlobalEventListener } from "@lynx-js/react";

export default function App() {
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
              exposure-id={`scroll-item-${item + 1}`}
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



Since the exposure capability focuses on whether the node is visible, the node visibility requirement here is more stringent. In addition, since [exposure capability](/guide/interaction/visibility-detection/exposure-ability.md) is a declarative interface, when developers need to monitor the exposure of multiple nodes, they only need to add the [`exposure-id`](/api/elements/built-in/view.md#exposure-id) attribute to the node.

## Detect whether nodes intersect

When developers only need to check whether nodes intersect, and do not care whether the nodes are on the screen, they can use the [intersection observer](/guide/interaction/visibility-detection/intersection-observer.md).

The [intersection observer](/guide/interaction/visibility-detection/intersection-observer.md) is used to detect whether the target node intersects with the reference node and the target node intersects with the ancestor node. Developers can flexibly specify the reference node, reference node boundary scaling value, node intersection ratio threshold, etc., to achieve a more flexible definition of node visibility.

In the following example, the developer monitors whether the parent node and the child node intersect, and outputs the intersecting child node [`id`](/api/elements/built-in/view.md#id) and the intersection position when they intersect.

**Example 1:**

**This is an example below:  event**

**Entry:** `src/visibility_intersection`
**Bundle:** `dist/visibility_intersection.lynx.bundle` | Web: `dist/visibility_intersection.web.bundle`

```tsx {8-24}
import { root, useState } from "@lynx-js/react";
import type { IntersectionObserver, ObserveCallbackResult, TouchEvent } from "@lynx-js/types";

export default function App() {
  const [eventLog, setEventLog] = useState<string>("");
  let observer: IntersectionObserver | null = null;

  function handleTap(e: TouchEvent) {
    "background only";
    setEventLog("");
    if (observer == null) {
      observer = lynx.createIntersectionObserver({ componentId: "" }, { thresholds: [] });
      observer.relativeTo("#container");
      for (let i = 1; i <= 7; i++) {
        observer.observe("#view-item-" + i, (res: ObserveCallbackResult) => {
          if (res.isIntersecting) {
            let rect = res.intersectionRect;
            let rect_str = ", location: [" + rect.left + ", " + rect.top + ", " + rect.right + ", " + rect.bottom + "]";
            setEventLog((log) => log + (log === "" ? "node: " : "\nnode: ") + res.observerId + rect_str);
          }
        });
      }
    }
  }

  return (
    <view
      style={{ width: "100%", height: "90%", overflow: "hidden" }}
      bindtap={(e) => {
        handleTap(e);
      }}
    >
      <view
        style={{
          width: "calc(100% - 10px)",
          height: "150px",
          margin: "5px",
          borderWidth: "2px",
        }}
      >
        <text>Click the page to get intersected nodes:</text>
        <text style={{ color: "red" }}>{eventLog}</text>
      </view>
      <view
        style={{
          width: "100%",
          height: "calc(100% - 165px)",
          paddingTop: "40px",
          marginTop: "15px",
          backgroundColor: "yellow",
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
                borderRadius: "5px",
                backgroundColor: `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${
                  Math.floor(Math.random() * 256)
                })`,
                alignItems: "center",
              }}
              id={`view-item-${item + 1}`}
            >
              <text>view-item-{item + 1}</text>
            </view>
          );
        })}
        <view style={{ position: "absolute" }}>
          <text style={{ color: "blue" }}>view container</text>
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



The node visibility here only requires the target node and the reference node to intersect, without requiring the target node to be on the screen, and there is no need to specify the reference node as a scroll container. In addition, since the [intersection observer](/guide/interaction/visibility-detection/intersection-observer.md) is an imperative interface, when developers need to monitor the intersection of multiple nodes, redundant code needs to be written.

## Summary

So far, you have learned how to detect whether nodes are intersecting or whether nodes are exposed.

For developers, when the focus is on whether a node is on the screen and you want to easily write exposure monitoring code for multiple nodes, you can use [Exposure Ability](/guide/interaction/visibility-detection/exposure-ability.md). when the focus is on whether nodes intersect and where they intersect, or when you need to flexibly define the visibility of nodes, you can use [Intersection Observer](/guide/interaction/visibility-detection/intersection-observer.md).
