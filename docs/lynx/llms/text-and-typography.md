# Source: https://lynxjs.org/guide/styling/text-and-typography.md

# Typography

## Text in Lynx

In Lynx, the text content needs to be written inside the [`<text>`](/api/elements/built-in/text.md) element. This is different from HTML, where text can be directly written inside a `<div>`. Let's look at a simple example:

```tsx
//❌ This won't work
<view>hello world</view>

//✅ Use the <text> component
<text>hello world</text>
```

You can add styles to the `<text>` element to change the text effect. For example, to change the text color:

```tsx
<text style={{ color: 'red' }}>hello world</text>
```

Similarly, to change the text size and make the text italic:

```tsx
<text style={{ fontSize:"30px" }}>hello world</text>
<text style={{ fontStyle:"italic" }}>hello world</text>
```

Lynx also supports adding shadows or strokes to the text by setting the [`text-shadow`](/api/css/properties/text-shadow.md) and [`text-stroke`](/api/css/properties/text-stroke.md) properties to enrich the display effect:

**This is an example below:  text**

**Entry:** `src/shadow_and_stroke`
**Bundle:** `dist/shadow_and_stroke.lynx.bundle` | Web: `dist/shadow_and_stroke.web.bundle`

```tsx {15-20}
import { root } from "@lynx-js/react";
import { Component } from "@lynx-js/react";

export default class TextShadowAndStrokeExample extends Component {
  render() {
    return (
      <view
        style={{
          display: "flex",
          flexDirection: "column",
          width: "100%",
          alignItems: "center",
        }}
      >
        <text style={{ textShadow: "2px 2px 4px green", fontSize: "30px" }}>
          Text Shadow
        </text>
        {/* @ts-expect-error TODO(types): Support textStroke in `@lynx-js/types` */}
        <text style={{ textStroke: "1px red", fontSize: "30px" }}>
          Text Stroke
        </text>
      </view>
    );
  }
}
root.render(<TextShadowAndStrokeExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Mixing Text with Different Styles

In daily text layout, it is often necessary to highlight some parts of the text, such as making keywords bold and changing their color. Suppose we want to make "important word" in the text "This is an important word" bold and red. We can put "important word" into an nested `<text>` and set the `color` and `font-weight` properties.

```tsx
<view>
  <text>
    This is an
    <text style={{ color: 'red', fontWeight: 'bold' }}>important word</text>
  </text>
</view>
```

You can use the properties in the CSS text module to control how text is displayed, such as line-breaking, alignment, and whitespace handling, to achieve more diverse text layout effects. For example, use [`text-indent`](/api/css/properties/text-indent.md) to control the first-line indentation of text, [`word-break`](/api/css/properties/word-break.md) to control the line-breaking behavior of words, and [`text-align`](/api/css/properties/text-align.md) to control the horizontal alignment of text content.

The following is an example of the comprehensive use of properties. You can also refer to [text-related properties](/api/elements/built-in/text.md#text-related-css-properties).

**This is an example below:  text**

**Entry:** `src/text_layout`
**Bundle:** `dist/text_layout.lynx.bundle` | Web: `dist/text_layout.web.bundle`

```tsx
import { root } from "@lynx-js/react";
import { Component } from "@lynx-js/react";

