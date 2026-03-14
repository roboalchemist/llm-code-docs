# Source: https://bulma.io/documentation/features/color-palettes/

Title: Color Palettes in Bulma

URL Source: https://bulma.io/documentation/features/color-palettes/

Markdown Content:
Bulma comes with 7 primary colors:

`text`
`link`
`primary`
`info`
`success`
`warning`
`danger`

Bulma will automatically **generate a collection of CSS variables** for each of those colors. These sets of variables act as a **color palette** you can use to play with different _shades_ of a same color.

For example, by setting the primary color with `$primary: hsl(171, 100%, 41%)`, Bulma will generate the following CSS variables:

*   `--bulma-primary`
*   `--bulma-primary-rgb` if you want to create your own RGBA shade: `rgba(var(--bulma-primary-rgb), 0.5)`
*   `--bulma-primary-h` equal to the primary **hue**
*   `--bulma-primary-s` equal to the primary **saturation**
*   `--bulma-primary-l` equal to the primary **lightness**
*   `--bulma-primary-base` (equal to `--bulma-primary`)
*   `--bulma-primary-invert` which is a color that will look decent on the primary color (in a foreground/background combination)
*   `--bulma-primary-light` which is the primary color at `90%` lightness
*   `--bulma-primary-light-invert` which is a color that looks good on the `-light` version
*   `--bulma-primary-dark` which is the primary color at `20%` lightness
*   `--bulma-primary-dark-invert` which is a color that looks good on the `-dark` version
*   `--bulma-primary-soft` which is a `light` color in light mode, and a `dark` color in dark mode
*   `--bulma-primary-bold` which is a `dark` color in light mode, and a `light` color in dark mode
*   `--bulma-primary-soft-invert` which is the same as the `bold` version
*   `--bulma-primary-bold-invert` which is the same as the `soft` version
*   `--bulma-primary-on-scheme` which is a color that looks good on the `scheme-main` color (which by default is white, and is used as the page’s background color)

Here is what they look like:

`--bulma-primary`The quick brown fox jumps over the lazy dog
`--bulma-primary-invert`The quick brown fox jumps over the lazy dog
`--bulma-primary-light`The quick brown fox jumps over the lazy dog
`--bulma-primary-light-invert`The quick brown fox jumps over the lazy dog
`--bulma-primary-dark`The quick brown fox jumps over the lazy dog
`--bulma-primary-dark-invert`The quick brown fox jumps over the lazy dog
`--bulma-primary-soft`The quick brown fox jumps over the lazy dog
`--bulma-primary-bold`The quick brown fox jumps over the lazy dog
`--bulma-primary-on-scheme`The quick brown fox jumps over the lazy dog

Soft and Bold colors
--------------------

Because Bulma now has a Dark Mode, it comes with a new color concept: **soft** and **bold** colors.

A **soft** color is a shade of a color that has little contrast with the background. It’s a muted, faint shade of that color.

In light mode, this means that a soft color will be light as well. It’s ideal of **backgrounds**:

`--bulma-primary-soft` as **background**The quick brown fox jumps over the lazy dog

On the other hand, the **bold** color has a stark contrast with the background. It’s a strong, distinct shade of that color.

In light mode, this means that a bold color will be dark. It’s ideal of **text colors**:

`--bulma-primary-bold` as **text color**The quick brown fox jumps over the lazy dog

The best use of these colors is to **combine them**: the soft color as background, the bold color as foreground:

`--bulma-primary-soft` as **background**

`--bulma-primary-bold` as **foreground**The quick brown fox jumps over the lazy dog

### Automatic switching when going into Dark Mode

If you use switch to between light mode and dark mode, you will notice that the soft and bold colors will **swap**. That way, you don’t need to update your CSS classes to keep a decent design.

| System | Light Mode | Dark Mode |
| --- | --- | --- |
| The quick brown fox jumps over the lazy dog | The quick brown fox jumps over the lazy dog | The quick brown fox jumps over the lazy dog |

Invert colors
-------------

The purpose of `-invert` colors is to combine them with their base counterparts. For example, if you use `primary-light` as the background color, you can use `primary-light-invert` as the foreground color:

