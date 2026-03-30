# Source: https://mojs.github.io/api/syntax/rand.html

Title: Rand Strings Syntax | mo.js

URL Source: https://mojs.github.io/api/syntax/rand.html

Markdown Content:
*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/dyXevEE?editors=0010)

`Rand` string was designed to express random numeric values. Can be unit based (percents, pixels, rems etc.).

Full API reference:

TIP

If you wanna update the random value after it's been declared, you can use the `generate()` function.

[#](https://mojs.github.io/api/syntax/rand.html#example-usage) Example usage
----------------------------------------------------------------------------

```
const example = new mojs.ShapeSwirl({
  parent: '#example',
  left: 0, top: 0,
  duration:       'rand(600, 1000)',
  radius:         'rand(10, 20)',
  pathScale:      'rand(.5, 1)',
  swirlFrequency: 'rand(2, 4)',
  swirlSize:      'rand(6, 14)',
});

document.getElementById('example').addEventListener( 'click', function (e) {
  const x = e.layerX,
    y = { [e.layerY]: e.layerY - 150 };
  example
    .tune({ x, y })
    .generate()
    .replay();
});

example.play();
```

Click anywere to see the updated random value

*   [CodePen Example(opens new window)](https://codepen.io/sandstedt/pen/dyXevEE?editors=0010)
