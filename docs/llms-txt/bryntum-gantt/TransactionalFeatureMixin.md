# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TransactionalFeatureMixin.md

# [TransactionalFeatureMixin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TransactionalFeatureMixin)

This mixin declares a common config to disable feature transactions in components which support scheduling engine: SchedulerPro and Gantt.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[enableTransactionalFeatures](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TransactionalFeatureMixin#config-enableTransactionalFeatures)
When true, some features will start a project transaction, blocking the project queue, suspending store events and preventing UI from updates. It behaves similar to [instantUpdate](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-instantUpdate) set to `false`. Set `false` to not use project queue.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTransactionalFeatureMixin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TransactionalFeatureMixin#property-isTransactionalFeatureMixin)
Identifies an object as an instance of [TransactionalFeatureMixin](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TransactionalFeatureMixin) class, or subclass thereof.

[isTransactionalFeatureMixin](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TransactionalFeatureMixin#property-isTransactionalFeatureMixin-static)
Identifies an object as an instance of [TransactionalFeatureMixin](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TransactionalFeatureMixin) class, or subclass thereof.

[transactionalFeaturesEnabled](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TransactionalFeatureMixin#property-transactionalFeaturesEnabled)
Returns `true` if queue is supported and enabled
