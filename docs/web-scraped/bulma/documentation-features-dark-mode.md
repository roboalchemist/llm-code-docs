# Source: https://bulma.io/documentation/features/dark-mode/

Title: Dark Mode in Bulma

URL Source: https://bulma.io/documentation/features/dark-mode/

Markdown Content:
Modern browsers come with a way to detect if a user has set their theme preference to `light` or `dark` by using the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) keyword.

This value can be used in a media query to change a website’s styles accordingly:

```
@media (prefers-color-scheme: dark) {
  :root {
    /* Update CSS variables */
  }
}
```

However, it’s not possible for a website to alter this preference. That’s why it’s preferable to **also** add a `data-theme` HTML attribute or a `theme-dark` CSS class.

This is how Bulma defines its dark theme:

```
@media (prefers-color-scheme: dark) {
  :root {
    /* Update CSS variables */
  }
}

[data-theme=dark],
.theme-dark {
  /* Update CSS variables */
}
```

With these rules:

*   the website will be **light by default**, if no user preference is set
*   it will also be **light** if the user has set their preference to `light`
*   the website will be **dark** if the user has set their preference to `dark`

### Force Dark Mode within a page [#](https://bulma.io/documentation/features/dark-mode/#force-dark-mode-within-a-page)

You can **enable** Dark Mode in part of your HTML by simply using the HTML attribute or the CSS class:

```
<div>
  This is in Light Mode if the user hasn't set a preference, or if their preference is set to <code>light</code>.
</div>

<div data-theme="dark">
  This is in Dark Mode
</div>

<div class="theme-dark">
  This is also in Dark Mode
</div>
```

### Force Dark Mode for a whole webpage [#](https://bulma.io/documentation/features/dark-mode/#force-dark-mode-for-a-whole-webpage)

If you want to enable Dark Mode for a whole webpage, simply set the attribute or the class on the `<html>` element:

```
<html data-theme="dark">
<!-- Or -->
<html class="theme-dark">
```

### How the Dark theme is created [#](https://bulma.io/documentation/features/dark-mode/#how-the-dark-theme-is-created)

This is the content of the `sass/themes/dark.scss` file:

```
@use "sass/utilities/initial-variables" as iv;
@use "sass/utilities/css-variables" as cv;
@use "sass/utilities/derived-variables" as dv;
@use "sass/themes/setup";

// The main lightness of this theme
$scheme-main-l: 11%;
$background-l: 14%;
$text-l: 71%;

// The main scheme color, used to make calculations
$scheme-main: hsl(iv.$scheme-h, iv.$scheme-s, $scheme-main-l);
$background: hsl(iv.$scheme-h, iv.$scheme-s, $background-l);
$text: hsl(iv.$scheme-h, iv.$scheme-s, $text-l);

@mixin dark-theme {
  // Required: update the lightness colors and hover/active states
  @include cv.register-vars(
    (
      "scheme-brightness": "dark",
      "scheme-main-l": $scheme-main-l,
      "scheme-main-bis-l": $scheme-main-l + 2%,
      "scheme-main-ter-l": $scheme-main-l + 4%,
      "background-l": $background-l,
      "border-weak-l": 21%,
      "border-l": 24%,
      "text-weak-l": 53%,
      "text-l": $text-l,
      "text-strong-l": 93%,
      "text-title-l": 100%,
      "hover-background-l-delta": 5%,
      "active-background-l-delta": 10%,
      "hover-border-l-delta": 10%,
      "active-border-l-delta": 20%,
      "hover-color-l-delta": 5%,
      "active-color-l-delta": 10%,
    )
  );

  // Required: update the "on scheme" colors since the main scheme color is changed
  // from white (100% lightness)
  // to black (11% lightness in this case)
   @each $name, $color in dv.$colors {
    @include cv.generate-on-scheme-colors($name, $color, $scheme-main);
  }

  // Optional: update the shadow color
  @include cv.register-hsl("shadow", white);
}
```

This mixin outputs a list of CSS variables and their new value.

To use this theme with the `prefer-color-scheme` media query, write the following:

```
@use "sass/utilities/css-variables" as cv;
@use "sass/themes/dark";

@include cv.system-theme($name: "dark") {
  @include dark.dark-theme;
}
```

To use this theme with the `[data-theme=dark]` and `.theme-dark` selectors, write the following:

```
@use "sass/utilities/css-variables" as cv;
@use "sass/themes/dark";
@use "sass/themes/setup";

@include cv.bulma-theme($name: "dark") {
  @include dark.dark-theme;
  @include setup.setup-theme;
}
```

### The `bulma-theme()` mixin

This mixin will allow you to generate a CSS rule-set with both an appropriate HTML attribute selector and a CSS class selector, which names are defined by the `$name` parameter.

```
@use "sass/utilities/css-variables" as cv;

@include cv.bulma-theme($name: "my-theme") {
  // Your code
}
```

This will output the following:

```
[data-theme=my-theme],
.theme-my-theme {
  /* Your code */
}
```

### The `system-theme()` mixin

This mixin will generate a `@media (prefers-color-scheme: $name)` media query.

```
@use "sass/utilities/css-variables" as cv;

@include cv.system-theme($name: "dark") {
  // Your code
}
```

This will output the following:

```
@media (prefers-color-scheme: dark) {
  :root {
    /* Your code */
  }
}
```

### The `register-vars()` function

All Bulma CSS variables are prefixed with `bulma-`. This prefix is defined with the `$cssvars-prefix: "bulma-";` Sass variable.

Because writing all CSS variables with this prefix can be cumbersome, Bulma provides a Sass function to register new variables: `register-vars()`.

This function accepts a Sass map of `name: value` pairs.

