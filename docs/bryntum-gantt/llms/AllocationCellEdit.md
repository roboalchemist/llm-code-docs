# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/AllocationCellEdit.md

# [AllocationCellEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCellEdit)

Adding this feature to the resource utilization view enables assignment effort data editing.

Start editing
-------------

In order to start editing effort, one can double click it or press ENTER or F2 key when the corresponding cell is selected, or just start typing a number if [autoEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/AllocationCellEdit#config-autoEdit) is enabled (which it is by default).

```
new ResourceUtilization({
   ...
   features : {
       // allow effort editing
       allocationCellEdit : true,
       ...
   },
   ...
});
```

Finish editing
--------------

Editing can be cancelled by pressing ESC key, which will reject the change. In order to complete the edit and apply the change press F2 key or just click outside the editor.

Keyboard shortcuts
------------------

### While not editing

Keys

Action

`Enter`

Starts editing currently focused cell

`F2`

Starts editing currently focused cell

### While editing

Keys

Action

`Enter`

Finish editing and start editing the same cell in next row

`Shift`+`Enter`

Finish editing and start editing the same cell in previous row

`F2`

Finish editing

`Escape`

Cancel editing without applying changes

`Tab`

Finish editing and start editing the next cell in the same row

`Shift`+`Tab`

Finish editing and start editing the previous cell in the same row

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[forceTickDatesUsage](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCellEdit#config-forceTickDatesUsage)
Provide `true` to always use the edited ticks start and end dates. If `false` (default) the feature will use the edited assignment start date when editing the very first tick of the assignment and respectively the assignment end date when editing the last ticks).

[editor](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCellEdit#config-editor)
The embedded editor configuration.

[autoEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCellEdit#config-autoEdit)
Set to `true` to start editing when user starts typing a number on a focused allocation cell

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAllocationCellEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCellEdit#property-isAllocationCellEdit)
Identifies an object as an instance of [AllocationCellEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/AllocationCellEdit) class, or subclass thereof.

[isAllocationCellEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCellEdit#property-isAllocationCellEdit-static)
Identifies an object as an instance of [AllocationCellEdit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/AllocationCellEdit) class, or subclass thereof.

[autoEdit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/AllocationCellEdit#property-autoEdit)
Set to `true` to start editing when user starts typing a number on a focused allocation cell
