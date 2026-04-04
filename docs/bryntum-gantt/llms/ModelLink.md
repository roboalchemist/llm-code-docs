# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/mixin/ModelLink.md

# [ModelLink](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink)

Mixin that allows creating proxy records linked to an original record. See [link](https://bryntum.com/docs/gantt/api/#Core/data/mixin/ModelLink#function-link) for more information.

Not all UI features support linked records

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isModelLink](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#property-isModelLink)
Identifies an object as an instance of [ModelLink](https://bryntum.com/docs/gantt/api/#Core/data/mixin/ModelLink) class, or subclass thereof.

[isModelLink](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#property-isModelLink-static)
Identifies an object as an instance of [ModelLink](https://bryntum.com/docs/gantt/api/#Core/data/mixin/ModelLink) class, or subclass thereof.

[isLinked](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#property-isLinked)
Is this record linked to another record?

[hasLinks](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#property-hasLinks)
Are other records linked to this record?

[recordLinks](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#property-recordLinks)
Get links to this record.

[originalRecord](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#property-originalRecord)
Get the original record this record is linked to.

## Functions

Functions are methods available for calling on the class

[link](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#function-link)
Creates a proxy record (using native Proxy) linked to this record (the original). The proxy records shares most data with the original, except for its `id` (which is always generated), and ordering fields such as `parentIndex` and `parentId` etc.

Any change to the proxy record will be reflected on the original, and vice versa. A proxy record is not meant to be persisted, only the original record should be persisted. Thus, proxy records are not added to stores change tracking (added, modified and removed records).

Removing the original record removes all proxies.

Creating a proxy record allows a Store to seemingly contain the record multiple times, something that is otherwise not possible. It also allows a record to be used in both a tree store and in a flat store.

Not all UI features support linked records

[getStoreLinks](https://bryntum.com/docs/gantt/api/Core/data/mixin/ModelLink#function-getStoreLinks)
Returns all links of the record in the provided store.
