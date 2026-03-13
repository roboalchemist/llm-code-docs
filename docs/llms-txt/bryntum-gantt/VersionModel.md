# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/VersionModel.md

# [VersionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/VersionModel)

Represents a snapshot of a [ProjectModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel) at a point in time. Each VersionModel has an associated set of [changes](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogTransactionModel) that describe the user-initiated modifications to the project that happened since the previous version was captured.

## Fields

Fields belong to a Model class and define the Model data structure

[name](https://bryntum.com/docs/gantt/api/SchedulerPro/model/VersionModel#field-name)
The name of the version. When an auto-saved version's `name` is `null`, the version description will return a default text description instead.

[isAutosave](https://bryntum.com/docs/gantt/api/SchedulerPro/model/VersionModel#field-isAutosave)
Whether this version was auto-saved.

[content](https://bryntum.com/docs/gantt/api/SchedulerPro/model/VersionModel#field-content)
A serializable object snapshot of the [ProjectModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel) at the point in time when the version was created.

Note that this field is not loaded from the backend by default, due to its size. The [Versions](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/Versions) feature manages loading the contents of this field on demand.

The format of this data should match that returned by [toJSON](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel#function-toJSON).

[savedAt](https://bryntum.com/docs/gantt/api/SchedulerPro/model/VersionModel#field-savedAt)
The timestamp when the version was created.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isVersionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/VersionModel#property-isVersionModel)
Identifies an object as an instance of [VersionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/VersionModel) class, or subclass thereof.

[isVersionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/VersionModel#property-isVersionModel-static)
Identifies an object as an instance of [VersionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/VersionModel) class, or subclass thereof.
