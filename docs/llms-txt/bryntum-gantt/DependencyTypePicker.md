# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/DependencyTypePicker.md

# [DependencyTypePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/DependencyTypePicker)

A combo box field used to select the link type for a [Dependency](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/DependencyModel) between two tasks.

Customize the picker to show only certain dependency types
----------------------------------------------------------

You can customize which dependency types to show in the picker by filtering the picker store. For example, to show only Finish-to-Start and Start-to-Start types:

```
 const dependencyTypePicker = new DependencyTypePicker({
    store : {
        filters : [{
            // Show only Finish-to-Start and Start-to-Start
            filterBy : record => record.id === DependencyModel.Type.EndToStart || record.id === DependencyModel.Type.StartToStart
        }]
    }
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[dependencyStore](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/DependencyTypePicker#config-dependencyStore)
The dependency store to use for filtering allowed types. If not provided, the picker will attempt to find it from its owner hierarchy.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyTypePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/DependencyTypePicker#property-isDependencyTypePicker)
Identifies an object as an instance of [DependencyTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/DependencyTypePicker) class, or subclass thereof.

[isDependencyTypePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/DependencyTypePicker#property-isDependencyTypePicker-static)
Identifies an object as an instance of [DependencyTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/DependencyTypePicker) class, or subclass thereof.

[allowedDependencyTypes](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/DependencyTypePicker#property-allowedDependencyTypes)
Returns the allowed dependency types from the dependency store.
