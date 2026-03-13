# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/ResourceHeader.md

# [ResourceHeader](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader)

Header widget that renders resource column headers and acts as the interaction point for resource columns in vertical mode. Note that it uses virtual rendering and element reusage to gain performance, only headers in view are available in DOM. Because of this you should avoid direct element manipulation, any such changes can be discarded at any time.

By default, it displays resources `name` and also applies its `iconCls` if any, like this:

```
<i class="iconCls">name</i>
```

If Scheduler is configured with a [resourceImagePath](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-resourceImagePath) the header will render miniatures for the resources, using [imageUrl](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-imageUrl) or [image](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-image) with fallback to [name](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-name) + [resourceImageExtension](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-resourceImageExtension) for unset values.

The contents and styling of the resource cells in the header can be customized using [headerRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/ResourceHeader#config-headerRenderer):

```
new Scheduler({
    mode            : 'vertical',
    resourceColumns : {
        headerRenderer : ({ resourceRecord }) => `Hello ${resourceRecord.name}`
    }
}
```

The width of the resource columns is determined by the [columnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/view/ResourceHeader#config-columnWidth) config.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resourceStore](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#config-resourceStore)
Resource store used to render resource headers. Assigned from Scheduler.

[headerRenderer](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#config-headerRenderer)
Custom header renderer function. Can be used to manipulate the element config used to create the element for the header:

```
new Scheduler({
  resourceColumns : {
    headerRenderer({ elementConfig, resourceRecord }) {
      elementConfig.dataset.myExtraData = 'extra';
      elementConfig.style.fontWeight = 'bold';
    }
  }
});
```

See [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) for more information.

You should never modify any records inside this method.

Or as a template by returning HTML from the function:

```
new Scheduler({
  resourceColumns : {
    headerRenderer : ({ resourceRecord }) => `
      <div class="my-custom-template">
      ${resourceRecord.firstName} {resourceRecord.surname}
      </div>
    `
  }
});
```

When using \`headerRenderer\` no default internal markup is applied to the resource header cell, \`iconCls\` and [imageUrl](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-imageUrl) or [image](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-image) will have no effect unless you supply custom markup for them.

[showAvatars](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#config-showAvatars)
Set to `false` to render just the resource name, `true` to render an avatar (or initials if no image exists)

[fillWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#config-fillWidth)
Automatically resize resource columns to **fill** available width. Set to `false` to always respect the configured `columnWidth`.

This is ignored if _any_ resources are loaded with [columnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-columnWidth).

[fitWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#config-fitWidth)
Automatically resize resource columns to always **fit** available width.

This is ignored if _any_ resources are loaded with [columnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-columnWidth).

[columnWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#config-columnWidth)
Width for each resource column.

This is used for resources which are not are loaded with a [columnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-columnWidth). This config may be ignored if resources do not fill the view and [fillWidth](https://bryntum.com/docs/gantt/api/#Scheduler/view/ResourceHeader#config-fillWidth) is set to `true`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceHeader](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#property-isResourceHeader)
Identifies an object as an instance of [ResourceHeader](https://bryntum.com/docs/gantt/api/#Scheduler/view/ResourceHeader) class, or subclass thereof.

[isResourceHeader](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#property-isResourceHeader-static)
Identifies an object as an instance of [ResourceHeader](https://bryntum.com/docs/gantt/api/#Scheduler/view/ResourceHeader) class, or subclass thereof.

[fillWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#property-fillWidth)
Assign to toggle resource columns \*_fill_ mode. `true` means they will stretch (grow) to fill viewport, `false` that they will respect their configured `columnWidth`.

This is ignored if _any_ resources are loaded with [columnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-columnWidth).

[fitWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#property-fitWidth)
Assign to toggle resource columns \*_fit_ mode. `true` means they will grow or shrink to always fit viewport, `false` that they will respect their configured `columnWidth`.

This is ignored if _any_ resources are loaded with [columnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-columnWidth).

[columnWidth](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#property-columnWidth)
Width for each resource column.

This is used for resources which are not are loaded with a [columnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceModel#field-columnWidth). This config may be ignored if resources do not fill the view and [fillWidth](https://bryntum.com/docs/gantt/api/#Scheduler/view/ResourceHeader#config-fillWidth) is set to `true`.

[firstResource](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#property-firstResource)
An index of the first visible resource in vertical mode

[lastResource](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#property-lastResource)
An index of the last visible resource in vertical mode

## Functions

Functions are methods available for calling on the class

[refresh](https://bryntum.com/docs/gantt/api/Scheduler/view/ResourceHeader#function-refresh)
Refreshes the visible headers
