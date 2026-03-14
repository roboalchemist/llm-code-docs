# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/data/TaskStore.md

# [TaskStore](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore)

A class representing the tree of tasks in the Gantt project. An individual task is represented as an instance of the [TaskModel](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel) class. The store expects the data loaded to be hierarchical. Each parent node should contain its children in a property called 'children'.

```
const taskStore = new TaskStore({
    data : [
        {
            "id"           : 1000,
            "name"         : "Cool project",
            "percentDone"  : 50,
            "startDate"    : "2019-01-02",
            "expanded"     : true,
            "children"     : [
                {
                    "id"           : 1,
                    "name"         : "A leaf node",
                    "startDate"    : "2019-01-02",
                    "percentDone"  : 50,
                    "duration"     : 10,
                }
            ]
        }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[loadPriority](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#config-loadPriority)
CrudManager must load stores in the correct order. Lowest first.

[syncPriority](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#config-syncPriority)
CrudManager must sync stores in the correct order. Lowest first.

[wbsMode](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#config-wbsMode)
Set to `'auto'` to automatically update [wbsValue](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-wbsValue) as records in the store are manipulated (e.g., when the user performs drag-and-drop reordering).

In manual mode, the WBS value is initialized as the store loads and only altered implicitly by the [indent](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore#function-indent) and [outdent](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore#function-outdent) methods. The WBS values are otherwise updated only by an explicit call to [refreshWbs](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-refreshWbs).

This can also be a [WbsMode](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore#typedef-WbsMode) object that indicates what operations should automatically [refresh](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-refreshWbs) WBS values.

The operations that trigger WBS refresh can be enabled explicitly in this object, for example:

```
 wbsMode : {
     add : true,
     remove : true
 }
```

The above is an opt-in list that enable auto WBS refresh for node add and remove operations (these two operations are associated with dragging to reorder items). No other operation will trigger WBS refresh. At present, this leaves out only the `sort` operation, but if new auto-refreshing operations were added in future releases, those would also not be included.

Alternatively, this object can be an opt-out specification if all values are falsy:

```
 wbsMode : {
     sort : false
 }
```

The above two examples are (currently) equivalent in outcome. The choice between opt-in or opt-out form is a matter of convenience as well as future-proofing preference.

The value `'auto'` is equivalent to all properties being `true`. The value `'manual'` (the default) is equivalent to all properties being `false`.

[useOrderedTreeForWbs](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#config-useOrderedTreeForWbs)
Specifies which tree to use to calculate WBS. Ordered tree is unsortable and unfilterable, it always holds complete tree hierarchy. By default, it uses sortable and filterable tree.

[outdentIgnoringSiblings](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#config-outdentIgnoringSiblings)
Controls behavior of the outdent logic regarding siblings. By default, outdent will move child to be its parent's sibling and will move all previous siblings to the outdented node's children. Visually, node will remain in place just changing the level. When set to `true` only node with its subtree will be outdented, siblings will not change parent. Visually, node will be moved as last child of the new parent.

[forceWbsOrderForChanges](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#config-forceWbsOrderForChanges)
Always return changes in increasing WBS order.

[validatePreRenderData](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#config-validatePreRenderData)
Whether to validate the loaded tasks data by checking if it is suitable for pre-rendering. Pre-rendering is activated with the [delayCalculation](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-delayCalculation) config option, and it allows to improve the perceived loading performance - the tasks are rendered immediately on load, before the initial calculation completes.

For that to be possible, tasks need to have both start date and end date defined in the incoming data package. If task is not supposed to be rendered (so called "unscheduled" task), it should have the [unscheduled](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-unscheduled) field set to `true`.

Validation process will only be activated for the first data load and only if more than 1k tasks are loaded. Validation will check the initial 100 tasks in the dataset and if less than 10 of them don't have enough data for pre-rendering, validation will pass. Otherwise, validation will issue a `console.warn()` call with the text, suggesting to include pre-rendering data in the initial dataset.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskStore](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#property-isTaskStore)
Identifies an object as an instance of [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore) class, or subclass thereof.

[isTaskStore](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#property-isTaskStore-static)
Identifies an object as an instance of [TaskStore](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore) class, or subclass thereof.

[validatePreRenderData](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#property-validatePreRenderData)
Whether to validate the loaded tasks data by checking if it is suitable for pre-rendering. Pre-rendering is activated with the [delayCalculation](https://bryntum.com/docs/gantt/api/#Gantt/model/ProjectModel#config-delayCalculation) config option, and it allows to improve the perceived loading performance - the tasks are rendered immediately on load, before the initial calculation completes.

For that to be possible, tasks need to have both start date and end date defined in the incoming data package. If task is not supposed to be rendered (so called "unscheduled" task), it should have the [unscheduled](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-unscheduled) field set to `true`.

Validation process will only be activated for the first data load and only if more than 1k tasks are loaded. Validation will check the initial 100 tasks in the dataset and if less than 10 of them don't have enough data for pre-rendering, validation will pass. Otherwise, validation will issue a `console.warn()` call with the text, suggesting to include pre-rendering data in the initial dataset.

## Functions

Functions are methods available for calling on the class

[setBaseline](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#function-setBaseline)
For each task in this TaskStore, sets the data in the passed baseline index to the current state of the task.

[indent](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#function-indent)
Increase the indentation level of one or more tasks in the tree

[outdent](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#function-outdent)
Decrease the indentation level of one or more tasks in the tree

[refreshWbsForChildren](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#function-refreshWbsForChildren)
This method updates the WBS values due to changes in the indentation of a given set of child records.

[isDateRangeAvailable](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#function-isDateRangeAvailable)
Checks if a date range is allocated or not for a given resource. Will return `true` if a Resource has its `allowOverlap` value set to `true`.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeIndent](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#event-beforeIndent)
Fired before tasks in the tree are indented. Return `false` from a listener to prevent the indent.

[indent](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#event-indent)
Fired after tasks in the tree are indented

[beforeOutdent](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#event-beforeOutdent)
Fired before tasks in the tree are outdented. Return `false` from a listener to prevent the outdent.

[outdent](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#event-outdent)
Fired after tasks in the tree are outdented

## Typedefs

Typedefs are type definitions for the class

[WbsMode](https://bryntum.com/docs/gantt/api/Gantt/data/TaskStore#typedef-WbsMode)
An object that describes the actions that should trigger a [refreshWbs](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#function-refreshWbs) to update WBS values. Objects of this type are passed to [wbsMode](https://bryntum.com/docs/gantt/api/#Gantt/data/TaskStore#config-wbsMode) when the simpler values of `'auto'` or (the default) `'manual'` are not desired.

The value `'auto'` is equivalent to all properties of this object being `true`. The value `'manual'` is equivalent to all properties of this object being `false`.