**Background**`--bulma-primary`bulma-primary-invert **on** bulma-primary
**Foreground**`--bulma-primary-invert`
**Background**`--bulma-primary-light`bulma-primary-light-invert **on** bulma-primary-light
**Foreground**`--bulma-primary-light-invert`
**Background**`--bulma-primary-dark`bulma-primary-dark-invert **on** bulma-primary-dark
**Foreground**`--bulma-primary-dark-invert`

21 shades for each color
------------------------

Bulma will automatically generate 21 shades of each color, one for each amount of **lightness**, starting from _around_`0%` and going up in `5%` increments, until `100%` is reached.

> I am saying _around_`0%` because the last digit is determined by the base color. If the base color’s lightness is `42%`, then `--bulma-primary-00` will be `2%`, not `0%`.

`--bulma-primary-00``--bulma-primary-00-invert`
`--bulma-primary-05``--bulma-primary-05-invert`
`--bulma-primary-10``--bulma-primary-10-invert`
`--bulma-primary-15``--bulma-primary-15-invert`
`--bulma-primary-20``--bulma-primary-20-invert`
`--bulma-primary-25``--bulma-primary-25-invert`
`--bulma-primary-30``--bulma-primary-30-invert`
`--bulma-primary-35``--bulma-primary-35-invert`
`--bulma-primary-40``--bulma-primary-40-invert`
`--bulma-primary-45``--bulma-primary-45-invert`
`--bulma-primary-50``--bulma-primary-50-invert`
`--bulma-primary-55``--bulma-primary-55-invert`
`--bulma-primary-60``--bulma-primary-60-invert`
`--bulma-primary-65``--bulma-primary-65-invert`
`--bulma-primary-70``--bulma-primary-70-invert`
`--bulma-primary-75``--bulma-primary-75-invert`
`--bulma-primary-80``--bulma-primary-80-invert`
`--bulma-primary-85``--bulma-primary-85-invert`
`--bulma-primary-90``--bulma-primary-90-invert`
`--bulma-primary-95``--bulma-primary-95-invert`
`--bulma-primary-100``--bulma-primary-100-invert`

Each of these shades has an `-invert` counterpart that can be used as a foreground color:

**Background**`--bulma-primary-00`bulma-primary-00-invert **on** bulma-primary-00
**Foreground**`--bulma-primary-00-invert`
**Background**`--bulma-primary-05`bulma-primary-05-invert **on** bulma-primary-05
**Foreground**`--bulma-primary-05-invert`
**Background**`--bulma-primary-10`bulma-primary-10-invert **on** bulma-primary-10
**Foreground**`--bulma-primary-10-invert`
**Background**`--bulma-primary-15`bulma-primary-15-invert **on** bulma-primary-15
**Foreground**`--bulma-primary-15-invert`
**Background**`--bulma-primary-20`bulma-primary-20-invert **on** bulma-primary-20
**Foreground**`--bulma-primary-20-invert`
**Background**`--bulma-primary-25`bulma-primary-25-invert **on** bulma-primary-25
**Foreground**`--bulma-primary-25-invert`
**Background**`--bulma-primary-30`bulma-primary-30-invert **on** bulma-primary-30
**Foreground**`--bulma-primary-30-invert`
**Background**`--bulma-primary-35`bulma-primary-35-invert **on** bulma-primary-35
**Foreground**`--bulma-primary-35-invert`
**Background**`--bulma-primary-40`bulma-primary-40-invert **on** bulma-primary-40
**Foreground**`--bulma-primary-40-invert`
**Background**`--bulma-primary-45`bulma-primary-45-invert **on** bulma-primary-45
**Foreground**`--bulma-primary-45-invert`
**Background**`--bulma-primary-50`bulma-primary-50-invert **on** bulma-primary-50
**Foreground**`--bulma-primary-50-invert`
**Background**`--bulma-primary-55`bulma-primary-55-invert **on** bulma-primary-55
**Foreground**`--bulma-primary-55-invert`
**Background**`--bulma-primary-60`bulma-primary-60-invert **on** bulma-primary-60
**Foreground**`--bulma-primary-60-invert`
**Background**`--bulma-primary-65`bulma-primary-65-invert **on** bulma-primary-65
**Foreground**`--bulma-primary-65-invert`
**Background**`--bulma-primary-70`bulma-primary-70-invert **on** bulma-primary-70
**Foreground**`--bulma-primary-70-invert`
**Background**`--bulma-primary-75`bulma-primary-75-invert **on** bulma-primary-75
**Foreground**`--bulma-primary-75-invert`
**Background**`--bulma-primary-80`bulma-primary-80-invert **on** bulma-primary-80
**Foreground**`--bulma-primary-80-invert`
**Background**`--bulma-primary-85`bulma-primary-85-invert **on** bulma-primary-85
**Foreground**`--bulma-primary-85-invert`
**Background**`--bulma-primary-90`bulma-primary-90-invert **on** bulma-primary-90
**Foreground**`--bulma-primary-90-invert`
**Background**`--bulma-primary-95`bulma-primary-95-invert **on** bulma-primary-95
**Foreground**`--bulma-primary-95-invert`
**Background**`--bulma-primary-100`bulma-primary-100-invert **on** bulma-primary-100
**Foreground**`--bulma-primary-100-invert`

