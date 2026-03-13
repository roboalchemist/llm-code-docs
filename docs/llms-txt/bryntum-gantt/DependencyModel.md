# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/DependencyModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/DependencyModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/model/DependencyModel.md

# [DependencyModel](https://bryntum.com/docs/gantt/api/Gantt/model/DependencyModel)

This class represents a single dependency between the tasks in your Gantt project.

Subclassing the Dependency class
--------------------------------

The name of any field in data can be customized in the subclass, see the example below.

```
class MyDependencyModel extends DependencyModel {
  static get fields() {
    return [
      { name: 'to', dataSource : 'targetId' },
      { name: 'from', dataSource : 'sourceId' }
    ];
  }
}
```

## Fields

Fields belong to a Model class and define the Model data structure

[fromTask](https://bryntum.com/docs/gantt/api/Gantt/model/DependencyModel#field-fromTask)
The origin task of this dependency.

Accepts multiple formats but always returns an [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel).

**NOTE:** This is not a proper field but rather an alias, it will be serialized but cannot be remapped. If you need to remap, consider using [from](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel#field-from) instead.

[toTask](https://bryntum.com/docs/gantt/api/Gantt/model/DependencyModel#field-toTask)
The destination task of this dependency.

Accepts multiple formats but always returns an [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel).

**NOTE:** This is not a proper field but rather an alias, it will be serialized but cannot be remapped. If you need to remap, consider using [to](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel#field-to) instead.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyModel](https://bryntum.com/docs/gantt/api/Gantt/model/DependencyModel#property-isDependencyModel)
Identifies an object as an instance of [DependencyModel](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel) class, or subclass thereof.

[isDependencyModel](https://bryntum.com/docs/gantt/api/Gantt/model/DependencyModel#property-isDependencyModel-static)
Identifies an object as an instance of [DependencyModel](https://bryntum.com/docs/gantt/api/#Gantt/model/DependencyModel) class, or subclass thereof.
