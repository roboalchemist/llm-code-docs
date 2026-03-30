# Source: https://uat.rive.app/docs/scripting/api-reference/paint/stroke-cap.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# StrokeCap

Defines the shape used at the ends of open stroke segments.

* `butt` – squared, no extension.
* `round` – semicircular cap.
* `square` – squared, extends past the end point.

```lua highlight={3} theme={null}
self.paint = Paint.with({
  color = Color.rgb(255, 100, 50),
  cap = 'round',
  style = 'stroke',
})
```
