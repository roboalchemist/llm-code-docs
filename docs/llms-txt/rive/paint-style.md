# Source: https://uat.rive.app/docs/scripting/api-reference/paint/paint-style.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PaintStyle

Specifies how the shape should be painted.

* `stroke`
* `fill`

```lua highlight={3} theme={null}
self.paint = Paint.with({
  color = Color.rgb(255, 100, 50),
  style = 'stroke',
})
```
