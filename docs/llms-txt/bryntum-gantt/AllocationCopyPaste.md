# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/AllocationCopyPaste.md

# [AllocationCopyPaste](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste)

This is a feature of [ResourceUtilization](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization) view that allows to copy-paste assignment time-phased effort values.

```
new ResourceUtilization({
   ...
   // the view should not be readOnly to allow pasting
   readOnly : false,
   features : {
       // allow effort copy-pasting
       allocationCopyPaste : true,
       ...
   },
   ...
});
```

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[pasteInEventTimeSpanOnly](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#config-pasteInEventTimeSpanOnly)
Provide `true` to accept pasting in an event timespan only.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAllocationCopyPaste](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#property-isAllocationCopyPaste)
Identifies an object as an instance of [AllocationCopyPaste](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/AllocationCopyPaste) class, or subclass thereof.

[isAllocationCopyPaste](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#property-isAllocationCopyPaste-static)
Identifies an object as an instance of [AllocationCopyPaste](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/AllocationCopyPaste) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[cut](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#function-cut)
Cuts selected cells to clipboard (native if accessible) to paste later

[copy](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#function-copy)
Copies selected cells to clipboard (native if accessible) to paste later

[paste](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#function-paste)
Pastes string data into a cell or a range of cells. Either from native clipboard if that is accessible or from a fallback clipboard that is only available to the owner view.

The string data will be split on `\n` and `\t` and put in different rows and columns accordingly.

Note that there must be a selected cell to paste the data into.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[copyTimelineCells](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#event-copyTimelineCells)
Fires on the owning view after a copy action is performed.

[beforeCopyTimelineCells](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#event-beforeCopyTimelineCells)
Fires on the owning view before a copy action is performed, return `false` to prevent the action

[pasteTimelineCells](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#event-pasteTimelineCells)
Fires on the owning view after a paste action is performed.

[beforePasteTimelineCells](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCopyPaste#event-beforePasteTimelineCells)
Fires on the owning Grid before a paste action is performed, return `false` to prevent the action
