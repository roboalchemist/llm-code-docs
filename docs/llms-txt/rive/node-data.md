# Source: https://uat.rive.app/docs/scripting/api-reference/artboards/node-data.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# NodeData

Represents a node in the hierarchy, providing transform properties and
access to parent and child nodes.

## Fields

### `children`

The node’s children.

### `parent`

The parent of the node, or nil if it has none.

## Methods

### `decompose`

Updates the node’s position, rotation, and scale from the given world
transform.
