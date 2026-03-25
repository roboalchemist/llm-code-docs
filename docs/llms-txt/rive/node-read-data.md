# Source: https://uat.rive.app/docs/scripting/api-reference/artboards/node-read-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# NodeReadData

Represents a node in the hierarchy, providing transform properties and
access to parent and child nodes.

## Fields

### `position`

The local position of the node.

### `rotation`

The local rotation of the node in radians.

### `scale`

The local scale of the node.

### `worldTransform`

The world transform of the node.

### `x`

The x-coordinate of the local position.

### `y`

The y-coordinate of the local position.

### `scaleX`

The x component of the local scale.

### `scaleY`

The y component of the local scale.

### `paint`

If node is a Path, paint trait is available with paint data

## Methods

### `asPath`

If node is a Path, returns the node as PathData

### `asPaint`

If node is a ShapePaint (Fill or Stroke), returns node as Paint
