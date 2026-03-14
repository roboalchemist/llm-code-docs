# Source: https://mojs.github.io/api/easing/base-functions.html

Title: Base Easing Functions | mo.js

URL Source: https://mojs.github.io/api/easing/base-functions.html

Markdown Content:
*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/BazxWag)

The base easing functions could be expressed with strings that contain `easing name` and `direction` delimited by `.` or could be accessed directly on `mojs.easing` object:

```
// ...
  easing: 'cubic.in',
  // or
  easing: mojs.easing.cubic.in
  // ...
```

The full list of base functions:

```
'linear.none'

  'ease.in'
  'ease.out'
  'ease.inout'

  'sin.in'
  'sin.out'
  'sin.inout'

  'quad.in'
  'quad.out'
  'quad.inout'

  'cubic.in'
  'cubic.out'
  'cubic.inout'

  'quart.in'
  'quart.out'
  'quart.inout'

  'quint.in'
  'quint.out'
  'quint.inout'

  'expo.in'
  'expo.out'
  'expo.inout'

  'circ.in'
  'circ.out'
  'circ.inout'

  'back.in'
  'back.out'
  'back.inout'

  'elastic.in'
  'elastic.out'
  'elastic.inout'

  'bounce.in'
  'bounce.out'
  'bounce.inout'
```

*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/BazxWag)
