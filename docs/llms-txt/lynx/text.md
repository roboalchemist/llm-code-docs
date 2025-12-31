# Source: https://lynxjs.org/api/elements/built-in/text.md

# `<text>`

<APISummary />

`<text>` is a built-in element in Lynx used to display text content. It supports specifying text style, binding click event callbacks, and can nest `<text>`, [`<image>`](/api/elements/built-in/image.md), and [`<view>`](/api/elements/built-in/view.md) elements to achieve relatively complex text and image content presentation.

## Usage

The `<text>` element has its own layout context similar to the Web's [inline formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_inline_layout/Inline_formatting_context). It does not support `display` properties like `<view>`. For advanced text styling with `<text>` element, see the [Text and Typography guide](/guide/styling/text-and-typography.md).

### Nested `<text>`

Nested `<text>` refers to `<text>` subelements within a `<text>` element.

**This is an example below:  text**

**Entry:** `src/inline_text`
**Bundle:** `dist/inline_text.lynx.bundle` | Web: `dist/inline_text.web.bundle`

```tsx
import { root } from "@lynx-js/react";
import "./index.scss";

const MyComponent = () => {
  return (
    <view className="fixed_area" data-test-tag="container">
      <view className="test-item">
        <text className="text">Case 1：inline-text Concatenate:</text>
        <text className="expection">
          <text>simple text scenario:</text>
          <text>[inline-text 1]</text>
          <text>[inline-text 2]</text>
        </text>
      </view>

      <view className="test-item" style={{ marginTop: "40px" }}>
        <text className="text">Case 2：inline-text: different color</text>
        <text className="expection">
          <text>simple text scenario:</text>
          <text style={{ color: "blue" }}>[inline-text 1]</text>
          <text style={{ color: "#62efff" }}>[inline-text 2]</text>
        </text>
        <text className="expection">
          <text>inline-text gradient-color:</text>
          <text style={{ color: "blue" }}>[inline-text 1]</text>
          <text
            style={{
              color: "linear-gradient(to right, red, #65499c, #62efff)",
            }}
          >
            [inline-text 2]
          </text>
        </text>
      </view>

      <view className="test-item" style={{ marginTop: "40px" }}>
        <text className="text">Case 3：inline-text: different style</text>
        <text className="expection">
          <text>simple text scenario:</text>
          <text style={{ fontStyle: "italic" }}>[inline-text 1]</text>
          <text style={{ textDecoration: "line-through" }}>
            [inline-text 2]
          </text>
        </text>
        <text className="expection">simple text scenario</text>
      </view>
    </view>
  );
};
export default MyComponent;
root.render(<MyComponent />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



Since the [CSS inheritance is not enabled](/guide/styling/custom-theming.md#leveraging-css-inheritance-as-needed) by default in Lynx, it's recommended to explicitly declare the required styles for `<text>`, as it will not inherit the text-related properties from its parent node.

```tsx
// When CSS inheritance is not enabled, the font-size of the parent node will not be applied to the child <text> node.
<view style={{ fontSize: '20px' }}>
  <text>hello world</text>
</view>
```

However, nested `<text>` is special. Even when CSS inheritance is not enabled, it will still apply `<color>` and `<font-family>` properties of the parent `<text>`. To maintain consistency, it is recommended to explicitly override the properties of the parent `<text>` in the inline `<text>`.

```tsx
<text style={{ color: 'red' }}>
  red
  <text>red</text>
  <text style={{ color: 'blue' }}>blue</text>
