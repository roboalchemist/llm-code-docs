# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/stm/Transaction.md

# [Transaction](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction)

STM transaction class holds a list of actions constituting a transaction.

A transaction can be undone and redone. Upon undo all the actions being held are undone in reverse order. Upon redo all the actions being held are redone in forward order.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[title](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#config-title)
Transaction title

## Properties

Properties are getters/setters or publicly accessible variables on this class

[inputGeneration](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#property-inputGeneration)
Last generation of the user input actions. Some transactions may contain conflict resolutions or just be a manual transaction, grouping several user actions and project calculations. This number represents the current number of user input stages. Used internally to count and group them.

[queue](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#property-queue)
Gets transaction's actions queue

[length](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#property-length)
Gets transaction's actions queue length

## Functions

Functions are methods available for calling on the class

[createTransactionWithOriginalInput](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#function-createTransactionWithOriginalInput-static)
Creates transaction with the lowest generation of actions

[addAction](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#function-addAction)
Adds an action to the transaction.

[undo](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#function-undo)
Undoes actions held

[redo](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#function-redo)
Redoes actions held

[mergeUpdateModelActions](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#function-mergeUpdateModelActions)
Merges all update actions into one per model, keeping the oldest and the newest values

[groupUserInput](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#function-groupUserInput)
Returns a map of actions grouped by `isUserInput` value

[getUserInput](https://bryntum.com/docs/gantt/api/Core/data/stm/Transaction#function-getUserInput)
Collects all updates from the transaction into a map with model as a key and changed data as value.