```
@use "sass/utilities/css-variables" as cv;

$scheme-main-l: 11%;
$background-l: 14%;
$text-l: 71%;

@include cv.bulma-theme($name: "my-theme") {
  @include cv.register-vars(
    (
      "scheme-brightness": "dark",
      "scheme-main-l": $scheme-main-l,
      "scheme-main-bis-l": $scheme-main-l + 2%,
      "scheme-main-ter-l": $scheme-main-l + 4%,
      "background-l": $background-l,
      "border-weak-l": 21%,
      "border-l": 24%,
      "text-weak-l": 53%,
      "text-l": $text-l,
      "text-strong-l": 93%,
      "text-title-l": 100%,
      "hover-background-l-delta": 5%,
      "active-background-l-delta": 10%,
      "hover-border-l-delta": 10%,
      "active-border-l-delta": 20%,
      "hover-color-l-delta": 5%,
      "active-color-l-delta": 10%,
    )
  );
}
```

### Updating the lightness

For Dark Mode, Bulma will keep the same hue and saturation of the main scheme color. It will however **invert the lightness** of background, borders, text colors, and hover/active states.

| Lightness Name | Light Mode (default) | Dark Mode (default) |
| --- | --- | --- |
| `--bulma-scheme-main-l` | `100%` |  | `11%` |  |
| `--bulma-scheme-main-bis-l` | `98%` |  | `13%` |  |
| `--bulma-scheme-main-ter-l` | `98%` |  | `15%` |  |
| `--bulma-background-l` | `96%` |  | `14%` |  |
| `--bulma-border-weak-l` | `93%` |  | `21%` |  |
| `--bulma-border-l` | `86%` |  | `24%` |  |
| `--bulma-text-weak-l` | `48%` |  | `53%` |  |
| `--bulma-text-l` | `29%` |  | `71%` |  |
| `--bulma-text-strong-l` | `21%` |  | `93%` |  |
| `--bulma-text-title-l` | `14%` |  | `100%` |  |
| `--bulma-hover-background-l-delta` | `5%` | `5%` |
| `--bulma-active-background-l-delta` | `10%` | `10%` |
| `--bulma-hover-border-l-delta` | `10%` | `10%` |
| `--bulma-active-border-l-delta` | `20%` | `20%` |
| `--bulma-hover-color-l-delta` | `5%` | `5%` |
| `--bulma-active-color-l-delta` | `10%` | `10%` |

### The `generate-on-scheme-colors()` function

The **scheme** color is the one used for:

*    backgrounds
*    borders
*   text shades 
    *    strong text
    *    weak text
    *    title text
    *    and normal text

For each of the 7 primary colors , the default Bulma theme generates **on scheme** shades, meaning shades of each color that will look decent on the main scheme color.

In Light Mode, they look like this:

| `link` | var(--bulma-link-on-scheme) |
| --- |
| `primary` | var(--bulma-primary-on-scheme) |
| `info` | var(--bulma-info-on-scheme) |
| `success` | var(--bulma-success-on-scheme) |
| `warning` | var(--bulma-warning-on-scheme) |
| `danger` | var(--bulma-danger-on-scheme) |

Because in Dark Mode we are inverting the lightness of these colors, the page background will go from white  to black . We thus need to update the `-on-scheme` colors of all 7 primary colors.

In Dark Mode, they look like this:

| `link` | var(--bulma-link-on-scheme) |
| --- |
| `primary` | var(--bulma-primary-on-scheme) |
| `info` | var(--bulma-info-on-scheme) |
| `success` | var(--bulma-success-on-scheme) |
| `warning` | var(--bulma-warning-on-scheme) |
| `danger` | var(--bulma-danger-on-scheme) |

If you are creating your own theme, you can automatically generate new `-on-scheme` colors by using the `generate-on-scheme-colors()` for **each** color. It takes 3 parameters:

*   `$name` which is a string. E.g. `"primary"`
*   `$color` which is the color value. E.g.
*   `$scheme-main` which is the theme’s main scheme color (the one used as the page background). E.g. `#fff`

The full code looks like this:

```
@use "sass/utilities/css-variables" as cv;
@use "sass/utilities/derived-variables" as dv;

$scheme-main-l: 11%;
$scheme-main: hsl(iv.$scheme-h, iv.$scheme-s, $scheme-main-l);

@include cv.bulma-theme($name: "my-theme") {
  @each $name, $color in dv.$colors {
    @include cv.generate-on-scheme-colors($name, $color, $scheme-main);
  }
}
```

### The `setup-theme()` function

In Bulma, some CSS variables reference other CSS variables. For example, `--bulma-scheme-main` is defined like this:

```
:root {
  --bulma-scheme-main: hsl(
    var(--bulma-scheme-h)
    var(--bulma-scheme-s)
    var(--bulma-scheme-main-l)
  );
}
```

Because of how CSS variables work, if you update the value of `--bulma-scheme-main-l`, you need to define `--bulma-scheme-main` again. That is what `setup-theme()` does.

```
[data-theme=my-theme],
.theme-my-theme {
  --bulma-scheme-main-l: 7%;
  --bulma-scheme-main: hsl(
    var(--bulma-scheme-h)
    var(--bulma-scheme-s)
    var(--bulma-scheme-main-l)
  );
}
```

If you create your own theme, simply call this function _after_ having set your own CSS variables:

```
@use "sass/themes/setup";

@include cv.bulma-theme($name: "my-theme") {
  // Set your own CSS variables,
  // either manually:
  --bulma-scheme-main-l: 7%;
  // or using Bulma's register-vars() function:
  @include register-vars((
    "bulma-scheme-main-l": 7%,
  ));

  // Then, setup the new theme.
  @include setup.setup-theme();
}
```
