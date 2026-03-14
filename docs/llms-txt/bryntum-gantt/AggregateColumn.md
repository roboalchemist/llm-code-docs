# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/AggregateColumn.md

# [AggregateColumn](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn)

A column, which, when used as part of a [TreeGrid](https://bryntum.com/docs/gantt/api/#Grid/view/TreeGrid), aggregates the values of this column's descendants using a configured function which defaults to `sum`. The aggregate value is re-calculated after any change to the data, and if you want aggregate values to be change-tracked, please set [includeParentInChangeSet](https://bryntum.com/docs/gantt/api/#Grid/column/AggregateColumn#config-includeParentInChangeSet) to true.

Default editor depends on the data field type. If it is a number, default editor is a [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField). Otherwise Default editor is a [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField).

```
const grid = new TreeGrid({
    // Custom aggregation handler.
    // For test purposes, this just does "sum"
    myAggregator(...values) {
        let result = 0;

        for (let i = 0, { length } = values; i < length; i++) {
            result += parseInt(args[i], 10);
        }
        return result;
    },
    columns : [
        { field : 'name', text : 'Name' },

        // Will sum the ages of leaf nodes. This is the default.
        { type : 'aggregate', field : 'age', text : 'Age', renderer : ({ value }) => `<b>${value}<b>` },

        // Will use AggregateColumn's built-in avg of scores of leaf nodes
        { type : 'aggregate', field : 'score', text : 'Score', function : 'avg' },

        // Will use the grid's myAggregator function
        { type : 'aggregate', field : 'revenue', text : 'Revenue', function : 'up.myAggregator' },
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[function](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#config-function)
Math Function name, or function name prepended by `"up."` that is resolvable in an ancestor component (such as the owning Grid, or a height Container), or a function to use to aggregate child record values for this column, or a function.

This Column is provided with a `sum` and `avg` function. The default function is `sum` which is used for the aggregation.

The function is passed a set of child node values, each value in a separate argument and should return a single value based upon the value set passed.

[includeParentInChangeSet](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#config-includeParentInChangeSet)
Set to `true` to include changes to parent (aggregate) rows in the store's modification tracking.

[enableAggregation](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#config-enableAggregation)
Set to `false` to disable aggregates being calculated.

[includeFilteredOutRecords](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#config-includeFilteredOutRecords)
Set to `true` to include filtered out records in the aggregation.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAggregateColumn](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#property-isAggregateColumn)
Identifies an object as an instance of [AggregateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/AggregateColumn) class, or subclass thereof.

[isAggregateColumn](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#property-isAggregateColumn-static)
Identifies an object as an instance of [AggregateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/AggregateColumn) class, or subclass thereof.

[function](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#property-function)
Math Function name, or function name prepended by `"up."` that is resolvable in an ancestor component (such as the owning Grid, or a height Container), or a function to use to aggregate child record values for this column, or a function.

This Column is provided with a `sum` and `avg` function. The default function is `sum` which is used for the aggregation.

The function is passed a set of child node values, each value in a separate argument and should return a single value based upon the value set passed.

[includeParentInChangeSet](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#property-includeParentInChangeSet)
Set to `true` to include changes to parent (aggregate) rows in the store's modification tracking.

[enableAggregation](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#property-enableAggregation)
Set to `false` to disable aggregates being calculated.

[includeFilteredOutRecords](https://bryntum.com/docs/gantt/api/Grid/column/AggregateColumn#property-includeFilteredOutRecords)
Set to `true` to include filtered out records in the aggregation.
