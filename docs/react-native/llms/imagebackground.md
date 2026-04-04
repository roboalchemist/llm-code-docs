# Source: https://reactnative.dev/docs/imagebackground.md

# ImageBackground

A common feature request from developers familiar with the web is `background-image`. To handle this use case, you can use the `<ImageBackground>` component, which has the same props as `<Image>`, and add whatever children to it you would like to layer on top of it.

You might not want to use `<ImageBackground>` in some cases, since the implementation is basic. Refer to `<ImageBackground>`'s [source code](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Image/ImageBackground.js) for more insight, and create your own custom component when needed.

Note that you must specify some width and height style attributes.

## Example[​](#example "Direct link to Example")

***

# Reference

## Props[​](#props "Direct link to Props")

### [Image Props](/docs/image.md#props)[​](#image-props "Direct link to image-props")

Inherits [Image Props](/docs/image.md#props).

***

### `imageStyle`[​](#imagestyle "Direct link to imagestyle")

| Type                                      |
| ----------------------------------------- |
| [Image Style](/docs/image-style-props.md) |

***

### `imageRef`[​](#imageref "Direct link to imageref")

A ref setter that will be assigned the [element node](/docs/element-nodes.md) of the inner `Image` component when mounted.

***

### `style`[​](#style "Direct link to style")

| Type                                    |
| --------------------------------------- |
| [View Style](/docs/view-style-props.md) |
