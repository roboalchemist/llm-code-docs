# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/mixin/DependencyCreation.md

# [DependencyCreation](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation)

Mixin for Dependencies feature that handles dependency creation (drag & drop from terminals which are shown on hover). Requires [Delayable](https://bryntum.com/docs/gantt/api/#Core/mixin/Delayable) to be mixed in alongside.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[allowDropOnEventBar](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-allowDropOnEventBar)
`false` to require a drop on a target event bar side circle to define the dependency type. If dropped on the event bar, the `defaultValue` of the DependencyModel `type` field will be used to determine the target task side.

[terminalSize](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-terminalSize)
Terminal diameter in px, overrides the default CSS value for it (which might depend on theme).

Use an even number to avoid cropped terminals.

Also accepts a string value representing a CSS size, e.g. '1.5em'.

When unset, the value specified in the `--b-dependency-terminal-size` CSS variable is used.

[terminalOffset](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-terminalOffset)
Terminal offset from their initial position, in px. Positive values move terminals further away from the event bar, negative values inside the event bar.

When unset, the value specified in the `--b-dependency-terminal-offset` CSS variable is used.

[terminalShowDelay](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-terminalShowDelay)
Delay in ms before showing the terminals when hovering over an event bar.

Can be used for a more "stable" UI, where the terminals are not shown immediately when hovering over an event bar and thus have fewer things moving when mouse is moved quickly over multiple event bars.

[terminalHideDelay](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-terminalHideDelay)
Delay in ms before hiding the terminals when the mouse leaves an event bar or terminal.

Can be used to make the UI more forgiving, accidentally leaving the event bar or terminal will not immediately hide the terminals.

Can also be used to play a hide animation, set a `terminalHideDelay` that is longer than your animation's duration. The `b-hiding-terminals` CSS class is added to the event wrapper while the terminals are being hidden.

[allowCreateOnlyParent](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-allowCreateOnlyParent)
Set it to `true` to allow dependency creation only for parent events (only applies to Scheduler Pro using the `NestedEvents` feature). Normally the nested event container inside parent events cannot be scrolled when using dependencies, but by enabling this setting and limiting to where dependencies can be drawn scrolling will be enabled.

[showCreationTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-showCreationTooltip)
`false` to not show a tooltip while creating a dependency

[creationTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-creationTooltip)
A tooltip config object that will be applied to the dependency creation [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip)

[creationTooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-creationTooltipTemplate)
A template function that will be called to generate the HTML contents of the dependency creation tooltip. You can return either an HTML string or a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

[terminalCls](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-terminalCls)
CSS class used for terminals

[terminalSides](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-terminalSides)
Where (on event bar edges) to display terminals. The sides are `'start'`, `'top'`, `'end'` and `'bottom'`

[allowCreate](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#config-allowCreate)
Set to `false` to not allow creating dependencies

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyCreation](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-isDependencyCreation)
Identifies an object as an instance of [DependencyCreation](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/DependencyCreation) class, or subclass thereof.

[isDependencyCreation](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-isDependencyCreation-static)
Identifies an object as an instance of [DependencyCreation](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/DependencyCreation) class, or subclass thereof.

[allowDropOnEventBar](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-allowDropOnEventBar)
`false` to require a drop on a target event bar side circle to define the dependency type. If dropped on the event bar, the `defaultValue` of the DependencyModel `type` field will be used to determine the target task side.

[terminalSize](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-terminalSize)
Terminal diameter in px, overrides the default CSS value for it (which might depend on theme).

Use an even number to avoid cropped terminals.

Also accepts a string value representing a CSS size, e.g. '1.5em'.

When unset, the value specified in the `--b-dependency-terminal-size` CSS variable is used.

[terminalOffset](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-terminalOffset)
Terminal offset from their initial position, in px. Positive values move terminals further away from the event bar, negative values inside the event bar.

When unset, the value specified in the `--b-dependency-terminal-offset` CSS variable is used.

[terminalShowDelay](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-terminalShowDelay)
Delay in ms before showing the terminals when hovering over an event bar.

Can be used for a more "stable" UI, where the terminals are not shown immediately when hovering over an event bar and thus have fewer things moving when mouse is moved quickly over multiple event bars.

[terminalHideDelay](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-terminalHideDelay)
Delay in ms before hiding the terminals when the mouse leaves an event bar or terminal.

Can be used to make the UI more forgiving, accidentally leaving the event bar or terminal will not immediately hide the terminals.

Can also be used to play a hide animation, set a `terminalHideDelay` that is longer than your animation's duration. The `b-hiding-terminals` CSS class is added to the event wrapper while the terminals are being hidden.

[creationTooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#property-creationTooltipTemplate)
A template function that will be called to generate the HTML contents of the dependency creation tooltip. You can return either an HTML string or a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

## Functions

Functions are methods available for calling on the class

[onTimeSpanMouseEnter](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-onTimeSpanMouseEnter)
Show terminals when mouse enters event/task element

[onTimeSpanMouseLeave](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-onTimeSpanMouseLeave)
Hide terminals when mouse leaves event/task element

[onTerminalMouseOut](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-onTerminalMouseOut)
Remove hover styling when mouse leaves terminal. Also hides terminals when mouse leaves one it and not creating a dependency.

[onTerminalPointerDown](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-onTerminalPointerDown)
Start creating a dependency when mouse is pressed over terminal

[onMouseMove](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-onMouseMove)
Update connector line showing dependency between source and target when mouse moves. Also check if mouse is over a valid target terminal

[onMouseUp](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-onMouseUp)
Create a new dependency if mouse release over valid terminal. Hides connector

[abort](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-abort)
Aborts dependency creation, removes proxy and cleans up listeners

[createConnector](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-createConnector)
Creates a connector line that visualizes dependency source & target

[removeConnector](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-removeConnector)
Remove connector

[showTerminals](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-showTerminals)
Show terminals for specified event at sides defined in #terminalSides.

[hideTerminals](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-hideTerminals)
Hide terminals for specified event

[createDependency](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-createDependency)
Create a new dependency from source terminal to target terminal

[refreshCreationTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#function-refreshCreationTooltip)
Update dependency creation tooltip

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeDependencyCreateDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-beforeDependencyCreateDrag)
Fired on the owning Scheduler/Gantt before a dependency creation drag operation starts. Return `false` to prevent it

[dependencyCreateDragStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-dependencyCreateDragStart)
Fired on the owning Scheduler/Gantt when a dependency creation drag operation starts

[dependencyValidationComplete](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-dependencyValidationComplete)
Fired on the owning Scheduler/Gantt when asynchronous dependency validation completes

[dependencyValidationStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-dependencyValidationStart)
Fired on the owning Scheduler/Gantt when asynchronous dependency validation starts

[beforeDependencyCreateFinalize](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-beforeDependencyCreateFinalize)
Fired on the owning Scheduler/Gantt when a dependency drag creation operation is about to finalize

[dependencyCreateDrop](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-dependencyCreateDrop)
Fired on the owning Scheduler/Gantt when a dependency drag creation operation succeeds

[afterDependencyCreateDrop](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-afterDependencyCreateDrop)
Fired on the owning Scheduler/Gantt after a dependency drag creation operation finished, no matter to outcome

[beforeShowTerminals](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyCreation#event-beforeShowTerminals)
Fired on the owning Scheduler/Gantt before showing dependency terminals on a task or event. Return `false` to prevent it
