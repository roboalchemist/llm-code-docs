# Source: https://lynxjs.org/api/elements/built-in/frame.md

# `<frame>`

<APISummary />

A page element similar to HTML's `<iframe>`, which can embed a Lynx page into the current page.

## Usage Guide

The following is an example of a main page loading an embedded page via the `<frame>` element.

- The main page passes `initData` and `globalProps` to the embedded page through the `data` and `globalProps` attributes.
- The main page listens for the embedded page loading status via the `bindload` event.

### Main Page

**This is an example below:  frame**

**Bundle:** `dist/frame.lynx.bundle`

```tsx {35-41}
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { type InitData, root, useState } from "@lynx-js/react";
import type { FrameLoadEvent, GlobalProps } from "@lynx-js/types";

const App = () => {
  const [bindLoadEvent, setBindLoadEvent] = useState({
    url: "",
    statusCode: 0,
    statusMessage: "",
  });
  const [initData, setInitData] = useState<InitData>({
    id: 123,
    name: "Alice",
    showDetail: true,
  });
  const [globalProps, setGlobalProps] = useState<GlobalProps>({
    message: "hello globalProps!",
    status: 42,
    loaded: true,
  });
  const handleLoad = (e: FrameLoadEvent) => {
    setBindLoadEvent(e.detail);
  };

  const frameUrl = `${process.env.ASSET_PREFIX}/in_frame.lynx.bundle`;
  return (
    <view>
      <text style={{ fontSize: "20px", color: "black", padding: "10px" }}>
        Below is the inline text example in frame page.
      </text>

      <frame
        style={{ width: "100%", height: "150px", border: "3px solid red" }}
        src={frameUrl}
        data={initData}
        bindload={handleLoad}
        global-props={globalProps}
      />
      <view
        style={{
          padding: "10px",
          width: "100%",
          height: "100px",
          border: "3px solid red",
        }}
        bindtap={() => setInitData({ ...initData, showDetail: !initData.showDetail })}
      >
        <text style={{ color: "black", fontSize: "20px" }}>
          {initData.showDetail ? "Hide Detail" : "Show Detail"}
        </text>
      </view>
      <text>load url: {bindLoadEvent.url}</text>
      <text>status code: {bindLoadEvent.statusCode}</text>
      <text>status message: {bindLoadEvent.statusMessage}</text>
    </view>
  );
};

root.render(<App />);

```



### Embedded Page

**This is an example below:  frame**

**Bundle:** `dist/frame.lynx.bundle`

```tsx
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root, useInitData } from "@lynx-js/react";

export function App() {
  const initData = useInitData();
  const globalProps = lynx.__globalProps;

  return (
    <view>
      <text style={{ fontSize: "30px", color: "orange" }}>I'm in frame!</text>
      <view style={{ border: "3px solid blue" }}>
        <text>{initData.id}</text>
        <text>{initData.name}</text>
        <text>{initData.showDetail ? "true" : "false"}</text>
        <text>{globalProps.message}</text>
        <text>{globalProps.status}</text>
        <text>{globalProps.loaded ? "true" : "false"}</text>
      </view>
    </view>
  );
}

root.render(<App />);

```



:::tip
The `<frame>`
 element was introduced in <VersionBadge v={3.4} />
. To use this element, the Lynx dependency version must be upgraded to <VersionBadge v={3.4} />
 or higher.
:::
:::caution
`<frame>` does not currently support automatic height adjustment. You need to manually set the width and height of the frame.
:::


## Attributes

### `data`

{' '}

<AndroidOnly />

<IOSOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
data?: Record<string, unknown>;
```

Passes data to the nested Lynx page within the frame.

### `global-props`

{' '}

<AndroidOnly />

<IOSOnly />

<VersionBadge>
  3.6
</VersionBadge>

```tsx
'global-props'?: Record<string, unknown>;
```

Passes `globalProps` to the Lynx page embedded in the frame. The embedded page can read it via [`lynx.__globalProps`](/api/lynx-api/lynx/lynx-global-props.md).

### `src`

{' '}

<AndroidOnly />

<IOSOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
src: string;
```

Sets the loading path for the frame resource.

## Events

Frontend can bind corresponding event callbacks to listen for runtime behaviors of the element, as shown below.

### `bindload`

{' '}

<AndroidOnly />

<IOSOnly />

<VersionBadge>
  3.6
</VersionBadge>

```tsx
bindload = (e: FrameLoadEvent) => {};
```

| Field         | Type   | Optional | Default | Platforms                                                    | Since | Description                  |
| ------------- | ------ | -------- | ------- | ------------------------------------------------------------ | ----- | ---------------------------- |
| statusCode    | number | No       | –       | <AndroidOnly /> <IOSOnly /> <VersionBadge>3.6</VersionBadge> | 3.6   | Frame loaded status code.    |
| statusMessage | string | No       | –       | <AndroidOnly /> <IOSOnly /> <VersionBadge>3.6</VersionBadge> | 3.6   | Frame loaded status message. |
| url           | string | No       | –       | <AndroidOnly /> <IOSOnly /> <VersionBadge>3.6</VersionBadge> | 3.6   | The loaded url of the frame. |

Bind frame load event callback.

## Compatibility

**Compatibility Table**
**Query:** `elements.frame`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 3.4 | - |
| iOS | 3.4 | - |
| HarmonyOS | ❌ No | - |
| Clay Android | ❌ No | - |
| Clay iOS | ❌ No | - |
| Clay Windows | ❌ No | - |
| Clay macOS | ❌ No | - |
| Web | ❌ No | - |

**Description:** frame