export default class TextLayoutExample extends Component {
  render() {
    return (
      <view
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          width: "100%",
        }}
      >
        <text
          style={{
            fontSize: "30px",
            color: "linear-gradient(to right, red,orange,yellow,green,blue,indigo,violet)",
          }}
        >
          Text Gradient Title
        </text>
        <text
          style={{ fontSize: "20px", textIndent: "20px", lineHeight: "30px" }}
        >
          You can
          <text style={{ fontWeight: "bold", fontSize: "20px" }}>
            {" "}
            bold
          </text>{" "}
          the text that needs to be emphasized.
          <text
            style={{
              backgroundImage: "linear-gradient(360deg, rgba(74, 170, 159, 0.2) 0%, rgba(74, 170, 159, 0) 100%)",
              backgroundSize: "100% 8px",
              backgroundPosition: "0 100%",
              backgroundRepeat: "no-repeat",
              fontSize: "20px",
            }}
          >
            You can add a gradual change to the background color of the text.
          </text>
          <text style={{ textDecoration: "underline", fontSize: "20px" }}>
            You can underline the sentence.
          </text>
        </text>
      </view>
    );
  }
}
root.render(<TextLayoutExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Implementing Text-Image Mixing Layout

To create more colorful pages, it is often necessary to embed images in text. The following describes how to mix text and images in layout. Take the following figure as an example:

<p align="center">
  <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/inline-image-demo.png" width="300" />
</p>

The first step is to use the `<text>` and `<image>` elements to build the page structure. They cooperate with each other to construct the basic framework.

```tsx
<text>
  <image />
  <text>
    This is a warning message.This is a warning message.This is a warning
    message.
  </text>
</text>
```

The second step is to set the style of the `<image>` element. The key is to set the width and height to ensure that the image is presented appropriately on the page and is compatible with the text. At the same time, set the `text-align` property on the `<text>` element to center the text horizontally.

**This is an example below:  text**

**Entry:** `src/inline_image`
**Bundle:** `dist/inline_image.lynx.bundle` | Web: `dist/inline_image.web.bundle`

```tsx {8-18}
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



The third step is to adjust the vertical position of the image within the line. By default, the bottom of the `<image>` element aligns with the text baseline. You can use the [`vertical-align`](/api/css/properties/vertical-align.md) property to precisely adjust the vertical position of the `<image>` element within the line.

**This is an example below:  text**

**Entry:** `src/inline_image`
**Bundle:** `dist/inline_image.lynx.bundle` | Web: `dist/inline_image.web.bundle`

```tsx {15}
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



In addition to images, you can also nest `<view>` within the `<text>` component to create more complex pages.

**This is an example below:  text**

**Entry:** `src/inline_view`
**Bundle:** `dist/inline_view.lynx.bundle` | Web: `dist/inline_view.web.bundle`

```tsx {11-26}
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



## Text Truncation and Ellipsis

When the text content is long and the space is limited, it is necessary to use ellipsis techniques to make the page concise and avoid information clutter. In Lynx, the [`text-overflow`](/api/css/properties/text-overflow.md) property can be used to add an ellipsis effect at the text truncation point. You can choose `ellipsis` to automatically add an ellipsis, or use `clip` to truncate according to the rules.

In specific implementation, first limit the number of lines or height of the `<text>` element. When the text exceeds the range, the ellipsis effect will be triggered. Then set the `text-overflow` property to control the presentation method:

```tsx
<text text-maxline={'1'} style={{ textOverflow: 'ellipsis' }}>
  This is an extremely long text.
</text>
```

Although `text-overflow` cannot directly specify the content displayed at the truncation point, the `<inline-truncation>` element provided by Lynx has strong customization capabilities and can display various contents such as images and `<view>` at the truncation point.

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



## Custom Font Settings

You can directly use [`@font-face`](/api/css/at-rule/font-face.md) to specify custom font resources (the [client needs to support the font resource loader](/api/elements/built-in/text.md#loading-custom-fonts)). At the same time, set the corresponding `font-family` on the `<text>` element.

In addition, if you need to load a font file in JS, you can refer to the addFont API designed based on Web Font Loading. This module provides the FontFace class and the [addFont](/api/lynx-api/lynx/lynx-add-font.md) method on the global object `lynx`.

**This is an example below:  text**

**Entry:** `src/custom_font`
**Bundle:** `dist/custom_font.lynx.bundle` | Web: `dist/custom_font.web.bundle`

```tsx
import { root } from "@lynx-js/react";
import { Component } from "@lynx-js/react";
import fontFile from "../../assets/font/Doto-Regular.ttf";

import "./index.scss";

export default class CustomFontExample extends Component<{}, { fontName: string }> {
  constructor(props: {}) {
    super(props);
    this.state = { fontName: "PingFang" };
  }
  componentDidMount() {
    lynx.addFont(
      {
        "font-family": "Doto",
        "src": `url(${fontFile})`,
      },
      () => {
        console.log("load Doto font");
        this.setState({ fontName: "Doto" });
      },
    );
  }
  render() {
    return (
      <view
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          width: "100%",
        }}
      >
        <text>Whereas recognition of the inherent dignity</text>
        <text style={{ fontFamily: "Inter" }}>Whereas recognition of the inherent dignity</text>
        <text style={{ fontFamily: this.state.fontName }}>Whereas recognition of the inherent dignity</text>
        <text style={{ fontFamily: "Icon" }}>&#xEA01;</text>
      </view>
    );
  }
}
root.render(<CustomFontExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```


