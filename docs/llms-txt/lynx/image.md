# Source: https://lynxjs.org/api/elements/built-in/image.md

# `<image>`

<APISummary />


Used to display different types of images, including web images, static resources, and locally stored images.

:::tip

This feature depends on the image loading service provided by [Lynx Service](/guide/start/integrate-with-existing-apps.md).

:::

## Usage Guide

`<image>` is an [empty element](/guide/ui/elements-components.md#empty-elements) and no longer supports child nodes.

:::note

To display the image correctly, the non-empty [src](/api/elements/built-in/image.md#required-src) attribute must be set, and at least one of the following must be provided:

- A [width](/api/css/properties/width.md) and [height](/api/css/properties/width.md) greater than 0
- [auto-size](/api/elements/built-in/image.md#auto-size)

:::

The following examples show how the `<image>` element is used in different scenarios.

### Displaying images with different cropping/scaling modes

Supports controlling the image cropping/scaling mode using [mode](/api/elements/built-in/image.md#mode).

**This is an example below:  image**

**Bundle:** `dist/main.lynx.bundle` | Web: `dist/main.web.bundle`

```tsx {30-42}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import type { ErrorEvent, LoadEvent } from "@lynx-js/types";

import LynxIcon from "@assets/image/lynxicon.png?inline";
import DoctorIcon from "@assets/image/rsdoctor.png?inline";
import LibIcon from "@assets/image/rslib.png?inline";
import SpeedyIcon from "@assets/image/rspeedy.png?inline";

import "./App.css";

interface ExampleProps {
  url: string;
}

const ImageAutoSizeExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear" style="linear-layout-gravity:left">
      <text className="sub-title">Image AutoSize Examples</text>
      <text>auto-size with no width</text>
      <image className="no-width" src={url} auto-size={true} />
      <text>auto-size with no height</text>
      <image className="no-height" src={url} auto-size={true} />
    </view>
  );
};

const ImageBasicExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Basic Examples</text>
      <text>scaleToFill</text>
      <image src={url} style="width:200px;height:100px" />
      <text>aspectFit</text>
      <image src={url} mode="aspectFit" style="width:200px;height:100px" />
      <text>aspectFill</text>
      <image src={url} mode="aspectFill" style="width:200px;height:100px" />
    </view>
  );
};

const ImageStyledExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Styled Examples</text>
      <text>aspectFit</text>
      <image
        className="mode-image"
        mode="aspectFit"
        src={url}
        style="border-radius: 10px"
      />

      <text>aspectFill</text>
      <image
        className="mode-image"
        mode="aspectFill"
        src={url}
        style="border-radius:50% "
      />

      <text>scaleToFill</text>
      <image
        className="mode-image"
        mode="scaleToFill"
        src={url}
        style="border-radius: 20px 30px 40px 10px"
      />
    </view>
  );
};

const ImageFilterExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Filter Examples</text>
      <text>origin pic</text>
      <image className="filter-image" src={url} />

      <text>blur pic</text>
      <image className="filter-image" src={url} blur-radius="5px" />

      <text>tint pic</text>
      <image className="filter-image" src={url} tint-color="#123aff" />
    </view>
  );
};

const ImageEventExample = ({ url }: ExampleProps) => {
  const handleImageLoad = (event: LoadEvent) => {
    console.log("Image loaded success:", JSON.stringify(event));
  };
  const handleImageError = (event: ErrorEvent) => {
    console.log("Image loaded error:", JSON.stringify(event));
  };
  return (
    <view className="linear">
      <text className="sub-title">Image Event Examples</text>
      <text>load event</text>
      <image className="filter-image" src={url} bindload={handleImageLoad} />
      <text>error event</text>
      <image
        className="filter-image"
        src={"error url"}
        binderror={handleImageError}
      />
    </view>
  );
};

const ImageExample = ({ type, url }: ExampleProps & { type: string }) => {
  switch (type) {
    case "auto-size":
      return <ImageAutoSizeExample url={url} />;
    case "styled":
      return <ImageStyledExample url={url} />;
    case "filter":
      return <ImageFilterExample url={url} />;
    case "event":
      return <ImageEventExample url={url} />;
    default:
      return <ImageBasicExample url={url} />;
  }
};

export const App = () => {
  const examples = [
    { type: "auto-size", url: LynxIcon },
    { type: "basic", url: SpeedyIcon },
    { type: "styled", url: LibIcon },
    { type: "filter", url: DoctorIcon },
    { type: "event", url: SpeedyIcon },
  ];

  return (
    <scroll-view scroll-orientation="vertical" style="padding:5px;width:100%; height:100%;">
      <text className="title">Image Examples</text>
      {examples.map((example, index) => <ImageExample type={example.type} url={example.url} />)}
    </scroll-view>
  );
};

```



### Adding borders, rounded corners, and backgrounds to the image

You can set the image's borders, rounded corners, and background colors using CSS styles.

**This is an example below:  image**

**Bundle:** `dist/main.lynx.bundle` | Web: `dist/main.web.bundle`

```tsx {44-73}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import type { ErrorEvent, LoadEvent } from "@lynx-js/types";

import LynxIcon from "@assets/image/lynxicon.png?inline";
import DoctorIcon from "@assets/image/rsdoctor.png?inline";
import LibIcon from "@assets/image/rslib.png?inline";
import SpeedyIcon from "@assets/image/rspeedy.png?inline";

import "./App.css";

interface ExampleProps {
  url: string;
}

const ImageAutoSizeExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear" style="linear-layout-gravity:left">
      <text className="sub-title">Image AutoSize Examples</text>
      <text>auto-size with no width</text>
      <image className="no-width" src={url} auto-size={true} />
      <text>auto-size with no height</text>
      <image className="no-height" src={url} auto-size={true} />
    </view>
  );
};

const ImageBasicExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Basic Examples</text>
      <text>scaleToFill</text>
      <image src={url} style="width:200px;height:100px" />
      <text>aspectFit</text>
      <image src={url} mode="aspectFit" style="width:200px;height:100px" />
      <text>aspectFill</text>
      <image src={url} mode="aspectFill" style="width:200px;height:100px" />
    </view>
  );
};

const ImageStyledExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Styled Examples</text>
      <text>aspectFit</text>
      <image
        className="mode-image"
        mode="aspectFit"
        src={url}
        style="border-radius: 10px"
      />

      <text>aspectFill</text>
      <image
        className="mode-image"
        mode="aspectFill"
        src={url}
        style="border-radius:50% "
      />

      <text>scaleToFill</text>
      <image
        className="mode-image"
        mode="scaleToFill"
        src={url}
        style="border-radius: 20px 30px 40px 10px"
      />
    </view>
  );
};

const ImageFilterExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Filter Examples</text>
      <text>origin pic</text>
      <image className="filter-image" src={url} />

      <text>blur pic</text>
      <image className="filter-image" src={url} blur-radius="5px" />

      <text>tint pic</text>
      <image className="filter-image" src={url} tint-color="#123aff" />
    </view>
  );
};

const ImageEventExample = ({ url }: ExampleProps) => {
  const handleImageLoad = (event: LoadEvent) => {
    console.log("Image loaded success:", JSON.stringify(event));
  };
  const handleImageError = (event: ErrorEvent) => {
    console.log("Image loaded error:", JSON.stringify(event));
  };
  return (
    <view className="linear">
      <text className="sub-title">Image Event Examples</text>
      <text>load event</text>
      <image className="filter-image" src={url} bindload={handleImageLoad} />
      <text>error event</text>
      <image
        className="filter-image"
        src={"error url"}
        binderror={handleImageError}
      />
    </view>
  );
};

const ImageExample = ({ type, url }: ExampleProps & { type: string }) => {
  switch (type) {
    case "auto-size":
      return <ImageAutoSizeExample url={url} />;
    case "styled":
      return <ImageStyledExample url={url} />;
    case "filter":
      return <ImageFilterExample url={url} />;
    case "event":
      return <ImageEventExample url={url} />;
    default:
      return <ImageBasicExample url={url} />;
  }
};

export const App = () => {
  const examples = [
    { type: "auto-size", url: LynxIcon },
    { type: "basic", url: SpeedyIcon },
    { type: "styled", url: LibIcon },
    { type: "filter", url: DoctorIcon },
    { type: "event", url: SpeedyIcon },
  ];

  return (
    <scroll-view scroll-orientation="vertical" style="padding:5px;width:100%; height:100%;">
      <text className="title">Image Examples</text>
      {examples.map((example, index) => <ImageExample type={example.type} url={example.url} />)}
    </scroll-view>
  );
};

```



### Adding special drawing effects to the image

Supports special drawing effects like Gaussian blur.

**This is an example below:  image**

**Bundle:** `dist/main.lynx.bundle` | Web: `dist/main.web.bundle`

```tsx {75-89}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import type { ErrorEvent, LoadEvent } from "@lynx-js/types";

import LynxIcon from "@assets/image/lynxicon.png?inline";
import DoctorIcon from "@assets/image/rsdoctor.png?inline";
import LibIcon from "@assets/image/rslib.png?inline";
import SpeedyIcon from "@assets/image/rspeedy.png?inline";

import "./App.css";

interface ExampleProps {
  url: string;
}

const ImageAutoSizeExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear" style="linear-layout-gravity:left">
      <text className="sub-title">Image AutoSize Examples</text>
      <text>auto-size with no width</text>
      <image className="no-width" src={url} auto-size={true} />
      <text>auto-size with no height</text>
      <image className="no-height" src={url} auto-size={true} />
    </view>
  );
};

const ImageBasicExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Basic Examples</text>
      <text>scaleToFill</text>
      <image src={url} style="width:200px;height:100px" />
      <text>aspectFit</text>
      <image src={url} mode="aspectFit" style="width:200px;height:100px" />
      <text>aspectFill</text>
      <image src={url} mode="aspectFill" style="width:200px;height:100px" />
    </view>
  );
};

const ImageStyledExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Styled Examples</text>
      <text>aspectFit</text>
      <image
        className="mode-image"
        mode="aspectFit"
        src={url}
        style="border-radius: 10px"
      />

      <text>aspectFill</text>
      <image
        className="mode-image"
        mode="aspectFill"
        src={url}
        style="border-radius:50% "
      />

      <text>scaleToFill</text>
      <image
        className="mode-image"
        mode="scaleToFill"
        src={url}
        style="border-radius: 20px 30px 40px 10px"
      />
    </view>
  );
};

const ImageFilterExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Filter Examples</text>
      <text>origin pic</text>
      <image className="filter-image" src={url} />

      <text>blur pic</text>
      <image className="filter-image" src={url} blur-radius="5px" />

      <text>tint pic</text>
      <image className="filter-image" src={url} tint-color="#123aff" />
    </view>
  );
};

const ImageEventExample = ({ url }: ExampleProps) => {
  const handleImageLoad = (event: LoadEvent) => {
    console.log("Image loaded success:", JSON.stringify(event));
  };
  const handleImageError = (event: ErrorEvent) => {
    console.log("Image loaded error:", JSON.stringify(event));
  };
  return (
    <view className="linear">
      <text className="sub-title">Image Event Examples</text>
      <text>load event</text>
      <image className="filter-image" src={url} bindload={handleImageLoad} />
      <text>error event</text>
      <image
        className="filter-image"
        src={"error url"}
        binderror={handleImageError}
      />
    </view>
  );
};

const ImageExample = ({ type, url }: ExampleProps & { type: string }) => {
  switch (type) {
    case "auto-size":
      return <ImageAutoSizeExample url={url} />;
    case "styled":
      return <ImageStyledExample url={url} />;
    case "filter":
      return <ImageFilterExample url={url} />;
    case "event":
      return <ImageEventExample url={url} />;
    default:
      return <ImageBasicExample url={url} />;
  }
};

export const App = () => {
  const examples = [
    { type: "auto-size", url: LynxIcon },
    { type: "basic", url: SpeedyIcon },
    { type: "styled", url: LibIcon },
    { type: "filter", url: DoctorIcon },
    { type: "event", url: SpeedyIcon },
  ];

  return (
    <scroll-view scroll-orientation="vertical" style="padding:5px;width:100%; height:100%;">
      <text className="title">Image Examples</text>
      {examples.map((example, index) => <ImageExample type={example.type} url={example.url} />)}
    </scroll-view>
  );
};

```



### Adapting to the original image aspect ratio

Use [auto-size](/api/elements/built-in/image.md#auto-size) to automatically adjust the `<image>` size to match the original image aspect ratio.

**This is an example below:  image**

**Bundle:** `dist/main.lynx.bundle` | Web: `dist/main.web.bundle`

```tsx {18-28}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import type { ErrorEvent, LoadEvent } from "@lynx-js/types";

import LynxIcon from "@assets/image/lynxicon.png?inline";
import DoctorIcon from "@assets/image/rsdoctor.png?inline";
import LibIcon from "@assets/image/rslib.png?inline";
import SpeedyIcon from "@assets/image/rspeedy.png?inline";

import "./App.css";

interface ExampleProps {
  url: string;
}

const ImageAutoSizeExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear" style="linear-layout-gravity:left">
      <text className="sub-title">Image AutoSize Examples</text>
      <text>auto-size with no width</text>
      <image className="no-width" src={url} auto-size={true} />
      <text>auto-size with no height</text>
      <image className="no-height" src={url} auto-size={true} />
    </view>
  );
};

const ImageBasicExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Basic Examples</text>
      <text>scaleToFill</text>
      <image src={url} style="width:200px;height:100px" />
      <text>aspectFit</text>
      <image src={url} mode="aspectFit" style="width:200px;height:100px" />
      <text>aspectFill</text>
      <image src={url} mode="aspectFill" style="width:200px;height:100px" />
    </view>
  );
};

const ImageStyledExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Styled Examples</text>
      <text>aspectFit</text>
      <image
        className="mode-image"
        mode="aspectFit"
        src={url}
        style="border-radius: 10px"
      />

      <text>aspectFill</text>
      <image
        className="mode-image"
        mode="aspectFill"
        src={url}
        style="border-radius:50% "
      />

      <text>scaleToFill</text>
      <image
        className="mode-image"
        mode="scaleToFill"
        src={url}
        style="border-radius: 20px 30px 40px 10px"
      />
    </view>
  );
};

const ImageFilterExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Filter Examples</text>
      <text>origin pic</text>
      <image className="filter-image" src={url} />

      <text>blur pic</text>
      <image className="filter-image" src={url} blur-radius="5px" />

      <text>tint pic</text>
      <image className="filter-image" src={url} tint-color="#123aff" />
    </view>
  );
};

const ImageEventExample = ({ url }: ExampleProps) => {
  const handleImageLoad = (event: LoadEvent) => {
    console.log("Image loaded success:", JSON.stringify(event));
  };
  const handleImageError = (event: ErrorEvent) => {
    console.log("Image loaded error:", JSON.stringify(event));
  };
  return (
    <view className="linear">
      <text className="sub-title">Image Event Examples</text>
      <text>load event</text>
      <image className="filter-image" src={url} bindload={handleImageLoad} />
      <text>error event</text>
      <image
        className="filter-image"
        src={"error url"}
        binderror={handleImageError}
      />
    </view>
  );
};

const ImageExample = ({ type, url }: ExampleProps & { type: string }) => {
  switch (type) {
    case "auto-size":
      return <ImageAutoSizeExample url={url} />;
    case "styled":
      return <ImageStyledExample url={url} />;
    case "filter":
      return <ImageFilterExample url={url} />;
    case "event":
      return <ImageEventExample url={url} />;
    default:
      return <ImageBasicExample url={url} />;
  }
};

export const App = () => {
  const examples = [
    { type: "auto-size", url: LynxIcon },
    { type: "basic", url: SpeedyIcon },
    { type: "styled", url: LibIcon },
    { type: "filter", url: DoctorIcon },
    { type: "event", url: SpeedyIcon },
  ];

  return (
    <scroll-view scroll-orientation="vertical" style="padding:5px;width:100%; height:100%;">
      <text className="title">Image Examples</text>
      {examples.map((example, index) => <ImageExample type={example.type} url={example.url} />)}
    </scroll-view>
  );
};

```



### Listening to image load success/failure

You can bind [events](/api/elements/built-in/image.md#events) to listen for the image load state.

**This is an example below:  image**

**Bundle:** `dist/main.lynx.bundle` | Web: `dist/main.web.bundle`

```tsx {91-111}
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import type { ErrorEvent, LoadEvent } from "@lynx-js/types";

import LynxIcon from "@assets/image/lynxicon.png?inline";
import DoctorIcon from "@assets/image/rsdoctor.png?inline";
import LibIcon from "@assets/image/rslib.png?inline";
import SpeedyIcon from "@assets/image/rspeedy.png?inline";

import "./App.css";

interface ExampleProps {
  url: string;
}

const ImageAutoSizeExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear" style="linear-layout-gravity:left">
      <text className="sub-title">Image AutoSize Examples</text>
      <text>auto-size with no width</text>
      <image className="no-width" src={url} auto-size={true} />
      <text>auto-size with no height</text>
      <image className="no-height" src={url} auto-size={true} />
    </view>
  );
};

const ImageBasicExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Basic Examples</text>
      <text>scaleToFill</text>
      <image src={url} style="width:200px;height:100px" />
      <text>aspectFit</text>
      <image src={url} mode="aspectFit" style="width:200px;height:100px" />
      <text>aspectFill</text>
      <image src={url} mode="aspectFill" style="width:200px;height:100px" />
    </view>
  );
};

const ImageStyledExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Styled Examples</text>
      <text>aspectFit</text>
      <image
        className="mode-image"
        mode="aspectFit"
        src={url}
        style="border-radius: 10px"
      />

      <text>aspectFill</text>
      <image
        className="mode-image"
        mode="aspectFill"
        src={url}
        style="border-radius:50% "
      />

      <text>scaleToFill</text>
      <image
        className="mode-image"
        mode="scaleToFill"
        src={url}
        style="border-radius: 20px 30px 40px 10px"
      />
    </view>
  );
};

const ImageFilterExample = ({ url }: ExampleProps) => {
  return (
    <view className="linear">
      <text className="sub-title">Image Filter Examples</text>
      <text>origin pic</text>
      <image className="filter-image" src={url} />

      <text>blur pic</text>
      <image className="filter-image" src={url} blur-radius="5px" />

      <text>tint pic</text>
      <image className="filter-image" src={url} tint-color="#123aff" />
    </view>
  );
};

const ImageEventExample = ({ url }: ExampleProps) => {
  const handleImageLoad = (event: LoadEvent) => {
    console.log("Image loaded success:", JSON.stringify(event));
  };
  const handleImageError = (event: ErrorEvent) => {
    console.log("Image loaded error:", JSON.stringify(event));
  };
  return (
    <view className="linear">
      <text className="sub-title">Image Event Examples</text>
      <text>load event</text>
      <image className="filter-image" src={url} bindload={handleImageLoad} />
      <text>error event</text>
      <image
        className="filter-image"
        src={"error url"}
        binderror={handleImageError}
      />
    </view>
  );
};

const ImageExample = ({ type, url }: ExampleProps & { type: string }) => {
  switch (type) {
    case "auto-size":
      return <ImageAutoSizeExample url={url} />;
    case "styled":
      return <ImageStyledExample url={url} />;
    case "filter":
      return <ImageFilterExample url={url} />;
    case "event":
      return <ImageEventExample url={url} />;
    default:
      return <ImageBasicExample url={url} />;
  }
};

export const App = () => {
  const examples = [
    { type: "auto-size", url: LynxIcon },
    { type: "basic", url: SpeedyIcon },
    { type: "styled", url: LibIcon },
    { type: "filter", url: DoctorIcon },
    { type: "event", url: SpeedyIcon },
  ];

  return (
    <scroll-view scroll-orientation="vertical" style="padding:5px;width:100%; height:100%;">
      <text className="title">Image Examples</text>
      {examples.map((example, index) => <ImageExample type={example.type} url={example.url} />)}
    </scroll-view>
  );
};

```




Used to display images

## Attributes

### `auto-size`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.6
</VersionBadge>

```tsx
// @defaultValue: false
'auto-size'?: boolean;
```

When set to true and the
`<image>`
element has no width or height,
the size of the
`<image>`
will be automatically adjusted
to match the image's original dimensions after the image is successfully loaded,
ensuring that the aspect ratio is maintained.

### `autoplay`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.11
</VersionBadge>

```tsx
// @defaultValue: true
autoplay?: boolean;
```

Specifies whether the animated image should start playing automatically once it is loaded.

### `blur-radius`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  0.2
</VersionBadge>

```tsx
'blur-radius'?: string;
```

Image blur radius

### `cap-insets`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
'cap-insets'?: string;
```

Stretchable area for 9patch images, in percentage or decimal, four values for top, right, bottom, left

### `cap-insets-scale`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: 1
'cap-insets-scale'?: number;
```

Adjust the scale of stretchable area for 9patch images

### `defer-src-invalidation`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.7
</VersionBadge>

```tsx
// @defaultValue: false
'defer-src-invalidation'?: boolean;
```

When set to true, the
`<image>`
will only clear the previously displayed image resource after a new image has successfully loaded.
The default behavior is to clear the image resource before starting a new load.
This can resolve flickering issues when the image src is switched and reloaded. It is not recommended to enable this in scenarios where there is node reuse in views like lists.

### `image-config`

{' '}

<AndroidOnly />

<ClayOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: "ARGB_8888"
'image-config'?: 'ARGB_8888' | 'RGB_565';
```

ARGB\_8888: 32-bit memory per pixel, supports semi-transparent images
RGB\_565: 16-bit memory per pixel, reduces memory usage but loses transparency
Support PC platform since 3.5

### `loop-count`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: 0
'loop-count'?: number;
```

Number of times an animated image plays, 0 stands for infinite

### `mode`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  0.2
</VersionBadge>

```tsx
// @defaultValue: 'scaleToFill'
mode?: 'scaleToFill' | 'aspectFit' | 'aspectFill' | 'center';
```

Specifies image cropping/scaling mode
scaleToFill: Scales the image without preserving the aspect ratio, stretching the image to fill the element
aspectFit: Scales the image while preserving aspect ratio so that the long side is fully visible
aspectFill: Scales the image while preserving aspect ratio, ensuring the short side fills the element
center: Does not scale the image; image is centered

### `placeholder`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
placeholder?: string;
```

Placeholder image, used same as src

### `prefetch-height`

{' '}

<AndroidOnly />

<IOSOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: "0px"
'prefetch-height'?: string;
```

Image won't load if its size is 0, but will load if prefetch-height is set

### `prefetch-width`

{' '}

<AndroidOnly />

<IOSOnly />

<VersionBadge>
  1.4
</VersionBadge>

```tsx
// @defaultValue: "0px"
'prefetch-width'?: string;
```

Image won't load if its size is 0, but will load if prefetch-width is set

### `src`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  0.2
</VersionBadge>

```tsx
// @defaultValue: undefined
src?: string;
```

Supports http/https/base64

### `tint-color`

{' '}

<AndroidOnly />

<IOSOnly />

<HarmonyOnly />

<VersionBadge>
  2.12
</VersionBadge>

```tsx
'tint-color'?: string;
```

Changes the color of all non-transparent pixels to the tint-color specified. The value is a
`<color>`
.

## Events

Frontend can bind corresponding event callbacks to listen for runtime behaviors of the element, as shown below.

### `binderror`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  0.2
</VersionBadge>

```tsx
binderror = (e: ErrorEvent) => {};
```

Image load error event

### `bindload`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  0.2
</VersionBadge>

```tsx
bindload = (e: LoadEvent) => {};
```

Image load success event

## Methods

Frontend can invoke component methods via the [SelectorQuery](/api/lynx-api/nodes-ref/nodes-ref-invoke.md) API.

### `pauseAnimation`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.11
</VersionBadge>

```ts

lynx.createSelectorQuery()
.select('#id')
.invoke({
method: 'pauseAnimation',
success: function (res) {},
fail: function (res) {},
})
.exec();

```

Pauses the animation, without resetting the loop-count.

### `resumeAnimation`

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.11
</VersionBadge>

```ts

lynx.createSelectorQuery()
     .select('#id')
     .invoke({
      method: 'resumeAnimation',
      success: function (res) {},
      fail: function (res) {},
    })
    .exec();

```

Resumes the animation, without resetting the loop-count.

### `startAnimate`

{' '}

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<Deprecated />

```ts

lynx.createSelectorQuery()
.select('#id')
.invoke({
method: 'startAnimate',
success: function (res) {},
fail: function (res) {},
})
.exec();

```

Restart the animation playback method controlled by the front end, and the animation playback progress and loop count will be reset.

### `stopAnimation`

<AndroidOnly />

<IOSOnly />

<ClayOnly />

<HarmonyOnly />

<VersionBadge>
  2.11
</VersionBadge>

```ts

lynx.createSelectorQuery()
     .select('#id')
     .invoke({
      method: 'stopAnimation',
      success: function (res) {},
      fail: function (res) {},
    })
    .exec();

```

Stops the animation, and it will reset the loop-count.

## Advanced Features

### Request URL Redirection Mapping

#### Feature Description

By implementing a URL redirection mechanism, developers can intercept specific image URLs and map them to specific resource paths. This ability is useful for the following scenarios:

- Improving static resource loading speed
- Supporting custom image protocol access schemes
- Protecting sensitive resource access paths

#### Implementation Principle

This feature is implemented based on the [`MediaResourceFetcher`](/api/lynx-native-api/lynx-media-resource-fetcher/should-redirect-url.md) interface, with the core process divided into two stages:

1. **Resource Type Detection** (`isLocalResource`)

   - Determines if the request URL matches the custom protocol
   - Returns a boolean indicating whether to handle it locally

2. **Path Conversion** (`shouldRedirectUrl`)
   - Parses the original URL
   - Converts it into a valid resource path
   - Returns the final accessible URL address

The following example shows how to map a URL like `http://localhost/xxx` to an app's built-in resource path:

<PlatformTabs queryKey="platform">
  <PlatformTabs.Tab platform="ios">
    ```objective-c
    /// Local resource handler header
    #import <LynxMediaResourceFetcher/LynxMediaResourceFetcher.h>

    @interface LocalMediaFetcher : NSObject <LynxMediaResourceFetcher>

    - (NSString *)shouldRedirectUrl:(LynxResourceRequest *)request;

    - (LynxResourceOptionalBool)isLocalResource:(NSURL *)url;

    @end
    ```

    ```objective-c
    /// Local resource handler implementation
    #import "LocalMediaFetcher.h"

    @implementation LocalMediaFetcher

    /**
     * Resource path conversion method
     * @param request Resource request object
     * @return Local file path or empty string
     */
    - (NSString *)shouldRedirectUrl:(LynxResourceRequest *)request {
      NSURL *url = [NSURL URLWithString:request.url];
      NSString *fileType = [url pathExtension];
      NSString *fileName = [[url URLByDeletingPathExtension] lastPathComponent];
      NSString *subdir = [[[url URLByDeletingLastPathComponent] absoluteString] stringByReplacingOccurrencesOfString:@"http://localhost" withString:@""];
      NSString *path = [[NSBundle mainBundle] pathForResource:fileName ofType:fileType inDirectory:subdir];
      return path ? [NSString stringWithFormat:@"file://%@", path] : @"";
    }

    /**
     * Local resource detection method
     * @param url The original request URL
     * @return LynxResourceOptionalBoolTrue indicates the request needs redirection
     */
    - (LynxResourceOptionalBool)isLocalResource:(NSURL *)url {
        return [url.absoluteString hasPrefix:@"http://localhost"] ?
               LynxResourceOptionalBoolTrue :
               LynxResourceOptionalBoolFalse;
    }

    @end
    ```
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="android">
    ```java
    import com.lynx.tasm.resourceprovider.LynxResourceRequest
    import com.lynx.tasm.resourceprovider.media.LynxMediaResourceFetcher
    import com.lynx.tasm.resourceprovider.media.OptionalBool

    /**
     * Custom media resource handler
     *
     * @property protocol The protocol to intercept "http://localhost"
     * @property scheme The target resource protocol "asset://"
     */
    class LocalMediaFetcher : LynxMediaResourceFetcher() {

        /**
         * Determines if the resource is local
         * @param url The original request URL
         * @return OptionalBool.TRUE indicates the request needs redirection
         */
        override fun isLocalResource(url: String?): OptionalBool {
            return if (url?.startsWith("http://localhost") == true) {
                OptionalBool.TRUE
            } else {
                OptionalBool.FALSE
            }
        }

        /**
         * Performs URL redirection
         * @param request The resource request object
         * @return The converted valid resource path
         */
        override fun shouldRedirectUrl(request: LynxResourceRequest?): String {
            return request?.url?.replace(
                oldValue = "http://localhost",
                newValue = "asset://",
                ignoreCase = true
            ) ?: ""
        }
    }
    ```
  </PlatformTabs.Tab>

  <PlatformTabs.Tab platform="harmony">
    ```typescript
    import {
      LynxMediaResourceFetcher,
      LynxResourceRequest,
      LynxOptionalBool,
    } from '@lynx/lynx';

    // Local resource handler implementation
    export class ExampleMediaResourceFetcher extends LynxMediaResourceFetcher {
      // Resource path conversion method
      // @param request Resource request object
      // @return Local file path or empty string
      shouldRedirectUrl(request: LynxResourceRequest): string {
        return request.url?.replace('http://localhost', 'file://') ?? '';
      }

      // Determines if the resource is local
      // @param url The original request URL
      // @return LynxOptionalBool.TRUE indicates the request needs redirection
      isLocalResource(url: string): LynxOptionalBool {
        if (url.startsWith('http://localhost')) {
          return LynxOptionalBool.TRUE;
        }
        return LynxOptionalBool.FALSE;
      }
    }
    ```
  </PlatformTabs.Tab>
</PlatformTabs>

Read the API reference of [`MediaResourceFetcher`](/api/lynx-native-api/lynx-media-resource-fetcher/should-redirect-url.md) for more details.

## Compatibility

**Compatibility Table**
**Query:** `elements.image`

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

**Description:** image


```
```
