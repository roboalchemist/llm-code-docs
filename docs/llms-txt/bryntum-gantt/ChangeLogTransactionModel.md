# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/changelog/ChangeLogTransactionModel.md

# [ChangeLogTransactionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/changelog/ChangeLogTransactionModel)

Represents a set of changes made as a result of a single user action. Changelog transactions may optionally be associated with a single VersionModel.

In normal usage, the Versions feature will capture one ChangeLogTransactionModel as a result of a single user action, for example, dragging a task on the timeline. This transaction will contain multiple [ChangeLogAction](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogAction)s representing the various effects that dragging a task can have - changes to start and end dates, updates to related dependent tasks, and so on.

Changelog transactions can be customized by extending a new model from `ChangeLogTransactionModel`. For an example, see the Gantt versions demo.

Individual changes making up a transaction are stored in the [actions](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogTransactionModel#field-actions) field.

Refer to [Versions](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/Versions) for more information about versioning.

## Fields

Fields belong to a Model class and define the Model data structure

[versionId](https://bryntum.com/docs/gantt/api/SchedulerPro/model/changelog/ChangeLogTransactionModel#field-versionId)
The ID of the version to which this transaction belongs, or null if the transaction is not yet associated with any version.

[actions](https://bryntum.com/docs/gantt/api/SchedulerPro/model/changelog/ChangeLogTransactionModel#field-actions)
The [ChangeLogAction](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogAction)s that this transaction comprises.

[occurredAt](https://bryntum.com/docs/gantt/api/SchedulerPro/model/changelog/ChangeLogTransactionModel#field-occurredAt)
The date and time when the transaction started.

[description](https://bryntum.com/docs/gantt/api/SchedulerPro/model/changelog/ChangeLogTransactionModel#field-description)
An optional, custom text description of the transaction.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChangeLogTransactionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/changelog/ChangeLogTransactionModel#property-isChangeLogTransactionModel)
Identifies an object as an instance of [ChangeLogTransactionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogTransactionModel) class, or subclass thereof.

[isChangeLogTransactionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/changelog/ChangeLogTransactionModel#property-isChangeLogTransactionModel-static)
Identifies an object as an instance of [ChangeLogTransactionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/changelog/ChangeLogTransactionModel) class, or subclass thereof.
