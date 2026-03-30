# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/LongPress.md

# [LongPress](https://bryntum.com/docs/gantt/api/Core/helper/util/LongPress)

This class recognizes and fires `longPress` gesture events.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[duration](https://bryntum.com/docs/gantt/api/Core/helper/util/LongPress#config-duration)
The number of milliseconds that a user must sustain a touch to trigger the `longPress` event.

[native](https://bryntum.com/docs/gantt/api/Core/helper/util/LongPress#config-native)
Set to `false` to disable firing `longPress` based on the native timeout behavior. On many mobile platforms, the native timeout is 500ms and would render the browser's native context menu.

[tolerance](https://bryntum.com/docs/gantt/api/Core/helper/util/LongPress#config-tolerance)
The number of pixels of movement allowed before rejecting the gesture as a longpress. In ideal conditions this would be 0, but some users may have difficulty holding perfectly still for the longpress `duration`.
