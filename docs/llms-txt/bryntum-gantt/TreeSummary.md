# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/TreeSummary.md

# [TreeSummary](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary)

A feature allowing you to roll up and display values in the time axis cell for each parent row in a tree scheduler.

This feature is **disabled** by default.

```
const scheduler = new Scheduler({
     appendTo : 'container',
     features : {
         treeSummary : {
             renderer({ startDate, endDate, resourceRecord, timeline }) {
                 let totalDemandedCapacity = 0;

                 resourceRecord.traverse(child => {
                     child.events.forEach(task => {
                         if (DateHelper.intersectSpans(task.startDate, task.endDate, startDate, endDate)) {
                             totalDemandedCapacity += task.demandedCapacity || 0;
                         }
                     });
                 }, true);

                 if (timeline.project.effectiveCalendar.isWorkingTime(startDate, endDate)) {
                     return 1 - totalDemandedCapacity;
                 }

                 return 0;
             }
         }
     }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[renderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#config-renderer)
Required, renderer function for parent resource summary cells. Used to both calculate and format the summary. Should return textual content or a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

```
new Scheduler({
    features : {
        treeSummary : {
            renderer({ startDate, endDate, resourceRecord, timeline }) {
                 let totalDemandedCapacity = 0;

                 resourceRecord.traverse(node => {
                    node.events.forEach(task => {
                         if (DateHelper.intersectSpans(task.startDate, task.endDate, startDate, endDate)) {
                             totalDemandedCapacity += task.demandedCapacity || 0;
                         }
                     });
                 }, true);

                 if (timeline.project.effectiveCalendar.isWorkingTime(startDate, endDate)) {
                     return 1 - totalDemandedCapacity;
                 }

                 return 0;
            }
        }
    }
});
```

[enableMouseEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#config-enableMouseEvents)
Set to `false` to disallow mouse interactions with the rendered range elements. By default, the range elements are reachable with the mouse.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTreeSummary](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#property-isTreeSummary)
Identifies an object as an instance of [TreeSummary](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TreeSummary) class, or subclass thereof.

[isTreeSummary](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#property-isTreeSummary-static)
Identifies an object as an instance of [TreeSummary](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TreeSummary) class, or subclass thereof.

[enableMouseEvents](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#property-enableMouseEvents)
Set to `false` to disallow mouse interactions with the rendered range elements. By default, the range elements are reachable with the mouse.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[tickCellMouseDown](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#event-tickCellMouseDown)
Triggered for mouse down on a tick cell. Only triggered if the TreeSummary feature is configured with `[enableMouseEvents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TreeSummary#config-enableMouseEvents): true`.

[tickCellMouseUp](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#event-tickCellMouseUp)
Triggered for mouse up on a tick cell. Only triggered if the TreeSummary feature is configured with `[enableMouseEvents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TreeSummary#config-enableMouseEvents): true`.

[tickCellClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#event-tickCellClick)
Triggered for click on a tick cell. Only triggered if the TreeSummary feature is configured with `[enableMouseEvents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TreeSummary#config-enableMouseEvents): true`.

[tickCellDblClick](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#event-tickCellDblClick)
Triggered for double-click on a tick cell. Only triggered if the TreeSummary feature is configured with `[enableMouseEvents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TreeSummary#config-enableMouseEvents): true`.

[tickCellContextMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/TreeSummary#event-tickCellContextMenu)
Triggered for right-click on a tick cell. Only triggered if the TreeSummary feature is configured with `[enableMouseEvents](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TreeSummary#config-enableMouseEvents): true`.
