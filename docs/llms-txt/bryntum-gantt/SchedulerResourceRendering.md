# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerResourceRendering.md

# [SchedulerResourceRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering)

Configs and functions used for resource rendering and by the [ResourceInfoColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ResourceInfoColumn) class.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resourceMargin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#config-resourceMargin)
Control how much space to leave between the first event/last event and the resources edge (top/bottom margin within the resource row in horizontal mode, left/right margin within the resource column in vertical mode), in px. Defaults to the value of [barMargin](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-barMargin).

Can be configured per resource by setting [resource.resourceMargin](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-resourceMargin).

It's also possible to set different values for top/left and bottom/right by assigning an object to `resourceMargin` with `start` (margin top in horizontal mode, margin left in vertical mode) and `end` (margin bottom / margin right) properties:

```
scheduler = new Scheduler({
    resourceMargin : {
        start : 15,
        end   : 1
    }
});
```

[resourceColumns](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#config-resourceColumns)
A config object used to configure the resource columns in vertical mode. See [ResourceHeader](https://bryntum.com/docs/gantt/api/#Scheduler/view/ResourceHeader) for more details on available properties.

```
new Scheduler({
    resourceColumns : {
        columnWidth    : 100,
        fillWidth      : false, // this is required for columnWidth to work
        headerRenderer : ({ resourceRecord }) => `${resourceRecord.id} - ${resourceRecord.name}`
    }
})
```

[resourceImagePath](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#config-resourceImagePath)
Path to load resource images from. Used by the resource header in vertical mode and the [ResourceInfoColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/ResourceInfoColumn) in horizontal mode. Set this to display miniature images for each resource using their `image` or `imageUrl` fields.

* `image` represents image name inside the specified `resourceImagePath`,
* `imageUrl` represents fully qualified image URL.

If set and a resource has no `imageUrl` or `image` specified it will try show miniature using the resource's name with [resourceImageExtension](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerResourceRendering#config-resourceImageExtension) appended.

**NOTE**: The path should end with a `/`:

```
new Scheduler({
  resourceImagePath : 'images/resources/'
});
```

[defaultResourceImageName](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#config-defaultResourceImageName)
Generic resource image, used when provided `imageUrl` or `image` fields or path calculated from resource name are all invalid. If left blank, resource name initials will be shown when no image can be loaded.

[resourceImageExtension](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#config-resourceImageExtension)
Resource image extension, used when creating image path from resource name.

[resourceImages](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#config-resourceImages)
Convenience config to set both [resourceImagePath](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerResourceRendering#config-resourceImagePath) and [resourceImageExtension](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerResourceRendering#config-resourceImageExtension).

```
new Scheduler({
  resourceImages : {
    path      : 'images/resources/',
    extension : '.png'
  }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerResourceRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#property-isSchedulerResourceRendering)
Identifies an object as an instance of [SchedulerResourceRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerResourceRendering) class, or subclass thereof.

[isSchedulerResourceRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#property-isSchedulerResourceRendering-static)
Identifies an object as an instance of [SchedulerResourceRendering](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerResourceRendering) class, or subclass thereof.

[resourceMargin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#property-resourceMargin)
Control how much space to leave between the first event/last event and the resources edge (top/bottom margin within the resource row in horizontal mode, left/right margin within the resource column in vertical mode), in px. Defaults to the value of [barMargin](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-barMargin).

Can be configured per resource by setting [resource.resourceMargin](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-resourceMargin).

It's also possible to set different values for top/left and bottom/right by assigning an object to `resourceMargin` with `start` (margin top in horizontal mode, margin left in vertical mode) and `end` (margin bottom / margin right) properties:

```
scheduler = new Scheduler({
    resourceMargin : {
        start : 15,
        end   : 1
    }
});
```

[resourceColumns](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#property-resourceColumns)
Use it to manipulate resource column properties at runtime.

[resourceColumnWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerResourceRendering#property-resourceColumnWidth)
Get resource column width. Only applies to vertical mode. To set it, assign to `scheduler.resourceColumns.columnWidth`.
