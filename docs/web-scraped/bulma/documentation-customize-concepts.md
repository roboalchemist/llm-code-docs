# Source: https://bulma.io/documentation/customize/concepts/

Title: Bulma Customization Concepts

URL Source: https://bulma.io/documentation/customize/concepts/

Markdown Content:
Bulma is a **highly customizable CSS framework**. From colors to typography, spacing and sizes, forms and layouts, all parts of Bulma can be customized by the user.

Bulma’s styles and variables are defined at several levels:

*   Global Sass variables
*   Component Sass variables
*   Global CSS variables
*   Component CSS variables
*   Helper classes

All Bulma components are styled using **Sass variables** and **CSS Variables** (which are also called CSS custom properties). Read more about them:

*   [on the Sass website](https://sass-lang.com/documentation/variables/)
*   [on the MDN Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

### Global Sass Variables [#](https://bulma.io/documentation/customize/concepts/#global-sass-variables)

Bulma uses Sass variables globally defined in 2 files located in the `utilities` folder:

*   `initial-variables.scss` where you define variables by literal value 
    *   **colors** like `$blue: hsl(229, 53%, 53%)`
    *   **font sizes** like `$size-1: 3rem`
    *   **dimensions** like `$block-spacing: 1.5rem`
    *   **breakpoints** like `$tablet: 769px`
    *   **other values** like `$easing: ease-out` or `$radius-large: 0.75rem`

*   `derived-variables.scss` where variables are calculated from the values set in the previous file 
    *   **primary colors**: 
        *   `$primary`
        *   `$link`
        *   `$success`
        *   `$info`
        *   `$warning`
        *   `$dark`

    *   **utility colors**: 
        *   `$background`
        *   `$border`
        *   `$code` and `$pre`
        *   `$shadow-color`

    *   **typography**: 
        *   `$family-primary`
        *   `$family-secondary`
        *   `$family-code`
        *   `$size-small`
        *   `$size-normal`
        *   `$size-medium`
        *   `$size-large`

    *   color maps: 
        *   `$colors`
        *   `$shades`
        *   `$sizes`

### Component Sass variables [#](https://bulma.io/documentation/customize/concepts/#component-sass-variables)

All Bulma components define its own Sass variables. For example, `components/breadcrumb.scss` define the following:

### Sass and CSS variables [#](https://bulma.io/documentation/customize/concepts/#sass-and-css-variables)

| Sass Variable | Value |
| --- | --- |
| `$breadcrumb-item-color` | `var(--bulma-link-text)` |
| `$breadcrumb-item-hover-color` | `var(--bulma-link-text-hover)` |
| `$breadcrumb-item-active-color` | `var(--bulma-link-text-active)` |
| `$breadcrumb-item-padding-vertical` | `0` |
| `$breadcrumb-item-padding-horizontal` | `0.75em` |
| `$breadcrumb-item-separator-color` | `var(--bulma-border)` |

### Global CSS Variables [#](https://bulma.io/documentation/customize/concepts/#global-css-variables)

Bulma uses global CSS variables defined at the `:root` level. They are all prefixed with `bulma-`:

```
:root {
  /* Colors and Lightness values */
  --bulma-scheme-h: 221;
  --bulma-scheme-s: 14%;
  --bulma-light-l: 90%;
  --bulma-light-invert-l: 20%;
  --bulma-dark-l: 20%;
  --bulma-dark-invert-l: 90%;
  --bulma-soft-l: 90%;
  --bulma-bold-l: 20%;
  --bulma-soft-invert-l: 20%;
  --bulma-bold-invert-l: 90%;
  /* etc. */

  /* Color Palettes */
  --bulma-primary: hsla(var(--bulma-primary-h), var(--bulma-primary-s), var(--bulma-primary-l), 1);
  --bulma-primary-base: hsla(var(--bulma-primary-h), var(--bulma-primary-s), var(--bulma-primary-l), 1);
  --bulma-primary-rgb: 0, 209, 178;
  --bulma-primary-h: 171deg;
  --bulma-primary-s: 100%;
  --bulma-primary-l: 41%;
  --bulma-primary-00-l: 1%;
  --bulma-primary-05-l: 6%;
  --bulma-primary-10-l: 11%;
  --bulma-primary-15-l: 16%;
  --bulma-primary-20-l: 21%;
  /* etc. */

  /* Typography */
  --bulma-family-primary: Inter, SF Pro, Segoe UI, Roboto, Oxygen, Ubuntu, Helvetica Neue, Helvetica, Arial, sans-serif;
  --bulma-family-secondary: Inter, SF Pro, Segoe UI, Roboto, Oxygen, Ubuntu, Helvetica Neue, Helvetica, Arial, sans-serif;
  --bulma-family-code: Inconsolata, Hack, SF Mono, Roboto Mono, Source Code Pro, Ubuntu Mono, monospace;
  --bulma-size-small: 0.75rem;
  --bulma-size-normal: 1rem;
  --bulma-size-medium: 1.25rem;
  --bulma-size-large: 1.5rem;
  /* etc. */
}
```

You can **overwrite** them simply by setting a new value at the same scope (or even a more specific one):

```
:root {
  /* Set new values */
  --bulma-scheme-h: 35;
  --bulma-scheme-s: 20%;
}
```

### Components CSS Variables [#](https://bulma.io/documentation/customize/concepts/#components-css-variables)

Bulma is also styled at the **component** level. For example, here is how the `.title` element is styled:

```
.title {
  --bulma-title-color: var(--bulma-text-strong);
  --bulma-title-family: false;
  --bulma-title-size: var(--bulma-size-3);
  --bulma-title-weight: var(--bulma-weight-extrabold);
  --bulma-title-line-height: 1.125;
  --bulma-title-strong-color: inherit;
  --bulma-title-strong-weight: inherit;
  --bulma-title-sub-size: 0.75em;
  --bulma-title-sup-size: 0.75em;
}

.title {
  color: var(--bulma-title-color);
  font-size: var(--bulma-title-size);
  font-weight: var(--bulma-title-weight);
  line-height: var(--bulma-title-line-height);
}
```

You can overwrite this simply by setting new values under the same scope:

```
.title {
  --bulma-title-color: #fff;
  --bulma-title-line-height: 1.6;
}
```
