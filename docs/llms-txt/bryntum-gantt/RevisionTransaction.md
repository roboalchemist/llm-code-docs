# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/stm/RevisionTransaction.md

# [RevisionTransaction](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction)

Transaction with additional metadata utilized by the Revisions feature

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[committed](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#config-committed)
Identifies if revision is temporary or not. Committed revisions get cleaned eventually, local revisions should be committed.

[conflictResolutionFor](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#config-conflictResolutionFor)
ID of the revision current revision contains resolution for

[type](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#config-type)
Transaction type.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRevisionTransaction](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#property-isRevisionTransaction)
Identifies an object as an instance of [RevisionTransaction](https://bryntum.com/docs/gantt/api/#Core/data/stm/RevisionTransaction) class, or subclass thereof.

[isRevisionTransaction](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#property-isRevisionTransaction-static)
Identifies an object as an instance of [RevisionTransaction](https://bryntum.com/docs/gantt/api/#Core/data/stm/RevisionTransaction) class, or subclass thereof.

[committed](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#property-committed)
Identifies if revision is temporary or not. Committed revisions get cleaned eventually, local revisions should be committed.

[conflictResolutionFor](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#property-conflictResolutionFor)
ID of the revision current revision contains resolution for

[type](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#property-type)
Transaction type.

## Functions

Functions are methods available for calling on the class

[from](https://bryntum.com/docs/gantt/api/Core/data/stm/RevisionTransaction#function-from-static)
Creates [RevisionTransaction](https://bryntum.com/docs/gantt/api/#Core/data/stm/RevisionTransaction) from [Transaction](https://bryntum.com/docs/gantt/api/#Core/data/stm/Transaction) with additional metadata utilized by the revisions feature
