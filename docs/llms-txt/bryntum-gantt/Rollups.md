# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/Rollups.md

# [Rollups](https://bryntum.com/docs/gantt/api/Gantt/feature/Rollups)

If the task's [rollup](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-rollup) data field is set to `true`, it displays a small bar or diamond below its summary task in the timeline. Each of the rollup elements show a tooltip when hovering it with details of the task. The tooltip content is customizable, see [template](https://bryntum.com/docs/gantt/api/#Gantt/feature/Rollups#config-template) config for details.

To edit the rollup data field, use [RollupColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/RollupColumn) or a checkbox on Advanced tab of [TaskEditor](https://bryntum.com/docs/gantt/api/#Gantt/widget/TaskEditor).

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[rollupToAllParents](https://bryntum.com/docs/gantt/api/Gantt/feature/Rollups#config-rollupToAllParents)
Set to true to roll up tasks to all parents and grandparents.

[template](https://bryntum.com/docs/gantt/api/Gantt/feature/Rollups#config-template)
Template (a function accepting event data and returning a string) used to display info in the tooltip. The template will be called with an object as with fields as detailed below

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRollups](https://bryntum.com/docs/gantt/api/Gantt/feature/Rollups#property-isRollups)
Identifies an object as an instance of [Rollups](https://bryntum.com/docs/gantt/api/#Gantt/feature/Rollups) class, or subclass thereof.

[isRollups](https://bryntum.com/docs/gantt/api/Gantt/feature/Rollups#property-isRollups-static)
Identifies an object as an instance of [Rollups](https://bryntum.com/docs/gantt/api/#Gantt/feature/Rollups) class, or subclass thereof.
