# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/TimeAxisBase.md

# [TimeAxisBase](https://bryntum.com/docs/gantt/api/Scheduler/view/TimeAxisBase)

Base class for HorizontalTimeAxis and VerticalTimeAxis. Contains shared functionality to only render ticks in view, should not be used directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[compactCellWidthThreshold](https://bryntum.com/docs/gantt/api/Scheduler/view/TimeAxisBase#config-compactCellWidthThreshold)
The minimum width for a bottom row header cell to be considered 'compact', which adds a special CSS class to the row (for special styling). Copied from Scheduler/Gantt.

[sizeProperty](https://bryntum.com/docs/gantt/api/Scheduler/view/TimeAxisBase#config-sizeProperty)
Style property to use as cell size. Either width or height depending on orientation

[positionProperty](https://bryntum.com/docs/gantt/api/Scheduler/view/TimeAxisBase#config-positionProperty)
Style property to use as cells position. Either left or top depending on orientation

## Functions

Functions are methods available for calling on the class

[refresh](https://bryntum.com/docs/gantt/api/Scheduler/view/TimeAxisBase#function-refresh)
Refresh the UI
