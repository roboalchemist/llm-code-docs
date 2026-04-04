# Source: https://mojs.github.io/api/easing/approximate.html

Title: Approximate | mo.js

URL Source: https://mojs.github.io/api/easing/approximate.html

Markdown Content:
Approximate | mo.js
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

[#](https://mojs.github.io/api/easing/approximate.html#approximate) Approximate
===============================================================================

*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/yLJjMWP)

The `approximate` function samples any given function with slow running time and returns new easing function with very fast one. The result still slower than `base easing functions` and may contain a tiny approximation error (by default less than `0.0001`).

The syntax:

```
var fastEasing = mojs.easing.approximate( slowEasing, n = 4 );
  // where `n` is optional quantity of samples as `10^n` (larger `n` - smaller error).
```

Another strategy for the `approximate` function is to feed it with precomputed `JSON` data to same `CPU` pressure from presampling the slow function:

```
var samples = require('./samples.json');
  var fastEasing = mojs.easing.approximate( slowEasing, samples );
  // where `samples` is `JSON` object that contains presampled data.
```

You can have the presampled data by calling `getSamples` function:

```
var fastEasing = mojs.easing.approximate( slowEasing );
  var samples = fastEasing.getSamples();
```

*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/yLJjMWP)

← [Path Easing](https://mojs.github.io/api/easing/path-easing.html)[Stagger Strings Syntax](https://mojs.github.io/api/syntax/stagger.html) →
