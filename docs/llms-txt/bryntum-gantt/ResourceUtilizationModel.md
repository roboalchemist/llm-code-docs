# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/ResourceUtilizationModel.md

# [ResourceUtilizationModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/ResourceUtilizationModel)

A model representing a [ResourceUtilization](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization) view row. The view rows are of two possible types **resources** and **assignments**. The model wraps either a resource or an assignment model. And each wrapped resource keeps its corresponding wrapped assignments as its **children**.

**NOTE:** You don't normally need to construct this class instances. The view does that automatically by processing the project resources and assignments, wrapping them with this model instances and putting them to its [store](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization#property-store).

The wrapped model is provided to [origin](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceUtilizationModel#config-origin) config and can be retrieved from it:

```
// get the real resource representing the first row of the view
resourceUtilizationView.store.first.origin
```

## Fields

Fields belong to a Model class and define the Model data structure

[name](https://bryntum.com/docs/gantt/api/SchedulerPro/model/ResourceUtilizationModel#field-name)
Name of the represented resource or the assigned event. If the model represents an assignment the field value is automatically set to the assigned event [name](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-name).

[iconCls](https://bryntum.com/docs/gantt/api/SchedulerPro/model/ResourceUtilizationModel#field-iconCls)
Icon for the corresponding row. If the model represents an assignment the field value is automatically set to the assigned event [iconCls](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-iconCls).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[origin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/ResourceUtilizationModel#config-origin)
A resource or an assignment wrapped by this model.

```
// get the real resource representing the first row of the view
resourceUtilizationView.store.first.origin
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceUtilizationModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/ResourceUtilizationModel#property-isResourceUtilizationModel)
Identifies an object as an instance of [ResourceUtilizationModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceUtilizationModel) class, or subclass thereof.

[isResourceUtilizationModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/ResourceUtilizationModel#property-isResourceUtilizationModel-static)
Identifies an object as an instance of [ResourceUtilizationModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceUtilizationModel) class, or subclass thereof.

[origin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/ResourceUtilizationModel#property-origin)
A resource or an assignment wrapped by this model.

```
// get the real resource representing the first row of the view
resourceUtilizationView.store.first.origin
```