### Lightness CSS variables

If you write your own CSS and want to use one these shades yourself, you can access the **lightness** value via its dedicated CSS variable that has a `-l` suffix.

For example, the `bulma-primary-75` color is defined like this:

```
:root {
  --bulma-primary-75: hsla(
    var(--bulma-primary-h),
    var(--bulma-primary-s),
    var(--bulma-primary-75-l),
    1
  );
}
```

In this case, `--bulma-primary-75-l` is equal to `76%`, and you can access its value with the `var(--bulma-primary-75-l)` CSS variable.

CSS helper classes
------------------

While you can access all a color’s CSS variables directly by writing `color: var(--bulma-primary)` for example, Bulma also provides **CSS helper classes** for each color.

Those helper classes exist for to set either the `color` or the `background`.

| # | Color | `color` class | `background` class |
| --- | --- | --- | --- |
|  | `--bulma-primary` | `has-text-primary` | Hello World | `has-background-primary` | Hello World |
| ``` <span class="has-text-primary">Color</span> <span class="has-background-primary">Background</span> ``` |
|  | `--bulma-primary-invert` | `has-text-primary-invert` | Hello World | `has-background-primary-invert` | Hello World |
| ``` <span class="has-text-primary-invert">Color</span> <span class="has-background-primary-invert">Background</span> ``` |
|  | `--bulma-primary-light` | `has-text-primary-light` | Hello World | `has-background-primary-light` | Hello World |
| ``` <span class="has-text-primary-light">Color</span> <span class="has-background-primary-light">Background</span> ``` |
|  | `--bulma-primary-light-invert` | `has-text-primary-light-invert` | Hello World | `has-background-primary-light-invert` | Hello World |
| ``` <span class="has-text-primary-light-invert">Color</span> <span class="has-background-primary-light-invert">Background</span> ``` |
|  | `--bulma-primary-dark` | `has-text-primary-dark` | Hello World | `has-background-primary-dark` | Hello World |
| ``` <span class="has-text-primary-dark">Color</span> <span class="has-background-primary-dark">Background</span> ``` |
|  | `--bulma-primary-dark-invert` | `has-text-primary-dark-invert` | Hello World | `has-background-primary-dark-invert` | Hello World |
| ``` <span class="has-text-primary-dark-invert">Color</span> <span class="has-background-primary-dark-invert">Background</span> ``` |
|  | `--bulma-primary-on-scheme` | `has-text-primary-on-scheme` | Hello World | `has-background-primary-on-scheme` | Hello World |
| ``` <span class="has-text-primary-on-scheme">Color</span> <span class="has-background-primary-on-scheme">Background</span> ``` |
|  | `--bulma-primary-00` | `has-text-primary-00` | Hello World | `has-background-primary-00` | Hello World |
| ``` <span class="has-text-primary-00">Color</span> <span class="has-background-primary-00">Background</span> ``` |
|  | `--bulma-primary-05` | `has-text-primary-05` | Hello World | `has-background-primary-05` | Hello World |
| ``` <span class="has-text-primary-05">Color</span> <span class="has-background-primary-05">Background</span> ``` |
|  | `--bulma-primary-10` | `has-text-primary-10` | Hello World | `has-background-primary-10` | Hello World |
| ``` <span class="has-text-primary-10">Color</span> <span class="has-background-primary-10">Background</span> ``` |
|  | `--bulma-primary-15` | `has-text-primary-15` | Hello World | `has-background-primary-15` | Hello World |
| ``` <span class="has-text-primary-15">Color</span> <span class="has-background-primary-15">Background</span> ``` |
|  | `--bulma-primary-20` | `has-text-primary-20` | Hello World | `has-background-primary-20` | Hello World |
| ``` <span class="has-text-primary-20">Color</span> <span class="has-background-primary-20">Background</span> ``` |
|  | `--bulma-primary-25` | `has-text-primary-25` | Hello World | `has-background-primary-25` | Hello World |
| ``` <span class="has-text-primary-25">Color</span> <span class="has-background-primary-25">Background</span> ``` |
|  | `--bulma-primary-30` | `has-text-primary-30` | Hello World | `has-background-primary-30` | Hello World |
| ``` <span class="has-text-primary-30">Color</span> <span class="has-background-primary-30">Background</span> ``` |
|  | `--bulma-primary-35` | `has-text-primary-35` | Hello World | `has-background-primary-35` | Hello World |
| ``` <span class="has-text-primary-35">Color</span> <span class="has-background-primary-35">Background</span> ``` |
|  | `--bulma-primary-40` | `has-text-primary-40` | Hello World | `has-background-primary-40` | Hello World |
| ``` <span class="has-text-primary-40">Color</span> <span class="has-background-primary-40">Background</span> ``` |
|  | `--bulma-primary-45` | `has-text-primary-45` | Hello World | `has-background-primary-45` | Hello World |
| ``` <span class="has-text-primary-45">Color</span> <span class="has-background-primary-45">Background</span> ``` |
|  | `--bulma-primary-50` | `has-text-primary-50` | Hello World | `has-background-primary-50` | Hello World |
| ``` <span class="has-text-primary-50">Color</span> <span class="has-background-primary-50">Background</span> ``` |
|  | `--bulma-primary-55` | `has-text-primary-55` | Hello World | `has-background-primary-55` | Hello World |
| ``` <span class="has-text-primary-55">Color</span> <span class="has-background-primary-55">Background</span> ``` |
|  | `--bulma-primary-60` | `has-text-primary-60` | Hello World | `has-background-primary-60` | Hello World |
| ``` <span class="has-text-primary-60">Color</span> <span class="has-background-primary-60">Background</span> ``` |
|  | `--bulma-primary-65` | `has-text-primary-65` | Hello World | `has-background-primary-65` | Hello World |
| ``` <span class="has-text-primary-65">Color</span> <span class="has-background-primary-65">Background</span> ``` |
|  | `--bulma-primary-70` | `has-text-primary-70` | Hello World | `has-background-primary-70` | Hello World |
| ``` <span class="has-text-primary-70">Color</span> <span class="has-background-primary-70">Background</span> ``` |
|  | `--bulma-primary-75` | `has-text-primary-75` | Hello World | `has-background-primary-75` | Hello World |
| ``` <span class="has-text-primary-75">Color</span> <span class="has-background-primary-75">Background</span> ``` |
|  | `--bulma-primary-80` | `has-text-primary-80` | Hello World | `has-background-primary-80` | Hello World |
| ``` <span class="has-text-primary-80">Color</span> <span class="has-background-primary-80">Background</span> ``` |
|  | `--bulma-primary-85` | `has-text-primary-85` | Hello World | `has-background-primary-85` | Hello World |
| ``` <span class="has-text-primary-85">Color</span> <span class="has-background-primary-85">Background</span> ``` |
|  | `--bulma-primary-90` | `has-text-primary-90` | Hello World | `has-background-primary-90` | Hello World |
| ``` <span class="has-text-primary-90">Color</span> <span class="has-background-primary-90">Background</span> ``` |
|  | `--bulma-primary-95` | `has-text-primary-95` | Hello World | `has-background-primary-95` | Hello World |
| ``` <span class="has-text-primary-95">Color</span> <span class="has-background-primary-95">Background</span> ``` |
|  | `--bulma-primary-100` | `has-text-primary-100` | Hello World | `has-background-primary-100` | Hello World |
| ``` <span class="has-text-primary-100">Color</span> <span class="has-background-primary-100">Background</span> ``` |
