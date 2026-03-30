# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/data/ResourceUtilizationStore.md

# [ResourceUtilizationStore](https://bryntum.com/docs/gantt/api/SchedulerPro/data/ResourceUtilizationStore)

A store representing [ResourceUtilization](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/ResourceUtilization) view records. This store accepts a model class inheriting from [ResourceUtilizationModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceUtilizationModel).

The store is a tree of nodes representing resources on the root level with sub-nodes representing corresponding resource assignments. The store tracks changes made in the [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/ResourceUtilizationStore#config-project) stores and rebuilds its content automatically. Thus the project config is mandatory and has to be provided.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/data/ResourceUtilizationStore#config-project)
Project instance to retrieve resources and assignments data from.

[combineTimePhasedAssignments](https://bryntum.com/docs/gantt/api/SchedulerPro/data/ResourceUtilizationStore#config-combineTimePhasedAssignments)
Provide `true` to combine multiple time-phased assignments of a resource to a task into a single record

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceUtilizationStore](https://bryntum.com/docs/gantt/api/SchedulerPro/data/ResourceUtilizationStore#property-isResourceUtilizationStore)
Identifies an object as an instance of [ResourceUtilizationStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/ResourceUtilizationStore) class, or subclass thereof.

[isResourceUtilizationStore](https://bryntum.com/docs/gantt/api/SchedulerPro/data/ResourceUtilizationStore#property-isResourceUtilizationStore-static)
Identifies an object as an instance of [ResourceUtilizationStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/ResourceUtilizationStore) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[fillFromProject](https://bryntum.com/docs/gantt/api/SchedulerPro/data/ResourceUtilizationStore#event-fillFromProject)
Fires when store completes synchronization with original (Event/Resource/Assignment) stores
