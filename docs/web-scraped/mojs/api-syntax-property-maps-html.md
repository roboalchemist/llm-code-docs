# Source: https://mojs.github.io/api/syntax/property-maps.html

Title: Property Map Syntax | mo.js

URL Source: https://mojs.github.io/api/syntax/property-maps.html

Markdown Content:
Property Map Syntax | mo.js
===============

[![Image 1: mo.js](https://mojs.github.io/assets/img/logo.svg)mo.js](https://mojs.github.io/)

[Home](https://mojs.github.io/)

[Tutorials](https://mojs.github.io/tutorials/)

[Api](https://mojs.github.io/api/)

[Tools](https://mojs.github.io/tools/)

[Github (opens new window)](https://github.com/mojs)

[Home](https://mojs.github.io/)

[Tutorials](https://mojs.github.io/tutorials/)

[Api](https://mojs.github.io/api/)

[Tools](https://mojs.github.io/tools/)

[Github (opens new window)](https://github.com/mojs)

*   Tutorials

*   Tools

*   API

    *   [API overview](https://mojs.github.io/api/)
    *   Modules

        *   [Html](https://mojs.github.io/api/modules/html/)
        *   [Shape](https://mojs.github.io/api/modules/shape/)
        *   [ShapeSwirl](https://mojs.github.io/api/modules/shape-swirl/)
        *   [Burst](https://mojs.github.io/api/modules/burst/)

    *   Tweens

        *   [Tween](https://mojs.github.io/api/tweens/tween.html)
        *   [Timeline](https://mojs.github.io/api/tweens/timeline.html)

    *   Utils

        *   [Stagger](https://mojs.github.io/api/utils/stagger.html)

    *   Easing

        *   [Base Easing Functions](https://mojs.github.io/api/easing/base-functions.html)
        *   [Bezier Curves](https://mojs.github.io/api/easing/bezier-curves.html)
        *   [Path Easing](https://mojs.github.io/api/easing/path-easing.html)
        *   [Approximate](https://mojs.github.io/api/easing/approximate.html)

    *   Syntax

        *   [Stagger Strings Syntax](https://mojs.github.io/api/syntax/stagger.html)
        *   [Rand Strings Syntax](https://mojs.github.io/api/syntax/rand.html)
        *   [Property Map Syntax](https://mojs.github.io/api/syntax/property-maps.html)
        *   [Available Units](https://mojs.github.io/api/syntax/units.html)

[#](https://mojs.github.io/api/syntax/property-maps.html#property-map-syntax) Property Map Syntax
=================================================================================================

*   [CodePen Example(opens new window)](https://codepen.io/sol0mka/pen/WxpGNm?editors=0010)

`Property Map` array was designed to express sequential values. Often used with `Burst` and `Stagger` modules to generate values that repeat over children length. Basically it is just an array that maps its values to children based on child index with `mod` function. So if you have `property map` with `3 values` and `5 children`, then `4`th and `5`th items will recieve `0`th and `1`st values from the map respecively. Works with any values inside the array.

You can provide a `null` value if you wanna use the default value.

Full API reference:

```
// ...
  property : [ 20, { 20 : 0 }, 'rand(0, 20)', null ]
  // ...
```

*   [CodePen Example(opens new window)](https://codepen.io/sol0mka/pen/WxpGNm?editors=0010)

← [Rand Strings Syntax](https://mojs.github.io/api/syntax/rand.html)[Available Units](https://mojs.github.io/api/syntax/units.html) →
