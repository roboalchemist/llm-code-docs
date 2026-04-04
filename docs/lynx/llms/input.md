# Source: https://lynxjs.org/api/elements/built-in/input.md

# `<input>`

<APISummary />


`<input>` is used to create interactive input controls that allow users to input and edit single-line text.

:::tip

This feature requires the client to add additional dependencies. Please refer to [More Elements](/guide/start/integrate-with-existing-apps.md) for the integration method.

:::

## Usage

### Basic

Below is a basic usage example of the `<input>` component:

**This is an example below:  input**

**Bundle:** `dist/autoHeight.lynx.bundle`

```tsx {13-20}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root, useState } from "@lynx-js/react";

const App = () => {
  const [inputContent, setInputContent] = useState("");

  return (
    <view style={{ linearOrientation: "vertical", width: "100%", height: "100%", padding: "10px" }}>
      <view style={{ width: "100%", padding: "10px", backgroundColor: "#12345678", borderRadius: "10px" }}>
        <input
          style={{ width: "100%", color: "blue", fontSize: "30px" }}
          placeholder="search"
          bindinput={(res: any) => {
            console.log(res.detail.value);
            setInputContent(res.detail.value);
          }}
        />
      </view>
      <scroll-view
        scroll-orientation="vertical"
        list-type="single"
        span-count={1}
        style={{
          width: "100%",
          height: "100%",
        }}
      >
        {Array.from({ length: 50 }).map((item, index) => {
          return (
            <text style={{ fontSize: "20px", color: "gray", padding: "10px" }}>
              {`item-${index}${inputContent ? `-${inputContent}` : ""}`}
            </text>
          );
        })}
      </scroll-view>
    </view>
  );
};

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Keyboard Avoidance

`<input>` doesn't automatically avoid keyboards, but you can adjust its position by listening to keyboard events and modifying its position accordingly:

**This is an example below:  input**

**Bundle:** `dist/autoHeight.lynx.bundle`

```tsx {116-123}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root, useLynxGlobalEventListener, useState } from "@lynx-js/react";

const App = () => {
  const [inputContent, setInputContent] = useState("");

  const setNativeProps = (itemId: string, props: Record<string, unknown>) => {
    lynx
      .createSelectorQuery()
      .select(`#${itemId}`)
      .setNativeProps(props)
      .exec();
  };

  const getItemRect = (
    itemId: string,
    success: (
      left: number,
      top: number,
      right: number,
      bottom: number,
      width: number,
      height: number,
    ) => void,
    fail?: (res: any) => void,
  ) => {
    const nodeRef = itemId === "root"
      ? lynx.createSelectorQuery().selectRoot()
      : lynx.createSelectorQuery().select(`#${itemId}`);

    nodeRef
      .invoke({
        method: "boundingClientRect",
        params: {
          relativeTo: "screen",
        },
        success: res => {
          success(
            /* eslint-disable @typescript-eslint/no-unsafe-argument, @typescript-eslint/no-unsafe-member-access*/
            res.left,
            res.top,
            res.right,
            res.bottom,
            res.width,
            res.height,
            /* eslint-enable. no-safe-argument */
          );
        },
        fail: res => {
          fail?.(res);
        },
      })
      .exec();
  };

  const keyboardChanged = (keyboardHeightInPx: number) => {
    if (keyboardHeightInPx === 0) {
      setNativeProps("panel", {
        transform: `translateY(${0}px)`,
        transition: "transform 0.1s",
      });
    } else {
      setNativeProps("panel", {
        transform: `translateY(${-keyboardHeightInPx}px)`,
        transition: "transform 0.3s",
      });
    }
  };

  useLynxGlobalEventListener(
    "keyboardstatuschanged",
    (status: unknown, keyboardHeight: unknown) => {
      console.log(status);
      console.log(keyboardHeight);
      // @ts-ignore
      keyboardChanged(status === "on" ? keyboardHeight : 0);
    },
  );

  return (
    <view style={{ linearOrientation: "vertical", width: "100%", height: "100%", padding: "10px" }}>
      <scroll-view
        scroll-orientation="vertical"
        list-type="single"
        span-count={1}
        style={{
          width: "100%",
          height: "100%",
        }}
      >
        {Array.from({ length: 50 }).map((item, index) => {
          return (
            <text style={{ fontSize: "20px", color: "gray", padding: "10px" }}>
              {`item-${index}${inputContent ? `-${inputContent}` : ""}`}
            </text>
          );
        })}
      </scroll-view>
      <view
        id="panel"
        style={{
          width: "100%",
          padding: "10px",
          backgroundColor: "white",
          height: "100px",
          background: "lightgray",
          border: "1px solid black",
          position: "absolute",
          bottom: "0px",
        }}
      >
        {
          <input
            style={{ width: "100%", color: "blue", fontSize: "30px" }}
            placeholder="search"
            bindinput={(res: any) => {
              console.log(res.detail.value);
              setInputContent(res.detail.value);
            }}
          />
        }
      </view>
    </view>
  );
};

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```




## Attributes

### `android-fullscreen-mode`

{' '}

<AndroidOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: true
'android-fullscreen-mode'?: boolean;
```

Whether to enter the full-screen input mode when in landscape screen, in which the keyboard and input box will take up the entire screen

### `confirm-type`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: 'send'
'confirm-type'?: 'search' | 'send' | 'go' | 'done' | 'next';
```

The type of confirm button

### `disabled`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.5
</VersionBadge>

```tsx
// @defaultValue: false
disabled?: boolean;
```

Interaction enabled

### `input-filter`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: undefined
'input-filter'?: string;
```

Filter the input content and process it in the form of regular expressions

### `ios-auto-correct`

