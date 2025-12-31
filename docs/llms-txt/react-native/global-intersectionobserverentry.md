# Source: https://reactnative.dev/docs/global-intersectionobserverentry.md

# IntersectionObserverEntry 🧪

Canary 🧪

**This API is currently only available in React Native’s Canary and Experimental channels.**

If you want to try it out, please [enable the Canary Channel](/docs/releases/release-levels.md) in your app.

The [`IntersectionObserverEntry`](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry) interface, as defined in Web specifications. It describes the intersection between the target element and its root container at a specific moment of transition.

Instances of `IntersectionObserverEntry` are delivered to an [`IntersectionObserver`](/docs/global-intersectionobserver.md) callback in its `entries` parameter.

***

# Reference

## Instance properties[​](#instance-properties "Direct link to Instance properties")

### `boundingClientRect`[​](#boundingclientrect "Direct link to boundingclientrect")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/boundingClientRect).

Returns the bounds rectangle of the target element as a `DOMRectReadOnly`.

### `intersectionRatio`[​](#intersectionratio "Direct link to intersectionratio")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio).

Returns the ratio of the `intersectionRect` to the `boundingClientRect`.

### `intersectionRect`[​](#intersectionrect "Direct link to intersectionrect")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRect).

Returns a `DOMRectReadOnly` representing the target's visible area.

### `isIntersecting`[​](#isintersecting "Direct link to isintersecting")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting).

A Boolean value which is `true` if the target element intersects with the intersection observer's root. If this is `true`, then the `IntersectionObserverEntry` describes a transition into a state of intersection; if it's `false`, then you know the transition is from intersecting to not-intersecting.

### `rnRootIntersectionRatio` ⚠️[​](#rnrootintersectionratio-️ "Direct link to rnrootintersectionratio-️")

Non-standard

This is a React Native specific extension.

Returns the ratio of the `intersectionRect` to the `rootBounds`.

ts

```
get rnRootIntersectionRatio(): number;
```

This is analogous to `intersectionRatio`, but computed relative to the root's bounding box instead of the target's bounding box. This corresponds to the `rnRootThreshold` option and allows you to determine what percentage of the root area is covered by the target element.

### `rootBounds`[​](#rootbounds "Direct link to rootbounds")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/rootBounds).

Returns a `DOMRectReadOnly` for the intersection observer's root.

### `target`[​](#target "Direct link to target")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/target).

The `Element` whose intersection with the root changed.

### `time`[​](#time "Direct link to time")

See [documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/time).

A `DOMHighResTimeStamp` indicating the time at which the intersection was recorded, relative to the `IntersectionObserver`'s time origin.
