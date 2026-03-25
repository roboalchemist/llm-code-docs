# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskCopyPaste.md

# [TaskCopyPaste](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskCopyPaste)

Allow using Ctrl/CMD + C/X and Ctrl/CMD + V to copy/cut and paste tasks. You can configure how a newly pasted record is named using [generateNewName](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskCopyPaste#config-generateNewName)

This feature is **enabled** by default

```
const gantt = new Gantt({
    features : {
        taskCopyPaste : true
    }
});
```

Dependencies between tasks in the current selected range will also be copied, but not dependencies with tasks outside of that range

Keyboard shortcuts
------------------

By default, this feature will react to Ctrl + C, Ctrl + X and Ctrl + V for standard clipboard actions. You can reconfigure the keys used to trigger these actions, see [keyMap](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskCopyPaste#config-keyMap) for more details.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskCopyPaste](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskCopyPaste#property-isTaskCopyPaste)
Identifies an object as an instance of [TaskCopyPaste](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskCopyPaste) class, or subclass thereof.

[isTaskCopyPaste](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskCopyPaste#property-isTaskCopyPaste-static)
Identifies an object as an instance of [TaskCopyPaste](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskCopyPaste) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[extractDependencies](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskCopyPaste#function-extractDependencies)
Extract dependencies from passed records. The result will include only deps via records and not include deps with foreign records.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[paste](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskCopyPaste#event-paste)
Fires on the owning Gantt after a paste action is performed.

[beforePaste](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskCopyPaste#event-beforePaste)
Fires on the owning Gantt before a paste action is performed, return `false` to prevent the action
