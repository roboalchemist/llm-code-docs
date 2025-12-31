# Source: https://lynxjs.org/guide/interaction/ifr.md

# Instant First-Frame Rendering (IFR)

Lynx supports "Instant First-Frame Rendering", which means that your page can display content directly when it is loaded, without a white screen or other intermediate states.

<Details title="Remind you of SSR?">
  This is usually achieved on the Web in a way similar to SSR, but Lynx's innovate dual-thread architecture makes it much easier. Your application code runs in Lynx's [JavaScript runtime](/guide/scripting-runtime/index.md),
  and will run simultaneously on two threads: the [main thread](/guide/spec.md#main-thread-or-lynx-main-thread) and the [background thread](/guide/spec.md#background-thread-aka-off-main-thread). If the data is ready at the beginning, your application code should be able to render the first screen content directly on the main thread.

  :::tip No magic
  "Instant First-Frame Rendering" is not magic, Lynx sometimes cannot achieve "Instant First-Frame Rendering":

  - When the Bundle of your page cannot be loaded synchronously, Lynx cannot achieve "Instant First-Frame Rendering" (for example, when using asynchronous file I/O, the main reason for your page to have a white screen is the asynchronous file I/O)
  - When the main content of your page needs to be loaded asynchronously, Lynx cannot achieve "Instant First-Frame Rendering" (for example, your page needs to request network data, the main reason for your page to have a white screen is the asynchronous network request)

  :::
</Details>

## Basic Example

In the following example, we simulate a complex rendering through an intensive mathematical calculation (calculating the Fibonacci sequence).
Although the rendering takes some time (obviously longer than the interval of frames), Lynx completes the rendering synchronously on the main thread, avoiding the UI intermediate state, and achieves "Instant First-Frame Rendering" without any white screen.

**This is an example below:  ifr**

**Entry:** `src/fib`
**Bundle:** `dist/fib.lynx.bundle` | Web: `dist/fib.web.bundle`

```tsx {34}
import JSBI from "jsbi";

import "./App.css";

const JSBI_ZERO = /* @__PURE__ */ JSBI.BigInt(0);
const JSBI_ONE = /* @__PURE__ */ JSBI.BigInt(1);
const JSBI_TWO = /* @__PURE__ */ JSBI.BigInt(2);

function fib(n: JSBI): JSBI {
  if (JSBI.lessThan(n, JSBI_ZERO)) {
    throw new Error("n must be non-negative");
  }
  if (JSBI.equal(n, JSBI_ZERO)) return JSBI_ZERO;
  if (JSBI.equal(n, JSBI_ONE)) return JSBI_ONE;

  let a = JSBI_ZERO, b = JSBI_ONE;
  for (let i = JSBI_TWO; JSBI.lessThanOrEqual(i, n); i = JSBI.add(i, JSBI_ONE)) {
    const next = JSBI.add(a, b);
    a = b;
    b = next;
  }

  return JSBI.BigInt(b);
}

export function App() {
  const n = JSBI.BigInt(10000);

  return (
    <view style="padding: 32rpx; display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%; height: 100%;">
      <text>fib({n.toString()})</text>
      <text>is</text>
      <scroll-view style="width: 100%; height: 50%;" scroll-y>
        <text>{fib(n).toString()}</text>
      </scroll-view>
    </view>
  );
}

```



## Do IFR with Data from Host Platform

Using static or preset data for "Instant First-Frame Rendering" is the simplest way, but it can only be used in scenes such as Showcase or Demo.
In actual applications, we usually need to use the data of the host platform for "Instant First-Frame Rendering". Go to [Using Data from Host Platform](/guide/use-data-from-host-platform.md) to learn more.

:::info
The following code uses `initData.mockData`, which is the data we set in LynxExplorer in advance to simulate the data of the host platform, so as to show you how to use the data of the host platform for "Instant First-Frame Rendering".
:::

**This is an example below:  ifr**

**Entry:** `src/initData`
**Bundle:** `dist/init_data.lynx.bundle` | Web: `dist/init_data.web.bundle`

```tsx {17}
import { useInitData } from "@lynx-js/react";

import "./App.css";

declare module "@lynx-js/react" {
  interface InitData {
    mockData: string;
  }
}

export function App() {
  const initData = useInitData();

  return (
    <view style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%; height: 100%;">
      <text>Hello World</text>
      <text>{initData.mockData}</text>
    </view>
  );
}

```



## IFR is one of the advantages of Lynx

Your end users may easily notice the difference brought by "Instant First-Frame Rendering", which is one of the advantages of Lynx.

:::info
Video below is slowed down to 0.3x speed for better observation.
:::

<VideoList
  videos={[
  {
    src: 'https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/ifr_fib_with_blank.mp4',
    title: 'Other cross-platform solutions (No IFR)',
  },
  {
    src: 'https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/ifr_fib.mp4',
    title: 'Lynx (IFR)',
  },
]}
  playbackRate={0.3}
/>

It can be seen that when there is no "Instant First-Frame Rendering", opening the App will present the change process of "Splash Screen → White Screen → Content", while Lynx's "Instant First-Frame Rendering" makes the transition after the splash screen ends more natural and provides a better user experience.
