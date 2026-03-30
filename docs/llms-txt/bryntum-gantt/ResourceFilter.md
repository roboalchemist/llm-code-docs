# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/widget/ResourceFilter.md

# [ResourceFilter](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter)

A List which allows selection of resources to filter a specified eventStore to only show events for the selected resources.

Because this widget maintains a state that can be changed through the UI, it offers some of the API of an input field. It has a read only [value](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ResourceFilter#property-value) property, and it fires a [change](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ResourceFilter#event-change) event.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[eventStore](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#config-eventStore)
The [EventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore) to filter. Events for resources which are deselected in this List will be filtered out.

[multiSelect](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#config-multiSelect)
Configure as `false` to only allow selecting one resource at a time

[useResourceColor](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#config-useResourceColor)
Configure as `false` to not use the Resource\`s color field to style the checkbox

[masterFilter](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#config-masterFilter)
An optional filter function to apply when loading resources from the project's resource store. Defaults to loading all resources.

**This is called using this `ResourceFilter` as the `this` object.**

[filterResources](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#config-filterResources)
By default, deselecting list items filters only the [eventStore](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ResourceFilter#config-eventStore) so that events for the deselected resources are hidden from view. The `resourceStore` is **not** filtered.

Configure this as `true` to also filter the `resourceStore` so that deselected resources are also hidden from view (They will remain in this `List`)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceFilter](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#property-isResourceFilter)
Identifies an object as an instance of [ResourceFilter](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ResourceFilter) class, or subclass thereof.

[isResourceFilter](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#property-isResourceFilter-static)
Identifies an object as an instance of [ResourceFilter](https://bryntum.com/docs/gantt/api/#Scheduler/widget/ResourceFilter) class, or subclass thereof.

[multiSelect](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#property-multiSelect)
Configure as `false` to only allow selecting one resource at a time

[value](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#property-value)
An array encapsulating the currently selected resources.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[change](https://bryntum.com/docs/gantt/api/Scheduler/widget/ResourceFilter#event-change)
Fired when this widget's selection changes