</text>
```

### Nested `<image>`

Nested `<image>` refers to `<image>` subelements within a `<text>` element. It can be used for mixed text and image layout.

**This is an example below:  text**

**Entry:** `src/inline_image`
**Bundle:** `dist/inline_image.lynx.bundle` | Web: `dist/inline_image.web.bundle`

```tsx
import ExclamationCircle from "@assets/image/exclamationcircle.png?inline";
import { root } from "@lynx-js/react";
import { Component } from "@lynx-js/react";
export default class Index extends Component {
  render() {
    return (
      <view style={{ width: "200px" }}>
        <text style={{ fontSize: "20px", textAlign: "center" }}>
          <image
            style={{
              width: "20px",
              height: "20px",
              border: "1px solid red",
              borderRadius: "50%",
              verticalAlign: "middle",
            }}
            src={ExclamationCircle}
          />
          <text style={{}}>
            This is a warning message.This is a warning message.This is a warning message.
          </text>
        </text>
      </view>
    );
  }
}
root.render(<Index />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Nested `<view>`

A `<view>` written inside a text element will have inline characteristics and participate in text layout. It also supports all functionalities of the `<view>` tag, including adding borders, rounded corners, and any other element content inside it.

**This is an example below:  text**

**Entry:** `src/inline_view`
**Bundle:** `dist/inline_view.lynx.bundle` | Web: `dist/inline_view.web.bundle`

```tsx
import { root } from "@lynx-js/react";
import { Component } from "@lynx-js/react";
import "./index.scss";

const InlineView = () => {
  return (
    <view
      style="flex-direction:column;align-items:center;border:1px red solid;"
      lynx-test-tag="container"
    >
      <text
        style="text-align:center;font-size:25px;text-overflow:ellipsis;"
        text-maxline="2"
      >
        <view
          style={{ flexDirection: "column", verticalAlign: "center" }}
          className="container"
          clip-radius="true"
        >
          <view className="title-name-wrapper-border">
            <view className="title-name-wrapper-border-before"></view>
            <view className="title-name-wrapper-border-after"></view>
          </view>
        </view>
        This is a paragraph containing animation.This is a paragraph containing animation.
      </text>
    </view>
  );
};

export default InlineView;
root.render(<InlineView />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### `<inline-truncation>`

`<inline-truncation>` tag is used to customize the content that needs to be displayed at the end of the text when truncation occurs.

**This is an example below:  text**

**Entry:** `src/inline_truncation`
**Bundle:** `dist/inline_truncation.lynx.bundle` | Web: `dist/inline_truncation.web.bundle`

```tsx
import ExclamationCircle from "@assets/image/exclamationcircle.png?inline";
import RightArrow from "@assets/image/rightarrow.png?inline";
import { root } from "@lynx-js/react";

const InlineTruncation = () => {
  return (
    <view style={{ width: "200px" }}>
      <text style={{ height: "30px", lineHeight: "20px" }} text-maxline="1">
        this is a test text. this is a test text. this is a test text.this is a test text. this is a test text. this is
        a test text.
        <inline-truncation>
          <text>...See More</text>
          <image src={RightArrow} style={{ width: "10px", height: "10px" }} />
        </inline-truncation>
      </text>

      <text
        style={{ lineHeight: "20px", marginTop: "30px" }}
        text-maxline={"2"}
      >
        this is a test text. this is a test text. this is a test text.this is a test text. this is a test text. this is
        a test text.
        <inline-truncation>
          <text style={{ color: "grey" }}>...See More</text>
          <view style={{ verticalAlign: "center" }} flatten={false}>
            <image
              src={ExclamationCircle}
              style={{ width: "15px", height: "15px" }}
            />
          </view>
        </inline-truncation>
      </text>
    </view>
  );
};

export default InlineTruncation;
root.render(<InlineTruncation />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### RTL

The `text` element supports RTL (Right-To-Left) language layout display. By default, the `text` element will determine the text language based on the content and use the corresponding layout method. Developers can also specify the use of RTL layout by setting the `direction` style.

:::tip

When `direction` is set to `rtl` or `lynx-rtl`, `text-align:start` will be converted to `text-align:right`, and similarly, `text-align:end` will be converted to `text-align:left`.
When `direction` is set to `lynx-rtl`, `text-align:left` will be converted to `text-align:right`, and similarly, `text-align:right` will be converted to `text-align:left`.

:::

**This is an example below:  text**

**Entry:** `src/text_style`
**Bundle:** `dist/text_style.lynx.bundle` | Web: `dist/text_style.web.bundle`

```tsx {303-356}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root } from "@lynx-js/react";
import "./index.scss";
import ExclamationCircle from "@assets/image/exclamationcircle.png?inline";

const AlignContent = () => {
  const examples = [
    { type: "text-overflow" },
    { type: "text-vertical-align" },
    { type: "text-decoration" },
    { type: "text-shadow" },
    { type: "text-direction-rtl" },
  ];

  const TextOverflowExample = () => {
    return (
      <view className="fixed_area">
        <text
          style={{
            fontSize: "20px",
          }}
        >
          text overflow:
        </text>
        <view
          style={{
            width: "100%",
            flexDirection: "column" as const,
          }}
        >
          <text className="item clip" text-maxline="1">
            Hello World Hello World Hello World
          </text>
          <text className="item ellipsis" text-maxline="1">
            Hello World Hello World Hello World
          </text>
        </view>
      </view>
    );
  };

  const TextVerticalAlignExample = () => {
    return (
      <view className="fixed_area">
        <text
          style={{
            marginTop: "20px",
            fontSize: "20px",
          }}
        >
          text vertical align:
        </text>
        <view
          style={{
            width: "100%",
            flexDirection: "column" as const,
          }}
        >
          <text
            style={{
              backgroundColor: "tomato",
              lineHeight: "50px",
            }}
            text-maxline="1"
          >
            <text
              style={{
                verticalAlign: "middle" as const,
              }}
            >
              middle
            </text>
            <text
              style={{
                verticalAlign: "center" as const,
              }}
            >
              center
            </text>
            <text
              style={{
                verticalAlign: "top" as const,
              }}
            >
              top
            </text>
            <text
              style={{
                verticalAlign: "bottom" as const,
              }}
            >
              bottom
            </text>
            <text
              style={{
                verticalAlign: "text-top" as const,
              }}
            >
              text-top
            </text>
            <text
              style={{
                verticalAlign: "baseline" as const,
              }}
            >
              baseline
            </text>
          </text>
          <text
            style={{
              marginTop: "10px",
              backgroundColor: "orange",
              lineHeight: "50px",
            }}
            text-maxline="1"
          >
            <view
              className="bg-yellow"
              style={{
                verticalAlign: "middle" as const,
              }}
            >
              <text>middle</text>
            </view>
            <view
              className="bg-yellow"
              style={{
                verticalAlign: "center" as const,
              }}
            >
              <text>center</text>
            </view>
            <view
              className="bg-yellow"
              style={{
                verticalAlign: "top" as const,
              }}
            >
              <text>top</text>
            </view>
            <view
              className="bg-yellow"
              style={{
                verticalAlign: "bottom" as const,
              }}
            >
              <text>bottom</text>
            </view>
            <view
              className="bg-yellow"
              style={{
                verticalAlign: "texttop" as const,
              }}
            >
              <text>text-top</text>
            </view>
            <view
              className="bg-yellow"
              style={{
                verticalAlign: "baseline" as const,
              }}
            >
              <text>baseline</text>
            </view>
          </text>
        </view>
      </view>
    );
  };

  const TextDecorationExample = () => {
    return (
      <view className="fixed_area">
        <text
          style={{
            marginTop: "20px",
            fontSize: "20px",
          }}
        >
          text decoration:
        </text>
        <view
          style={{
            width: "100%",
            flexDirection: "column" as const,
          }}
        >
          <text
            style={{
              backgroundColor: "#ccc",
              marginTop: "10px",
            }}
          >
            text-decoration
          </text>
          <text
            style={{
              textDecoration: "none" as const,
            }}
          >
            none
          </text>
          <text
            style={{
              textDecoration: "underline" as const,
            }}
          >
            underline
          </text>
          <text
            style={{
              textDecoration: "line-through" as const,
            }}
          >
            line-through
          </text>
          <text
            style={{
              textDecoration: "underline line-through red solid" as const,
            }}
          >
            red solid
          </text>
          <text
            style={{
              textDecoration: "underline line-through green dotted" as const,
            }}
          >
            green dotted
          </text>
          <text
            style={{
              textDecoration: "underline line-through blue dashed" as const,
            }}
          >
            blue dashed
          </text>
        </view>
      </view>
    );
  };

  const TextShadowExample = () => {
    return (
      <view className="fixed_area">
        <text
          style={{
            marginTop: "20px",
            fontSize: "20px",
          }}
        >
          text shadow:
        </text>
        <view
          style={{
            width: "100%",
            flexDirection: "column" as const,
          }}
        >
          <text
            style={{
              backgroundColor: "#ccc",
              marginTop: "10px",
            }}
          >
            Text Shadow Properties
          </text>
          <text
            style={{
              textShadow: "none" as const,
            }}
          >
            text-shadow: none;
          </text>
          <text
            style={{
              textShadow: "1px 1px 2px #558abb" as const,
            }}
          >
            text-shadow: 1px 1px 2px #558abb;
          </text>
          <text
            style={{
              textShadow: "1px 1px 2px red, 0 0 1em blue, 0 0 0.2em blue" as const,
            }}
          >
            text-shadow: 1px 1px 2px red, 0 0 1em blue, 0 0 0.2em blue;
          </text>
          <text
            style={{
              textShadow: "0 .005px .01rem rgba(70, 70, 70, .3)" as const,
            }}
          >
            text-shadow: 0 .005px .01rem rgba(70, 70, 70, .3);
          </text>
        </view>
      </view>
    );
  };

  const TextDirectionRtlExample = () => {
    return (
      <view className="fixed_area">
        <text
          style={{
            marginTop: "20px",
            fontSize: "20px",
          }}
        >
          text direction rtl:
        </text>
        <view
          style={{
            width: "100%",
            flexDirection: "column" as const,
          }}
        >
          <text
            style={{
              direction: "rtl" as const,
            }}
          >
            لإعادة الشحن على دون دفع رسوم الخدمة داخل
            <image
              src={ExclamationCircle}
              style={{
                width: "22px",
                height: "22px",
              }}
            />
            رسوم الخدمة داخل
            <view
              style={{
                padding: "10px",
                border: "1px solid red",
                borderRadius: "20px",
              }}
            >
              <text
                style={{
                  fontSize: "30px",
                  color: "linear-gradient(green, yellow)",
                }}
              >
                {" "}
                sub text{" "}
              </text>
            </view>
            الشحن على دون دفع
          </text>
        </view>
      </view>
    );
  };

  const renderExample = (type: string) => {
    switch (type) {
      case "text-overflow":
        return <TextOverflowExample />;
      case "text-vertical-align":
        return <TextVerticalAlignExample />;
      case "text-decoration":
        return <TextDecorationExample />;
      case "text-shadow":
        return <TextShadowExample />;
      case "text-direction-rtl":
        return <TextDirectionRtlExample />;
      default:
        return null;
    }
  };

  return (
    <scroll-view
      scroll-orientation="vertical"
      style={{
        padding: "5px",
        width: "100%",
        height: "100%",
      }}
    >
      {examples.map((example, index) => renderExample(example.type))}
    </scroll-view>
  );
};

export default AlignContent;

root.render(<AlignContent />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Attributes

Attribute names and values are used to describe the behavior and appearance of elements.

### `text-maxline`

```tsx
// DefaultValue: '-1'
text-maxline?: number;
```

Limits the maximum number of lines displayed for the text content, `overflow:hidden` should be set simultaneously.

### `include-font-padding`
 <AndroidOnly />

```tsx
// DefaultValue: false
include-font-padding?: boolean;
```

Add additional padding for Android text on top and bottom. Enabling this may cause inconsistencies between platforms.

### `tail-color-convert`

```tsx
// DefaultValue: false
tail-color-convert?: boolean;
```

By default, if the text is truncated, the inserted `...` will be displayed with the color specified by the closest inline-text's style. If this attribute is enabled, the color of `...` will be specified by the outermost `text` tag's style.

### `text-single-line-vertical-align`

```tsx
// DefaultValue: 'normal'
text-single-line-vertical-align?: 'normal' | 'top' | 'center' | 'bottom';
```

Used to set vertical alignment for single-line plain text. It can be changed by setting 'top' | 'center' | 'bottom'. It is recommended to use this only when the default font does not meet the center alignment requirements, as it increases text measurement time.

### `text-selection`

```tsx

// DefaultValue: false
text-selection?: boolean;

```

Sets whether to enable text selection. When enabled, `flatten={false}` should be set simultaneously.

### `custom-context-menu`

```tsx

// DefaultValue: false
custom-context-menu?: boolean;

```

Used to set whether to turn on the custom pop-up context menu after selection and copying. It takes effect after enabling `text-selection`.

### `custom-text-selection`

```tsx

// DefaultValue: false
custom-text-selection?: boolean;

```

Used to set whether to enable the custom text selection function. When it is enabled, the element will no longer handle the gesture logic related to selection and copying. Developers need to control it through APIs such as `setTextSelection`. It takes effect after enabling `text-selection`.

## Events

Frontend can bind corresponding event callbacks to elements to listen to runtime behaviors. All [basic events](/api/elements/built-in/view.md#events) are supported.

### `layout`

```ts
bindlayout = (e: layoutEvent) => {};

interface LineInfo {
  /**
   * The starting character offset of this line relative to the entire text
   */
  start: number;
  /**
   * The ending character offset of this line relative to the entire text
   */
  end: number;
  /**
   * The number of characters truncated in this line. A non-zero value indicates truncation occurred on this line.
   */
  ellipsisCount: number;
}

interface layoutEvent extends CustomEvent {
  detail: {
    /**
     * Number of visible text lines after layout.
     */
    lineCount: number;
    /**
     * Detailed information of each line after layout.
     */
    lines: LineInfo[];
    /**
     * Dimensions of the text element.
     */
    size: { width: number; height: number };
  };
}
```

The layout event returns the result information after text layout, including the number of lines of the current text, and the start and end positions of the text in each line relative to the entire text.

### `selectionchange`

```ts
bindselectionchange = (e: selectionChangeEvent) => {};

interface selectionChangeEvent extends CustomEvent {
  detail: {
    /**
     * The start index of the selected text. Value is -1 when no text is selected.
     */
    start;
    /**
     * The end index of the selected text. Value is -1 when no text is selected.
     */
    end;
    /**
     * Selection direction: `forward` or `backward`
     */
    direction;
  };
}
```

This event is triggered whenever the selected text range changes.

## Methods

You can invoke element methods from the frontend using the [SelectorQuery](/api/lynx-api/nodes-ref/nodes-ref-invoke.md) API.

### `setTextSelection`

```ts
<text id="test" text-selection={true} flatten={false}></text>

lynx.createSelectorQuery()
  .select('#test')
  .invoke({
    method: "setTextSelection",
    params: {
      startX,  // X-coordinate of the selection start relative to the element
      startY,  // Y-coordinate of the selection start
      endX,    // X-coordinate of the selection end
      endY,    // Y-coordinate of the selection end
      showStartHandle, // Whether to show the start selection handle
      showEndHandle,   // Whether to show the end selection handle
    },
    success: function (res) {
      console.log(res);
    },
    fail: function (error) {
      console.log(error);
    },
}).exec();
```

This method sets the selected text based on start and end positions and controls the visibility of selection handles. The response `res` contains:

```ts
interface Rect {
  left: number;    // Left boundary
  right: number;   // Right boundary
  top: number;     // Top boundary
  bottom: number;  // Bottom boundary
  width: number;   // Width
  height: number;  // Height
}

interface Handle {
  x: number;       // Center X of handle
  y: number;       // Center Y of handle
  radius: number;  // Touch radius of the handle
}

{
  /**
   * Bounding box of the selected text
   */
  boundingRect: Rect;
  /**
   * Bounding boxes for each line within the selection
   */
  boxes: Rect[];
  /**
   * Position and touch radius for each handle
   */
  handles: Handle[];
}
```

### `getTextBoundingRect`

```ts
<text id="test"></text>

lynx.createSelectorQuery()
  .select('#test')
  .invoke({
    method: "getTextBoundingRect",
    params: {
      start,
      end,
    },
    success: function (res) {
      console.log(res);
    },
    fail: function (error) {
      console.log(error);
    },
}).exec();
```

This method retrieves the bounding box of a specific range of text. The response `res` includes:

```ts
{
  /**
   * Bounding box of the selected text
   */
  boundingRect: Rect;
  /**
   * Bounding boxes for each line in the selected range
   */
  boxes: Rect[];
}
```

### `getSelectedText`

```ts
<text id="test" text-selection={true} flatten={false}></text>

lynx.createSelectorQuery()
  .select('#test')
  .invoke({
    method: "getSelectedText",
    params: {},
    success: function (res) {
      console.log(res);
    },
    fail: function (error) {
      console.log(error);
    },
}).exec();
```

This method retrieves the string content of the currently selected text.

## Loading Custom Fonts

You can specify custom font resources using [`@font-face`](/api/css/at-rule/font-face.md) and utilize them with the [`font-family`](/api/css/properties/font-family.md) property.
The client needs to implement the corresponding font resource loader using [`GenericResourceFetcher`](/api/lynx-native-api/lynx-generic-resource-fetcher/fetch-resource.md) to download web font resources.

<PlatformTabs queryKey="platform">
  <PlatformTabs.Tab platform="ios">
    ```objective-c
    @interface ExampleGenericResourceFetcher : NSObject <LynxGenericResourceFetcher>

    - (void)fetchResource:(LynxResourceRequest *)request
               onComplete:(LynxGenericResourceCompletionBlock)callback;

    @end
    ```

    ```objective-c
    @implementation ExampleGenericResourceFetcher

    NSURL *url = [NSURL URLWithString:request.url];
    NSURLRequest *urlRequest = [NSURLRequest requestWithURL:url
                                                 cachePolicy:NSURLRequestReloadIgnoringCacheData
                                             timeoutInterval:5];

    [NSURLConnection sendAsynchronousRequest:urlRequest
                                       queue:[NSOperationQueue mainQueue]
                           completionHandler:^(NSURLResponse * _Nullable response,
                                               NSData * _Nullable data,
                                               NSError * _Nullable connectionError) {
        if (!connectionError) {
            // Notify font data
            callback(data, nil);
        } else {
            callback(data, connectionError);
        }
    }];
    @end

    // Register when constructing LynxView.
    LynxViewBuilder.genericResourceFetcher = [[ExampleGenericResourceFetcher alloc] init];
    ```
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="android">
    ```java
    public class ExampleGenericResourceFetcher extends LynxGenericResourceFetcher {
      @Override
      public void fetchResource(LynxResourceRequest request, LynxResourceCallback<byte[]> callback) {
        ...
          // download font file through http
          byte[] data = new byte[(int) file.length()];

          // notify the font data if success
          callback.onResponse(LynxResourceResponse.onSuccess(data));

        ...
      }
    }

    // Register when constructing LynxView.
    LynxViewBuilder.setGenericResourceFetcher(new ExampleGenericResourceFetcher(context));
    ```
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="harmony">
    ```typescript
    import {
      LynxError,
      LynxSubErrorCode,
      LynxGenericResourceFetcher,
      LynxResourceRequest,
      LynxResourceType,
    } from '@lynx/lynx';

    export class ExampleGenericResourceFetcher extends LynxGenericResourceFetcher {
      fetchResource(
        request: LynxResourceRequest,
        callback: AsyncCallback<ArrayBuffer, void>,
      ): void {
        // download font file through http
        let data: http.HttpResponse;
        // notify the font data if success
        callback.onResponse(LynxResourceResponse.onSuccess(data));
      }
    }
    ```
  </PlatformTabs.Tab>
</PlatformTabs>

## Big Font

Clients can use font scaling related APIs to modify the font scaling ratio after users change the system or application font size. This will also trigger the `onFontScaleChanged` event.

<img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/big-font-flow.png" width="75%" height="75%" />

### Usage

1. Client-side: Use `LynxViewBuilder.setFontScale()` to set the font scale when creating the LynxView\.Update the font scale with `LynxView.updateFontScale()`.

2. Front-end: `font-size` and `line-height` will zoom in and out according to the font scale.
   The front-end can obtain the updated `fontScale` from the client by listening to the `onFontScaleChanged` event.

The front-end to listen to `onFontScaleChanged`:

```jsx
const YourComponent = () => {
  const [touchCount, setTouchCount] = useState(0);

  useEffect(() => {
    const eventEmitter = getJSModule('GlobalEventEmitter');
    const listener = (msg) => {
      console.log('onFontScaleChanged testGlobalEvent:', msg);
      setTouchCount((prevCount) => prevCount + 1);
    };

    eventEmitter.addListener('onFontScaleChanged', listener);

    return () => {
      eventEmitter.removeListener('onFontScaleChanged', listener);
    };
  }, []);

  return (
    <view>
      <text>touch: {touchCount}</text>
    </view>
  );
};
```

## More Features

### `<text>` selection and copying

The `<text>` element supports text selection and copying. You can enable this feature by setting the `text-selection` attribute on the `<text>` element, and make sure to set `flatten={false}` as well:

```tsx
<text text-selection={true} flatten={false}>
  hello world
</text>
```

Long-pressing the text will highlight the selected area and trigger the default context menu, which includes options like "Select All" and "Copy".

::: note
Text selection is currently not supported for RTL (Right-to-Left) mode.
:::

If you want to implement a **custom context menu**, you need to set the `custom-context-menu` attribute and bind the `selectionchange` event along with the `getTextBoundingRect` method to determine the position for rendering your custom menu.

**This is an example below:  text**

**Entry:** `src/text_selection`
**Bundle:** `dist/cross_text_selection.lynx.bundle` | Web: `dist/cross_text_selection.web.bundle`

```tsx {26-48,128}
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root, useState } from "@lynx-js/react";

import "./index.scss";

// TextSelection component for text selection and context menu handling
const TextSelection = () => {
  // State for selected text element ID
  const [selectedId, setSelectedId] = useState("");
  // State for context menu visibility
  const [showContextMenu, setShowContextMenu] = useState(false);
  // State for context menu left offset
  const [contextMenuLeftOffset, setContextMenuLeftOffset] = useState(0);
  // State for context menu top offset
  const [contextMenuTopOffset, setContextMenuTopOffset] = useState(0);

  // Handle query errors
  const handleQueryError = (res: { code: number; data: unknown }) => {
    console.log(res.code, res.data);
  };

  // Handle text selection change
  // TODO(types): support selection change event in `@lynx-js/types`
  const handleSelectionChange = (e: any) => {
    if (e.detail.start === -1) {
      setSelectedId("");
      hiddenContextMenu();
      return;
    }
    const newSelectedId = "#" + e.target.id;
    setSelectedId(newSelectedId);
    lynx.createSelectorQuery()
      .select(newSelectedId)
      .invoke({
        method: "getTextBoundingRect",
        params: { start: e.detail.start, end: e.detail.end },
        success: (res) => {
          showContextMenuAtPosition(
            res.boundingRect.left + res.boundingRect.width / 2 - 50,
            res.boundingRect.top + res.boundingRect.height + 20,
          );
        },
        fail: handleQueryError,
      })
      .exec();
  };

  // Handle copy action
  const handleCopy = () => {
    copyText();
    clearSelection();
  };

  // Copy selected text
  const copyText = () => {
    if (selectedId === "") return;
    lynx.createSelectorQuery()
      .select(selectedId)
      .invoke({
        method: "getSelectedText",
        params: {},
        success: (res) => {
          console.log("getSelectedText:" + JSON.stringify(res));
        },
        fail: handleQueryError,
      })
      .exec();
  };

  // Clear text selection
  const clearSelection = () => {
    if (selectedId === "") return;
    lynx.createSelectorQuery()
      .select(selectedId)
      .invoke({
        method: "setTextSelection",
        params: { startX: -1, startY: -1, endX: -1, endY: -1, showStartHandle: false, showEndHandle: false },
        success(res) {
          console.log("clearTextSelection", res);
        },
        fail: handleQueryError,
      })
      .exec();
    setSelectedId("");
  };

  // Hide context menu
  const hiddenContextMenu = () => {
    if (!showContextMenu) return;
    setShowContextMenu(false);
  };

  // Show context menu at given position
  const showContextMenuAtPosition = (left: number, top: number) => {
    setShowContextMenu(true);
    setContextMenuLeftOffset(left);
    setContextMenuTopOffset(top);
  };

  return (
    <page>
      <view className="Background" />
      <view className="App">
        <view
          style={{
            left: contextMenuLeftOffset + "px",
            top: contextMenuTopOffset + "px",
            visibility: showContextMenu ? "visible" : "hidden",
          }}
          className="ContextMenu"
        >
          <text className="ContextMenuText" bindtap={handleCopy}>
            Copy
          </text>
          <text className="ContextMenuText">
            Search
          </text>
        </view>
        <view id="container" style={{ width: "90vw" }} className="Container">
          <text
            id="1"
            className="NormalText"
            text-selection={true}
            custom-context-menu={true}
            flatten={false}
            bindselectionchange={handleSelectionChange}
          >
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
            dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat justo id, feugiat leo.
            Cras eu elementum dui.
          </text>
        </view>
      </view>
    </page>
  );
};

export default TextSelection;

root.render(<TextSelection />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### cross `<text>` selection and copying

For more advanced scenarios, such as supporting **cross-node selection** across multiple `<text>` elements, you need to implement custom selection logic.

Step-by-Step: Implementing Cross-Text Selection

1. Enable Custom Text Selection Mode

Set the `custom-text-selection` attribute on each `<text>` element. This disables the built-in selection and gesture handling, allowing you to define your own.

**This is an example below:  text**

**Entry:** `src/cross_text_selection`
**Bundle:** `dist/cross_text_selection.lynx.bundle` | Web: `dist/cross_text_selection.web.bundle`

```tsx {270}
// Copyright 2025 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import { root, useEffect } from "@lynx-js/react";
import type { CommonEvent, SelectorQuery, TouchEvent } from "@lynx-js/types";

import "./index.scss";

/**
 * Metadata for each <text> node: position, dimensions, and selection bounds.
 */
interface TextNodeInfo {
  id: string; // Unique identifier for the DOM node
  left: number; // X-coordinate of node's left edge
  top: number; // Y-coordinate of node's top edge
  width: number; // Width of the node's bounding box
  height: number; // Height of the node's bounding box
  startX: number; // Selected region's start X
  startY: number; // Selected region's start Y
  endX: number; // Selected region's end X
  endY: number; // Selected region's end Y
}

// Global storage for node info and selection handlers
let textsInfo: TextNodeInfo[] = [];
let handlers: Array<{ x: number; y: number; radius: number; startX: number; startY: number }> = [];
let startPosition = { x: 0, y: 0 }; // Initial touch point for selection
let isSelecting = false; // Flag: currently dragging a selection handle

const CrossTextSelection = () => {
  // useEffect hook to run code when the component mounts and unmounts
  useEffect(() => {
    console.log("component did mount");
    getTextNodeRect();
    return () => {
      console.log("component will unmount");
    };
  }, []);

  // Handle long press event to start text selection
  const handleLongPress = (e: CommonEvent) => {
    isSelecting = true;
    startPosition.x = e.detail.x;
    startPosition.y = e.detail.y;
    setSelection(e.detail.x, e.detail.y, e.detail.x, e.detail.y);
  };

  // Handle touch start event to check if the touch is on a handler
  const handleTouchStart = (e: TouchEvent) => {
    if (handlers.length === 0) {
      return;
    }
    const { x, y } = e.detail;
    for (const [index, handler] of handlers.entries()) {
      if (Math.pow(handler.x - x, 2) + Math.pow(handler.y - y, 2) < Math.pow(handler.radius, 2)) {
        isSelecting = true;
        const another = handlers[(index + 1) % 2];
        startPosition = { x: another.startX, y: another.startY };
        break;
      }
    }
  };

  // Handle touch move event to update the selection area
  const handleTouchMove = (e: TouchEvent) => {
    if (isSelecting) {
      setSelection(startPosition.x, startPosition.y, e.detail.x, e.detail.y);
    }
  };

  // Handle touch end event to finalize the selection
  const handleTouchEnd = (e: TouchEvent) => {
    if (isSelecting) {
      setSelection(startPosition.x, startPosition.y, e.detail.x, e.detail.y);
    }
    isSelecting = false;
  };

  // Handle tap event to clear the selection
  const handleTap = () => {
    if (handlers.length === 0) {
      return;
    }
    setSelection(-1, -1, -1, -1);
  };

  // Asynchronous function to get the bounding rectangles of text nodes
  async function getTextNodeRect() {
    let resArray = await new Promise<SelectorQuery[]>((resolve) => {
      lynx.createSelectorQuery()
        .selectAll("#container text")
        .fields(
          {
            // @ts-expect-error TODO(types): support `query` in `@lynx-js/types`
            query: true,
            id: true,
          },
          resolve,
        )
        .exec();
    });

    Promise.all(
      resArray.map((element) => {
        return new Promise<{
          top: number;
          left: number;
          width: number;
          height: number;
          id: string;
        }>((resolve) => {
          // @ts-expect-error TODO(types): support `query` in `@lynx-js/types`
          element.query
            .selectRoot()
            .invoke({
              method: "boundingClientRect",
              success: (res: {
                top: number;
                left: number;
                width: number;
                height: number;
                id: string;
              }) => {
                resolve(res);
              },
            })
            .exec();
        });
      }),
    ).then((values) => {
      textsInfo = [...values].map(({ top, left, width, height, id }) => ({
        id: String(id),
        left: Number(left),
        top: Number(top),
        width: Number(width),
        height: Number(height),
        startX: -1,
        startY: 0,
        endX: width,
        endY: height,
      }));
    });
  }

  // Function to execute text selection on a specific node
  function execSelection(
    node: TextNodeInfo,
    startX: number,
    startY: number,
    endX: number,
    endY: number,
    showStartHandle = true,
    showEndHandle = true,
  ) {
    lynx
      .createSelectorQuery()
      .select(`#${node.id}`)
      .invoke({
        method: "setTextSelection",
        params: {
          startX,
          startY,
          endX,
          endY,
          showStartHandle,
          showEndHandle,
        },
        success(res) {
          if (!res) {
            return;
          }
          const boxes = res.boxes || [];
          const hs = res.handles || [];
          if (Array.isArray(boxes) && boxes.length > 0) {
            node.startX = boxes[0].left;
            node.startY = boxes[0].top + boxes[0].height / 2;
            node.endX = boxes[boxes.length - 1].left + boxes[boxes.length - 1].width;
            node.endY = boxes[boxes.length - 1].top + boxes[boxes.length - 1].height / 2;
          } else {
            node.startX =
              node.startY =
              node.endX =
              node.endY =
                -1;
          }
          showStartHandle && (handlers[0] = { ...hs[0], startX: node.startX, startY: node.startY });
          showEndHandle && (handlers[1] = { ...hs[1], startX: node.endX, startY: node.endY });
        },
      })
      .exec();
    if (startX === -1) {
      node.startX = -1;
      handlers = [];
    }
  }

  // Function to set the text selection based on the start and end coordinates
  function setSelection(x1: number, y1: number, x2: number, y2: number) {
    const [[startX, startY], [endX, endY]] = [
      [x1, y1],
      [x2, y2],
    ].sort((a, b) => {
      if (a[1] === b[1]) {
        return a[0] - b[0];
      }
      return a[1] - b[1];
    });
    const clear: TextNodeInfo[] = [];
    const update: TextNodeInfo[] = [];
    for (const node of textsInfo) {
      if (
        (startY < node.top && node.top + node.height < endY)
        || (node.left <= startX && startX <= node.left + node.width && node.top <= startY
          && startY <= node.top + node.height)
        || (node.left <= endX && endX <= node.left + node.width && node.top <= endY && endY <= node.top + node.height)
      ) {
        update.push(node);
      } else if (node.startX !== -1) {
        clear.push(node);
      }
    }
    if (clear.length > 0 || update.length > 0) {
      for (const node of clear) {
        execSelection(node, -1, -1, -1, -1, false, false);
      }
      const start = update[0];
      const end = update[update.length - 1];
      if (update.length === 1) {
        execSelection(
          start,
          Math.max(0, startX - start.left),
          Math.max(0, startY - start.top),
          Math.min(start.width, endX - start.left),
          Math.min(start.height, endY - start.top),
          true,
          true,
        );
      } else if (update.length > 1) {
        execSelection(
          start,
          Math.max(0, startX - start.left),
          Math.max(0, startY - start.top),
          start.width,
          start.height,
          true,
          false,
        );
        for (let i = 1; i < update.length - 1; i++) {
          execSelection(update[i], 0, 0, update[i].width, update[i].height, false, false);
        }
        execSelection(
          end,
          0,
          0,
          Math.min(end.width, endX - end.left),
          Math.min(end.height, endY - end.top),
          false,
          true,
        );
      }
      return true;
    }
    return false;
  }

  return (
    <page>
      <view className="Background" />
      <view className="App">
        <view
          id="container"
          style={{ width: "90vw" }}
          className="Container"
          bindlongpress={handleLongPress}
          bindtouchstart={handleTouchStart}
          bindtouchmove={handleTouchMove}
          bindtouchend={handleTouchEnd}
          bindtap={handleTap}
        >
          <text id="0" text-selection={true} custom-text-selection={true} flatten={false} className="Title">
            This is title
          </text>
          <view className="SplitLine" />
          <text id="1" className="NormalText" text-selection={true} custom-text-selection={true} flatten={false}>
            1.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
            dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat justo id, feugiat leo.
            Cras eu elementum dui.
          </text>
          <view className="SplitLine" />
          <text id="2" className="NormalText" text-selection={true} custom-text-selection={true} flatten={false}>
            2.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
            dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat justo id, feugiat leo.
            Cras eu elementum dui.
          </text>
          <view className="SplitLine" />
          <text id="3" className="NormalText" text-selection={true} custom-text-selection={true} flatten={false}>
            3.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
            dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat justo id, feugiat leo.
            Cras eu elementum dui.
          </text>
        </view>
      </view>
    </page>
  );
};

