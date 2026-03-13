# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/mixin/ProjectChangeHandlerMixin.md

# [ProjectChangeHandlerMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectChangeHandlerMixin)

This mixin allows syncing a changes object between projects. See [applyProjectChanges](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/ProjectChangeHandlerMixin#function-applyProjectChanges) for usage

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectChangeHandlerMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectChangeHandlerMixin#property-isProjectChangeHandlerMixin)
Identifies an object as an instance of [ProjectChangeHandlerMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/ProjectChangeHandlerMixin) class, or subclass thereof.

[isProjectChangeHandlerMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectChangeHandlerMixin#property-isProjectChangeHandlerMixin-static)
Identifies an object as an instance of [ProjectChangeHandlerMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/ProjectChangeHandlerMixin) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[applyProjectChanges](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectChangeHandlerMixin#function-applyProjectChanges)
Allows to apply changes from one project to another. For method to produce correct results, projects should be isomorphic - they should use same models and store configuration, also data in source and target projects should be identical before changes to the source project are made and applied to the target project. This method is meant to apply changes in real time - as source project is changed, changes should be applied to the target project before it is changed. When changes are applied all changes are committed and project is recalculated, which means target project won't have any local changes after.

Usage:

```
// Collect changes from first project
const { changes } = projectA;

// Apply changes to second project
await projectB.applyProjectChanges(changes);
```

This method will override local fields with values from the changes object and commit changed fields. It will keep changes in the project, if they are not present in the changes object.

When [autoSync](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#config-autoSync) is enabled, and client wants to apply changes without triggering a sync request, this method should be used instead of [applyChangeset](https://bryntum.com/docs/gantt/api/#Scheduler/crud/AbstractCrudManagerMixin#function-applyChangeset). It helps maintain current behavior while providing flexibility for scenarios where syncing is not required.
