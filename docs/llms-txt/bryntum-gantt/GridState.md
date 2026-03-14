# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/mixin/GridState.md

# [GridState](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState)

Mixin for Grid that handles state. It serializes the following grid properties:

* rowHeight
* selectedCell
* selectedRecords
* columns (order, widths, visibility)
* store (sorters, groupers, filters)
* scroll position
* collapsed group records
* tree group levels

See [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) for more information on state.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[stateSettings](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#config-stateSettings)
The properties of this settings object controls how grid is restored from state data.

To disable state restoration for unconfigured columns:

```
const grid = new Grid({
    stateSettings : {
        restoreUnconfiguredColumns : false
    }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridState](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#property-isGridState)
Identifies an object as an instance of [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) class, or subclass thereof.

[isGridState](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#property-isGridState-static)
Identifies an object as an instance of [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) class, or subclass thereof.

[stateSettings](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#property-stateSettings)
The properties of this settings object controls how grid is restored from state data.

To disable state restoration for unconfigured columns:

```
const grid = new Grid({
    stateSettings : {
        restoreUnconfiguredColumns : false
    }
});
```

[state](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#property-state)
Gets or sets grid's state. Check out [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) mixin for details.

## Functions

Functions are methods available for calling on the class

[getState](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#function-getState)
Get grid's current state for serialization. State includes rowHeight, headerHeight, selectedCell, selectedRecordId, column states and store state etc.

[applyState](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#function-applyState)
Apply previously stored state.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeStateSave](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#event-beforeStateSave)
Fired before state is saved by the StateProvider. Allows editing the state object or preventing the operation.

[beforeStateApply](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#event-beforeStateApply)
Fired before state is applied to the source. Allows editing the state object or preventing the operation.

## Typedefs

Typedefs are type definitions for the class

[ColumnState](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#typedef-ColumnState)
An object which encapsulates a [column](https://bryntum.com/docs/gantt/api/#Grid/column/Column)'s saved state.

[SubGridState](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#typedef-SubGridState)
An object which encapsulates a [SubGrid](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid)'s saved state.

[GridStateInfo](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridState#typedef-GridStateInfo)
An object which encapsulates a [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid)'s saved state.
