# Source: https://bulma.io/documentation/sass/mixins/

Title: Bulma Sass Mixins

URL Source: https://bulma.io/documentation/sass/mixins/

Markdown Content:
Throughout the codebase, Bulma uses Sass mixins to **enhance** and facilitate the CSS output. While these mixins are mainly used within the context of Bulma, they are of course available for you to **re-use** in your own projects.

### Element Mixins [#](https://bulma.io/documentation/sass/mixins/#element-mixins)

These mixins create a **visual** HTML element.

#### Arrow [#](https://bulma.io/documentation/sass/mixins/#arrow)

The `arrow()` mixin creates a down-facing arrow. The `$color` parameter defines the color of the arrow.

```
.bulma-arrow-mixin {
  @include mixins.arrow(purple);
}
```

Example

HTML

`<span class="bulma-arrow-mixin"></span>`

#### Burger [#](https://bulma.io/documentation/sass/mixins/#burger)

The `burger()` mixin creates a 16x16px set of **3 horizontal bars** grouped within square. The dimensions of this square are defined by the `$dimensions` parameter.

```
.bulma-burger-mixin {
  @include mixins.burger(2.5rem);
}
```

Example

HTML

```
<button class="bulma-burger-mixin">
  <span></span>
  <span></span>
  <span></span>
  <span></span>
</button>
```

#### Delete [#](https://bulma.io/documentation/sass/mixins/#delete)

The `delete()` mixin creates a 20x20px circle containing a **cross**. It comes with 3 modifiers: `is-small`, `is-medium` and `is-large`.

```
.bulma-delete-mixin {
  @include mixins.delete;
}
```

Example

HTML

```
<button class="bulma-delete-mixin is-small"></button>
<button class="bulma-delete-mixin"></button>
<button class="bulma-delete-mixin is-medium"></button>
<button class="bulma-delete-mixin is-large"></button>
```

#### Loader [#](https://bulma.io/documentation/sass/mixins/#loader)

The `loader()` mixin creates a 1em **spinning circle**.

```
.bulma-loader-mixin {
  @include mixins.loader;
}
```

Example

HTML

`<span class="bulma-loader-mixin"></span>`

#### Font Awesome container [#](https://bulma.io/documentation/sass/mixins/#font-awesome-container)

The `fa()` mixin creates a **square inline-block element**, ideal for containing a Font Awesome icon, or any other type of icon font. 

 The first `$size` parameter defines the icon font size. 

 The second `$dimensions` parameter defines the dimensions of the square container.

```
.bulma-fa-mixin {
  @include mixins.fa(1rem, 2rem);
  background-color: lavender; // For demo purposes
}
```

Example

HTML

```
<span class="bulma-fa-mixin">
  <i class="fas fa-thumbs-up"></i>
</span>
```

### CSS Mixins [#](https://bulma.io/documentation/sass/mixins/#css-mixins)

These mixins add **CSS rules** to the element.

#### Block [#](https://bulma.io/documentation/sass/mixins/#block)

The `block()` mixin adds **spacing** below an element, but only if it's **not the last child**. 

 The `$spacing` parameter defines the value of the `margin-bottom`.

```
.bulma-block-mixin {
  @include mixins.block(1rem);
}
```

Example

This element has a margin-bottom.

This element too.

Not this one because it's the last child.

HTML

```
<p class="bulma-block-mixin">This element has a margin-bottom.</p>
<p class="bulma-block-mixin">This element too.</p>
<p class="bulma-block-mixin">Not this one because it's the last child.</p>
```

#### Overlay [#](https://bulma.io/documentation/sass/mixins/#overlay)

The `overlay()` mixin makes the element **cover** its closest positioned ancestor. 

 The `$offset` parameter defines how far inside the element is positioned from each edge (top, bottom, left and right).

```
.bulma-overlay-mixin {
  @include mixins.overlay(1.5rem);
  background-color: darkorange;
  border-radius: 0.25em;
  color: white;
  opacity: 0.9;
  padding: 1em;
}
```

Example

Overlay element

HTML

```
<div class="bulma-overlay-mixin-parent">
  <div class="bulma-overlay-mixin">Overlay element</div>
</div>
```

#### Center [#](https://bulma.io/documentation/sass/mixins/#center)

