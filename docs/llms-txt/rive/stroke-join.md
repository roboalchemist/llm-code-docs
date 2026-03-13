# Source: https://uat.rive.app/docs/scripting/api-reference/paint/stroke-join.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# StrokeJoin

Defines how two stroke segments are joined at a corner.

* `miter` – sharp corner.
* `round` – rounded corner.
* `bevel` – flattened corner.

```lua highlight={3} theme={null}
self.paint = Paint.with({
  color = Color.rgb(255, 100, 50),
  join = 'round',
  style = 'stroke',
})
```
