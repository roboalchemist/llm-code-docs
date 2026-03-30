# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/crud/mixin/AbstractCrudManagerValidation.md

# [AbstractCrudManagerValidation](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/AbstractCrudManagerValidation)

Mixin proving responses validation API to Crud Manager.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[validateResponse](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/AbstractCrudManagerValidation#config-validateResponse)
This config validates the response structure for requests made by the Crud Manager. When `true`, the Crud Manager checks every parsed response structure for errors and if the response format is invalid, a warning is logged to the browser console.

The config is intended to help developers implementing backend integration.

[skipSuccessProperty](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/AbstractCrudManagerValidation#config-skipSuccessProperty)
When `true` treats parsed responses without `success` property as successful. In this mode a parsed response is treated as invalid if it has explicitly set `success : false`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAbstractCrudManagerValidation](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/AbstractCrudManagerValidation#property-isAbstractCrudManagerValidation)
Identifies an object as an instance of [AbstractCrudManagerValidation](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/AbstractCrudManagerValidation) class, or subclass thereof.

[isAbstractCrudManagerValidation](https://bryntum.com/docs/gantt/api/Scheduler/crud/mixin/AbstractCrudManagerValidation#property-isAbstractCrudManagerValidation-static)
Identifies an object as an instance of [AbstractCrudManagerValidation](https://bryntum.com/docs/gantt/api/#Scheduler/crud/mixin/AbstractCrudManagerValidation) class, or subclass thereof.
