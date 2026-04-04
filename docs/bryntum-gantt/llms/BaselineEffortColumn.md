# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/BaselineEffortColumn.md

# [BaselineEffortColumn](https://bryntum.com/docs/gantt/api/Gantt/column/BaselineEffortColumn)

A column that displays the task baseline effort. A task could have multiple baselines and by default the column displays the very first (`0`\-index) baseline effort. To change that please use the following syntax:

```
new Gantt({
    ...
    columns : [
        {
            type : 'baselineeffort',
            // display the baseline with index 3
            field : 'baselines[3].fullEffort'
        },
        ...
    ]
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isBaselineEffortColumn](https://bryntum.com/docs/gantt/api/Gantt/column/BaselineEffortColumn#property-isBaselineEffortColumn)
Identifies an object as an instance of [BaselineEffortColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/BaselineEffortColumn) class, or subclass thereof.

[isBaselineEffortColumn](https://bryntum.com/docs/gantt/api/Gantt/column/BaselineEffortColumn#property-isBaselineEffortColumn-static)
Identifies an object as an instance of [BaselineEffortColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/BaselineEffortColumn) class, or subclass thereof.
