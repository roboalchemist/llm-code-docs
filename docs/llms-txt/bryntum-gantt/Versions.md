# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/Versions.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/Versions.md

# [Versions](https://bryntum.com/docs/gantt/api/Gantt/feature/Versions)

Captures versions (snapshots) of the active project, including a detailed log of the changes new in each version.

When active, the feature monitors the project for changes and appends them to the changelog. When a version is captured, the version will consist of a complete snapshot of the project data at the time of the capture, in addition to the list of changes in the changelog that have occurred since the last version was captured.

For information about the data structure representing a version and how to persist it, see [VersionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/VersionModel).

For information about the data structures representing the changelog and how to persist them, see [ChangeLogTransactionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogTransactionModel).

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

```
const gantt = new Gantt({
    features : {
        versions : true
    }
});
```

To display versions and their changes, use a [VersionGrid](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/VersionGrid) configured with a [ProjectModel](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel).

See also:

* [VersionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/VersionModel) A stored version of a ProjectModel, captured at a point in time, with change log
* [ChangeLogTransactionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogTransactionModel) The set of add/remove/update actions that occurred in response to a user action
* [VersionGrid](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/VersionGrid) Widget for displaying a project's versions and changes

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[knownBaseTypes](https://bryntum.com/docs/gantt/api/Gantt/feature/Versions#config-knownBaseTypes)
The set of Model types whose subtypes should be recorded as the base type in the change log. For example, by default if a subclassed TaskModelEx exists and an instance of one is updated, it will be recorded in the changelog as a TaskModel.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isVersions](https://bryntum.com/docs/gantt/api/Gantt/feature/Versions#property-isVersions)
Identifies an object as an instance of [Versions](https://bryntum.com/docs/gantt/api/#Gantt/feature/Versions) class, or subclass thereof.

[isVersions](https://bryntum.com/docs/gantt/api/Gantt/feature/Versions#property-isVersions-static)
Identifies an object as an instance of [Versions](https://bryntum.com/docs/gantt/api/#Gantt/feature/Versions) class, or subclass thereof.