export default CrossTextSelection;

root.render(<CrossTextSelection />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



2. Bind Gesture Events on the Wrapper `<view>`

Bind long-press, tap, and touch events on the outer `<view>` container. These will be used to control your custom selection and gesture logic.

```jsx
<view
  id="container"
  style={{ width: '90vw' }}
  className="Container"
  bindlongpress={handleLongPress}
  bindtouchstart={handleTouchStart}
  bindtouchmove={handleTouchMove}
  bindtouchend={handleTouchEnd}
  bindtap={handleTap}
>
  <text
    id="0"
    text-selection={true}
    custom-text-selection={true}
    flatten={false}
    className="Title"
  >
    This is title
  </text>
  <view className="SplitLine" />
</view>
```

3. Handle Selection and Copying Logic

- On component mount, retrieve metadata for all selectable `<text>` nodes, including their ID, dimensions, and positions:

```jsx
const CrossTextSelection = () => {
  useEffect(() => {
    getTextNodeRect();
}, []);

// Asynchronous function to get the bounding rectangles of text nodes
async function getTextNodeRect() {
  // 1.Use lynx.createSelectorQuery () to get the required text node.
  // 2.Call boundingClientRect method of the text node to get the rect of the node.
}

```

- On Long Press: Start Selection
  `handleLongPress()` is triggered on long press. It initiates the selection state, records the starting point, and performs the first selection update:

```jsx
// Handle long press event to start text selection
const handleLongPress = (e) => {
  isSelecting = true;
  startPosition.x = e.detail.x;
  startPosition.y = e.detail.y;
  setSelection(e.detail.x, e.detail.y, e.detail.x, e.detail.y);
};
```

- On Drag: Update Selection Area in Real Time

As the user drags, `handleTouchMove()` is called. If a selection is in progress, it updates the highlighted area accordingly:

```jsx
// Handle touch move event to update the selection area
const handleTouchMove = (e) => {
  if (isSelecting) {
    setSelection(startPosition.x, startPosition.y, e.detail.x, e.detail.y);
  }
};
```

- On Finger Release: Finalize Selection

`handleTouchEnd()` is triggered on finger release. This finalizes the selected region and exits selection mode:

```jsx
// Handle touch end event to finalize the selection
const handleTouchEnd = (e) => {
  if (isSelecting) {
    setSelection(startPosition.x, startPosition.y, e.detail.x, e.detail.y);
  }
  isSelecting = false;
};
```

On Tap Blank Area: Clear Selection

Tapping outside the text elements triggers a selection clear:

```jsx
// Handle tap event to clear the selection
const handleTap = (e) => {
  if (handlers.length === 0) {
    return;
  }
  setSelection(-1, -1, -1, -1);
};
```

- On Handle Drag: Adjust Selection Range

In `handleTouchStart()`, determine if the touch point is near one of the draggable handles. If so, allow real-time adjustment of the selection:

```jsx
// Handle touch start event to check if the touch is on a handler
const handleTouchStart = (e) => {
  if (handlers.length === 0) {
    return;
  }
  const { x, y } = e.detail;
  for (const [index, handler] of handlers.entries()) {
    if (
      Math.pow(handler.x - x, 2) + Math.pow(handler.y - y, 2) <
      Math.pow(handler.radius, 2)
    ) {
      isSelecting = true;
      const another = handlers[(index + 1) % 2];
      startPosition = { x: another.startX, y: another.startY };
      break;
    }
  }
};
```

## Compatibility

### `<text>`

**Compatibility Table**
**Query:** `elements.text`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 1.5 | - |
| iOS | 1.5 | - |
| HarmonyOS | 3.4 | - |
| Clay Android | 1.5 | - |
| Clay iOS | 1.5 | - |
| Clay Windows | 1.5 | - |
| Clay macOS | 1.5 | - |
| Web | ✅ Yes | - |

**Description:** <code>text</code>


### Nested `<text>`

**Compatibility Table**
**Query:** `elements.nested-text`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 1.5 | - |
| iOS | 1.5 | - |
| HarmonyOS | 3.4 | - |
| Clay Android | 1.5 | - |
| Clay iOS | 1.5 | - |
| Clay Windows | 1.5 | - |
| Clay macOS | 1.5 | - |
| Web | ✅ Yes | - |

**Description:** nested <code>text</code>


### nested `<image>`

**Compatibility Table**
**Query:** `elements.nested-image`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 1.5 | - |
| iOS | 1.5 | - |
| HarmonyOS | 3.4 | - |
| Clay Android | 1.5 | - |
| Clay iOS | 1.5 | - |
| Clay Windows | 1.5 | - |
| Clay macOS | 1.5 | - |
| Web | ✅ Yes | - |

**Description:** nested <code>image</code>


### `<inline-truncation>`

**Compatibility Table**
**Query:** `elements.inline-truncation`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 1.5 | - |
| iOS | 1.5 | - |
| HarmonyOS | 3.4 | - |
| Clay Android | 1.5 | - |
| Clay iOS | 1.5 | - |
| Clay Windows | 1.5 | - |
| Clay macOS | 1.5 | - |
| Web | ✅ Yes | - |

**Description:** <code>inline-truncation</code>

