# Source: https://devdocs.io/sass/modules

Title: Built-In Modules — DevDocs

URL Source: https://devdocs.io/sass/modules

Markdown Content:
Compatibility:

Dart Sass since 1.23.0

LibSass✗

Ruby Sass✗

Only Dart Sass currently supports loading built-in modules with `@use`. Users of other implementations must call functions using their global names instead.

Sass provides many built-in modules which contain useful functions (and the occasional mixin). These modules can be loaded with the [`@use` rule](https://devdocs.io/sass/at-rules/use) like any user-defined stylesheet, and their functions can be called [like any other module member](https://devdocs.io/sass/at-rules/use#loading-members). All built-in module URLs begin with `sass:` to indicate that they’re part of Sass itself.

Before the Sass module system was introduced, all Sass functions were globally available at all times. Many functions still have global aliases (these are listed in their documentation). The Sass team discourages their use and will eventually deprecate them, but for now they remain available for compatibility with older Sass versions and with LibSass (which doesn’t support the module system yet).

[A few functions](https://devdocs.io/sass/modules#global-functions) are _only_ available globally even in the new module system because they add extra behavior on top of built-in CSS functions.

@use "sass:color";

.button {
  $primary-color: #6b717f;
  color: $primary-color;
  border: 1px solid color.scale($primary-color, $lightness: 20%);
}

// SASS
@use "sass:color"

.button
  $primary-color: #6b717f
  color: $primary-color
  border: 1px solid color.scale($primary-color, $lightness: 20%)

.button {
  color: #6b717f;
  border: 1px solid rgb(135.1641025641, 140.8256410256, 154.0358974359);
}

Sass provides the following built-in modules:

*   The [`sass:math` module](https://devdocs.io/sass/modules/math) provides functions that operate on [numbers](https://devdocs.io/sass/values/numbers).

*   The [`sass:string` module](https://devdocs.io/sass/modules/string) makes it easy to combine, search, or split apart [strings](https://devdocs.io/sass/values/strings).

*   The [`sass:color` module](https://devdocs.io/sass/modules/color) generates new [colors](https://devdocs.io/sass/values/colors) based on existing ones, making it easy to build color themes.

*   The [`sass:list` module](https://devdocs.io/sass/modules/list) lets you access and modify values in [lists](https://devdocs.io/sass/values/lists).

*   The [`sass:map` module](https://devdocs.io/sass/modules/map) makes it possible to look up the value associated with a key in a [map](https://devdocs.io/sass/values/maps), and much more.

*   The [`sass:selector` module](https://devdocs.io/sass/modules/selector) provides access to Sass’s powerful selector engine.

*   The [`sass:meta` module](https://devdocs.io/sass/modules/meta) exposes the details of Sass’s inner workings.

Global Functions
----------------

### 💡 Fun fact:

You can pass [special functions](https://devdocs.io/sass/syntax/special-functions) like `calc()` or `var()` in place of any argument to a global color constructor. You can even use `var()` in place of multiple arguments, since it might be replaced by multiple values! When a color function is called this way, it returns an unquoted string using the same signature it was called with.

@debug rgb(0 51 102 / var(--opacity)); 
@debug color(display-p3 var(--peach)); 

// SASS
@debug rgb(0 51 102 / var(--opacity))  // rgb(0 51 102 / var(--opacity))
@debug color(display-p3 var(--peach))  // color(display-p3 var(--peach))

color($space $channel1 $channel2 $channel3)
color($space $channel1 $channel2 $channel3 / $alpha) 
Compatibility:

Dart Sass since 1.78.0

LibSass✗

Ruby Sass✗

Returns a color in the given color space with the given channel values.

This supports the color spaces `srgb`, `srgb-linear`, `display-p3`, `a98-rgb`, `prophoto-rgb`, `rec2020`, `xyz`, and `xyz-d50`, as well as `xyz-d65` which is an alias for `xyz`. For all spaces, the channels are numbers between 0 and 1 (inclusive) or percentages between `0%` and `100%` (inclusive).

If any color channel is outside the range 0 to 1, this represents a color outside the standard gamut for its color space.

@debug color(srgb 0.1 0.6 1); 
@debug color(xyz 30% 0% 90% / 50%); 

// SASS
@debug color(srgb 0.1 0.6 1)  // color(srgb 0.1 0.6 1)
@debug color(xyz 30% 0% 90% / 50%)  // color(xyz 0.3 0 0.9 / 50%)

hsl($hue $saturation $lightness)
hsl($hue $saturation $lightness / $alpha)
hsl($hue, $saturation, $lightness, $alpha: 1)
hsla($hue $saturation $lightness)
hsla($hue $saturation $lightness / $alpha)
hsla($hue, $saturation, $lightness, $alpha: 1) 
Compatibility (Level 4 Syntax):

Dart Sass since 1.15.0

LibSass✗

Ruby Sass✗

LibSass and Ruby Sass only support the following signatures:

*   `hsl($hue, $saturation, $lightness)`
*   `hsla($hue, $saturation, $lightness, $alpha)`

Note that for these implementations, the `$alpha` argument is _required_ if the function name `hsla()` is used, and _forbidden_ if the function name `hsl()` is used.

Compatibility (Percent Alpha):

Dart Sass✓

LibSass✗

Ruby Sass since 3.7.0

LibSass and older versions of Ruby Sass don’t support alpha values specified as percentages.

Returns a color with the given [hue, saturation, and lightness](https://en.wikipedia.org/wiki/HSL_and_HSV) and the given alpha channel.

The hue is a number between `0deg` and `360deg` (inclusive) and may be unitless. The saturation and lightness are typically numbers between `0%` and `100%` (inclusive) and may _not_ be unitless. The alpha channel can be specified as either a unitless number between 0 and 1 (inclusive), or a percentage between `0%` and `100%` (inclusive).

A hue outside `0deg` and `360deg` is equivalent to `$hue % 360deg`. A saturation less than `0%` is clamped to `0%`. A saturation above `100%` or a lightness outside `0%` and `100%` are both allowed, and represent colors outside the standard RGB gamut.

Sass’s [special parsing rules](https://devdocs.io/sass/operators/numeric#slash-separated-values) for slash-separated values make it difficult to pass variables for `$lightness` or `$alpha` when using the `hsl($hue $saturation $lightness / $alpha)` signature. Consider using `hsl($hue, $saturation, $lightness, $alpha)` instead.

@debug hsl(210deg 100% 20%); 
@debug hsl(210deg 100% 20% / 50%); 
@debug hsla(34, 35%, 92%, 0.2); 

// SASS
@debug hsl(210deg 100% 20%) // #036
@debug hsl(210deg 100% 20% / 50%)  // rgba(0, 51, 102, 0.5)
@debug hsla(34, 35%, 92%, 0.2)  // rgba(241.74, 235.552, 227.46, 0.2)

hwb($hue $whiteness $blackness)
hwb($hue $whiteness $blackness / $alpha)
color.hwb($hue $whiteness $blackness)
color.hwb($hue $whiteness $blackness / $alpha)
color.hwb($hue, $whiteness, $blackness, $alpha: 1) 
Compatibility:

Dart Sass since 1.78.0

LibSass✗

Ruby Sass✗

Returns a color with the given [hue, whiteness, and blackness](https://en.wikipedia.org/wiki/HWB_color_model) and the given alpha channel.

The hue is a number between `0deg` and `360deg` (inclusive) and may be unitless. The whiteness and blackness are numbers typically between `0%` and `100%` (inclusive) and may _not_ be unitless. The alpha channel can be specified as either a unitless number between 0 and 1 (inclusive), or a percentage between `0%` and `100%` (inclusive).

A hue outside `0deg` and `360deg` is equivalent to `$hue % 360deg`. If `$whiteness + $blackness > 100%`, the two values are scaled so that they add up to `100%`. If `$whiteness`, `$blackness`, or both are less than `0%`, this represents a color outside the standard RGB gamut.

The `color.hwb()` variants are deprecated. New Sass code should use the global `hwb()` function instead.

@debug hwb(210deg 0% 60%); 
@debug hwb(210 0% 60% / 0.5); 

// SASS
@debug hwb(210deg 0% 60%)  // #036
@debug hwb(210 0% 60% / 0.5)  // rgba(0, 51, 102, 0.5)

lab($lightness $a $b)
lab($lightness $a $b / $alpha) 
Compatibility:

Dart Sass since 1.78.0

LibSass✗

Ruby Sass✗

Returns a color with the given [lightness, a, b], and alpha channels.

The lightness is a number between `0%` and `100%` (inclusive) and may be unitless. The a and b channels can be specified as either [unitless](https://devdocs.io/sass/values/numbers#units) numbers between -125 and 125 (inclusive), or percentages between `-100%` and `100%` (inclusive). The alpha channel can be specified as either a unitless number between 0 and 1 (inclusive), or a percentage between `0%` and `100%` (inclusive).

A lightness outside the range `0%` and `100%` is clamped to be within that range. If the a or b channels are outside the range `-125` to `125`, this represents a color outside the standard CIELAB gamut.

@debug lab(50% -20 30); 
@debug lab(80% 0% 20% / 0.5); 

// SASS
@debug lab(50% -20 30)  // lab(50% -20 30)
@debug lab(80% 0% 20% / 0.5)  // lab(80% 0 25 / 0.5);

lch($lightness $chroma $hue)
lch($lightness $chroma $hue / $alpha) 
Compatibility:

Dart Sass since 1.78.0

LibSass✗

Ruby Sass✗

Returns a color with the given [lightness, chroma, and hue], and the given alpha channel.

The lightness is a number between `0%` and `100%` (inclusive) and may be unitless. The chroma channel can be specified as either a [unitless](https://devdocs.io/sass/values/numbers#units) number between 0 and 150 (inclusive), or a percentage between `0%` and `100%` (inclusive). The hue is a number between `0deg` and `360deg` (inclusive) and may be unitless. The alpha channel can be specified as either a unitless number between 0 and 1 (inclusive), or a percentage between `0%` and `100%` (inclusive).

A lightness outside the range `0%` and `100%` is clamped to be within that range. A chroma below 0 is clamped to 0, and a chroma above 150 represents a color outside the standard CIELAB gamut. A hue outside `0deg` and `360deg` is equivalent to `$hue % 360deg`.

@debug lch(50% 10 270deg); 
@debug lch(80% 50% 0.2turn / 0.5); 

// SASS
@debug lch(50% 10 270deg)  // lch(50% 10 270deg)
@debug lch(80% 50% 0.2turn / 0.5)  // lch(80% 75 72deg / 0.5);

oklab($lightness $a $b)
oklab($lightness $a $b / $alpha) 
Compatibility:

Dart Sass since 1.78.0

LibSass✗

Ruby Sass✗

Returns a color with the given [perceptually-uniform lightness, a, b](https://bottosson.github.io/posts/oklab/), and alpha channels.

The lightness is a number between `0%` and `100%` (inclusive) and may be unitless. The a and b channels can be specified as either [unitless](https://devdocs.io/sass/values/numbers#units) numbers between -0.4 and 0.4 (inclusive), or percentages between `-100%` and `100%` (inclusive). The alpha channel can be specified as either a unitless number between 0 and 1 (inclusive), or a percentage between `0%` and `100%` (inclusive).

A lightness outside the range `0%` and `100%` is clamped to be within that range. If the a or b channels are outside the range `-0.4` to `0.4`, this represents a color outside the standard Oklab gamut.

@debug oklab(50% -0.1 0.15); 
@debug oklab(80% 0% 20% / 0.5); 

// SASS
@debug oklab(50% -0.1 0.15)  // oklab(50% -0.1 0.15)
@debug oklab(80% 0% 20% / 0.5)  // oklab(80% 0 0.08 / 0.5)

oklch($lightness $chroma $hue)
oklch($lightness $chroma $hue / $alpha) 
Compatibility:

Dart Sass since 1.78.0

LibSass✗

Ruby Sass✗

Returns a color with the given [perceptually-uniform lightness, chroma, and hue], and the given alpha channel.

The lightness is a number between `0%` and `100%` (inclusive) and may be unitless. The chroma channel can be specified as either a [unitless](https://devdocs.io/sass/values/numbers#units) number between 0 and 0.4 (inclusive), or a percentage between `0%` and `100%` (inclusive). The hue is a number between `0deg` and `360deg` (inclusive) and may be unitless. The alpha channel can be specified as either a unitless number between 0 and 1 (inclusive), or a percentage between `0%` and `100%` (inclusive).

A lightness outside the range `0%` and `100%` is clamped to be within that range. A chroma below 0 is clamped to 0, and a chroma above 0.4 represents a color outside the standard Oklab gamut. A hue outside `0deg` and `360deg` is equivalent to `$hue % 360deg`.

@debug oklch(50% 0.3 270deg); 
@debug oklch(80% 50% 0.2turn / 0.5); 

// SASS
@debug oklch(50% 0.3 270deg)  // oklch(50% 0.3 270deg)
@debug oklch(80% 50% 0.2turn / 0.5)  // oklch(80% 0.2 72deg / 0.5);

rgb($red $green $blue)
rgb($red $green $blue / $alpha)
rgb($red, $green, $blue, $alpha: 1)
rgb($color, $alpha)
rgba($red $green $blue)
rgba($red $green $blue / $alpha)
rgba($red, $green, $blue, $alpha: 1)
rgba($color, $alpha) 
Compatibility (Level 4 Syntax):

Dart Sass since 1.15.0

LibSass✗

Ruby Sass✗

LibSass and Ruby Sass only support the following signatures:

*   `rgb($red, $green, $blue)`
*   `rgba($red, $green, $blue, $alpha)`
*   `rgba($color, $alpha)`

Note that for these implementations, the `$alpha` argument is _required_ if the function name `rgba()` is used, and _forbidden_ if the function name `rgb()` is used.

Compatibility (Percent Alpha):

Dart Sass✓

LibSass✗

Ruby Sass since 3.7.0

LibSass and older versions of Ruby Sass don’t support alpha values specified as percentages.

If `$red`, `$green`, `$blue`, and optionally `$alpha` are passed, returns a color with the given red, green, blue, and alpha channels.

Each channel can be specified as either a [unitless](https://devdocs.io/sass/values/numbers#units) number between 0 and 255 (inclusive), or a percentage between `0%` and `100%` (inclusive). The alpha channel can be specified as either a unitless number between 0 and 1 (inclusive), or a percentage between `0%` and `100%` (inclusive).

If any color channel is outside the range 0 to 255, this represents a color outside the standard RGB gamut.

Sass’s [special parsing rules](https://devdocs.io/sass/operators/numeric#slash-separated-values) for slash-separated values make it difficult to pass variables for `$blue` or `$alpha` when using the `rgb($red $green $blue / $alpha)` signature. Consider using `rgb($red, $green, $blue, $alpha)` instead.

@debug rgb(0 51 102); 
@debug rgb(95%, 92.5%, 89.5%); 
@debug rgb(0 51 102 / 50%); 
@debug rgba(95%, 92.5%, 89.5%, 0.2); 

// SASS
@debug rgb(0 51 102)  // #036
@debug rgb(95%, 92.5%, 89.5%)  // #f2ece4
@debug rgb(0 51 102 / 50%)  // rgba(0, 51, 102, 0.5)
@debug rgba(95%, 92.5%, 89.5%, 0.2)  // rgba(242, 236, 228, 0.2)

* * *

If `$color` and `$alpha` are passed, this returns `$color` with the given `$alpha` channel instead of its original alpha channel.

@debug rgb(#f2ece4, 50%); 
@debug rgba(rgba(0, 51, 102, 0.5), 1); 

// SASS
@debug rgb(#f2ece4, 50%)  // rgba(242, 236, 228, 0.5)
@debug rgba(rgba(0, 51, 102, 0.5), 1)  // #003366

Deprecated Functions
--------------------

if($condition, $if-true, $if-false)
Returns `$if-true` if `$condition` is [truthy](https://devdocs.io/sass/at-rules/control/if#truthiness-and-falsiness), and `$if-false` otherwise.

This function is special in that it doesn’t even evaluate the argument that isn’t returned, so it’s safe to call even if the unused argument would throw an error.

Now that CSS supports its own [`if()` function syntax](https://devdocs.io/sass/syntax/special-functions#if), Sass is moving to use that syntax instead. The old `if()` function is deprecated, although it will continue to be supported in Dart Sass until version 3.0.0. See [/d/if-function](https://sass-lang.com/documentation/breaking-changes/if-function) for more information.

@debug if(true, 10px, 15px); 
@debug if(false, 10px, 15px); 
@debug if(variable-defined($var), $var, null); 

// SASS
@debug if(true, 10px, 15px)  // 10px
@debug if(false, 10px, 15px)  // 15px
@debug if(variable-defined($var), $var, null)  // null
