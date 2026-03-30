# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/ResourceAssignmentColumn.md

# [ResourceAssignmentColumn](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn)

Column allowing resource manipulation (assignment/unassignment/units changing) on a task. In the column cells, assignments are either shown as badges or avatars. To show avatars, set [showAvatars](https://bryntum.com/docs/gantt/api/#Gantt/column/ResourceAssignmentColumn#config-showAvatars) to `true`. When showing avatars there are two options for how to specify image paths:

* You may provide a [resourceImagePath](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-resourceImagePath) on your Gantt panel pointing to where resource images are located. Set the resource image filename in the `image` field of the resource data.
* And/or you may provide an `imageUrl` on your record, which then will take precedence when showing images.

If a resource has no name, or its image cannot be loaded, the resource initials are rendered. If the resource has an [eventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/ResourceModelMixin#field-eventColor) specified, it will be used as the background color of the initials.

Default editor is a [AssignmentField](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentField).

Customizing displayed elements
------------------------------

If [showAvatars](https://bryntum.com/docs/gantt/api/#Gantt/column/ResourceAssignmentColumn#config-showAvatars) is false, column will render resource name and utilization wrapped in a small element called _a chip_. Content of the chip can be customized. For example, if you don't want to see percent value, or want to display different resource name, you can specify an [itemTpl](https://bryntum.com/docs/gantt/api/#Gantt/column/ResourceAssignmentColumn#config-itemTpl) config. Please keep in mind that when you start editing the cell, chip will be rendered by the default editor. If you want chips to be consistent, you need to customize the editor too.

```
new Gantt({
    columns: [
        {
            type     : 'resourceassignment',
            itemTpl  : assignment => assignment.resourceName,
            editor   : {
                chipView : {
                    itemTpl : assignment => assignment.resourceName
                }
            }
        }
    ]
});
```

Subscribing to avatar click events
----------------------------------

The owning Gantt instance triggers a [resourceAssignmentClick](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#event-resourceAssignmentClick)\` event when a resource avatar or chip is clicked.

```
new Gantt({
    columns: [
        {
            type         : 'resourceassignment',
            showAvatars : true
        }
    ],
    listeners : {
         resourceAssignmentClick({ taskRecord, resourceRecord, event }) {
             console.log(resourceRecord.name);
         }
     }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showAvatars](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#config-showAvatars)
True to show a resource avatar for every assignment. Note that you also have to provide a [resourceImagePath](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-resourceImagePath) for where to load images from. And/or you may provide an `imageUrl` on your record, which then will take precedence when showing images.

[itemTpl](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#config-itemTpl)
A function which produces the content to put in the resource assignment cell. May be overridden in subclasses, or injected into the column to customize the Chip content.

Defaults to returning `${assignment.resourceName} ${assignment.units}%`

[avatarTooltipTemplate](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#config-avatarTooltipTemplate)
A function which receives data about the resource and returns a html string to be displayed in the tooltip.

```
const gantt = new Gantt({
    columns : [
         {
             type          : 'resourceassignment',
             showAvatars : true,
             avatarTooltipTemplate({ resourceRecord }) {
                 return `<b>${resourceRecord.name}</b>`;
             }
         }
    ]
});
```

This function will be called with an object containing the fields below:

[showAllNames](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#config-showAllNames)
When `true`, the names of all overflowing resources are shown in the tooltip. When `false`, the number of overflowing resources is displayed instead. Only valid for last shown resource, if there are overflowing resources.

[enableResourceDragging](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#config-enableResourceDragging)
True to allow drag-drop of resource avatars between rows. Dropping a resource outside the resource assignment cells will unassign the resource.

[avatarTooltip](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#config-avatarTooltip)
A config object passed to the avatar [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip)

```
const gantt = new Gantt({
    columns : [
         {
             type          : 'resourceassignment',
             showAvatars : true,
             avatarTooltip : {
                 // Allow moving mouse over the tooltip
                 allowOver : true
             }
         }
    ]
});
```

This function will be called with an object containing the fields below:

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceAssignmentColumn](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-isResourceAssignmentColumn)
Identifies an object as an instance of [ResourceAssignmentColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ResourceAssignmentColumn) class, or subclass thereof.

[isResourceAssignmentColumn](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-isResourceAssignmentColumn-static)
Identifies an object as an instance of [ResourceAssignmentColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/ResourceAssignmentColumn) class, or subclass thereof.

[showAvatars](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-showAvatars)
True to show a resource avatar for every assignment. Note that you also have to provide a [resourceImagePath](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-resourceImagePath) for where to load images from. And/or you may provide an `imageUrl` on your record, which then will take precedence when showing images.

[itemTpl](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-itemTpl)
A function which produces the content to put in the resource assignment cell. May be overridden in subclasses, or injected into the column to customize the Chip content.

Defaults to returning `${assignment.resourceName} ${assignment.units}%`

[avatarTooltipTemplate](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-avatarTooltipTemplate)
A function which receives data about the resource and returns a html string to be displayed in the tooltip.

```
const gantt = new Gantt({
    columns : [
         {
             type          : 'resourceassignment',
             showAvatars : true,
             avatarTooltipTemplate({ resourceRecord }) {
                 return `<b>${resourceRecord.name}</b>`;
             }
         }
    ]
});
```

This function will be called with an object containing the fields below:

[showAllNames](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-showAllNames)
When `true`, the names of all overflowing resources are shown in the tooltip. When `false`, the number of overflowing resources is displayed instead. Only valid for last shown resource, if there are overflowing resources.

[enableResourceDragging](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-enableResourceDragging)
True to allow drag-drop of resource avatars between rows. Dropping a resource outside the resource assignment cells will unassign the resource.

[avatarTooltip](https://bryntum.com/docs/gantt/api/Gantt/column/ResourceAssignmentColumn#property-avatarTooltip)
A config object passed to the avatar [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip)

```
const gantt = new Gantt({
    columns : [
         {
             type          : 'resourceassignment',
             showAvatars : true,
             avatarTooltip : {
                 // Allow moving mouse over the tooltip
                 allowOver : true
             }
         }
    ]
});
```

This function will be called with an object containing the fields below:
