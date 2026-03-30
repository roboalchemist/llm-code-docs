# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/mixin/TransactionalFeature.md

# [TransactionalFeature](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/TransactionalFeature)

Feature defining methods to lock the view for a time of a user action

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTransactionalFeature](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/TransactionalFeature#property-isTransactionalFeature)
Identifies an object as an instance of [TransactionalFeature](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/TransactionalFeature) class, or subclass thereof.

[isTransactionalFeature](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/TransactionalFeature#property-isTransactionalFeature-static)
Identifies an object as an instance of [TransactionalFeature](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/TransactionalFeature) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[captureFeatureTransaction](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/TransactionalFeature#function-captureFeatureTransaction)
Capturing transaction is a process of passing control over current revision boundaries from one feature to another. At the moment it is only used by the CellEdit feature which keeps revision open while new records are being created. We take the promise which unblocks the queue, store transaction id and raise a flag which tells this mixin to not actually start new or finish existing transaction. Rejection, however, cleans up the flag and unblocks the queue like it should. Workflow is like this:

```
const capture = feature1.captureFeatureTransaction
feature2.applyCapturedFeatureTransaction(capture);
```

[applyCapturedFeatureTransaction](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/TransactionalFeature#function-applyCapturedFeatureTransaction)
Applies captured feature transaction to pass control to the current feature
