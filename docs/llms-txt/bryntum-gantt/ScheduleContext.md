# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ScheduleContext.md

# [ScheduleContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext)

Allow visually selecting a schedule "cell" by clicking, or [any other pointer gesture](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-triggerEvent).

This feature is **disabled** by default

```
const scheduler = new Scheduler({
    features : {
        // Configure as a truthy value to enable the feature
        scheduleContext : {
            triggerEvent : 'hover',
            renderer     : (context, element) => {
                element.innerText = '😎';
            }
        }
    }
});
```

The contextual details are available in the [context](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#property-context) property.

**Note that the context is cleared upon change of [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#property-viewPreset) such as when zooming in or out.**

Multiple cell selection
-----------------------

The feature allows selecting multiple schedule cells (can be toggled with the [multiSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-multiSelect) config). The selected cells are stored in the [selectedCells](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-selectedCells) collection. Selecting multiple cells can be done using the mouse by clicking while pressing the `[Shift]` key or using the keyboard (see next chapter for shortcuts). Also selection can be done programmatically by calling the [selectCellRange](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#function-selectCellRange) method.

Keyboard navigation and cell selection
--------------------------------------

The feature also implements keyboard navigation across cells (can be toggled with [keyNavigation](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-keyNavigation) config) and keyboard cell selection (can be toggled with [multiSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-multiSelect) config).

When enabled it uses following default keyboard shortcuts:

Keys

Action

`ArrowUp`

Focuses the cell above currently focused cell.

`ArrowRight`

Focuses the cell to the right of currently focused cell

`ArrowDown`

Focuses the cell below currently focused cell

`ArrowLeft`

Focuses the cell to the left of currently focused cell

`Shift`+`ArrowUp`

Extends the selection one row up from currently focused cell

`Shift`+`ArrowRight`

Extends the selection one column to the right from currently focused cell

`Shift`+`ArrowDown`

Extends the selection one row down from currently focused cell

`Shift`+`ArrowLeft`

Extends the selection one column to the left from currently focused cell

\`Escape

Clears cells selection

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[triggerEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-triggerEvent)
The pointer event type to use to update the context. May be `'hover'` to highlight the tick context when moving the mouse across the timeline.

[renderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-renderer)
A function (or the name of a function) which may mutate the contents of the context overlay element which tracks the active resource/tick context. Use this when simple, decorative or informational HTML is required.

When [multiSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-multiSelect) is enabled the function is called for each of the selected cells and then its second argument receives a DOM configuration object of the cell. In contrast when [multiSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-multiSelect) is `false` (default) the second argument provides a DOM element.

Use the [widget](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-widget) option to show a widget with interaction in a tick cell.

[widget](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-widget)
A widget config describing the widget to show in the context tick.

[activateOnEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-activateOnEvent)
By default, the ScheduleContext feature hides its widget or element when the pointer is over event/task bar.

Set this property to `true` to activate when over an event/task bar.

[shareWithEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-shareWithEvent)
By default, the ScheduleContext feature hides its widget or element when the pointer is over a tick in which an event/task bar exists.

Set this property to `true` to activate when an event/task bar also exists in the context tick.

[keyNavigation](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-keyNavigation)
Enables keyboard navigation across ticks.

[multiSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-multiSelect)
Enables multiple cell selection. Selected cells are stored in [selectedCells](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-selectedCells) collection.

[startNavigationOnColumnFocus](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-startNavigationOnColumnFocus)
`true` to automatically enable tick cells navigation when focusing the timeaxis column

[selectedCells](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#config-selectedCells)
Collection of selected cells.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScheduleContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-isScheduleContext)
Identifies an object as an instance of [ScheduleContext](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext) class, or subclass thereof.

[isScheduleContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-isScheduleContext-static)
Identifies an object as an instance of [ScheduleContext](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext) class, or subclass thereof.

[widget](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-widget)
The widget shown in timeline ticks. The widget will be sized and positioned to fit the tick.

Before being shown, it will be primed with a property called `timelineContext` which is a [TimelineContext](https://bryntum.com/docs/gantt/api/#Scheduler/util/TimelineContext) which describes exactly which tick is active.

The widget's [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-owner) will be the Scheduler.

The [owner](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#property-owner)'s [timelineContext](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#property-timelineContext) will also reference the current context.

[timelineContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-timelineContext)
The active context.

[activateOnEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-activateOnEvent)
By default, the ScheduleContext feature hides its widget or element when the pointer is over event/task bar.

Set this property to `true` to activate when over an event/task bar.

[shareWithEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-shareWithEvent)
By default, the ScheduleContext feature hides its widget or element when the pointer is over a tick in which an event/task bar exists.

Set this property to `true` to activate when an event/task bar also exists in the context tick.

[context](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-context)
The contextual information about which cell was clicked on and highlighted.

When the [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#property-viewPreset) is changed (such as when zooming) the context is cleared and the highlight is removed.

[element](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-element)
The element which is used to highlight the context if a [renderer](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-renderer) is being used. This is created lazily, and is not created if a widget is configured.

[timelineCell](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-timelineCell)
Currently active timeline cell.

[isNavigatingTimelineCells](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#property-isNavigatingTimelineCells)
Indicates whether navigating in the TimeAxis column is started and the timeaxis column is focused

## Functions

Functions are methods available for calling on the class

[clear](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#function-clear)
Clears the current visible context element

[hasEvent](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#function-hasEvent)
Utility function to see if there is an event bar coinciding with the passed timeline context

[selectCellRange](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#function-selectCellRange)
Extends selection from one cell to another.

[startTimelineCellsNavigation](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#function-startTimelineCellsNavigation)
Starts navigating the TimeAxis column cells (if the timeaxis column is focused)

[stopTimelineCellsNavigation](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#function-stopTimelineCellsNavigation)
Stops navigating the TimeAxis column cells

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeContextShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#event-beforeContextShow)
This event is fired on the owning Scheduler when the context [element](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#property-element) or [widget](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#property-widget) is about to be shown.

The position and size of the context element may be mutated by a handler.

If using a widget, the `position` object will be applied by the widget's `setConfig` method, so properties may be deleted or added or mutated to affect the widget in any way.

If using a renderer, the `position` object will be used to size and position the [element](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#property-element) which is used to highlight the context.

Returning `false` from a handler will prevent the context element from being shown.

[beforeSelectedContextsShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/ScheduleContext#event-beforeSelectedContextsShow)
This event is fired on the owning Scheduler before the selected contexts are rendered. The event is triggered only when [multiSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#config-multiSelect) is enabled

The position and size of the context element may be mutated by a handler.

If using a widget, the `position` object will be applied by the widget's `setConfig` method, so properties may be deleted or added or mutated to affect the widget in any way.

If using a renderer, the `position` object will be used to size and position the [element](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ScheduleContext#property-element) which is used to highlight the context.

Returning `false` from a handler will prevent the context element from being shown.
