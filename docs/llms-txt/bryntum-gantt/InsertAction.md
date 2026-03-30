# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/stm/action/InsertAction.md

# [InsertAction](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction)

Action to record the fact of models inserting into a store.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[store](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#config-store)
Reference to a store that models have been inserted into.

[modelList](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#config-modelList)
List of models inserted into the store.

[insertIndex](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#config-insertIndex)
Index the models have been inserted at.

[context](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#config-context)
Models move context (if models has been moved), if any. Map this [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) instances as keys and their previous index as values

[silent](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#config-silent)
Flag showing if undo/redo should be done silently i.e. with events suppressed

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isInsertAction](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#property-isInsertAction)
Identifies an object as an instance of [InsertAction](https://bryntum.com/docs/gantt/api/#Core/data/stm/action/InsertAction) class, or subclass thereof.

[isInsertAction](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#property-isInsertAction-static)
Identifies an object as an instance of [InsertAction](https://bryntum.com/docs/gantt/api/#Core/data/stm/action/InsertAction) class, or subclass thereof.

[store](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#property-store)
Reference to a store that models have been inserted into.

[modelList](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#property-modelList)
List of models inserted into the store.

[insertIndex](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#property-insertIndex)
Index the models have been inserted at.

[context](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#property-context)
Models move context (if models has been moved), if any. Map this [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) instances as keys and their previous index as values

[silent](https://bryntum.com/docs/gantt/api/Core/data/stm/action/InsertAction#property-silent)
Flag showing if undo/redo should be done silently i.e. with events suppressed
