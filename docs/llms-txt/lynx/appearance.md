# Source: https://lynxjs.org/guide/styling/appearance.md

# Visual Appearance


## Background and Borders

You can do a lot creative things with background and borders. Using [`background-image`](/api/css/properties/background-image.md) to
apply network image or gradient effects to the background area of an element, using [`border-radius`](/api/css/properties/border-radius.md) to add a rounded corner, using [`box-shadow`](/api/css/properties/box-shadow.md) to create a shadow effect.

In the following example, we add a background with gradient effect, two styles of borders at top and left sides, a black shadow to an element with the top right corner rounded.

**This is an example below:  css**

**Entry:** `src/border_background_shadow`
**Bundle:** `dist/border_background_shadow.lynx.bundle` | Web: `dist/border_background_shadow.web.bundle`

```tsx {8-12}
import { root } from "@lynx-js/react";

function App() {
  return (
    <view
      style={{
        flexDirection: "column",
        background: "linear-gradient(to right, rgb(255,53,26), rgb(0,235,235))",
        borderRadius: "0 50% 0 0",
        boxShadow: "3px 5px 5px black",
        borderLeft: "2px rgb(0,235,235) dotted",
        borderTop: "2px rgb(255,53,26) dashed",
        marginTop: "50%",
        transform: "translate(-50%, -50%)",
        marginLeft: "50%",
        width: "150px",
        height: "150px",
      }}
    >
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



:::info

[`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-image) and related properties are under development.

:::

## Colors

With Lynx CSS, you can apply color values to various properties to create the look you want.

### Properties that can have color

#### Text

- [`color`](/api/css/properties/color.md): The color to use when drawing the text.
- [`-x-handle-color`](): The color of selection handlers (the cursur on the two ends of the selected text) when text is selected.
- [`text-shadow`](/api/css/properties/text-shadow.md): The color of the shadow in the shape of text.
- [`text-decoration-color`](/api/css/properties/text-decoration.md#text-decoration-color): The color to use when drawing the decoration line on the text.

#### Background and Border

- [`background-color`](/api/css/properties/background-color.md): The background color of the element.
- [`box-shadow`](/api/css/properties/box-shadow.md): The color of shadow.
- [`border-color`](/api/css/properties/border-color.md): The color to use when drawing the border. Can be set separately for the foursides via [`border-top-color`](/api/css/properties/border-color.md), [`border-top-color`](/api/css/properties/border-color.md), [`border-top-color`](/api/css/properties/border-color.md) or [`border-top-color`](/api/css/properties/border-color.md) as well.

Colors can be set to the property via [`selectors`](/api/css/selectors.md) or the `style` property of the element directly.
The color value should be a hex number start with a '#', or a value calculated by function `rgb()`, `rgba()` or `hsl()`. View the specification for [`<color>`](/api/css/data-type/color.md) value for more details.

## Gradient

You can use [`<gradient>`](/api/css/data-type/gradient.md) value to define a gradient effect and apply it to the following properties:

- [`color`](/api/css/properties/color.md): Drawing the text with a gradient effect.
- [`background-image`](/api/css/properties/background-image.md): Fill the background area with a gradient effect.
- [`mask-image`](/api/css/properties/mask-image.md): Use the gradient effect to create a alpha mask.

<table rules="none" align="center" width="100%" style={{tableLayout:"fixed"}}>
  <tr style={{height: '275px'}}>
    <td style={{padding: '15px'}}>
      <center>
        <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/color-gradient.png" style={{width: "80%"}} />

        <br />

        <span>
          Text with a gradient 

          <code>color</code>
        </span>
      </center>
    </td>

    <td style={{padding: '15px'}}>
      <center>
        <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/guide-radial-gradient.png" style={{width: "80%"}} />

        <br />

        <span>
          Filling background with 

          <code>radial-gradient</code>
        </span>
      </center>
    </td>

    <td style={{padding: '15px'}}>
      <center>
        <img src="https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/assets/doc/guide-fading-edge.gif" style={{width: "80%"}} />

        <br />

        <span>
           Create a 'fading edge' effect by adding 

          <code>linear-gradient</code>

           to 

          <code>mask-image</code>

          property
        </span>
      </center>
    </td>
  </tr>
</table>

## Clipping and Masking

In Lynx, besides [`overflow`](/api/css/properties/overflow.md), you can show content of an element in the area you want using [`clip-path`](/api/css/properties/clip-path.md) and [`mask-image`](/api/css/properties/mask-image.md).

**This is an example below:  css**

**Entry:** `src/clip_path_super_ellipse`
**Bundle:** `dist/clip_path_super_ellipse.lynx.bundle` | Web: `dist/clip_path_super_ellipse.web.bundle`

```tsx {14}
import { root } from "@lynx-js/react";

function App() {
  return (
    <view
      style={{
        flexDirection: "column",
        background: "radial-gradient(circle at top left, rgb(255,53,26), rgb(0,235,235))",
        marginTop: "50%",
        transform: "translate(-50%, -50%)",
        marginLeft: "50%",
        width: "150px",
        height: "150px",
        clipPath: "inset(5px super-ellipse 3 3 50px/50px)",
      }}
    >
      <text
        style={{
          fontSize: "32px",
          fontWeight: "bold",
          alignSelf: "center",
          color: "white",
          marginTop: "50%",
          transform: "translateY(-50%)",
        }}
      >
        LYNX
      </text>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



<center>
  <span>
    Using <code>clip-path</code> to clip out a super-elliptical area
  </span>
</center>

**This is an example below:  css**

**Entry:** `src/mask_image_circle_gradient`
**Bundle:** `dist/mask_image_circle_gradient.lynx.bundle` | Web: `dist/mask_image_circle_gradient.web.bundle`

```tsx {14}
import { root } from "@lynx-js/react";

function App() {
  return (
    <view
      style={{
        marginTop: "50%",
        transform: "translate(-50%, -50%)",
        marginLeft: "50%",
        width: "150px",
        height: "150px",
      }}
    >
      <view
        style={{
          flexDirection: "column",
          background: "radial-gradient(circle at top left, rgb(255,53,26), rgb(0,235,235))",
          width: "100%",
          height: "100%",
          maskImage: "radial-gradient(circle 75px, black 75%, transparent)",
          position: "absolute",
        }}
      >
        <text
          style={{
            fontSize: "32px",
            fontWeight: "bold",
            alignSelf: "center",
            color: "white",
            marginTop: "50%",
            transform: "translateY(-50%)",
          }}
        >
          LYNX
        </text>
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



<center>
  <span>
    Using <code>mask-image</code> to create a circle area with fading edge
  </span>
</center>
