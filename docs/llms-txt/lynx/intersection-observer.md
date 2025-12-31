# Source: https://lynxjs.org/guide/interaction/visibility-detection/intersection-observer.md

# Intersection Observer

The intersection observer provides a method to observe the intersection status between the target node and the reference node and between the target node and the ancestor node. When the intersection status changes, the corresponding callback is triggered.

Developers can observe the changes in the intersection status between the target node and the reference node through the following three steps:

1. Call [`lynx.createIntersectionObserver`](/api/lynx-api/lynx/lynx-create-intersection-observer.md) to create an [`IntersectionObserver`](/api/lynx-api/intersection-observer.md) object and specify the threshold list of intersection status changes.
2. Call the [`relativeTo`](/api/lynx-api/intersection-observer.md) method of the [`IntersectionObserver`](/api/lynx-api/intersection-observer/intersection-observer-relative-to.md) object to specify the reference node.
3. Call the [`observe`](/api/lynx-api/intersection-observer.md) method of the [`IntersectionObserver`](/api/lynx-api/intersection-observer.md) object to specify the target node and callback.
4. Call the [`disconnect`](/api/lynx-api/intersection-observer.md) method of the [`IntersectionObserver`](/api/lynx-api/intersection-observer/intersection-observer-disconnect.md) object to clear the target node and callback.

In the following example, the developer monitors whether the parent node and the child node intersect, and outputs the intersecting child node [`id`](/api/elements/built-in/view.md#id) and the intersection position when they intersect.

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



For the specific syntax of the intersection observer, please refer to [`IntersectionObserver`](/api/lynx-api/intersection-observer.md).
