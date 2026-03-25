# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/FieldContainer.md

# [FieldContainer](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer)

This widget is created when using the [container](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-container) config on fields.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[animation](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#config-animation)
An animation config object to use when expanding or collapsing the field's [container](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-container).

[collapsed](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#config-collapsed)
Controls whether the field is collapsed (that is, the field's [container](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-container) is hidden).

[collapser](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#config-collapser)
The animator performing the field's currently running expand or collapse animation.

[syncableConfigs](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#config-syncableConfigs)
A mapping object for config properties of the items in the [container](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-container). The keys are the config names and the values are functions that compute the config value when passed the field instance.

For example, this is the default:

```
     syncableConfigs : {
         disabled : field => field.disabled
     }
```

This indicates that the config property named with the key ('disabled') should be assigned to the result of the function assigned to that key (`field => field.disabled`). In other words, when the field is [disabled](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-disabled), all of the field's items should also be disabled.

[syncConfigTriggers](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#config-syncConfigTriggers)
This object holds truthy values for each config property that, when modified, should trigger a sync of this field's items as defined in [syncableConfigs](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer#config-syncableConfigs).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFieldContainer](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#property-isFieldContainer)
Identifies an object as an instance of [FieldContainer](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer) class, or subclass thereof.

[isFieldContainer](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#property-isFieldContainer-static)
Identifies an object as an instance of [FieldContainer](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer) class, or subclass thereof.

[collapsing](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#property-collapsing)
This property is `true` if the field container is currently collapsing.

[collapsingExpanding](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#property-collapsingExpanding)
This property is `true` if the field container is currently either collapsing or expanding.

[expanding](https://bryntum.com/docs/gantt/api/Core/widget/FieldContainer#property-expanding)
This property is `true` if the field container is currently expanding.
