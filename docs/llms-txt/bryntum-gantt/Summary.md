# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/Summary.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Summary.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/Summary.md

# [Summary](https://bryntum.com/docs/gantt/api/Gantt/feature/Summary)

A feature displaying a summary bar in the grid footer.

Summaries in the locked grid
----------------------------

For regular columns in the locked section - specify type of summary on columns, available types are:

Type

Description

`sum`

Sum of all values in the column

`add`

Alias for sum

`count`

Number of rows

`countNotEmpty`

Number of rows containing a value

`average`

Average of all values in the column

`function`

A custom function, used with store.reduce. Should take arguments (sum, record)

Columns can also specify a [summaryRenderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-summaryRenderer) to format the calculated sum.

Summaries in the time axis grid
-------------------------------

To output summaries in the ticks of the time axis summary bar, either provide a [renderer](https://bryntum.com/docs/gantt/api/#Gantt/feature/Summary#config-renderer) or use [summaries](https://bryntum.com/docs/gantt/api/#Gantt/feature/Summary#config-summaries). The `renderer` method provides the current tick `startDate` and `endDate` which you can use to output the data you want to present in each summary cell.

```
features : {
    summary     : {
        // Find all intersecting task and render the count in each cell
        renderer: ({ taskStore, startDate, endDate }) => {
            const intersectingTasks = taskStore.query(task =>
                // Gantt by default renders tasks as early as possible, if loaded with un-normalized data there
                // might not be any start and end dates calculated yet
                task.isScheduled &&
                // Find tasks that intersect the current tick
                DateHelper.intersectSpans(task.startDate, task.endDate, startDate, endDate)
            );

            return intersectingTasks.length;
        }
    }
}
```

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[summaries](https://bryntum.com/docs/gantt/api/Gantt/feature/Summary#config-summaries)
Array of summary configs which consists of a label and a [renderer](https://bryntum.com/docs/gantt/api/#Gantt/feature/Summary#config-renderer) function

```
new Gantt({
    features : {
        summary : {
            summaries : [
                {
                    label : 'Label',
                    renderer : ({ startDate, endDate, taskStore }) => {
                        // return display value
                        returns '<div>Renderer output</div>';
                    }
                }
            ]
        }
    }
});
```

[renderer](https://bryntum.com/docs/gantt/api/Gantt/feature/Summary#config-renderer)
Renderer function for a single time axis tick. Should calculate a sum and return HTML as a result.

```
new Gantt({
    features : {
        summary : {
            renderer : ({ startDate, endDate, taskStore }) => {
                // return display value
                returns '<div>Renderer output</div>';
            }
        }
    }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSummary](https://bryntum.com/docs/gantt/api/Gantt/feature/Summary#property-isSummary)
Identifies an object as an instance of [Summary](https://bryntum.com/docs/gantt/api/#Gantt/feature/Summary) class, or subclass thereof.

[isSummary](https://bryntum.com/docs/gantt/api/Gantt/feature/Summary#property-isSummary-static)
Identifies an object as an instance of [Summary](https://bryntum.com/docs/gantt/api/#Gantt/feature/Summary) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[updateTimelineSummaries](https://bryntum.com/docs/gantt/api/Gantt/feature/Summary#function-updateTimelineSummaries)
Updates summaries.

## Typedefs

Typedefs are type definitions for the class

[GanttSummaryOptions](https://bryntum.com/docs/gantt/api/Gantt/feature/Summary#typedef-GanttSummaryOptions)
Describes a summary level for the time axis in Gantt
