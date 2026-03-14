# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/StoreRelation.md

# [StoreRelation](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation)

Mixin for Store that handles relations with other stores.

The relation is defined in a Model subclass, see Model's [relations](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-relations-static) property for more information.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStoreRelation](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#property-isStoreRelation)
Identifies an object as an instance of [StoreRelation](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreRelation) class, or subclass thereof.

[isStoreRelation](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#property-isStoreRelation-static)
Identifies an object as an instance of [StoreRelation](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreRelation) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[initRelations](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-initRelations)
Initialized relations, called from constructor

[initRelationCollection](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-initRelationCollection)
Called from other end of a relation when this store should hold a collection of related records.

[resetRelationCache](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-resetRelationCache)
Updates relationCache for all records.

[updateRecordRelationCache](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-updateRecordRelationCache)
Caches related records from related store on the local store.

[getRelationCollection](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-getRelationCollection)
Returns records the relation cache. Same result as if retrieving the collection on the dependent store, but without the need of accessing that store.

[getCollection](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-getCollection)
Returns records from a collection of related records. Not to be called directly, called from Model getter.

[setCollection](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-setCollection)
Sets a collection of related records. Will updated the related store and trigger events from it. Not to be called directly, called from Model setter.

[cacheRelatedRecord](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-cacheRelatedRecord)
Adds a record to relation cache, optionally removing it if already there.

[uncacheRelatedRecord](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-uncacheRelatedRecord)
Removes a record from relation cache, for a specific relation (specify relation name and id) or for all relations

[updateDependentStores](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-updateDependentStores)
Updates related stores when store is cleared, a record is removed or added.

[updateDependentRecordIds](https://bryntum.com/docs/gantt/api/Core/data/mixin/StoreRelation#function-updateDependentRecordIds)
Updates relation cache and foreign key value when a related objects id is changed.
