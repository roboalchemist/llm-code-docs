# Source: https://lynxjs.org/guide/custom-native-component.md

# Custom Element

If the built-in elements do not meet your requirements, you can extend Lynx's capabilities by creating custom native elements. This section will guide you through creating and registering custom elements on Android, iOS and HarmonyOS platforms.

:::info Prerequisites

✅ Completed [Quick Start](/guide/start/quick-start.md)

✅ Completed [Lynx Integration](/guide/start/integrate-with-existing-apps.md)

✅ Familiar with [element Basics](/guide/ui/elements-components.md)

:::

## Building your Native Code

<PlatformTabs queryKey="platform">
  <PlatformTabs.Tab platform="ios">
    <CustomComponentLynxIOS />
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="android">
    <CustomComponentLynxAndroid />
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="harmony">
    <CustomComponentLynxHarmony />
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="web">
    <CustomComponentLynxWeb />
  </PlatformTabs.Tab>
</PlatformTabs>

## Use your Native Element

Once you have completed the development of a custom element, you can use it just like a built-in element. Below is a simple example of using an `<explorer-input>` element:

**This is an example below:  native-element**

**Bundle:** `dist/main.lynx.bundle`

```tsx {33-39}
import { useState } from "@lynx-js/react";
import * as Lynx from "@lynx-js/types";

import "./App.css";

export function App() {
  const [inputValue, setInputValue] = useState("");

  const handleInput = (e: Lynx.BaseEvent<"input", { value: string }>) => {
    const currentValue = e.detail.value.trim();
    setInputValue(currentValue);
  };

  const requestFocus = () => {
    lynx
      .createSelectorQuery()
      .select("#input-id")
      .invoke({
        method: "focus",
        params: {},
        success: function(res) {
          console.log("lynx", "request focus success");
        },
        fail: function(res) {
          console.log("lynx", "request focus fail");
        },
      })
      .exec();
  };

  return (
    <view className="input-card-url">
      <text className="bold-text">Card URL</text>
      <explorer-input
        id="input-id"
        className="input-box"
        bindinput={handleInput}
        value={inputValue}
        placeholder="Enter Card URL"
      />
      <view className="connect-button" bindtap={requestFocus}>
        <text className="button-text">Go</text>
      </view>
    </view>
  );
}

```


