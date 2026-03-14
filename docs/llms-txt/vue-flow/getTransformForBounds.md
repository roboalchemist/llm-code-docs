# Source: https://vueflow.dev/typedocs/functions/getTransformForBounds.md

---
url: /typedocs/functions/getTransformForBounds.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: getTransformForBounds()

> **getTransformForBounds**(`bounds`, `width`, `height`, `minZoom`, `maxZoom`, `padding`): [`ViewportTransform`](../interfaces/ViewportTransform.md)

Returns a viewport that encloses the given bounds with padding.

## Parameters

• **bounds**: [`Rect`](../interfaces/Rect.md)

Bounds to fit inside viewport.

• **width**: `number`

Width of the viewport.

• **height**: `number`

Height of the viewport.

• **minZoom**: `number`

Minimum zoom level of the resulting viewport.

• **maxZoom**: `number`

Maximum zoom level of the resulting viewport.

• **padding**: [`Padding`](../type-aliases/Padding.md) = `0.1`

Padding around the bounds.

## Returns

[`ViewportTransform`](../interfaces/ViewportTransform.md)

A transformed Viewport that encloses the given bounds which you can pass to e.g. setViewport.

## Remarks

You can determine bounds of nodes with getNodesBounds and getBoundsOfRects

## Example

```ts
const { x, y, zoom } = getViewportForBounds(
{ x: 0, y: 0, width: 100, height: 100},
1200, 800, 0.5, 2);
```
