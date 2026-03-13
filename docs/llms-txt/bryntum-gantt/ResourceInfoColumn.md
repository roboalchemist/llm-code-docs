# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/column/ResourceInfoColumn.md

# [ResourceInfoColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn)

Displays basic resource information. Defaults to showing an image + name + event count (all configurable).

If a resource has no image, you can either provide an icon using `iconCls` in the data (you then need to specify `image === false` in your data) or the resource initials will be shown. If you don't want to show any avatar at all, you can set `showAvatar` to false for the Resource record.

Be sure to specify [resourceImagePath](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-resourceImagePath) to instruct the column where to look for the images.

If an image fails to load or if a resource lacks an image, the resource name initials will be rendered. If the resource has an [eventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ResourceModelMixin#field-eventColor) specified, it will be used as the background color of the initials.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showImage](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#config-showImage)
Show image. Looks for image name in fields on the resource in the following order: 'imageUrl', 'image', 'name'. Set `showImage` to a field name to use a custom field. Set `Scheduler.resourceImagePath` to specify where to load images from. If no extension found, defaults to [resourceImageExtension](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-resourceImageExtension).

[showEventCount](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#config-showEventCount)
Show number of events assigned to the resource below the name.

[showMeta](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#config-showMeta)
A template string to render any extra information about the resource below the name

[showRole](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#config-showRole)
Show resource role below the name. Specify `true` to display data from the `role` field, or specify a field name to read this value from.

[autoScaleThreshold](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#config-autoScaleThreshold)
Specify 0 to prevent the column from adapting its content according to the used row height, or specify a threshold (row height) at which scaling should start.

[useNameAsImageName](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#config-useNameAsImageName)
Use the resource name as the image name when no `image` is specified on the resource.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceInfoColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-isResourceInfoColumn)
Identifies an object as an instance of [ResourceInfoColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ResourceInfoColumn) class, or subclass thereof.

[isResourceInfoColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-isResourceInfoColumn-static)
Identifies an object as an instance of [ResourceInfoColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ResourceInfoColumn) class, or subclass thereof.

[showImage](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-showImage)
Show image. Looks for image name in fields on the resource in the following order: 'imageUrl', 'image', 'name'. Set `showImage` to a field name to use a custom field. Set `Scheduler.resourceImagePath` to specify where to load images from. If no extension found, defaults to [resourceImageExtension](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-resourceImageExtension).

[showEventCount](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-showEventCount)
Show number of events assigned to the resource below the name.

[showMeta](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-showMeta)
A template string to render any extra information about the resource below the name

[showRole](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-showRole)
Show resource role below the name. Specify `true` to display data from the `role` field, or specify a field name to read this value from.

[autoScaleThreshold](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-autoScaleThreshold)
Specify 0 to prevent the column from adapting its content according to the used row height, or specify a threshold (row height) at which scaling should start.

[useNameAsImageName](https://bryntum.com/docs/gantt/api/Scheduler/column/ResourceInfoColumn#property-useNameAsImageName)
Use the resource name as the image name when no `image` is specified on the resource.
