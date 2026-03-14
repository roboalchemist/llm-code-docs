# Source: https://bulma.io/documentation/sass/responsive-mixins/

Title: Bulma Sass Responsive Mixins

URL Source: https://bulma.io/documentation/sass/responsive-mixins/

Markdown Content:
### from() and until() mixins [#](https://bulma.io/documentation/sass/responsive-mixins/#from-and-until-mixins)

Responsiveness in CSS is based on **media queries** (see [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries)).

Bulma provides **2 useful responsive mixins:**

*   `@mixin from($breakpoint)`  to target devices with a screen _wider_ than or equal to the breakpoint 
*   `@mixin until($breakpoint)`  to target devices with a screen _narrower_ than the breakpoint 

Their usage is very simple:

#### from() [#](https://bulma.io/documentation/sass/responsive-mixins/#from)

The `from()` mixin has a single parameter which sets the **screen width** from which the styles it contains will be applied:

Sass source

```
@use "bulma/sass/utilities/mixins";

.my-element {
  background: red;

  @include mixins.from(1280px) {
    background: blue;
  }
}
```

CSS output

```
.my-element {
  background: red;
}

@media screen and (min-width: 1280px) {
  .my-element {
    background: blue;
  }
}
```

For screens with a width of 1279px or less, the element's background will be **red**. 

 For screens 1280px-wide or more, the element's background will be **blue**.

#### until() [#](https://bulma.io/documentation/sass/responsive-mixins/#until)

The `until()` mixin has a single parameter which sets the **screen width (minus `1px`)** until which the styles it contains will be applied.

This means that if you set a value of `1280px`, the styles will be applied on a screen width of `1279px` but **not** on a screen width of `1280px`.

The reason for this **1px offset** is to allow you to use both `from()` and `until()` with the **same breakpoint value**. This leaves **no gap** between the 2 sets of rules.

Sass source

```
@use "bulma/sass/utilities/mixins";

$breakpoint: 1280px;

.my-element {
  @include mixins.until($breakpoint) {
    background: green;
  }

  @include mixins.from($breakpoint) {
    background: orange;
  }
}
```

CSS output

```
@media screen and (max-width: 1279px) {
  .my-element {
    background: green;
  }
}

@media screen and (min-width: 1280px) {
  .my-element {
    background: orange;
  }
}
```

For screens with a width of 1279px or less, the element's background will be **green**. 

 For screens 1280px-wide or more, the element's background will be **orange**.

### Named mixins [#](https://bulma.io/documentation/sass/responsive-mixins/#named-mixins)

By having **4 breakpoints** and supporting **5 screen sizes**, Bulma can support a lot of different setups.

While you could use the mixins

`@include mixins.from()`

and

`@include mixins.until()`

, Bulma provides **quick shortcuts** with **11 named mixins**.

These **responsive mixins** are named after the screen sizes and breakpoints used in Bulma, so that you can use them to create a **responsive designs**:

| Mobile Up to `768px` | Tablet Between `769px` and `1023px` | Desktop Between `1024px` and `1215px` | Widescreen Between `1216px` and `1407px` | FullHD `1408px` and above |
| --- | --- | --- | --- | --- |
| ``` @use "bulma/sass/utilities/mixins"; @include mixins.mobile { // Styles applied // below $tablet } ``` | - |
| - | ``` @use "bulma/sass/utilities/mixins"; @include mixins.tablet { // Styles applied // above $tablet } ``` |
| - | ``` @use "bulma/sass/utilities/mixins"; @include mixins.desktop { // Styles applied // above $desktop } ``` |
| - | ``` @use "bulma/sass/utilities/mixins"; @include mixins.widescreen { // Styles applied // above $widescreen } ``` |
| - | ``` @use "bulma/sass/utilities/mixins"; @include mixins.fullhd { // Styles applied // above $fullhd } ``` |
| - | ``` @use "bulma/sass/utilities/mixins"; @include mixins.tablet-only { // Styles applied // between $tablet // and $desktop } ``` | - |
| - | ``` @use "bulma/sass/utilities/mixins"; @include mixins.desktop-only { // Styles applied // between $desktop // and $widescreen } ``` | - |
| - | ``` @use "bulma/sass/utilities/mixins"; @include mixins.widescreen-only { // Styles applied // between $widescreen // and $fullhd } ``` | - |
| ``` @use "bulma/sass/utilities/mixins"; @include mixins.touch { // Styles applied // below $desktop } ``` | - |
| ``` @use "bulma/sass/utilities/mixins"; @include mixins.until-widescreen { // Styles applied // below $widescreen } ``` | - |
| ``` @use "bulma/sass/utilities/mixins"; @include mixins.until { // Styles applied // below $fullhd } ``` | - |
