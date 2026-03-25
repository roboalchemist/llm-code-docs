# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/ResourceModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/ResourceModel.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/model/ResourceModel.md

# [ResourceModel](https://bryntum.com/docs/gantt/api/Gantt/model/ResourceModel)

This class represents a single resource in your Gantt project.

If you want to add or change some fields, describing resources - subclass this class:

```
class MyResourceModel extends ResourceModel {

  static get fields() {
    return [
      { name: 'company', type: 'string' }
    ]
  }
}
```

See also: [AssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceModel](https://bryntum.com/docs/gantt/api/Gantt/model/ResourceModel#property-isResourceModel)
Identifies an object as an instance of [ResourceModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel) class, or subclass thereof.

[isResourceModel](https://bryntum.com/docs/gantt/api/Gantt/model/ResourceModel#property-isResourceModel-static)
Identifies an object as an instance of [ResourceModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ResourceModel) class, or subclass thereof.

[events](https://bryntum.com/docs/gantt/api/Gantt/model/ResourceModel#property-events)
Get associated tasks
