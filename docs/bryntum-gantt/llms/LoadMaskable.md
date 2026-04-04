# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/LoadMaskable.md

# [LoadMaskable](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable)

Simple mixin for load masking configs and helper methods.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[loadMaskDefaults](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#config-loadMaskDefaults)
A [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) config object to adjust the [maskDefaults](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-maskDefaults) when data is loading. The message and optional configuration from the [loadMask](https://bryntum.com/docs/gantt/api/#Core/mixin/LoadMaskable#config-loadMask) config take priority over these options, just as they do for `maskDefaults`, respectively.

The final mask configuration for a load mask is as if the following were applied:

```
 Object.assign({},
     widget.maskDefaults,
     widget.loadMaskDefaults,
     widget.loadMask);
```

[loadMaskError](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#config-loadMaskError)
A [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) config object to adjust the [maskDefaults](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-maskDefaults) when an error occurs loading data.

Set to `false` to disable showing data loading error mask.

The final mask configuration for an error mask is as if the following were applied:

```
 Object.assign({},
     widget.maskDefaults,
     widget.loadMaskDefaults,
     widget.loadMaskError,
     errorMessage);
```

[loadMask](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#config-loadMask)
A [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) config object, or a message to be shown when a store is performing a remote operation, or Crud Manager is loading data from the sever. Set to `null` to disable default load mask.

[syncMask](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#config-syncMask)
A [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) config object, or a message to be shown when Crud Manager is persisting changes on the server. Set to `null` to disable default sync mask.

This config is similar to [loadMask](https://bryntum.com/docs/gantt/api/#Core/mixin/LoadMaskable#config-loadMask) but designed for saving data.

To create a custom sync mask need to subscribe to the Crud Manager events and show [Mask](https://bryntum.com/docs/gantt/api/#Core/widget/Mask) on `beforeSend` and hide it on `requestDone` and `requestFail`.

To create a custom sync mask, set this config to `null` and subscribe to the CrudManager's events to show or hide the [mask](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-masked) as desired.

```
 widget.crudManager.on({
     loadStart() {
         widget.masked = {
             text : 'Data is loading...'
         };
     },
     load() {
         widget.masked = null;
     },
     loadCanceled() {
         widget.masked = null;
     },
     syncStart() {
         widget.masked = null;
     },
     sync() {
         widget.masked = null;
     },
     syncCanceled() {
         widget.masked = null;
     },
     requestFail({ response }) {
         widget.masked.error = response.message || 'Sync failed';
     }
 });

 store.load();
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isLoadMaskable](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#property-isLoadMaskable)
Identifies an object as an instance of [LoadMaskable](https://bryntum.com/docs/gantt/api/#Core/mixin/LoadMaskable) class, or subclass thereof.

[isLoadMaskable](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#property-isLoadMaskable-static)
Identifies an object as an instance of [LoadMaskable](https://bryntum.com/docs/gantt/api/#Core/mixin/LoadMaskable) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[applyLoadMask](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#function-applyLoadMask)
Applies the [loadMask](https://bryntum.com/docs/gantt/api/#Core/mixin/LoadMaskable#config-loadMask) as the [mask](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-masked) for this widget.

[applyMaskError](https://bryntum.com/docs/gantt/api/Core/mixin/LoadMaskable#function-applyMaskError)
Updates the current [mask](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-masked) for this widget to present the specified `error`.
