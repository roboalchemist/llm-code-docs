# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/mixin/ProjectProgressMixin.md

# [ProjectProgressMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/ProjectProgressMixin)

This is a mixin that tracks the progress of project calculations, either as a progress bar in the time axis header or in a mask.

Defaults to displaying a progress bar for projects that use delayed calculations to enable early rendering and to a mask for those that do not (which requires configuring the project with `enableProgressNotifications : true`). Configurable using the [projectProgressReporting](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/ProjectProgressMixin#config-projectProgressReporting) config.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[projectProgressReporting](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/ProjectProgressMixin#config-projectProgressReporting)
Accepts the following values:

* 'auto' - Auto selects 'progressbar' or 'mask' depending on projects configuration
* 'progressbar' - Renders a thin progress bar to the time axis header
* 'mask' - Uses a mask to display progress
* null - Do not display progress

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectProgressMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/ProjectProgressMixin#property-isProjectProgressMixin)
Identifies an object as an instance of [ProjectProgressMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/ProjectProgressMixin) class, or subclass thereof.

[isProjectProgressMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/ProjectProgressMixin#property-isProjectProgressMixin-static)
Identifies an object as an instance of [ProjectProgressMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/ProjectProgressMixin) class, or subclass thereof.
