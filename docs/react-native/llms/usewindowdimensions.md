# Source: https://reactnative.dev/docs/usewindowdimensions.md

# useWindowDimensions

tsx

```
import {useWindowDimensions} from 'react-native';
```

`useWindowDimensions` automatically updates all of its values when screen size or font scale changes. You can get your application window's width and height like so:

tsx

```
const {height, width} = useWindowDimensions();
```

## Example[​](#example "Direct link to Example")

## Properties[​](#properties "Direct link to Properties")

### `fontScale`[​](#fontscale "Direct link to fontscale")

tsx

```
useWindowDimensions().fontScale;
```

The scale of the font currently used. Some operating systems allow users to scale their font sizes larger or smaller for reading comfort. This property will let you know what is in effect.

***

### `height`[​](#height "Direct link to height")

tsx

```
useWindowDimensions().height;
```

The height in pixels of the window or screen your app occupies.

***

### `scale`[​](#scale "Direct link to scale")

tsx

```
useWindowDimensions().scale;
```

The pixel ratio of the device your app is running on. The values can be:

* `1` which indicates that one point equals one pixel (usually PPI/DPI of 96, 76 on some platforms).
* `2` or `3` which indicates a Retina or high DPI display.

***

### `width`[​](#width "Direct link to width")

tsx

```
useWindowDimensions().width;
```

The width in pixels of the window or screen your app occupies.
