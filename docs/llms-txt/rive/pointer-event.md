# Source: https://uat.rive.app/docs/scripting/api-reference/artboards/pointer-event.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PointerEvent

Represents a pointer interaction event containing position and pointer id.

## Fields

### `position`

The position of the pointer in local coordinates.

### `id`

The unique identifier for the pointer.

## Constructors

### `new`

## Methods

### `hit`

Marks the event as handled. If isTranslucent is true, the event may
continue to propagate through translucent hit targets.
