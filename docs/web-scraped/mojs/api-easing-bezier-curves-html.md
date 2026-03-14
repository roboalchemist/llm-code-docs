# Source: https://mojs.github.io/api/easing/bezier-curves.html

Title: Bezier Curves | mo.js

URL Source: https://mojs.github.io/api/easing/bezier-curves.html

Markdown Content:
Bezier Curves | mo.js
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

[#](https://mojs.github.io/api/easing/bezier-curves.html#bezier-curves) Bezier Curves
=====================================================================================

*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/QWErpLw)

The bezier curves functions can be expressed with string containing `bezier()` function or with `mojs.easing.bezier` constructor that returns a function:

```
// ...
  easing: 'bezier()',
  // or
  easing: mojs.easing.path('M0,100 C50,100 50,67.578125 50,50 C50,32.421875 50,0 100,0')
  // ...
```

*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/QWErpLw)

← [Base Easing Functions](https://mojs.github.io/api/easing/base-functions.html)[Path Easing](https://mojs.github.io/api/easing/path-easing.html) →