The `center()` mixin allows you to absolutely position an element with **fixed dimensions** at the **center** of its closest positioned ancestor. 

 The value of the `$width` parameter should be the width of the element the mixin is applied on. 

 Unless the element has square dimensions, the second parameter `$height` is required and its value should be the height of the element the mixin is applied on.

```
.bulma-center-mixin {
  @include mixins.center;
}
```

Example

![Image 1](https://bulma.io/assets/images/unsplash/mEZ3PoFGs_k.jpg)

HTML

```
<div class="bulma-center-mixin-parent">
  <img class="bulma-center-mixin" height="96" width="96" src="/assets/images/unsplash/mEZ3PoFGs_k.jpg">
</div>
```

#### Placeholder [#](https://bulma.io/documentation/sass/mixins/#placeholder)

The `placeholder()` mixin allows you to change the style of an **input's placeholder**. 

 The `$offset` parameter defines how far inside the element is positioned from each edge (top, bottom, left and right).

```
.bulma-placeholder-mixin {
  @include mixins.placeholder {
    color: lightblue;
  }
}
```

Example

HTML

```
<input
  class="input bulma-placeholder-mixin"
  type="text"
  placeholder="I am a styled placeholder"
>
```

#### Clearfix [#](https://bulma.io/documentation/sass/mixins/#clearfix)

The `clearfix()` mixin adds a `::after` pseudo-element with a `clear: both` rule.

```
.bulma-clearfix-mixin {
  @include mixins.clearfix;
}
```

Example

![Image 2](https://bulma.io/assets/images/unsplash/La2kOu2dmH4.jpg)

This is a short image description.

This text is following the clearfix element and is correctly placed after.

HTML

```
<div class="bulma-clearfix-mixin">
  <img height="80" width="80" style="float: left;" src="/assets/images/unsplash/La2kOu2dmH4.jpg">
  <p>This is a short image description.</p>
</div>

<p>This text is following the clearfix element and is correctly placed after.</p>
```

#### Reset [#](https://bulma.io/documentation/sass/mixins/#reset)

The `reset()` mixin applies a soft style reset. This is especially useful for `<button>` elements.

```
.bulma-reset-mixin {
  @include mixins.reset;
}
```

Example

HTML

```
<button>Default button</button>
<button class="bulma-reset-mixin">Reset button</button>
```

#### Unselectable [#](https://bulma.io/documentation/sass/mixins/#unselectable)

The `unselectable()` mixin makes an element not selectable. This is to prevent the text to be selected when double-clicked.

```
.bulma-unselectable-mixin {
  @include mixins.unselectable;
}
```

Example

This text is selectable.

This text is not selectable.

HTML

```
<p>This text is selectable.</p>
<p class="bulma-unselectable-mixin">This text is not selectable.</p>
```

#### Overflow Touch [#](https://bulma.io/documentation/sass/mixins/#overflow-touch)

The `overflow-touch()` mixin add the `-webkit-overflow-scrolling: touch;` rule to the element.

### Direction Mixins [#](https://bulma.io/documentation/sass/mixins/#direction-mixins)

#### Left-to-right and Right-to-left Mixins [#](https://bulma.io/documentation/sass/mixins/#left-to-right-and-right-to-left-mixins)

Bulma has a global `$rtl` flag, which allows the framework to output a Right-to-left version of the CSS. By default, this flag's value is set to `false`. This means the framework output a Left-to-right version.

The mixins `@mixin ltr` and `@mixin rtl` are here to output CSS rules based on the value of `$rtl`:

*    if `$rtl: true`, `@include mixins.ltr` outputs nothing 
*    if `$rtl: false`, `@include mixins.rtl` outputs nothing 

This is useful for properties that are specific to the side of an element.

```
.bulma-ltr-rtl-mixin {
  background-color: lightgreen;
  padding: 0.5em 1em;
  border: 1px solid seagreen;
  margin-right: -1px;

  &:first-child {
    @include mixins.ltr {
      border-bottom-left-radius: 0.5em;
      border-top-left-radius: 0.5em;
    }

    @include mixins.rtl {
      border-bottom-right-radius: 0.5em;
      border-top-right-radius: 0.5em;
    }
  }

  &:last-child {
    @include mixins.ltr {
      border-bottom-right-radius: 0.5em;
      border-top-right-radius: 0.5em;
    }

    @include mixins.rtl {
      border-bottom-left-radius: 0.5em;
      border-top-left-radius: 0.5em;
    }
  }
}
```

Example

One Two Three

HTML

```
<div style="display: flex;">
  <span class="bulma-ltr-rtl-mixin">One</span>
  <span class="bulma-ltr-rtl-mixin">Two</span>
  <span class="bulma-ltr-rtl-mixin">Three</span>
</div>
```

#### LTR Position [#](https://bulma.io/documentation/sass/mixins/#ltr-position)

The `ltr-position()` mixin is a quick way to switch between `left` and `right` CSS properties when dealing with positioned elements. 

 The first `$spacing` parameter defines the value of the offset, whether it's right or left. 

 The second `$right` parameter defines if the property outputs `right` (default) or `left`.

Here is what the output looks like with a `$spacing` parameter set to `1rem`:

| Flag → | `$rtl: false;` | `$rtl: true;` |
| --- | --- | --- |
| `@include mixins.ltr-position(1rem, true)` | `right: 1rem` | `left: 1rem` |
| `@include mixins.ltr-position(1rem, false)` | `left: 1rem` | `right: 1rem` |

Sass source

```
.bulma-ltr-position-mixin {
  @include mixins.ltr-position(1rem, false);
  border-radius: 0.25em;
  position: absolute;
  top: 1rem;
}
```

CSS output

```
.bulma-ltr-position-mixin {
  left: 1rem;
  border-radius: 0.25em;
  position: absolute;
  top: 1rem;
}
```

Example

![Image 3](https://bulma.io/assets/images/unsplash/iFgRcqHznqg.jpg)

Cras mattis consectetur purus sit amet fermentum. Nulla vitae elit libero, a pharetra augue. Aenean lacinia bibendum nulla sed consectetur. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Curabitur blandit tempus porttitor. Maecenas faucibus mollis interdum.

HTML

```
<div class="bulma-ltr-position-mixin-parent">
  <img class="bulma-ltr-position-mixin" height="48" width="48" src="/assets/images/unsplash/iFgRcqHznqg.jpg">
  <p>Cras mattis consectetur purus sit amet fermentum. Nulla vitae elit libero, a pharetra augue. Aenean lacinia bibendum nulla sed consectetur. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Curabitur blandit tempus porttitor. Maecenas faucibus mollis interdum.</p>
</div>
```

#### LTR Property [#](https://bulma.io/documentation/sass/mixins/#ltr-property)

The `ltr-property()` mixin works like the `ltr-position()` mixin but allows you to choose **which CSS property** to set. The mixin will append `-right` or `-left` to that property. This is especially useful for `margin` and `padding`. 

 The first `$property` parameter which property you want to "flip" left and right. 

 The second `$spacing` parameter defines the value of the offset, whether it's right or left. 

 The third `$right` parameter defines if the property outputs `right` (default) or `left`.

Here is what the output looks like with a `$spacing` parameter set to `1rem`:

| Flag → | `$rtl: false;` | `$rtl: true;` |
| --- | --- | --- |
| `@include mixins.ltr-property("margin", 1rem, true)` | `margin-right: 1rem` | `margin-left: 1rem` |
| `@include mixins.ltr-property("margin", 1rem, false)` | `margin-left: 1rem` | `margin-right: 1rem` |

Sass source

```
.bulma-ltr-property-mixin {
  @include mixins.ltr-property("margin", 1rem, false);
  border-radius: 0.25em;
}
```

CSS output

```
.bulma-ltr-property-mixin {
  margin-left: 1rem;
  border-radius: 0.25em;
}
```

Example

Cras mattis consectetur purus sit amet fermentum. Nulla vitae elit libero, a pharetra augue. Aenean lacinia bibendum nulla sed consectetur. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Curabitur blandit tempus porttitor. Maecenas faucibus mollis interdum.

![Image 4](https://bulma.io/assets/images/unsplash/jTSf1xnsoCs.jpg)

HTML

```
<div class="bulma-ltr-property-mixin-parent">
  <p>Cras mattis consectetur purus sit amet fermentum. Nulla vitae elit libero, a pharetra augue. Aenean lacinia bibendum nulla sed consectetur. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Curabitur blandit tempus porttitor. Maecenas faucibus mollis interdum.</p>
  <img class="bulma-ltr-property-mixin" height="96" width="96" src="/assets/images/unsplash/jTSf1xnsoCs.jpg">
</div>
```
