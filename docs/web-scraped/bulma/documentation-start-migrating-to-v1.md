# Source: https://bulma.io/documentation/start/migrating-to-v1/

Title: Migrating to Bulma v1

URL Source: https://bulma.io/documentation/start/migrating-to-v1/

Markdown Content:
Bulma v1 is basically a **full rewrite** of the framework using [**Dart Sass**](https://sass-lang.com/dart-sass/), which is the primary implementation of Sass. While this affects a few development details, everything has been done to make the transition **as easy as possible**.

### What remains the same [#](https://bulma.io/documentation/start/migrating-to-v1/#what-remains-the-same)

**All HTML snippets are the same**. This means you don’t need to update your markup. **This is important** because it means, if you’re using Bulma straight “out of the box”, you don’t need to change anything.

You can just swap `bulma@0.9.4/css/bulma.min.css` with `bulma@1.0.0/css/bulma.min.css` and everything will work. Things will look slightly different, but they will still work.

### What changes [#](https://bulma.io/documentation/start/migrating-to-v1/#what-changes)

*   [**Dart Sass**](https://sass-lang.com/dart-sass/) is used to build Bulma 
    *   if you use the `sass` npm package, you’re already using Dart Sass

*   [**CSS Variables**](https://bulma.io/documentation/features/css-variables/) are used instead of literals: `color: var(--bulma-primary);` instead of `color: hsl(171deg, 100%, 41%);`, which means you can customize Bulma with CSS only (without using Sass)
*   Customization by setting your own value for Sass variables works differently. See [how to customize Bulma with Sass](https://bulma.io/documentation/customize/with-sass/).

### What's new (i.e. did not exist before) [#](https://bulma.io/documentation/start/migrating-to-v1/#what-s-new-i-e-did-not-exist-before)

*   The notion of [**Themes**](https://bulma.io/documentation/features/themes/) is introduced: a theme is a collection of CSS variables within a context, and is the best approach to customize Bulma
*   As a result, a Theme for [**Dark Mode**](https://bulma.io/documentation/features/dark-mode/) is included
*   [**Color Palettes**](https://bulma.io/documentation/features/color-palettes/) are created for each of the 7 primary colors
*   [**Skeleton loaders**](https://bulma.io/documentation/features/skeletons/) exist as standalone components but also as variants of other components
*   You can add a **prefix** to all your Bulma classes so that `.button` becomes `.my-prefix-button`
    *   a pre-built prefixed version exists as one of the [**alternative versions**](https://bulma.io/documentation/start/alternative-versions/)

### Breaking Changes [#](https://bulma.io/documentation/start/migrating-to-v1/#breaking-changes)

| ⛔️ Deprecated | ✅ How to fix |
| --- | --- |
| **Tiles** are deprecated ``` <!-- Before --> <div class="tile is-ancestor"> <div class="tile is-parent"> <article class="tile is-child box"> <p class="title">Hello World</p> <p class="subtitle">What is up?</p> </article> </div> <div class="tile is-parent"> <article class="tile is-child box"> <p class="title">Foo</p> <p class="subtitle">Bar</p> </article> </div> </div> ``` | Use the new and improved [Smart Grid](https://bulma.io/documentation/grid/smart-grid/) ``` <!-- After --> <div class="grid"> <div class="cell"> <article class="box"> <p class="title">Hello World</p> <p class="subtitle">What is up?</p> </article> </div> <div class="cell"> <article class="box"> <p class="title">Foo</p> <p class="subtitle">Bar</p> </article> </div> </div> ``` |
| `@import` is not recommended ``` // Before $purple: #8A4D76; $pink: #FA7C91; $brown: #757763; $beige-light: #D0D1CD; $beige-lighter: #EFF0EB; // Update Bulma's global variables $family-sans-serif: "Nunito", sans-serif; $grey-dark: $brown; $grey-light: $beige-light; $primary: $purple; $link: $pink; // Update some of Bulma's component variables $control-border-width: 2px; $input-background-color: $beige-lighter; $input-border-color: transparent; $input-shadow: none; // Import the rest of Bulma @import "../path/to/bulma"; ``` | Use Dart Sass's new [`@use` and `@forward` keywords](https://sass-lang.com/documentation/at-rules/use/) ``` // After $purple: #8a4d76; $pink: #fa7c91; $brown: #757763; $beige-light: #d0d1cd; $beige-lighter: #eff0eb; // Path to Bulma's sass folder @use "path/to/bulma/sass" with ( $family-primary: '"Nunito", sans-serif', $grey-dark: $brown, $grey-light: $beige-light, $primary: $purple, $link: $pink, $control-border-width: 2px, $input-h: color.hue($beige-lighter), $input-s: color.saturation($beige-lighter), $input-background-l: color.lightness($beige-lighter), $input-border-l: color.lightness($beige-lighter), $input-shadow: none ); ``` |
