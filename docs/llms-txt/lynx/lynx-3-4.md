# Source: https://lynxjs.org/blog/lynx-3-4.md

_September 3rd, 2025_

# Lynx 3.4: HarmonyOS Support, Trace and Recorder, Text Input Elements

<BlogAvatar list={['liujilong', 'lynx']} />

Lynx 3.4 is now officially released!

In line with the [technical roadmap](/blog/lynx-open-source-roadmap-2025.md) announced earlier this year, we've kept a steady bimonthly release rhythm. We skipped a blog for Lynx 3.3 since it had few user-facing features, but that release set the stage for a packed 3.4 releases, bringing new platform support for HarmonyOS, enabling Windows development, launching new developer tools _Trace_ and _Recorder_, open-sourcing the highly-requested `<input>` and `<textarea>` elements, even more flexible animations, variable fonts, and more!

## New Platform Support

### HarmonyOS Support Public Beta

Lynx now officially supports the [HarmonyOS](https://www.harmonyos.com/en/) platform. Developers can integrate Lynx into their HarmonyOS applications by following our [Integration Guide](/guide/start/integrate-with-existing-apps.md#platform=harmony).
Additionally, we will soon be publishing a dedicated blog that takes a closer look at Lynx on HarmonyOS. Stay tuned.

![](https://tosv-sg.tiktok-row.org/obj/lynx-artifacts-oss-sg/lynx-website/assets/blog/lynx-harmony/background.png)

### Support for Windows Development

- The build tool [Rspeedy](/rspeedy.md) now supports the Windows, enabling developers to develop and build Lynx projects on Windows PCs;

- Developers can successfully compile the Android Lynx Engine and [LynxExplorer](/guide/start/quick-start.md#prepare-lynx-explorer) application in a Windows environment;

Support for the Windows version of Devtool desktop is currently in development and will be released soon.

## New Developer Tools

Lynx 3.4 introduces two developer tools dedicated to improving the developer experience and debugging efficiency.

### Trace

[Trace](/guide/devtool/trace.md) delivers comprehensive, end-to-end insight into your Lynx app’s rendering pipeline. From parsing and construction to layout and rendering, Trace captures and visualizes every stage of your page’s lifecycle. What was once a “black box” is now a transparent, interactive map of your app’s inner workings. Developers can finally observe, understand, and optimize performance at the deepest levels, making it easier than ever to identify bottlenecks and fine-tune for maximum efficiency.

![](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/plugin/static/trace-tool-overview-latest2.png)

### Recorder

[Recorder](/guide/devtool/recorder.md) is your time machine for Lynx apps. It logs every aspect of your app’s runtime behavior—from external resource loading and native module calls (with results), to the complete stream of user interactions. These sessions can be exported and replayed with pixel-perfect accuracy in LynxExplorer, transforming elusive, hard-to-reproduce bugs and tricky asynchronous issues into solvable problems. With Recorder, debugging is as easy as pressing “play,” offering clarity and confidence even in the most complex scenarios.

![](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/plugin/static/recorder-concept.png)

## Text Input Elements

In a recent UI capability survey conducted within the Lynx community, `<input>`/`<textarea>` elements emerged as the most highly anticipated core features, garnering over 50% of the vote.

Lynx 3.4 delivers two core text input elements.
We will continue to improve core elements. Developers are welcome to continue voting in the [discussion](https://github.com/lynx-family/lynx/discussions/673) to help shape Lynx's future.

### Single-line [`<input>`](/api/elements/built-in/input.md) Element

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



### Multi-line [`<textarea>`](/api/elements/built-in/textarea.md) element

**This is an example below:  textarea**

**Bundle:** `dist/base.lynx.bundle`

```tsx {13-21}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root, useState } from "@lynx-js/react";

const App = () => {
  const [inputContent, setInputContent] = useState("");

  return (
    <view style={{ linearOrientation: "vertical", width: "100%", height: "100%", padding: "20px" }}>
      <view style={{ width: "100%", padding: "10px", backgroundColor: "#87654321", borderRadius: "10px" }}>
        <textarea
          style={{ width: "100%", color: "blue", fontSize: "50px" }}
          placeholder="Title"
          maxlines={2}
          bindinput={(res: any) => {
            console.log(res.detail.value);
            setInputContent(res.detail.value);
          }}
        />
      </view>

      <view
        style={{
          width: "100%",
          padding: "10px",
          marginTop: "20px",
          backgroundColor: "#12345678",
          borderRadius: "10px",
        }}
      >
        {
          <textarea
            style={{ width: "100%", height: "300px", fontSize: "30px" }}
            placeholder="Content"
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



## List Recycle Optimization

Lynx 3.4 optimizes the recycling strategy of the `<list>` element to improve rendering performance.

### Recycle `<list>` Sticky Item

When a `<list-item>` is scrolled out of the `<list>` viewport, the original recycling mechanism would cache the item for reuse. Prior to Lynx 3.4, `<list-item>` elements with the sticky attribute were not recycled. In long lists making heavy use of the sticky feature, this could lead to high memory usage. Lynx 3.4 optimizes this strategy; sticky items are now also recycled after scrolling out of the viewport.
If this change adversely affects your existing scenarios, you can temporarily disable this optimization by setting [`experimental-recycle-sticky-item={false}`](/api/elements/built-in/list.md#experimental-recycle-sticky-item). If you encounter any issues, please provide feedback via an issue.

<table border="0">
   

  <tr> <td>![](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/plugin/static/not-recycle-sticky-1.gif)</td> <td>![](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/plugin/static/recycle-sticky-1.gif)</td> </tr>

   

  <tr> <td>sticky `<list-item>` in Lynx 3.3</td> <td>sticky `<list-item>` in Lynx 3.4</td> </tr>

   
</table>

### Prevent `<list-item>` from Being Recycled

When a `<list-item>` contains complex components, recycling and re-updating the node incurs significant CPU overhead. Developers can now set `recyclable={false}` to [prevent specific `<list-item>` from being recycled](/api/elements/built-in/list.md#not-recycle-list-item). Once disabled, the item will not be recycled when it slides out of the viewport and won't require re-rendering when it reappears, making it suitable for scenarios demanding rendering performance.

**This is an example below:  list**

**Entry:** `src/recyclable`
**Bundle:** `dist/recyclable.lynx.bundle` | Web: `dist/recyclable.web.bundle`

```tsx
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root } from "@lynx-js/react";
import "./index.scss";

const ListContainer = () => {
  return (
    <list
      className="list-container"
      scroll-orientation="vertical"
      list-type="flow"
      span-count={2}
    >
      <list-item
        item-key="list-item-over-flow"
        key="list-item-over-flow"
        style={{
          overflow: "visible",
          height: "40px",
          width: "100%",
        }}
        full-span={true}
        recyclable={false}
      >
        <view
          style={{
            height: "600px",
            backgroundImage: "linear-gradient(to bottom, rgba(255, 255, 0, 0.5), rgb(255, 255, 255, 0))",
          }}
        >
          <text style={{ fontSize: "15px" }}>
            {`The list item with overflow background color and recyclable: false`}
          </text>
        </view>
      </list-item>
      {Array.from({ length: 50 }).map((item, index) => {
        return (
          <list-item
            item-key={`list-item-${index + 1}`}
            key={`list-item-${index + 1}`}
            style={{
              height: "160px",
            }}
          >
            <view
              style={{
                border: "1px solid black",
                height: "100%",
              }}
            >
              <text style={{ height: "100%", fontSize: "20px" }}>{`list-item-${index + 1}`}</text>
            </view>
          </list-item>
        );
      })}
    </list>
  );
};

root.render(<ListContainer />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## More Flexible Animations

### `Element.animate()`

The [`MainThread.Element`](/api/lynx-api/main-thread/main-thread-element.md) now features an animate() method for finely controlling CSS animations on the MTS (Main Thread Scripting), including operations like play, pause, and seeking, enabling more flexible interactive animations.

**This is an example below:  animation**

**Entry:** `src/animate_mt`
**Bundle:** `dist/animate_mt.lynx.bundle` | Web: `dist/animate_mt.web.bundle`

```tsx
import { root, useMainThreadRef } from "@lynx-js/react";
import { MainThread } from "@lynx-js/types";

import "./index.scss";

const AnimateAnimationExample = () => {
  return (
    <view style={{ width: "100%", height: "100%" }}>
      <text style={{ textAlign: "center", fontSize: "30px" }}>
        Click To Start Animation
      </text>
      <view
        className="box"
        flatten={false}
        main-thread:bindtap={(event) => {
          "main thread";
          const ani = event.currentTarget.animate(
            [
              {
                transform: "translate(0%, 0%) rotate(0deg)",
                "animation-timing-function": "linear",
              },
              {
                transform: "translate(200px, 0%) rotate(90deg)",
                "animation-timing-function": "cubic-bezier(.91,.03,.94,.11)",
              },
              {
                transform: "translate(200px, 100%) rotate(180deg)",
                "animation-timing-function": "linear",
              },
              {
                transform: "translate(0%, 100%) rotate(270deg)",
                "animation-timing-function": "cubic-bezier(.91,.03,.94,.11)",
              },
              {
                transform: "translate(0%, 0%) rotate(360deg)",
              },
            ],
            {
              name: "animation-1",
              duration: 5000,
              iterations: Infinity,
              easing: "linear",
            },
          );
        }}
      >
      </view>
    </view>
  );
};
root.render(<AnimateAnimationExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### CSS Variables Triggering Transition

Transition animations can now be triggered by changes in CSS variables, enhancing the flexibility and maintainability of transition animations. In multi-theme designs, developers can associate animation parameters with theme variables. Switching themes only requires modifying the variable values without changing selector logic to complete the theme transition.

**This is an example below:  animation**

**Entry:** `src/transition_variable`
**Bundle:** `dist/transition_variable.lynx.bundle` | Web: `dist/transition_variable.web.bundle`

```scss
.button_scene_bright {
  --bg-color: #f2f2f2;
  --color: #000000;
}

.button_scene_dark {
  --bg-color: #343a46;
  --color: #ffffff;
}

.button {
  background-color: var(--bg-color);
  transition: all 0.3s;
  width: 142px;
  height: 48px;
  border-radius: 25px;
  align-items: center;
  justify-content: center;
}

.txt {
  color: var(--color);
  transition: all 0.3s;
  font-size: 16px;
  font-weight: 700;
}

.container {
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
}

```



## Variable Fonts

Lynx 3.4 adds support for variable fonts. Developers can now perform finer adjustments to font styles using underlying CSS properties like font-variation-settings and font-optical-sizing.
Read the [MDN](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_fonts/Variable_fonts_guide) and [web.dev](https://web.dev/articles/variable-fonts) guides to learn more about variable fonts technology.

**This is an example below:  text**

**Entry:** `src/variable_font`
**Bundle:** `dist/variable_font.lynx.bundle` | Web: `dist/variable_font.web.bundle`

```tsx
import { root } from "@lynx-js/react";
import "./index.scss";

const VariableFont = () => {
  const fontSamples = [
    {
      title: "Normal",
      description: "Default font style",
      className: "",
    },
    {
      title: "Variable Weight (wght)",
      description: "font-variation-settings: 'wght' 750",
      className: "font-variation-settings",
    },
    {
      title: "Old-style Figures (onum)",
      description: "font-feature-settings: 'onum'",
      className: "font-feature-settings",
    },
    {
      title: "Combined Usage",
      description: "Applying both 'wght' and 'onum' features",
      className: "font-feature-settings font-variation-settings",
    },
  ];

  return (
    <view
      style={{ padding: "16px", display: "flex", flexDirection: "column", gap: "16px", backgroundColor: "#f4f4f4" }}
    >
      {fontSamples.map((sample, index) => (
        <view key={index} style={{ backgroundColor: "white", padding: "16px", borderRadius: "8px" }}>
          <text style={{ fontSize: "18px", fontWeight: "bold", color: "#333" }}>
            {sample.title}
          </text>
          <text style={{ fontSize: "14px", color: "#666", marginTop: "4px", marginBottom: "12px" }}>
            {sample.description}
          </text>
          <text className={`variable-font-normal ${sample.className}`} style={{ fontSize: "32px" }}>
            1234567890
          </text>
        </view>
      ))}
    </view>
  );
};

root.render(<VariableFont />);

```



## Upgrade Guide

Refer to the official guide on [Integrating Lynx into Existing Apps](/zh/guide/start/integrate-with-existing-apps.md), update the Lynx and LynxService dependency versions to complete the upgrade to Lynx 3.4.
