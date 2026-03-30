# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/crud/mixin/CrudManagerView.md

# [CrudManagerView](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/CrudManagerView)

Mixin to track Crud Manager requests to the server and mask the view during them. For masking, it uses the [loadMask](https://bryntum.com/docs/gantt/api/#Core/mixin/LoadMaskable#config-loadMask) and [syncMask](https://bryntum.com/docs/gantt/api/#Core/mixin/LoadMaskable#config-syncMask) properties.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCrudManagerView](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/CrudManagerView#property-isCrudManagerView)
Identifies an object as an instance of [CrudManagerView](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/CrudManagerView) class, or subclass thereof.

[isCrudManagerView](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/CrudManagerView#property-isCrudManagerView-static)
Identifies an object as an instance of [CrudManagerView](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/CrudManagerView) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[applySyncMask](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/CrudManagerView#function-applySyncMask)
Applies the [syncMask](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/CrudManagerView#config-syncMask) as the [mask](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-masked) for this widget.

[bindCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/CrudManagerView#function-bindCrudManager)
Hooks up crud manager listeners
