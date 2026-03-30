# Source: https://uat.rive.app/docs/scripting/api-reference/artboards/animation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Animation

## Fields

### `duration`

The duration of the animation.

## Methods

### `advance`

Advances the animation by the given time in seconds. Returns true if the
animation hasn't reached its end. If the animation is set to loop or ping
pong, it will always return true

### `setTime`

set the animation time in seconds

### `setTimeFrames`

set the animation time in frames

### `setTimePercentage`

set the animation time as a percentage of the duration
