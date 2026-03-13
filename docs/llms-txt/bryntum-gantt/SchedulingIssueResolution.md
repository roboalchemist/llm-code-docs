# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/view/mixin/SchedulingIssueResolution.md

# [SchedulingIssueResolution](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulingIssueResolution)

This is a mixin, adding ability to track project scheduling issues (scheduling conflicts, cycles and calendar misconfigurations) and displaying a special popup allowing user to handle them.

The mixin basically add listeners to the project [schedulingConflict](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel#event-schedulingConflict), [cycle](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel#event-cycle) and [emptyCalendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel#event-emptyCalendar) events and shows a popup depending on the case:

* [SchedulingIssueResolutionPopup](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingIssueResolutionPopup) for _scheduling conflicts_ and _calendar misconfigurations_.
* [CycleResolutionPopup](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CycleResolutionPopup) for _scheduling cycles_.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[schedulingIssueResolutionPopupClass](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulingIssueResolution#config-schedulingIssueResolutionPopupClass)
Class implementing the popup resolving _scheduling conflicts_ and _calendar misconfigurations_.

Use this to provide a custom popup for the above cases.

[cycleResolutionPopupClass](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulingIssueResolution#config-cycleResolutionPopupClass)
Class implementing the popup resolving _scheduling cycles_.

Use this to provide a custom popup for that case.

[displaySchedulingIssueResolutionPopup](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulingIssueResolution#config-displaySchedulingIssueResolutionPopup)
Set to `true` to display special popups allowing user to resolve [scheduling conflicts](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingIssueResolutionPopup), [cycles](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CycleResolutionPopup) or calendar misconfigurations. The popup will suggest user ways to resolve the corresponding case.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulingIssueResolution](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulingIssueResolution#property-isSchedulingIssueResolution)
Identifies an object as an instance of [SchedulingIssueResolution](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/SchedulingIssueResolution) class, or subclass thereof.

[isSchedulingIssueResolution](https://bryntum.com/docs/gantt/api/SchedulerPro/view/mixin/SchedulingIssueResolution#property-isSchedulingIssueResolution-static)
Identifies an object as an instance of [SchedulingIssueResolution](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/mixin/SchedulingIssueResolution) class, or subclass thereof.
