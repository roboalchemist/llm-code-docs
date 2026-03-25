# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerRegions.md

# [SchedulerRegions](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerRegions)

Functions to get regions (bounding boxes) for scheduler, events etc.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerRegions](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerRegions#property-isSchedulerRegions)
Identifies an object as an instance of [SchedulerRegions](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerRegions) class, or subclass thereof.

[isSchedulerRegions](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerRegions#property-isSchedulerRegions-static)
Identifies an object as an instance of [SchedulerRegions](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerRegions) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getScheduleRegion](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerRegions#function-getScheduleRegion)
Gets the region represented by the schedule and optionally only for a single resource. The view will ask the scheduler for the resource availability by calling getResourceAvailability. By overriding that method you can constrain events differently for different resources.

[getResourceRegion](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerRegions#function-getResourceRegion)
Gets the region, relative to the timeline view element, representing the passed resource and optionally just for a certain date interval.

[getResourceEventBox](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerRegions#function-getResourceEventBox)
Get the region for a specified resources specified event.

[getItemBox](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerRegions#function-getItemBox)
Gets box for displayed item designated by the record. If several boxes are displayed for the given item then the method returns all of them. Box coordinates are in view coordinate system.

Boxes outside scheduling view timeaxis timespan and inside collapsed rows (if row defining store is a tree store) will not be returned. Boxes outside scheduling view vertical visible area (i.e. boxes above currently visible top row or below currently visible bottom row) will be calculated approximately.
