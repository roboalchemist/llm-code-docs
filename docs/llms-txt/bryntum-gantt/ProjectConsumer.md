# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/mixin/ProjectConsumer.md

# [ProjectConsumer](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer)

Creates a Project using any configured stores, and sets the stores configured into the project into the host object.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[project](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#config-project)
A [ProjectModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel) instance or a config object. The project holds all Scheduler data. Can be omitted in favor of individual store configs or [crudManager](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerStores#config-crudManager) config.

**Note:** In SchedulerPro the project is instance of SchedulerPro.model.ProjectModel class.

[destroyStores](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#config-destroyStores)
Configure as `true` to destroy the Project and stores when `this` is destroyed.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectConsumer](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#property-isProjectConsumer)
Identifies an object as an instance of [ProjectConsumer](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/ProjectConsumer) class, or subclass thereof.

[isProjectConsumer](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#property-isProjectConsumer-static)
Identifies an object as an instance of [ProjectConsumer](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/ProjectConsumer) class, or subclass thereof.

[project](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#property-project)
A [ProjectModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel) instance or a config object. The project holds all Scheduler data. Can be omitted in favor of individual store configs or [crudManager](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerStores#config-crudManager) config.

**Note:** In SchedulerPro the project is instance of SchedulerPro.model.ProjectModel class.

[isEngineReady](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#property-isEngineReady)
Returns `true` if engine is in a stable calculated state, `false` otherwise.

## Functions

Functions are methods available for calling on the class

[updateProject](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#function-updateProject)
Implement in subclass to take action when project is replaced.

**`super.updateProject(...arguments)` must be called first.**

[whenProjectReady](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#function-whenProjectReady)
Accepts a callback that will be called when the underlying project is ready (no commit pending and current commit finalized)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dataChange](https://bryntum.com/docs/gantt/api/Scheduler/data/mixin/ProjectConsumer#event-dataChange)
Fired when data in any of the projects stores changes.

Basically a relayed version of each store's own change event, decorated with which store it originates from. See the [store change event](https://bryntum.com/docs/gantt/api/#Core/data/Store#event-change) documentation for more information.
