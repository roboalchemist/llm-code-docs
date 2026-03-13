# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/Swipe.md

# [Swipe](https://bryntum.com/docs/gantt/api/Core/helper/util/Swipe)

This class recognizes and fires `swipe` gesture events.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[durationLimit](https://bryntum.com/docs/gantt/api/Core/helper/util/Swipe#config-durationLimit)
The maximum amount of time (in milliseconds) for the swipe gesture to complete. If the touch gesture lasts longer than this limit, the gesture will not be recognized as a `swipe`.

[idleLimit](https://bryntum.com/docs/gantt/api/Core/helper/util/Swipe#config-idleLimit)
The time limit (in milliseconds) for a gesture to receive no events. If no touch movement occurs for this amount of time, the gesture will not be recognized as a `swipe`.

[threshold](https://bryntum.com/docs/gantt/api/Core/helper/util/Swipe#config-threshold)
The minimum amount of movement (in pixels) that must occur for the touch gesture to be recognized as a `swipe`.

[tolerance](https://bryntum.com/docs/gantt/api/Core/helper/util/Swipe#config-tolerance)
The maximum amount of movement (in pixels) that is allowed on the opposite axis to still be recognized as a `swipe`. By default, up to 30px of movement is allowed in the Y-axis of an X-axis swipe, and vice versa.