{' '}

<IOSOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: true
'ios-auto-correct'?: boolean;
```

Auto correct input content on iOS

### `ios-spell-check`

{' '}

<IOSOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: true
'ios-spell-check'?: boolean;
```

Check spelling issue on iOS

### `maxlength`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: 140
maxlength?: number;
```

Max input length

### `placeholder`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
placeholder?: string;
```

Placeholder

### `readonly`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: false
readonly?: boolean;
```

Readonly

### `show-soft-input-on-focus`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: true
'show-soft-input-on-focus'?: boolean;
```

Show soft input keyboard while focused

### `type`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
// @defaultValue: "text"
type?: 'number' | 'text' | 'digit' | 'password' | 'tel' | 'email';
```

Input content type

## Events

Frontend can bind corresponding event callbacks to listen for runtime behaviors of the element, as shown below.

### `bindblur`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
bindblur = (e: InputBlurEvent) => {};
```

| Field | Type   | Optional | Default | Platforms                                                                    | Since | Description   |
| ----- | ------ | -------- | ------- | ---------------------------------------------------------------------------- | ----- | ------------- |
| value | string | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | Input content |

Blurred

### `bindconfirm`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
bindconfirm = (e: InputConfirmEvent) => {};
```

| Field | Type   | Optional | Default | Platforms                                                                    | Since | Description   |
| ----- | ------ | -------- | ------- | ---------------------------------------------------------------------------- | ----- | ------------- |
| value | string | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | Input content |

Confirm button clicked

### `bindfocus`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
bindfocus = (e: InputFocusEvent) => {};
```

| Field | Type   | Optional | Default | Platforms                                                                    | Since | Description   |
| ----- | ------ | -------- | ------- | ---------------------------------------------------------------------------- | ----- | ------------- |
| value | string | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | Input content |

Focused

### `bindinput`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
bindinput = (e: InputInputEvent) => {};
```

| Field          | Type    | Optional | Default | Platforms                                                                    | Since | Description                         |
| -------------- | ------- | -------- | ------- | ---------------------------------------------------------------------------- | ----- | ----------------------------------- |
| isComposing    | boolean | Yes      | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | Is composing or not                 |
| selectionEnd   | number  | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | The end position of the selection   |
| selectionStart | number  | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | The start position of the selection |
| value          | string  | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | Input content                       |

Input content changed

### `bindselection`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```tsx
bindselection = (e: InputSelectionEvent) => {};
```

| Field          | Type   | Optional | Default | Platforms                                                                    | Since | Description                         |
| -------------- | ------ | -------- | ------- | ---------------------------------------------------------------------------- | ----- | ----------------------------------- |
| selectionEnd   | number | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | The end position of the selection   |
| selectionStart | number | No       | –       | <AndroidOnly /> <IOSOnly /> <HarmonyOnly /> <VersionBadge>3.4</VersionBadge> | 3.4   | The start position of the selection |

Input selection changed

## Methods

Frontend can invoke component methods via the [SelectorQuery](/api/lynx-api/nodes-ref/nodes-ref-invoke.md) API.

### `blur`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```ts

lynx.createSelectorQuery()
.select('#id')
.invoke({
method: 'blur',
success: function (res) {},
fail: function (res) {},
})
.exec();

```

Release focus

### `focus`

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```ts

lynx.createSelectorQuery()
     .select('#id')
     .invoke({
      method: 'focus',
      success: function (res) {},
      fail: function (res) {},
    })
    .exec();

```

Require focus

### `getValue`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```ts

lynx.createSelectorQuery()
.select('#id')
.invoke({
method: 'getValue',
success: Callback<{
/**
_ Is composing or not, iOS only
_ @Android
_ @iOS
_ @Harmony
_ @Web
_ @since 3.4
\*/
isComposing: boolean;
/**
_ End position of the selection
_ @Android
_ @iOS
_ @Harmony
_ @Web
_ @since 3.4
_/
selectionEnd: number;
/\*\*
_ Begin position of the selection
_ @Android
_ @iOS
_ @Harmony
_ @Web
_ @since 3.4
_/
selectionStart: number;
/\*\*
_ Input content
_ @Android
_ @iOS
_ @Harmony
_ @Web
_ @since 3.4
\*/
value: string;
}>;
fail: function (res) {},
})
.exec();

```

Get input content

### `setSelectionRange`

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```ts

lynx.createSelectorQuery()
     .select('#id')
     .invoke({
      method: 'setSelectionRange',
      params: {
        /**
         * End position of the selection
         * @Android
         * @iOS
         * @Harmony
         * @Web
         * @since 3.4
         */
        selectionEnd: number;
        /**
         * Start position of the selection
         * @Android
         * @iOS
         * @Harmony
         * @Web
         * @since 3.4
         */
        selectionStart: number;
      };
      success: function (res) {},
      fail: function (res) {},
    })
    .exec();

```

Set selection range

### `setValue`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  3.4
</VersionBadge>

```ts

lynx.createSelectorQuery()
.select('#id')
.invoke({
method: 'setValue',
params: {
/\*\*
_ Input content
_ @Android
_ @iOS
_ @Harmony
_ @Web
_ @since 3.4
\*/
value: string;
};
success: function (res) {},
fail: function (res) {},
})
.exec();

```

Set input content

```
```

## Compatibility

**Compatibility Table**
**Query:** `elements.input`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 3.4 | - |
| iOS | 3.4 | - |
| HarmonyOS | 3.4 | - |
| Clay Android | 3.4 | - |
| Clay iOS | 3.4 | - |
| Clay Windows | 3.4 | - |
| Clay macOS | 3.4 | - |
| Web | ✅ Yes | - |

**Description:** input

