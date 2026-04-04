# Source: https://lynxjs.org/rspeedy/styling.md

# Source: https://lynxjs.org/guide/ui/styling.md

# Styling with CSS

Cascading Style Sheets (CSS) are used to style and layout Lynx pages. For example, you can change the font, color, size, and position of the content, split the content into multiple columns, or add animations and other decorative elements to make your pages more vivid and interesting.
In addition, Lynx provides numerous properties starting with `-x-` to help you achieve style design more easily.
The following tutorial will demonstrate how to add styles to elements using CSS.

:::tip

If you have no basic knowledges about CSS,
you can go through the [guidance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics) from web docs.

:::

## Selectors and inline styles

You can use selectors and inline styles to set values to element's properties.

Such as using `class` attribute with a class selector:

The following example set the background property of the element whose `class` has 'bg-gradient'.

**This is an example below:  css**

**Entry:** `src/class_guide`
**Bundle:** `dist/class_guide.lynx.bundle` | Web: `dist/class_guide.web.bundle`

```tsx {16}
import { root } from "@lynx-js/react";

import "./index.css";

function App() {
  return (
    <view
      style={{
        flexDirection: "column",
        marginTop: "50%",
        transform: "translate(-50%, -50%)",
        marginLeft: "50%",
        width: "150px",
        height: "150px",
      }}
      className="bg-gradient"
    >
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



And you can also set the element's properties via `style` attribute directly. In the example before, we use `style` to change the element's position and size.

- [Learn more about styling properties](/guide/styling/appearance.md)
- [Property API references](/api/css/properties.md)
- [Selector API references](/api/css/selectors.md)

### Nesting

With nesting syntax, you can declare classes in an easier way.
You can get this in [Sass](/rspeedy/styling.md#%E4%BD%BF%E7%94%A8-sass), which is already supported in ReactLynx, or other [post css plugins](/rspeedy/styling.md#using-postcss), such as [postcss-nesting](https://github.com/csstools/postcss-plugins/tree/main/plugins/postcss-nesting).

```scss
.a {
  background: red;
  &-b {
    border-radius: 30px;
  }
}

/* equals */

.a {
  background: red;
}

.a-b {
  border-radius: 30px;
}
```

## CSS cascading

The [Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Cascade) specification defines which value takes effect when multiple selectors applied to the same element, and they got duplicate properties with different values.

For example, properties set by `style` attribute covers those set by style rules (e.g class selector), class with higher [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity) covers those lower ones.

**This is an example below:  css**

**Entry:** `src/cascade_guide`
**Bundle:** `dist/cascade_guide.lynx.bundle` | Web: `dist/cascade_guide.web.bundle`

```css
.bg-gradient {
  background: radial-gradient(
    circle at top left,
    rgb(255, 53, 26),
    rgb(0, 235, 235)
  );
}

.bg-color {
  background: rgb(255, 53, 26);
}

```



In the case above，both two selectors, `bg-gradient` and `bg-color` are taking effect on the `<view>`，and they are both changing the `background` property.
Following the specification of the cascade, the class appears later in the document covers the earlier one, thus the rectangle should be red.

## CSS Variables and Opt-in Inheritance

Lynx supports [CSS custom properties](/api/css/properties/css-variable.md) (CSS variables) and opt-in CSS inheritance for dynamic styling and theming.

CSS custom properties are inherited by default, while regular (non-custom) CSS properties require explicit configuration.
See the Theming guide for details:

- [Switch themes using CSS descendant selectors](/guide/styling/custom-theming.md#using-css-descendant-selectors-to-switch-themes)
- [Switch themes using CSS custom properties](/guide/styling/custom-theming.md#using-css-variables-to-switch-themes)
- [Configure Lynx's opt-in CSS inheritance](/guide/styling/custom-theming.md#leveraging-css-inheritance-as-needed)
