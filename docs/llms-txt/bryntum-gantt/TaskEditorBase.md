# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/TaskEditorBase.md

# [TaskEditorBase](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase)

Abstract base class for Scheduler and Gantt task editors

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[durationDisplayPrecision](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase#config-durationDisplayPrecision)
The decimal precision to use for Duration field / columns, normally provided by the owning Scheduler´s [durationDisplayPrecision](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerPro#config-durationDisplayPrecision)

[calculateMask](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase#config-calculateMask)
A message to be shown when Engine is performing task scheduling. Disabled by default.

Localizable text is defined in the `TaskEditorBase.calculateMask` locale key.

[calculateMaskDelay](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase#config-calculateMaskDelay)
A delay before the [mask](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/TaskEditorBase#config-calculateMask) becomes visible. This config is needed to avoid UI blinking when calculating is relatively fast.

Note, the mask is applied immediately and blocks the content anyway. However, if the delay is set, it will be transparent. If `null`, the mask is visible immediately.

[dependencyIdField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase#config-dependencyIdField)
A task field (id, wbsCode, sequenceNumber, etc.) that will be used when displaying and editing linked tasks. Defaults to Gantt `dependencyIdField`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskEditorBase](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase#property-isTaskEditorBase)
Identifies an object as an instance of [TaskEditorBase](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/TaskEditorBase) class, or subclass thereof.

[isTaskEditorBase](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase#property-isTaskEditorBase-static)
Identifies an object as an instance of [TaskEditorBase](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/TaskEditorBase) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[loadEvent](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/TaskEditorBase#function-loadEvent)
Loads a task model into the editor
